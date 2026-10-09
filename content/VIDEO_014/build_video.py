import json, subprocess, textwrap, hashlib
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import soundfile as sf
from kokoro_onnx import Kokoro

p=Path(__file__).resolve().parent
models=p.parents[2]/'video011/models'
script=[
 'Your newer release deployed. Then the older pipeline put stale code back into production.',
 'This local fixture reproduces the race. Version two lands first, but version one finishes last.',
 'GitLab resource groups serialize deploys. The default unordered mode does not guarantee queue order.',
 'For continuous delivery, evaluate newest ready first, with idempotent deploys. Configure outdated job protection separately.',
 'Check manual jobs and rollback retries too. The free lab explains these limits.'
]
cards=[
 ('GREEN PIPELINE.', 'OLDER CODE IN PROD.', ['v2-new   deployed first', '', 'v1-old   finished last', '', 'production = v1-old'], 'Two deploys. One shared target.', 'PROBLEM / DEPLOY RACE'),
 ('REPRODUCE IT.', 'A real local fixture run.', [], 'Local Python output. Not GitLab Runner.', 'LOCAL FIXTURE / NO GITLAB RUNNER'),
 ('ONE DEPLOY AT A TIME.', 'Serialization is only one control.', ['deploy_production:', '  environment:', '    name: production', '  resource_group: production', '', '# Default process mode:', '# unordered'], 'A lock does not guarantee queue order.', 'GITLAB YAML / DOCS WALKTHROUGH'),
 ('CONTROL THE QUEUE.', 'Then reject outdated jobs.', ['1  resource_group: production', '', '2  process_mode via API:', '   newest_ready_first', '', '3  Prevent outdated', '   deployment jobs'], 'Deploy scripts must be idempotent.', 'CONFIGURATION / NOT EXECUTED'),
 ('CHECK THE LIMITS.', 'Manual deploys and rollback retries.', ['Job age uses job start time.', 'It is not commit chronology.', '', 'Review rollback retry policy.', '', 'Free fixture + YAML template', 'GitHub: phoenix-field-kit'], 'Copy the lab URL from the post text.', 'FREE LAB / EXPLAINED LIMITS')
]

run=subprocess.run(['python3','run_fixture.py'],cwd=p,text=True,capture_output=True,check=True)
(p/'fixture-output.txt').write_text(run.stdout)
# The displayed excerpt is copied from captured output, with explicit local provenance.
cards[1][2].extend(['$ python3 run_fixture.py','']+run.stdout.strip().splitlines()[:3]+['','fixture: PASS'])
fonts='/usr/share/fonts/truetype/dejavu'
def font(size,mono=False,bold=False):
 return ImageFont.truetype(f'{fonts}/DejaVuSans'+('Mono' if mono else '-Bold' if bold else '')+'.ttf',size)
def draw_wrapped(d,text,x,y,size,maxwidth=880,color='#EAF0F8',bold=False):
 words=text.split();lines=[];line=''
 for word in words:
  candidate=(line+' '+word).strip()
  if d.textlength(candidate,font=font(size,bold=bold))>maxwidth and line:
   lines.append(line);line=word
  else:line=candidate
 if line:lines.append(line)
 for line in lines:
  assert d.textlength(line,font=font(size,bold=bold))<=maxwidth,(text,line)
  d.text((x,y),line,font=font(size,bold=bold),fill=color);y+=int(size*1.3)
 return y

k=Kokoro(str(p.parents[1]/'kokoro-v1.0.int8.onnx'),str(models/'voices-v1.0.bin'))
scenes=[];subs=[];offset=0
def timestamp(t):
 ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
for i,(line,card) in enumerate(zip(script,cards)):
 wav=p/f'voice{i}.wav'
 if not wav.exists():
  a,rate=k.create(line,voice='af_heart',speed=1.0,lang='en-us');sf.write(wav,a,rate)
 else:a,rate=sf.read(wav)
 dur=len(a)/rate+0.30;scenes.append({'text':line,'duration':dur})
 im=Image.new('RGB',(1080,1920),'#0B1323');d=ImageDraw.Draw(im)
 d.rectangle((0,0,1080,18),fill='#60E5CC')
 d.text((82,155),'PHOENIX / DEVOPS FIELD NOTES',font=font(29,bold=True),fill='#60E5CC')
 title,subtitle,lines,footer,badge=card
 y=draw_wrapped(d,title,80,260,64,bold=True)
 draw_wrapped(d,subtitle,80,y+22,43,color='#AFC2D8')
 d.rounded_rectangle((75,560,1005,1120),radius=22,fill='#16273C')
 y=605
 for t in lines:
  assert d.textlength(t,font=font(34,mono=True))<850,(i,t)
  d.text((102,y),t,font=font(34,mono=True),fill='#FFA775' if 'v1-old' in t else '#EAF0F8');y+=57
 assert y<=1130,(i,y)
 draw_wrapped(d,footer,80,1190,39,color='#60E5CC')
 d.text((80,1340),badge,font=font(25,bold=True),fill='#AFC2D8')
 d.text((80,1400),f'{i+1:02} / 05',font=font(28,mono=True),fill='#AFC2D8')
 im.save(p/f'card{i}.png')
 words=line.split();chunks=[' '.join(words[j:j+6]) for j in range(0,len(words),6)]
 for j,chunk in enumerate(chunks):
  st=offset+j*(dur-.25)/len(chunks);en=offset+(j+1)*(dur-.25)/len(chunks)
  subs.append(f'{len(subs)+1}\n{timestamp(st)} --> {timestamp(en)}\n'+ '\n'.join(textwrap.wrap(chunk,28))+'\n')
 subprocess.run(['ffmpeg','-y','-v','error','-loop','1','-i',str(p/f'card{i}.png'),'-i',str(wav),'-af','apad','-t',str(dur),'-r','30','-c:v','libx264','-threads','2','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-b:a','128k',str(p/f'segment{i}.mp4')],check=True)
 offset+=dur
(p/'captions.srt').write_text('\n'.join(subs))
(p/'script.txt').write_text('\n'.join(script)+'\n')
(p/'timeline.json').write_text(json.dumps(scenes,indent=2))
(p/'concat.txt').write_text('\n'.join(f"file '{p/f'segment{i}.mp4'}'" for i in range(5)))
subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',str(p/'concat.txt'),'-c','copy',str(p/'joined.mp4')],check=True)
style='FontName=DejaVu Sans,FontSize=11,PrimaryColour=&H00FFFFFF,OutlineColour=&H00101924,BorderStyle=3,Outline=2,MarginL=32,MarginR=48,MarginV=48,Alignment=2'
out=p/'VIDEO_014_gitlab_deploy_race.mp4'
subprocess.run(['ffmpeg','-y','-v','error','-i',str(p/'joined.mp4'),'-vf',f"subtitles={p/'captions.srt'}:force_style='{style}'",'-c:v','libx264','-threads','2','-preset','veryfast','-crf','20','-c:a','copy','-movflags','+faststart',str(out)],check=True)
for i,s in enumerate(scenes):
 pos=sum(x['duration'] for x in scenes[:i])+s['duration']/2
 subprocess.run(['ffmpeg','-y','-v','error','-ss',str(pos),'-i',str(out),'-frames:v','1',str(p/f'preview{i}.png')],check=True)
contact=Image.new('RGB',(360*5,640))
for i in range(5):
 im=Image.open(p/f'preview{i}.png');im.thumbnail((360,640));contact.paste(im,(360*i,0))
contact.save(p/'contact.png')
print(json.dumps({'duration':offset,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'path':str(out)}))
