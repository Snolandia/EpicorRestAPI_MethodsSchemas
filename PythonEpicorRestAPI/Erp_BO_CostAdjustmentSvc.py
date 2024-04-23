import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CostAdjustmentSvc
# Description: Cost Adjustment Business Object
        Business object which provides the fields needed by
        the UI for the Coswt Adjustment process.
       
        Provides a dataset containing the fields necessary
        to build multiple PartTran records.
       
        Lewis Batcher
        10-14-2003
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetCostAdjustment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCostAdjustment
   Description: Obtains the cost fields, part description, transaction date, cost method
and other fields for the Cost Adjustment UI.
   OperationID: GetCostAdjustment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCostAdjustment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCostAdjustment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCostAdjustmentRow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCostAdjustmentRow
   Description: Returns CostAdjustment with the cost fields, part description, transaction date, cost method
and other fields
   OperationID: GetCostAdjustmentRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCostAdjustmentRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCostAdjustmentRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCostAdjustmentMultiple(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCostAdjustmentMultiple
   Description: It accepts a list of Partnumber and builds a CostAdjustmentDataSet.
The CostAdjustmentDataSet contains the cost fields, part description, transaction date, cost method
and other fields for the Cost Adjustment UI.
   OperationID: GetCostAdjustmentMultiple
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCostAdjustmentMultiple_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCostAdjustmentMultiple_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFIFOCosts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFIFOCosts
   Description: Obtains the FIFO costs for a part which has a cost method of 'F'.
   OperationID: GetFIFOCosts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFIFOCosts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFIFOCosts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLotCosts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLotCosts
   Description: Obtains the lot costs for a part which has a cost method of 'T'.
   OperationID: GetLotCosts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLotCosts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLotCosts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCostAdjustment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCostAdjustment
   Description: This method creates a new CostAdjustmentDataSet row entry.
   OperationID: GetNewCostAdjustment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCostAdjustment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCostAdjustment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCostAdjustmentList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCostAdjustmentList
   Description: This method creates a new ttCostAdjustmentList row entry.
   OperationID: GetNewCostAdjustmentList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCostAdjustmentList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCostAdjustmentList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAvgMtlUnitCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAvgMtlUnitCost
   Description: Call this method when the user changes the Average Material Unit Cost.
   OperationID: OnChangeAvgMtlUnitCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAvgMtlUnitCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAvgMtlUnitCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFIFOMaterialCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFIFOMaterialCost
   Description: Call this method when the user changes the FIFO Material Unit Cost.
   OperationID: OnChangeFIFOMaterialCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFIFOMaterialCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFIFOMaterialCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeLastMtlUnitCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeLastMtlUnitCost
   Description: Call this method when the user changes the Last Material Unit Cost.
   OperationID: OnChangeLastMtlUnitCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeLastMtlUnitCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLastMtlUnitCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartNum
   Description: Call this method when the user enters a PartNum.
   OperationID: OnChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeStdMtlUnitCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeStdMtlUnitCost
   Description: Call this method when the user changes the Standard Material Unit Cost.
   OperationID: OnChangeStdMtlUnitCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeStdMtlUnitCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeStdMtlUnitCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreSetCostAdjustment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreSetCostAdjustment
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreSetCostAdjustment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreSetCostAdjustment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreSetCostAdjustment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetCostAdjustment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetCostAdjustment
   Description: This procedure validates the fields in the CostAdjustment dataset.
Then updates the costs in the Part record, PartLot (if applicable)
and creates the appropriate PartTran records.
   OperationID: SetCostAdjustment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetCostAdjustment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetCostAdjustment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetCostAdjustmentForWeb(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetCostAdjustmentForWeb
   Description: This procedure validates the fields in the CostAdjustment dataset.
Then updates the costs in the Part record, PartLot (if applicable)
and creates the appropriate PartTran records.
Specific for web (client) use.
   OperationID: SetCostAdjustmentForWeb
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetCostAdjustmentForWeb_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetCostAdjustmentForWeb_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetCostAdjustmentCommon(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetCostAdjustmentCommon
   Description: This procedure validates the fields in the CostAdjustment dataset.
Then updates the costs in the Part record, PartLot (if applicable)
and creates the appropriate PartTran records.
If plant, warehouse, qty parameters are set then use them instead of current warehouse values
   OperationID: SetCostAdjustmentCommon
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetCostAdjustmentCommon_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetCostAdjustmentCommon_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTranDocTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTranDocTypes
   OperationID: GetAvailTranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_CostAdjustmentListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.PartNum:str = obj["PartNum"]
      self.SearchWord:str = obj["SearchWord"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CostAdjustmentListTableset:
   def __init__(self, obj):
      self.CostAdjustmentList:list[Erp_Tablesets_CostAdjustmentListRow] = obj["CostAdjustmentList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CostAdjustmentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part description  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Cost Method  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction date  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot number  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Reason code  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.AvgMtlUnitCost:int = obj["AvgMtlUnitCost"]
      """  Average material unit cost  """  
      self.AvgLbrUnitCost:int = obj["AvgLbrUnitCost"]
      """  Average labor unit cost  """  
      self.AvgBurUnitCost:int = obj["AvgBurUnitCost"]
      """  Average burden unit cost  """  
      self.AvgSubUnitCost:int = obj["AvgSubUnitCost"]
      """  Average subcontract unit cost  """  
      self.AvgMatBurUnitCost:int = obj["AvgMatBurUnitCost"]
      """  Average material burden unit cost  """  
      self.AvgTotUnitCost:int = obj["AvgTotUnitCost"]
      """  Average total unit cost  """  
      self.LastMtlUnitCost:int = obj["LastMtlUnitCost"]
      """  Last material unit cost  """  
      self.LastLbrUnitCost:int = obj["LastLbrUnitCost"]
      """  Last labor unit cost  """  
      self.LastBurUnitCost:int = obj["LastBurUnitCost"]
      """  Last burden unit cost  """  
      self.LastSubUnitCost:int = obj["LastSubUnitCost"]
      """  Last subcontract unit cost  """  
      self.LastMatBurUnitCost:int = obj["LastMatBurUnitCost"]
      """  Last material burden unit cost  """  
      self.LastTotUnitCost:int = obj["LastTotUnitCost"]
      """  Last total unit cost  """  
      self.StdMtlUnitCost:int = obj["StdMtlUnitCost"]
      """  Standard material unit cost  """  
      self.StdLbrUnitCost:int = obj["StdLbrUnitCost"]
      """  Standard labor unit cost  """  
      self.StdBurUnitCost:int = obj["StdBurUnitCost"]
      """  Standard burden unit cost  """  
      self.StdSubUnitCost:int = obj["StdSubUnitCost"]
      """  Standard subcontract unit cost  """  
      self.StdMatBurUnitCost:int = obj["StdMatBurUnitCost"]
      """  Standard material burden unit cost  """  
      self.StdTotUnitCost:int = obj["StdTotUnitCost"]
      """  Standard total unit cost  """  
      self.OrigAvgMtlUnitCost:int = obj["OrigAvgMtlUnitCost"]
      """  Original average material unit cost  """  
      self.OrigAvgLbrUnitCost:int = obj["OrigAvgLbrUnitCost"]
      """  Original average labor unit cost  """  
      self.OrigAvgSubUnitCost:int = obj["OrigAvgSubUnitCost"]
      """  Original average subcontract unit cost  """  
      self.OrigAvgMatBurUnitCost:int = obj["OrigAvgMatBurUnitCost"]
      """  Original average material burden unit cost  """  
      self.OrigLastMtlUnitCost:int = obj["OrigLastMtlUnitCost"]
      """  Original last material unit cost  """  
      self.OrigLastLbrUnitCost:int = obj["OrigLastLbrUnitCost"]
      """  Original last labor unit cost  """  
      self.OrigLastBurUnitCost:int = obj["OrigLastBurUnitCost"]
      """  Original last burden unit cost  """  
      self.OrigLastSubUnitCost:int = obj["OrigLastSubUnitCost"]
      """  Original last subcontract unit cost  """  
      self.OrigLastMatBurUnitCost:int = obj["OrigLastMatBurUnitCost"]
      """  Original last material burden unit cost  """  
      self.OrigAvgBurUnitCost:int = obj["OrigAvgBurUnitCost"]
      """  Original average burden unit cost  """  
      self.OrigStdMtlUnitCost:int = obj["OrigStdMtlUnitCost"]
      """  Original standard material unit cost  """  
      self.OrigStdLbrUnitCost:int = obj["OrigStdLbrUnitCost"]
      """  Original standard labor unit cost  """  
      self.OrigStdBurUnitCost:int = obj["OrigStdBurUnitCost"]
      """  Original standard burden unit cost  """  
      self.OrigStdSubUnitCost:int = obj["OrigStdSubUnitCost"]
      """  Original standard subcontract unit cost  """  
      self.OrigStdMatBurUnitCost:int = obj["OrigStdMatBurUnitCost"]
      """  Original standard material burden unit cost  """  
      self.CostMethodDisplay:str = obj["CostMethodDisplay"]
      """  Cost method description  """  
      self.TransactionPosted:bool = obj["TransactionPosted"]
      self.DummyKeyField:int = obj["DummyKeyField"]
      """  Dummy field to make the records unique.  Required for providing multiple cost adjustment capabality for a part.  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.TrackLots:bool = obj["TrackLots"]
      self.FIFOBurdenCost:int = obj["FIFOBurdenCost"]
      """  FIFO Unit Burden Cost  """  
      self.FIFODate:str = obj["FIFODate"]
      """  This could be the transaction date or the system date at the time this FIFO cost record was created.  Depending on the setting at Company Configuration (XbSyst.UseTranDate).  """  
      self.FIFOLaborCost:int = obj["FIFOLaborCost"]
      """  FIFO Unit Labor Cost  """  
      self.FIFOMaterialCost:int = obj["FIFOMaterialCost"]
      """  FIFO Unit Material Cost  """  
      self.FIFOMtlBurCost:int = obj["FIFOMtlBurCost"]
      """  FIFO Unit Material Burden Cost  """  
      self.FIFOSeq:int = obj["FIFOSeq"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.FIFOSubContCost:int = obj["FIFOSubContCost"]
      """  FIFO Unit Subcontract Cost  """  
      self.FIFOTotalCost:int = obj["FIFOTotalCost"]
      """  FIFO Total Cost. FIFOBurdenCost + FIFOLaborCost + FIFOMaterialCost + FIFOMtlBurCost + FIFOSubContCost  """  
      self.CostID:str = obj["CostID"]
      self.OrigFIFOBurdenCost:int = obj["OrigFIFOBurdenCost"]
      """  Original FIFO burden unit cost  """  
      self.OrigFIFOLaborCost:int = obj["OrigFIFOLaborCost"]
      """  Original FIFO labor unit cost  """  
      self.OrigFIFOMaterialCost:int = obj["OrigFIFOMaterialCost"]
      """  Original FIFO material unit cost  """  
      self.OrigFIFOMtlBurCost:int = obj["OrigFIFOMtlBurCost"]
      """  Original FIFO material burden unit cost  """  
      self.OrigFIFOSubContCost:int = obj["OrigFIFOSubContCost"]
      """  Original FIFO subcontract unit cost  """  
      self.EnableFIFOCosts:bool = obj["EnableFIFOCosts"]
      """  Indicates if valid FIFO is found.  """  
      self.EnableLotCosts:bool = obj["EnableLotCosts"]
      """  Indicates if valid PartLot is found.  """  
      self.FIFOSubSeq:int = obj["FIFOSubSeq"]
      """  FIFO Subsequence  """  
      self.EnableFIFOLayers:bool = obj["EnableFIFOLayers"]
      """  Indicates if the logic for the FIFO Layers is enabled.  """  
      self.FIFOAvgBurUnitCost:int = obj["FIFOAvgBurUnitCost"]
      """  FIFO Average Burden Unit Cost  """  
      self.FIFOAvgLbrUnitCost:int = obj["FIFOAvgLbrUnitCost"]
      """  FIFO Average Labor Unit Cost  """  
      self.FIFOAvgMtlUnitCost:int = obj["FIFOAvgMtlUnitCost"]
      """  FIFO Average Material Unit Cost  """  
      self.FIFOAvgSubUnitCost:int = obj["FIFOAvgSubUnitCost"]
      """  FIFO Average Subcontract Unit Cost  """  
      self.FIFOAvgMatBurUnitCost:int = obj["FIFOAvgMatBurUnitCost"]
      """  FIFO Average Material Burden Unit Cost  """  
      self.FIFOAvgTotUnitCost:int = obj["FIFOAvgTotUnitCost"]
      """  FIFO Average Total Unit Cost  """  
      self.OrigFIFOAvgBurUnitCost:int = obj["OrigFIFOAvgBurUnitCost"]
      """  Original FIFO Average Burden Unit Cost  """  
      self.OrigFIFOAvgLbrUnitCost:int = obj["OrigFIFOAvgLbrUnitCost"]
      """  Original FIFO Average Labor Unit Cost  """  
      self.OrigFIFOAvgMtlUnitCost:int = obj["OrigFIFOAvgMtlUnitCost"]
      """  Original FIFO Average Material UInit Cost  """  
      self.OrigFIFOAvgSubUnitCost:int = obj["OrigFIFOAvgSubUnitCost"]
      """  Original FIFO Average Subcontract Unit Cost  """  
      self.OrigFIFOAvgMatBurUnitCost:int = obj["OrigFIFOAvgMatBurUnitCost"]
      """  Original FIFO Average Material Burden Unit Cost  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number assigned  """  
      self.VarTarget:str = obj["VarTarget"]
      """  VarTarget, used for PartTran creating in Actual Cost Allocation Post process (value ACA - Actual Cost Allocation)  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CostAdjustmentTableset:
   def __init__(self, obj):
      self.CostAdjustment:list[Erp_Tablesets_CostAdjustmentRow] = obj["CostAdjustment"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.listAvailTranDocTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetCostAdjustmentMultiple_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentListTableset] = obj["ds"]
      pass

class GetCostAdjustmentMultiple_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CostAdjustmentTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentListTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetCostAdjustmentRow_input:
   """ Required : 
   pcPartNumber
   applyDate
   """  
   def __init__(self, obj):
      self.pcPartNumber:str = obj["pcPartNumber"]
      """  The part number entered by the user..  """  
      self.applyDate:str = obj["applyDate"]
      """  Cost Adjustment Apply/Transaction Date  """  
      pass

class GetCostAdjustmentRow_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CostAdjustmentRow] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.hasError:bool = obj["hasError"]
      pass

      """  output parameters  """  

class GetCostAdjustment_input:
   """ Required : 
   pcPartNumber
   ds
   """  
   def __init__(self, obj):
      self.pcPartNumber:str = obj["pcPartNumber"]
      """  The part number entered by the user..  """  
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      pass

class GetCostAdjustment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetFIFOCosts_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      pass

class GetFIFOCosts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetLotCosts_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      pass

class GetLotCosts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCostAdjustmentList_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentListTableset] = obj["ds"]
      pass

class GetNewCostAdjustmentList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentListTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCostAdjustment_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      pass

class GetNewCostAdjustment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
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

class OnChangeAvgMtlUnitCost_input:
   """ Required : 
   dAvgMtlUnitCost
   ds
   """  
   def __init__(self, obj):
      self.dAvgMtlUnitCost:int = obj["dAvgMtlUnitCost"]
      """  The average material unit cost entered by the user..  """  
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      pass

class OnChangeAvgMtlUnitCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeFIFOMaterialCost_input:
   """ Required : 
   dFIFOMaterialCost
   ds
   """  
   def __init__(self, obj):
      self.dFIFOMaterialCost:int = obj["dFIFOMaterialCost"]
      """  The FIFO material unit cost entered by the user.  """  
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      pass

class OnChangeFIFOMaterialCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeLastMtlUnitCost_input:
   """ Required : 
   dLastMtlUnitCost
   ds
   """  
   def __init__(self, obj):
      self.dLastMtlUnitCost:int = obj["dLastMtlUnitCost"]
      """  The last material unit cost entered by the user..  """  
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      pass

class OnChangeLastMtlUnitCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePartNum_input:
   """ Required : 
   pcPartNumber
   ds
   """  
   def __init__(self, obj):
      self.pcPartNumber:str = obj["pcPartNumber"]
      """  The part number entered by the user..  """  
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      pass

class OnChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeStdMtlUnitCost_input:
   """ Required : 
   dStdMtlUnitCost
   ds
   """  
   def __init__(self, obj):
      self.dStdMtlUnitCost:int = obj["dStdMtlUnitCost"]
      """  The standard material unit cost entered by the user..  """  
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      pass

class OnChangeStdMtlUnitCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PreSetCostAdjustment_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      pass

class PreSetCostAdjustment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      pass

      """  output parameters  """  

class SetCostAdjustmentCommon_input:
   """ Required : 
   ds
   allowEmptyReason
   ipPlant
   ipWarehouseCode
   ipOnHandQty
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      self.allowEmptyReason:bool = obj["allowEmptyReason"]
      """  Allow Empty Reason for Cost Adjustment  """  
      self.ipPlant:str = obj["ipPlant"]
      """  plant  """  
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      """  warehouse  """  
      self.ipOnHandQty:int = obj["ipOnHandQty"]
      """  quantity  """  
      pass

class SetCostAdjustmentCommon_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      self.partTranPKs:str = obj["parameters"]
      self.hasError:bool = obj["hasError"]
      pass

      """  output parameters  """  

class SetCostAdjustmentForWeb_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      pass

class SetCostAdjustmentForWeb_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      self.partTranPKs:str = obj["parameters"]
      pass

      """  output parameters  """  

class SetCostAdjustment_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      pass

class SetCostAdjustment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CostAdjustmentTableset] = obj["ds"]
      self.partTranPKs:str = obj["parameters"]
      pass

      """  output parameters  """  

