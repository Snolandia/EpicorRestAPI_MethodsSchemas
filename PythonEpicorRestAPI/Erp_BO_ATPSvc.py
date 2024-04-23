import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ATPSvc
# Description: Part Tracker , Part Advisor -> Available to Promise screen.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_ForecastButtonHandler(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ForecastButtonHandler
   Description: Call this method from Forecast button of ATP screen.
   OperationID: ForecastButtonHandler
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ForecastButtonHandler_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ForecastButtonHandler_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePlantWithDS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePlantWithDS
   Description: Update the ATP table when changing Plants in Kinetic.
   OperationID: OnChangePlantWithDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePlantWithDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePlantWithDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeField(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeField
   Description: When the user changes the value of any field except Plant and Part call this method.
   OperationID: OnChangeField
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeField_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VerifyShortDescription(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VerifyShortDescription
   Description: Validate short description
   OperationID: VerifyShortDescription
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VerifyShortDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyShortDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePlant
   Description: When the user changes the Plant, call this method.
   OperationID: OnChangePlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProjectedReceipts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProjectedReceipts
   Description: Call this method from Receipts button of ATP screen.
   OperationID: ProjectedReceipts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProjectedReceipts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProjectedReceipts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProjectedReceiptsWithDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProjectedReceiptsWithDate
   Description: Call this method from Receipts button of ATP screen for Kinetic.
   OperationID: ProjectedReceiptsWithDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProjectedReceiptsWithDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProjectedReceiptsWithDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SalesOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SalesOrder
   Description: Call this method from Sales Order button of ATP screen.
   OperationID: SalesOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SalesOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SalesOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TransferOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TransferOrder
   Description: Call this method from Transfer Order button of ATP screen.
   OperationID: TransferOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TransferOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TransferOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_getPlanningAttributeSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method getPlanningAttributeSet
   Description: Get the planning attribute set for an attribute set
   OperationID: getPlanningAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getPlanningAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getPlanningAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindPlanningAttributeSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindPlanningAttributeSet
   OperationID: FindPlanningAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindPlanningAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPlanningAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateAttributeSetIDFromRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateAttributeSetIDFromRevisionNum
   Description: This method updates attributeSetID and planningAttributeSetSeq when new revision is selected.
   OperationID: UpdateAttributeSetIDFromRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateAttributeSetIDFromRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAttributeSetIDFromRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PartsAttributeClassHasRevisionAndIsMRPTracked(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PartsAttributeClassHasRevisionAndIsMRPTracked
   Description: This method updates attributeSetID and planningAttributeSetSeq when new revision is selected.
   OperationID: PartsAttributeClassHasRevisionAndIsMRPTracked
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartsAttributeClassHasRevisionAndIsMRPTracked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartsAttributeClassHasRevisionAndIsMRPTracked_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_HasMRPPlanningAttribute(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HasMRPPlanningAttribute
   Description: Return true if the Part has an MRP Planning Attribute, thus requiring an Attribute Set to be selected
   OperationID: HasMRPPlanningAttribute
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HasMRPPlanningAttribute_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HasMRPPlanningAttribute_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ATPSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_ATPForecastRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ForeDate:str = obj["ForeDate"]
      self.ForeQty:int = obj["ForeQty"]
      self.Name:str = obj["Name"]
      self.ConsumedQty:int = obj["ConsumedQty"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ATPForecastTableset:
   def __init__(self, obj):
      self.ATPForecast:list[Erp_Tablesets_ATPForecastRow] = obj["ATPForecast"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ATPOrderRelTableset:
   def __init__(self, obj):
      self.OrderRel:list[Erp_Tablesets_OrderRelRow] = obj["OrderRel"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ATPTFOrderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.NeedByDate:str = obj["NeedByDate"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.TFOrdLine:int = obj["TFOrdLine"]
      self.PartNum:str = obj["PartNum"]
      self.Quantity:int = obj["Quantity"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ATPTFOrderTableset:
   def __init__(self, obj):
      self.ATPTFOrder:list[Erp_Tablesets_ATPTFOrderRow] = obj["ATPTFOrder"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ATPTableset:
   def __init__(self, obj):
      self.AvailableToPromiseHead:list[Erp_Tablesets_AvailableToPromiseHeadRow] = obj["AvailableToPromiseHead"]
      self.AvailableToPromise:list[Erp_Tablesets_AvailableToPromiseRow] = obj["AvailableToPromise"]
      self.CustomATP:list[Erp_Tablesets_CustomATPRow] = obj["CustomATP"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_AvailableToPromiseHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.Plant:str = obj["Plant"]
      self.ATPMethod:str = obj["ATPMethod"]
      """  Available to method.  Valid values are "Q" and "D"  """  
      self.SellingATPQty:int = obj["SellingATPQty"]
      self.ATPDate:str = obj["ATPDate"]
      self.OurATPQty:int = obj["OurATPQty"]
      self.StartAtDate:str = obj["StartAtDate"]
      self.OnHandQty:int = obj["OnHandQty"]
      self.UMFactor:str = obj["UMFactor"]
      """  Radio set with valid values as "S" and "O"  """  
      self.DaysBefore:int = obj["DaysBefore"]
      self.DaysAfter:int = obj["DaysAfter"]
      self.PlantEnabled:bool = obj["PlantEnabled"]
      """  Set to No if it needs to be disabled in the UI.  """  
      self.LeadTime:int = obj["LeadTime"]
      """  Lead Time from the Part Plant record.  """  
      self.LeadDate:str = obj["LeadDate"]
      """  Calculated at Today + LeadTime.  """  
      self.ReceiveTime:int = obj["ReceiveTime"]
      """  ReceiveTime  """  
      self.SalesUOM:str = obj["SalesUOM"]
      self.OurUOM:str = obj["OurUOM"]
      self.OurUM:str = obj["OurUM"]
      self.SellUM:str = obj["SellUM"]
      self.EnableAttrSetSearch:bool = obj["EnableAttrSetSearch"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AvailableToPromiseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.Plant:str = obj["Plant"]
      self.DueDate:str = obj["DueDate"]
      self.ForeQty:int = obj["ForeQty"]
      self.OrderQty:int = obj["OrderQty"]
      self.ProdQty:int = obj["ProdQty"]
      self.MpsQty:int = obj["MpsQty"]
      self.RcvQty:int = obj["RcvQty"]
      self.ATPQty:int = obj["ATPQty"]
      """  Cumulative ATP Qty  """  
      self.ConsumedQty:int = obj["ConsumedQty"]
      self.TOrderQty:int = obj["TOrderQty"]
      self.sfForeQty:int = obj["sfForeQty"]
      """  Selling factor Forecast Qty  """  
      self.sfOrderQty:int = obj["sfOrderQty"]
      """  Selling Factor Order Qty  """  
      self.sfProdQty:int = obj["sfProdQty"]
      """  Selling Factor Prod Qty  """  
      self.sfMpsQty:int = obj["sfMpsQty"]
      """  Selling Factor MPS Qty  """  
      self.sfRcvQty:int = obj["sfRcvQty"]
      """  Selling Factor Recipt Qty  """  
      self.sfATPQty:int = obj["sfATPQty"]
      """  Selling Factor ATP Qty  """  
      self.sfConsumedQty:int = obj["sfConsumedQty"]
      """  Selling Factor Consumed Qty  """  
      self.sfTOrderQty:int = obj["sfTOrderQty"]
      self.DiscreteATPQty:int = obj["DiscreteATPQty"]
      """  DiscreteATPQty  """  
      self.sfDiscreteATPQty:int = obj["sfDiscreteATPQty"]
      """  Selling Factor Discrete ATP Qty  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustomATPRow:
   def __init__(self, obj):
      self.ATPQty:int = obj["ATPQty"]
      """  Cumulative ATP Qty  """  
      self.ForeQty:int = obj["ForeQty"]
      self.MpsQty:int = obj["MpsQty"]
      self.OrderQty:int = obj["OrderQty"]
      self.ProdQty:int = obj["ProdQty"]
      self.RowCaption:str = obj["RowCaption"]
      """  Caption for the row. Will show a date formatted as a string.  """  
      self.SalesQtyOurQty:str = obj["SalesQtyOurQty"]
      """  Radio set with valid values as "S" and "O". Taken from AvailableToPromiseHead.UMFactor.  """  
      self.sfATPQty:int = obj["sfATPQty"]
      """  Selling Factor ATP Qty  """  
      self.sfForeQty:int = obj["sfForeQty"]
      """  Selling factor Forecast Qty  """  
      self.sfMpsQty:int = obj["sfMpsQty"]
      """  Selling Factor MPS Qty  """  
      self.sfOrderQty:int = obj["sfOrderQty"]
      """  Selling Factor Order Qty  """  
      self.sfProdQty:int = obj["sfProdQty"]
      """  Selling Factor Prod Qty  """  
      self.sfTOrderQty:int = obj["sfTOrderQty"]
      self.TOrderQty:int = obj["TOrderQty"]
      self.DueDate:str = obj["DueDate"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OrderRelRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order Number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Sales order Line number that this order release is linked to.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.ReqDate:str = obj["ReqDate"]
      """  Date which the item needs to be shipped by in order to meet the customers due date. Initially defaulted as OrderHed.ReqDate.  """  
      self.OurReqQty:int = obj["OurReqQty"]
      """  Quantity ,using Our U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used for this scheduled release record. This MUST BE VALID IN THE SHIPTO file. Use the OrderHead.ShiptoNum as the default when creating new records.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Ship Via ID that is used for this shipment release. THIS CAN BE BLANK or MUST BE VALID IN THE SHIPVIA master file. Use the OrderHead.ShipViaCode as the default.  """  
      self.OpenRelease:bool = obj["OpenRelease"]
      """  Indicates if this release is open.  This is normally set to closed via the shipping program. But can be changed indirectly  by the user during order entry when they "Void" the release..  """  
      self.FirmRelease:bool = obj["FirmRelease"]
      """  Indicates if this release is  "FIRM". The opposite is an uncommitted release, that is when the customer gives releases that are just 'Best Guesses' of what they will require in the future, such as in blanket order situations. This type of  releases is no different to the system, except that the FirmRelease field will be printed on reports such as TimePhase requirements.  """  
      self.Make:bool = obj["Make"]
      """   Indicates if this requirement or any part of it will be manufactured. Default the setting to "No" if valid Part and the Part.Type is "S" or "P".

Default the setting to "Yes" if the part is not found in Part master or the Part.Type = "J".  This flag also gets set if this release gets linked to a Job via Job Entry. There is an Index on this field so that we can display releases that need have a job assigned to them. This display is part of Job Entry.  """  
      self.OurJobQty:int = obj["OurJobQty"]
      """  The planned production quantity, using Our U/M, for the Job. This is not maintainable in order entry. It gets updated via Job Entry.  """  
      self.OurJobShippedQty:int = obj["OurJobShippedQty"]
      """  Actual quantity, using our U/M, shipped from the Job.  Updated via the shipping process.  """  
      self.VoidRelease:bool = obj["VoidRelease"]
      """   Indicates if the release was voided. Voided releases items are not maintainable, can't "unvoid". This field is not directly maintainable. Instead the void function will be performed via a "Void Release" button. Which then presents a verification dialog box.

When an OrderRel record is 'voided' any outstanding inventory allocations are relieved, OrderRel.OpenRelease is set to "no" and records are created/updated in the OrdJobMsg file for all the related  open OrderRel records if the OrderDtl that was tied to a Job to indicate that the line item was voided.  """  
      self.OurStockQty:int = obj["OurStockQty"]
      """  Quantity, using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  """  
      self.OurStockShippedQty:int = obj["OurStockShippedQty"]
      """  Actual quantity, using our U/M, shipped from Stock.  Updated via the shipping process.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number the release quantity is currently allocated to (if it exists in the part master file).  This is a duplicate of the OrderDtl part number and is not user maintainable.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number.  Mirror image of OrderDtl.RevisionNum.  Not directly maintainable.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this customer/shipto  is exempt from sales tax for this line item. If field is non-blank it is considered exempt. Defaults from the Customer/Shipto file.  This code is totally user definable and no validation is required. This field will be printed on the Tax report if this item is reportable .  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Enter via a DDSL fill-in for contact name. Use OrderHed.ShpConNum when the OrderRel.ShipToNum = OrderHed.ShipToNum else use ShipTo.PrimScon as a default.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the item to be delivered. Defaulted as OrderHed.NeedByDate.  """  
      self.Reference:str = obj["Reference"]
      """  EDI Reference  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.SellingReqQty:int = obj["SellingReqQty"]
      """  Quantity ,using Selling U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  """  
      self.SellingJobQty:int = obj["SellingJobQty"]
      """  The planned production quantity, using selling U/M, for the Job. This is not maintainable in order entry. It gets updated via Job Entry.  """  
      self.SellingJobShippedQty:int = obj["SellingJobShippedQty"]
      """  Actual quantity, using selling U/M, shipped from the Job.  Updated via the shipping process.  """  
      self.SellingStockQty:int = obj["SellingStockQty"]
      """  Quantity, using selling U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  """  
      self.SellingStockShippedQty:int = obj["SellingStockShippedQty"]
      """  Actual quantity, using selling U/M, shipped from Stock.  Updated via the shipping process.  """  
      self.SelectForPicking:bool = obj["SelectForPicking"]
      """  Indicates if the release is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  """  
      self.StagingWarehouseCode:str = obj["StagingWarehouseCode"]
      """  The shipping "Staging" warehouse for the release.  Defaults from the system default shipping area (Site.DefShippingWhse). This is maintainable in the Sales Allocation program.  """  
      self.StagingBinNum:str = obj["StagingBinNum"]
      """  The shipping "Staging" bin for the release.  Defaults from the system default shipping area (Site.DefShippingBin). This is maintainable in the Sales Allocation program.  """  
      self.PickError:str = obj["PickError"]
      """   A non blank character indicates that the release could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  """  
      self.CumeQty:int = obj["CumeQty"]
      """  Quantity from last EDI update.  """  
      self.CumeDate:str = obj["CumeDate"]
      """  Date of last update  """  
      self.Linked:bool = obj["Linked"]
      """  Indicates if this order release is linked to an inter-company PO release.  """  
      self.ICPONum:int = obj["ICPONum"]
      """  Inter-Company Purchase order number  that the detail line item is linked to.  """  
      self.ICPOLine:int = obj["ICPOLine"]
      """  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.ICPORelNum:int = obj["ICPORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  A link to the demand schedule that created/updated this OrderRel.  """  
      self.MarkForNum:str = obj["MarkForNum"]
      """  The Mark For to be used for this order release record. This MUST BE VALID IN THE SHIPTO file.  """  
      self.DropShipName:str = obj["DropShipName"]
      """  Full name for the drop shipment.  """  
      self.RAN:str = obj["RAN"]
      """  RAN Number.  Used for informational purposes.  Supplied by EDI.  """  
      self.DemandReference:str = obj["DemandReference"]
      """  Demand Reference.  Used for informational purposes and to aide in matching demand schedules with existing OrderRel records.  Supplied by EDI.  """  
      self.DemandSchedRejected:bool = obj["DemandSchedRejected"]
      """  Indicates if the demand schedule that created/updated this order release has been rejected.  """  
      self.DatePickTicketPrinted:str = obj["DatePickTicketPrinted"]
      """  The last date that the Material Queue Report was run for this release.  This field will be null until the Material Queue Report is run.  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.VerbalConf:bool = obj["VerbalConf"]
      """  Verbal Confirmation required  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.ServSatDelivery:bool = obj["ServSatDelivery"]
      """  Is a Service Saturday delivery acceptable  """  
      self.ServSatPickup:bool = obj["ServSatPickup"]
      """  Is a Service Saturday pickup available  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServPOD:bool = obj["ServPOD"]
      """  Service Auto POD flag  """  
      self.ServAOD:bool = obj["ServAOD"]
      """  AOD  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      """  Override Carrier Defaults.  If not checked then the Site values will be used  """  
      self.OverrideService:bool = obj["OverrideService"]
      """  Override Service Options.  If not checked then the Site values will be used  """  
      self.DockingStation:str = obj["DockingStation"]
      """  The dockingstation of the shipto address.  For future use.  """  
      self.Location:str = obj["Location"]
      """  The location within the customer shipto address.  For future use.  """  
      self.TransportID:str = obj["TransportID"]
      """  The code of the transport routing/time. For future use.  """  
      self.ShipbyTime:int = obj["ShipbyTime"]
      """  Ship the good by this time.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, the OrderRelTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the release before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  Indicates that the One Time ShipTO information defined for this release should be used.  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipment country  """  
      self.SubShipTo:str = obj["SubShipTo"]
      """   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a store description.
Will be printed on the packing slip  """  
      self.ShipRouting:str = obj["ShipRouting"]
      """   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a routing description.
Will be printed on the packing slip  """  
      self.BuyToOrder:bool = obj["BuyToOrder"]
      """  This field identifies Buy To Order releases.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The value for this field will be defaulted from the Supplier defined in the Part Site sub tab at the Part form. Used only for Buy To Order releases.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Supplier Purchase Point. Used only for Buy To Order releases.  """  
      self.DropShip:bool = obj["DropShip"]
      """  This field identifies Drop Ship releases. Used only for Buy To Order releases.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order related to this Buy To Order release. Used only for Buy To Order releases.  """  
      self.POLine:int = obj["POLine"]
      """  The line number of the purchase order related to this Buy To Order release. Used only for Buy To Order releases.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  The release number of the purchase order line related to this Buy To Order release. Used only for Buy To Order releases.  """  
      self.OpenOrder:bool = obj["OpenOrder"]
      """  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  """  
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      """  Indicates if/how the OTS can be saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  """  
      self.OTSSaveCustID:str = obj["OTSSaveCustID"]
      """  CustID to be used if the OTS is used to create a customer record.  """  
      self.OTSCustSaved:bool = obj["OTSCustSaved"]
      """  True if Customer or ShipTo record was created using the OTS info.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.IUM:str = obj["IUM"]
      """   Unit of Measure that qualifies the "our" quantity fields.
If a valid part then it is the Base Stocking UOM (Part.IUM).
A mirror image of OrderDtl.IUM. Not directly maintainable  """  
      self.SalesUM:str = obj["SalesUM"]
      """   Selling Unit of measure. Qualifies the "Selling" quantity fields.
A mirror image of OrderDtl.SalesUM. Not directly maintainable.  """  
      self.RelStatus:str = obj["RelStatus"]
      """  Status of Order Release  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.PrevSellQty:int = obj["PrevSellQty"]
      """  Previous Selling Quantity  """  
      self.PrevPartNum:str = obj["PrevPartNum"]
      """  Previous Part Number  """  
      self.PrevXPartNum:str = obj["PrevXPartNum"]
      """  Previous Customer Part Number  """  
      self.PrevNeedByDate:str = obj["PrevNeedByDate"]
      """  Previous Need By Date  """  
      self.PrevReqDate:str = obj["PrevReqDate"]
      """  Previous Require Date  """  
      self.PrevShipToNum:str = obj["PrevShipToNum"]
      """  Previous Ship To Num  """  
      self.MFCustNum:int = obj["MFCustNum"]
      """  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  """  
      self.UseOTMF:bool = obj["UseOTMF"]
      """  Indicates that the One Time Mark For information defined for this record should be used.  """  
      self.OTMFName:str = obj["OTMFName"]
      """  One Time Mark For Name of the ShipTo.  """  
      self.OTMFAddress1:str = obj["OTMFAddress1"]
      """  One Time Mark For first line of the ShipTo address.  """  
      self.OTMFAddress2:str = obj["OTMFAddress2"]
      """  One Time Mark For second line of the ShipTo address.  """  
      self.OTMFAddress3:str = obj["OTMFAddress3"]
      """  One Time Mark For third line of the ShipTo address.  """  
      self.OTMFCity:str = obj["OTMFCity"]
      """  City portion of the One Time Mark For address.  """  
      self.OTMFState:str = obj["OTMFState"]
      """  The state or province portion of the One Time Mark For address.  """  
      self.OTMFZIP:str = obj["OTMFZIP"]
      """  The zip or postal code portion of the One Time Mark For address.  """  
      self.OTMFContact:str = obj["OTMFContact"]
      """  One Time Mark For Contact Name  """  
      self.OTMFFaxNum:str = obj["OTMFFaxNum"]
      """  Fax number for the One Time Mark For.  """  
      self.OTMFPhoneNum:str = obj["OTMFPhoneNum"]
      """  Phone number for the One Time Mark For  """  
      self.OTMFCountryNum:int = obj["OTMFCountryNum"]
      """  Country number for the One Time Mark For  """  
      self.ECCPlant:str = obj["ECCPlant"]
      """  ECCPlant  """  
      self.WIOrderLine:str = obj["WIOrderLine"]
      """  WIOrderLine  """  
      self.WIOrder:str = obj["WIOrder"]
      """  WIOrder  """  
      self.WebSKU:str = obj["WebSKU"]
      """  WebSKU  """  
      self.ShipOvers:bool = obj["ShipOvers"]
      """  ShipOvers  """  
      self.WIItemPrice:int = obj["WIItemPrice"]
      """  WIItemPrice  """  
      self.WIItemShipCost:int = obj["WIItemShipCost"]
      """  WIItemShipCost  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EntityUseCode:str = obj["EntityUseCode"]
      """  EntityUseCode  """  
      self.PhaseID:str = obj["PhaseID"]
      """  PhaseID  """  
      self.OTSShipToNum:str = obj["OTSShipToNum"]
      """  OTSShipToNum  """  
      self.WasRecInvoiced:bool = obj["WasRecInvoiced"]
      """  WasRecInvoiced  """  
      self.ContractID:str = obj["ContractID"]
      """  The identifier of the planning contract.  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the sales order release is ready to be fulfilled.  """  
      self.OTSEMailAddress:str = obj["OTSEMailAddress"]
      """  One Time ShipTo email address.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.NumberOfPiecesUOM:str = obj["NumberOfPiecesUOM"]
      """  Unit of measure for the NumberOfPieces.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.PartAllocQueueAction:str = obj["PartAllocQueueAction"]
      """  Indicates if the release should be added or removed from the fulfillment queue.  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.AvailableQuantity:int = obj["AvailableQuantity"]
      self.BuyOverride:bool = obj["BuyOverride"]
      """  BuyOverride  """  
      self.CreditLimitMessage:str = obj["CreditLimitMessage"]
      """  The message returned when checking a customer credit limit.  """  
      self.CreditLimitSource:str = obj["CreditLimitSource"]
      """  The source that put the customer on credit hold.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CustAllowOTS:bool = obj["CustAllowOTS"]
      """  Is OTS allowed by the Sold to Customer?  """  
      self.CustomerAllowShipTo3:bool = obj["CustomerAllowShipTo3"]
      """  True when Customer allows shipping to a Third-Party  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.DisablePlantWhse:bool = obj["DisablePlantWhse"]
      self.DocSelfAssessTax:int = obj["DocSelfAssessTax"]
      self.DocTotalTax:int = obj["DocTotalTax"]
      self.DocWithholdTax:int = obj["DocWithholdTax"]
      self.DropShipOverride:bool = obj["DropShipOverride"]
      """  DropShipOverride  """  
      self.DspInvMeth:str = obj["DspInvMeth"]
      """   Invoicing Method. If advanced billing is not licensed the only options are CS and MB. Code/Desc: CS = Customer Shipment, MB = Milestone Billing, PB = Progress Billing, TM = Time and aterials
'CP' = Cost Plus
The default is Customer Shipment.  """  
      self.DspRevMethod:str = obj["DspRevMethod"]
      """  Revenue Recognition Method has system list of the following options: LBR = Labor Booking Recognition, MAN = Manual Recognition, BDN = Actual Burden Recognition, PCC = POC-Cost-to-Cost, PCE = POC-Efforts, PCU = POC-Units-of-Delivery  """  
      self.EnableBuyToOrder:bool = obj["EnableBuyToOrder"]
      self.EnableMake:bool = obj["EnableMake"]
      self.EntryProcess:str = obj["EntryProcess"]
      """  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  """  
      self.ExistPOSugg:bool = obj["ExistPOSugg"]
      """  ExistPOSugg, external field to show/hide an epishape  """  
      self.HdrOTS:bool = obj["HdrOTS"]
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  Inventory UOM that the Order Release is allocated against. It is the similare column to the OrderDtl InvtyUOM and should always has the same value as in OrderDtl  """  
      self.KitDisable:bool = obj["KitDisable"]
      """  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  """  
      self.LinkToPONum:bool = obj["LinkToPONum"]
      """  LinkToPONum, external field to show/hide an epishape  """  
      self.MakeOverride:bool = obj["MakeOverride"]
      self.MarkForAddrFormatted:str = obj["MarkForAddrFormatted"]
      """  The formatted mark for address  """  
      self.MarkForAddrList:str = obj["MarkForAddrList"]
      """  Contains the Mark For Address  """  
      self.MFCustID:str = obj["MFCustID"]
      self.NoRelTaxRgnChange:bool = obj["NoRelTaxRgnChange"]
      """  The flag based on the user anwer if Ship To of the release is supposed be changed but Tax info is not changed because of the conflict in tax pricing  """  
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  """  
      self.OnHandQuantity:int = obj["OnHandQuantity"]
      self.OTSSaved:bool = obj["OTSSaved"]
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  OTS Tax Liability Code (Order Release)  """  
      self.PartExists:bool = obj["PartExists"]
      self.PhaseWasRecInvoiced:bool = obj["PhaseWasRecInvoiced"]
      """  If the phase has been recognized or invoiced.  """  
      self.ProjectID:str = obj["ProjectID"]
      self.ReleaseStatus:str = obj["ReleaseStatus"]
      self.RemoveManAdTax:bool = obj["RemoveManAdTax"]
      """  the flag to indicate if all previously creaded manually added and manual tax relcords related to Order line release should be deleted if the user populates Tax Exempt field.  """  
      self.Rpt1SelfAssessTax:int = obj["Rpt1SelfAssessTax"]
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      self.Rpt1WithholdTax:int = obj["Rpt1WithholdTax"]
      self.Rpt2SelfAssessTax:int = obj["Rpt2SelfAssessTax"]
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      self.Rpt2WithholdTax:int = obj["Rpt2WithholdTax"]
      self.Rpt3SelfAssessTax:int = obj["Rpt3SelfAssessTax"]
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      self.Rpt3WithholdTax:int = obj["Rpt3WithholdTax"]
      self.SalesOrderLinked:bool = obj["SalesOrderLinked"]
      """  SalesOrderLinked  """  
      self.SelfAssessTax:int = obj["SelfAssessTax"]
      """  Self-Assessed Tax  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """  Selling Factor for display only  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Selling Factor Direction for display oly  """  
      self.ShipToAddressFormatted:str = obj["ShipToAddressFormatted"]
      """  The formatted ship to address  """  
      self.ShipToAddressList:str = obj["ShipToAddressList"]
      self.ShipToContactEMailAddress:str = obj["ShipToContactEMailAddress"]
      self.ShipToContactName:str = obj["ShipToContactName"]
      self.ShipToSelected:bool = obj["ShipToSelected"]
      self.SNEnable:bool = obj["SNEnable"]
      self.ThisRelInvtyQty:int = obj["ThisRelInvtyQty"]
      self.TotalJobStockShipped:int = obj["TotalJobStockShipped"]
      self.TotalTax:int = obj["TotalTax"]
      """  Invoice Tax  """  
      self.UpdateMarkForRecords:bool = obj["UpdateMarkForRecords"]
      self.VoidOrder:bool = obj["VoidOrder"]
      self.WithholdTax:int = obj["WithholdTax"]
      """  Withholding Tax  """  
      self.AllowTaxCodeUpd:bool = obj["AllowTaxCodeUpd"]
      self.EnableDynAttrButton:bool = obj["EnableDynAttrButton"]
      """  Allow enable/disable for the button Attibutes in Order Release  """  
      self.AttributeMismatch:bool = obj["AttributeMismatch"]
      """  Attribute class is MRP Planned but AttributeSetID has not been set on release.  """  
      self.AllocatedQuantity:int = obj["AllocatedQuantity"]
      """  The total allocated quantity for this release.  """  
      self.ErrorStatusDisplay:str = obj["ErrorStatusDisplay"]
      """  Error Status Display  """  
      self.InPartAllocQueue:bool = obj["InPartAllocQueue"]
      """  True if this release is in the fulfillment queue.  """  
      self.ShowAllocationQueueActions:bool = obj["ShowAllocationQueueActions"]
      """  Show Fulfillment Queue Actions  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.MarkForNumInactive:bool = obj["MarkForNumInactive"]
      self.MFCustNumInactive:bool = obj["MFCustNumInactive"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OTMFCountryDescription:str = obj["OTMFCountryDescription"]
      self.OTSCntryISOCode:str = obj["OTSCntryISOCode"]
      self.OTSCntryEUMember:bool = obj["OTSCntryEUMember"]
      self.OTSCntryDescription:str = obj["OTSCntryDescription"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PlantName:str = obj["PlantName"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.TPShipToName:str = obj["TPShipToName"]
      self.TPShipToBTName:str = obj["TPShipToBTName"]
      self.TPShipToCustID:str = obj["TPShipToCustID"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProjectedReceiptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.Plant:str = obj["Plant"]
      self.DueDate:str = obj["DueDate"]
      self.Type:str = obj["Type"]
      self.Source:str = obj["Source"]
      self.ReceivedQty:int = obj["ReceivedQty"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.PONum:int = obj["PONum"]
      self.POLine:int = obj["POLine"]
      self.PORelNum:int = obj["PORelNum"]
      self.ReqDueDate:str = obj["ReqDueDate"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProjectedReceiptsTableset:
   def __init__(self, obj):
      self.ProjectedReceipts:list[Erp_Tablesets_ProjectedReceiptsRow] = obj["ProjectedReceipts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FindPlanningAttributeSet_input:
   """ Required : 
   partNum
   attributeSetID
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.attributeSetID:int = obj["attributeSetID"]
      pass

class FindPlanningAttributeSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.attributeSetShortDesc:str = obj["parameters"]
      self.attributeSetDesc:str = obj["parameters"]
      self.newAttributeSetID:int = obj["parameters"]
      pass

      """  output parameters  """  

class ForecastButtonHandler_input:
   """ Required : 
   pcPartNum
   pcPlant
   pdtStartDate
   attributeSetID
   """  
   def __init__(self, obj):
      self.pcPartNum:str = obj["pcPartNum"]
      """  Part number.  """  
      self.pcPlant:str = obj["pcPlant"]
      """  Plant  """  
      self.pdtStartDate:str = obj["pdtStartDate"]
      """  Start Date  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  Attribute Set ID  """  
      pass

class ForecastButtonHandler_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ATPForecastTableset] = obj["returnObj"]
      pass

class HasMRPPlanningAttribute_input:
   """ Required : 
   partNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part  """  
      pass

class HasMRPPlanningAttribute_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
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

class OnChangeField_input:
   """ Required : 
   pcFieldName
   pcPartNum
   pcPlant
   ds
   """  
   def __init__(self, obj):
      self.pcFieldName:str = obj["pcFieldName"]
      """  Field name from where this method is called.  """  
      self.pcPartNum:str = obj["pcPartNum"]
      """  Part number.  """  
      self.pcPlant:str = obj["pcPlant"]
      """  Plant  """  
      self.ds:list[Erp_Tablesets_ATPTableset] = obj["ds"]
      pass

class OnChangeField_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcRowIdent:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ATPTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePlantWithDS_input:
   """ Required : 
   partNum
   plant
   attributeSetID
   ds
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.plant:str = obj["plant"]
      self.attributeSetID:int = obj["attributeSetID"]
      self.ds:list[Erp_Tablesets_ATPTableset] = obj["ds"]
      pass

class OnChangePlantWithDS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.startAtDate:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ATPTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePlant_input:
   """ Required : 
   pcPartNum
   pcPlant
   attributeSetID
   """  
   def __init__(self, obj):
      self.pcPartNum:str = obj["pcPartNum"]
      """  Part number.  """  
      self.pcPlant:str = obj["pcPlant"]
      """  Plant  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  AttributeSetID  """  
      pass

class OnChangePlant_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ATPTableset] = obj["returnObj"]
      pass

class PartsAttributeClassHasRevisionAndIsMRPTracked_input:
   """ Required : 
   attrClassID
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      """  current Attribute Class ID  """  
      pass

class PartsAttributeClassHasRevisionAndIsMRPTracked_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ProjectedReceiptsWithDate_input:
   """ Required : 
   pcPartNum
   pcPlant
   pdtStartDate
   """  
   def __init__(self, obj):
      self.pcPartNum:str = obj["pcPartNum"]
      """  Part number.  """  
      self.pcPlant:str = obj["pcPlant"]
      """  Plant  """  
      self.pdtStartDate:str = obj["pdtStartDate"]
      pass

class ProjectedReceiptsWithDate_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ProjectedReceiptsTableset] = obj["returnObj"]
      pass

class ProjectedReceipts_input:
   """ Required : 
   pcPartNum
   pcPlant
   attributeSetID
   """  
   def __init__(self, obj):
      self.pcPartNum:str = obj["pcPartNum"]
      """  Part number.  """  
      self.pcPlant:str = obj["pcPlant"]
      """  Plant  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  Attribute Set ID  """  
      pass

class ProjectedReceipts_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ProjectedReceiptsTableset] = obj["returnObj"]
      pass

class SalesOrder_input:
   """ Required : 
   pcPartNum
   pcPlant
   pdtStartDate
   attributeSetID
   """  
   def __init__(self, obj):
      self.pcPartNum:str = obj["pcPartNum"]
      """  Part number.  """  
      self.pcPlant:str = obj["pcPlant"]
      """  Plant  """  
      self.pdtStartDate:str = obj["pdtStartDate"]
      """  Start Date  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  Attribute Set ID  """  
      pass

class SalesOrder_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ATPOrderRelTableset] = obj["returnObj"]
      pass

class TransferOrder_input:
   """ Required : 
   pcPartNum
   pcPlant
   pdtStartDate
   attributeSetID
   """  
   def __init__(self, obj):
      self.pcPartNum:str = obj["pcPartNum"]
      """  Part number.  """  
      self.pcPlant:str = obj["pcPlant"]
      """  Plant  """  
      self.pdtStartDate:str = obj["pdtStartDate"]
      """  Start Date  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  Attribute Set ID  """  
      pass

class TransferOrder_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ATPTFOrderTableset] = obj["returnObj"]
      pass

class UpdateAttributeSetIDFromRevisionNum_input:
   """ Required : 
   partNum
   revisionNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  current part number  """  
      self.revisionNum:str = obj["revisionNum"]
      """  new revision selected  """  
      pass

class UpdateAttributeSetIDFromRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.attributeSetID:int = obj["parameters"]
      pass

      """  output parameters  """  

class VerifyShortDescription_input:
   """ Required : 
   attrClassID
   shortAttrdesc
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.shortAttrdesc:str = obj["shortAttrdesc"]
      pass

class VerifyShortDescription_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.attributeSetID:int = obj["parameters"]
      self.longDescription:str = obj["parameters"]
      pass

      """  output parameters  """  

class getPlanningAttributeSet_input:
   """ Required : 
   attributeSetID
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      """  Attribute Set ID  """  
      pass

class getPlanningAttributeSet_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

