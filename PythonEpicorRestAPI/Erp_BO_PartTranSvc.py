import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PartTranSvc
# Description: Part activity transactions. This includes issues, PO receipts, Mfg receipts, Adjustments,
Transfers, Physical count adjustments, Cost replace. These are for all parts regardless
of being defined in the part master file.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PartTrans(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartTrans
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/PartTrans",headers=creds) as resp:
           return await resp.json()

async def post_PartTrans(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/PartTrans", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PartTrans_Company_SysDate_SysTime_TranNum(Company, SysDate, SysTime, TranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartTran item
   Description: Calls GetByID to retrieve the PartTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SysDate: Desc: SysDate   Required: True   Allow empty value : True
      :param SysTime: Desc: SysTime   Required: True
      :param TranNum: Desc: TranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/PartTrans(" + Company + "," + SysDate + "," + SysTime + "," + TranNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PartTrans_Company_SysDate_SysTime_TranNum(Company, SysDate, SysTime, TranNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PartTran for the service
   Description: Calls UpdateExt to update PartTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SysDate: Desc: SysDate   Required: True   Allow empty value : True
      :param SysTime: Desc: SysTime   Required: True
      :param TranNum: Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/PartTrans(" + Company + "," + SysDate + "," + SysTime + "," + TranNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PartTrans_Company_SysDate_SysTime_TranNum(Company, SysDate, SysTime, TranNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PartTran item
   Description: Call UpdateExt to delete PartTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SysDate: Desc: SysDate   Required: True   Allow empty value : True
      :param SysTime: Desc: SysTime   Required: True
      :param TranNum: Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/PartTrans(" + Company + "," + SysDate + "," + SysTime + "," + TranNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartTranListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePartTran, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePartTran=" + whereClausePartTran
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(sysDate, sysTime, tranNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "sysDate=" + sysDate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "sysTime=" + sysTime
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "tranNum=" + tranNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetWhereClause(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetWhereClause
   Description: Get Where Clause for transaction log based on Mode
   OperationID: GetWhereClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartTran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartTranListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartTranRow] = obj["value"]
      pass

class Erp_Tablesets_PartTranListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.TranNum:int = obj["TranNum"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transaction is for.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.TranClass:str = obj["TranClass"]
      """   Transaction Class...A-adjustment, D-DMR, I-issue, R-receipt, S-Shipment X-Job Adjustment. A character field which classifies PartTran records.  This is a higher level of classification of the TransType field. Their relationships are;
 R = DMR-STK, INS-MTL, INS-STK, INS-SUB, MFG-PLT, MFG-STK, MFG-WIP, PLT-STK, PUR-INS, PUR-MTL, PUR-STK, PUR-SUB, PUR-UKN, RMA-INS, STK-DMR, SVG-STK
I = ASM-INS, INS-ASM, INS-REJ, MTL-INS, PLT-ASM, PLT-MTL, STK-ASM, STK-INS, STK-MTL, STK-SRV, STK-UKN, SUB-DMR, SUB-INS,WIP-MFG
A = ADJ-CST, ADJ-PUR, ADJ-QTY, MFG-VAR, STK-PLT, STK-STK
S = MFG-CUS, MFG-VEN, STK-CUS
D = DMR-MTL, DMR-REJ, DMR-SUB, INS-DMR, MTL-DMR
X = ADJ-MTL, ADJ-SUB
Intended to  be used for record selection purposes.  """  
      self.TranType:str = obj["TranType"]
      """   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  """  
      self.InventoryTrans:bool = obj["InventoryTrans"]
      """  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  """  
      self.TranDate:str = obj["TranDate"]
      """  date of transaction.  """  
      self.TranQty:int = obj["TranQty"]
      """   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  (part primary inventory uom)  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.ExtCost:int = obj["ExtCost"]
      """   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the Part.CostMethod.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that transaction is associated with.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence #  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl),  "S" = SubContract Operation (JobOper) or "O" = Inside Operation(JobOper)
(FYI: Non-Coformance/Inspection transactions, ASM-INS, INS-ASM, INS-DMR, DMR-ASM are the only ones which create "O" types  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.PackType:str = obj["PackType"]
      """  Indicates the type of Packing Slip... "C" = Customer (related to ShipDtl), "M" = Miscellaneous(MscShpDt),  "S" = Subcontractor (SubShipd) "TO" = (Transfer Order). This field, used along with PackNum/PackLine can be used to find the related shipping document record.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number.  """  
      self.PackLine:int = obj["PackLine"]
      """   The packing slip line # that this transaction is linked to.
Note: This field is used for both  a shipment to customer packing slip  or a receipt from vendor packing slip.  """  
      self.PONum:int = obj["PONum"]
      """  Created by Purchase Order Receipt Process.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of detail record on the purchase order.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # of the POSched record that this transaction is for.  """  
      self.WareHouse2:str = obj["WareHouse2"]
      """  Transfer "From/To" warehouse code. This is used for the warehouse transfer transactions. For the Issue side of the transaction it identifies the "transfer to" warehouse. For the receipt side of the transaction it identifies the "transfer from" warehouse.  """  
      self.BinNum2:str = obj["BinNum2"]
      """  This value only exists for the warehouse transaction. TranSrc = "4".  For the Issue side of the transaction it identifies the Bin location that the quantity is transferred in to. On the Receipt side of the transaction it identifies the Bin location that the quantity was transferred from.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The sales order line that this transaction is associated with.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.TranReference:str = obj["TranReference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part, JobOPer, JobMtl, ShipDtl,  SubShipD ....  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that along with PurPoint is used to tie back to the VendorPP master file. Applicable for shipments to subcontractors (MFG-VEN) and receipts (PUR-STK, PUR-MTL, PUR-SUB, PUR-UKN).  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor purchase point ID. (see VendorNum)  """  
      self.POReceiptQty:int = obj["POReceiptQty"]
      """  Quantity received against a purchase order in the vendors unit of measure.  """  
      self.POUnitCost:int = obj["POUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the PO detail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the MtlUnitCost field which is used as cost to job or stock.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvHed record. Applicable only with the purchase variance adjustment record (TranType = "ADJ-PUR") generated via A/P invoice posting.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Used along with InvoiceNum to relate to the corresponding APInvDtl record that generated this PartTran record. (see PartTran.InvoiceNum)  """  
      self.InvAdjSrc:str = obj["InvAdjSrc"]
      """  Inventory Adjustment Source for ADJ-QTY, ADJ-CST transaction types only.  "P" = Physical Inventory Count, "C" = Cycle Inventory Count, "O" = Other Adjustment  """  
      self.InvAdjReason:str = obj["InvAdjReason"]
      """  Used for Inventory Adjustment Source "Other" OR MTL-DMR, STK-DMR, SUB-DMR, or INS-DMR transaction types.  Refers to the Reason table.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.LotNum2:str = obj["LotNum2"]
      """  Transfer "From/To" lot number.  """  
      self.DimCode2:str = obj["DimCode2"]
      """  Transfer "From/To" Part Dimension  """  
      self.DUM2:str = obj["DUM2"]
      """  Transfer "From/To" Dimension unit of measure.  """  
      self.DimConvFactor2:int = obj["DimConvFactor2"]
      """  Transfer "From/To" Dimension conversion factor.  """  
      self.GLTrans:bool = obj["GLTrans"]
      """  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  For example: Adj-Cst for other than the parts costing method are not posted to G/L.  """  
      self.PostedToGL:bool = obj["PostedToGL"]
      """  Indicates if transaction was posted to G/L.  Transactions are posted in summary form via the Job Management Capture COS/WIP process .  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal number that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.Costed:bool = obj["Costed"]
      """  The "Costed" field indicates if the Capture COS/Wip Activity has run on that part transaction. If "Yes" the transaction costs cant be changed anymore.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR number used to identify the related DMR record.  """  
      self.ActionNum:int = obj["ActionNum"]
      """  DMR action number  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number  """  
      self.COSPostingReqd:bool = obj["COSPostingReqd"]
      """   If the amount of this PartTran was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped, its costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Plant2:str = obj["Plant2"]
      """  Site Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  Reference to the service call that the material is being issued for.  """  
      self.CallLine:int = obj["CallLine"]
      """  Reference to the service call line  that the material is being issued for.  """  
      self.MatNum:int = obj["MatNum"]
      """  Reference to the service call line Material sequence that the material is being issued for.  """  
      self.JobNum2:str = obj["JobNum2"]
      """  Job Number of transfer source/target.  """  
      self.AssemblySeq2:int = obj["AssemblySeq2"]
      """  Assembly Sequence  of transfer source/target.  """  
      self.JobSeq2:int = obj["JobSeq2"]
      """  Seq # of transfer source/target.  """  
      self.CustNum:int = obj["CustNum"]
      """   NOTE: Applies only to the RMA-INS transactions.
Contains the system internal customer number of the related customer record. 
Not directly updateable, updated via the RmaRcpt write trigger.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA Receipt  """  
      self.RMADisp:int = obj["RMADisp"]
      """  RMA Disposition  """  
      self.OtherDivValue:int = obj["OtherDivValue"]
      """  Other division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of Site transaction costs.  OtherDivValue only applies to Site to Site transactions (TranType="PLT-" and Site <> S  """  
      self.PlantTranNum:int = obj["PlantTranNum"]
      """  Site Transaction Number  """  
      self.NonConfID:int = obj["NonConfID"]
      """  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.BeginQty:int = obj["BeginQty"]
      """  On Hand Quantity before the part costing calculations were run.  """  
      self.AfterQty:int = obj["AfterQty"]
      """  On Hand Quantity after part costing calculation were run.  """  
      self.BegBurUnitCost:int = obj["BegBurUnitCost"]
      """  Burden Unit cost before the part costing calculation was run  """  
      self.BegLbrUnitCost:int = obj["BegLbrUnitCost"]
      """  Labor Unit cost before the costing calculation was run  """  
      self.BegMtlBurUnitCost:int = obj["BegMtlBurUnitCost"]
      """  Material Burden Unit Cost before the costing calculation was run  """  
      self.BegMtlUnitCost:int = obj["BegMtlUnitCost"]
      """  Material Unit Cost before the costing calculation was run  """  
      self.BegSubUnitCost:int = obj["BegSubUnitCost"]
      """  Sub Contract Unit Cost before the costing calculation was run  """  
      self.AfterBurUnitCost:int = obj["AfterBurUnitCost"]
      """  Burden Unit cost after the part costing calculation was run  """  
      self.AfterLbrUnitCost:int = obj["AfterLbrUnitCost"]
      """  Labor Unit Cost after the costing calculation was run  """  
      self.AfterMtlBurUnitCost:int = obj["AfterMtlBurUnitCost"]
      """  Material Burden Unit Cost after the costing calculation was run  """  
      self.AfterMtlUnitCost:int = obj["AfterMtlUnitCost"]
      """  Material Unit Cost after the costing calculation was run  """  
      self.AfterSubUnitCost:int = obj["AfterSubUnitCost"]
      """  Sub Contract Unit Cost after the costing calculation was run  """  
      self.PlantCostValue:int = obj["PlantCostValue"]
      """  To Site division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of To Site transaction costs.  SiteCostValue only applies to Site to Site transactions (TranType="PLT-" and Site  """  
      self.EmpID:str = obj["EmpID"]
      """  The Shop Employee ID of the user that created this transaction.  """  
      self.ReconcileNum:int = obj["ReconcileNum"]
      """  The unique identifier of the DemandReconcile that created this PartTran record.  """  
      self.CostID:str = obj["CostID"]
      """  Id to the Cost Set Group that is used as the default CostGrp.  """  
      self.FIFODate:str = obj["FIFODate"]
      """  For FIFO costed part, use this date to find the FIFO cost queue record affected by this transaction.  """  
      self.FIFOSeq:int = obj["FIFOSeq"]
      """  For FIFO costed part, use this sequence number to find the FIFO cost queue record affected by this transaction.  """  
      self.ActTranQty:int = obj["ActTranQty"]
      """   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  """  
      self.ActTransUOM:str = obj["ActTransUOM"]
      """  Actual Unit of Measure of the ActTransQty.  """  
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  The Inventory Tracking Unit of Measure that transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  """  
      self.InvtyUOM2:str = obj["InvtyUOM2"]
      """  The Inventory Tracking Unit of Measure that inventory transfer transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  """  
      self.FIFOAction:str = obj["FIFOAction"]
      """   Internal flag to indicate what type of FIFO update is needed.  Valid values are: (A/U/D)
"A" - Add new FIFO cost queue
"U" - Update existing FIFO cost queue
"D" - Delete existing FIFO cost queue (Technically, this is more of voiding/deactivating the FIFO since we don't delete historical FIFO records).  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BinType:str = obj["BinType"]
      """  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  """  
      self.CCYear:int = obj["CCYear"]
      """  Calendar year of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  """  
      self.CCMonth:int = obj["CCMonth"]
      """  Calendar month of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl..  """  
      self.CycleSeq:int = obj["CycleSeq"]
      """  CycleSeq of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  GUID - reference on PE ABT.  """  
      self.BaseCostMethod:str = obj["BaseCostMethod"]
      """  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the PartSite.CostMethod or Part.CostMethod  """  
      self.RevertStatus:int = obj["RevertStatus"]
      """   Revert Status field, with following values:
0.	Not reverted (default initial value)
1.	Reverted  """  
      self.RevertID:str = obj["RevertID"]
      """  Reference on revert line  by SySRowID.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.VarTarget:str = obj["VarTarget"]
      """   PartTran.VarTarget, with following values:
'JOB' ? Use Job Expense Account
'STK' ? Use Inventory Account
'VAR' ? Use Purchase Variance Account
'INS' ? Use Inspection Account
'UKN' ? Expense Account (Miscellaneous receipt)
'MTL' ? Use WIP Material Account
'SUB' ? Use WIP Subcontract account
'DMR' ? Use DMR account
'REJ' ? Use DMR Write off Account
'ACA' ? Use Actual Cost Account  """  
      self.FIFOSubSeq:int = obj["FIFOSubSeq"]
      """  The FIFO subsequence number of the related PartFIFOCost record.  """  
      self.AltMtlUnitCost:int = obj["AltMtlUnitCost"]
      """  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltLbrUnitCost:int = obj["AltLbrUnitCost"]
      """  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltBurUnitCost:int = obj["AltBurUnitCost"]
      """  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltSubUnitCost:int = obj["AltSubUnitCost"]
      """  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlBurUnitCost:int = obj["AltMtlBurUnitCost"]
      """  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltExtCost:int = obj["AltExtCost"]
      """  Alternate FIFO Extended Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlMtlUnitCost:int = obj["AltMtlMtlUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlLabUnitCost:int = obj["AltMtlLabUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlSubUnitCost:int = obj["AltMtlSubUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlBurdenUnitCost:int = obj["AltMtlBurdenUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.PBInvNum:int = obj["PBInvNum"]
      """  Invoice Number from Progress Billing Invoice preparation  """  
      self.LoanFlag:str = obj["LoanFlag"]
      """   This is only relevant for TranType MFG-MFG.
Valid types are '' , 'L', and 'B'.  
For Transfers, set to ''.
For Loans and Repayment of Loans set PartTran. LoanType to either 'L' or 'B' based on PartTran.JobNum.  If PartTran.JobNum is the job who is making the loan (or who made the loan, in the case of a repayment), then set to 'L' (loaner).  If PartTran.JobNum is the job who originally received the loan or who is receiving a loan set to 'B' (borrower).  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Unique identifier of the Asset.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Unique number to identify the Addition activity of an asset.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the Disposal activity of an asset.  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process.  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  Used by Project Analysis process.  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  Used By Project Analysis Process  """  
      self.MscNum:int = obj["MscNum"]
      """  Like RcvMisc.MscNum. Filled only for ADJ-PUR transactions created from late costs.  """  
      self.ODCUnitCost:int = obj["ODCUnitCost"]
      """  ODC Unit Cost  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TranRefType:int = obj["TranRefType"]
      """  TranRefType  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.PCIDCollapseCounter:int = obj["PCIDCollapseCounter"]
      """  PCIDCollapseCounter  """  
      self.PCID2:str = obj["PCID2"]
      """  PCID2  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  """  
      self.ExtMtlCost:int = obj["ExtMtlCost"]
      """  ExtMtlCost  """  
      self.ExtLbrCost:int = obj["ExtLbrCost"]
      """  ExtLbrCost  """  
      self.ExtBurCost:int = obj["ExtBurCost"]
      """  ExtBurCost  """  
      self.ExtSubCost:int = obj["ExtSubCost"]
      """  ExtSubCost  """  
      self.ExtMtlBurCost:int = obj["ExtMtlBurCost"]
      """  ExtMtlBurCost  """  
      self.ExtMtlMtlCost:int = obj["ExtMtlMtlCost"]
      """  ExtMtlMtlCost  """  
      self.ExtMtlLabCost:int = obj["ExtMtlLabCost"]
      """  ExtMtlLabCost  """  
      self.ExtMtlSubCost:int = obj["ExtMtlSubCost"]
      """  ExtMtlSubCost  """  
      self.ExtMtlBurdenCost:int = obj["ExtMtlBurdenCost"]
      """  ExtMtlBurdenCost  """  
      self.MYImportNum:str = obj["MYImportNum"]
      """  MYImportNum  """  
      self.AutoReverse:bool = obj["AutoReverse"]
      """  AutoReverse  """  
      self.RevTranNum:int = obj["RevTranNum"]
      """  RevTranNum  """  
      self.RevSysDate:str = obj["RevSysDate"]
      """  RevSysDate  """  
      self.RevSysTime:int = obj["RevSysTime"]
      """  RevSysTime  """  
      self.ExtNonRecoverableCost:int = obj["ExtNonRecoverableCost"]
      """  The Non Recoverable Tax that has been included on the Extended Cost.  This will be calculated from the Receipt Header and Receipt Line tax records by subtracting the total deductable tax from the total tax.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.WIPPCID:str = obj["WIPPCID"]
      """  WIPPCID  """  
      self.WIPPCID2:str = obj["WIPPCID2"]
      """  WIPPCID2  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.JobSubUnitCost:int = obj["JobSubUnitCost"]
      self.LegalNumberNumber:str = obj["LegalNumberNumber"]
      self.LegalNumberPrefix:str = obj["LegalNumberPrefix"]
      self.LegalNumberPrefixList:str = obj["LegalNumberPrefixList"]
      self.LegalNumberReadOnlyFields:str = obj["LegalNumberReadOnlyFields"]
      self.LegalNumberYear:int = obj["LegalNumberYear"]
      self.MtlLbrUnitCost:int = obj["MtlLbrUnitCost"]
      self.MtlQueueRowId:str = obj["MtlQueueRowId"]
      self.MultiEndParts:bool = obj["MultiEndParts"]
      """  Used/Set only by MfgReceipts - Indicates if Job has multiple end parts.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.OverRideCosts:bool = obj["OverRideCosts"]
      """  Override Costs.  Set to yes if the user chooses to override the cost.  """  
      self.PackNumName:str = obj["PackNumName"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  """  
      self.PartDescriptionAsm:str = obj["PartDescriptionAsm"]
      self.PartDescriptionJH:str = obj["PartDescriptionJH"]
      self.PartDescriptionMS:str = obj["PartDescriptionMS"]
      self.PartDescriptionSP:str = obj["PartDescriptionSP"]
      self.PartLotPartLotDescription:str = obj["PartLotPartLotDescription"]
      """  Optional lot number description.  """  
      self.PartNumAsm:str = obj["PartNumAsm"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumJH:str = obj["PartNumJH"]
      self.PartNumMS:str = obj["PartNumMS"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumSP:str = obj["PartNumSP"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.QtyAvailToComplete:int = obj["QtyAvailToComplete"]
      self.QtyBearing:bool = obj["QtyBearing"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      """  Quantity Completed  """  
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.SalvageQtyToDate:int = obj["SalvageQtyToDate"]
      self.SerialNoTempTranID:int = obj["SerialNoTempTranID"]
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.TreeDisplay:str = obj["TreeDisplay"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorPPNumAddress1:str = obj["VendorPPNumAddress1"]
      """  First address line  """  
      self.VendorPPNumAddress2:str = obj["VendorPPNumAddress2"]
      """  Second address line  """  
      self.VendorPPNumAddress3:str = obj["VendorPPNumAddress3"]
      """  Third address line  """  
      self.VendorPPNumCity:str = obj["VendorPPNumCity"]
      """  City portion of the address  """  
      self.VendorPPNumCountry:str = obj["VendorPPNumCountry"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.VendorPPNumName:str = obj["VendorPPNumName"]
      """  Purchase Point Name...can't be blank.  """  
      self.VendorPPNumPrimPCon:int = obj["VendorPPNumPrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.VendorPPNumState:str = obj["VendorPPNumState"]
      """  State portion of the address  """  
      self.VendorPPNumZip:str = obj["VendorPPNumZip"]
      """  Postal Code or Zip code portion of the address  """  
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      """  Description.  """  
      self.BinNumDescription:str = obj["BinNumDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.CostMethodDisplay:str = obj["CostMethodDisplay"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      """  Description for the dimension code.  """  
      self.DIMDescription:str = obj["DIMDescription"]
      self.DisableFieldPart:bool = obj["DisableFieldPart"]
      """  Part field objects must be enabled when the Final Assembly (0) is selected and the Job has multiple end parts.  """  
      self.DispSysTime:str = obj["DispSysTime"]
      """  Display format of System Time in Hrs:Min.  """  
      self.DispUOM:str = obj["DispUOM"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      """  Describes the Part.  System maintained, not user modifiable.  """  
      self.dummyKeyField:str = obj["dummyKeyField"]
      self.FromBinDescription:str = obj["FromBinDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.FromPlantName:str = obj["FromPlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.FromWareHouseDescription:str = obj["FromWareHouseDescription"]
      """  Description.  """  
      self.FullPhysical:bool = obj["FullPhysical"]
      """  If InvAdjSrc = "P", then this field is true, InvAdjSrc = "C", then this field is false  """  
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.InvBurUnitCost:int = obj["InvBurUnitCost"]
      """  Inventory subcontract unit cost  """  
      self.InvLbrUnitCost:int = obj["InvLbrUnitCost"]
      """  Inventory Labor unit cost.  """  
      self.InvMtlBurUnitCost:int = obj["InvMtlBurUnitCost"]
      """  Inventory burden unit cost  """  
      self.InvMtlUnitCost:int = obj["InvMtlUnitCost"]
      """  Inventory material unit cost  """  
      self.InvSubUnitCost:int = obj["InvSubUnitCost"]
      """  Inventory subcontract unit cost.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      self.JobBurUnitCost:int = obj["JobBurUnitCost"]
      self.JobLbrUnitCost:int = obj["JobLbrUnitCost"]
      self.JobMtlBurUnitCost:int = obj["JobMtlBurUnitCost"]
      self.JobMtlUnitCost:int = obj["JobMtlUnitCost"]
      self.Selected:bool = obj["Selected"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.TranNum:int = obj["TranNum"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transaction is for.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.TranClass:str = obj["TranClass"]
      """   Transaction Class...A-adjustment, D-DMR, I-issue, R-receipt, S-Shipment X-Job Adjustment. A character field which classifies PartTran records.  This is a higher level of classification of the TransType field. Their relationships are;
 R = DMR-STK, INS-MTL, INS-STK, INS-SUB, MFG-PLT, MFG-STK, MFG-WIP, PLT-STK, PUR-INS, PUR-MTL, PUR-STK, PUR-SUB, PUR-UKN, RMA-INS, STK-DMR, SVG-STK
I = ASM-INS, INS-ASM, INS-REJ, MTL-INS, PLT-ASM, PLT-MTL, STK-ASM, STK-INS, STK-MTL, STK-SRV, STK-UKN, SUB-DMR, SUB-INS,WIP-MFG
A = ADJ-CST, ADJ-PUR, ADJ-QTY, MFG-VAR, STK-PLT, STK-STK
S = MFG-CUS, MFG-VEN, STK-CUS
D = DMR-MTL, DMR-REJ, DMR-SUB, INS-DMR, MTL-DMR
X = ADJ-MTL, ADJ-SUB
Intended to  be used for record selection purposes.  """  
      self.TranType:str = obj["TranType"]
      """   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  """  
      self.InventoryTrans:bool = obj["InventoryTrans"]
      """  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  """  
      self.TranDate:str = obj["TranDate"]
      """  date of transaction.  """  
      self.TranQty:int = obj["TranQty"]
      """   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  (part primary inventory uom)  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.ExtCost:int = obj["ExtCost"]
      """   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the Part.CostMethod.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that transaction is associated with.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence #  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl),  "S" = SubContract Operation (JobOper) or "O" = Inside Operation(JobOper)
(FYI: Non-Coformance/Inspection transactions, ASM-INS, INS-ASM, INS-DMR, DMR-ASM are the only ones which create "O" types  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.PackType:str = obj["PackType"]
      """  Indicates the type of Packing Slip... "C" = Customer (related to ShipDtl), "M" = Miscellaneous(MscShpDt),  "S" = Subcontractor (SubShipd) "TO" = (Transfer Order). This field, used along with PackNum/PackLine can be used to find the related shipping document record.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number.  """  
      self.PackLine:int = obj["PackLine"]
      """   The packing slip line # that this transaction is linked to.
Note: This field is used for both  a shipment to customer packing slip  or a receipt from vendor packing slip.  """  
      self.PONum:int = obj["PONum"]
      """  Created by Purchase Order Receipt Process.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of detail record on the purchase order.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # of the POSched record that this transaction is for.  """  
      self.WareHouse2:str = obj["WareHouse2"]
      """  Transfer "From/To" warehouse code. This is used for the warehouse transfer transactions. For the Issue side of the transaction it identifies the "transfer to" warehouse. For the receipt side of the transaction it identifies the "transfer from" warehouse.  """  
      self.BinNum2:str = obj["BinNum2"]
      """  This value only exists for the warehouse transaction. TranSrc = "4".  For the Issue side of the transaction it identifies the Bin location that the quantity is transferred in to. On the Receipt side of the transaction it identifies the Bin location that the quantity was transferred from.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The sales order line that this transaction is associated with.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.TranReference:str = obj["TranReference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part, JobOPer, JobMtl, ShipDtl,  SubShipD ....  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that along with PurPoint is used to tie back to the VendorPP master file. Applicable for shipments to subcontractors (MFG-VEN) and receipts (PUR-STK, PUR-MTL, PUR-SUB, PUR-UKN).  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor purchase point ID. (see VendorNum)  """  
      self.POReceiptQty:int = obj["POReceiptQty"]
      """  Quantity received against a purchase order in the vendors unit of measure.  """  
      self.POUnitCost:int = obj["POUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the PO detail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the MtlUnitCost field which is used as cost to job or stock.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvHed record. Applicable only with the purchase variance adjustment record (TranType = "ADJ-PUR") generated via A/P invoice posting.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Used along with InvoiceNum to relate to the corresponding APInvDtl record that generated this PartTran record. (see PartTran.InvoiceNum)  """  
      self.InvAdjSrc:str = obj["InvAdjSrc"]
      """  Inventory Adjustment Source for ADJ-QTY, ADJ-CST transaction types only.  "P" = Physical Inventory Count, "C" = Cycle Inventory Count, "O" = Other Adjustment  """  
      self.InvAdjReason:str = obj["InvAdjReason"]
      """  Used for Inventory Adjustment Source "Other" OR MTL-DMR, STK-DMR, SUB-DMR, or INS-DMR transaction types.  Refers to the Reason table.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.LotNum2:str = obj["LotNum2"]
      """  Transfer "From/To" lot number.  """  
      self.DimCode2:str = obj["DimCode2"]
      """  Transfer "From/To" Part Dimension  """  
      self.DUM2:str = obj["DUM2"]
      """  Transfer "From/To" Dimension unit of measure.  """  
      self.DimConvFactor2:int = obj["DimConvFactor2"]
      """  Transfer "From/To" Dimension conversion factor.  """  
      self.GLTrans:bool = obj["GLTrans"]
      """  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  For example: Adj-Cst for other than the parts costing method are not posted to G/L.  """  
      self.PostedToGL:bool = obj["PostedToGL"]
      """  Indicates if transaction was posted to G/L.  Transactions are posted in summary form via the Job Management Capture COS/WIP process .  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal number that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.Costed:bool = obj["Costed"]
      """  The "Costed" field indicates if the Capture COS/Wip Activity has run on that part transaction. If "Yes" the transaction costs cant be changed anymore.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR number used to identify the related DMR record.  """  
      self.ActionNum:int = obj["ActionNum"]
      """  DMR action number  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number  """  
      self.COSPostingReqd:bool = obj["COSPostingReqd"]
      """   If the amount of this PartTran was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped, its costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Plant2:str = obj["Plant2"]
      """  Site Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  Reference to the service call that the material is being issued for.  """  
      self.CallLine:int = obj["CallLine"]
      """  Reference to the service call line  that the material is being issued for.  """  
      self.MatNum:int = obj["MatNum"]
      """  Reference to the service call line Material sequence that the material is being issued for.  """  
      self.JobNum2:str = obj["JobNum2"]
      """  Job Number of transfer source/target.  """  
      self.AssemblySeq2:int = obj["AssemblySeq2"]
      """  Assembly Sequence  of transfer source/target.  """  
      self.JobSeq2:int = obj["JobSeq2"]
      """  Seq # of transfer source/target.  """  
      self.CustNum:int = obj["CustNum"]
      """   NOTE: Applies only to the RMA-INS transactions.
Contains the system internal customer number of the related customer record. 
Not directly updateable, updated via the RmaRcpt write trigger.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA Receipt  """  
      self.RMADisp:int = obj["RMADisp"]
      """  RMA Disposition  """  
      self.OtherDivValue:int = obj["OtherDivValue"]
      """  Other division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of Site transaction costs.  OtherDivValue only applies to Site to Site transactions (TranType="PLT-" and Site <> S  """  
      self.PlantTranNum:int = obj["PlantTranNum"]
      """  Site Transaction Number  """  
      self.NonConfID:int = obj["NonConfID"]
      """  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.BeginQty:int = obj["BeginQty"]
      """  On Hand Quantity before the part costing calculations were run.  """  
      self.AfterQty:int = obj["AfterQty"]
      """  On Hand Quantity after part costing calculation were run.  """  
      self.BegBurUnitCost:int = obj["BegBurUnitCost"]
      """  Burden Unit cost before the part costing calculation was run  """  
      self.BegLbrUnitCost:int = obj["BegLbrUnitCost"]
      """  Labor Unit cost before the costing calculation was run  """  
      self.BegMtlBurUnitCost:int = obj["BegMtlBurUnitCost"]
      """  Material Burden Unit Cost before the costing calculation was run  """  
      self.BegMtlUnitCost:int = obj["BegMtlUnitCost"]
      """  Material Unit Cost before the costing calculation was run  """  
      self.BegSubUnitCost:int = obj["BegSubUnitCost"]
      """  Sub Contract Unit Cost before the costing calculation was run  """  
      self.AfterBurUnitCost:int = obj["AfterBurUnitCost"]
      """  Burden Unit cost after the part costing calculation was run  """  
      self.AfterLbrUnitCost:int = obj["AfterLbrUnitCost"]
      """  Labor Unit Cost after the costing calculation was run  """  
      self.AfterMtlBurUnitCost:int = obj["AfterMtlBurUnitCost"]
      """  Material Burden Unit Cost after the costing calculation was run  """  
      self.AfterMtlUnitCost:int = obj["AfterMtlUnitCost"]
      """  Material Unit Cost after the costing calculation was run  """  
      self.AfterSubUnitCost:int = obj["AfterSubUnitCost"]
      """  Sub Contract Unit Cost after the costing calculation was run  """  
      self.PlantCostValue:int = obj["PlantCostValue"]
      """  To Site division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of To Site transaction costs.  SiteCostValue only applies to Site to Site transactions (TranType="PLT-" and Site  """  
      self.EmpID:str = obj["EmpID"]
      """  The Shop Employee ID of the user that created this transaction.  """  
      self.ReconcileNum:int = obj["ReconcileNum"]
      """  The unique identifier of the DemandReconcile that created this PartTran record.  """  
      self.CostID:str = obj["CostID"]
      """  Id to the Cost Set Group that is used as the default CostGrp.  """  
      self.FIFODate:str = obj["FIFODate"]
      """  For FIFO costed part, use this date to find the FIFO cost queue record affected by this transaction.  """  
      self.FIFOSeq:int = obj["FIFOSeq"]
      """  For FIFO costed part, use this sequence number to find the FIFO cost queue record affected by this transaction.  """  
      self.ActTranQty:int = obj["ActTranQty"]
      """   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  """  
      self.ActTransUOM:str = obj["ActTransUOM"]
      """  Actual Unit of Measure of the ActTransQty.  """  
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  The Inventory Tracking Unit of Measure that transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  """  
      self.InvtyUOM2:str = obj["InvtyUOM2"]
      """  The Inventory Tracking Unit of Measure that inventory transfer transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  """  
      self.FIFOAction:str = obj["FIFOAction"]
      """   Internal flag to indicate what type of FIFO update is needed.  Valid values are: (A/U/D)
"A" - Add new FIFO cost queue
"U" - Update existing FIFO cost queue
"D" - Delete existing FIFO cost queue (Technically, this is more of voiding/deactivating the FIFO since we don't delete historical FIFO records).  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BinType:str = obj["BinType"]
      """  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  """  
      self.CCYear:int = obj["CCYear"]
      """  Calendar year of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  """  
      self.CCMonth:int = obj["CCMonth"]
      """  Calendar month of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl..  """  
      self.CycleSeq:int = obj["CycleSeq"]
      """  CycleSeq of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  GUID - reference on PE ABT.  """  
      self.BaseCostMethod:str = obj["BaseCostMethod"]
      """  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the PartSite.CostMethod or Part.CostMethod  """  
      self.RevertStatus:int = obj["RevertStatus"]
      """   Revert Status field, with following values:
0.	Not reverted (default initial value)
1.	Reverted  """  
      self.RevertID:str = obj["RevertID"]
      """  Reference on revert line  by SySRowID.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.VarTarget:str = obj["VarTarget"]
      """   PartTran.VarTarget, with following values:
'JOB' ? Use Job Expense Account
'STK' ? Use Inventory Account
'VAR' ? Use Purchase Variance Account
'INS' ? Use Inspection Account
'UKN' ? Expense Account (Miscellaneous receipt)
'MTL' ? Use WIP Material Account
'SUB' ? Use WIP Subcontract account
'DMR' ? Use DMR account
'REJ' ? Use DMR Write off Account
'ACA' ? Use Actual Cost Account  """  
      self.FIFOSubSeq:int = obj["FIFOSubSeq"]
      """  The FIFO subsequence number of the related PartFIFOCost record.  """  
      self.AltMtlUnitCost:int = obj["AltMtlUnitCost"]
      """  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltLbrUnitCost:int = obj["AltLbrUnitCost"]
      """  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltBurUnitCost:int = obj["AltBurUnitCost"]
      """  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltSubUnitCost:int = obj["AltSubUnitCost"]
      """  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlBurUnitCost:int = obj["AltMtlBurUnitCost"]
      """  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltExtCost:int = obj["AltExtCost"]
      """  Alternate FIFO Extended Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlMtlUnitCost:int = obj["AltMtlMtlUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlLabUnitCost:int = obj["AltMtlLabUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlSubUnitCost:int = obj["AltMtlSubUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlBurdenUnitCost:int = obj["AltMtlBurdenUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.PBInvNum:int = obj["PBInvNum"]
      """  Invoice Number from Progress Billing Invoice preparation  """  
      self.LoanFlag:str = obj["LoanFlag"]
      """   This is only relevant for TranType MFG-MFG.
Valid types are '' , 'L', and 'B'.  
For Transfers, set to ''.
For Loans and Repayment of Loans set PartTran. LoanType to either 'L' or 'B' based on PartTran.JobNum.  If PartTran.JobNum is the job who is making the loan (or who made the loan, in the case of a repayment), then set to 'L' (loaner).  If PartTran.JobNum is the job who originally received the loan or who is receiving a loan set to 'B' (borrower).  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Unique identifier of the Asset.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Unique number to identify the Addition activity of an asset.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the Disposal activity of an asset.  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process.  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  Used by Project Analysis process.  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  Used By Project Analysis Process  """  
      self.MscNum:int = obj["MscNum"]
      """  Like RcvMisc.MscNum. Filled only for ADJ-PUR transactions created from late costs.  """  
      self.ODCUnitCost:int = obj["ODCUnitCost"]
      """  ODC Unit Cost  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TranRefType:int = obj["TranRefType"]
      """  TranRefType  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.PCIDCollapseCounter:int = obj["PCIDCollapseCounter"]
      """  PCIDCollapseCounter  """  
      self.PCID2:str = obj["PCID2"]
      """  PCID2  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  """  
      self.ExtMtlCost:int = obj["ExtMtlCost"]
      """  ExtMtlCost  """  
      self.ExtLbrCost:int = obj["ExtLbrCost"]
      """  ExtLbrCost  """  
      self.ExtBurCost:int = obj["ExtBurCost"]
      """  ExtBurCost  """  
      self.ExtSubCost:int = obj["ExtSubCost"]
      """  ExtSubCost  """  
      self.ExtMtlBurCost:int = obj["ExtMtlBurCost"]
      """  ExtMtlBurCost  """  
      self.ExtMtlMtlCost:int = obj["ExtMtlMtlCost"]
      """  ExtMtlMtlCost  """  
      self.ExtMtlLabCost:int = obj["ExtMtlLabCost"]
      """  ExtMtlLabCost  """  
      self.ExtMtlSubCost:int = obj["ExtMtlSubCost"]
      """  ExtMtlSubCost  """  
      self.ExtMtlBurdenCost:int = obj["ExtMtlBurdenCost"]
      """  ExtMtlBurdenCost  """  
      self.MYImportNum:str = obj["MYImportNum"]
      """  MYImportNum  """  
      self.AutoReverse:bool = obj["AutoReverse"]
      """  AutoReverse  """  
      self.RevTranNum:int = obj["RevTranNum"]
      """  RevTranNum  """  
      self.RevSysDate:str = obj["RevSysDate"]
      """  RevSysDate  """  
      self.RevSysTime:int = obj["RevSysTime"]
      """  RevSysTime  """  
      self.ExtNonRecoverableCost:int = obj["ExtNonRecoverableCost"]
      """  The Non Recoverable Tax that has been included on the Extended Cost.  This will be calculated from the Receipt Header and Receipt Line tax records by subtracting the total deductable tax from the total tax.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.WIPPCID:str = obj["WIPPCID"]
      """  WIPPCID  """  
      self.WIPPCID2:str = obj["WIPPCID2"]
      """  WIPPCID2  """  
      self.CallCode:str = obj["CallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.DIMDescription:str = obj["DIMDescription"]
      self.DisableFieldPart:bool = obj["DisableFieldPart"]
      """  Part field objects must be enabled when the Final Assembly (0) is selected and the Job has multiple end parts.  """  
      self.DispSysTime:str = obj["DispSysTime"]
      """  Display format of System Time in Hrs:Min.  """  
      self.DispUOM:str = obj["DispUOM"]
      self.dummyKeyField:str = obj["dummyKeyField"]
      self.EnableSerialNumbers:bool = obj["EnableSerialNumbers"]
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.FSACallCode:str = obj["FSACallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.FSAContractCode:str = obj["FSAContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.FSAContractNum:int = obj["FSAContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.FSAEmpID:str = obj["FSAEmpID"]
      """  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAWarrantyCode:str = obj["FSAWarrantyCode"]
      """  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  """  
      self.FullPhysical:bool = obj["FullPhysical"]
      """  If InvAdjSrc = "P", then this field is true, InvAdjSrc = "C", then this field is false  """  
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.InvBurUnitCost:int = obj["InvBurUnitCost"]
      """  Inventory subcontract unit cost  """  
      self.InvLbrUnitCost:int = obj["InvLbrUnitCost"]
      """  Inventory Labor unit cost.  """  
      self.InvMtlBurUnitCost:int = obj["InvMtlBurUnitCost"]
      """  Inventory burden unit cost  """  
      self.InvMtlUnitCost:int = obj["InvMtlUnitCost"]
      """  Inventory material unit cost  """  
      self.InvSubUnitCost:int = obj["InvSubUnitCost"]
      """  Inventory subcontract unit cost.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      self.JobBurUnitCost:int = obj["JobBurUnitCost"]
      self.JobLbrUnitCost:int = obj["JobLbrUnitCost"]
      self.JobMtlBurUnitCost:int = obj["JobMtlBurUnitCost"]
      self.JobMtlUnitCost:int = obj["JobMtlUnitCost"]
      self.JobSubUnitCost:int = obj["JobSubUnitCost"]
      self.LegalNumberNumber:str = obj["LegalNumberNumber"]
      self.LegalNumberPrefix:str = obj["LegalNumberPrefix"]
      self.LegalNumberPrefixList:str = obj["LegalNumberPrefixList"]
      self.LegalNumberReadOnlyFields:str = obj["LegalNumberReadOnlyFields"]
      self.LegalNumberYear:int = obj["LegalNumberYear"]
      self.MtlLbrUnitCost:int = obj["MtlLbrUnitCost"]
      self.MtlQueueRowId:str = obj["MtlQueueRowId"]
      self.MultiEndParts:bool = obj["MultiEndParts"]
      """  Used/Set only by MfgReceipts - Indicates if Job has multiple end parts.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      self.OverRideCosts:bool = obj["OverRideCosts"]
      """  Override Costs.  Set to yes if the user chooses to override the cost.  """  
      self.PartDescriptionAsm:str = obj["PartDescriptionAsm"]
      self.PartDescriptionJH:str = obj["PartDescriptionJH"]
      self.PartDescriptionMS:str = obj["PartDescriptionMS"]
      self.PartDescriptionSP:str = obj["PartDescriptionSP"]
      self.PartNumAsm:str = obj["PartNumAsm"]
      self.PartNumJH:str = obj["PartNumJH"]
      self.PartNumMS:str = obj["PartNumMS"]
      self.PartNumSP:str = obj["PartNumSP"]
      self.QtyAvailToComplete:int = obj["QtyAvailToComplete"]
      self.QtyBearing:bool = obj["QtyBearing"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      """  Quantity Completed  """  
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.SalvageQtyToDate:int = obj["SalvageQtyToDate"]
      self.SerialNoTempTranID:int = obj["SerialNoTempTranID"]
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.TranAmount:int = obj["TranAmount"]
      """  Transaction Amount  """  
      self.TreeDisplay:str = obj["TreeDisplay"]
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.CostMethodDisplay:str = obj["CostMethodDisplay"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts  """  
      self.RevisionNumAsm:str = obj["RevisionNumAsm"]
      self.RevisionNumMS:str = obj["RevisionNumMS"]
      self.RevisionNumSP:str = obj["RevisionNumSP"]
      self.PlantConfCtrlEnablePackageControl:bool = obj["PlantConfCtrlEnablePackageControl"]
      self.AttributeSetDescriptionMS:str = obj["AttributeSetDescriptionMS"]
      """  Description for AttributeSetID associated with PartNumMS  """  
      self.AttributeSetIDMS:int = obj["AttributeSetIDMS"]
      """  AttributeSetID associated with PartNumMS  """  
      self.AttributeSetShortDescriptionMS:str = obj["AttributeSetShortDescriptionMS"]
      """  AttributeSetShortDescription associated with PartNumMS  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumName:str = obj["CustNumName"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      self.FromBinDescription:str = obj["FromBinDescription"]
      self.FromPlantName:str = obj["FromPlantName"]
      self.FromWareHouseDescription:str = obj["FromWareHouseDescription"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.MatNumLineDesc:str = obj["MatNumLineDesc"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      self.PackNumName:str = obj["PackNumName"]
      self.PartLotPartLotDescription:str = obj["PartLotPartLotDescription"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PlantName:str = obj["PlantName"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorPPNumAddress1:str = obj["VendorPPNumAddress1"]
      self.VendorPPNumAddress2:str = obj["VendorPPNumAddress2"]
      self.VendorPPNumPrimPCon:int = obj["VendorPPNumPrimPCon"]
      self.VendorPPNumAddress3:str = obj["VendorPPNumAddress3"]
      self.VendorPPNumCountry:str = obj["VendorPPNumCountry"]
      self.VendorPPNumState:str = obj["VendorPPNumState"]
      self.VendorPPNumZip:str = obj["VendorPPNumZip"]
      self.VendorPPNumCity:str = obj["VendorPPNumCity"]
      self.VendorPPNumName:str = obj["VendorPPNumName"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   sysDate
   sysTime
   tranNum
   """  
   def __init__(self, obj):
      self.sysDate:str = obj["sysDate"]
      self.sysTime:int = obj["sysTime"]
      self.tranNum:int = obj["tranNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PartTranListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.TranNum:int = obj["TranNum"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transaction is for.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.TranClass:str = obj["TranClass"]
      """   Transaction Class...A-adjustment, D-DMR, I-issue, R-receipt, S-Shipment X-Job Adjustment. A character field which classifies PartTran records.  This is a higher level of classification of the TransType field. Their relationships are;
 R = DMR-STK, INS-MTL, INS-STK, INS-SUB, MFG-PLT, MFG-STK, MFG-WIP, PLT-STK, PUR-INS, PUR-MTL, PUR-STK, PUR-SUB, PUR-UKN, RMA-INS, STK-DMR, SVG-STK
I = ASM-INS, INS-ASM, INS-REJ, MTL-INS, PLT-ASM, PLT-MTL, STK-ASM, STK-INS, STK-MTL, STK-SRV, STK-UKN, SUB-DMR, SUB-INS,WIP-MFG
A = ADJ-CST, ADJ-PUR, ADJ-QTY, MFG-VAR, STK-PLT, STK-STK
S = MFG-CUS, MFG-VEN, STK-CUS
D = DMR-MTL, DMR-REJ, DMR-SUB, INS-DMR, MTL-DMR
X = ADJ-MTL, ADJ-SUB
Intended to  be used for record selection purposes.  """  
      self.TranType:str = obj["TranType"]
      """   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  """  
      self.InventoryTrans:bool = obj["InventoryTrans"]
      """  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  """  
      self.TranDate:str = obj["TranDate"]
      """  date of transaction.  """  
      self.TranQty:int = obj["TranQty"]
      """   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  (part primary inventory uom)  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.ExtCost:int = obj["ExtCost"]
      """   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the Part.CostMethod.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that transaction is associated with.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence #  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl),  "S" = SubContract Operation (JobOper) or "O" = Inside Operation(JobOper)
(FYI: Non-Coformance/Inspection transactions, ASM-INS, INS-ASM, INS-DMR, DMR-ASM are the only ones which create "O" types  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.PackType:str = obj["PackType"]
      """  Indicates the type of Packing Slip... "C" = Customer (related to ShipDtl), "M" = Miscellaneous(MscShpDt),  "S" = Subcontractor (SubShipd) "TO" = (Transfer Order). This field, used along with PackNum/PackLine can be used to find the related shipping document record.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number.  """  
      self.PackLine:int = obj["PackLine"]
      """   The packing slip line # that this transaction is linked to.
Note: This field is used for both  a shipment to customer packing slip  or a receipt from vendor packing slip.  """  
      self.PONum:int = obj["PONum"]
      """  Created by Purchase Order Receipt Process.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of detail record on the purchase order.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # of the POSched record that this transaction is for.  """  
      self.WareHouse2:str = obj["WareHouse2"]
      """  Transfer "From/To" warehouse code. This is used for the warehouse transfer transactions. For the Issue side of the transaction it identifies the "transfer to" warehouse. For the receipt side of the transaction it identifies the "transfer from" warehouse.  """  
      self.BinNum2:str = obj["BinNum2"]
      """  This value only exists for the warehouse transaction. TranSrc = "4".  For the Issue side of the transaction it identifies the Bin location that the quantity is transferred in to. On the Receipt side of the transaction it identifies the Bin location that the quantity was transferred from.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The sales order line that this transaction is associated with.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.TranReference:str = obj["TranReference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part, JobOPer, JobMtl, ShipDtl,  SubShipD ....  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that along with PurPoint is used to tie back to the VendorPP master file. Applicable for shipments to subcontractors (MFG-VEN) and receipts (PUR-STK, PUR-MTL, PUR-SUB, PUR-UKN).  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor purchase point ID. (see VendorNum)  """  
      self.POReceiptQty:int = obj["POReceiptQty"]
      """  Quantity received against a purchase order in the vendors unit of measure.  """  
      self.POUnitCost:int = obj["POUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the PO detail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the MtlUnitCost field which is used as cost to job or stock.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvHed record. Applicable only with the purchase variance adjustment record (TranType = "ADJ-PUR") generated via A/P invoice posting.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Used along with InvoiceNum to relate to the corresponding APInvDtl record that generated this PartTran record. (see PartTran.InvoiceNum)  """  
      self.InvAdjSrc:str = obj["InvAdjSrc"]
      """  Inventory Adjustment Source for ADJ-QTY, ADJ-CST transaction types only.  "P" = Physical Inventory Count, "C" = Cycle Inventory Count, "O" = Other Adjustment  """  
      self.InvAdjReason:str = obj["InvAdjReason"]
      """  Used for Inventory Adjustment Source "Other" OR MTL-DMR, STK-DMR, SUB-DMR, or INS-DMR transaction types.  Refers to the Reason table.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.LotNum2:str = obj["LotNum2"]
      """  Transfer "From/To" lot number.  """  
      self.DimCode2:str = obj["DimCode2"]
      """  Transfer "From/To" Part Dimension  """  
      self.DUM2:str = obj["DUM2"]
      """  Transfer "From/To" Dimension unit of measure.  """  
      self.DimConvFactor2:int = obj["DimConvFactor2"]
      """  Transfer "From/To" Dimension conversion factor.  """  
      self.GLTrans:bool = obj["GLTrans"]
      """  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  For example: Adj-Cst for other than the parts costing method are not posted to G/L.  """  
      self.PostedToGL:bool = obj["PostedToGL"]
      """  Indicates if transaction was posted to G/L.  Transactions are posted in summary form via the Job Management Capture COS/WIP process .  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal number that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.Costed:bool = obj["Costed"]
      """  The "Costed" field indicates if the Capture COS/Wip Activity has run on that part transaction. If "Yes" the transaction costs cant be changed anymore.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR number used to identify the related DMR record.  """  
      self.ActionNum:int = obj["ActionNum"]
      """  DMR action number  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number  """  
      self.COSPostingReqd:bool = obj["COSPostingReqd"]
      """   If the amount of this PartTran was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped, its costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Plant2:str = obj["Plant2"]
      """  Site Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  Reference to the service call that the material is being issued for.  """  
      self.CallLine:int = obj["CallLine"]
      """  Reference to the service call line  that the material is being issued for.  """  
      self.MatNum:int = obj["MatNum"]
      """  Reference to the service call line Material sequence that the material is being issued for.  """  
      self.JobNum2:str = obj["JobNum2"]
      """  Job Number of transfer source/target.  """  
      self.AssemblySeq2:int = obj["AssemblySeq2"]
      """  Assembly Sequence  of transfer source/target.  """  
      self.JobSeq2:int = obj["JobSeq2"]
      """  Seq # of transfer source/target.  """  
      self.CustNum:int = obj["CustNum"]
      """   NOTE: Applies only to the RMA-INS transactions.
Contains the system internal customer number of the related customer record. 
Not directly updateable, updated via the RmaRcpt write trigger.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA Receipt  """  
      self.RMADisp:int = obj["RMADisp"]
      """  RMA Disposition  """  
      self.OtherDivValue:int = obj["OtherDivValue"]
      """  Other division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of Site transaction costs.  OtherDivValue only applies to Site to Site transactions (TranType="PLT-" and Site <> S  """  
      self.PlantTranNum:int = obj["PlantTranNum"]
      """  Site Transaction Number  """  
      self.NonConfID:int = obj["NonConfID"]
      """  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.BeginQty:int = obj["BeginQty"]
      """  On Hand Quantity before the part costing calculations were run.  """  
      self.AfterQty:int = obj["AfterQty"]
      """  On Hand Quantity after part costing calculation were run.  """  
      self.BegBurUnitCost:int = obj["BegBurUnitCost"]
      """  Burden Unit cost before the part costing calculation was run  """  
      self.BegLbrUnitCost:int = obj["BegLbrUnitCost"]
      """  Labor Unit cost before the costing calculation was run  """  
      self.BegMtlBurUnitCost:int = obj["BegMtlBurUnitCost"]
      """  Material Burden Unit Cost before the costing calculation was run  """  
      self.BegMtlUnitCost:int = obj["BegMtlUnitCost"]
      """  Material Unit Cost before the costing calculation was run  """  
      self.BegSubUnitCost:int = obj["BegSubUnitCost"]
      """  Sub Contract Unit Cost before the costing calculation was run  """  
      self.AfterBurUnitCost:int = obj["AfterBurUnitCost"]
      """  Burden Unit cost after the part costing calculation was run  """  
      self.AfterLbrUnitCost:int = obj["AfterLbrUnitCost"]
      """  Labor Unit Cost after the costing calculation was run  """  
      self.AfterMtlBurUnitCost:int = obj["AfterMtlBurUnitCost"]
      """  Material Burden Unit Cost after the costing calculation was run  """  
      self.AfterMtlUnitCost:int = obj["AfterMtlUnitCost"]
      """  Material Unit Cost after the costing calculation was run  """  
      self.AfterSubUnitCost:int = obj["AfterSubUnitCost"]
      """  Sub Contract Unit Cost after the costing calculation was run  """  
      self.PlantCostValue:int = obj["PlantCostValue"]
      """  To Site division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of To Site transaction costs.  SiteCostValue only applies to Site to Site transactions (TranType="PLT-" and Site  """  
      self.EmpID:str = obj["EmpID"]
      """  The Shop Employee ID of the user that created this transaction.  """  
      self.ReconcileNum:int = obj["ReconcileNum"]
      """  The unique identifier of the DemandReconcile that created this PartTran record.  """  
      self.CostID:str = obj["CostID"]
      """  Id to the Cost Set Group that is used as the default CostGrp.  """  
      self.FIFODate:str = obj["FIFODate"]
      """  For FIFO costed part, use this date to find the FIFO cost queue record affected by this transaction.  """  
      self.FIFOSeq:int = obj["FIFOSeq"]
      """  For FIFO costed part, use this sequence number to find the FIFO cost queue record affected by this transaction.  """  
      self.ActTranQty:int = obj["ActTranQty"]
      """   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  """  
      self.ActTransUOM:str = obj["ActTransUOM"]
      """  Actual Unit of Measure of the ActTransQty.  """  
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  The Inventory Tracking Unit of Measure that transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  """  
      self.InvtyUOM2:str = obj["InvtyUOM2"]
      """  The Inventory Tracking Unit of Measure that inventory transfer transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  """  
      self.FIFOAction:str = obj["FIFOAction"]
      """   Internal flag to indicate what type of FIFO update is needed.  Valid values are: (A/U/D)
"A" - Add new FIFO cost queue
"U" - Update existing FIFO cost queue
"D" - Delete existing FIFO cost queue (Technically, this is more of voiding/deactivating the FIFO since we don't delete historical FIFO records).  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BinType:str = obj["BinType"]
      """  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  """  
      self.CCYear:int = obj["CCYear"]
      """  Calendar year of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  """  
      self.CCMonth:int = obj["CCMonth"]
      """  Calendar month of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl..  """  
      self.CycleSeq:int = obj["CycleSeq"]
      """  CycleSeq of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  GUID - reference on PE ABT.  """  
      self.BaseCostMethod:str = obj["BaseCostMethod"]
      """  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the PartSite.CostMethod or Part.CostMethod  """  
      self.RevertStatus:int = obj["RevertStatus"]
      """   Revert Status field, with following values:
0.	Not reverted (default initial value)
1.	Reverted  """  
      self.RevertID:str = obj["RevertID"]
      """  Reference on revert line  by SySRowID.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.VarTarget:str = obj["VarTarget"]
      """   PartTran.VarTarget, with following values:
'JOB' ? Use Job Expense Account
'STK' ? Use Inventory Account
'VAR' ? Use Purchase Variance Account
'INS' ? Use Inspection Account
'UKN' ? Expense Account (Miscellaneous receipt)
'MTL' ? Use WIP Material Account
'SUB' ? Use WIP Subcontract account
'DMR' ? Use DMR account
'REJ' ? Use DMR Write off Account
'ACA' ? Use Actual Cost Account  """  
      self.FIFOSubSeq:int = obj["FIFOSubSeq"]
      """  The FIFO subsequence number of the related PartFIFOCost record.  """  
      self.AltMtlUnitCost:int = obj["AltMtlUnitCost"]
      """  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltLbrUnitCost:int = obj["AltLbrUnitCost"]
      """  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltBurUnitCost:int = obj["AltBurUnitCost"]
      """  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltSubUnitCost:int = obj["AltSubUnitCost"]
      """  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlBurUnitCost:int = obj["AltMtlBurUnitCost"]
      """  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltExtCost:int = obj["AltExtCost"]
      """  Alternate FIFO Extended Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlMtlUnitCost:int = obj["AltMtlMtlUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlLabUnitCost:int = obj["AltMtlLabUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlSubUnitCost:int = obj["AltMtlSubUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlBurdenUnitCost:int = obj["AltMtlBurdenUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.PBInvNum:int = obj["PBInvNum"]
      """  Invoice Number from Progress Billing Invoice preparation  """  
      self.LoanFlag:str = obj["LoanFlag"]
      """   This is only relevant for TranType MFG-MFG.
Valid types are '' , 'L', and 'B'.  
For Transfers, set to ''.
For Loans and Repayment of Loans set PartTran. LoanType to either 'L' or 'B' based on PartTran.JobNum.  If PartTran.JobNum is the job who is making the loan (or who made the loan, in the case of a repayment), then set to 'L' (loaner).  If PartTran.JobNum is the job who originally received the loan or who is receiving a loan set to 'B' (borrower).  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Unique identifier of the Asset.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Unique number to identify the Addition activity of an asset.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the Disposal activity of an asset.  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process.  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  Used by Project Analysis process.  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  Used By Project Analysis Process  """  
      self.MscNum:int = obj["MscNum"]
      """  Like RcvMisc.MscNum. Filled only for ADJ-PUR transactions created from late costs.  """  
      self.ODCUnitCost:int = obj["ODCUnitCost"]
      """  ODC Unit Cost  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TranRefType:int = obj["TranRefType"]
      """  TranRefType  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.PCIDCollapseCounter:int = obj["PCIDCollapseCounter"]
      """  PCIDCollapseCounter  """  
      self.PCID2:str = obj["PCID2"]
      """  PCID2  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  """  
      self.ExtMtlCost:int = obj["ExtMtlCost"]
      """  ExtMtlCost  """  
      self.ExtLbrCost:int = obj["ExtLbrCost"]
      """  ExtLbrCost  """  
      self.ExtBurCost:int = obj["ExtBurCost"]
      """  ExtBurCost  """  
      self.ExtSubCost:int = obj["ExtSubCost"]
      """  ExtSubCost  """  
      self.ExtMtlBurCost:int = obj["ExtMtlBurCost"]
      """  ExtMtlBurCost  """  
      self.ExtMtlMtlCost:int = obj["ExtMtlMtlCost"]
      """  ExtMtlMtlCost  """  
      self.ExtMtlLabCost:int = obj["ExtMtlLabCost"]
      """  ExtMtlLabCost  """  
      self.ExtMtlSubCost:int = obj["ExtMtlSubCost"]
      """  ExtMtlSubCost  """  
      self.ExtMtlBurdenCost:int = obj["ExtMtlBurdenCost"]
      """  ExtMtlBurdenCost  """  
      self.MYImportNum:str = obj["MYImportNum"]
      """  MYImportNum  """  
      self.AutoReverse:bool = obj["AutoReverse"]
      """  AutoReverse  """  
      self.RevTranNum:int = obj["RevTranNum"]
      """  RevTranNum  """  
      self.RevSysDate:str = obj["RevSysDate"]
      """  RevSysDate  """  
      self.RevSysTime:int = obj["RevSysTime"]
      """  RevSysTime  """  
      self.ExtNonRecoverableCost:int = obj["ExtNonRecoverableCost"]
      """  The Non Recoverable Tax that has been included on the Extended Cost.  This will be calculated from the Receipt Header and Receipt Line tax records by subtracting the total deductable tax from the total tax.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.WIPPCID:str = obj["WIPPCID"]
      """  WIPPCID  """  
      self.WIPPCID2:str = obj["WIPPCID2"]
      """  WIPPCID2  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.JobSubUnitCost:int = obj["JobSubUnitCost"]
      self.LegalNumberNumber:str = obj["LegalNumberNumber"]
      self.LegalNumberPrefix:str = obj["LegalNumberPrefix"]
      self.LegalNumberPrefixList:str = obj["LegalNumberPrefixList"]
      self.LegalNumberReadOnlyFields:str = obj["LegalNumberReadOnlyFields"]
      self.LegalNumberYear:int = obj["LegalNumberYear"]
      self.MtlLbrUnitCost:int = obj["MtlLbrUnitCost"]
      self.MtlQueueRowId:str = obj["MtlQueueRowId"]
      self.MultiEndParts:bool = obj["MultiEndParts"]
      """  Used/Set only by MfgReceipts - Indicates if Job has multiple end parts.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.OverRideCosts:bool = obj["OverRideCosts"]
      """  Override Costs.  Set to yes if the user chooses to override the cost.  """  
      self.PackNumName:str = obj["PackNumName"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  """  
      self.PartDescriptionAsm:str = obj["PartDescriptionAsm"]
      self.PartDescriptionJH:str = obj["PartDescriptionJH"]
      self.PartDescriptionMS:str = obj["PartDescriptionMS"]
      self.PartDescriptionSP:str = obj["PartDescriptionSP"]
      self.PartLotPartLotDescription:str = obj["PartLotPartLotDescription"]
      """  Optional lot number description.  """  
      self.PartNumAsm:str = obj["PartNumAsm"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumJH:str = obj["PartNumJH"]
      self.PartNumMS:str = obj["PartNumMS"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumSP:str = obj["PartNumSP"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.QtyAvailToComplete:int = obj["QtyAvailToComplete"]
      self.QtyBearing:bool = obj["QtyBearing"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      """  Quantity Completed  """  
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.SalvageQtyToDate:int = obj["SalvageQtyToDate"]
      self.SerialNoTempTranID:int = obj["SerialNoTempTranID"]
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.TreeDisplay:str = obj["TreeDisplay"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorPPNumAddress1:str = obj["VendorPPNumAddress1"]
      """  First address line  """  
      self.VendorPPNumAddress2:str = obj["VendorPPNumAddress2"]
      """  Second address line  """  
      self.VendorPPNumAddress3:str = obj["VendorPPNumAddress3"]
      """  Third address line  """  
      self.VendorPPNumCity:str = obj["VendorPPNumCity"]
      """  City portion of the address  """  
      self.VendorPPNumCountry:str = obj["VendorPPNumCountry"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.VendorPPNumName:str = obj["VendorPPNumName"]
      """  Purchase Point Name...can't be blank.  """  
      self.VendorPPNumPrimPCon:int = obj["VendorPPNumPrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.VendorPPNumState:str = obj["VendorPPNumState"]
      """  State portion of the address  """  
      self.VendorPPNumZip:str = obj["VendorPPNumZip"]
      """  Postal Code or Zip code portion of the address  """  
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      """  Description.  """  
      self.BinNumDescription:str = obj["BinNumDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.CostMethodDisplay:str = obj["CostMethodDisplay"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      """  Description for the dimension code.  """  
      self.DIMDescription:str = obj["DIMDescription"]
      self.DisableFieldPart:bool = obj["DisableFieldPart"]
      """  Part field objects must be enabled when the Final Assembly (0) is selected and the Job has multiple end parts.  """  
      self.DispSysTime:str = obj["DispSysTime"]
      """  Display format of System Time in Hrs:Min.  """  
      self.DispUOM:str = obj["DispUOM"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      """  Describes the Part.  System maintained, not user modifiable.  """  
      self.dummyKeyField:str = obj["dummyKeyField"]
      self.FromBinDescription:str = obj["FromBinDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.FromPlantName:str = obj["FromPlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.FromWareHouseDescription:str = obj["FromWareHouseDescription"]
      """  Description.  """  
      self.FullPhysical:bool = obj["FullPhysical"]
      """  If InvAdjSrc = "P", then this field is true, InvAdjSrc = "C", then this field is false  """  
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.InvBurUnitCost:int = obj["InvBurUnitCost"]
      """  Inventory subcontract unit cost  """  
      self.InvLbrUnitCost:int = obj["InvLbrUnitCost"]
      """  Inventory Labor unit cost.  """  
      self.InvMtlBurUnitCost:int = obj["InvMtlBurUnitCost"]
      """  Inventory burden unit cost  """  
      self.InvMtlUnitCost:int = obj["InvMtlUnitCost"]
      """  Inventory material unit cost  """  
      self.InvSubUnitCost:int = obj["InvSubUnitCost"]
      """  Inventory subcontract unit cost.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      self.JobBurUnitCost:int = obj["JobBurUnitCost"]
      self.JobLbrUnitCost:int = obj["JobLbrUnitCost"]
      self.JobMtlBurUnitCost:int = obj["JobMtlBurUnitCost"]
      self.JobMtlUnitCost:int = obj["JobMtlUnitCost"]
      self.Selected:bool = obj["Selected"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartTranListTableset:
   def __init__(self, obj):
      self.PartTranList:list[Erp_Tablesets_PartTranListRow] = obj["PartTranList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.TranNum:int = obj["TranNum"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transaction is for.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.TranClass:str = obj["TranClass"]
      """   Transaction Class...A-adjustment, D-DMR, I-issue, R-receipt, S-Shipment X-Job Adjustment. A character field which classifies PartTran records.  This is a higher level of classification of the TransType field. Their relationships are;
 R = DMR-STK, INS-MTL, INS-STK, INS-SUB, MFG-PLT, MFG-STK, MFG-WIP, PLT-STK, PUR-INS, PUR-MTL, PUR-STK, PUR-SUB, PUR-UKN, RMA-INS, STK-DMR, SVG-STK
I = ASM-INS, INS-ASM, INS-REJ, MTL-INS, PLT-ASM, PLT-MTL, STK-ASM, STK-INS, STK-MTL, STK-SRV, STK-UKN, SUB-DMR, SUB-INS,WIP-MFG
A = ADJ-CST, ADJ-PUR, ADJ-QTY, MFG-VAR, STK-PLT, STK-STK
S = MFG-CUS, MFG-VEN, STK-CUS
D = DMR-MTL, DMR-REJ, DMR-SUB, INS-DMR, MTL-DMR
X = ADJ-MTL, ADJ-SUB
Intended to  be used for record selection purposes.  """  
      self.TranType:str = obj["TranType"]
      """   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  """  
      self.InventoryTrans:bool = obj["InventoryTrans"]
      """  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  """  
      self.TranDate:str = obj["TranDate"]
      """  date of transaction.  """  
      self.TranQty:int = obj["TranQty"]
      """   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  (part primary inventory uom)  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.ExtCost:int = obj["ExtCost"]
      """   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the Part.CostMethod.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that transaction is associated with.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence #  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl),  "S" = SubContract Operation (JobOper) or "O" = Inside Operation(JobOper)
(FYI: Non-Coformance/Inspection transactions, ASM-INS, INS-ASM, INS-DMR, DMR-ASM are the only ones which create "O" types  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.PackType:str = obj["PackType"]
      """  Indicates the type of Packing Slip... "C" = Customer (related to ShipDtl), "M" = Miscellaneous(MscShpDt),  "S" = Subcontractor (SubShipd) "TO" = (Transfer Order). This field, used along with PackNum/PackLine can be used to find the related shipping document record.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number.  """  
      self.PackLine:int = obj["PackLine"]
      """   The packing slip line # that this transaction is linked to.
Note: This field is used for both  a shipment to customer packing slip  or a receipt from vendor packing slip.  """  
      self.PONum:int = obj["PONum"]
      """  Created by Purchase Order Receipt Process.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of detail record on the purchase order.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # of the POSched record that this transaction is for.  """  
      self.WareHouse2:str = obj["WareHouse2"]
      """  Transfer "From/To" warehouse code. This is used for the warehouse transfer transactions. For the Issue side of the transaction it identifies the "transfer to" warehouse. For the receipt side of the transaction it identifies the "transfer from" warehouse.  """  
      self.BinNum2:str = obj["BinNum2"]
      """  This value only exists for the warehouse transaction. TranSrc = "4".  For the Issue side of the transaction it identifies the Bin location that the quantity is transferred in to. On the Receipt side of the transaction it identifies the Bin location that the quantity was transferred from.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The sales order line that this transaction is associated with.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.TranReference:str = obj["TranReference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part, JobOPer, JobMtl, ShipDtl,  SubShipD ....  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that along with PurPoint is used to tie back to the VendorPP master file. Applicable for shipments to subcontractors (MFG-VEN) and receipts (PUR-STK, PUR-MTL, PUR-SUB, PUR-UKN).  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor purchase point ID. (see VendorNum)  """  
      self.POReceiptQty:int = obj["POReceiptQty"]
      """  Quantity received against a purchase order in the vendors unit of measure.  """  
      self.POUnitCost:int = obj["POUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the PO detail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the MtlUnitCost field which is used as cost to job or stock.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvHed record. Applicable only with the purchase variance adjustment record (TranType = "ADJ-PUR") generated via A/P invoice posting.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Used along with InvoiceNum to relate to the corresponding APInvDtl record that generated this PartTran record. (see PartTran.InvoiceNum)  """  
      self.InvAdjSrc:str = obj["InvAdjSrc"]
      """  Inventory Adjustment Source for ADJ-QTY, ADJ-CST transaction types only.  "P" = Physical Inventory Count, "C" = Cycle Inventory Count, "O" = Other Adjustment  """  
      self.InvAdjReason:str = obj["InvAdjReason"]
      """  Used for Inventory Adjustment Source "Other" OR MTL-DMR, STK-DMR, SUB-DMR, or INS-DMR transaction types.  Refers to the Reason table.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.LotNum2:str = obj["LotNum2"]
      """  Transfer "From/To" lot number.  """  
      self.DimCode2:str = obj["DimCode2"]
      """  Transfer "From/To" Part Dimension  """  
      self.DUM2:str = obj["DUM2"]
      """  Transfer "From/To" Dimension unit of measure.  """  
      self.DimConvFactor2:int = obj["DimConvFactor2"]
      """  Transfer "From/To" Dimension conversion factor.  """  
      self.GLTrans:bool = obj["GLTrans"]
      """  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  For example: Adj-Cst for other than the parts costing method are not posted to G/L.  """  
      self.PostedToGL:bool = obj["PostedToGL"]
      """  Indicates if transaction was posted to G/L.  Transactions are posted in summary form via the Job Management Capture COS/WIP process .  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal number that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.Costed:bool = obj["Costed"]
      """  The "Costed" field indicates if the Capture COS/Wip Activity has run on that part transaction. If "Yes" the transaction costs cant be changed anymore.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR number used to identify the related DMR record.  """  
      self.ActionNum:int = obj["ActionNum"]
      """  DMR action number  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number  """  
      self.COSPostingReqd:bool = obj["COSPostingReqd"]
      """   If the amount of this PartTran was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped, its costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Plant2:str = obj["Plant2"]
      """  Site Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  Reference to the service call that the material is being issued for.  """  
      self.CallLine:int = obj["CallLine"]
      """  Reference to the service call line  that the material is being issued for.  """  
      self.MatNum:int = obj["MatNum"]
      """  Reference to the service call line Material sequence that the material is being issued for.  """  
      self.JobNum2:str = obj["JobNum2"]
      """  Job Number of transfer source/target.  """  
      self.AssemblySeq2:int = obj["AssemblySeq2"]
      """  Assembly Sequence  of transfer source/target.  """  
      self.JobSeq2:int = obj["JobSeq2"]
      """  Seq # of transfer source/target.  """  
      self.CustNum:int = obj["CustNum"]
      """   NOTE: Applies only to the RMA-INS transactions.
Contains the system internal customer number of the related customer record. 
Not directly updateable, updated via the RmaRcpt write trigger.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA Receipt  """  
      self.RMADisp:int = obj["RMADisp"]
      """  RMA Disposition  """  
      self.OtherDivValue:int = obj["OtherDivValue"]
      """  Other division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of Site transaction costs.  OtherDivValue only applies to Site to Site transactions (TranType="PLT-" and Site <> S  """  
      self.PlantTranNum:int = obj["PlantTranNum"]
      """  Site Transaction Number  """  
      self.NonConfID:int = obj["NonConfID"]
      """  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.BeginQty:int = obj["BeginQty"]
      """  On Hand Quantity before the part costing calculations were run.  """  
      self.AfterQty:int = obj["AfterQty"]
      """  On Hand Quantity after part costing calculation were run.  """  
      self.BegBurUnitCost:int = obj["BegBurUnitCost"]
      """  Burden Unit cost before the part costing calculation was run  """  
      self.BegLbrUnitCost:int = obj["BegLbrUnitCost"]
      """  Labor Unit cost before the costing calculation was run  """  
      self.BegMtlBurUnitCost:int = obj["BegMtlBurUnitCost"]
      """  Material Burden Unit Cost before the costing calculation was run  """  
      self.BegMtlUnitCost:int = obj["BegMtlUnitCost"]
      """  Material Unit Cost before the costing calculation was run  """  
      self.BegSubUnitCost:int = obj["BegSubUnitCost"]
      """  Sub Contract Unit Cost before the costing calculation was run  """  
      self.AfterBurUnitCost:int = obj["AfterBurUnitCost"]
      """  Burden Unit cost after the part costing calculation was run  """  
      self.AfterLbrUnitCost:int = obj["AfterLbrUnitCost"]
      """  Labor Unit Cost after the costing calculation was run  """  
      self.AfterMtlBurUnitCost:int = obj["AfterMtlBurUnitCost"]
      """  Material Burden Unit Cost after the costing calculation was run  """  
      self.AfterMtlUnitCost:int = obj["AfterMtlUnitCost"]
      """  Material Unit Cost after the costing calculation was run  """  
      self.AfterSubUnitCost:int = obj["AfterSubUnitCost"]
      """  Sub Contract Unit Cost after the costing calculation was run  """  
      self.PlantCostValue:int = obj["PlantCostValue"]
      """  To Site division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of To Site transaction costs.  SiteCostValue only applies to Site to Site transactions (TranType="PLT-" and Site  """  
      self.EmpID:str = obj["EmpID"]
      """  The Shop Employee ID of the user that created this transaction.  """  
      self.ReconcileNum:int = obj["ReconcileNum"]
      """  The unique identifier of the DemandReconcile that created this PartTran record.  """  
      self.CostID:str = obj["CostID"]
      """  Id to the Cost Set Group that is used as the default CostGrp.  """  
      self.FIFODate:str = obj["FIFODate"]
      """  For FIFO costed part, use this date to find the FIFO cost queue record affected by this transaction.  """  
      self.FIFOSeq:int = obj["FIFOSeq"]
      """  For FIFO costed part, use this sequence number to find the FIFO cost queue record affected by this transaction.  """  
      self.ActTranQty:int = obj["ActTranQty"]
      """   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  """  
      self.ActTransUOM:str = obj["ActTransUOM"]
      """  Actual Unit of Measure of the ActTransQty.  """  
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  The Inventory Tracking Unit of Measure that transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  """  
      self.InvtyUOM2:str = obj["InvtyUOM2"]
      """  The Inventory Tracking Unit of Measure that inventory transfer transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  """  
      self.FIFOAction:str = obj["FIFOAction"]
      """   Internal flag to indicate what type of FIFO update is needed.  Valid values are: (A/U/D)
"A" - Add new FIFO cost queue
"U" - Update existing FIFO cost queue
"D" - Delete existing FIFO cost queue (Technically, this is more of voiding/deactivating the FIFO since we don't delete historical FIFO records).  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BinType:str = obj["BinType"]
      """  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  """  
      self.CCYear:int = obj["CCYear"]
      """  Calendar year of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  """  
      self.CCMonth:int = obj["CCMonth"]
      """  Calendar month of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl..  """  
      self.CycleSeq:int = obj["CycleSeq"]
      """  CycleSeq of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  GUID - reference on PE ABT.  """  
      self.BaseCostMethod:str = obj["BaseCostMethod"]
      """  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the PartSite.CostMethod or Part.CostMethod  """  
      self.RevertStatus:int = obj["RevertStatus"]
      """   Revert Status field, with following values:
0.	Not reverted (default initial value)
1.	Reverted  """  
      self.RevertID:str = obj["RevertID"]
      """  Reference on revert line  by SySRowID.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.VarTarget:str = obj["VarTarget"]
      """   PartTran.VarTarget, with following values:
'JOB' ? Use Job Expense Account
'STK' ? Use Inventory Account
'VAR' ? Use Purchase Variance Account
'INS' ? Use Inspection Account
'UKN' ? Expense Account (Miscellaneous receipt)
'MTL' ? Use WIP Material Account
'SUB' ? Use WIP Subcontract account
'DMR' ? Use DMR account
'REJ' ? Use DMR Write off Account
'ACA' ? Use Actual Cost Account  """  
      self.FIFOSubSeq:int = obj["FIFOSubSeq"]
      """  The FIFO subsequence number of the related PartFIFOCost record.  """  
      self.AltMtlUnitCost:int = obj["AltMtlUnitCost"]
      """  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltLbrUnitCost:int = obj["AltLbrUnitCost"]
      """  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltBurUnitCost:int = obj["AltBurUnitCost"]
      """  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltSubUnitCost:int = obj["AltSubUnitCost"]
      """  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlBurUnitCost:int = obj["AltMtlBurUnitCost"]
      """  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltExtCost:int = obj["AltExtCost"]
      """  Alternate FIFO Extended Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlMtlUnitCost:int = obj["AltMtlMtlUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlLabUnitCost:int = obj["AltMtlLabUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlSubUnitCost:int = obj["AltMtlSubUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlBurdenUnitCost:int = obj["AltMtlBurdenUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.PBInvNum:int = obj["PBInvNum"]
      """  Invoice Number from Progress Billing Invoice preparation  """  
      self.LoanFlag:str = obj["LoanFlag"]
      """   This is only relevant for TranType MFG-MFG.
Valid types are '' , 'L', and 'B'.  
For Transfers, set to ''.
For Loans and Repayment of Loans set PartTran. LoanType to either 'L' or 'B' based on PartTran.JobNum.  If PartTran.JobNum is the job who is making the loan (or who made the loan, in the case of a repayment), then set to 'L' (loaner).  If PartTran.JobNum is the job who originally received the loan or who is receiving a loan set to 'B' (borrower).  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Unique identifier of the Asset.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Unique number to identify the Addition activity of an asset.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the Disposal activity of an asset.  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process.  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  Used by Project Analysis process.  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  Used By Project Analysis Process  """  
      self.MscNum:int = obj["MscNum"]
      """  Like RcvMisc.MscNum. Filled only for ADJ-PUR transactions created from late costs.  """  
      self.ODCUnitCost:int = obj["ODCUnitCost"]
      """  ODC Unit Cost  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TranRefType:int = obj["TranRefType"]
      """  TranRefType  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.PCIDCollapseCounter:int = obj["PCIDCollapseCounter"]
      """  PCIDCollapseCounter  """  
      self.PCID2:str = obj["PCID2"]
      """  PCID2  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  """  
      self.ExtMtlCost:int = obj["ExtMtlCost"]
      """  ExtMtlCost  """  
      self.ExtLbrCost:int = obj["ExtLbrCost"]
      """  ExtLbrCost  """  
      self.ExtBurCost:int = obj["ExtBurCost"]
      """  ExtBurCost  """  
      self.ExtSubCost:int = obj["ExtSubCost"]
      """  ExtSubCost  """  
      self.ExtMtlBurCost:int = obj["ExtMtlBurCost"]
      """  ExtMtlBurCost  """  
      self.ExtMtlMtlCost:int = obj["ExtMtlMtlCost"]
      """  ExtMtlMtlCost  """  
      self.ExtMtlLabCost:int = obj["ExtMtlLabCost"]
      """  ExtMtlLabCost  """  
      self.ExtMtlSubCost:int = obj["ExtMtlSubCost"]
      """  ExtMtlSubCost  """  
      self.ExtMtlBurdenCost:int = obj["ExtMtlBurdenCost"]
      """  ExtMtlBurdenCost  """  
      self.MYImportNum:str = obj["MYImportNum"]
      """  MYImportNum  """  
      self.AutoReverse:bool = obj["AutoReverse"]
      """  AutoReverse  """  
      self.RevTranNum:int = obj["RevTranNum"]
      """  RevTranNum  """  
      self.RevSysDate:str = obj["RevSysDate"]
      """  RevSysDate  """  
      self.RevSysTime:int = obj["RevSysTime"]
      """  RevSysTime  """  
      self.ExtNonRecoverableCost:int = obj["ExtNonRecoverableCost"]
      """  The Non Recoverable Tax that has been included on the Extended Cost.  This will be calculated from the Receipt Header and Receipt Line tax records by subtracting the total deductable tax from the total tax.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.WIPPCID:str = obj["WIPPCID"]
      """  WIPPCID  """  
      self.WIPPCID2:str = obj["WIPPCID2"]
      """  WIPPCID2  """  
      self.CallCode:str = obj["CallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.DIMDescription:str = obj["DIMDescription"]
      self.DisableFieldPart:bool = obj["DisableFieldPart"]
      """  Part field objects must be enabled when the Final Assembly (0) is selected and the Job has multiple end parts.  """  
      self.DispSysTime:str = obj["DispSysTime"]
      """  Display format of System Time in Hrs:Min.  """  
      self.DispUOM:str = obj["DispUOM"]
      self.dummyKeyField:str = obj["dummyKeyField"]
      self.EnableSerialNumbers:bool = obj["EnableSerialNumbers"]
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.FSACallCode:str = obj["FSACallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.FSAContractCode:str = obj["FSAContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.FSAContractNum:int = obj["FSAContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.FSAEmpID:str = obj["FSAEmpID"]
      """  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAWarrantyCode:str = obj["FSAWarrantyCode"]
      """  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  """  
      self.FullPhysical:bool = obj["FullPhysical"]
      """  If InvAdjSrc = "P", then this field is true, InvAdjSrc = "C", then this field is false  """  
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.InvBurUnitCost:int = obj["InvBurUnitCost"]
      """  Inventory subcontract unit cost  """  
      self.InvLbrUnitCost:int = obj["InvLbrUnitCost"]
      """  Inventory Labor unit cost.  """  
      self.InvMtlBurUnitCost:int = obj["InvMtlBurUnitCost"]
      """  Inventory burden unit cost  """  
      self.InvMtlUnitCost:int = obj["InvMtlUnitCost"]
      """  Inventory material unit cost  """  
      self.InvSubUnitCost:int = obj["InvSubUnitCost"]
      """  Inventory subcontract unit cost.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      self.JobBurUnitCost:int = obj["JobBurUnitCost"]
      self.JobLbrUnitCost:int = obj["JobLbrUnitCost"]
      self.JobMtlBurUnitCost:int = obj["JobMtlBurUnitCost"]
      self.JobMtlUnitCost:int = obj["JobMtlUnitCost"]
      self.JobSubUnitCost:int = obj["JobSubUnitCost"]
      self.LegalNumberNumber:str = obj["LegalNumberNumber"]
      self.LegalNumberPrefix:str = obj["LegalNumberPrefix"]
      self.LegalNumberPrefixList:str = obj["LegalNumberPrefixList"]
      self.LegalNumberReadOnlyFields:str = obj["LegalNumberReadOnlyFields"]
      self.LegalNumberYear:int = obj["LegalNumberYear"]
      self.MtlLbrUnitCost:int = obj["MtlLbrUnitCost"]
      self.MtlQueueRowId:str = obj["MtlQueueRowId"]
      self.MultiEndParts:bool = obj["MultiEndParts"]
      """  Used/Set only by MfgReceipts - Indicates if Job has multiple end parts.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      self.OverRideCosts:bool = obj["OverRideCosts"]
      """  Override Costs.  Set to yes if the user chooses to override the cost.  """  
      self.PartDescriptionAsm:str = obj["PartDescriptionAsm"]
      self.PartDescriptionJH:str = obj["PartDescriptionJH"]
      self.PartDescriptionMS:str = obj["PartDescriptionMS"]
      self.PartDescriptionSP:str = obj["PartDescriptionSP"]
      self.PartNumAsm:str = obj["PartNumAsm"]
      self.PartNumJH:str = obj["PartNumJH"]
      self.PartNumMS:str = obj["PartNumMS"]
      self.PartNumSP:str = obj["PartNumSP"]
      self.QtyAvailToComplete:int = obj["QtyAvailToComplete"]
      self.QtyBearing:bool = obj["QtyBearing"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      """  Quantity Completed  """  
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.SalvageQtyToDate:int = obj["SalvageQtyToDate"]
      self.SerialNoTempTranID:int = obj["SerialNoTempTranID"]
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.TranAmount:int = obj["TranAmount"]
      """  Transaction Amount  """  
      self.TreeDisplay:str = obj["TreeDisplay"]
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.CostMethodDisplay:str = obj["CostMethodDisplay"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts  """  
      self.RevisionNumAsm:str = obj["RevisionNumAsm"]
      self.RevisionNumMS:str = obj["RevisionNumMS"]
      self.RevisionNumSP:str = obj["RevisionNumSP"]
      self.PlantConfCtrlEnablePackageControl:bool = obj["PlantConfCtrlEnablePackageControl"]
      self.AttributeSetDescriptionMS:str = obj["AttributeSetDescriptionMS"]
      """  Description for AttributeSetID associated with PartNumMS  """  
      self.AttributeSetIDMS:int = obj["AttributeSetIDMS"]
      """  AttributeSetID associated with PartNumMS  """  
      self.AttributeSetShortDescriptionMS:str = obj["AttributeSetShortDescriptionMS"]
      """  AttributeSetShortDescription associated with PartNumMS  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumName:str = obj["CustNumName"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      self.FromBinDescription:str = obj["FromBinDescription"]
      self.FromPlantName:str = obj["FromPlantName"]
      self.FromWareHouseDescription:str = obj["FromWareHouseDescription"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.MatNumLineDesc:str = obj["MatNumLineDesc"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      self.PackNumName:str = obj["PackNumName"]
      self.PartLotPartLotDescription:str = obj["PartLotPartLotDescription"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PlantName:str = obj["PlantName"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorPPNumAddress1:str = obj["VendorPPNumAddress1"]
      self.VendorPPNumAddress2:str = obj["VendorPPNumAddress2"]
      self.VendorPPNumPrimPCon:int = obj["VendorPPNumPrimPCon"]
      self.VendorPPNumAddress3:str = obj["VendorPPNumAddress3"]
      self.VendorPPNumCountry:str = obj["VendorPPNumCountry"]
      self.VendorPPNumState:str = obj["VendorPPNumState"]
      self.VendorPPNumZip:str = obj["VendorPPNumZip"]
      self.VendorPPNumCity:str = obj["VendorPPNumCity"]
      self.VendorPPNumName:str = obj["VendorPPNumName"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartTranTableset:
   def __init__(self, obj):
      self.PartTran:list[Erp_Tablesets_PartTranRow] = obj["PartTran"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPartTranTableset:
   def __init__(self, obj):
      self.PartTran:list[Erp_Tablesets_PartTranRow] = obj["PartTran"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   sysDate
   sysTime
   tranNum
   """  
   def __init__(self, obj):
      self.sysDate:str = obj["sysDate"]
      self.sysTime:int = obj["sysTime"]
      self.tranNum:int = obj["tranNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartTranTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartTranTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartTranTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartTranListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPartTran_input:
   """ Required : 
   ds
   sysDate
   sysTime
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartTranTableset] = obj["ds"]
      self.sysDate:str = obj["sysDate"]
      self.sysTime:int = obj["sysTime"]
      pass

class GetNewPartTran_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartTranTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePartTran
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePartTran:str = obj["whereClausePartTran"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartTranTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetWhereClause_input:
   """ Required : 
   mode
   """  
   def __init__(self, obj):
      self.mode:str = obj["mode"]
      pass

class GetWhereClause_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPartTranTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPartTranTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartTranTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartTranTableset] = obj["ds"]
      pass

      """  output parameters  """  

