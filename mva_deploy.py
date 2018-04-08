def getToken():
        import os,commands,ast
        out=commands.getoutput('curl -k https://simplivity@15.112.66.141:443/api/oauth/token -d grant_type=password -d username=administrator@vsphere.local -d password=12ISO*help')
        out1=out.split('\n')
        #print out1[3]
        stringTodic = ast.literal_eval(out1[3])
        #print stringTodic
        #print stringTodic['access_token']
        return stringTodic['access_token']

def MVAdeploy():
        import commands
        input = '{"management_gateway":"15.112.64.1", "management_ip":"15.112.65.29", "management_mask": "255.255.248.0","svtcli_user_password":"12ISO*help", "network_mtu":"1500","network_name":"VM Network"}'
        cmd = 'curl -k -H  "Authorization: Bearer '+ token + '"' + ' -H "Content-Type: application/vnd.simplivity.v1.8+json"' + ' -d ' +'\''+ input +'\'' +'  -X POST https://simplivity@15.112.66.141:443/api/mvas'
        #print cmd
        output=commands.getoutput(cmd)
        return output


token = getToken()
print "Token : ",token
#print type(token)
deploy_status = MVAdeploy()
print deploy_status
