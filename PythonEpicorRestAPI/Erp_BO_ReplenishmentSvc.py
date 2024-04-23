import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ReplenishmentSvc
# Description: Replenishment BO - Used by Replenishment Workbench
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Replenishments(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Replenishments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Replenishments
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MtlQueueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/Replenishments",headers=creds) as resp:
           return await resp.json()

async def post_Replenishments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Replenishments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MtlQueueRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MtlQueueRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/Replenishments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Replenishments_Company_MtlQueueSeq(Company, MtlQueueSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Replenishment item
   Description: Calls GetByID to retrieve the Replenishment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Replenishment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MtlQueueSeq: Desc: MtlQueueSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MtlQueueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/Replenishments(" + Company + "," + MtlQueueSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Replenishments_Company_MtlQueueSeq(Company, MtlQueueSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Replenishment for the service
   Description: Calls UpdateExt to update Replenishment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Replenishment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MtlQueueSeq: Desc: MtlQueueSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MtlQueueRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/Replenishments(" + Company + "," + MtlQueueSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Replenishments_Company_MtlQueueSeq(Company, MtlQueueSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Replenishment item
   Description: Call UpdateExt to delete Replenishment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Replenishment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MtlQueueSeq: Desc: MtlQueueSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/Replenishments(" + Company + "," + MtlQueueSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ReplenishSuggs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ReplenishSuggs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ReplenishSuggs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReplenishSuggRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/ReplenishSuggs",headers=creds) as resp:
           return await resp.json()

async def post_ReplenishSuggs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ReplenishSuggs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ReplenishSuggRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ReplenishSuggRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/ReplenishSuggs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ReplenishSuggs_PartNum_WarehouseCode_BinNum_TranType(PartNum, WarehouseCode, BinNum, TranType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ReplenishSugg item
   Description: Calls GetByID to retrieve the ReplenishSugg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReplenishSugg
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param TranType: Desc: TranType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ReplenishSuggRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/ReplenishSuggs(" + PartNum + "," + WarehouseCode + "," + BinNum + "," + TranType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ReplenishSuggs_PartNum_WarehouseCode_BinNum_TranType(PartNum, WarehouseCode, BinNum, TranType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ReplenishSugg for the service
   Description: Calls UpdateExt to update ReplenishSugg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ReplenishSugg
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param TranType: Desc: TranType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ReplenishSuggRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/ReplenishSuggs(" + PartNum + "," + WarehouseCode + "," + BinNum + "," + TranType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ReplenishSuggs_PartNum_WarehouseCode_BinNum_TranType(PartNum, WarehouseCode, BinNum, TranType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ReplenishSugg item
   Description: Call UpdateExt to delete ReplenishSugg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ReplenishSugg
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param TranType: Desc: TranType   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/ReplenishSuggs(" + PartNum + "," + WarehouseCode + "," + BinNum + "," + TranType + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MtlQueueListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseMtlQueue, whereClauseReplenishSugg, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseMtlQueue=" + whereClauseMtlQueue
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseReplenishSugg=" + whereClauseReplenishSugg
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(mtlQueueSeq, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "mtlQueueSeq=" + mtlQueueSeq

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AssignMoves(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignMoves
   Description: Selected records are assigned to specified employee ID or group. If both are blank fields are blanked.
   OperationID: AssignMoves
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignMoves_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignMoves_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignPriority(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignPriority
   Description: Sets priority on selected records
   OperationID: AssignPriority
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignPriority_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignPriority_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalculateAvailableQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalculateAvailableQty
   Description: Calculate available qty
   OperationID: CalculateAvailableQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateAvailableQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateAvailableQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteMoves(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteMoves
   Description: Delete selected moves
   OperationID: DeleteMoves
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteMoves_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteMoves_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateManaged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateManaged
   Description: Generates manual suggestion table
   OperationID: GenerateManaged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateManaged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateManaged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateManual(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateManual
   Description: Generates manual suggestion table
   OperationID: GenerateManual
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateManual_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateManual_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultWhse(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultWhse
   Description: Gets the default warehouse
   OperationID: GetDefaultWhse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultWhse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetMoveRequests(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMoveRequests
   Description: Retrieve existing move requests
   OperationID: GetMoveRequests
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMoveRequests_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMoveRequests_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMoveQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMoveQty
   Description: Column Changed event of MoveQty field
   OperationID: OnChangeMoveQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMoveQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMoveQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingMoveQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingMoveQty
   Description: Column Changing event of MoveQty field
   OperationID: OnChangingMoveQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingMoveQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingMoveQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessManagedReplenishment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessManagedReplenishment
   Description: Generates moves for managed replenishment
   OperationID: ProcessManagedReplenishment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessManagedReplenishment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessManagedReplenishment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessManualReplenishment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessManualReplenishment
   Description: Generates moves for manual replenishment
   OperationID: ProcessManualReplenishment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessManualReplenishment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessManualReplenishment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ToggleHoldStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ToggleHoldStatus
   Description: Sets selected records to hold or release
   OperationID: ToggleHoldStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ToggleHoldStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ToggleHoldStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMtlQueue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMtlQueue
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMtlQueue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMtlQueue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMtlQueue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReplenishmentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MtlQueueListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MtlQueueListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MtlQueueRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MtlQueueRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReplenishSuggRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ReplenishSuggRow] = obj["value"]
      pass

class Erp_Tablesets_MtlQueueListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time(seconds since midnight) when transaction was created.  """  
      self.MtlQueueSeq:int = obj["MtlQueueSeq"]
      """  Number assigned by the system to uniquely identify the record.  Created by using the database sequence "MtlQueueSeq".  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of item in the container.  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity  """  
      self.TranType:str = obj["TranType"]
      """   Internal flag to indicate the type of transaction that this request is for.  This will control which functions are invoked for processing.
The same codes as in PartTran are used.  However, there are some additional codes also. 
They are; GET-WIP,  RTN-WIP, RTN-MTL, PUT-MTL, PUT-WIP, PICK-SO, PICK-JOB, PICK-TFO, BIN-REPLENISH, BIN-CONSOLIDATE, PICK-SO-XDOCK, PICK-JOB-XDOCK, PICK-TFO-XDOCK  """  
      self.ReferencePrefix:str = obj["ReferencePrefix"]
      """   Used as a translatable prefix for the Reference field.
For example for a purchase receipt of stock it has "PS", (Packing Slip). For display purposes this is field is translated, then concatenated with the value in the Refernce field. 
Other values are "Job",  """  
      self.Reference:str = obj["Reference"]
      """  Contains a reference about the request. May contain Job/Asm/Seq, WrkCtr,  Packing Slip #,  Sales Order, etc...depending on the TranType.  """  
      self.RequestedByEmpID:str = obj["RequestedByEmpID"]
      """  Employee ID that made the request.  """  
      self.SelectedByEmpID:str = obj["SelectedByEmpID"]
      """  Employee ID that has selected this record from the queue for processing.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that the request is related to.  This allows sorting by Job, which provides the user a method of working on all the requests for a specific job.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "O" = Job Operation (JobOper).  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of the related specific material or operation record.  For WIP parts it's the operation sequence that created the part. For raw materials it's the related JobMtl.MtlSeq.  """  
      self.FromWhse:str = obj["FromWhse"]
      """  Warehouse Code where item is to be found. For example a Get Raw Material request of a stocked part  would be the warehouse  the requirement was allocated against (JobMtl.WareHouseCode).  A "Move of a WIP part" will contain the Warehouse defined by the WrkCenter.PutWhse...  """  
      self.FromBinNum:str = obj["FromBinNum"]
      """  Warehouse bin where item is to be found. For example a Get Raw Material request of a stocked part  would be the Primary Bin of the part/warehouse, if no primary bin, then the first Bin in the warehouse which contains this part, else blank.  A "Move of a WIP part" will contain the bin defined by the WrkCenter.PutBin...  """  
      self.ToWhse:str = obj["ToWhse"]
      """  Warehouse where item should be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputWhse).  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  Warehouse bin where item is to be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputBin).  """  
      self.NextAssemblySeq:int = obj["NextAssemblySeq"]
      """  Assembly sequence of the operation that completed quantity of the job operation  will be moved to.  """  
      self.NextJobSeq:int = obj["NextJobSeq"]
      """  Sequence of the operation that completed quantity of the job operation will be moved to.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date the this request is needed by.  Defaults, to current system date.  """  
      self.NeedByTime:int = obj["NeedByTime"]
      """  Time (seconds since midnight) that request is need by.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor number of the related purchase receipt (RcvDtl).  Company,VendorNum, PurPoint, PackSlip,Packline are used to provide the link to the related RcvDtl record.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor purchase point id of the related purchase receipt (RcvDtl).  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip # of the related RcvDtl.  """  
      self.PackLine:int = obj["PackLine"]
      """  Vendors Packing Slip line  # of the related RcvDtl.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   Order number job is making parts for. (See JobProd.OrderNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

OrderNum pertains only to "make to order" requirements.  
Provides relationship to the JobProd for "make to order" requirements.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related Sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Related sales order release number.  """  
      self.TargetJobNum:str = obj["TargetJobNum"]
      """   Job that this job is making parts for. (See JobProd.TargetJobNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

TargetJobNum pertains only to "make to job" requirements.  
Provides relationship to the JobProd for "make to Job" requirements.  """  
      self.TargetAssemblySeq:int = obj["TargetAssemblySeq"]
      """  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.TargetMtlSeq:int = obj["TargetMtlSeq"]
      """  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  A description of the Part.  """  
      self.IUM:str = obj["IUM"]
      """  Internal unit of measure.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.Visible:bool = obj["Visible"]
      """  Indicates if this MtlQueue is visible to the user on the Material Queue browse.  Set based on the users response to make a "move  request" when reporting quantities.  Set to true visible), if a move request is made.  This was implemented to keep track of labor quantity reported without making a move request.  The move request will then reflect the total quantity to move instead of what was reported on the labor transaction that requested the move.  Regardless of making a "Move Request" labor quantity reporting always creates/updates a MtlQueue record.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Material Authorization number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMAReceipt number of the related RMARcpt record.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  RMADisp number of the related RMADisp record.  """  
      self.NCTranID:int = obj["NCTranID"]
      """  The related NonConf.TranID number. Used to link the MtlQueue table to the NonConf table.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the part.  """  
      self.Lock:bool = obj["Lock"]
      """  Indicates this record has been locked by a Advanced Shipping user and is not available for processing by any other user.  """  
      self.QueueID:str = obj["QueueID"]
      """  Used by Advanced Shipping to designate which queue this record is in.  Advanced Shipping queues can prioritize and process records.  """  
      self.QueuePickSeq:int = obj["QueuePickSeq"]
      """  Sequence of this record within an Advanced Shipping Queue.  """  
      self.ReleaseForPickingSeq:int = obj["ReleaseForPickingSeq"]
      """  This is an internal sequence number for grouping MtlQueue records.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group that was assigned to this transaction.  """  
      self.TranStatus:str = obj["TranStatus"]
      """   The status of the transaction of the material.  Valid values:
MGMT-LOCK - Manager locked, RELEASED - Released, HOLD - On Hold, USER-LOCK - Locked for a user, ORDER-HOLD - On Hold for Order Based Picking, QUALITY-HOLD - On Hold for Quality Control, and PICK-PACK - Three step allocation Pick-Pack Method  """  
      self.WaveNum:int = obj["WaveNum"]
      """  The Wave that was assigned during the allocation process.  """  
      self.Priority:int = obj["Priority"]
      """  Transaction Priority.  Valid values are 1,2,3,4,5,6,7,8,9.  One is the highest priority.  """  
      self.TranSource:str = obj["TranSource"]
      """  Transaction Source  """  
      self.LastMgrChangeEmpID:str = obj["LastMgrChangeEmpID"]
      """  When the TranStatus, AssignedToEmpID or Priority are modified, this value is updated with the ID of the Manager making the change.  """  
      self.AssignedToEmpID:str = obj["AssignedToEmpID"]
      """  Employee ID that was selected by the Warehouse Manager to process record from the queue.  """  
      self.TargetTFOrdNum:str = obj["TargetTFOrdNum"]
      """  Transfer Order for which Demand is being satisfied.  """  
      self.TargetTFOrdLine:int = obj["TargetTFOrdLine"]
      """  Transfer Order Line for which Demand is being satisfied.  """  
      self.PackStation:str = obj["PackStation"]
      """  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  """  
      self.DistributionType:str = obj["DistributionType"]
      """  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OkToProcess:bool = obj["OkToProcess"]
      """  Holds the result of checking sub-menu security.  NO indicates the current user does not have permission to carry out the indicated TranType.  """  
      self.RequestedByEmpName:str = obj["RequestedByEmpName"]
      self.SelectedByEmpName:str = obj["SelectedByEmpName"]
      self.NeedByTimeDisp:str = obj["NeedByTimeDisp"]
      self.SameWhseGroupEmp:bool = obj["SameWhseGroupEmp"]
      """  Is this material queue row part of the employees warehouse group  """  
      self.SortByPriority:int = obj["SortByPriority"]
      """  Sort priority from highest to lowest (1,2,3,4,5,6,7,8,9,0)  """  
      self.WaveRelated:bool = obj["WaveRelated"]
      """  Value is true if this mtlqueue record is related to a wave. False if it is not.  """  
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.POLinePartNum:str = obj["POLinePartNum"]
      """  OUR internal Part number for this item.  """  
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      """  Supplier Part Number  """  
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.PORelNumRefCodeDesc:str = obj["PORelNumRefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      """  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.WarehouseGroupCodeWhseGroupDesc:str = obj["WarehouseGroupCodeWhseGroupDesc"]
      """  Warehouse Group Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MtlQueueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time(seconds since midnight) when transaction was created.  """  
      self.MtlQueueSeq:int = obj["MtlQueueSeq"]
      """  Number assigned by the system to uniquely identify the record.  Created by using the database sequence "MtlQueueSeq".  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of item in the container.  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity  """  
      self.TranType:str = obj["TranType"]
      """   Internal flag to indicate the type of transaction that this request is for.  This will control which functions are invoked for processing.
The same codes as in PartTran are used.  However, there are some additional codes also. 
They are; GET-WIP,  RTN-WIP, RTN-MTL, PUT-MTL, PUT-WIP, PICK-SO, PICK-JOB, PICK-TFO, BIN-REPLENISH, BIN-CONSOLIDATE, PICK-SO-XDOCK, PICK-JOB-XDOCK, PICK-TFO-XDOCK  """  
      self.ReferencePrefix:str = obj["ReferencePrefix"]
      """   Used as a translatable prefix for the Reference field.
For example for a purchase receipt of stock it has "PS", (Packing Slip). For display purposes this is field is translated, then concatenated with the value in the Refernce field. 
Other values are "Job",  """  
      self.Reference:str = obj["Reference"]
      """  Contains a reference about the request. May contain Job/Asm/Seq, WrkCtr,  Packing Slip #,  Sales Order, etc...depending on the TranType.  """  
      self.RequestedByEmpID:str = obj["RequestedByEmpID"]
      """  Employee ID that made the request.  """  
      self.SelectedByEmpID:str = obj["SelectedByEmpID"]
      """  Employee ID that has selected this record from the queue for processing.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that the request is related to.  This allows sorting by Job, which provides the user a method of working on all the requests for a specific job.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "O" = Job Operation (JobOper).  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of the related specific material or operation record.  For WIP parts it's the operation sequence that created the part. For raw materials it's the related JobMtl.MtlSeq.  """  
      self.FromWhse:str = obj["FromWhse"]
      """  Warehouse Code where item is to be found. For example a Get Raw Material request of a stocked part  would be the warehouse  the requirement was allocated against (JobMtl.WareHouseCode).  A "Move of a WIP part" will contain the Warehouse defined by the WrkCenter.PutWhse...  """  
      self.FromBinNum:str = obj["FromBinNum"]
      """  Warehouse bin where item is to be found. For example a Get Raw Material request of a stocked part  would be the Primary Bin of the part/warehouse, if no primary bin, then the first Bin in the warehouse which contains this part, else blank.  A "Move of a WIP part" will contain the bin defined by the WrkCenter.PutBin...  """  
      self.ToWhse:str = obj["ToWhse"]
      """  Warehouse where item should be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputWhse).  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  Warehouse bin where item is to be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputBin).  """  
      self.NextAssemblySeq:int = obj["NextAssemblySeq"]
      """  Assembly sequence of the operation that completed quantity of the job operation  will be moved to.  """  
      self.NextJobSeq:int = obj["NextJobSeq"]
      """  Sequence of the operation that completed quantity of the job operation will be moved to.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date the this request is needed by.  Defaults, to current system date.  """  
      self.NeedByTime:int = obj["NeedByTime"]
      """  Time (seconds since midnight) that request is need by.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor number of the related purchase receipt (RcvDtl).  Company,VendorNum, PurPoint, PackSlip,Packline are used to provide the link to the related RcvDtl record.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor purchase point id of the related purchase receipt (RcvDtl).  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip # of the related RcvDtl.  """  
      self.PackLine:int = obj["PackLine"]
      """  Vendors Packing Slip line  # of the related RcvDtl.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   Order number job is making parts for. (See JobProd.OrderNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

OrderNum pertains only to "make to order" requirements.  
Provides relationship to the JobProd for "make to order" requirements.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related Sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Related sales order release number.  """  
      self.TargetJobNum:str = obj["TargetJobNum"]
      """   Job that this job is making parts for. (See JobProd.TargetJobNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

TargetJobNum pertains only to "make to job" requirements.  
Provides relationship to the JobProd for "make to Job" requirements.  """  
      self.TargetAssemblySeq:int = obj["TargetAssemblySeq"]
      """  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.TargetMtlSeq:int = obj["TargetMtlSeq"]
      """  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  A description of the Part.  """  
      self.IUM:str = obj["IUM"]
      """  Internal unit of measure.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.Visible:bool = obj["Visible"]
      """  Indicates if this MtlQueue is visible to the user on the Material Queue browse.  Set based on the users response to make a "move  request" when reporting quantities.  Set to true visible), if a move request is made.  This was implemented to keep track of labor quantity reported without making a move request.  The move request will then reflect the total quantity to move instead of what was reported on the labor transaction that requested the move.  Regardless of making a "Move Request" labor quantity reporting always creates/updates a MtlQueue record.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Material Authorization number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMAReceipt number of the related RMARcpt record.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  RMADisp number of the related RMADisp record.  """  
      self.NCTranID:int = obj["NCTranID"]
      """  The related NonConf.TranID number. Used to link the MtlQueue table to the NonConf table.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the part.  """  
      self.Lock:bool = obj["Lock"]
      """  Indicates this record has been locked by a Advanced Shipping user and is not available for processing by any other user.  """  
      self.QueueID:str = obj["QueueID"]
      """  Used by Advanced Shipping to designate which queue this record is in.  Advanced Shipping queues can prioritize and process records.  """  
      self.QueuePickSeq:int = obj["QueuePickSeq"]
      """  Sequence of this record within an Advanced Shipping Queue.  """  
      self.ReleaseForPickingSeq:int = obj["ReleaseForPickingSeq"]
      """  This is an internal sequence number for grouping MtlQueue records.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group that was assigned to this transaction.  """  
      self.TranStatus:str = obj["TranStatus"]
      """   The status of the transaction of the material.  Valid values:
MGMT-LOCK - Manager locked, RELEASED - Released, HOLD - On Hold, USER-LOCK - Locked for a user, ORDER-HOLD - On Hold for Order Based Picking, QUALITY-HOLD - On Hold for Quality Control, and PICK-PACK - Three step allocation Pick-Pack Method  """  
      self.WaveNum:int = obj["WaveNum"]
      """  The Wave that was assigned during the allocation process.  """  
      self.Priority:int = obj["Priority"]
      """  Transaction Priority.  Valid values are 1,2,3,4,5,6,7,8,9.  One is the highest priority.  """  
      self.TranSource:str = obj["TranSource"]
      """  Transaction Source  """  
      self.LastMgrChangeEmpID:str = obj["LastMgrChangeEmpID"]
      """  When the TranStatus, AssignedToEmpID or Priority are modified, this value is updated with the ID of the Manager making the change.  """  
      self.AssignedToEmpID:str = obj["AssignedToEmpID"]
      """  Employee ID that was selected by the Warehouse Manager to process record from the queue.  """  
      self.TargetTFOrdNum:str = obj["TargetTFOrdNum"]
      """  Transfer Order for which Demand is being satisfied.  """  
      self.TargetTFOrdLine:int = obj["TargetTFOrdLine"]
      """  Transfer Order Line for which Demand is being satisfied.  """  
      self.PackStation:str = obj["PackStation"]
      """  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  """  
      self.DistributionType:str = obj["DistributionType"]
      """  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.LastUsedPCID:str = obj["LastUsedPCID"]
      """  Last Used PCID on the selected line.  """  
      self.FromPCID:str = obj["FromPCID"]
      """  The PCID from which the material movement will occur.  """  
      self.ToPCID:str = obj["ToPCID"]
      """  The PCID to which the material movement will occur.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeValueSeq:int = obj["AttributeValueSeq"]
      """  AttributeValueSeq  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.CustID:str = obj["CustID"]
      self.CustTerritoryID:str = obj["CustTerritoryID"]
      self.DisableTO:bool = obj["DisableTO"]
      """  Indicates whether Transfer Order Selector Flag should be disabled.  """  
      self.FromInv:bool = obj["FromInv"]
      """  From Inventory Selector Flag  """  
      self.FromJob:bool = obj["FromJob"]
      """  From Manufacturing Selector Flag  """  
      self.FromPO:bool = obj["FromPO"]
      """  From Purchasing Selector Flag  """  
      self.FromTO:bool = obj["FromTO"]
      """  From Transfer Order Selector Flag  """  
      self.FromWhseDesc:str = obj["FromWhseDesc"]
      self.FSAServiceOrderNumber:int = obj["FSAServiceOrderNumber"]
      """  Service Order Number from FSA. Only available in FSA Request Workbench.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource Num from FSA. Only available in FSA Request Workbench.  """  
      self.HoldStatus:bool = obj["HoldStatus"]
      self.LeadTime:int = obj["LeadTime"]
      self.MaxMfgLotSize:int = obj["MaxMfgLotSize"]
      self.MfgLeadTime:int = obj["MfgLeadTime"]
      self.MinMfgLotSize:int = obj["MinMfgLotSize"]
      self.NeedByTimeDisp:str = obj["NeedByTimeDisp"]
      self.NonStock:bool = obj["NonStock"]
      self.OkToProcess:bool = obj["OkToProcess"]
      """  Holds the result of checking sub-menu security.  NO indicates the current user does not have permission to carry out the indicated TranType.  """  
      self.OnHandQtySite:int = obj["OnHandQtySite"]
      self.OnHandQtyWhse:int = obj["OnHandQtyWhse"]
      self.PlantName:str = obj["PlantName"]
      self.PrimWhseCode:str = obj["PrimWhseCode"]
      self.PrimWhseDesc:str = obj["PrimWhseDesc"]
      self.RequestedByEmpName:str = obj["RequestedByEmpName"]
      self.RequestError:bool = obj["RequestError"]
      """  Indicates whether an error occured in processing.  """  
      self.RequestMsg:str = obj["RequestMsg"]
      """  Message used to return status information after processing.  """  
      self.SameWhseGroupEmp:bool = obj["SameWhseGroupEmp"]
      """  Is this material queue row part of the employees warehouse group  """  
      self.SelectedByEmpName:str = obj["SelectedByEmpName"]
      self.SelectedForProcessing:bool = obj["SelectedForProcessing"]
      """  Used by user to select rows for mass processing  """  
      self.ShipToCity:str = obj["ShipToCity"]
      self.ShipToCountry:str = obj["ShipToCountry"]
      self.ShipToName:str = obj["ShipToName"]
      """  Customer Ship To Name  """  
      self.ShipToNum:str = obj["ShipToNum"]
      self.ShipToState:str = obj["ShipToState"]
      self.ShipToZIP:str = obj["ShipToZIP"]
      self.SortByPriority:int = obj["SortByPriority"]
      """  Sort priority from highest to lowest (1,2,3,4,5,6,7,8,9,0)  """  
      self.SourceTypeDesc:str = obj["SourceTypeDesc"]
      """  Transfer, Sales Kit, Manufactured or Purchased.  """  
      self.ToWhseDesc:str = obj["ToWhseDesc"]
      self.TransferLeadTime:int = obj["TransferLeadTime"]
      self.TransferPlant:str = obj["TransferPlant"]
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Readable tran type (used in Replenishment Workbench)  """  
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.WaveRelated:bool = obj["WaveRelated"]
      """  Value is true if this mtlqueue record is related to a wave. False if it is not.  """  
      self.CustRegionCode:str = obj["CustRegionCode"]
      """  Customer Sales Territory Region Code  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Display (decimal) number of pieces for inventory tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumVendorID_:str = obj["VendorNumVendorID_"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumName_:str = obj["VendorNumName_"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.WarehouseGroupCodeWhseGroupDesc:str = obj["WarehouseGroupCodeWhseGroupDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReplenishSuggRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.BinNum:str = obj["BinNum"]
      self.OnhandQty:int = obj["OnhandQty"]
      self.InProcessQty:int = obj["InProcessQty"]
      self.MoveQty:int = obj["MoveQty"]
      self.AfterMoveQty:int = obj["AfterMoveQty"]
      self.MinimumQty:int = obj["MinimumQty"]
      self.MaximumQty:int = obj["MaximumQty"]
      self.ReplenishQty:int = obj["ReplenishQty"]
      self.SafetyQty:int = obj["SafetyQty"]
      self.AllocatedQty:int = obj["AllocatedQty"]
      self.AvailQty:int = obj["AvailQty"]
      self.SelectedForProcessing:bool = obj["SelectedForProcessing"]
      self.BinZoneID:str = obj["BinZoneID"]
      self.BinZoneDesc:str = obj["BinZoneDesc"]
      self.TranType:str = obj["TranType"]
      """  Either RMN-STK or RMG-STK  """  
      self.IUM:str = obj["IUM"]
      self.ReservedQty:int = obj["ReservedQty"]
      self.TriggerPoint:str = obj["TriggerPoint"]
      self.TriggerSource:str = obj["TriggerSource"]
      self.InProcessSupplyQty:int = obj["InProcessSupplyQty"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AssignMoves_input:
   """ Required : 
   ipEmpID
   ipGrpID
   ds
   """  
   def __init__(self, obj):
      self.ipEmpID:str = obj["ipEmpID"]
      """  Emp ID to assign to  """  
      self.ipGrpID:str = obj["ipGrpID"]
      """  Group ID to assign to  """  
      self.ds:list[Erp_Tablesets_ReplenishmentTableset] = obj["ds"]
      pass

class AssignMoves_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReplenishmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AssignPriority_input:
   """ Required : 
   ipPriority
   ds
   """  
   def __init__(self, obj):
      self.ipPriority:int = obj["ipPriority"]
      """  Priority  """  
      self.ds:list[Erp_Tablesets_ReplenishmentTableset] = obj["ds"]
      pass

class AssignPriority_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReplenishmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CalculateAvailableQty_input:
   """ Required : 
   ipTranType
   ipIncludeSupplier
   ds
   """  
   def __init__(self, obj):
      self.ipTranType:str = obj["ipTranType"]
      """  TranType  """  
      self.ipIncludeSupplier:bool = obj["ipIncludeSupplier"]
      """  Include supplier bins  """  
      self.ds:list[Erp_Tablesets_ReplenishmentTableset] = obj["ds"]
      pass

class CalculateAvailableQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReplenishmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   mtlQueueSeq
   """  
   def __init__(self, obj):
      self.mtlQueueSeq:int = obj["mtlQueueSeq"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteMoves_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReplenishmentTableset] = obj["ds"]
      pass

class DeleteMoves_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReplenishmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_MtlQueueListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time(seconds since midnight) when transaction was created.  """  
      self.MtlQueueSeq:int = obj["MtlQueueSeq"]
      """  Number assigned by the system to uniquely identify the record.  Created by using the database sequence "MtlQueueSeq".  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of item in the container.  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity  """  
      self.TranType:str = obj["TranType"]
      """   Internal flag to indicate the type of transaction that this request is for.  This will control which functions are invoked for processing.
The same codes as in PartTran are used.  However, there are some additional codes also. 
They are; GET-WIP,  RTN-WIP, RTN-MTL, PUT-MTL, PUT-WIP, PICK-SO, PICK-JOB, PICK-TFO, BIN-REPLENISH, BIN-CONSOLIDATE, PICK-SO-XDOCK, PICK-JOB-XDOCK, PICK-TFO-XDOCK  """  
      self.ReferencePrefix:str = obj["ReferencePrefix"]
      """   Used as a translatable prefix for the Reference field.
For example for a purchase receipt of stock it has "PS", (Packing Slip). For display purposes this is field is translated, then concatenated with the value in the Refernce field. 
Other values are "Job",  """  
      self.Reference:str = obj["Reference"]
      """  Contains a reference about the request. May contain Job/Asm/Seq, WrkCtr,  Packing Slip #,  Sales Order, etc...depending on the TranType.  """  
      self.RequestedByEmpID:str = obj["RequestedByEmpID"]
      """  Employee ID that made the request.  """  
      self.SelectedByEmpID:str = obj["SelectedByEmpID"]
      """  Employee ID that has selected this record from the queue for processing.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that the request is related to.  This allows sorting by Job, which provides the user a method of working on all the requests for a specific job.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "O" = Job Operation (JobOper).  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of the related specific material or operation record.  For WIP parts it's the operation sequence that created the part. For raw materials it's the related JobMtl.MtlSeq.  """  
      self.FromWhse:str = obj["FromWhse"]
      """  Warehouse Code where item is to be found. For example a Get Raw Material request of a stocked part  would be the warehouse  the requirement was allocated against (JobMtl.WareHouseCode).  A "Move of a WIP part" will contain the Warehouse defined by the WrkCenter.PutWhse...  """  
      self.FromBinNum:str = obj["FromBinNum"]
      """  Warehouse bin where item is to be found. For example a Get Raw Material request of a stocked part  would be the Primary Bin of the part/warehouse, if no primary bin, then the first Bin in the warehouse which contains this part, else blank.  A "Move of a WIP part" will contain the bin defined by the WrkCenter.PutBin...  """  
      self.ToWhse:str = obj["ToWhse"]
      """  Warehouse where item should be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputWhse).  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  Warehouse bin where item is to be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputBin).  """  
      self.NextAssemblySeq:int = obj["NextAssemblySeq"]
      """  Assembly sequence of the operation that completed quantity of the job operation  will be moved to.  """  
      self.NextJobSeq:int = obj["NextJobSeq"]
      """  Sequence of the operation that completed quantity of the job operation will be moved to.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date the this request is needed by.  Defaults, to current system date.  """  
      self.NeedByTime:int = obj["NeedByTime"]
      """  Time (seconds since midnight) that request is need by.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor number of the related purchase receipt (RcvDtl).  Company,VendorNum, PurPoint, PackSlip,Packline are used to provide the link to the related RcvDtl record.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor purchase point id of the related purchase receipt (RcvDtl).  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip # of the related RcvDtl.  """  
      self.PackLine:int = obj["PackLine"]
      """  Vendors Packing Slip line  # of the related RcvDtl.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   Order number job is making parts for. (See JobProd.OrderNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

OrderNum pertains only to "make to order" requirements.  
Provides relationship to the JobProd for "make to order" requirements.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related Sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Related sales order release number.  """  
      self.TargetJobNum:str = obj["TargetJobNum"]
      """   Job that this job is making parts for. (See JobProd.TargetJobNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

TargetJobNum pertains only to "make to job" requirements.  
Provides relationship to the JobProd for "make to Job" requirements.  """  
      self.TargetAssemblySeq:int = obj["TargetAssemblySeq"]
      """  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.TargetMtlSeq:int = obj["TargetMtlSeq"]
      """  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  A description of the Part.  """  
      self.IUM:str = obj["IUM"]
      """  Internal unit of measure.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.Visible:bool = obj["Visible"]
      """  Indicates if this MtlQueue is visible to the user on the Material Queue browse.  Set based on the users response to make a "move  request" when reporting quantities.  Set to true visible), if a move request is made.  This was implemented to keep track of labor quantity reported without making a move request.  The move request will then reflect the total quantity to move instead of what was reported on the labor transaction that requested the move.  Regardless of making a "Move Request" labor quantity reporting always creates/updates a MtlQueue record.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Material Authorization number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMAReceipt number of the related RMARcpt record.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  RMADisp number of the related RMADisp record.  """  
      self.NCTranID:int = obj["NCTranID"]
      """  The related NonConf.TranID number. Used to link the MtlQueue table to the NonConf table.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the part.  """  
      self.Lock:bool = obj["Lock"]
      """  Indicates this record has been locked by a Advanced Shipping user and is not available for processing by any other user.  """  
      self.QueueID:str = obj["QueueID"]
      """  Used by Advanced Shipping to designate which queue this record is in.  Advanced Shipping queues can prioritize and process records.  """  
      self.QueuePickSeq:int = obj["QueuePickSeq"]
      """  Sequence of this record within an Advanced Shipping Queue.  """  
      self.ReleaseForPickingSeq:int = obj["ReleaseForPickingSeq"]
      """  This is an internal sequence number for grouping MtlQueue records.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group that was assigned to this transaction.  """  
      self.TranStatus:str = obj["TranStatus"]
      """   The status of the transaction of the material.  Valid values:
MGMT-LOCK - Manager locked, RELEASED - Released, HOLD - On Hold, USER-LOCK - Locked for a user, ORDER-HOLD - On Hold for Order Based Picking, QUALITY-HOLD - On Hold for Quality Control, and PICK-PACK - Three step allocation Pick-Pack Method  """  
      self.WaveNum:int = obj["WaveNum"]
      """  The Wave that was assigned during the allocation process.  """  
      self.Priority:int = obj["Priority"]
      """  Transaction Priority.  Valid values are 1,2,3,4,5,6,7,8,9.  One is the highest priority.  """  
      self.TranSource:str = obj["TranSource"]
      """  Transaction Source  """  
      self.LastMgrChangeEmpID:str = obj["LastMgrChangeEmpID"]
      """  When the TranStatus, AssignedToEmpID or Priority are modified, this value is updated with the ID of the Manager making the change.  """  
      self.AssignedToEmpID:str = obj["AssignedToEmpID"]
      """  Employee ID that was selected by the Warehouse Manager to process record from the queue.  """  
      self.TargetTFOrdNum:str = obj["TargetTFOrdNum"]
      """  Transfer Order for which Demand is being satisfied.  """  
      self.TargetTFOrdLine:int = obj["TargetTFOrdLine"]
      """  Transfer Order Line for which Demand is being satisfied.  """  
      self.PackStation:str = obj["PackStation"]
      """  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  """  
      self.DistributionType:str = obj["DistributionType"]
      """  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OkToProcess:bool = obj["OkToProcess"]
      """  Holds the result of checking sub-menu security.  NO indicates the current user does not have permission to carry out the indicated TranType.  """  
      self.RequestedByEmpName:str = obj["RequestedByEmpName"]
      self.SelectedByEmpName:str = obj["SelectedByEmpName"]
      self.NeedByTimeDisp:str = obj["NeedByTimeDisp"]
      self.SameWhseGroupEmp:bool = obj["SameWhseGroupEmp"]
      """  Is this material queue row part of the employees warehouse group  """  
      self.SortByPriority:int = obj["SortByPriority"]
      """  Sort priority from highest to lowest (1,2,3,4,5,6,7,8,9,0)  """  
      self.WaveRelated:bool = obj["WaveRelated"]
      """  Value is true if this mtlqueue record is related to a wave. False if it is not.  """  
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.POLinePartNum:str = obj["POLinePartNum"]
      """  OUR internal Part number for this item.  """  
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      """  Supplier Part Number  """  
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.PORelNumRefCodeDesc:str = obj["PORelNumRefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      """  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.WarehouseGroupCodeWhseGroupDesc:str = obj["WarehouseGroupCodeWhseGroupDesc"]
      """  Warehouse Group Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MtlQueueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time(seconds since midnight) when transaction was created.  """  
      self.MtlQueueSeq:int = obj["MtlQueueSeq"]
      """  Number assigned by the system to uniquely identify the record.  Created by using the database sequence "MtlQueueSeq".  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of item in the container.  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity  """  
      self.TranType:str = obj["TranType"]
      """   Internal flag to indicate the type of transaction that this request is for.  This will control which functions are invoked for processing.
The same codes as in PartTran are used.  However, there are some additional codes also. 
They are; GET-WIP,  RTN-WIP, RTN-MTL, PUT-MTL, PUT-WIP, PICK-SO, PICK-JOB, PICK-TFO, BIN-REPLENISH, BIN-CONSOLIDATE, PICK-SO-XDOCK, PICK-JOB-XDOCK, PICK-TFO-XDOCK  """  
      self.ReferencePrefix:str = obj["ReferencePrefix"]
      """   Used as a translatable prefix for the Reference field.
For example for a purchase receipt of stock it has "PS", (Packing Slip). For display purposes this is field is translated, then concatenated with the value in the Refernce field. 
Other values are "Job",  """  
      self.Reference:str = obj["Reference"]
      """  Contains a reference about the request. May contain Job/Asm/Seq, WrkCtr,  Packing Slip #,  Sales Order, etc...depending on the TranType.  """  
      self.RequestedByEmpID:str = obj["RequestedByEmpID"]
      """  Employee ID that made the request.  """  
      self.SelectedByEmpID:str = obj["SelectedByEmpID"]
      """  Employee ID that has selected this record from the queue for processing.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that the request is related to.  This allows sorting by Job, which provides the user a method of working on all the requests for a specific job.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "O" = Job Operation (JobOper).  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of the related specific material or operation record.  For WIP parts it's the operation sequence that created the part. For raw materials it's the related JobMtl.MtlSeq.  """  
      self.FromWhse:str = obj["FromWhse"]
      """  Warehouse Code where item is to be found. For example a Get Raw Material request of a stocked part  would be the warehouse  the requirement was allocated against (JobMtl.WareHouseCode).  A "Move of a WIP part" will contain the Warehouse defined by the WrkCenter.PutWhse...  """  
      self.FromBinNum:str = obj["FromBinNum"]
      """  Warehouse bin where item is to be found. For example a Get Raw Material request of a stocked part  would be the Primary Bin of the part/warehouse, if no primary bin, then the first Bin in the warehouse which contains this part, else blank.  A "Move of a WIP part" will contain the bin defined by the WrkCenter.PutBin...  """  
      self.ToWhse:str = obj["ToWhse"]
      """  Warehouse where item should be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputWhse).  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  Warehouse bin where item is to be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputBin).  """  
      self.NextAssemblySeq:int = obj["NextAssemblySeq"]
      """  Assembly sequence of the operation that completed quantity of the job operation  will be moved to.  """  
      self.NextJobSeq:int = obj["NextJobSeq"]
      """  Sequence of the operation that completed quantity of the job operation will be moved to.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date the this request is needed by.  Defaults, to current system date.  """  
      self.NeedByTime:int = obj["NeedByTime"]
      """  Time (seconds since midnight) that request is need by.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor number of the related purchase receipt (RcvDtl).  Company,VendorNum, PurPoint, PackSlip,Packline are used to provide the link to the related RcvDtl record.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor purchase point id of the related purchase receipt (RcvDtl).  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip # of the related RcvDtl.  """  
      self.PackLine:int = obj["PackLine"]
      """  Vendors Packing Slip line  # of the related RcvDtl.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   Order number job is making parts for. (See JobProd.OrderNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

OrderNum pertains only to "make to order" requirements.  
Provides relationship to the JobProd for "make to order" requirements.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related Sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Related sales order release number.  """  
      self.TargetJobNum:str = obj["TargetJobNum"]
      """   Job that this job is making parts for. (See JobProd.TargetJobNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

TargetJobNum pertains only to "make to job" requirements.  
Provides relationship to the JobProd for "make to Job" requirements.  """  
      self.TargetAssemblySeq:int = obj["TargetAssemblySeq"]
      """  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.TargetMtlSeq:int = obj["TargetMtlSeq"]
      """  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  A description of the Part.  """  
      self.IUM:str = obj["IUM"]
      """  Internal unit of measure.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.Visible:bool = obj["Visible"]
      """  Indicates if this MtlQueue is visible to the user on the Material Queue browse.  Set based on the users response to make a "move  request" when reporting quantities.  Set to true visible), if a move request is made.  This was implemented to keep track of labor quantity reported without making a move request.  The move request will then reflect the total quantity to move instead of what was reported on the labor transaction that requested the move.  Regardless of making a "Move Request" labor quantity reporting always creates/updates a MtlQueue record.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Material Authorization number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMAReceipt number of the related RMARcpt record.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  RMADisp number of the related RMADisp record.  """  
      self.NCTranID:int = obj["NCTranID"]
      """  The related NonConf.TranID number. Used to link the MtlQueue table to the NonConf table.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the part.  """  
      self.Lock:bool = obj["Lock"]
      """  Indicates this record has been locked by a Advanced Shipping user and is not available for processing by any other user.  """  
      self.QueueID:str = obj["QueueID"]
      """  Used by Advanced Shipping to designate which queue this record is in.  Advanced Shipping queues can prioritize and process records.  """  
      self.QueuePickSeq:int = obj["QueuePickSeq"]
      """  Sequence of this record within an Advanced Shipping Queue.  """  
      self.ReleaseForPickingSeq:int = obj["ReleaseForPickingSeq"]
      """  This is an internal sequence number for grouping MtlQueue records.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group that was assigned to this transaction.  """  
      self.TranStatus:str = obj["TranStatus"]
      """   The status of the transaction of the material.  Valid values:
MGMT-LOCK - Manager locked, RELEASED - Released, HOLD - On Hold, USER-LOCK - Locked for a user, ORDER-HOLD - On Hold for Order Based Picking, QUALITY-HOLD - On Hold for Quality Control, and PICK-PACK - Three step allocation Pick-Pack Method  """  
      self.WaveNum:int = obj["WaveNum"]
      """  The Wave that was assigned during the allocation process.  """  
      self.Priority:int = obj["Priority"]
      """  Transaction Priority.  Valid values are 1,2,3,4,5,6,7,8,9.  One is the highest priority.  """  
      self.TranSource:str = obj["TranSource"]
      """  Transaction Source  """  
      self.LastMgrChangeEmpID:str = obj["LastMgrChangeEmpID"]
      """  When the TranStatus, AssignedToEmpID or Priority are modified, this value is updated with the ID of the Manager making the change.  """  
      self.AssignedToEmpID:str = obj["AssignedToEmpID"]
      """  Employee ID that was selected by the Warehouse Manager to process record from the queue.  """  
      self.TargetTFOrdNum:str = obj["TargetTFOrdNum"]
      """  Transfer Order for which Demand is being satisfied.  """  
      self.TargetTFOrdLine:int = obj["TargetTFOrdLine"]
      """  Transfer Order Line for which Demand is being satisfied.  """  
      self.PackStation:str = obj["PackStation"]
      """  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  """  
      self.DistributionType:str = obj["DistributionType"]
      """  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.LastUsedPCID:str = obj["LastUsedPCID"]
      """  Last Used PCID on the selected line.  """  
      self.FromPCID:str = obj["FromPCID"]
      """  The PCID from which the material movement will occur.  """  
      self.ToPCID:str = obj["ToPCID"]
      """  The PCID to which the material movement will occur.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeValueSeq:int = obj["AttributeValueSeq"]
      """  AttributeValueSeq  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.CustID:str = obj["CustID"]
      self.CustTerritoryID:str = obj["CustTerritoryID"]
      self.DisableTO:bool = obj["DisableTO"]
      """  Indicates whether Transfer Order Selector Flag should be disabled.  """  
      self.FromInv:bool = obj["FromInv"]
      """  From Inventory Selector Flag  """  
      self.FromJob:bool = obj["FromJob"]
      """  From Manufacturing Selector Flag  """  
      self.FromPO:bool = obj["FromPO"]
      """  From Purchasing Selector Flag  """  
      self.FromTO:bool = obj["FromTO"]
      """  From Transfer Order Selector Flag  """  
      self.FromWhseDesc:str = obj["FromWhseDesc"]
      self.FSAServiceOrderNumber:int = obj["FSAServiceOrderNumber"]
      """  Service Order Number from FSA. Only available in FSA Request Workbench.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource Num from FSA. Only available in FSA Request Workbench.  """  
      self.HoldStatus:bool = obj["HoldStatus"]
      self.LeadTime:int = obj["LeadTime"]
      self.MaxMfgLotSize:int = obj["MaxMfgLotSize"]
      self.MfgLeadTime:int = obj["MfgLeadTime"]
      self.MinMfgLotSize:int = obj["MinMfgLotSize"]
      self.NeedByTimeDisp:str = obj["NeedByTimeDisp"]
      self.NonStock:bool = obj["NonStock"]
      self.OkToProcess:bool = obj["OkToProcess"]
      """  Holds the result of checking sub-menu security.  NO indicates the current user does not have permission to carry out the indicated TranType.  """  
      self.OnHandQtySite:int = obj["OnHandQtySite"]
      self.OnHandQtyWhse:int = obj["OnHandQtyWhse"]
      self.PlantName:str = obj["PlantName"]
      self.PrimWhseCode:str = obj["PrimWhseCode"]
      self.PrimWhseDesc:str = obj["PrimWhseDesc"]
      self.RequestedByEmpName:str = obj["RequestedByEmpName"]
      self.RequestError:bool = obj["RequestError"]
      """  Indicates whether an error occured in processing.  """  
      self.RequestMsg:str = obj["RequestMsg"]
      """  Message used to return status information after processing.  """  
      self.SameWhseGroupEmp:bool = obj["SameWhseGroupEmp"]
      """  Is this material queue row part of the employees warehouse group  """  
      self.SelectedByEmpName:str = obj["SelectedByEmpName"]
      self.SelectedForProcessing:bool = obj["SelectedForProcessing"]
      """  Used by user to select rows for mass processing  """  
      self.ShipToCity:str = obj["ShipToCity"]
      self.ShipToCountry:str = obj["ShipToCountry"]
      self.ShipToName:str = obj["ShipToName"]
      """  Customer Ship To Name  """  
      self.ShipToNum:str = obj["ShipToNum"]
      self.ShipToState:str = obj["ShipToState"]
      self.ShipToZIP:str = obj["ShipToZIP"]
      self.SortByPriority:int = obj["SortByPriority"]
      """  Sort priority from highest to lowest (1,2,3,4,5,6,7,8,9,0)  """  
      self.SourceTypeDesc:str = obj["SourceTypeDesc"]
      """  Transfer, Sales Kit, Manufactured or Purchased.  """  
      self.ToWhseDesc:str = obj["ToWhseDesc"]
      self.TransferLeadTime:int = obj["TransferLeadTime"]
      self.TransferPlant:str = obj["TransferPlant"]
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Readable tran type (used in Replenishment Workbench)  """  
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.WaveRelated:bool = obj["WaveRelated"]
      """  Value is true if this mtlqueue record is related to a wave. False if it is not.  """  
      self.CustRegionCode:str = obj["CustRegionCode"]
      """  Customer Sales Territory Region Code  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Display (decimal) number of pieces for inventory tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumVendorID_:str = obj["VendorNumVendorID_"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumName_:str = obj["VendorNumName_"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.WarehouseGroupCodeWhseGroupDesc:str = obj["WarehouseGroupCodeWhseGroupDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReplenishSuggRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.BinNum:str = obj["BinNum"]
      self.OnhandQty:int = obj["OnhandQty"]
      self.InProcessQty:int = obj["InProcessQty"]
      self.MoveQty:int = obj["MoveQty"]
      self.AfterMoveQty:int = obj["AfterMoveQty"]
      self.MinimumQty:int = obj["MinimumQty"]
      self.MaximumQty:int = obj["MaximumQty"]
      self.ReplenishQty:int = obj["ReplenishQty"]
      self.SafetyQty:int = obj["SafetyQty"]
      self.AllocatedQty:int = obj["AllocatedQty"]
      self.AvailQty:int = obj["AvailQty"]
      self.SelectedForProcessing:bool = obj["SelectedForProcessing"]
      self.BinZoneID:str = obj["BinZoneID"]
      self.BinZoneDesc:str = obj["BinZoneDesc"]
      self.TranType:str = obj["TranType"]
      """  Either RMN-STK or RMG-STK  """  
      self.IUM:str = obj["IUM"]
      self.ReservedQty:int = obj["ReservedQty"]
      self.TriggerPoint:str = obj["TriggerPoint"]
      self.TriggerSource:str = obj["TriggerSource"]
      self.InProcessSupplyQty:int = obj["InProcessSupplyQty"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReplenishmentListTableset:
   def __init__(self, obj):
      self.MtlQueueList:list[Erp_Tablesets_MtlQueueListRow] = obj["MtlQueueList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ReplenishmentTableset:
   def __init__(self, obj):
      self.MtlQueue:list[Erp_Tablesets_MtlQueueRow] = obj["MtlQueue"]
      self.ReplenishSugg:list[Erp_Tablesets_ReplenishSuggRow] = obj["ReplenishSugg"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtReplenishmentTableset:
   def __init__(self, obj):
      self.MtlQueue:list[Erp_Tablesets_MtlQueueRow] = obj["MtlQueue"]
      self.ReplenishSugg:list[Erp_Tablesets_ReplenishSuggRow] = obj["ReplenishSugg"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenerateManaged_input:
   """ Required : 
   ipWarehouseCode
   ipBinType
   ipZone
   ipBinStart
   ipBinEnd
   ipPartNum
   ipPartClass
   ipPartGroup
   """  
   def __init__(self, obj):
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      """  Warehouse  """  
      self.ipBinType:str = obj["ipBinType"]
      """  Bin Type  """  
      self.ipZone:str = obj["ipZone"]
      """  Zone  """  
      self.ipBinStart:str = obj["ipBinStart"]
      """  Start Bin  """  
      self.ipBinEnd:str = obj["ipBinEnd"]
      """  End Bin  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  Fill to Max ("M") or Replenishment ("R") or None ("N")  """  
      self.ipPartClass:str = obj["ipPartClass"]
      """  Include over maximum  """  
      self.ipPartGroup:str = obj["ipPartGroup"]
      """  Include zero moves  """  
      pass

class GenerateManaged_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReplenishmentTableset] = obj["returnObj"]
      pass

class GenerateManual_input:
   """ Required : 
   ipWarehouseCode
   ipBinType
   ipZone
   ipBinStart
   ipBinEnd
   ipIncludeAuto
   ipFillMode
   ipIncludeAboveMax
   ipIncludeAboveMin
   ipIncludeAboveThreshold
   ipIncludeBelowThreshold
   """  
   def __init__(self, obj):
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      """  Warehouse  """  
      self.ipBinType:str = obj["ipBinType"]
      """  Bin Type  """  
      self.ipZone:str = obj["ipZone"]
      """  Zone  """  
      self.ipBinStart:str = obj["ipBinStart"]
      """  Start Bin  """  
      self.ipBinEnd:str = obj["ipBinEnd"]
      """  End Bin  """  
      self.ipIncludeAuto:bool = obj["ipIncludeAuto"]
      """  Include Auto Replenishment  """  
      self.ipFillMode:str = obj["ipFillMode"]
      """  Fill to Max ("M") or Replenishment ("R") or None ("N")  """  
      self.ipIncludeAboveMax:bool = obj["ipIncludeAboveMax"]
      """  Include over maximum  """  
      self.ipIncludeAboveMin:bool = obj["ipIncludeAboveMin"]
      """  Include over minimum  """  
      self.ipIncludeAboveThreshold:bool = obj["ipIncludeAboveThreshold"]
      """  Include over safety  """  
      self.ipIncludeBelowThreshold:bool = obj["ipIncludeBelowThreshold"]
      """  Include below safety  """  
      pass

class GenerateManual_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReplenishmentTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   mtlQueueSeq
   """  
   def __init__(self, obj):
      self.mtlQueueSeq:int = obj["mtlQueueSeq"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReplenishmentTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ReplenishmentTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ReplenishmentTableset] = obj["returnObj"]
      pass

class GetDefaultWhse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opWarehouseCode:str = obj["parameters"]
      self.opWarehouseDesc:str = obj["parameters"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Erp_Tablesets_ReplenishmentListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMoveRequests_input:
   """ Required : 
   ipAuto
   ipManual
   ipManaged
   ipToWarehouseCode
   """  
   def __init__(self, obj):
      self.ipAuto:bool = obj["ipAuto"]
      """  Include RAU-STK?  """  
      self.ipManual:bool = obj["ipManual"]
      """  Include RMN-STK?  """  
      self.ipManaged:bool = obj["ipManaged"]
      """  Include RMG-STK?  """  
      self.ipToWarehouseCode:str = obj["ipToWarehouseCode"]
      """  To Warehouse Code  """  
      pass

class GetMoveRequests_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReplenishmentTableset] = obj["returnObj"]
      pass

class GetNewMtlQueue_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReplenishmentTableset] = obj["ds"]
      pass

class GetNewMtlQueue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReplenishmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseMtlQueue
   whereClauseReplenishSugg
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMtlQueue:str = obj["whereClauseMtlQueue"]
      self.whereClauseReplenishSugg:str = obj["whereClauseReplenishSugg"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReplenishmentTableset] = obj["returnObj"]
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

class OnChangeMoveQty_input:
   """ Required : 
   ipMoveQty
   ipTranType
   ipPartNum
   ipWarehouseCode
   ipBinNum
   ds
   """  
   def __init__(self, obj):
      self.ipMoveQty:int = obj["ipMoveQty"]
      """  New Move Quantity  """  
      self.ipTranType:str = obj["ipTranType"]
      """  Transaction Type  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  Part Number  """  
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      """  Warehouse Code  """  
      self.ipBinNum:str = obj["ipBinNum"]
      """  Bin Num  """  
      self.ds:list[Erp_Tablesets_ReplenishmentTableset] = obj["ds"]
      pass

class OnChangeMoveQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReplenishmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingMoveQty_input:
   """ Required : 
   ipMoveQty
   ipAvailQty
   """  
   def __init__(self, obj):
      self.ipMoveQty:int = obj["ipMoveQty"]
      """  New Move Quantity  """  
      self.ipAvailQty:int = obj["ipAvailQty"]
      """  AvailQty  """  
      pass

class OnChangingMoveQty_output:
   def __init__(self, obj):
      pass

class ProcessManagedReplenishment_input:
   """ Required : 
   ipIncludeSupplier
   ds
   """  
   def __init__(self, obj):
      self.ipIncludeSupplier:bool = obj["ipIncludeSupplier"]
      """  Include supplier bins  """  
      self.ds:list[Erp_Tablesets_ReplenishmentTableset] = obj["ds"]
      pass

class ProcessManagedReplenishment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReplenishmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ProcessManualReplenishment_input:
   """ Required : 
   ipIncludeSupplier
   ds
   """  
   def __init__(self, obj):
      self.ipIncludeSupplier:bool = obj["ipIncludeSupplier"]
      """  Include supplier bins  """  
      self.ds:list[Erp_Tablesets_ReplenishmentTableset] = obj["ds"]
      pass

class ProcessManualReplenishment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReplenishmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ToggleHoldStatus_input:
   """ Required : 
   ipHold
   ds
   """  
   def __init__(self, obj):
      self.ipHold:bool = obj["ipHold"]
      """  Set to hold? (Otherwise set to release)  """  
      self.ds:list[Erp_Tablesets_ReplenishmentTableset] = obj["ds"]
      pass

class ToggleHoldStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReplenishmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtReplenishmentTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtReplenishmentTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReplenishmentTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReplenishmentTableset] = obj["ds"]
      pass

      """  output parameters  """  

