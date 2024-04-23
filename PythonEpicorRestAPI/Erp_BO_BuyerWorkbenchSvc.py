import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.BuyerWorkbenchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_AddSuggSupplier(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddSuggSupplier
   Description: This methods will add supplier record for an individual suggestion.
   OperationID: AddSuggSupplier
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddSuggSupplier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddSuggSupplier_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRFQSuggVendPurPoint(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRFQSuggVendPurPoint
   Description: This method validates the RFQSuggVend.PurPoint when it changes.
This method should run when changing the RFQSuggVend.PurPoint.
   OperationID: ChangeRFQSuggVendPurPoint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRFQSuggVendPurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRFQSuggVendPurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRFQSuggVendVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRFQSuggVendVendorID
   Description: This methods takes the RFQSuggVend.VendorNum and populates the associated fields
with value based on the vendornum.
This method should run when changing the RFQSuggVend.VendorNum.
   OperationID: ChangeRFQSuggVendVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRFQSuggVendVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRFQSuggVendVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckRFQSuggVendVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckRFQSuggVendVendorID
   Description: This methods checks to see if the new RFQSuggVend.VendorNum has changed from the original
RFQSuggVend.VendorNum and validates the value.
This method should run before changing the RFQSuggVend.VendorNum.
   OperationID: CheckRFQSuggVendVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRFQSuggVendVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRFQSuggVendVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateDatasetWithCounters(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateDatasetWithCounters
   Description: This methods will return all of the records for the Buyer Workbench.
   OperationID: CreateDatasetWithCounters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateDatasetWithCounters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateDatasetWithCounters_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateDataset(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateDataset
   Description: This methods will return all of the records for the Buyer Workbench.
   OperationID: CreateDataset
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateDataset_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateDataset_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteSuggSupplier(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteSuggSupplier
   Description: This methods will delete supplier record for an individual suggestion.
   OperationID: DeleteSuggSupplier
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteSuggSupplier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteSuggSupplier_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeselectAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeselectAll
   Description: This method will change the ProcessRFQ field in the RFQSugg table and the
RFQSuggBWB temp table to false (deselected) for the inputted buyerid.
   OperationID: DeselectAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeselectAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeselectAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Generate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Generate
   Description: This method will generate RFQ's for lines.  This method can generate for all
suggestions for a buyer by only entering a buyerid or a specific suggestion by
also entering a suggestion number.  This method will call CreateDataset at the
end of running to refresh the dataset.
   OperationID: Generate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Generate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Generate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSugPOChgCount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSugPOChgCount
   Description: This methods will return a count of Change PO Suggestions for the selected Buyer
   OperationID: GetSugPOChgCount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSugPOChgCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSugPOChgCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSugPoDtlCount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSugPoDtlCount
   Description: This methods will return a count of NEW PO Suggestions for the selected Buyer
   OperationID: GetSugPoDtlCount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSugPoDtlCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSugPoDtlCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSuggSupp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSuggSupp
   Description: This methods will create a blank RFQSuggVend record for an individual suggestion
and allow the user to type in field values through the grid.
   OperationID: GetNewSuggSupp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSuggSupp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSuggSupp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SelectAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SelectAll
   Description: This method will change the ProcessRFQ field in the RFQSugg table and the
RFQSuggBWB temp table to true (selected) for the inputted buyerid.
   OperationID: SelectAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SupplierWizard(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SupplierWizard
   Description: This methods will return suppliers for the suggestion
   OperationID: SupplierWizard
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SupplierWizard_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SupplierWizard_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AddSuggSupplier_input:
   """ Required : 
   ipBuyerID
   ipSugNum
   ipVendorNum
   ipPurPoint
   ds
   """  
   def __init__(self, obj):
      self.ipBuyerID:str = obj["ipBuyerID"]
      """  The buyer id to add data for.  """  
      self.ipSugNum:int = obj["ipSugNum"]
      """  The suggestion number to link suppliers to.  """  
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  The vendor number of the supplier to add.  """  
      self.ipPurPoint:str = obj["ipPurPoint"]
      """  The purchase point of the supplier to add.  """  
      self.ds:list[Erp_Tablesets_BuyerWorkbenchTableset] = obj["ds"]
      pass

class AddSuggSupplier_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opStatusMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_BuyerWorkbenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRFQSuggVendPurPoint_input:
   """ Required : 
   ipRFQSuggVendRowid
   ds
   """  
   def __init__(self, obj):
      self.ipRFQSuggVendRowid:str = obj["ipRFQSuggVendRowid"]
      """  The rowident of the record being updated/created.  """  
      self.ds:list[Erp_Tablesets_BuyerWorkbenchTableset] = obj["ds"]
      pass

class ChangeRFQSuggVendPurPoint_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BuyerWorkbenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRFQSuggVendVendorID_input:
   """ Required : 
   ipBuyerID
   ipRFQSuggVendRowid
   ds
   """  
   def __init__(self, obj):
      self.ipBuyerID:str = obj["ipBuyerID"]
      """  The buyer id used to locate records.  """  
      self.ipRFQSuggVendRowid:str = obj["ipRFQSuggVendRowid"]
      """  The rowident of the record being updated/created.  """  
      self.ds:list[Erp_Tablesets_BuyerWorkbenchTableset] = obj["ds"]
      pass

class ChangeRFQSuggVendVendorID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opStatusMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_BuyerWorkbenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckRFQSuggVendVendorID_input:
   """ Required : 
   ipProposedVendorID
   ipRFQSuggVendRowid
   ds
   """  
   def __init__(self, obj):
      self.ipProposedVendorID:str = obj["ipProposedVendorID"]
      """  The new proposed RFQSuggVend.VendorID value  """  
      self.ipRFQSuggVendRowid:str = obj["ipRFQSuggVendRowid"]
      """  The rowident of the record being updated/created.  """  
      self.ds:list[Erp_Tablesets_BuyerWorkbenchTableset] = obj["ds"]
      pass

class CheckRFQSuggVendVendorID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BuyerWorkbenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateDatasetWithCounters_input:
   """ Required : 
   ipBuyerID
   """  
   def __init__(self, obj):
      self.ipBuyerID:str = obj["ipBuyerID"]
      """  The buyer id to return data for.  """  
      pass

class CreateDatasetWithCounters_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BuyerWorkbenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.poSuggCount:int = obj["parameters"]
      self.poSuggChgCount:int = obj["parameters"]
      pass

      """  output parameters  """  

class CreateDataset_input:
   """ Required : 
   ipBuyerID
   """  
   def __init__(self, obj):
      self.ipBuyerID:str = obj["ipBuyerID"]
      """  The buyer id to return data for.  """  
      pass

class CreateDataset_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BuyerWorkbenchTableset] = obj["returnObj"]
      pass

class DeleteSuggSupplier_input:
   """ Required : 
   ipSugNum
   ipVendorNum
   ds
   """  
   def __init__(self, obj):
      self.ipSugNum:int = obj["ipSugNum"]
      """  The suggestion number to delete suppliers for.  """  
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  The vendor number of the supplier to delete.  """  
      self.ds:list[Erp_Tablesets_BuyerWorkbenchTableset] = obj["ds"]
      pass

class DeleteSuggSupplier_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opStatusMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_BuyerWorkbenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeselectAll_input:
   """ Required : 
   ipBuyerID
   ds
   """  
   def __init__(self, obj):
      self.ipBuyerID:str = obj["ipBuyerID"]
      """  The buyer id to deselect all for.  """  
      self.ds:list[Erp_Tablesets_BuyerWorkbenchTableset] = obj["ds"]
      pass

class DeselectAll_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BuyerWorkbenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_BuyerWorkbenchTableset:
   def __init__(self, obj):
      self.POTotal:list[Erp_Tablesets_POTotalRow] = obj["POTotal"]
      self.POApproval:list[Erp_Tablesets_POApprovalRow] = obj["POApproval"]
      self.POChangeSugg:list[Erp_Tablesets_POChangeSuggRow] = obj["POChangeSugg"]
      self.POFuture:list[Erp_Tablesets_POFutureRow] = obj["POFuture"]
      self.POLate:list[Erp_Tablesets_POLateRow] = obj["POLate"]
      self.PONewSugg:list[Erp_Tablesets_PONewSuggRow] = obj["PONewSugg"]
      self.POReject:list[Erp_Tablesets_PORejectRow] = obj["POReject"]
      self.POThisWeek:list[Erp_Tablesets_POThisWeekRow] = obj["POThisWeek"]
      self.POToday:list[Erp_Tablesets_POTodayRow] = obj["POToday"]
      self.RFQTotal:list[Erp_Tablesets_RFQTotalRow] = obj["RFQTotal"]
      self.RFQFuture:list[Erp_Tablesets_RFQFutureRow] = obj["RFQFuture"]
      self.RFQOverdue:list[Erp_Tablesets_RFQOverdueRow] = obj["RFQOverdue"]
      self.RFQReady:list[Erp_Tablesets_RFQReadyRow] = obj["RFQReady"]
      self.RFQSuggBWB:list[Erp_Tablesets_RFQSuggBWBRow] = obj["RFQSuggBWB"]
      self.RFQSuggVend:list[Erp_Tablesets_RFQSuggVendRow] = obj["RFQSuggVend"]
      self.RFQThisWeek:list[Erp_Tablesets_RFQThisWeekRow] = obj["RFQThisWeek"]
      self.RFQToday:list[Erp_Tablesets_RFQTodayRow] = obj["RFQToday"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_POApprovalRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company identifier  """  
      self.PONum:int = obj["PONum"]
      """  The po number.  """  
      self.MsgType:str = obj["MsgType"]
      """  The message type.  """  
      self.MsgDate:str = obj["MsgDate"]
      """  The message date.  """  
      self.MsgTime:int = obj["MsgTime"]
      """  The message time.  """  
      self.MsgTo:str = obj["MsgTo"]
      """  The message to value.  """  
      self.MsgFrom:str = obj["MsgFrom"]
      """  The message from value.  """  
      self.ApproverResponse:str = obj["ApproverResponse"]
      """  The approver's response.  """  
      self.DCDUserID:str = obj["DCDUserID"]
      """  The user id.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The buyer id.  """  
      self.MsgText:str = obj["MsgText"]
      """  Text for communication.  """  
      self.BuyerName:str = obj["BuyerName"]
      """  The buyer id name.  """  
      self.MsgToName:str = obj["MsgToName"]
      """  The buyer name of the buyerid in the msgto field.  """  
      self.MsgFromName:str = obj["MsgFromName"]
      """  The buyer name for the buyerid in the msgfrom field.  """  
      self.FormattedMsgTime:str = obj["FormattedMsgTime"]
      """  The formatted representation of the msgtime field.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POChangeSuggRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company identifier.  """  
      self.PONum:int = obj["PONum"]
      """  The po number.  """  
      self.POLine:int = obj["POLine"]
      """  The po release line number.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  The po release number.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The buyer id.  """  
      self.RequireDate:str = obj["RequireDate"]
      """  The require date.  """  
      self.Plant:str = obj["Plant"]
      """  The plant identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part number.  """  
      self.Suggestion:str = obj["Suggestion"]
      """  The suggestion text or exception text  """  
      self.VendorID:str = obj["VendorID"]
      """  The vendor id.  """  
      self.VendName:str = obj["VendName"]
      """  The vendor name.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The purchase point.  """  
      self.VendorChange:bool = obj["VendorChange"]
      """  The vendor change flag.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POFutureRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company identifier.  """  
      self.PONum:int = obj["PONum"]
      """  The po number.  """  
      self.POLine:int = obj["POLine"]
      """  The po line number.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  The po release number.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date.  """  
      self.PromiseDt:str = obj["PromiseDt"]
      """  The promise date.  """  
      self.JobNum:str = obj["JobNum"]
      """  The job number.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part number.  """  
      self.RelQty:int = obj["RelQty"]
      """  The release quantity.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  The received quantity.  """  
      self.RemainQty:int = obj["RemainQty"]
      """  The remaining quantity.  """  
      self.VendorID:str = obj["VendorID"]
      """  The vendor id.  """  
      self.VendName:str = obj["VendName"]
      """  The vendor name.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The buyer id.  """  
      self.RelQtyUOM:str = obj["RelQtyUOM"]
      self.ReceivedQtyUOM:str = obj["ReceivedQtyUOM"]
      self.RemainQtyUOM:str = obj["RemainQtyUOM"]
      self.DeviationQty:int = obj["DeviationQty"]
      """  The difference between RelQty and ReceivedQty  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.ShortDescription:str = obj["ShortDescription"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POLateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company identifier.  """  
      self.PONum:int = obj["PONum"]
      """  The po number.  """  
      self.POLine:int = obj["POLine"]
      """  The po line number.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  The po release number.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date.  """  
      self.PromiseDt:str = obj["PromiseDt"]
      """  The promise date.  """  
      self.JobNum:str = obj["JobNum"]
      """  The job number.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part.  """  
      self.RelQty:int = obj["RelQty"]
      """  The release quantity.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  The received quantity.  """  
      self.RemainQty:int = obj["RemainQty"]
      """  The remaining quantity  """  
      self.VendorID:str = obj["VendorID"]
      """  The vendor id.  """  
      self.VendName:str = obj["VendName"]
      """  The vendor name.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The buyer id.  """  
      self.RelQtyUOM:str = obj["RelQtyUOM"]
      self.ReceivedQtyUOM:str = obj["ReceivedQtyUOM"]
      self.RemainQtyUOM:str = obj["RemainQtyUOM"]
      self.DeviationQty:int = obj["DeviationQty"]
      """  The difference between RelQty and ReceivedQty  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.ShortDescription:str = obj["ShortDescription"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PONewSuggRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company identifier.  """  
      self.SugNum:int = obj["SugNum"]
      """  The suggestion number.  """  
      self.SugType:str = obj["SugType"]
      """  The suggestion type.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The buyer id.  """  
      self.PONum:int = obj["PONum"]
      """  The po number.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.Buy:bool = obj["Buy"]
      self.ClassDescription:str = obj["ClassDescription"]
      self.ContractID:str = obj["ContractID"]
      self.CreateRFQ:bool = obj["CreateRFQ"]
      self.DueDate:str = obj["DueDate"]
      self.DynAttrValueSetShortDesc:str = obj["DynAttrValueSetShortDesc"]
      self.JobNum:str = obj["JobNum"]
      self.JobSeq:int = obj["JobSeq"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PurPoint:str = obj["PurPoint"]
      self.ReqLine:int = obj["ReqLine"]
      self.ReqNum:int = obj["ReqNum"]
      self.Review:bool = obj["Review"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.ShipViaCode:str = obj["ShipViaCode"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.VendorID:str = obj["VendorID"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.OrderByDate:str = obj["OrderByDate"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PORejectRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company identifier.  """  
      self.TranID:int = obj["TranID"]
      """  The transaction id.  """  
      self.TranType:str = obj["TranType"]
      """  The transaction type.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The buyer id.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The vendor number.  """  
      self.PONum:int = obj["PONum"]
      """  The po number.  """  
      self.POLine:int = obj["POLine"]
      """  The po line number.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  The po release number.  """  
      self.TranDate:str = obj["TranDate"]
      """  The transaction date.  """  
      self.TranTime:int = obj["TranTime"]
      """  The transaction time  """  
      self.VendName:str = obj["VendName"]
      """  The vendor name.  """  
      self.OpenOrder:bool = obj["OpenOrder"]
      """  Is this po open?  """  
      self.DspTranTime:str = obj["DspTranTime"]
      """  Display transaction time formatted Time display.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POThisWeekRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company identifier.  """  
      self.PONum:int = obj["PONum"]
      """  The po number.  """  
      self.POLine:int = obj["POLine"]
      """  The po line number.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  The po release number.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date.  """  
      self.PromiseDt:str = obj["PromiseDt"]
      """  The promise date.  """  
      self.JobNum:str = obj["JobNum"]
      """  The job number.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part number.  """  
      self.RelQty:int = obj["RelQty"]
      """  The release quantity.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  The received quantity.  """  
      self.RemainQty:int = obj["RemainQty"]
      """  The remaining quantity.  """  
      self.VendorID:str = obj["VendorID"]
      """  The vendor id.  """  
      self.VendName:str = obj["VendName"]
      """  The vendor name.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The buyer id.  """  
      self.RelQtyUOM:str = obj["RelQtyUOM"]
      self.ReceivedQtyUOM:str = obj["ReceivedQtyUOM"]
      self.RemainQtyUOM:str = obj["RemainQtyUOM"]
      self.DeviationQty:int = obj["DeviationQty"]
      """  The difference between RelQty and ReceivedQty  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.ShortDescription:str = obj["ShortDescription"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POTodayRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company identifier.  """  
      self.PONum:int = obj["PONum"]
      """  The po number.  """  
      self.POLine:int = obj["POLine"]
      """  The po line number.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  The po release number.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date.  """  
      self.PromiseDt:str = obj["PromiseDt"]
      """  The promise date.  """  
      self.JobNum:str = obj["JobNum"]
      """  The job number.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part number.  """  
      self.RelQty:int = obj["RelQty"]
      """  The release quantity.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  The received quantity.  """  
      self.RemainQty:int = obj["RemainQty"]
      """  The remaining quantity.  """  
      self.VendorID:str = obj["VendorID"]
      """  The vendor id.  """  
      self.VendName:str = obj["VendName"]
      """  The vendor name.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The buyer id.  """  
      self.RelQtyUOM:str = obj["RelQtyUOM"]
      self.ReceivedQtyUOM:str = obj["ReceivedQtyUOM"]
      self.RemainQtyUOM:str = obj["RemainQtyUOM"]
      self.DeviationQty:int = obj["DeviationQty"]
      """  The difference between RelQty and ReceivedQty  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.ShortDescription:str = obj["ShortDescription"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POTotalRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company identifier.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The buyer id.  """  
      self.TotalPOCnt:int = obj["TotalPOCnt"]
      """  The total count of pos for this buyer.  """  
      self.BuyerName:str = obj["BuyerName"]
      """  The buyer name.  """  
      self.TotalApproval:int = obj["TotalApproval"]
      """  Number of POs that require approval  """  
      self.TotalFuture:int = obj["TotalFuture"]
      """  Number of POs with a due date greater than the last day of the current week  """  
      self.TotalLate:int = obj["TotalLate"]
      """  Number of POs with a due date earlier than todays date  """  
      self.TotalReject:int = obj["TotalReject"]
      """  Number of POs that have been rejected  """  
      self.TotalThisWeek:int = obj["TotalThisWeek"]
      """  Number of POs with due date greater than today but less than the last day of the week  """  
      self.TotalToday:int = obj["TotalToday"]
      """  Number of POs with a due date of today  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQFutureRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company identifier.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  The rfq number.  """  
      self.OpenRFQ:bool = obj["OpenRFQ"]
      """  Is the rfq open?  """  
      self.RFQDate:str = obj["RFQDate"]
      """  The rfq date.  """  
      self.RFQDueDate:str = obj["RFQDueDate"]
      """  The rfq due date.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The buyer id.  """  
      self.CommentText:str = obj["CommentText"]
      """  The comment text.  """  
      self.ReadyToPrint:bool = obj["ReadyToPrint"]
      """  Is rfq ready to be printed?  """  
      self.RespondDate:str = obj["RespondDate"]
      """  The respond date.  """  
      self.DecisionDate:str = obj["DecisionDate"]
      """  The decision date.  """  
      self.PostToWeb:bool = obj["PostToWeb"]
      """  Post to web?  """  
      self.PostDate:str = obj["PostDate"]
      """  The post date.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQOverdueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company identifier.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  The rfq number.  """  
      self.OpenRFQ:bool = obj["OpenRFQ"]
      """  Is the rfq open?  """  
      self.RFQDate:str = obj["RFQDate"]
      """  The rfq date.  """  
      self.RFQDueDate:str = obj["RFQDueDate"]
      """  The rfq due date.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The buyer id.  """  
      self.CommentText:str = obj["CommentText"]
      """  The comment text.  """  
      self.ReadyToPrint:bool = obj["ReadyToPrint"]
      """  Is rfq ready to be printed?  """  
      self.RespondDate:str = obj["RespondDate"]
      """  The respond date.  """  
      self.DecisionDate:str = obj["DecisionDate"]
      """  The decision date.  """  
      self.PostToWeb:bool = obj["PostToWeb"]
      """  Post to web?  """  
      self.PostDate:str = obj["PostDate"]
      """  The post date.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQReadyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company identifier.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  The rfq number.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The rfq line number.  """  
      self.RFQDate:str = obj["RFQDate"]
      """  The rfq date.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The part number description.  """  
      self.RFQDueDate:str = obj["RFQDueDate"]
      """  The rfq due date.  """  
      self.RespondDate:str = obj["RespondDate"]
      """  The respond date.  """  
      self.DecisionDate:str = obj["DecisionDate"]
      """  The decision date.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The buyer id.  """  
      self.RcvdRspns:int = obj["RcvdRspns"]
      """  The number of received responses.  """  
      self.NeededRspns:int = obj["NeededRspns"]
      """  The number of minimum needed responses.  """  
      self.TotRspns:int = obj["TotRspns"]
      """  The total responses.  """  
      self.ItemType:str = obj["ItemType"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQSuggBWBRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company identifier.  """  
      self.SugNum:int = obj["SugNum"]
      """  The suggestion number.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  The line description.  """  
      self.IUM:str = obj["IUM"]
      """  The ium.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description for the part number.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The part revision number.  """  
      self.CommentText:str = obj["CommentText"]
      """  The comment text.  """  
      self.Class:str = obj["Class"]
      """  The class.  """  
      self.JobNum:str = obj["JobNum"]
      """  The job number.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  The quote number.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The quote line number.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The assembly sequence.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  The job sequence.  """  
      self.ItemType:str = obj["ItemType"]
      """  The item type.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The vendor number.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The vendor quote requirements.  """  
      self.ProcessRFQ:bool = obj["ProcessRFQ"]
      """  Process the rfq?  """  
      self.VendorID:str = obj["VendorID"]
      """  The vendor id.  """  
      self.Source:str = obj["Source"]
      """  The source.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The buyer id.  """  
      self.QtyList:str = obj["QtyList"]
      self.GlbSuggestion:bool = obj["GlbSuggestion"]
      self.GlbCompany:str = obj["GlbCompany"]
      self.PurPoint:str = obj["PurPoint"]
      """  The purchase point.  """  
      self.OpCode:str = obj["OpCode"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQSuggVendRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The vendor number.  """  
      self.VendorID:str = obj["VendorID"]
      """  The vendor id.  """  
      self.VendName:str = obj["VendName"]
      """  The vendor name.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The purchase point.  """  
      self.Approved:bool = obj["Approved"]
      """  Approved?  """  
      self.SugNum:int = obj["SugNum"]
      """  The suggestion number.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The buyer id.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQThisWeekRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company identifier.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  The rfq number.  """  
      self.OpenRFQ:bool = obj["OpenRFQ"]
      """  Is the rfq open?  """  
      self.RFQDate:str = obj["RFQDate"]
      """  The rfq date.  """  
      self.RFQDueDate:str = obj["RFQDueDate"]
      """  The rfq due date.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The buyer id.  """  
      self.CommentText:str = obj["CommentText"]
      """  The comment text.  """  
      self.ReadyToPrint:bool = obj["ReadyToPrint"]
      """  Is the rfq ready to be printed?  """  
      self.RespondDate:str = obj["RespondDate"]
      """  The respond date.  """  
      self.DecisionDate:str = obj["DecisionDate"]
      """  The decision date.  """  
      self.PostToWeb:bool = obj["PostToWeb"]
      """  Post to web?  """  
      self.PostDate:str = obj["PostDate"]
      """  The post date.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQTodayRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company identifier.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  The rfq number.  """  
      self.OpenRFQ:bool = obj["OpenRFQ"]
      """  Is the rfq open?  """  
      self.RFQDate:str = obj["RFQDate"]
      """  The rfq date.  """  
      self.RFQDueDate:str = obj["RFQDueDate"]
      """  The rfq due date.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The buyer id.  """  
      self.CommentText:str = obj["CommentText"]
      """  The comment text.  """  
      self.ReadyToPrint:bool = obj["ReadyToPrint"]
      """  Is the rfq ready to be printed?  """  
      self.RespondDate:str = obj["RespondDate"]
      """  The respond date.  """  
      self.DecisionDate:str = obj["DecisionDate"]
      """  The decision date.  """  
      self.PostToWeb:bool = obj["PostToWeb"]
      """  Post to web?  """  
      self.PostDate:str = obj["PostDate"]
      """  The post date.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQTotalRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company indentifier.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  The buyer id.  """  
      self.TotalRFQCnt:int = obj["TotalRFQCnt"]
      """  The total count of rfqs for this buyer.  """  
      self.BuyerName:str = obj["BuyerName"]
      """  The buyer name.  """  
      self.DecisionDate:str = obj["DecisionDate"]
      """  The descision date  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date  """  
      self.CommentText:str = obj["CommentText"]
      """  Comment field for RFQHead when an RFQ Suggestion is generated into an RFQ.  Used in BuyerWorkbench.  """  
      self.PostToWeb:bool = obj["PostToWeb"]
      self.RespondDate:str = obj["RespondDate"]
      """  The respond date  """  
      self.TotalFuture:int = obj["TotalFuture"]
      """  Number of RFQs with a due date greater than the last day of the current week  """  
      self.TotalOverdue:int = obj["TotalOverdue"]
      """  Number of RFQs with a due date earlier than todays date  """  
      self.TotalReady:int = obj["TotalReady"]
      """  Number of RFQs that have received supplier responses and are ready to be turned into purchase orders  """  
      self.TotalThisWeek:int = obj["TotalThisWeek"]
      """  Number of RFQs with due date greater than today but less than the last day of the week  """  
      self.TotalToday:int = obj["TotalToday"]
      """  Number of RFQs with a due date of today  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Generate_input:
   """ Required : 
   ipBuyerID
   ds
   """  
   def __init__(self, obj):
      self.ipBuyerID:str = obj["ipBuyerID"]
      """  The buyer id to generate for.  """  
      self.ds:list[Erp_Tablesets_BuyerWorkbenchTableset] = obj["ds"]
      pass

class Generate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BuyerWorkbenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSuggSupp_input:
   """ Required : 
   ipBuyerID
   ipSugNum
   ds
   """  
   def __init__(self, obj):
      self.ipBuyerID:str = obj["ipBuyerID"]
      """  The buyer id to add data for.  """  
      self.ipSugNum:int = obj["ipSugNum"]
      """  The suggestion number to link suppliers to.  """  
      self.ds:list[Erp_Tablesets_BuyerWorkbenchTableset] = obj["ds"]
      pass

class GetNewSuggSupp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BuyerWorkbenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSugPOChgCount_input:
   """ Required : 
   buyerID
   """  
   def __init__(self, obj):
      self.buyerID:str = obj["buyerID"]
      """  buyerID  """  
      pass

class GetSugPOChgCount_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      """  Count  """  
      pass

class GetSugPoDtlCount_input:
   """ Required : 
   buyerID
   """  
   def __init__(self, obj):
      self.buyerID:str = obj["buyerID"]
      """  buyerID  """  
      pass

class GetSugPoDtlCount_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      """  Count  """  
      pass

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

class SelectAll_input:
   """ Required : 
   ipBuyerID
   ds
   """  
   def __init__(self, obj):
      self.ipBuyerID:str = obj["ipBuyerID"]
      """  The buyer id to select all for.  """  
      self.ds:list[Erp_Tablesets_BuyerWorkbenchTableset] = obj["ds"]
      pass

class SelectAll_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BuyerWorkbenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SupplierWizard_input:
   """ Required : 
   sugNum
   ipSoldPart
   ipPreviousRFQ
   ipPriceBreak
   ipComplianceList
   includeVendAttrList
   excludeVendAttrList
   ds
   """  
   def __init__(self, obj):
      self.sugNum:int = obj["sugNum"]
      """  Suggestion number the wizard is running for  """  
      self.ipSoldPart:bool = obj["ipSoldPart"]
      """  Suppliers have sold us this part?  """  
      self.ipPreviousRFQ:bool = obj["ipPreviousRFQ"]
      """  Suppliers have previously received an RFQ?  """  
      self.ipPriceBreak:bool = obj["ipPriceBreak"]
      """  Suppliers have provided price break information?  """  
      self.ipComplianceList:str = obj["ipComplianceList"]
      """  Compliance list  """  
      self.includeVendAttrList:str = obj["includeVendAttrList"]
      """  The include vendor attributes list  """  
      self.excludeVendAttrList:str = obj["excludeVendAttrList"]
      """  The exclude vendor attributes list  """  
      self.ds:list[Erp_Tablesets_BuyerWorkbenchTableset] = obj["ds"]
      pass

class SupplierWizard_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opStatusMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_BuyerWorkbenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

