import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.RFQDecisionWizardSvc
# Description: The Decision Wizard from Buyer Workbench.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQDecisionWizardSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQDecisionWizardSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_Accept(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Accept
   Description: This method will do the following (text from 6.1 procedure):
Find Related JobMtl/JobOper/QuoteMtl/QuoteOpr (must be avail), and update estunitcost.
Note, if related to Job, the JobMtl write trigger was changed to fire off and create a POSuggestion -
like it should have done when you marked it "Purchase/direct" but we changed it so that if you flag
RFQNeeded also, would create an RFQSuggestion INSTEAD of a POSuggestion.
Once the RFQ has been created and vendor responds, the trigger will create a POSuggestion.
Set rest of vendor responses for this rfq to status = NO,
close rfqLine/item
   OperationID: Accept
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Accept_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Accept_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQDecisionWizardSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Apply(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Apply
   Description: This method will create the RFQReadyVend records associated with the RFQFilterDW
record and the selected filter and sort options.
   OperationID: Apply
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Apply_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Apply_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQDecisionWizardSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBeforeCreatePO(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBeforeCreatePO
   Description: Asks user before create the PO for a Quoted Item
   OperationID: CheckBeforeCreatePO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBeforeCreatePO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBeforeCreatePO_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQDecisionWizardSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreatePO(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreatePO
   Description: This method create the purchase order for this rfqitem.
   OperationID: CreatePO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreatePO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreatePO_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQDecisionWizardSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetHeaderRecord(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetHeaderRecord
   Description: This method will create a RFQFilterDW record with information from the RFQ and
populate the attributes to include/exclude and sort options.  The record created
here will then be used for the Apply method to generate the RFQReadyVend records.
Run this as the first method.
   OperationID: GetHeaderRecord
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetHeaderRecord_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHeaderRecord_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQDecisionWizardSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLineQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLineQty
   Description: This method gets the Job Qty (if job related) and sets a flag to tell the UI
to update the Qty, duedate and promise date fields.
Run this before CreatePO.
   OperationID: GetLineQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLineQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLineQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQDecisionWizardSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreAccept(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreAccept
   Description: This method will potentially produce a message that will provide the user with
a choice of continuing with the Accept.  Call this before the Accept method and
then pass into the Accept method the logical choice from the user's response
to the potential message from this method.
   OperationID: PreAccept
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreAccept_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreAccept_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQDecisionWizardSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Accept_input:
   """ Required : 
   ipRFQNum
   ipRFQLine
   ipVendorNum
   ipPurPoint
   ipAnswer
   ds
   """  
   def __init__(self, obj):
      self.ipRFQNum:int = obj["ipRFQNum"]
      """  The rfq number to accept for.  """  
      self.ipRFQLine:int = obj["ipRFQLine"]
      """  The rfq line number to accept for.  """  
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  The vendor num to accept for.  """  
      self.ipPurPoint:str = obj["ipPurPoint"]
      """  The purchase point to accept for.  """  
      self.ipAnswer:bool = obj["ipAnswer"]
      """  The user answer to PreAccept potential message.  """  
      self.ds:list[Erp_Tablesets_RFQDecisionWizardTableset] = obj["ds"]
      pass

class Accept_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQDecisionWizardTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Apply_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQDecisionWizardTableset] = obj["ds"]
      pass

class Apply_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQDecisionWizardTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckBeforeCreatePO_input:
   """ Required : 
   iQuoteNum
   """  
   def __init__(self, obj):
      self.iQuoteNum:int = obj["iQuoteNum"]
      """  Quote Number on RFQItem. Can be zero  """  
      pass

class CheckBeforeCreatePO_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.oMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CreatePO_input:
   """ Required : 
   ipRFQNum
   ipRFQLine
   ipVendorNum
   ipPurPoint
   ipLineQty
   ipDueDate
   ipPromiseDate
   ds
   """  
   def __init__(self, obj):
      self.ipRFQNum:int = obj["ipRFQNum"]
      """  The rfq number to create po for.  """  
      self.ipRFQLine:int = obj["ipRFQLine"]
      """  The rfq line number to create po for.  """  
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  The vendor num to create po for.  """  
      self.ipPurPoint:str = obj["ipPurPoint"]
      """  The purchase point to create po for.  """  
      self.ipLineQty:int = obj["ipLineQty"]
      """  The line quantity.  """  
      self.ipDueDate:str = obj["ipDueDate"]
      """  The due date.  """  
      self.ipPromiseDate:str = obj["ipPromiseDate"]
      """  The promise date.  """  
      self.ds:list[Erp_Tablesets_RFQDecisionWizardTableset] = obj["ds"]
      pass

class CreatePO_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opStatusMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_RFQDecisionWizardTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_RFQDecisionWizardTableset:
   def __init__(self, obj):
      self.RFQFilterDW:list[Erp_Tablesets_RFQFilterDWRow] = obj["RFQFilterDW"]
      self.RFQReadyVend:list[Erp_Tablesets_RFQReadyVendRow] = obj["RFQReadyVend"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RFQFilterDWRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company identifier.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  The rfq number.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The rfq line number.  """  
      self.AttributeList:str = obj["AttributeList"]
      """  The attribute list of options to include or exclude.  """  
      self.IncludeList:str = obj["IncludeList"]
      """  The list of attributes to include.  """  
      self.ExcludeList:str = obj["ExcludeList"]
      """  The list of attributes to exclude.  """  
      self.Quantity:int = obj["Quantity"]
      """  The quantity field.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  The required quantity.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description for the part number.  """  
      self.AvailSortChoices:str = obj["AvailSortChoices"]
      """  The list of available sort choices.  """  
      self.SelectedSortChoices:str = obj["SelectedSortChoices"]
      """  The selected sort choices.  """  
      self.ComplianceList:str = obj["ComplianceList"]
      """  Compliance List that Vendor must accomplish in order to be retrieved  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  OUR revision number of the OUR part.  An optional field. Defaults from the most current PartRev.RevisionNum.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQReadyVendRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company identifier.  """  
      self.VendorID:str = obj["VendorID"]
      """  The vendor id.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The vendor number.  """  
      self.OnTimeRating:str = obj["OnTimeRating"]
      """  The on time rating.  """  
      self.VendName:str = obj["VendName"]
      """  The vendor name  """  
      self.ServiceRating:str = obj["ServiceRating"]
      """  The service rating.  """  
      self.PriceRating:str = obj["PriceRating"]
      """  Freeform field for rating Price Accuracy.  This field is used as a criteria in selecting vendors in RFQ responses  """  
      self.QualityRating:str = obj["QualityRating"]
      """  The quality rating.  """  
      self.LeadTime:int = obj["LeadTime"]
      """  The lead time.  """  
      self.BreakQty:int = obj["BreakQty"]
      """  The break quantity.  """  
      self.Price:int = obj["Price"]
      """  The price.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  The on hand quantity.  """  
      self.OnHandDate:str = obj["OnHandDate"]
      """  The on hand date.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The purchase point.  """  
      self.Response:str = obj["Response"]
      """  The response.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  The rfq number.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The rfq line number.  """  
      self.EnableCreatePO:bool = obj["EnableCreatePO"]
      """  Enable Create PO button?  """  
      self.EnableAccept:bool = obj["EnableAccept"]
      """  Enable Accept button?  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetHeaderRecord_input:
   """ Required : 
   ipRFQNum
   ipRFQLine
   """  
   def __init__(self, obj):
      self.ipRFQNum:int = obj["ipRFQNum"]
      """  The rfq number to get data for.  """  
      self.ipRFQLine:int = obj["ipRFQLine"]
      """  The rfq line number to get data for.  """  
      pass

class GetHeaderRecord_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RFQDecisionWizardTableset] = obj["returnObj"]
      pass

class GetLineQty_input:
   """ Required : 
   ipRFQNum
   ipRFQLine
   ipVendorNum
   ipPurPoint
   """  
   def __init__(self, obj):
      self.ipRFQNum:int = obj["ipRFQNum"]
      """  RFQ Number  """  
      self.ipRFQLine:int = obj["ipRFQLine"]
      """  RFQ Line Number  """  
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  Vendor Number  """  
      self.ipPurPoint:str = obj["ipPurPoint"]
      """  Vendor Purchase Point  """  
      pass

class GetLineQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opTmpLineQty:str = obj["parameters"]
      self.opPromptQty:bool = obj["opPromptQty"]
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

class PreAccept_input:
   """ Required : 
   ipRFQNum
   ipRFQLine
   ipVendorNum
   ipPurPoint
   """  
   def __init__(self, obj):
      self.ipRFQNum:int = obj["ipRFQNum"]
      """  The rfq number to validate for.  """  
      self.ipRFQLine:int = obj["ipRFQLine"]
      """  The rfq line number to validate for.  """  
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  The vendor num to validate for.  """  
      self.ipPurPoint:str = obj["ipPurPoint"]
      """  The purchase point to validate for.  """  
      pass

class PreAccept_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opStatusMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

