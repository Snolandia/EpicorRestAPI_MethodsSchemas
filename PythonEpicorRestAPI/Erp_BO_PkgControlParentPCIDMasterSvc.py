import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PkgControlParentPCIDMasterSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_Init(epicorHeaders = None):
   """  
   Summary: Invoke method Init
   OperationID: Init
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Init_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetNewPCIDMaster(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPCIDMaster
   Description: This returns a blank master record to the UI
   OperationID: GetNewPCIDMaster
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPCIDMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCIDMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPCIDPrinted(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPCIDPrinted
   Description: to check if pcid has been printed and throw a error.
   OperationID: CheckPCIDPrinted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPCIDPrinted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPCIDPrinted_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReportStyleNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetReportStyleNum
   OperationID: GetReportStyleNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReportStyleNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportStyleNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessParentPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessParentPCID
   Description: This method updates the parent pcid record when the ui is closed.
   OperationID: ProcessParentPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessParentPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessParentPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessChildPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessChildPCID
   Description: this method creates the parent/child links if a child is scanned in the UI.
   OperationID: ProcessChildPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessChildPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessChildPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessPCIDPrinted(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessPCIDPrinted
   Description: This method updates the parent pcid record after a mixed label has been printed
   OperationID: ProcessPCIDPrinted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessPCIDPrinted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessPCIDPrinted_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreProcess(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreProcess
   Description: this method checks the parent/child records for errors before processing.
   OperationID: PreProcess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreProcess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreProcess_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateEDIMasterMixed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateEDIMasterMixed
   Description: To validate the EDI Data before print and during confirm
   OperationID: ValidateEDIMasterMixed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateEDIMasterMixed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateEDIMasterMixed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreProcessConfirm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreProcessConfirm
   OperationID: PreProcessConfirm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreProcessConfirm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreProcessConfirm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConfirmParent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConfirmParent
   Description: This method should be called when a child pcid has already been entered and
if the parent needs to be confirmed
   OperationID: ConfirmParent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConfirmParent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfirmParent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConfirmChild(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConfirmChild
   Description: This method should be called if the parent PCID is already entered
and the user wants to confirm the child.
   OperationID: ConfirmChild
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConfirmChild_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfirmChild_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MasterPCIDNeedsToBeLoaded(epicorHeaders = None):
   """  
   Summary: Invoke method MasterPCIDNeedsToBeLoaded
   Description: Method to throw a error message
   OperationID: MasterPCIDNeedsToBeLoaded
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/MasterPCIDNeedsToBeLoaded_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_ContactSupervisor(epicorHeaders = None):
   """  
   Summary: Invoke method ContactSupervisor
   OperationID: ContactSupervisor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ContactSupervisor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlParentPCIDMasterSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CheckPCIDPrinted_input:
   """ Required : 
   ipPCID
   """  
   def __init__(self, obj):
      self.ipPCID:str = obj["ipPCID"]
      pass

class CheckPCIDPrinted_output:
   def __init__(self, obj):
      pass

class ConfirmChild_input:
   """ Required : 
   ds
   ipPCID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlParentPCIDMasterTableset] = obj["ds"]
      self.ipPCID:str = obj["ipPCID"]
      """  child pcid that needs to be confirmed  """  
      pass

class ConfirmChild_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlParentPCIDMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ConfirmParent_input:
   """ Required : 
   ds
   ipPCID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlParentPCIDMasterTableset] = obj["ds"]
      self.ipPCID:str = obj["ipPCID"]
      pass

class ConfirmParent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlParentPCIDMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ContactSupervisor_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PkgControlParentPCIDMasterRow:
   def __init__(self, obj):
      self.PCID:str = obj["PCID"]
      self.Status:str = obj["Status"]
      self.Label:str = obj["Label"]
      self.Part:str = obj["Part"]
      self.Quantity:int = obj["Quantity"]
      self.UOM:str = obj["UOM"]
      self.NumberOfPCIDs:int = obj["NumberOfPCIDs"]
      self.PrevPCID:str = obj["PrevPCID"]
      self.ChildPCID:str = obj["ChildPCID"]
      self.PkgMasterMixedPrint:bool = obj["PkgMasterMixedPrint"]
      self.ControlIDCode:str = obj["ControlIDCode"]
      self.MasterMixedMaster:str = obj["MasterMixedMaster"]
      self.Seq:int = obj["Seq"]
      self.MessageUI:str = obj["MessageUI"]
      self.RemoveChild:bool = obj["RemoveChild"]
      self.EnablePrint:bool = obj["EnablePrint"]
      self.ConfirmPCID:str = obj["ConfirmPCID"]
      self.EnableParent:bool = obj["EnableParent"]
      """  Enable parent PCID field.  """  
      self.EnableChild:bool = obj["EnableChild"]
      self.EnableConfirmPCID:bool = obj["EnableConfirmPCID"]
      self.ParentPCID:str = obj["ParentPCID"]
      self.UpdatedDate:str = obj["UpdatedDate"]
      """  Last Time and Date when the PCID was updated  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlParentPCIDMasterTableset:
   def __init__(self, obj):
      self.PkgControlParentPCIDMaster:list[Erp_Tablesets_PkgControlParentPCIDMasterRow] = obj["PkgControlParentPCIDMaster"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetNewPCIDMaster_input:
   """ Required : 
   ipType
   """  
   def __init__(self, obj):
      self.ipType:str = obj["ipType"]
      pass

class GetNewPCIDMaster_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlParentPCIDMasterTableset] = obj["returnObj"]
      pass

class GetReportStyleNum_input:
   """ Required : 
   MasterMixed
   ipPCID
   """  
   def __init__(self, obj):
      self.MasterMixed:str = obj["MasterMixed"]
      """  master or mixedmaster  """  
      self.ipPCID:str = obj["ipPCID"]
      """  input pcid  """  
      pass

class GetReportStyleNum_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.NumLabelsToPrint:int = obj["parameters"]
      self.promptForReportStyle:bool = obj["promptForReportStyle"]
      self.printerID:str = obj["parameters"]
      pass

      """  output parameters  """  

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class Init_output:
   def __init__(self, obj):
      pass

class MasterPCIDNeedsToBeLoaded_output:
   def __init__(self, obj):
      pass

class PreProcessConfirm_input:
   """ Required : 
   ds
   ipPCID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlParentPCIDMasterTableset] = obj["ds"]
      self.ipPCID:str = obj["ipPCID"]
      pass

class PreProcessConfirm_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlParentPCIDMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PreProcess_input:
   """ Required : 
   ds
   ipChildPCID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlParentPCIDMasterTableset] = obj["ds"]
      self.ipChildPCID:str = obj["ipChildPCID"]
      pass

class PreProcess_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlParentPCIDMasterTableset] = obj["ds"]
      self.opMessageUI:str = obj["parameters"]
      self.opSupervisorPwdRequired:bool = obj["opSupervisorPwdRequired"]
      pass

      """  output parameters  """  

class ProcessChildPCID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlParentPCIDMasterTableset] = obj["ds"]
      pass

class ProcessChildPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlParentPCIDMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ProcessPCIDPrinted_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlParentPCIDMasterTableset] = obj["ds"]
      pass

class ProcessPCIDPrinted_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlParentPCIDMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ProcessParentPCID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlParentPCIDMasterTableset] = obj["ds"]
      pass

class ProcessParentPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlParentPCIDMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateEDIMasterMixed_input:
   """ Required : 
   ipParentPCID
   """  
   def __init__(self, obj):
      self.ipParentPCID:str = obj["ipParentPCID"]
      pass

class ValidateEDIMasterMixed_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

