import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CrossDockSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CrossDocks(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CrossDocks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CrossDocks
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CrossDockRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/CrossDocks",headers=creds) as resp:
           return await resp.json()

async def post_CrossDocks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CrossDocks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CrossDockRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CrossDockRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/CrossDocks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CrossDocks_Company_PartNum_WarehouseCode_BinNum_SupplyJobNum_OrderNum_OrderLine_OrderRelNum_JobNum_AssemblySeq_MtlSeq_TFOrdNum_TFOrdLine(Company, PartNum, WarehouseCode, BinNum, SupplyJobNum, OrderNum, OrderLine, OrderRelNum, JobNum, AssemblySeq, MtlSeq, TFOrdNum, TFOrdLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CrossDock item
   Description: Calls GetByID to retrieve the CrossDock item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CrossDock
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param SupplyJobNum: Desc: SupplyJobNum   Required: True   Allow empty value : True
      :param OrderNum: Desc: OrderNum   Required: True
      :param OrderLine: Desc: OrderLine   Required: True
      :param OrderRelNum: Desc: OrderRelNum   Required: True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param TFOrdNum: Desc: TFOrdNum   Required: True   Allow empty value : True
      :param TFOrdLine: Desc: TFOrdLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CrossDockRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/CrossDocks(" + Company + "," + PartNum + "," + WarehouseCode + "," + BinNum + "," + SupplyJobNum + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + "," + TFOrdNum + "," + TFOrdLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CrossDocks_Company_PartNum_WarehouseCode_BinNum_SupplyJobNum_OrderNum_OrderLine_OrderRelNum_JobNum_AssemblySeq_MtlSeq_TFOrdNum_TFOrdLine(Company, PartNum, WarehouseCode, BinNum, SupplyJobNum, OrderNum, OrderLine, OrderRelNum, JobNum, AssemblySeq, MtlSeq, TFOrdNum, TFOrdLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CrossDock for the service
   Description: Calls UpdateExt to update CrossDock. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CrossDock
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param SupplyJobNum: Desc: SupplyJobNum   Required: True   Allow empty value : True
      :param OrderNum: Desc: OrderNum   Required: True
      :param OrderLine: Desc: OrderLine   Required: True
      :param OrderRelNum: Desc: OrderRelNum   Required: True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param TFOrdNum: Desc: TFOrdNum   Required: True   Allow empty value : True
      :param TFOrdLine: Desc: TFOrdLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CrossDockRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/CrossDocks(" + Company + "," + PartNum + "," + WarehouseCode + "," + BinNum + "," + SupplyJobNum + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + "," + TFOrdNum + "," + TFOrdLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CrossDocks_Company_PartNum_WarehouseCode_BinNum_SupplyJobNum_OrderNum_OrderLine_OrderRelNum_JobNum_AssemblySeq_MtlSeq_TFOrdNum_TFOrdLine(Company, PartNum, WarehouseCode, BinNum, SupplyJobNum, OrderNum, OrderLine, OrderRelNum, JobNum, AssemblySeq, MtlSeq, TFOrdNum, TFOrdLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CrossDock item
   Description: Call UpdateExt to delete CrossDock item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CrossDock
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param SupplyJobNum: Desc: SupplyJobNum   Required: True   Allow empty value : True
      :param OrderNum: Desc: OrderNum   Required: True
      :param OrderLine: Desc: OrderLine   Required: True
      :param OrderRelNum: Desc: OrderRelNum   Required: True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param TFOrdNum: Desc: TFOrdNum   Required: True   Allow empty value : True
      :param TFOrdLine: Desc: TFOrdLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/CrossDocks(" + Company + "," + PartNum + "," + WarehouseCode + "," + BinNum + "," + SupplyJobNum + "," + OrderNum + "," + OrderLine + "," + OrderRelNum + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + "," + TFOrdNum + "," + TFOrdLine + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CrossDockListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCrossDock, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCrossDock=" + whereClauseCrossDock
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(partNum, warehouseCode, binNum, supplyJobNum, orderNum, orderLine, orderRelNum, jobNum, assemblySeq, mtlSeq, tfOrdNum, tfOrdLine, epicorHeaders = None):
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
   Required: True
   Required: True   Allow empty value : True
   Required: True
   Required: True
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
   params += "partNum=" + partNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "warehouseCode=" + warehouseCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "binNum=" + binNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "supplyJobNum=" + supplyJobNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "orderNum=" + orderNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "orderLine=" + orderLine
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "orderRelNum=" + orderRelNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "jobNum=" + jobNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "assemblySeq=" + assemblySeq
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "mtlSeq=" + mtlSeq
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "tfOrdNum=" + tfOrdNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "tfOrdLine=" + tfOrdLine

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: Get Code Description List
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCrossDock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCrossDock
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCrossDock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCrossDock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCrossDock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CrossDockSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CrossDockListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CrossDockListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CrossDockRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CrossDockRow] = obj["value"]
      pass

class Erp_Tablesets_CrossDockListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number that the cross dock is for.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse that is quantity cross docked is being supplied from.  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin number  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  Job that is supplying the cross docked quantity  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number of the order release that is cross docked.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order line number of the order release that is cross docked.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Order release number of the order release that is cross docked.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number of the JobMtl/JobAsmbl that is cross docked.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly number of the JobMtl/JobAsmbl that is cross docked.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Material sequence number of the JobMtl that is cross docked.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Transfer Order that is cross docked.  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  Transfer Order Line that is cross docked.  """  
      self.CrossDockedQty:int = obj["CrossDockedQty"]
      """  Quantity that is "Cross Docked" for the Allocation (sales order, job or transfer order requirement).  """  
      self.CrossDockedUM:str = obj["CrossDockedUM"]
      """  Unit of measure (how it is cross docked).  """  
      self.ToPlant:str = obj["ToPlant"]
      """  The To Site for a Transfer Order Cross Dock.  """  
      self.FromPlant:str = obj["FromPlant"]
      """  The From Site for a Transfer Order Cross Dock.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Creation date  """  
      self.BuyToOrder:bool = obj["BuyToOrder"]
      """  Is this Cross Dock transaction a result of a Buy To Order transaction?  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.Priority:int = obj["Priority"]
      """  Cross Dock Priority.  When inventory increases, Cross Dock transactions are consumed.  This field is used to determine the priority (order) in which they are consumed.  One is the highest priority.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DistributionType:str = obj["DistributionType"]
      """  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  """  
      self.AssignEmpID:str = obj["AssignEmpID"]
      """  Employee ID that should be assigned to process record from the queue.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.OnHold:bool = obj["OnHold"]
      """  When Material Queue items are added, they should be automatically On Hold.  """  
      self.ReleaseToPicking:bool = obj["ReleaseToPicking"]
      """  The allocated demand is ready to be Released to Picking.  """  
      self.CrossDockedAttributeSetID:int = obj["CrossDockedAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.CrossDockedRevisionNum:str = obj["CrossDockedRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.CommitedQty:int = obj["CommitedQty"]
      self.DemandType:str = obj["DemandType"]
      """  valid values: Order, Job or Transfer.  """  
      self.DemandTypeDesc:str = obj["DemandTypeDesc"]
      """  Description of Demand Type code.  """  
      self.DispSysTime:str = obj["DispSysTime"]
      """  HH:MM:SS Format of System Time.  """  
      self.TFOrdNumTFOrdLine:int = obj["TFOrdNumTFOrdLine"]
      self.TranType:str = obj["TranType"]
      self.SalesOrderLineRelease:str = obj["SalesOrderLineRelease"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CrossDockRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number that the cross dock is for.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse that is quantity cross docked is being supplied from.  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin number  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  Job that is supplying the cross docked quantity  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number of the order release that is cross docked.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order line number of the order release that is cross docked.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Order release number of the order release that is cross docked.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number of the JobMtl/JobAsmbl that is cross docked.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly number of the JobMtl/JobAsmbl that is cross docked.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Material sequence number of the JobMtl that is cross docked.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Transfer Order that is cross docked.  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  Transfer Order Line that is cross docked.  """  
      self.CrossDockedQty:int = obj["CrossDockedQty"]
      """  Quantity that is "Cross Docked" for the Allocation (sales order, job or transfer order requirement).  """  
      self.CrossDockedUM:str = obj["CrossDockedUM"]
      """  Unit of measure (how it is cross docked).  """  
      self.ToPlant:str = obj["ToPlant"]
      """  The To Site for a Transfer Order Cross Dock.  """  
      self.FromPlant:str = obj["FromPlant"]
      """  The From Site for a Transfer Order Cross Dock.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Creation date  """  
      self.CreateTime:int = obj["CreateTime"]
      """  Creation Time  """  
      self.BuyToOrder:bool = obj["BuyToOrder"]
      """  Is this Cross Dock transaction a result of a Buy To Order transaction?  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.Priority:int = obj["Priority"]
      """  Cross Dock Priority.  When inventory increases, Cross Dock transactions are consumed.  This field is used to determine the priority (order) in which they are consumed.  One is the highest priority.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DistributionType:str = obj["DistributionType"]
      """  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  """  
      self.AssignEmpID:str = obj["AssignEmpID"]
      """  Employee ID that should be assigned to process record from the queue.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.OnHold:bool = obj["OnHold"]
      """  When Material Queue items are added, they should be automatically On Hold.  """  
      self.ReleaseToPicking:bool = obj["ReleaseToPicking"]
      """  The allocated demand is ready to be Released to Picking.  """  
      self.CrossDockedAttributeSetID:int = obj["CrossDockedAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.CrossDockedRevisionNum:str = obj["CrossDockedRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.CommittedQty:int = obj["CommittedQty"]
      self.DemandType:str = obj["DemandType"]
      """  valid values: Order, Job or Transfer  """  
      self.DemandTypeDesc:str = obj["DemandTypeDesc"]
      """  Description of Demand Type Code.  """  
      self.DispSysTime:str = obj["DispSysTime"]
      """  HH:MM:SS format of system time.  """  
      self.TFOrdNumTFOrdLine:int = obj["TFOrdNumTFOrdLine"]
      self.TranType:str = obj["TranType"]
      """  Transaction Type  """  
      self.SalesOrderLineRelease:str = obj["SalesOrderLineRelease"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartAttrClassID:str = obj["PartAttrClassID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   partNum
   warehouseCode
   binNum
   supplyJobNum
   orderNum
   orderLine
   orderRelNum
   jobNum
   assemblySeq
   mtlSeq
   tfOrdNum
   tfOrdLine
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.binNum:str = obj["binNum"]
      self.supplyJobNum:str = obj["supplyJobNum"]
      self.orderNum:int = obj["orderNum"]
      self.orderLine:int = obj["orderLine"]
      self.orderRelNum:int = obj["orderRelNum"]
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.mtlSeq:int = obj["mtlSeq"]
      self.tfOrdNum:str = obj["tfOrdNum"]
      self.tfOrdLine:int = obj["tfOrdLine"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CrossDockListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number that the cross dock is for.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse that is quantity cross docked is being supplied from.  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin number  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  Job that is supplying the cross docked quantity  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number of the order release that is cross docked.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order line number of the order release that is cross docked.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Order release number of the order release that is cross docked.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number of the JobMtl/JobAsmbl that is cross docked.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly number of the JobMtl/JobAsmbl that is cross docked.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Material sequence number of the JobMtl that is cross docked.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Transfer Order that is cross docked.  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  Transfer Order Line that is cross docked.  """  
      self.CrossDockedQty:int = obj["CrossDockedQty"]
      """  Quantity that is "Cross Docked" for the Allocation (sales order, job or transfer order requirement).  """  
      self.CrossDockedUM:str = obj["CrossDockedUM"]
      """  Unit of measure (how it is cross docked).  """  
      self.ToPlant:str = obj["ToPlant"]
      """  The To Site for a Transfer Order Cross Dock.  """  
      self.FromPlant:str = obj["FromPlant"]
      """  The From Site for a Transfer Order Cross Dock.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Creation date  """  
      self.BuyToOrder:bool = obj["BuyToOrder"]
      """  Is this Cross Dock transaction a result of a Buy To Order transaction?  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.Priority:int = obj["Priority"]
      """  Cross Dock Priority.  When inventory increases, Cross Dock transactions are consumed.  This field is used to determine the priority (order) in which they are consumed.  One is the highest priority.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DistributionType:str = obj["DistributionType"]
      """  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  """  
      self.AssignEmpID:str = obj["AssignEmpID"]
      """  Employee ID that should be assigned to process record from the queue.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.OnHold:bool = obj["OnHold"]
      """  When Material Queue items are added, they should be automatically On Hold.  """  
      self.ReleaseToPicking:bool = obj["ReleaseToPicking"]
      """  The allocated demand is ready to be Released to Picking.  """  
      self.CrossDockedAttributeSetID:int = obj["CrossDockedAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.CrossDockedRevisionNum:str = obj["CrossDockedRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.CommitedQty:int = obj["CommitedQty"]
      self.DemandType:str = obj["DemandType"]
      """  valid values: Order, Job or Transfer.  """  
      self.DemandTypeDesc:str = obj["DemandTypeDesc"]
      """  Description of Demand Type code.  """  
      self.DispSysTime:str = obj["DispSysTime"]
      """  HH:MM:SS Format of System Time.  """  
      self.TFOrdNumTFOrdLine:int = obj["TFOrdNumTFOrdLine"]
      self.TranType:str = obj["TranType"]
      self.SalesOrderLineRelease:str = obj["SalesOrderLineRelease"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CrossDockListTableset:
   def __init__(self, obj):
      self.CrossDockList:list[Erp_Tablesets_CrossDockListRow] = obj["CrossDockList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CrossDockRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number that the cross dock is for.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse that is quantity cross docked is being supplied from.  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin number  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  Job that is supplying the cross docked quantity  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number of the order release that is cross docked.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order line number of the order release that is cross docked.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Order release number of the order release that is cross docked.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number of the JobMtl/JobAsmbl that is cross docked.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly number of the JobMtl/JobAsmbl that is cross docked.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Material sequence number of the JobMtl that is cross docked.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Transfer Order that is cross docked.  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  Transfer Order Line that is cross docked.  """  
      self.CrossDockedQty:int = obj["CrossDockedQty"]
      """  Quantity that is "Cross Docked" for the Allocation (sales order, job or transfer order requirement).  """  
      self.CrossDockedUM:str = obj["CrossDockedUM"]
      """  Unit of measure (how it is cross docked).  """  
      self.ToPlant:str = obj["ToPlant"]
      """  The To Site for a Transfer Order Cross Dock.  """  
      self.FromPlant:str = obj["FromPlant"]
      """  The From Site for a Transfer Order Cross Dock.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Creation date  """  
      self.CreateTime:int = obj["CreateTime"]
      """  Creation Time  """  
      self.BuyToOrder:bool = obj["BuyToOrder"]
      """  Is this Cross Dock transaction a result of a Buy To Order transaction?  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.Priority:int = obj["Priority"]
      """  Cross Dock Priority.  When inventory increases, Cross Dock transactions are consumed.  This field is used to determine the priority (order) in which they are consumed.  One is the highest priority.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DistributionType:str = obj["DistributionType"]
      """  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  """  
      self.AssignEmpID:str = obj["AssignEmpID"]
      """  Employee ID that should be assigned to process record from the queue.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group Identifier.  """  
      self.OnHold:bool = obj["OnHold"]
      """  When Material Queue items are added, they should be automatically On Hold.  """  
      self.ReleaseToPicking:bool = obj["ReleaseToPicking"]
      """  The allocated demand is ready to be Released to Picking.  """  
      self.CrossDockedAttributeSetID:int = obj["CrossDockedAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.CrossDockedRevisionNum:str = obj["CrossDockedRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.CommittedQty:int = obj["CommittedQty"]
      self.DemandType:str = obj["DemandType"]
      """  valid values: Order, Job or Transfer  """  
      self.DemandTypeDesc:str = obj["DemandTypeDesc"]
      """  Description of Demand Type Code.  """  
      self.DispSysTime:str = obj["DispSysTime"]
      """  HH:MM:SS format of system time.  """  
      self.TFOrdNumTFOrdLine:int = obj["TFOrdNumTFOrdLine"]
      self.TranType:str = obj["TranType"]
      """  Transaction Type  """  
      self.SalesOrderLineRelease:str = obj["SalesOrderLineRelease"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartAttrClassID:str = obj["PartAttrClassID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CrossDockTableset:
   def __init__(self, obj):
      self.CrossDock:list[Erp_Tablesets_CrossDockRow] = obj["CrossDock"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCrossDockTableset:
   def __init__(self, obj):
      self.CrossDock:list[Erp_Tablesets_CrossDockRow] = obj["CrossDock"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   partNum
   warehouseCode
   binNum
   supplyJobNum
   orderNum
   orderLine
   orderRelNum
   jobNum
   assemblySeq
   mtlSeq
   tfOrdNum
   tfOrdLine
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.binNum:str = obj["binNum"]
      self.supplyJobNum:str = obj["supplyJobNum"]
      self.orderNum:int = obj["orderNum"]
      self.orderLine:int = obj["orderLine"]
      self.orderRelNum:int = obj["orderRelNum"]
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.mtlSeq:int = obj["mtlSeq"]
      self.tfOrdNum:str = obj["tfOrdNum"]
      self.tfOrdLine:int = obj["tfOrdLine"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CrossDockTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CrossDockTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CrossDockTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name  """  
      self.fieldName:str = obj["fieldName"]
      """  Field Name  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Description List  """  
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
      self.returnObj:list[Erp_Tablesets_CrossDockListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCrossDock_input:
   """ Required : 
   ds
   partNum
   warehouseCode
   binNum
   supplyJobNum
   orderNum
   orderLine
   orderRelNum
   jobNum
   assemblySeq
   mtlSeq
   tfOrdNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CrossDockTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.binNum:str = obj["binNum"]
      self.supplyJobNum:str = obj["supplyJobNum"]
      self.orderNum:int = obj["orderNum"]
      self.orderLine:int = obj["orderLine"]
      self.orderRelNum:int = obj["orderRelNum"]
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.mtlSeq:int = obj["mtlSeq"]
      self.tfOrdNum:str = obj["tfOrdNum"]
      pass

class GetNewCrossDock_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CrossDockTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCrossDock
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCrossDock:str = obj["whereClauseCrossDock"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CrossDockTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtCrossDockTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCrossDockTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CrossDockTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CrossDockTableset] = obj["ds"]
      pass

      """  output parameters  """  

