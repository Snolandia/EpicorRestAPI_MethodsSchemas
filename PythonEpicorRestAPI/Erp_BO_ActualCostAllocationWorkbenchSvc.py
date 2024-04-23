import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ActualCostAllocationWorkbenchSvc
# Description: Actual Cost Allocation Workbench
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostAllocationWorkbenchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostAllocationWorkbenchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ActualCostAllocationWorkbenches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ActualCostAllocationWorkbenches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ActualCostAllocationWorkbenches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ActualCostAllocationHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostAllocationWorkbenchSvc/ActualCostAllocationWorkbenches",headers=creds) as resp:
           return await resp.json()

async def post_ActualCostAllocationWorkbenches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ActualCostAllocationWorkbenches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ActualCostAllocationHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ActualCostAllocationHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostAllocationWorkbenchSvc/ActualCostAllocationWorkbenches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ActualCostAllocationWorkbenches_Company_Plant_ActualCostingCategoryID_AllocationNum(Company, Plant, ActualCostingCategoryID, AllocationNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ActualCostAllocationWorkbench item
   Description: Calls GetByID to retrieve the ActualCostAllocationWorkbench item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ActualCostAllocationWorkbench
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ActualCostingCategoryID: Desc: ActualCostingCategoryID   Required: True   Allow empty value : True
      :param AllocationNum: Desc: AllocationNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ActualCostAllocationHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostAllocationWorkbenchSvc/ActualCostAllocationWorkbenches(" + Company + "," + Plant + "," + ActualCostingCategoryID + "," + AllocationNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ActualCostAllocationWorkbenches_Company_Plant_ActualCostingCategoryID_AllocationNum(Company, Plant, ActualCostingCategoryID, AllocationNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ActualCostAllocationWorkbench for the service
   Description: Calls UpdateExt to update ActualCostAllocationWorkbench. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ActualCostAllocationWorkbench
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ActualCostingCategoryID: Desc: ActualCostingCategoryID   Required: True   Allow empty value : True
      :param AllocationNum: Desc: AllocationNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ActualCostAllocationHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostAllocationWorkbenchSvc/ActualCostAllocationWorkbenches(" + Company + "," + Plant + "," + ActualCostingCategoryID + "," + AllocationNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ActualCostAllocationWorkbenches_Company_Plant_ActualCostingCategoryID_AllocationNum(Company, Plant, ActualCostingCategoryID, AllocationNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ActualCostAllocationWorkbench item
   Description: Call UpdateExt to delete ActualCostAllocationWorkbench item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ActualCostAllocationWorkbench
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ActualCostingCategoryID: Desc: ActualCostingCategoryID   Required: True   Allow empty value : True
      :param AllocationNum: Desc: AllocationNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostAllocationWorkbenchSvc/ActualCostAllocationWorkbenches(" + Company + "," + Plant + "," + ActualCostingCategoryID + "," + AllocationNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ActualCostAllocHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostAllocationWorkbenchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseActualCostAllocationHead, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseActualCostAllocationHead=" + whereClauseActualCostAllocationHead
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostAllocationWorkbenchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(plant, actualCostingCategoryID, allocationNum, epicorHeaders = None):
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
   params += "actualCostingCategoryID=" + actualCostingCategoryID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "allocationNum=" + allocationNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostAllocationWorkbenchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostAllocationWorkbenchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostAllocationWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingActualCostingCategoryID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingActualCostingCategoryID
   Description: ActualCostingCategoryID is changing
   OperationID: OnChangingActualCostingCategoryID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingActualCostingCategoryID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingActualCostingCategoryID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostAllocationWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetActualCostAllocationLineRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetActualCostAllocationLineRows
   Description: Returns ActualCostAllocationLine
   OperationID: GetActualCostAllocationLineRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetActualCostAllocationLineRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetActualCostAllocationLineRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostAllocationWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCutoffDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCutoffDate
   Description: CutoffDate check
   OperationID: CheckCutoffDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCutoffDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCutoffDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostAllocationWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewActualCostAllocationHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewActualCostAllocationHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewActualCostAllocationHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewActualCostAllocationHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewActualCostAllocationHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostAllocationWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostAllocationWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostAllocationWorkbenchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostAllocationWorkbenchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostAllocationWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostAllocationWorkbenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ActualCostAllocHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ActualCostAllocHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ActualCostAllocationHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ActualCostAllocationHeadRow] = obj["value"]
      pass

class Erp_Tablesets_ActualCostAllocHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Site  """  
      self.ActualCostingCategoryID:str = obj["ActualCostingCategoryID"]
      """  Actual Costing Category ID  """  
      self.AllocationNum:int = obj["AllocationNum"]
      """  Allocation Number  """  
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
      self.CutoffDate:str = obj["CutoffDate"]
      """  Cut-off Date  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Posted Date  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ActualCostAllocationHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Site  """  
      self.ActualCostingCategoryID:str = obj["ActualCostingCategoryID"]
      """  Actual Costing Category ID  """  
      self.AllocationNum:int = obj["AllocationNum"]
      """  Allocation Number  """  
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
      self.CutoffDate:str = obj["CutoffDate"]
      """  Cut-off Date  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Posted Date  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Generated:bool = obj["Generated"]
      self.IsTheFirstAllocation:bool = obj["IsTheFirstAllocation"]
      self.BitFlag:int = obj["BitFlag"]
      self.ActualCostingCategoryBookID:str = obj["ActualCostingCategoryBookID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckCutoffDate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ActualCostAllocationWorkbenchTableset] = obj["ds"]
      pass

class CheckCutoffDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ActualCostAllocationWorkbenchTableset] = obj["ds"]
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   plant
   actualCostingCategoryID
   allocationNum
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.actualCostingCategoryID:str = obj["actualCostingCategoryID"]
      self.allocationNum:int = obj["allocationNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ActualCostAllocHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Site  """  
      self.ActualCostingCategoryID:str = obj["ActualCostingCategoryID"]
      """  Actual Costing Category ID  """  
      self.AllocationNum:int = obj["AllocationNum"]
      """  Allocation Number  """  
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
      self.CutoffDate:str = obj["CutoffDate"]
      """  Cut-off Date  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Posted Date  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ActualCostAllocWorkbenchListTableset:
   def __init__(self, obj):
      self.ActualCostAllocHeadList:list[Erp_Tablesets_ActualCostAllocHeadListRow] = obj["ActualCostAllocHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ActualCostAllocationHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Site  """  
      self.ActualCostingCategoryID:str = obj["ActualCostingCategoryID"]
      """  Actual Costing Category ID  """  
      self.AllocationNum:int = obj["AllocationNum"]
      """  Allocation Number  """  
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
      self.CutoffDate:str = obj["CutoffDate"]
      """  Cut-off Date  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Posted Date  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Generated:bool = obj["Generated"]
      self.IsTheFirstAllocation:bool = obj["IsTheFirstAllocation"]
      self.BitFlag:int = obj["BitFlag"]
      self.ActualCostingCategoryBookID:str = obj["ActualCostingCategoryBookID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ActualCostAllocationLineListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.ActualCostingCategoryID:str = obj["ActualCostingCategoryID"]
      """  Actual Costing Category  """  
      self.AllocationNum:int = obj["AllocationNum"]
      """  Allocation Number  """  
      self.PartNum:str = obj["PartNum"]
      """  Part  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revison  """  
      self.UOM:str = obj["UOM"]
      """  UOM  """  
      self.ManufacturedQty:int = obj["ManufacturedQty"]
      """  Manufactured Quantity  """  
      self.SoldQty:int = obj["SoldQty"]
      """  Sold Quantity  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  Onhand Quantity  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Cost Method  """  
      self.CurrentMtlCost:int = obj["CurrentMtlCost"]
      """  Current Material Cost  """  
      self.CurrentMtlBurCost:int = obj["CurrentMtlBurCost"]
      """  Current Material Burden Cost  """  
      self.CurrentLaborCost:int = obj["CurrentLaborCost"]
      """  Current Labor Cost  """  
      self.CurrentBurCost:int = obj["CurrentBurCost"]
      """  Current Burden Cost  """  
      self.CurrentSubContCost:int = obj["CurrentSubContCost"]
      """  Current Subcontract Cost  """  
      self.CurrentExtendedCost:int = obj["CurrentExtendedCost"]
      """  Current Extended Cost  """  
      self.AllocationAmtMaterial:int = obj["AllocationAmtMaterial"]
      """  Allocation Amount Material  """  
      self.AllocationAmtLabor:int = obj["AllocationAmtLabor"]
      """  Allocation Amount Labor  """  
      self.AllocationAmtBurden:int = obj["AllocationAmtBurden"]
      """  Allocation Amount Burden  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CostMethodDesc:str = obj["CostMethodDesc"]
      self.TotalCost:int = obj["TotalCost"]
      self.FromDate:str = obj["FromDate"]
      self.ToDate:str = obj["ToDate"]
      self.Posted:bool = obj["Posted"]
      self.PostedDate:str = obj["PostedDate"]
      self.ActualCosBurdenCost:int = obj["ActualCosBurdenCost"]
      self.ActualCosLaborCost:int = obj["ActualCosLaborCost"]
      self.ActualCosMaterialCost:int = obj["ActualCosMaterialCost"]
      self.ActualInventoryBurdenCost:int = obj["ActualInventoryBurdenCost"]
      self.ActualInventoryLaborCost:int = obj["ActualInventoryLaborCost"]
      self.ActualInventoryMaterialCost:int = obj["ActualInventoryMaterialCost"]
      self.ActualWIPBurdenCost:int = obj["ActualWIPBurdenCost"]
      self.ActualWIPLaborCost:int = obj["ActualWIPLaborCost"]
      self.ActualWIPMaterialCost:int = obj["ActualWIPMaterialCost"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ActualCostAllocationLineTableset:
   def __init__(self, obj):
      self.ActualCostAllocationLineList:list[Erp_Tablesets_ActualCostAllocationLineListRow] = obj["ActualCostAllocationLineList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ActualCostAllocationWorkbenchTableset:
   def __init__(self, obj):
      self.ActualCostAllocationHead:list[Erp_Tablesets_ActualCostAllocationHeadRow] = obj["ActualCostAllocationHead"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtActualCostAllocationWorkbenchTableset:
   def __init__(self, obj):
      self.ActualCostAllocationHead:list[Erp_Tablesets_ActualCostAllocationHeadRow] = obj["ActualCostAllocationHead"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetActualCostAllocationLineRows_input:
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

class GetActualCostAllocationLineRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ActualCostAllocationLineTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   plant
   actualCostingCategoryID
   allocationNum
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.actualCostingCategoryID:str = obj["actualCostingCategoryID"]
      self.allocationNum:int = obj["allocationNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ActualCostAllocationWorkbenchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ActualCostAllocationWorkbenchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ActualCostAllocationWorkbenchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ActualCostAllocWorkbenchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewActualCostAllocationHead_input:
   """ Required : 
   ds
   plant
   actualCostingCategoryID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ActualCostAllocationWorkbenchTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      self.actualCostingCategoryID:str = obj["actualCostingCategoryID"]
      pass

class GetNewActualCostAllocationHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ActualCostAllocationWorkbenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseActualCostAllocationHead
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseActualCostAllocationHead:str = obj["whereClauseActualCostAllocationHead"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ActualCostAllocationWorkbenchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_ActualCostAllocationWorkbenchTableset] = obj["ds"]
      pass

class OnChangedFiscalYrPeriod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ActualCostAllocationWorkbenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingActualCostingCategoryID_input:
   """ Required : 
   actualCostingCategoryID
   ds
   """  
   def __init__(self, obj):
      self.actualCostingCategoryID:str = obj["actualCostingCategoryID"]
      self.ds:list[Erp_Tablesets_ActualCostAllocationWorkbenchTableset] = obj["ds"]
      pass

class OnChangingActualCostingCategoryID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ActualCostAllocationWorkbenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtActualCostAllocationWorkbenchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtActualCostAllocationWorkbenchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ActualCostAllocationWorkbenchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ActualCostAllocationWorkbenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

