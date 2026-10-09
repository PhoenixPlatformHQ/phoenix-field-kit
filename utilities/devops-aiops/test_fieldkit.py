import unittest
import fieldkit as f

def pod(c):
    return {'kind':'Pod','metadata':{'name':'demo'},'spec':{'containers':[c]}}

class Tests(unittest.TestCase):
    def test_chain_order(self):
        out=f.jenkins({'jobs':[{'name':'deploy','needs':['test']},{'name':'test','needs':['build']},{'name':'build'}]})
        self.assertLess(out.index("stage('build')"),out.index("stage('test')"))
        self.assertLess(out.index("stage('test')"),out.index("stage('deploy')"))
        self.assertIn('wait: true, propagate: true',out)
        self.assertIn('agent none',out)
    def test_chain_cycle(self):
        with self.assertRaises(ValueError): f.jenkins({'jobs':[{'name':'a','needs':['b']},{'name':'b','needs':['a']}]})
    def test_chain_unknown(self):
        with self.assertRaises(ValueError): f.jenkins({'jobs':[{'name':'a','needs':['missing']}]})
    def test_chain_injection(self):
        with self.assertRaises(ValueError): f.jenkins({'jobs':[{'name':"evil');sh('x"}]})
    def test_chain_duplicates(self):
        with self.assertRaises(ValueError): f.jenkins({'jobs':[{'name':'a'},{'name':'a'}]})
    def test_resource_exceeds(self):
        r=f.resources([pod({'name':'app','resources':{'requests':{'cpu':'1500m','memory':'2Gi'},'limits':{'cpu':'1','memory':'512Mi'}}})])
        self.assertEqual(sum(x['level']=='FAIL' for x in r),2)
    def test_limit_default_warning(self):
        r=f.resources([pod({'name':'app','resources':{'limits':{'cpu':'1'}}})])
        self.assertTrue(any('may default' in x['message'] for x in r))
    def test_quantities(self):
        self.assertEqual(f.quantity('1000m'),f.quantity('1'))
        self.assertEqual(f.quantity('1024Mi'),f.quantity('1Gi'))
        self.assertEqual(f.quantity('1e3'),f.quantity('1k'))
    def test_invalid_quantity(self):
        r=f.resources([pod({'resources':{'requests':{'cpu':'banana'}}})])
        self.assertTrue(any(x['level']=='FAIL' for x in r))
    def test_probe_named_port(self):
        c={'ports':[{'name':'web','containerPort':8080}],'readinessProbe':{'httpGet':{'port':'http','path':'/'}}}
        self.assertTrue(any(x['level']=='FAIL' for x in f.probes([pod(c)])))
        c['readinessProbe']['httpGet']['port']='web'
        self.assertFalse(any(x['level']=='FAIL' for x in f.probes([pod(c)])))
    def test_probe_action_conflict(self):
        self.assertTrue(any(x['level']=='FAIL' for x in f.probes([pod({'livenessProbe':{'exec':{'command':['true']},'httpGet':{'port':80}}})])))
    def test_threshold(self):
        self.assertTrue(any(x['level']=='FAIL' for x in f.probes([pod({'livenessProbe':{'exec':{'command':['true']},'successThreshold':2}})])))
    def test_alert_not_rootcause(self):
        r=f.alerts([{'labels':{'alertname':'High','pod':'a'}},{'labels':{'alertname':'High','pod':'b'}}],['alertname'])
        self.assertEqual(r[0]['records'],2)
        self.assertEqual(r[0]['distinct_label_sets'],2)
        self.assertIn('not proof',r[0]['interpretation'])
    def test_redact(self):
        s=f.incident('password=abc\nAuthorization: Bearer xyz\nhttps://user:pass@example.test\ntoken="two words"')
        for secret in ('abc','xyz','user:pass','two words'): self.assertNotIn(secret,s)
        self.assertIn('untrusted',s)
    def test_redact_privatekey(self):
        self.assertNotIn('KEYDATA',f.incident('-----BEGIN RSA PRIVATE KEY-----\nKEYDATA\n-----END RSA PRIVATE KEY-----'))

if __name__=='__main__': unittest.main()
