import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PartFIFOCostSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PartFIFOCosts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartFIFOCosts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartFIFOCosts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartFIFOCostRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/PartFIFOCosts",headers=creds) as resp:
           return await resp.json()

async def post_PartFIFOCosts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartFIFOCosts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartFIFOCostRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartFIFOCostRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/PartFIFOCosts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PartFIFOCosts_Company_PartNum_LotNum_CostID_FIFODate_FIFOSeq_FIFOSubSeq(Company, PartNum, LotNum, CostID, FIFODate, FIFOSeq, FIFOSubSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartFIFOCost item
   Description: Calls GetByID to retrieve the PartFIFOCost item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartFIFOCost
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param CostID: Desc: CostID   Required: True   Allow empty value : True
      :param FIFODate: Desc: FIFODate   Required: True   Allow empty value : True
      :param FIFOSeq: Desc: FIFOSeq   Required: True
      :param FIFOSubSeq: Desc: FIFOSubSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartFIFOCostRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/PartFIFOCosts(" + Company + "," + PartNum + "," + LotNum + "," + CostID + "," + FIFODate + "," + FIFOSeq + "," + FIFOSubSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PartFIFOCosts_Company_PartNum_LotNum_CostID_FIFODate_FIFOSeq_FIFOSubSeq(Company, PartNum, LotNum, CostID, FIFODate, FIFOSeq, FIFOSubSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PartFIFOCost for the service
   Description: Calls UpdateExt to update PartFIFOCost. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartFIFOCost
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param CostID: Desc: CostID   Required: True   Allow empty value : True
      :param FIFODate: Desc: FIFODate   Required: True   Allow empty value : True
      :param FIFOSeq: Desc: FIFOSeq   Required: True
      :param FIFOSubSeq: Desc: FIFOSubSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartFIFOCostRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/PartFIFOCosts(" + Company + "," + PartNum + "," + LotNum + "," + CostID + "," + FIFODate + "," + FIFOSeq + "," + FIFOSubSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PartFIFOCosts_Company_PartNum_LotNum_CostID_FIFODate_FIFOSeq_FIFOSubSeq(Company, PartNum, LotNum, CostID, FIFODate, FIFOSeq, FIFOSubSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PartFIFOCost item
   Description: Call UpdateExt to delete PartFIFOCost item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartFIFOCost
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param CostID: Desc: CostID   Required: True   Allow empty value : True
      :param FIFODate: Desc: FIFODate   Required: True   Allow empty value : True
      :param FIFOSeq: Desc: FIFOSeq   Required: True
      :param FIFOSubSeq: Desc: FIFOSubSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/PartFIFOCosts(" + Company + "," + PartNum + "," + LotNum + "," + CostID + "," + FIFODate + "," + FIFOSeq + "," + FIFOSubSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartFIFOCostListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePartFIFOCost, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePartFIFOCost=" + whereClausePartFIFOCost
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(partNum, lotNum, costID, fiFODate, fiFOSeq, fiFOSubSeq, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "partNum=" + partNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "lotNum=" + lotNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "costID=" + costID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fiFODate=" + fiFODate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fiFOSeq=" + fiFOSeq
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fiFOSubSeq=" + fiFOSubSeq

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartFIFOCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartFIFOCost
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartFIFOCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartFIFOCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartFIFOCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartFIFOCostListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartFIFOCostListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartFIFOCostRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartFIFOCostRow] = obj["value"]
      pass

class Erp_Tablesets_PartFIFOCostListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.CostID:str = obj["CostID"]
      """  Included in the unique index this value allows the Part to have different costs in different Sites.  Default value for CostID = 1.  """  
      self.FIFODate:str = obj["FIFODate"]
      """  This could be the transaction date or the system date at the time this FIFO cost record was created.  Depending on the setting at Company Configuration (XbSyst.UseTranDate).  """  
      self.FIFOSeq:int = obj["FIFOSeq"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.FIFOSubSeq:int = obj["FIFOSubSeq"]
      """  A subsequence number which is used to create a unique FIFO Sequence within the same FIFO Date.  """  
      self.InActive:bool = obj["InActive"]
      """   Flag which indicates if the Part FIFO cost queue is considered as "Inactive".  This flag will be used to exclude FIFO from the queue of valid FIFO costs.
This flag will be used to exclude parts from certain searches and reports.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  Holds the Quantity On Hand for this Part FIFO cost queue.  Whenever this quantity becomes zero the record should be deactivated.  This quantity is updated by Manufactured receipts, Purchased receipts, Physical inventories, Inventory issues, Warehouse transfers, Shipping and Adjustments.  """  
      self.FIFOLaborCost:int = obj["FIFOLaborCost"]
      """   FIFO Unit Labor Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  """  
      self.FIFOBurdenCost:int = obj["FIFOBurdenCost"]
      """   FIFO Unit Burden Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  """  
      self.FIFOMaterialCost:int = obj["FIFOMaterialCost"]
      """   FIFO Unit Material Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  """  
      self.FIFOSubContCost:int = obj["FIFOSubContCost"]
      """   FIFO Unit Subcontract Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  """  
      self.FIFOMtlBurCost:int = obj["FIFOMtlBurCost"]
      """   FIFO Unit Material Burden Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.SourceType:str = obj["SourceType"]
      """  An internal code to identify the source transaction that created this FIFO cost queue.  To make it match with the source PartTran that created it, SourceType will have the same value as the source transaction type if part's cost method is FIFO or LOT FIFO.  But if the source is a non-FIFO part and FIFO Layer is enabled then Source Type is "NON-FIFO":U.  """  
      self.SourceSysDate:str = obj["SourceSysDate"]
      """  System date of the source PartTran that created this FIFO cost queue record.  """  
      self.SourceSysTime:int = obj["SourceSysTime"]
      """  System Time (hr-min-sec) of the source PartTran that created this FIFO cost queue record.  """  
      self.SourceTranNum:int = obj["SourceTranNum"]
      """  The Transaction number of the source PartTran that created this FIFO cost queue record.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  One of the internal keys that is used to tie back to the RcvDtl.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  One of the internal keys that is used to tie back to the RcvDtl.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  One of the internal keys that is used to tie back to the RcvDtl.  """  
      self.PackLine:int = obj["PackLine"]
      """  One of the internal keys that is used to tie back to the RcvDtl.  """  
      self.OrigOnHandQty:int = obj["OrigOnHandQty"]
      """  Holds the original Quantity On Hand of the Part FIFO cost when first created.  """  
      self.ConsumedQty:int = obj["ConsumedQty"]
      """  Holds the quantity consumed from this Part FIFO cost queue.  This quantity plus the OnHand quantity will equal the OrigOnHandQty in most cases.  But in the event where the FIFO cost queue is deactivated due to backing out of the transaction then the OrigOnHandQty and OnHandQty are set to zero but ConsumedQty retains its value.  """  
      self.LastRefDate:str = obj["LastRefDate"]
      """  Latest date that the FIFO cost record was referenced.  """  
      self.SourceTable:str = obj["SourceTable"]
      """  Identifies the transaction file that created this FIFO cost.  """  
      self.SourceKey1:str = obj["SourceKey1"]
      """  First component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SourceKey2:str = obj["SourceKey2"]
      """  2nd component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SourceKey3:str = obj["SourceKey3"]
      """  3rd component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SourceKey4:str = obj["SourceKey4"]
      """  4th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SourceKey5:str = obj["SourceKey5"]
      """  5th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SourceKey6:str = obj["SourceKey6"]
      """  6th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartFIFOCostRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.CostID:str = obj["CostID"]
      """  Included in the unique index this value allows the Part to have different costs in different Sites.  Default value for CostID = 1.  """  
      self.FIFODate:str = obj["FIFODate"]
      """  This could be the transaction date or the system date at the time this FIFO cost record was created.  Depending on the setting at Company Configuration (XbSyst.UseTranDate).  """  
      self.FIFOSeq:int = obj["FIFOSeq"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.FIFOSubSeq:int = obj["FIFOSubSeq"]
      """  A subsequence number which is used to create a unique FIFO Sequence within the same FIFO Date.  """  
      self.InActive:bool = obj["InActive"]
      """   Flag which indicates if the Part FIFO cost queue is considered as "Inactive".  This flag will be used to exclude FIFO from the queue of valid FIFO costs.
This flag will be used to exclude parts from certain searches and reports.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  Holds the Quantity On Hand for this Part FIFO cost queue.  Whenever this quantity becomes zero the record should be deactivated.  This quantity is updated by Manufactured receipts, Purchased receipts, Physical inventories, Inventory issues, Warehouse transfers, Shipping and Adjustments.  """  
      self.FIFOLaborCost:int = obj["FIFOLaborCost"]
      """   FIFO Unit Labor Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  """  
      self.FIFOBurdenCost:int = obj["FIFOBurdenCost"]
      """   FIFO Unit Burden Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  """  
      self.FIFOMaterialCost:int = obj["FIFOMaterialCost"]
      """   FIFO Unit Material Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  """  
      self.FIFOSubContCost:int = obj["FIFOSubContCost"]
      """   FIFO Unit Subcontract Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  """  
      self.FIFOMtlBurCost:int = obj["FIFOMtlBurCost"]
      """   FIFO Unit Material Burden Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.SourceType:str = obj["SourceType"]
      """  An internal code to identify the source transaction that created this FIFO cost queue.  To make it match with the source PartTran that created it, SourceType will have the same value as the source transaction type if part's cost method is FIFO or LOT FIFO.  But if the source is a non-FIFO part and FIFO Layer is enabled then Source Type is "NON-FIFO":U.  """  
      self.SourceSysDate:str = obj["SourceSysDate"]
      """  System date of the source PartTran that created this FIFO cost queue record.  """  
      self.SourceSysTime:int = obj["SourceSysTime"]
      """  System Time (hr-min-sec) of the source PartTran that created this FIFO cost queue record.  """  
      self.SourceTranNum:int = obj["SourceTranNum"]
      """  The Transaction number of the source PartTran that created this FIFO cost queue record.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  One of the internal keys that is used to tie back to the RcvDtl.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  One of the internal keys that is used to tie back to the RcvDtl.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  One of the internal keys that is used to tie back to the RcvDtl.  """  
      self.PackLine:int = obj["PackLine"]
      """  One of the internal keys that is used to tie back to the RcvDtl.  """  
      self.OrigOnHandQty:int = obj["OrigOnHandQty"]
      """  Holds the original Quantity On Hand of the Part FIFO cost when first created.  """  
      self.ConsumedQty:int = obj["ConsumedQty"]
      """  Holds the quantity consumed from this Part FIFO cost queue.  This quantity plus the OnHand quantity will equal the OrigOnHandQty in most cases.  But in the event where the FIFO cost queue is deactivated due to backing out of the transaction then the OrigOnHandQty and OnHandQty are set to zero but ConsumedQty retains its value.  """  
      self.LastRefDate:str = obj["LastRefDate"]
      """  Latest date that the FIFO cost record was referenced.  """  
      self.SourceTable:str = obj["SourceTable"]
      """  Identifies the transaction file that created this FIFO cost.  """  
      self.SourceKey1:str = obj["SourceKey1"]
      """  First component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SourceKey2:str = obj["SourceKey2"]
      """  2nd component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SourceKey3:str = obj["SourceKey3"]
      """  3rd component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SourceKey4:str = obj["SourceKey4"]
      """  4th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SourceKey5:str = obj["SourceKey5"]
      """  5th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SourceKey6:str = obj["SourceKey6"]
      """  6th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartTranExtNonRecoverableCost:int = obj["PartTranExtNonRecoverableCost"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   partNum
   lotNum
   costID
   fiFODate
   fiFOSeq
   fiFOSubSeq
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.lotNum:str = obj["lotNum"]
      self.costID:str = obj["costID"]
      self.fiFODate:str = obj["fiFODate"]
      self.fiFOSeq:int = obj["fiFOSeq"]
      self.fiFOSubSeq:int = obj["fiFOSubSeq"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PartFIFOCostListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.CostID:str = obj["CostID"]
      """  Included in the unique index this value allows the Part to have different costs in different Sites.  Default value for CostID = 1.  """  
      self.FIFODate:str = obj["FIFODate"]
      """  This could be the transaction date or the system date at the time this FIFO cost record was created.  Depending on the setting at Company Configuration (XbSyst.UseTranDate).  """  
      self.FIFOSeq:int = obj["FIFOSeq"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.FIFOSubSeq:int = obj["FIFOSubSeq"]
      """  A subsequence number which is used to create a unique FIFO Sequence within the same FIFO Date.  """  
      self.InActive:bool = obj["InActive"]
      """   Flag which indicates if the Part FIFO cost queue is considered as "Inactive".  This flag will be used to exclude FIFO from the queue of valid FIFO costs.
This flag will be used to exclude parts from certain searches and reports.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  Holds the Quantity On Hand for this Part FIFO cost queue.  Whenever this quantity becomes zero the record should be deactivated.  This quantity is updated by Manufactured receipts, Purchased receipts, Physical inventories, Inventory issues, Warehouse transfers, Shipping and Adjustments.  """  
      self.FIFOLaborCost:int = obj["FIFOLaborCost"]
      """   FIFO Unit Labor Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  """  
      self.FIFOBurdenCost:int = obj["FIFOBurdenCost"]
      """   FIFO Unit Burden Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  """  
      self.FIFOMaterialCost:int = obj["FIFOMaterialCost"]
      """   FIFO Unit Material Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  """  
      self.FIFOSubContCost:int = obj["FIFOSubContCost"]
      """   FIFO Unit Subcontract Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  """  
      self.FIFOMtlBurCost:int = obj["FIFOMtlBurCost"]
      """   FIFO Unit Material Burden Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.SourceType:str = obj["SourceType"]
      """  An internal code to identify the source transaction that created this FIFO cost queue.  To make it match with the source PartTran that created it, SourceType will have the same value as the source transaction type if part's cost method is FIFO or LOT FIFO.  But if the source is a non-FIFO part and FIFO Layer is enabled then Source Type is "NON-FIFO":U.  """  
      self.SourceSysDate:str = obj["SourceSysDate"]
      """  System date of the source PartTran that created this FIFO cost queue record.  """  
      self.SourceSysTime:int = obj["SourceSysTime"]
      """  System Time (hr-min-sec) of the source PartTran that created this FIFO cost queue record.  """  
      self.SourceTranNum:int = obj["SourceTranNum"]
      """  The Transaction number of the source PartTran that created this FIFO cost queue record.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  One of the internal keys that is used to tie back to the RcvDtl.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  One of the internal keys that is used to tie back to the RcvDtl.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  One of the internal keys that is used to tie back to the RcvDtl.  """  
      self.PackLine:int = obj["PackLine"]
      """  One of the internal keys that is used to tie back to the RcvDtl.  """  
      self.OrigOnHandQty:int = obj["OrigOnHandQty"]
      """  Holds the original Quantity On Hand of the Part FIFO cost when first created.  """  
      self.ConsumedQty:int = obj["ConsumedQty"]
      """  Holds the quantity consumed from this Part FIFO cost queue.  This quantity plus the OnHand quantity will equal the OrigOnHandQty in most cases.  But in the event where the FIFO cost queue is deactivated due to backing out of the transaction then the OrigOnHandQty and OnHandQty are set to zero but ConsumedQty retains its value.  """  
      self.LastRefDate:str = obj["LastRefDate"]
      """  Latest date that the FIFO cost record was referenced.  """  
      self.SourceTable:str = obj["SourceTable"]
      """  Identifies the transaction file that created this FIFO cost.  """  
      self.SourceKey1:str = obj["SourceKey1"]
      """  First component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SourceKey2:str = obj["SourceKey2"]
      """  2nd component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SourceKey3:str = obj["SourceKey3"]
      """  3rd component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SourceKey4:str = obj["SourceKey4"]
      """  4th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SourceKey5:str = obj["SourceKey5"]
      """  5th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SourceKey6:str = obj["SourceKey6"]
      """  6th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartFIFOCostListTableset:
   def __init__(self, obj):
      self.PartFIFOCostList:list[Erp_Tablesets_PartFIFOCostListRow] = obj["PartFIFOCostList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartFIFOCostRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.CostID:str = obj["CostID"]
      """  Included in the unique index this value allows the Part to have different costs in different Sites.  Default value for CostID = 1.  """  
      self.FIFODate:str = obj["FIFODate"]
      """  This could be the transaction date or the system date at the time this FIFO cost record was created.  Depending on the setting at Company Configuration (XbSyst.UseTranDate).  """  
      self.FIFOSeq:int = obj["FIFOSeq"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.FIFOSubSeq:int = obj["FIFOSubSeq"]
      """  A subsequence number which is used to create a unique FIFO Sequence within the same FIFO Date.  """  
      self.InActive:bool = obj["InActive"]
      """   Flag which indicates if the Part FIFO cost queue is considered as "Inactive".  This flag will be used to exclude FIFO from the queue of valid FIFO costs.
This flag will be used to exclude parts from certain searches and reports.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  Holds the Quantity On Hand for this Part FIFO cost queue.  Whenever this quantity becomes zero the record should be deactivated.  This quantity is updated by Manufactured receipts, Purchased receipts, Physical inventories, Inventory issues, Warehouse transfers, Shipping and Adjustments.  """  
      self.FIFOLaborCost:int = obj["FIFOLaborCost"]
      """   FIFO Unit Labor Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  """  
      self.FIFOBurdenCost:int = obj["FIFOBurdenCost"]
      """   FIFO Unit Burden Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  """  
      self.FIFOMaterialCost:int = obj["FIFOMaterialCost"]
      """   FIFO Unit Material Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  """  
      self.FIFOSubContCost:int = obj["FIFOSubContCost"]
      """   FIFO Unit Subcontract Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  """  
      self.FIFOMtlBurCost:int = obj["FIFOMtlBurCost"]
      """   FIFO Unit Material Burden Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.SourceType:str = obj["SourceType"]
      """  An internal code to identify the source transaction that created this FIFO cost queue.  To make it match with the source PartTran that created it, SourceType will have the same value as the source transaction type if part's cost method is FIFO or LOT FIFO.  But if the source is a non-FIFO part and FIFO Layer is enabled then Source Type is "NON-FIFO":U.  """  
      self.SourceSysDate:str = obj["SourceSysDate"]
      """  System date of the source PartTran that created this FIFO cost queue record.  """  
      self.SourceSysTime:int = obj["SourceSysTime"]
      """  System Time (hr-min-sec) of the source PartTran that created this FIFO cost queue record.  """  
      self.SourceTranNum:int = obj["SourceTranNum"]
      """  The Transaction number of the source PartTran that created this FIFO cost queue record.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  One of the internal keys that is used to tie back to the RcvDtl.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  One of the internal keys that is used to tie back to the RcvDtl.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  One of the internal keys that is used to tie back to the RcvDtl.  """  
      self.PackLine:int = obj["PackLine"]
      """  One of the internal keys that is used to tie back to the RcvDtl.  """  
      self.OrigOnHandQty:int = obj["OrigOnHandQty"]
      """  Holds the original Quantity On Hand of the Part FIFO cost when first created.  """  
      self.ConsumedQty:int = obj["ConsumedQty"]
      """  Holds the quantity consumed from this Part FIFO cost queue.  This quantity plus the OnHand quantity will equal the OrigOnHandQty in most cases.  But in the event where the FIFO cost queue is deactivated due to backing out of the transaction then the OrigOnHandQty and OnHandQty are set to zero but ConsumedQty retains its value.  """  
      self.LastRefDate:str = obj["LastRefDate"]
      """  Latest date that the FIFO cost record was referenced.  """  
      self.SourceTable:str = obj["SourceTable"]
      """  Identifies the transaction file that created this FIFO cost.  """  
      self.SourceKey1:str = obj["SourceKey1"]
      """  First component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SourceKey2:str = obj["SourceKey2"]
      """  2nd component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SourceKey3:str = obj["SourceKey3"]
      """  3rd component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SourceKey4:str = obj["SourceKey4"]
      """  4th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SourceKey5:str = obj["SourceKey5"]
      """  5th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SourceKey6:str = obj["SourceKey6"]
      """  6th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartTranExtNonRecoverableCost:int = obj["PartTranExtNonRecoverableCost"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartFIFOCostTableset:
   def __init__(self, obj):
      self.PartFIFOCost:list[Erp_Tablesets_PartFIFOCostRow] = obj["PartFIFOCost"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPartFIFOCostTableset:
   def __init__(self, obj):
      self.PartFIFOCost:list[Erp_Tablesets_PartFIFOCostRow] = obj["PartFIFOCost"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   partNum
   lotNum
   costID
   fiFODate
   fiFOSeq
   fiFOSubSeq
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.lotNum:str = obj["lotNum"]
      self.costID:str = obj["costID"]
      self.fiFODate:str = obj["fiFODate"]
      self.fiFOSeq:int = obj["fiFOSeq"]
      self.fiFOSubSeq:int = obj["fiFOSubSeq"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartFIFOCostTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartFIFOCostTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartFIFOCostTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartFIFOCostListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPartFIFOCost_input:
   """ Required : 
   ds
   partNum
   lotNum
   costID
   fiFODate
   fiFOSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartFIFOCostTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.lotNum:str = obj["lotNum"]
      self.costID:str = obj["costID"]
      self.fiFODate:str = obj["fiFODate"]
      self.fiFOSeq:int = obj["fiFOSeq"]
      pass

class GetNewPartFIFOCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartFIFOCostTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePartFIFOCost
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePartFIFOCost:str = obj["whereClausePartFIFOCost"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartFIFOCostTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

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
      self.ds:list[Erp_Tablesets_UpdExtPartFIFOCostTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPartFIFOCostTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartFIFOCostTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartFIFOCostTableset] = obj["ds"]
      pass

      """  output parameters  """  

