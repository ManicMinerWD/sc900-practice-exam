#!/usr/bin/env python3
import random
from collections import Counter
from _bal import balance

DOMAINS = {
  "C": "Security, compliance & identity concepts (12%)",
  "E": "Microsoft Entra (27%)",
  "S": "Security solutions (37%)",
  "M": "Compliance solutions (23%)"
}

# Each tuple is ONE line: (domain, question, o0, o1, o2, o3, correctIndex, explanation)
Q_raw = [
 # ===== C: CONCEPTS (12%) =====
("C","In Microsoft's shared responsibility model, the cloud provider is always responsible for:","The physical datacenter, network, and host infrastructure","All application code","All data classification","All user training",0,"Microsoft owns physical/host infrastructure; the customer owns data and usage."),
("C","The principle of least privilege means:","Users get only the access necessary for their role","Everyone is a global admin","Access is denied to all","Admins have no limits",0,"Least privilege limits access to what is needed."),
("C","Defense in depth means:","Using multiple layers of security controls","One strong firewall","No controls","A single password",0,"Layering controls so one failure does not breach security."),
("C","Zero Trust is best summarized as:","Never trust, always verify, regardless of location","Trust the internal network","Trust devices by default","No verification needed",0,"Zero Trust assumes no implicit trust."),
("C","Confidentiality, integrity, and availability (CIA) refer to:","The core goals of information security","A Microsoft product","A compliance law","A pricing tier",0,"CIA is the foundational security triad."),
("C","Encryption is used primarily to protect:","Data confidentiality in transit and at rest","Application speed","User morale","Network cables",0,"Encryption protects data confidentiality."),
("C","Authentication is:","Verifying the identity of a user or device","Granting access to a resource","Deleting a user","Buying a license",0,"Authentication proves identity."),
("C","Authorization is:","Determining what an authenticated user is allowed to do","Proving who you are","Encrypting data","Creating a password",0,"Authorization governs permissions after authentication."),
("C","Identity is considered the primary security perimeter because:","Most attacks target credentials, not the network edge","Networks are unbreakable","Devices are trusted","Passwords are optional",0,"Identity is the modern perimeter."),
("C","A directory service like Active Directory is used to:","Store and manage identities and their access","Host websites","Store files only","Run databases",0,"Directory services manage identities."),
("C","Federation allows:","Users in one identity provider to access another via trust","Passwords to be removed","Devices to be trusted","Networks to merge",0,"Federation enables cross-identity-provider access."),
("C","The shared responsibility model says the customer is responsible for:","Their data, identities, and how they configure cloud services","The datacenter power","The hypervisor","The physical rack",0,"Customer owns data, identities, and configuration."),
("C","Encryption at rest protects data:","Stored on disk or in a database","While traveling over the network","In memory only","On paper",0,"At rest = stored data."),
("C","Encryption in transit protects data:","While moving across a network","Stored on disk","Printed","In a drawer",0,"In transit = moving across networks."),
("C","A security baseline is:","A standard set of secure configurations","A random setting","A license","A report",0,"Baselines standardize secure config."),
("C","The difference between a threat and a vulnerability is:","A threat exploits a vulnerability (the weakness)","They are the same","A vulnerability attacks","A threat is a weakness",0,"Threat exploits; vulnerability is the weakness."),
("C","Compliance means:","Meeting legal, regulatory, and policy requirements","Ignoring rules","Maximizing cost","Avoiding audits",0,"Compliance = meeting requirements."),
("C","Privacy principles include:","Transparency, purpose limitation, and data minimization","Selling all data","Hiding breaches","No notices",0,"Privacy principles protect personal data."),

 # ===== E: MICROSOFT ENTRA (27%) =====
("E","Microsoft Entra ID (Azure AD) is primarily:","A cloud-based identity and access management service","A file storage service","A database engine","A firewall",0,"Entra ID is the cloud identity service."),
("E","Authentication in Entra ID is provided by:","Microsoft Entra ID verifying user credentials","A firewall","DNS","A switch",0,"Entra ID authenticates users."),
("E","Multi-factor authentication (MFA) adds security by:","Requiring two or more verification methods","Using one long password","Removing passwords","Disabling accounts",0,"MFA requires multiple factors."),
("E","A user principal name (UPN) in Entra ID looks like:","user@domain.com","A random GUID only","A phone number","An IP address",0,"UPN is the user@example.com style identity."),
("E","Entra ID Connect (formerly AD Connect) is used to:","Synchronize on-premises Active Directory with Entra ID","Delete accounts","Host apps","Encrypt disks",0,"Connect syncs on-prem AD to the cloud."),
("E","Single sign-on (SSO) allows a user to:","Authenticate once and access multiple apps","Use a different password per app","Avoid authentication","Share credentials",0,"SSO = one login, many apps."),
("E","Conditional Access policies evaluate:","Sign-in risk, device, location, and app to grant or block access","Only the username","Only the password","Only the time",0,"Conditional Access uses signals to decide access."),
("E","A Conditional Access policy can require:","A compliant device or MFA before granting access","No checks","Always deny","Public Wi-Fi only",0,"Policies can require compliance/MFA."),
("E","Microsoft Entra ID P1/P2 adds capabilities such as:","Conditional Access and identity protection","Only basic sign-in","No extra features","File storage",0,"P1/P2 add advanced features."),
("E","Identity Protection can detect:","Risky sign-ins and compromised users using signals","Only password changes","Hardware faults","Network speed",0,"Identity Protection scores risk."),
("E","A guest user in Entra ID is:","An external user from another organization","An internal employee","A deleted account","A service account",0,"Guests are external collaborators."),
("E","Entra ID Governance helps with:","Access reviews, entitlement management, and lifecycle","Only passwords","Only licensing","Only reports",0,"Governance manages access lifecycle."),
("E","An access review in Entra ID is used to:","Periodically confirm a user still needs access","Create users","Delete data","Buy licenses",0,"Reviews validate continued need."),
("E","Privileged Identity Management (PIM) is used to:","Provide just-in-time, time-limited admin access","Give permanent global admin","Remove MFA","Delete roles",0,"PIM grants eligible, time-bound admin."),
("E","The difference between authentication and authorization in Entra is:","Authentication proves who you are; authorization decides what you can do","They are the same","Authorization proves identity","Authentication grants access",0,"AuthN vs AuthZ distinction."),
("E","A service principal in Entra ID represents:","An application or service's identity","A human user","A group","A device",0,"Service principals are app identities."),
("E","Entra ID groups are used to:","Assign access to many users at once","Store files","Encrypt data","Host apps",0,"Groups simplify access assignment."),
("E","Role-based access control (RBAC) assigns permissions based on:","A user's role rather than individual identity","Random choice","Device type","Location only",0,"RBAC = role-based permissions."),
("E","Passwordless authentication options include:","Windows Hello, FIDO2 keys, and phone sign-in","Only sticky notes","Only SMS","Only paper",0,"Passwordless uses biometrics/keys."),
("E","Self-service password reset (SSPR) lets users:","Reset their own password securely without a ticket","Share passwords","Disable MFA","Delete accounts",0,"SSPR reduces help-desk load."),
("E","A tenant in Entra ID is:","A dedicated instance of Entra ID for an organization","A server","A database","A network",0,"A tenant is the org's directory instance."),
("E","Entra ID supports federation with:","External identity providers via standards like SAML","No external providers","Only Facebook","Only email",0,"Federation uses SAML/OIDC etc."),
("E","The purpose of a Conditional Access 'report-only' mode is to:","Evaluate policies without enforcing them","Block all access","Disable MFA","Delete users",0,"Report-only tests impact safely."),
("E","Entra ID Protection risk levels are:","Low, medium, high, and risk detections","Only 'ok'","Only colors","Only numbers",0,"Risk levels guide response."),
("E","An application proxy in Entra ID is used to:","Securely publish on-prem apps to remote users","Host websites","Store data","Encrypt disks",0,"App Proxy publishes internal apps safely."),
("E","Entra ID Verifiable Credentials let users:","Present proof of attributes without revealing everything","Share passwords","Delete accounts","Buy licenses",0,"Verifiable credentials prove claims."),
("E","The default user permission in Entra ID can allow:","Users to register apps or read directory unless restricted","Always full admin","Never any access","Only printing",0,"Defaults matter for least privilege."),
("E","Identity Protection can automatically:","Trigger risk-based MFA or block sign-in","Do nothing","Only email","Delete users",0,"Risk-based remediation."),
("E","A managed identity in Azure is used to:","Let Azure resources authenticate to services without secrets","Log in as a human","Store files","Host apps",0,"Managed identities remove secrets."),

 # ===== S: SECURITY SOLUTIONS (37%) =====
("S","Microsoft Defender for Cloud is used to:","Assess and improve cloud security posture and protect workloads","Host websites","Store files","Send email",0,"Defender for Cloud = CSPM + workload protection."),
("S","Microsoft Defender for Endpoint protects:","Devices (servers, desktops, mobiles) from threats","Only networks","Only databases","Only emails",0,"Defender for Endpoint is device EDR."),
("S","Microsoft Sentinel is:","A cloud-native SIEM and SOAR for threat detection and response","A firewall","A database","A switch",0,"Sentinel = SIEM/SOAR."),
("S","A SIEM collects and analyzes:","Security logs and events for detection","Only emails","Only files","Only passwords",0,"SIEM aggregates security data."),
("S","Microsoft Defender for Identity monitors:","On-premises AD for advanced attacks","Only cloud apps","Only mobile","Only email",0,"Defender for Identity watches AD."),
("S","Azure DDoS Protection defends against:","Distributed denial-of-service attacks","Phishing","Malware only","Insider threat",0,"DDoS protection = volumetric attacks."),
("S","Azure Firewall is a:","Managed, cloud-based network firewall","A physical router","A database","A switch",0,"Azure Firewall filters traffic."),
("S","Network Security Groups (NSGs) filter:","Traffic to and from Azure resources by rule","Only users","Only files","Only emails",0,"NSGs are traffic filters."),
("S","Microsoft Defender for Office 365 protects:","Email and collaboration from phishing and malware","Only servers","Only databases","Only networks",0,"Defender for O365 guards email/collaboration."),
("S","Microsoft Defender for Cloud Apps is a:","Cloud Access Security Broker (CASB) for SaaS visibility","A firewall","A database","A switch",0,"Defender for Cloud Apps = CASB."),
("S","Azure Key Vault is used to store:","Secrets, keys, and certificates securely","Virtual machines","Websites","Databases",0,"Key Vault holds secrets/keys/certs."),
("S","Microsoft Purview (in security context) relates to:","Data governance, classification, and information protection","A firewall","A database","A switch",0,"Purview governs data."),
("S","Microsoft Intune is used for:","Mobile device and app management (MDM/MAM)","Hosting websites","Storing files","Encrypting disks only",0,"Intune = endpoint management."),
("S","Endpoint protection via Intune can:","Enforce device compliance and app protection","Only send email","Only store files","Only print",0,"Intune enforces compliance."),
("S","Microsoft Defender Vulnerability Management helps by:","Discovering and prioritizing software weaknesses","Only patching automatically","Ignoring risk","Deleting apps",0,"VM discovers and prioritizes flaws."),
("S","Azure SQL Database security features include:","Auditing, threat detection, and row-level security","Only backups","Only indexing","Only pricing",0,"SQL offers auditing and threat detection."),
("S","Microsoft Defender for Servers protects:","Windows and Linux servers with EDR and recommendations","Only desktops","Only mobile","Only email",0,"Defender for Servers = server EDR."),
("S","A secure score in Defender for Cloud indicates:","How well your environment follows security best practices","Your license level","Your bill","Your region",0,"Secure score measures posture."),
("S","Just-in-time VM access reduces risk by:","Opening management ports only when needed","Always opening ports","Closing all ports forever","Deleting VMs",0,"JIT limits exposure of management ports."),
("S","Microsoft Entra ID Protection is part of:","Identity security, detecting risky sign-ins","Network security","A firewall","A database",0,"Identity Protection is identity security."),
("S","Adaptive network hardening in Defender for Cloud:","Recommends tighter NSG rules based on traffic","Randomly opens ports","Deletes firewalls","Ignores traffic",0,"Adaptive hardening tightens rules."),
("S","Microsoft 365 Defender is:","An XDR that correlates signals across endpoints, email, identity, and apps","A single firewall","A database","A switch",0,"M365 Defender = extended detection."),
("S","Threat intelligence in security tools provides:","Known indicators of compromise to aid detection","Only user names","Only passwords","Only licenses",0,"TI uses IoCs."),
("S","Azure Bastion provides:","Secure RDP/SSH to VMs without exposing public IPs","A database","A firewall","A switch",0,"Bastion = secure VM access."),
("S","Microsoft Defender for Containers protects:","Container images and Kubernetes workloads","Only VMs","Only databases","Only email",0,"Defender for Containers = K8s/images."),
("S","Data loss prevention (DLP) in Microsoft 365 aims to:","Prevent sharing of sensitive content","Delete all data","Encrypt only passwords","Ignore data",0,"DLP controls sensitive data movement."),
("S","Information protection (labels) in Microsoft 365:","Classify and protect content with sensitivity labels","Only delete files","Only store files","Only email",0,"Sensitivity labels classify/protect."),
("S","Azure Policy can enforce:","Allowed regions, resource types, and configurations","Only passwords","Only licenses","Only reports",0,"Azure Policy governs resources."),
("S","Microsoft Defender for DevOps secures:","Code repositories and pipelines","Only VMs","Only databases","Only email",0,"Defender for DevOps = pipeline security."),
("S","A Web Application Firewall (WAF) protects:","Web apps from common attacks like SQL injection","Only databases","Only email","Only files",0,"WAF guards web apps."),
("S","Microsoft Security Copilot is used to:","Augment security analysts with AI-assisted investigation","Replace all analysts","Delete logs","Host websites",0,"Security Copilot = AI assistance."),
("S","Azure Private Link provides:","Private connectivity to services without public internet","Public IPs","A firewall","A database",0,"Private Link = private access."),
("S","Microsoft Defender for Storage protects:","Blob and file storage from malware and anomalies","Only VMs","Only email","Only networks",0,"Defender for Storage = storage threats."),
("S","The difference between MDM and MAM is:","MDM manages the whole device; MAM manages only the apps/data","They are identical","MAM manages hardware","MDM manages apps only",0,"MDM=device, MAM=apps/data."),
("S","Azure Sentinel playbooks (SOAR) are used to:","Automate response actions to incidents","Only store logs","Only send email","Only delete data",0,"Playbooks automate response."),
("S","Threat detection for email is primarily provided by:","Microsoft Defender for Office 365","Azure Firewall","A switch","A database",0,"Defender for O365 = email security."),
("S","Azure DDoS Network Protection safeguards:","Virtual networks from large-scale attacks","Only emails","Only files","Only databases",0,"DDoS Network Protection = vNet scale."),
("S","Microsoft Defender for Identity uses:","Lightweight sensors on AD to detect lateral movement","Only cloud logs","Only mobile","Only email",0,"Defender for Identity watches AD."),
("S","Encryption keys in Azure are managed via:","Azure Key Vault and customer-managed keys","Sticky notes","Spreadsheets","Email",0,"Key Vault manages keys."),
("S","Azure Security Benchmark provides:","Microsoft's recommended security configuration baselines","A firewall","A database","A switch",0,"Benchmark = config guidance."),
("S","A CASB like Defender for Cloud Apps helps discover:","Shadow IT and SaaS usage outside IT control","Only VMs","Only databases","Only email",0,"CASB finds shadow IT."),
("S","Microsoft Intune app protection policies can:","Prevent copy/paste from managed to unmanaged apps","Only wipe devices","Only email","Only store files",0,"App protection limits data movement."),
("S","Azure Firewall Premium adds:","TLS inspection and IDPS beyond standard firewall","Nothing extra","Only DNS","Only routing",0,"Premium adds inspection/IDPS."),
("S","Microsoft Defender for Endpoint's EDR capability:","Investigates and responds to advanced attacks on devices","Only scans files","Only emails","Only networks",0,"EDR = endpoint detection/response."),

 # ===== M: COMPLIANCE SOLUTIONS (23%) =====
("M","Microsoft Purview is used for:","Data governance, compliance, and risk management","Hosting websites","Storing virtual machines","Encrypting disks",0,"Purview = data governance/compliance."),
("M","Sensitivity labels in Microsoft 365:","Classify and protect content and apply policies","Only delete files","Only store files","Only email",0,"Labels classify and protect."),
("M","Data loss prevention (DLP) policies can:","Detect and block sensitive data leaving the org","Only encrypt files","Only store data","Only email",0,"DLP blocks sensitive data egress."),
("M","Retention policies in Microsoft 365:","Keep or delete content per legal/business rules","Only back up","Only encrypt","Only share",0,"Retention governs keep/delete."),
("M","The Microsoft Service Trust Portal provides:","Compliance reports, audits, and trust documents","A firewall","A database","A switch",0,"STP = compliance/audit docs."),
("M","The Microsoft Purview Compliance Manager helps by:","Tracking compliance activities and providing an actionable score","Only storing files","Only email","Only licensing",0,"Compliance Manager scores readiness."),
("M","A communication compliance policy can:","Detect inappropriate or risky communications","Only encrypt mail","Only delete mail","Only store mail",0,"Communication compliance monitors messages."),
("M","Insider risk management helps detect:","Potential malicious or accidental insider data leaks","Only external attacks","Only malware","Only phishing",0,"Insider risk = internal threats."),
("M","eDiscovery in Microsoft 365 is used to:","Find and preserve relevant data for legal cases","Only back up","Only encrypt","Only delete",0,"eDiscovery supports legal holds."),
("M","Audit logs in Microsoft 365 record:","User and admin activities for investigation","Only passwords","Only licenses","Only regions",0,"Audit logs trace activity."),
("M","Data classification helps by:","Identifying and labeling sensitive information","Deleting data","Encrypting only passwords","Ignoring data",0,"Classification finds sensitive data."),
("M","The difference between retention and deletion is:","Retention keeps content for a period; deletion removes it","They are the same","Deletion keeps content","Retention deletes immediately",0,"Retention vs deletion distinction."),
("M","Microsoft's privacy principles include:","Accountability, transparency, and data minimization","Selling all data","Hiding breaches","No notices",0,"Privacy principles protect users."),
("M","Compliance Manager's improvement actions help you:","Close gaps against a compliance framework","Only store files","Only email","Only license",0,"Improvement actions remediate gaps."),
("M","A data subject request (DSR) relates to:","GDPR-style requests to access or delete personal data","A firewall","A database","A switch",0,"DSR = privacy data requests."),
("M","Microsoft Purview Information Barriers prevent:","Communication between conflicting groups (e.g., trading vs research)","Only email storage","Only file storage","Only licensing",0,"Info Barriers restrict communication."),
("M","The Service Trust Portal includes documents such as:","ISO, SOC, and FedRAMP audit reports","Only marketing","Only pricing","Only manuals",0,"STP holds audit reports."),
("M","Records management in Microsoft 365:","Declares and retains content as records per policy","Only deletes","Only encrypts","Only shares",0,"Records management = declared records."),
("M","Data residency refers to:","Where an organization's data is physically stored","The color of the data","The price of data","The owner's name",0,"Residency = storage location."),
("M","Adaptive protection in Purview uses:","Risk signals to dynamically adjust DLP/enforcement","Only static rules","Only deletion","Only encryption",0,"Adaptive protection responds to risk."),
("M","Microsoft Entra ID's role in compliance includes:","Access governance and audit of who accessed what","Only hosting","Only storage","Only pricing",0,"Entra supports access compliance."),
("M","A compliance score in Compliance Manager reflects:","How well controls are implemented versus a baseline","Your license","Your bill","Your region",0,"Score = control implementation."),
("M","Data lifecycle management handles:","Retention, deletion, and archival of data over time","Only creation","Only encryption","Only sharing",0,"DLM = retain/delete/archival."),
("M","Microsoft Purview trainable classifiers can:","Identify sensitive content by pattern, not just keywords","Only delete","Only encrypt","Only store",0,"Classifiers detect by learning."),
("M","Legal hold preserves data by:","Preventing deletion during a case","Immediately deleting","Encrypting only","Sharing only",0,"Legal hold preserves evidence."),
("M","The difference between compliance and security is:","Compliance meets rules; security protects from threats","They are the same","Security is optional","Compliance is optional",0,"Compliance=rules; security=threats."),
("M","Microsoft 365 audit retention can be configured to:","Keep logs for a defined period for investigations","Delete instantly","Ignore logs","Only email",0,"Audit retention supports investigations."),
("M","A DLP policy tip notifies the user when:","They are about to share sensitive content","Nothing happens","Only admins see it","Only on delete",0,"Policy tips warn users."),
("M","Microsoft's approach to responsible AI relates to compliance via:","Transparency and accountability in automated decisions","Ignoring AI","Hiding models","No policy",0,"Responsible AI = accountable automation."),
("M","The Microsoft Privacy Statement explains:","How Microsoft handles personal data","Only pricing","Only marketing","Only manuals",0,"Privacy statement = data handling."),
("M","Tenant isolation in Microsoft 365 means:","Customer data is logically separated between tenants","All data is shared","No separation","Only encrypted",0,"Isolation separates tenant data."),
("M","A compliance framework like ISO 27001 is:","A recognized standard your controls can be assessed against","A firewall","A database","A switch",0,"Frameworks are assessment standards."),
("M","Microsoft Purview eDiscovery (Premium) supports:","Custodian management and review sets","Only backup","Only encryption","Only deletion",0,"Premium eDiscovery = legal tooling."),
("M","Sensitivity label encryption can:","Protect content so only authorized users can open it","Delete the file","Share with everyone","Ignore permissions",0,"Label encryption restricts access."),
("M","The Service Trust Portal is accessed to:","Review Microsoft's compliance and audit artifacts","Configure firewalls","Buy licenses","Host apps",0,"STP = review compliance artifacts."),
 ("E","Entra ID B2B is used to collaborate with:","External guest users from partner organizations","Internal employees only","Devices only","Service accounts only",0,"B2B = external guest collaboration."),
("E","Entra ID B2C is designed for:","Customer-facing app identities, not internal staff","Internal employees only","Servers only","Databases only",0,"B2C = customer identities."),
("E","Microsoft Entra Domain Services provides:","Managed Active Directory Domain Services in the cloud","A firewall","A database","A switch",0,"Entra Domain Services = managed AD DS."),
("E","Sign-in risk vs user risk in Identity Protection:","Sign-in risk is the current session; user risk is the identity compromised","They are identical","User risk is the session","Sign-in risk is the identity",0,"Two distinct risk types."),
("E","Entra ID Free supports:","Cloud SSO and basic directory, but not Conditional Access","Full PIM","Full Identity Protection","CASB",0,"Free tier lacks advanced controls."),
("E","Entitlement management access packages bundle:","Groups, apps, and SharePoint sites with access policies","Only passwords","Only licenses","Only reports",0,"Access packages bundle resources."),
("E","The My Apps portal lets users:","Launch and manage their assigned applications","Configure firewalls","Manage databases","Host websites",0,"My Apps = app launcher."),
("E","Entra ID Connect cloud sync differs from Connect by:","Using a lightweight agent and cloud-driven rules","Deleting accounts","Hosting apps","Encrypting disks",0,"Cloud sync = lightweight agent."),
("E","A Terms of Use in Entra ID is used to:","Present legal/consent text before granting access","Only store files","Only email","Only license",0,"ToU captures consent."),
("E","Entra ID acts as the authentication provider for:","Azure, Microsoft 365, and many SaaS apps","Only one app","Only databases","Only networks",0,"Entra is the broad IdP."),
("E","Identity Secure Score measures:","How well identity protections are configured","Your license","Your bill","Your region",0,"Secure Score = identity posture."),
("E","Microsoft Entra ID Governance lifecycle workflows can:","Automate provisioning and deprovisioning of access","Only store files","Only email","Only license",0,"Lifecycle workflows automate access."),

("S","Security alerts in Defender for Cloud appear for:","Detected threats and misconfigurations","Only emails","Only licenses","Only regions",0,"Alerts flag threats/misconfig."),
("S","Microsoft Defender for Business targets:","Small and medium businesses with endpoint protection","Only enterprises","Only governments","Only schools",0,"Defender for Business = SMB."),
("S","Microsoft 365 E5 Security includes capabilities such as:","Defender, Entra ID P2, and Purview protections","Only email","Only storage","Only a firewall",0,"E5 Security bundles protections."),
("S","Conditional Access session controls can:","Enforce app-enforced restrictions like limited download","Only block login","Only email","Only license",0,"Session controls limit in-session actions."),
("S","Microsoft Defender for Containers can scan:","Container registries for vulnerabilities","Only VMs","Only email","Only networks",0,"Container scanning = registry images."),
("S","STRIDE is a model used for:","Threat modeling to categorize software threats","Pricing","Licensing","Networking",0,"STRIDE = threat modeling."),
("S","An Azure Policy initiative is:","A set of policies assigned together","A single firewall","A database","A switch",0,"Initiatives group policies."),
("S","Microsoft Defender for IoT protects:","Operational technology and IoT devices","Only laptops","Only email","Only databases",0,"Defender for IoT = OT/ IoT."),
("S","Secure score recommendations suggest:","Concrete steps to improve security posture","Only pricing","Only licensing","Only regions",0,"Recommendations improve posture."),
("S","Azure Firewall Manager centralizes:","Policy and configuration across firewall deployments","Only databases","Only email","Only storage",0,"Firewall Manager = central policy."),
("S","Microsoft Defender for Cloud's regulatory compliance dashboard maps:","Your controls to compliance standards","Only pricing","Only licensing","Only regions",0,"Dashboard maps to standards."),

("M","Microsoft Purview Data Map provides:","A catalog of data assets and their lineage","A firewall","A database engine","A switch",0,"Data Map = catalog/lineage."),
]

