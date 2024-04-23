import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PeriodicAvgCostingWorkbenchSvc
# Description: Periodic Average CostingWorkbenchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PeriodicAvgCostingWorkbenches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PeriodicAvgCostingWorkbenches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PeriodicAvgCostingWorkbenches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PeriodicAverageCostHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/PeriodicAvgCostingWorkbenches",headers=creds) as resp:
           return await resp.json()

async def post_PeriodicAvgCostingWorkbenches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PeriodicAvgCostingWorkbenches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PeriodicAverageCostHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PeriodicAverageCostHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/PeriodicAvgCostingWorkbenches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PeriodicAvgCostingWorkbenches_Company_Plant_PeriodicAverageCostID_CalculationNum(Company, Plant, PeriodicAverageCostID, CalculationNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PeriodicAvgCostingWorkbench item
   Description: Calls GetByID to retrieve the PeriodicAvgCostingWorkbench item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PeriodicAvgCostingWorkbench
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param PeriodicAverageCostID: Desc: PeriodicAverageCostID   Required: True   Allow empty value : True
      :param CalculationNum: Desc: CalculationNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PeriodicAverageCostHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/PeriodicAvgCostingWorkbenches(" + Company + "," + Plant + "," + PeriodicAverageCostID + "," + CalculationNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PeriodicAvgCostingWorkbenches_Company_Plant_PeriodicAverageCostID_CalculationNum(Company, Plant, PeriodicAverageCostID, CalculationNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PeriodicAvgCostingWorkbench for the service
   Description: Calls UpdateExt to update PeriodicAvgCostingWorkbench. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PeriodicAvgCostingWorkbench
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param PeriodicAverageCostID: Desc: PeriodicAverageCostID   Required: True   Allow empty value : True
      :param CalculationNum: Desc: CalculationNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PeriodicAverageCostHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/PeriodicAvgCostingWorkbenches(" + Company + "," + Plant + "," + PeriodicAverageCostID + "," + CalculationNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PeriodicAvgCostingWorkbenches_Company_Plant_PeriodicAverageCostID_CalculationNum(Company, Plant, PeriodicAverageCostID, CalculationNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PeriodicAvgCostingWorkbench item
   Description: Call UpdateExt to delete PeriodicAvgCostingWorkbench item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PeriodicAvgCostingWorkbench
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param PeriodicAverageCostID: Desc: PeriodicAverageCostID   Required: True   Allow empty value : True
      :param CalculationNum: Desc: CalculationNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/PeriodicAvgCostingWorkbenches(" + Company + "," + Plant + "," + PeriodicAverageCostID + "," + CalculationNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PeriodicAverageCostHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePeriodicAverageCostHead, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePeriodicAverageCostHead=" + whereClausePeriodicAverageCostHead
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(plant, periodicAverageCostID, calculationNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "plant=" + plant
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "periodicAverageCostID=" + periodicAverageCostID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "calculationNum=" + calculationNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedFiscalYrPeriod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedFiscalYrPeriod
   Description: Sets FromDate and ToDate
   OperationID: OnChangedFiscalYrPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedFiscalYrPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedFiscalYrPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPeriodicAverageCostLineRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPeriodicAverageCostLineRows
   Description: Returns PeriodicAverageCostLine
   OperationID: GetPeriodicAverageCostLineRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPeriodicAverageCostLineRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPeriodicAverageCostLineRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPeriodicAverageCostHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPeriodicAverageCostHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPeriodicAverageCostHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPeriodicAverageCostHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPeriodicAverageCostHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PeriodicAverageCostHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PeriodicAverageCostHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PeriodicAverageCostHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PeriodicAverageCostHeadRow] = obj["value"]
      pass

class Erp_Tablesets_PeriodicAverageCostHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.PeriodicAverageCostID:str = obj["PeriodicAverageCostID"]
      """  Periodic Average Cost ID  """  
      self.CalculationNum:int = obj["CalculationNum"]
      """  Calculation Num  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.FromPeriod:int = obj["FromPeriod"]
      """  From Period  """  
      self.ToPeriod:int = obj["ToPeriod"]
      """  To Period  """  
      self.FromDate:str = obj["FromDate"]
      """  From Date  """  
      self.ToDate:str = obj["ToDate"]
      """  To Date  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Posted Date  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date  """  
      self.IncludePartZeroQty:bool = obj["IncludePartZeroQty"]
      """  Include Parts with Zero Quantities  """  
      self.IncludePartAnyCostMethod:bool = obj["IncludePartAnyCostMethod"]
      """  Include Parts with any Costing Method  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PeriodicAverageCostHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.PeriodicAverageCostID:str = obj["PeriodicAverageCostID"]
      """  Periodic Average Cost ID  """  
      self.CalculationNum:int = obj["CalculationNum"]
      """  Calculation Num  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.FromPeriod:int = obj["FromPeriod"]
      """  From Period  """  
      self.ToPeriod:int = obj["ToPeriod"]
      """  To Period  """  
      self.FromDate:str = obj["FromDate"]
      """  From Date  """  
      self.ToDate:str = obj["ToDate"]
      """  To Date  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Posted Date  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date  """  
      self.IncludePartZeroQty:bool = obj["IncludePartZeroQty"]
      """  Include Parts with Zero Quantities  """  
      self.IncludePartAnyCostMethod:bool = obj["IncludePartAnyCostMethod"]
      """  Include Parts with any Costing Method  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Generated:bool = obj["Generated"]
      self.IsTheFirstCalculation:bool = obj["IsTheFirstCalculation"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   plant
   periodicAverageCostID
   calculationNum
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.periodicAverageCostID:str = obj["periodicAverageCostID"]
      self.calculationNum:int = obj["calculationNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PeriodicAverageCostHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.PeriodicAverageCostID:str = obj["PeriodicAverageCostID"]
      """  Periodic Average Cost ID  """  
      self.CalculationNum:int = obj["CalculationNum"]
      """  Calculation Num  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.FromPeriod:int = obj["FromPeriod"]
      """  From Period  """  
      self.ToPeriod:int = obj["ToPeriod"]
      """  To Period  """  
      self.FromDate:str = obj["FromDate"]
      """  From Date  """  
      self.ToDate:str = obj["ToDate"]
      """  To Date  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Posted Date  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date  """  
      self.IncludePartZeroQty:bool = obj["IncludePartZeroQty"]
      """  Include Parts with Zero Quantities  """  
      self.IncludePartAnyCostMethod:bool = obj["IncludePartAnyCostMethod"]
      """  Include Parts with any Costing Method  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PeriodicAverageCostHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.PeriodicAverageCostID:str = obj["PeriodicAverageCostID"]
      """  Periodic Average Cost ID  """  
      self.CalculationNum:int = obj["CalculationNum"]
      """  Calculation Num  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.FromPeriod:int = obj["FromPeriod"]
      """  From Period  """  
      self.ToPeriod:int = obj["ToPeriod"]
      """  To Period  """  
      self.FromDate:str = obj["FromDate"]
      """  From Date  """  
      self.ToDate:str = obj["ToDate"]
      """  To Date  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Posted Date  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date  """  
      self.IncludePartZeroQty:bool = obj["IncludePartZeroQty"]
      """  Include Parts with Zero Quantities  """  
      self.IncludePartAnyCostMethod:bool = obj["IncludePartAnyCostMethod"]
      """  Include Parts with any Costing Method  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Generated:bool = obj["Generated"]
      self.IsTheFirstCalculation:bool = obj["IsTheFirstCalculation"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PeriodicAverageCostLineListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.PeriodicAverageCostID:str = obj["PeriodicAverageCostID"]
      """  Periodic Average Cost ID  """  
      self.CalculationNum:int = obj["CalculationNum"]
      """  Calculation Num  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Num  """  
      self.UOM:str = obj["UOM"]
      """  UOM  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Received Qunatity  """  
      self.SoldQty:int = obj["SoldQty"]
      """  Sold Qunatity  """  
      self.OnHandQtyStart:int = obj["OnHandQtyStart"]
      """  On-hand Qunatity Start  """  
      self.OnHandQtyEnd:int = obj["OnHandQtyEnd"]
      """  On-hand Qunatity End  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Cost Method  """  
      self.CurrentMaterialCost:int = obj["CurrentMaterialCost"]
      """  Original Material Cost  """  
      self.CurrentMtlBurCost:int = obj["CurrentMtlBurCost"]
      """  Original Material Burden Cost  """  
      self.CurrentLaborCost:int = obj["CurrentLaborCost"]
      """  Original Labor Cost  """  
      self.CurrentBurdenCost:int = obj["CurrentBurdenCost"]
      """  Original Burden Cost  """  
      self.CurrentSubContCost:int = obj["CurrentSubContCost"]
      """  Original Subcontract Cost  """  
      self.CurrentExtendedCost:int = obj["CurrentExtendedCost"]
      """  Original Extended Cost  """  
      self.StartMaterialCost:int = obj["StartMaterialCost"]
      """  Start Material Cost  """  
      self.StartMtlBurCost:int = obj["StartMtlBurCost"]
      """  Start Material Burden Cost  """  
      self.StartLaborCost:int = obj["StartLaborCost"]
      """  Start Labor Cost  """  
      self.StartBurdenCost:int = obj["StartBurdenCost"]
      """  Start Burden Cost  """  
      self.StartSubContCost:int = obj["StartSubContCost"]
      """  Start Subcontract Cost  """  
      self.StartExtendedCost:int = obj["StartExtendedCost"]
      """  Start Extended Cost  """  
      self.PACMaterialCost:int = obj["PACMaterialCost"]
      """  PAC Material Cost  """  
      self.PACMtlBurCost:int = obj["PACMtlBurCost"]
      """  PAC Materilal Burden Cost  """  
      self.PACLaborCost:int = obj["PACLaborCost"]
      """  PAC Labor Cost  """  
      self.PACBurdenCost:int = obj["PACBurdenCost"]
      """  PAC Burden Cost  """  
      self.PACSubContCost:int = obj["PACSubContCost"]
      """  PAC Subcontract Cost  """  
      self.PACExtendedCost:int = obj["PACExtendedCost"]
      """  PAC Extended Cost  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CostMethodDesc:str = obj["CostMethodDesc"]
      self.FromDate:str = obj["FromDate"]
      self.ToDate:str = obj["ToDate"]
      self.PostedDate:str = obj["PostedDate"]
      self.Posted:bool = obj["Posted"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PeriodicAverageCostLineTableset:
   def __init__(self, obj):
      self.PeriodicAverageCostLineList:list[Erp_Tablesets_PeriodicAverageCostLineListRow] = obj["PeriodicAverageCostLineList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PeriodicAvgCostWorkbenchListTableset:
   def __init__(self, obj):
      self.PeriodicAverageCostHeadList:list[Erp_Tablesets_PeriodicAverageCostHeadListRow] = obj["PeriodicAverageCostHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PeriodicAvgCostingWorkbenchTableset:
   def __init__(self, obj):
      self.PeriodicAverageCostHead:list[Erp_Tablesets_PeriodicAverageCostHeadRow] = obj["PeriodicAverageCostHead"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPeriodicAvgCostingWorkbenchTableset:
   def __init__(self, obj):
      self.PeriodicAverageCostHead:list[Erp_Tablesets_PeriodicAverageCostHeadRow] = obj["PeriodicAverageCostHead"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   plant
   periodicAverageCostID
   calculationNum
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.periodicAverageCostID:str = obj["periodicAverageCostID"]
      self.calculationNum:int = obj["calculationNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PeriodicAvgCostingWorkbenchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PeriodicAvgCostingWorkbenchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PeriodicAvgCostingWorkbenchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PeriodicAvgCostWorkbenchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPeriodicAverageCostHead_input:
   """ Required : 
   ds
   plant
   periodicAverageCostID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PeriodicAvgCostingWorkbenchTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      self.periodicAverageCostID:str = obj["periodicAverageCostID"]
      pass

class GetNewPeriodicAverageCostHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PeriodicAvgCostingWorkbenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPeriodicAverageCostLineRows_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetPeriodicAverageCostLineRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PeriodicAverageCostLineTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePeriodicAverageCostHead
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePeriodicAverageCostHead:str = obj["whereClausePeriodicAverageCostHead"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PeriodicAvgCostingWorkbenchTableset] = obj["returnObj"]
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

class OnChangedFiscalYrPeriod_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PeriodicAvgCostingWorkbenchTableset] = obj["ds"]
      pass

class OnChangedFiscalYrPeriod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PeriodicAvgCostingWorkbenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPeriodicAvgCostingWorkbenchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPeriodicAvgCostingWorkbenchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PeriodicAvgCostingWorkbenchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PeriodicAvgCostingWorkbenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

