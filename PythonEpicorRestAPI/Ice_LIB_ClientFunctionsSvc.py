import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.ClientFunctionsSvc
# Description: Miscellaneous client functions.
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetAuthenticationModeCodeDescriptionList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAuthenticationModeCodeDescriptionList
   Description: Gets a delimited list of authentication modes.
   OperationID: GetAuthenticationModeCodeDescriptionList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAuthenticationModeCodeDescriptionList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAuthenticationModeCodeDescriptionList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTaxConnect(epicorHeaders = None):
   """  
   Summary: Invoke method GetTaxConnect
   Description: This method returns TaxSvcConfig.TaxConnectEnabled for the current Company
otherwise it returns false.
   OperationID: GetTaxConnect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxConnect_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_AlertLogAvailable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AlertLogAvailable
   Description: Return whether alert log records exist.
   OperationID: AlertLogAvailable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AlertLogAvailable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AlertLogAvailable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetWorkstationMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetWorkstationMethod
   Description: Returns The workstation method for a company.
   OperationID: GetWorkstationMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWorkstationMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWorkstationMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSSRSPrintOption(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSSRSPrintOption
   Description: Returns SSRS Printer for a company.
   OperationID: GetSSRSPrintOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSSRSPrintOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSSRSPrintOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPrinterOptions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPrinterOptions
   Description: Gets the SSRS Printer Options for a company.
   OperationID: GetPrinterOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPrinterOptions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPrinterOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessZDHelpTopicOrLabel(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessZDHelpTopicOrLabel
   Description: Utility method for clients (often Kinetic clients) to use returned URL launch Epicor help hosted on Zendesk Epicor help portals (also called "Guides"). The return value of this method (the URL) contains a JWT token for Zendesk
that includes a data payload of some of the method parameters. Zendesk logs the user on with the JWT/payload and uses return_to querystring to navigate user to correct topic.
The typical action a client will take on the client with the returned URL is (to give a simple js example) javascript: window.open(url,"epHelpWindow",null,false). The token has a 3 minute window to be used.
   OperationID: ProcessZDHelpTopicOrLabel
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessZDHelpTopicOrLabel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessZDHelpTopicOrLabel_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClientDownloadAvailable(epicorHeaders = None):
   """  
   Summary: Invoke method ClientDownloadAvailable
   Description: Checks if the configuration required for the client download is available.
   OperationID: ClientDownloadAvailable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClientDownloadAvailable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetClientDownloadUrl(epicorHeaders = None):
   """  
   Summary: Invoke method GetClientDownloadUrl
   Description: Gets the client download URL.
   OperationID: GetClientDownloadUrl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetClientDownloadUrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetIsProductionInstance(epicorHeaders = None):
   """  
   Summary: Invoke method GetIsProductionInstance
   Description: Return the boolean value for first  "IsProductionInstance" value from ice.SysLicense table.
   OperationID: GetIsProductionInstance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIsProductionInstance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_SetIsProductionInstance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetIsProductionInstance
   Description: Set the server/db combination as a production/non-production server.
   OperationID: SetIsProductionInstance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetIsProductionInstance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetIsProductionInstance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetInstancePurposes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetInstancePurposes
   Description: Set the isProduction value for all records in ice.SysLienses Table
   OperationID: SetInstancePurposes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetInstancePurposes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetInstancePurposes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetInstancePurpose(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetInstancePurpose
   Description: Set IsProductionInstance Value for the license instance based on the license id, and DB values from current context
   OperationID: SetInstancePurpose
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetInstancePurpose_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetInstancePurpose_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInstancePurpose(epicorHeaders = None):
   """  
   Summary: Invoke method GetInstancePurpose
   Description: Getting  the single license purpose based on the installation id in the current context/session
   OperationID: GetInstancePurpose
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInstancePurpose_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetProductionServerInstances(epicorHeaders = None):
   """  
   Summary: Invoke method GetProductionServerInstances
   Description: Get Production  Server Instance Details from the DB
   OperationID: GetProductionServerInstances
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetProductionServerInstances_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_SetUpdateAvailableToFalse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetUpdateAvailableToFalse
   Description: Setting UpdateAvailable to false after applying the license
   OperationID: SetUpdateAvailableToFalse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetUpdateAvailableToFalse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUpdateAvailableToFalse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetUpdateAvailableToFalseForAllAppliedLicenses(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetUpdateAvailableToFalseForAllAppliedLicenses
   Description: Flipping UpdateAvailalble field value to false for a list of licenses
   OperationID: SetUpdateAvailableToFalseForAllAppliedLicenses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetUpdateAvailableToFalseForAllAppliedLicenses_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUpdateAvailableToFalseForAllAppliedLicenses_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemoveFromFileStore(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemoveFromFileStore
   Description: Remove the license content from ice.FileStote, once the license is applied
   OperationID: RemoveFromFileStore
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveFromFileStore_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveFromFileStore_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLicenseLiveStatus(epicorHeaders = None):
   """  
   Summary: Invoke method GetLicenseLiveStatus
   Description: Get the license live status
   OperationID: GetLicenseLiveStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLicenseLiveStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_ProcessZDHelpRequestCategory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessZDHelpRequestCategory
   Description: Utility method to open online help (in Zendesk) at the category heading level, instead of navigating directly to a topic.
   OperationID: ProcessZDHelpRequestCategory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessZDHelpRequestCategory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessZDHelpRequestCategory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AlertLogAvailable_input:
   """ Required : 
   companyID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      pass

class AlertLogAvailable_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  Return false if the user doesn't have permission.  """  
      pass

class ClientDownloadAvailable_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  `true`if available  """  
      pass

   def parameters(self, obj):
      self.configurationError:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetAuthenticationModeCodeDescriptionList_input:
   """ Required : 
   includeIdP
   includeToken
   includeTcpBinary
   includeAzureAD
   """  
   def __init__(self, obj):
      self.includeIdP:bool = obj["includeIdP"]
      """  Include Idp in list.  """  
      self.includeToken:bool = obj["includeToken"]
      """  Include Token in list.  """  
      self.includeTcpBinary:bool = obj["includeTcpBinary"]
      """  Include TcpBinary in list.  """  
      self.includeAzureAD:bool = obj["includeAzureAD"]
      """  Include AzureAD in list.  """  
      pass

class GetAuthenticationModeCodeDescriptionList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetClientDownloadUrl_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Url that can be used to download the ERP client installer.  """  
      pass

class GetInstancePurpose_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class GetIsProductionInstance_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class GetLicenseLiveStatus_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class GetPrinterOptions_input:
   """ Required : 
   companyID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  company ID.  """  
      pass

class GetPrinterOptions_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Lib_ClientFunctions_PrinterOptions] = obj["returnObj"]
      pass

class GetProductionServerInstances_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Lib_ClientFunctions_InstanceDetails] = obj["returnObj"]
      pass

class GetSSRSPrintOption_input:
   """ Required : 
   companyID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  Company  """  
      pass

class GetSSRSPrintOption_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetTaxConnect_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.compTaxConnectEnabled:bool = obj["compTaxConnectEnabled"]
      pass

      """  output parameters  """  

class GetWorkstationMethod_input:
   """ Required : 
   companyID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  Company  """  
      pass

class GetWorkstationMethod_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class Ice_Lib_ClientFunctions_InstanceDetails:
   def __init__(self, obj):
      self.LicenseID:str = obj["LicenseID"]
      self.InstanceDescription:str = obj["InstanceDescription"]
      self.IsProductionInstance:bool = obj["IsProductionInstance"]
      pass

class Ice_Lib_ClientFunctions_PrinterOptions:
   def __init__(self, obj):
      self.AllowedPrinter:str = obj["AllowedPrinter"]
      self.DefaultPaperSize:int = obj["DefaultPaperSize"]
      pass

class ProcessZDHelpRequestCategory_input:
   """ Required : 
   label
   category
   helpTopic
   userName
   userEmail
   aryTags
   zdSubDomain
   locale
   """  
   def __init__(self, obj):
      self.label:str = obj["label"]
      """  Corresponds to Label used in Zendesk for an article, and used to locate the URL of an article. Should be lowercase without spaces. In the case of Kinetic forms, use page title as label (lowercasing and trimming spaces)  """  
      self.category:str = obj["category"]
      """  search Zendesk for category landing page using category name  """  
      self.helpTopic:str = obj["helpTopic"]
      """  The fully qualified URL of a Zendesk article. Example- 'https://epicorerp.zendesk.com/hc/en-us/articles/360022072552-View-Schedule' If using label (preferred technique) send null for helpTopic.  """  
      self.userName:str = obj["userName"]
      """  Consult with Epicor University writer on the generic user or users that may be appropriate. Until Epicor Idp is used, most apps will use a single user for the whole app.
            Example- 'Epicor TimeExpenseUser'  """  
      self.userEmail:str = obj["userEmail"]
      """  Email for user. Until actual users are passed (afer Idp), email is just meeting a Zendesk requirement and will not be used (but must consistent for user from call to call).
            Example-'erptimeexpense@epicor.com'  """  
      self.aryTags:str = obj["aryTags"]
      """  Tags are used in Zendesk to show or hide (segment) content. Consult with Epicor University writer on appropriate tags for user.
            Tags sent with call replace previous tag set. Example- ['erptime', 'erpexpense']  """  
      self.zdSubDomain:str = obj["zdSubDomain"]
      """  Consult with EU writer on the Zendesk subdomain to use  """  
      self.locale:str = obj["locale"]
      """  Set to locale of user session. For example - en-us  """  
      pass

class ProcessZDHelpRequestCategory_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  A URL with Zendesk SSO token and redirect url as querystring.  """  
      pass

class ProcessZDHelpTopicOrLabel_input:
   """ Required : 
   label
   helpTopic
   userName
   userEmail
   aryTags
   zdSubDomain
   locale
   """  
   def __init__(self, obj):
      self.label:str = obj["label"]
      """  Corresponds to Label used in Zendesk for an article, and used to locate the URL of an article. Should be lowercase without spaces. In the case of Kinetic forms, use page title as label (lowercasing and trimming spaces)  """  
      self.helpTopic:str = obj["helpTopic"]
      """  The fully qualified URL of a Zendesk article. Example- 'https://epicorerp.zendesk.com/hc/en-us/articles/360022072552-View-Schedule' If using label (preferred technique) send null for helpTopic.  """  
      self.userName:str = obj["userName"]
      """  Consult with Epicor University writer on the generic user or users that may be appropriate. Until Epicor Idp is used, most apps will use a single user for the whole app.
            Example- 'Epicor TimeExpenseUser'  """  
      self.userEmail:str = obj["userEmail"]
      """  Email for user. Until actual users are passed (afer Idp), email is just meeting a Zendesk requirement and will not be used (but must consistent for user from call to call).
            Example-'erptimeexpense@epicor.com'  """  
      self.aryTags:str = obj["aryTags"]
      """  Tags are used in Zendesk to show or hide (segment) content. Consult with Epicor University writer on appropriate tags for user.
            Tags sent with call replace previous tag set. Example- ['erptime', 'erpexpense']  """  
      self.zdSubDomain:str = obj["zdSubDomain"]
      """  Consult with EU writer on the Zendesk subdomain to use  """  
      self.locale:str = obj["locale"]
      """  Set to locale of user session. For example - en-us  """  
      pass

class ProcessZDHelpTopicOrLabel_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  A URL with Zendesk SSO token and redirect url as querystring.  """  
      pass

class RemoveFromFileStore_input:
   """ Required : 
   fileName
   """  
   def __init__(self, obj):
      self.fileName:str = obj["fileName"]
      pass

class RemoveFromFileStore_output:
   def __init__(self, obj):
      pass

class SetInstancePurpose_input:
   """ Required : 
   isProduction
   """  
   def __init__(self, obj):
      self.isProduction:bool = obj["isProduction"]
      pass

class SetInstancePurpose_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class SetInstancePurposes_input:
   """ Required : 
   isProduction
   """  
   def __init__(self, obj):
      self.isProduction:bool = obj["isProduction"]
      pass

class SetInstancePurposes_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class SetIsProductionInstance_input:
   """ Required : 
   isProduction
   """  
   def __init__(self, obj):
      self.isProduction:bool = obj["isProduction"]
      pass

class SetIsProductionInstance_output:
   def __init__(self, obj):
      pass

class SetUpdateAvailableToFalseForAllAppliedLicenses_input:
   """ Required : 
   fileNames
   """  
   def __init__(self, obj):
      self.fileNames:str = obj["fileNames"]
      pass

class SetUpdateAvailableToFalseForAllAppliedLicenses_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class SetUpdateAvailableToFalse_input:
   """ Required : 
   fileName
   """  
   def __init__(self, obj):
      self.fileName:str = obj["fileName"]
      pass

class SetUpdateAvailableToFalse_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