Q_raw = balance(Q_raw)

# safety net: trim/pad to exactly 150
print("raw count:", len(Q_raw), "domains:", dict(Counter(q[0] for q in Q_raw)))
while len(Q_raw) > 150:
    for i in range(len(Q_raw)-1, -1, -1):
        if Q_raw[i][0] == "C":
            del Q_raw[i]; break
while len(Q_raw) < 150:
    Q_raw.append(("C","The shared responsibility model means:","Microsoft and the customer each own specific security duties","Only Microsoft is responsible","Only the customer is responsible","No one is responsible",0,"Responsibilities are split by layer."))

# balance correct positions A/B/C/D
random.seed(2026)
targets = [0,1,2,3] * (150//4)
while len(targets) < 150:
    targets.append(len(targets) % 4)
random.shuffle(targets)
Q = []
for i,(dom,q,o0,o1,o2,o3,ai,exp) in enumerate(Q_raw):
    opts=[o0,o1,o2,o3]
    t = targets[i]
    shift = (ai - t) % len(opts)
    rotd = opts[shift:] + opts[:shift]
    Q.append({"d":dom,"q":q,"o":rotd,"a":t,"x":exp})
dist = [0,0,0,0]
for q in Q: dist[q["a"]] += 1
for i,(dom,q,o0,o1,o2,o3,ai,exp) in enumerate(Q_raw):
    assert Q[i]["o"][Q[i]["a"]] == [o0,o1,o2,o3][ai], "integrity fail at %d" % i
print("final:", len(Q), "domains:", dict(Counter(q["d"] for q in Q)), "dist:", dist, "INTEGRITY OK")

# ---------------- HTML builder (fixed: reveal only on click) ----------------
def jss(s): return s.replace("\\","\\\\").replace('"','\\"').replace("\n","\\n")
STUDYGUIDE = {
  "C":["Know CIA, shared responsibility, zero trust, and identity as the perimeter.","Encryption, least privilege, defense in depth.","AuthN vs AuthZ; threats vs vulnerabilities."],
  "E":["Entra ID is the cloud identity plane: SSO, MFA, Conditional Access.","PIM for just-in-time admin; Identity Protection for risk.","Governance: access reviews, entitlement management."],
  "S":["Defender family spans endpoints, cloud, identity, email, SaaS (CASB).","Sentinel = SIEM/SOAR; Intune = MDM/MAM; Key Vault = secrets.","DLP, sensitivity labels, and WAF protect data and apps."],
  "M":["Purview governs data: classification, labels, retention, DLP.","Compliance Manager scores readiness; STP holds audit reports.","eDiscovery, audit logs, and insider risk support legal/compliance."]
}
Q_json = "[\n" + ",\n".join(
    '  {d:"%s",q:"%s",o:["%s","%s","%s","%s"],a:%d,x:"%s"}' % (
        q["d"], jss(q["q"]), jss(q["o"][0]), jss(q["o"][1]), jss(q["o"][2]), jss(q["o"][3]), q["a"], jss(q["x"])
    ) for q in Q
) + "\n]"
DOM_json = "{" + ",".join('"%s":"%s"' % (k, jss(v)) for k,v in DOMAINS.items()) + "}"
SG_json = "{" + ",".join('"%s":["%s"]' % (k, '","'.join(jss(s) for s in v)) for k,v in STUDYGUIDE.items()) + "}"

html = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SC-900 Practice Exam</title>
<style>
:root{--bg:#0b1020;--card:#151c2e;--fg:#e8ecf5;--muted:#9aa6c0;--accent:#6ea8fe;--good:#3ecf8e;--bad:#ff6b6b;--line:#26304a}
*{box-sizing:border-box}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;background:var(--bg);color:var(--fg);line-height:1.5}
header{padding:18px 22px;border-bottom:1px solid var(--line);display:flex;flex-wrap:wrap;align-items:center;gap:12px}
header h1{font-size:1.15rem;margin:0;font-weight:650}
.pill{background:#1d2742;border:1px solid var(--line);color:var(--muted);padding:3px 10px;border-radius:999px;font-size:.78rem}
.spacer{flex:1}
button{cursor:pointer;border:1px solid var(--line);background:#1b2540;color:var(--fg);padding:9px 16px;border-radius:8px;font-size:.92rem;transition:.15s}
button:hover{border-color:var(--accent)}
button.primary{background:var(--accent);color:#08101f;border-color:var(--accent);font-weight:600}
button:disabled{opacity:.45;cursor:not-allowed}
.toolbar{display:flex;flex-wrap:wrap;gap:10px;align-items:center;padding:14px 22px;border-bottom:1px solid var(--line)}
.modebtns button.active{background:var(--accent);color:#08101f;border-color:var(--accent)}
#timer{font-variant-numeric:tabular-nums;color:var(--muted);font-size:.9rem}
main{padding:22px;max-width:820px;margin:0 auto}
#quiz{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:22px}
.qhead{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;gap:10px}
.qdomain{font-size:.74rem;color:var(--accent);text-transform:uppercase;letter-spacing:.04em}
.qno{font-size:.8rem;color:var(--muted)}
.question{font-size:1.05rem;margin-bottom:18px;font-weight:550}
.options{display:flex;flex-direction:column;gap:10px}
.opt{display:flex;align-items:center;gap:12px;padding:12px 14px;border:1px solid var(--line);border-radius:9px;background:#121a2e;transition:.12s}
.opt:hover{border-color:var(--accent)}
.opt input{accent-color:var(--accent);width:17px;height:17px}
.opt.correct{border-color:var(--good);background:rgba(62,207,142,.12)}
.opt.wrong{border-color:var(--bad);background:rgba(255,107,107,.12)}
.opt.dim{opacity:.55}
.exp{margin-top:16px;padding:13px 15px;border-left:3px solid var(--accent);background:#101a30;border-radius:6px;font-size:.92rem;color:#cdd6ea}
.qnav{display:flex;justify-content:space-between;align-items:center;margin-top:20px;gap:10px}
.qcontrols{display:flex;gap:10px}
.score{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:24px;margin-top:22px;display:none}
.score h2{margin-top:0}
.big{font-size:2.4rem;font-weight:700;margin:6px 0}
.legend{font-size:.85rem;color:var(--muted);margin-top:8px}
#pie{display:flex;flex-direction:column;align-items:center;margin:16px 0}
#pie svg{max-width:240px}
.pielabel{font-size:.8rem;color:var(--muted);text-align:center;margin-top:4px}
.break{display:flex;flex-direction:column;gap:9px;margin-top:16px}
.brow{display:flex;justify-content:space-between;gap:12px;font-size:.9rem;padding:9px 12px;background:#121a2e;border:1px solid var(--line);border-radius:8px}
.brow .pct{font-weight:650}
.rec{margin-top:18px;padding:16px;border:1px solid var(--good);border-radius:10px;background:rgba(62,207,142,.08);display:none}
.rec h3{margin:0 0 8px;font-size:1rem}
.rec ul{margin:6px 0 0;padding-left:20px;font-size:.9rem;color:#cdd6ea}
#review{margin-top:20px}
.review-item{padding:13px 15px;border:1px solid var(--line);border-radius:9px;margin-bottom:10px;background:#121a2e}
.review-item .rq{font-weight:550;margin-bottom:6px}
.review-item .rr{font-size:.85rem}
.review-item .ok{color:var(--good)}
.review-item .no{color:var(--bad)}
.review-item .rx{font-size:.84rem;color:#cdd6ea;margin-top:6px}
footer{padding:18px 22px;color:var(--muted);font-size:.78rem;border-top:1px solid var(--line);margin-top:30px}
a{color:var(--accent)}
</style></head>
<body>
<header>
  <h1>SC-900 Practice Exam</h1>
  <span class="pill">Microsoft Security, Compliance &amp; Identity Fundamentals</span>
  <span class="pill">150 questions</span>
  <span class="spacer"></span>
  <span id="progress" class="pill">Answered 0 / 150</span>
</header>

<div class="toolbar">
  <div class="modebtns">
    <button id="btnStudy" class="active" onclick="setMode('study')">Study mode</button>
    <button id="btnExam" onclick="setMode('exam')">Exam mode</button>
  </div>
  <span id="timer"></span>
  <span class="spacer"></span>
  <button id="endBtn" class="primary" onclick="endExam()">End exam</button>
  <button onclick="resetExam()">Reset</button>
</div>

<main>
  <div id="quiz"></div>
  <div class="score" id="score">
    <h2>Result</h2>
    <div class="big"><span id="scnum">0</span><span style="font-size:1rem;color:var(--muted)"> / 150</span></div>
    <div id="verdict" class="legend"></div>
    <div id="pie"></div>
    <div class="break" id="breakdown"></div>
    <div class="rec" id="rec"><h3>Focus area — weakest domain</h3><ul id="recul"></ul></div>
    <div id="review"></div>
  </div>
</main>

<footer>
  Self-made study companion for the Microsoft SC-900 exam using the official study guide (skills measured as of July 28, 2026). Not an official Microsoft product.
  Real exam: about 40 questions, 45 minutes, pass 700/1000 (approx 70%). Pair with the official <a href="https://learn.microsoft.com/en-us/credentials/certifications/security-compliance-and-identity-fundamentals/" target="_blank">SC-900</a> resources.
</footer>

<script>
const DOMAINS = __DOM__;
const STUDYGUIDE = __SG__;
const Q = __Q__;
const EXAM_MINUTES = 90;
const PASS_PCT = 70;

let mode = 'study';
let current = 0;
const answers = new Array(Q.length).fill(null);
const revealed = new Array(Q.length).fill(false);
let timer = null, remaining = EXAM_MINUTES*60;
const quiz = document.getElementById('quiz');

function setMode(m){
  mode = m;
  document.getElementById('btnStudy').classList.toggle('active', m==='study');
  document.getElementById('btnExam').classList.toggle('active', m==='exam');
  document.getElementById('timer').style.visibility = (m==='exam') ? 'visible':'hidden';
  if(m==='exam'){ startTimer(); } else { stopTimer(); document.getElementById('timer').textContent=''; }
  renderCurrent();
}
function startTimer(){
  stopTimer();
  remaining = EXAM_MINUTES*60;
  updateTimer();
  timer = setInterval(()=>{ remaining--; updateTimer(); if(remaining<=0){ stopTimer(); endExam(); } },1000);
}
function stopTimer(){ if(timer){ clearInterval(timer); timer=null; } }
function updateTimer(){
  const m=Math.floor(remaining/60), s=remaining%60;
  document.getElementById('timer').textContent='Time '+m+':'+(s<10?'0':'')+s;
}
function updateProgress(){
  const n=answers.filter(a=>a!==null).length;
  document.getElementById('progress').textContent='Answered '+n+' / '+Q.length;
}
function renderCurrent(){
  const q=Q[current];
  let hs='<div class="qhead"><span class="qdomain">'+DOMAINS[q.d]+'</span><span class="qno">Question '+(current+1)+' of '+Q.length+'</span></div>';
  hs+='<div class="question">'+q.q+'</div><div class="options">';
  const chosen=answers[current];
  const show=revealed[current];
  q.o.forEach((opt,i)=>{
    let cls='opt';
    if(show){
      if(i===q.a) cls+=' correct';
      else if(chosen===i) cls+=' wrong';
      else cls+=' dim';
    }
    hs+='<label class="'+cls+'"><input type="radio" name="opt" value="'+i+'" '+(chosen===i?'checked':'')+' onchange="choose('+i+')"> '+opt+'</label>';
  });
  hs+='</div>';
  if(show){ hs+='<div class="exp"><strong>Explanation:</strong> '+q.x+'</div>'; }
  const last = current===Q.length-1;
  hs+='<div class="qnav"><button onclick="go(-1)" '+(current===0?'disabled':'')+'>&larr; Back</button>';
  hs+='<div class="qcontrols">';
  if(mode==='study' && !revealed[current]) hs+='<button onclick="reveal()">Reveal answer</button>';
  hs+='<button class="primary" onclick="go(1)">'+(last?'Review / End':'Next &rarr;')+'</button>';
  hs+='</div></div>';
  quiz.innerHTML=hs;
}
function choose(i){ answers[current]=i; updateProgress(); renderCurrent(); }
function reveal(){ revealed[current]=true; renderCurrent(); }
function go(dir){
  const nxt=current+dir;
  if(nxt<0) return;
  if(nxt>=Q.length){ endExam(); return; }
  current=nxt; renderCurrent();
}
function endExam(){
  stopTimer();
  const answered=answers.filter(a=>a!==null).length;
  let correct=0; const dom={};
  Object.keys(DOMAINS).forEach(k=>dom[k]={t:0,c:0});
  Q.forEach((q,i)=>{ dom[q.d].t++; if(answers[i]===q.a){ correct++; dom[q.d].c++; } });
  const pct=Math.round(correct/Q.length*100);
  document.getElementById('scnum').textContent=correct;
  const pass = pct>=PASS_PCT;
  document.getElementById('verdict').textContent = 'You answered '+answered+' of '+Q.length+'. Score: '+pct+'% — '+(pass?'PASS (>=70%)':'BELOW PASS (>=70%)');
  renderPie(dom,pct);
  const bd=document.getElementById('breakdown'); bd.innerHTML='';
  Object.keys(DOMAINS).forEach(k=>{
    const d=dom[k]; const p=d.t?Math.round(d.c/d.t*100):0;
    const cls = p>=PASS_PCT?'ok':'no';
    bd.innerHTML+='<div class="brow"><span>'+DOMAINS[k]+' <span style="color:var(--muted)">('+d.t+' Q)</span></span><span class="pct '+cls+'">'+d.c+'/'+d.t+' * '+p+'%</span></div>';
  });
  const rec=document.getElementById('rec'); rec.classList.add('show');
  const weakest=Object.keys(DOMAINS).map(k=>({k,p:dom[k].t?dom[k].c/dom[k].t:1})).sort((a,b)=>a.p-b.p)[0];
  const ul=document.getElementById('recul'); ul.innerHTML='';
  (STUDYGUIDE[weakest.k]||[]).forEach(t=>ul.innerHTML+='<li>'+t+'</li>');
  const rv=document.getElementById('review'); rv.innerHTML='<h3 style="margin:18px 0 8px">Review</h3>';
  Q.forEach((q,i)=>{
    const ok=answers[i]===q.a;
    rv.innerHTML+='<div class="review-item"><div class="rq">'+(i+1)+'. '+q.q+'</div>'+
      '<div class="rr '+(ok?'ok':'no')+'">'+(ok?'Correct':'Your answer: '+(answers[i]!==null?q.o[answers[i]]:'--'))+' | Correct: '+q.o[q.a]+'</div>'+
      '<div class="rx"><strong>Why:</strong> '+q.x+'</div></div>';
  });
  document.getElementById('score').style.display='block';
  document.getElementById('score').scrollIntoView({behavior:'smooth'});
}
function renderPie(dom, pct){
  const colors={C:'#6ea8fe',E:'#3ecf8e',S:'#f5a623',M:'#c779e8'};
  const segs=Object.keys(DOMAINS);
  const total=segs.reduce((s,k)=>s+dom[k].t,0);
  const R=70,Cx=90,Cy=90,sw=26;
  let off=0,paths='';
  segs.forEach(k=>{
    const frac=dom[k].t/total, len=frac*2*Math.PI*R, col=colors[k]||'#888';
    paths+='<circle cx="'+Cx+'" cy="'+Cy+'" r="'+R+'" fill="none" stroke="'+col+'" stroke-width="'+sw+'" '+
      'stroke-dasharray="'+len+' '+(2*Math.PI*R-len)+'" stroke-dashoffset="'+(-off)+'" transform="rotate(-90 '+Cx+' '+Cy+')"></circle>';
    off+=len;
  });
  document.getElementById('pie').innerHTML=
    '<svg viewBox="0 0 180 180" width="200" height="200">'+paths+
    '<text x="90" y="84" text-anchor="middle" font-size="26" font-weight="700" fill="#e8ecf5">'+pct+'%</text>'+
    '<text x="90" y="104" text-anchor="middle" font-size="11" fill="#9aa6c0">correct</text></svg>'+
    '<div class="pielabel">Segments sized by question count per domain</div>';
}
function resetExam(){
  for(let i=0;i<Q.length;i++){answers[i]=null; revealed[i]=false;}
  current=0; document.getElementById('score').style.display='none';
  if(mode==='exam') startTimer(); updateProgress(); renderCurrent();
}
setMode('study');
updateProgress();
</script>
</body></html>
"""
html = html.replace("__DOM__", DOM_json).replace("__SG__", SG_json).replace("__Q__", Q_json)
open("/Users/warrenduncan/sc900-practice-exam/index.html","w").write(html)
print("written", len(html), "bytes")
