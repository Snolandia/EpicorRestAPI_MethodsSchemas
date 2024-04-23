import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.WorkQueueSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_WorkQueues(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WorkQueues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WorkQueues
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WorkQueueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/WorkQueues",headers=creds) as resp:
           return await resp.json()

async def post_WorkQueues(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WorkQueues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WorkQueueRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WorkQueueRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/WorkQueues", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WorkQueues_Company_JobNum_AssemblySeq_OprSeq(Company, JobNum, AssemblySeq, OprSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WorkQueue item
   Description: Calls GetByID to retrieve the WorkQueue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WorkQueue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WorkQueueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/WorkQueues(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WorkQueues_Company_JobNum_AssemblySeq_OprSeq(Company, JobNum, AssemblySeq, OprSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WorkQueue for the service
   Description: Calls UpdateExt to update WorkQueue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WorkQueue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WorkQueueRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/WorkQueues(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WorkQueues_Company_JobNum_AssemblySeq_OprSeq(Company, JobNum, AssemblySeq, OprSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WorkQueue item
   Description: Call UpdateExt to delete WorkQueue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WorkQueue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/WorkQueues(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_WorkQueues_Company_JobNum_AssemblySeq_OprSeq_LaborOperActions(Company, JobNum, AssemblySeq, OprSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LaborOperActions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborOperActions1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborOperActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/WorkQueues(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + ")/LaborOperActions",headers=creds) as resp:
           return await resp.json()

async def get_WorkQueues_Company_JobNum_AssemblySeq_OprSeq_LaborOperActions_SysRowID(Company, JobNum, AssemblySeq, OprSeq, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborOperAction item
   Description: Calls GetByID to retrieve the LaborOperAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborOperAction1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborOperActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/WorkQueues(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + ")/LaborOperActions(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_WorkQueues_Company_JobNum_AssemblySeq_OprSeq_PartWipOps(Company, JobNum, AssemblySeq, OprSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PartWipOps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PartWipOps1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartWipOpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/WorkQueues(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + ")/PartWipOps",headers=creds) as resp:
           return await resp.json()

async def get_WorkQueues_Company_JobNum_AssemblySeq_OprSeq_PartWipOps_Company_Plant_PartNum_JobNum_AssemblySeq_OprSeq_WareHouseCode_BinNum_LotNum_DimCode_TrackType_MtlSeq_AttributeSetID_SysRowID(Company, JobNum, AssemblySeq, OprSeq, Plant, PartNum, WareHouseCode, BinNum, LotNum, DimCode, TrackType, MtlSeq, AttributeSetID, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartWipOp item
   Description: Calls GetByID to retrieve the PartWipOp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartWipOp1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param WareHouseCode: Desc: WareHouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param DimCode: Desc: DimCode   Required: True   Allow empty value : True
      :param TrackType: Desc: TrackType   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartWipOpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/WorkQueues(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + ")/PartWipOps(" + Company + "," + Plant + "," + PartNum + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + WareHouseCode + "," + BinNum + "," + LotNum + "," + DimCode + "," + TrackType + "," + MtlSeq + "," + AttributeSetID + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborOperActions(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LaborOperActions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborOperActions
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborOperActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/LaborOperActions",headers=creds) as resp:
           return await resp.json()

async def post_LaborOperActions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborOperActions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborOperActionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborOperActionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/LaborOperActions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LaborOperActions_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborOperAction item
   Description: Calls GetByID to retrieve the LaborOperAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborOperAction
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborOperActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/LaborOperActions(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LaborOperActions_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LaborOperAction for the service
   Description: Calls UpdateExt to update LaborOperAction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborOperAction
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborOperActionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/LaborOperActions(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LaborOperActions_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LaborOperAction item
   Description: Call UpdateExt to delete LaborOperAction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborOperAction
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/LaborOperActions(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PartWipOps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartWipOps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartWipOps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartWipOpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/PartWipOps",headers=creds) as resp:
           return await resp.json()

async def post_PartWipOps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartWipOps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartWipOpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartWipOpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/PartWipOps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PartWipOps_Company_Plant_PartNum_JobNum_AssemblySeq_OprSeq_WareHouseCode_BinNum_LotNum_DimCode_TrackType_MtlSeq_AttributeSetID_SysRowID(Company, Plant, PartNum, JobNum, AssemblySeq, OprSeq, WareHouseCode, BinNum, LotNum, DimCode, TrackType, MtlSeq, AttributeSetID, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartWipOp item
   Description: Calls GetByID to retrieve the PartWipOp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartWipOp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param WareHouseCode: Desc: WareHouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param DimCode: Desc: DimCode   Required: True   Allow empty value : True
      :param TrackType: Desc: TrackType   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartWipOpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/PartWipOps(" + Company + "," + Plant + "," + PartNum + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + WareHouseCode + "," + BinNum + "," + LotNum + "," + DimCode + "," + TrackType + "," + MtlSeq + "," + AttributeSetID + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PartWipOps_Company_Plant_PartNum_JobNum_AssemblySeq_OprSeq_WareHouseCode_BinNum_LotNum_DimCode_TrackType_MtlSeq_AttributeSetID_SysRowID(Company, Plant, PartNum, JobNum, AssemblySeq, OprSeq, WareHouseCode, BinNum, LotNum, DimCode, TrackType, MtlSeq, AttributeSetID, SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PartWipOp for the service
   Description: Calls UpdateExt to update PartWipOp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartWipOp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param WareHouseCode: Desc: WareHouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param DimCode: Desc: DimCode   Required: True   Allow empty value : True
      :param TrackType: Desc: TrackType   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartWipOpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/PartWipOps(" + Company + "," + Plant + "," + PartNum + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + WareHouseCode + "," + BinNum + "," + LotNum + "," + DimCode + "," + TrackType + "," + MtlSeq + "," + AttributeSetID + "," + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PartWipOps_Company_Plant_PartNum_JobNum_AssemblySeq_OprSeq_WareHouseCode_BinNum_LotNum_DimCode_TrackType_MtlSeq_AttributeSetID_SysRowID(Company, Plant, PartNum, JobNum, AssemblySeq, OprSeq, WareHouseCode, BinNum, LotNum, DimCode, TrackType, MtlSeq, AttributeSetID, SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PartWipOp item
   Description: Call UpdateExt to delete PartWipOp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartWipOp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param JobNum: Desc: JobNum   Required: True   Allow empty value : True
      :param AssemblySeq: Desc: AssemblySeq   Required: True
      :param OprSeq: Desc: OprSeq   Required: True
      :param WareHouseCode: Desc: WareHouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param DimCode: Desc: DimCode   Required: True   Allow empty value : True
      :param TrackType: Desc: TrackType   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/PartWipOps(" + Company + "," + Plant + "," + PartNum + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + WareHouseCode + "," + BinNum + "," + LotNum + "," + DimCode + "," + TrackType + "," + MtlSeq + "," + AttributeSetID + "," + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WorkQueueListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseWorkQueue, whereClauseLaborOperAction, whereClausePartWipOp, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseWorkQueue=" + whereClauseWorkQueue
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLaborOperAction=" + whereClauseLaborOperAction
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePartWipOp=" + whereClausePartWipOp
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(jobNum, assemblySeq, oprSeq, epicorHeaders = None):
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
   params += "oprSeq=" + oprSeq

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetOpsInResourceGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetOpsInResourceGroup
   Description: To build the priority dispatch temp table (JCR65) from the JobOper records for the given workcenter.
This procedure reads the JobOper, and sets values of certain variables used by the BuildTempTable
procedure defined in JCR65-RP.i
   OperationID: GetOpsInResourceGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOpsInResourceGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOpsInResourceGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLaborOperActionDS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLaborOperActionDS
   Description: GetLaborOperActionDS
   OperationID: GetLaborOperActionDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLaborOperActionDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLaborOperActionDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetOpsInResourceGroupWithBaq(ipBaqID, ipResourceGrpID, ipEmpID, ipLaborType, ipStartDate, ipJobNum, ipAssemblySeq, ipOpCode, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetOpsInResourceGroupWithBaq
   Description: Extension of GetOpsInResourceGroup which takes a BAQ, executes and processes the results for the Work Queue.
   OperationID: Get_GetOpsInResourceGroupWithBaq
      :param ipBaqID: Desc: BAQ Query ID   Required: True   Allow empty value : True
      :param ipResourceGrpID: Desc: Resource Group ID   Required: True   Allow empty value : True
      :param ipEmpID: Desc: Employee ID   Required: True   Allow empty value : True
      :param ipLaborType: Desc: Labor Type   Required: True   Allow empty value : True
      :param ipStartDate: Desc: Start Date to cut off from   Required: True   Allow empty value : True
      :param ipJobNum: Desc: Job, empty will exclude from filter   Required: True   Allow empty value : True
      :param ipAssemblySeq: Desc: Assembly Seq, empty will exclude from filter   Required: True   Allow empty value : True
      :param ipOpCode: Desc: Operation Code, empty will exclude from filter   Required: True   Allow empty value : True
      :param pageSize: Desc: Page Size   Required: True
      :param absolutePage: Desc: Absolute Page   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOpsInResourceGroupWithBaq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ipBaqID=" + ipBaqID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ipResourceGrpID=" + ipResourceGrpID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ipEmpID=" + ipEmpID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ipLaborType=" + ipLaborType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ipStartDate=" + ipStartDate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ipJobNum=" + ipJobNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ipAssemblySeq=" + ipAssemblySeq
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ipOpCode=" + ipOpCode
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_RefreshSelectedRecords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshSelectedRecords
   Description: Refresh the selected records within the Work Queue
   OperationID: RefreshSelectedRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshSelectedRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshSelectedRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EndActivity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EndActivity
   Description: End Activity on the selected work.
   OperationID: EndActivity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EndActivity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EndActivity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWorkQueue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWorkQueue
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWorkQueue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWorkQueue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWorkQueue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartWipOp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartWipOp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartWipOp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartWipOp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartWipOp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborOperActionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LaborOperActionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartWipOpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartWipOpRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WorkQueueListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WorkQueueListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WorkQueueRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WorkQueueRow] = obj["value"]
      pass

class Erp_Tablesets_LaborOperActionRow:
   def __init__(self, obj):
      self.ActionDesc:str = obj["ActionDesc"]
      """  Description of Action.  """  
      self.ActionSeq:int = obj["ActionSeq"]
      """  A sequence number which uniquely identifies action record within the operation set.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number which uniquely identifies the assembly record within the method.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Completed:bool = obj["Completed"]
      """  Indicates if this Action was completed.  """  
      self.CompletedBy:str = obj["CompletedBy"]
      """  The number of the employee that performed the work.  """  
      self.CompletedByName:str = obj["CompletedByName"]
      """  Name of the user ID in CompletedBy  """  
      self.CompletedOn:str = obj["CompletedOn"]
      """  Date the Action was completed.  """  
      self.JobNum:str = obj["JobNum"]
      """  JobNum  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  Used as the foreign key to the LaborDtl record.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborDtl record.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the method.  """  
      self.Required:bool = obj["Required"]
      """  Indicated if this Action must be completed before Operation can be completed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartWipOpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of item in the container.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that the part allocated to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence which may be on the next assembly sequence.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  job operation sequence number that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  The MtlSeq of the related JobMtl record.  Pertains only to  Raw Materials (TrackType = "R")  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """   Warehouse Code of the warehouse where the container of parts are currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutWhse of the workcenter that created the parts.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the parts.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the parts.  """  
      self.BinNum:str = obj["BinNum"]
      """   Warehouse Bin where the container is currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutBinNum of the workcenter that created the parts.  """  
      self.TrackType:str = obj["TrackType"]
      """   Internal flag to distiguish between tracking of issued raw material, and the actual manufactured product.
"R" - Raw Material a part which was issued to the job.
"M" - Manufactured Part. The part that is being manufactured.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group of the related operation.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation code of the related job operation.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.Quantity:int = obj["Quantity"]
      """  Part Quantity balance for a  Job/Asm/Opr at a warehouse/bin location.  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure of items in the container.  """  
      self.FromAssemblySeq:int = obj["FromAssemblySeq"]
      """  Assembly Sequence # which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  """  
      self.FromOprSeq:int = obj["FromOprSeq"]
      """  Operation Sequence # which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  """  
      self.FromResourceGrpID:str = obj["FromResourceGrpID"]
      """  Resource Group which created the parts allocated to this operation.  This only pertains to semi-finished manufactured parts (TrackType = M)  """  
      self.FromOpCode:str = obj["FromOpCode"]
      """  Operation Code which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  """  
      self.LastActivityDate:str = obj["LastActivityDate"]
      """  Last Activity Date.  """  
      self.LastActivityTime:int = obj["LastActivityTime"]
      """  Time of last activity expressed in seconds from midnight.  """  
      self.FinalOp:bool = obj["FinalOp"]
      """  Indicates if the completed (OutPut) quantity is for the final operation.  It is used as a filter in Part Tracker to find completed quantities that have not been moved off the job.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.UpdateStageQty:str = obj["UpdateStageQty"]
      """  Used in the PartWip write trigger to control update to JobMtl.QtyStagedToDate field. Only transactions which  move the material in/out of the staging area update this field.  This field will contain the transaction type that moved the material. For example; STK-MTL(issue of stock), PUR-MTL( movement of purchased material), MTL-STK( Returns to stock).  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.TrackTypeDesc:str = obj["TrackTypeDesc"]
      self.PartDescription:str = obj["PartDescription"]
      self.PageNum:int = obj["PageNum"]
      """  Used for caching pagination in UI  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WorkQueueListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JCDept:str = obj["JCDept"]
      """  The Key ID of the Home Department for this Resource Group.  This is a foreign key to the JCDept table.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence # that this Operation is associated with.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.OprQty:int = obj["OprQty"]
      """  The total operation quantity. This is a calculated field.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master Code - Links the JobOper  record with a OpMaster record.  Default is given from WrkCenter.OpCode.  Must be valid in the OpMaster file.  """  
      self.EstSetHours:int = obj["EstSetHours"]
      """  Total estimated set up hours.  Calculated as EstSetHoursPerMch * Machines.  It is set to zero if operation qty is zero.  This is maintained via the JobOper write trigger.  """  
      self.EstProdHours:int = obj["EstProdHours"]
      """   The estimated Production run hours for internal operations (JobOper.Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to  recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (JobOper.RunQty / Std).
If StdFormat = "PM" then (JobOper.RunQty / Std ) / 60.
If StdFormat = "OH" then (JobOper.RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((JobOper.RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (JobOPer.RunQty/Basis) X Std.
If StdFormat = "MP" then ((JobOper.RunQty/Basis) X Std) / 60.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  """  
      self.SchedCode:str = obj["SchedCode"]
      """  Scheduling Code.  SchedCode references a record in the SchedPri table.  """  
      self.SetupLoadHrs:int = obj["SetupLoadHrs"]
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  """  
      self.ProdLoadHrs:int = obj["ProdLoadHrs"]
      self.RegionCode:int = obj["RegionCode"]
      """  1=CurrentWork, 2=AvailableWork, 3=ExpectedWork  """  
      self.OpsPerPart:int = obj["OpsPerPart"]
      """  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  """  
      self.StartDate:str = obj["StartDate"]
      """  Scheduled production start date. Not directly maintainable, updated via the scheduling process.  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  """  
      self.DueDate:str = obj["DueDate"]
      """  Scheduled production due date. Not directly maintainable, updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  """  
      self.SortDate:str = obj["SortDate"]
      self.WIPQty:int = obj["WIPQty"]
      self.CrewCount:int = obj["CrewCount"]
      """  Number Of Employees Now Working On This Operation  """  
      self.QtyLeft:int = obj["QtyLeft"]
      self.SetupLeft:int = obj["SetupLeft"]
      self.WIPQtyDetails:bool = obj["WIPQtyDetails"]
      """  TRUE indicates there are WIP Qty Details available (i.e. the Staged Details button should be enabled)  """  
      self.Machines:int = obj["Machines"]
      """  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  """  
      self.CanRequest:bool = obj["CanRequest"]
      """  TRUE indicates the current employee is authorized to Request Material  """  
      self.CanSelect:bool = obj["CanSelect"]
      """  TRUE indicates the current employee can select this operation to work on (i.e. the Select For Work button should be enabled).  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to setup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.JobHeadPartNum:str = obj["JobHeadPartNum"]
      """  Part number of the manufactured item.  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  """  
      self.JobHeadPartDescription:str = obj["JobHeadPartDescription"]
      """  The description of the part that is to be manufactured.  """  
      self.OprCommentText:str = obj["OprCommentText"]
      """  Editor widget for Job operation comments.  """  
      self.AsmCommentText:str = obj["AsmCommentText"]
      """  Editor widget for Job header comments.  """  
      self.JobHeadCommentText:str = obj["JobHeadCommentText"]
      """  Editor widget for Job header comments.  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  """  
      self.RegionDescription:str = obj["RegionDescription"]
      """  "Current Work", "Available Work", or "Expected Work" as indicated by the RegionCode.  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  Uniquely identifies an OpDtl.  System assigned.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum to be shipped to the subcontract. Default the JobHead.PartNum or JobAsmbl.PartNum depending on the JobMtl.AssemblySeq.  """  
      self.OpDtlDescription:str = obj["OpDtlDescription"]
      """  Description is initially created when the JobOpDtl is created.  """  
      self.OpDtlType:str = obj["OpDtlType"]
      """  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "Setup", "Production", or "Both".  """  
      self.Description:str = obj["Description"]
      """  Description used only for subcontract operations  """  
      self.SortHour:int = obj["SortHour"]
      """  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job operation comments.  """  
      self.Selected:bool = obj["Selected"]
      """  Used by the UI to allow selection of rows  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Description for PartNum  """  
      self.RunQty:int = obj["RunQty"]
      """   The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0.
This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  """  
      self.SchResourceList:str = obj["SchResourceList"]
      """  Delimited list of resources oper is schedueld to  """  
      self.CurQty:int = obj["CurQty"]
      """  Current Production Qty (for user reporting qty)  """  
      self.LaborQty:int = obj["LaborQty"]
      """  Qty currently being completed  """  
      self.ScrapQty:int = obj["ScrapQty"]
      """  Scrap Qty currently being entered  """  
      self.DiscrepQty:int = obj["DiscrepQty"]
      """  Discrep Qty currently being entered  """  
      self.DiscrepRsnCode:str = obj["DiscrepRsnCode"]
      """  Reason code for discrep qty currently being entered  """  
      self.ScrapRsnCode:str = obj["ScrapRsnCode"]
      """  Reason code for scrap currently being entered  """  
      self.ScrapRsnDesc:str = obj["ScrapRsnDesc"]
      """  Description for ScrapRsnCode  """  
      self.DiscrepRsnDesc:str = obj["DiscrepRsnDesc"]
      """  Description for DescrepRsnCode  """  
      self.Complete:bool = obj["Complete"]
      """  Operation complete  """  
      self.ResourceID:str = obj["ResourceID"]
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  """  
      self.FirstCustNum:int = obj["FirstCustNum"]
      """  CustNum from first order  """  
      self.FirstCustID:str = obj["FirstCustID"]
      self.FirstCustName:str = obj["FirstCustName"]
      self.FirstShipViaCode:str = obj["FirstShipViaCode"]
      self.FirstShipViaDesc:str = obj["FirstShipViaDesc"]
      self.SetupGrpDesc:str = obj["SetupGrpDesc"]
      self.SetupGroup:str = obj["SetupGroup"]
      """  Used to group operation to save on setups.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.Date01:str = obj["Date01"]
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WorkQueueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JCDept:str = obj["JCDept"]
      """  The Key ID of the Home Department for this Resource Group.  This is a foreign key to the JCDept table.  """  
      self.OpComplete:bool = obj["OpComplete"]
      """   Indicates if this operation is completed. This is normally set to complete via labor entry transactions.   Not maintainable by Job Entry. It can't be reset to "No" if the JobHead.Complete = Yes.
Labor entry setting logic is: If SetUpComplete = Yes and  EstProdHours = 0 or ProdComplete = Yes and EstSetHours = 0 or both ProdComplete = Yes and SetupComplete = Yes  then OpComplete = Yes.
This field is also set by PO receipt entry "issue complete" for subcontract operations.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence # that this Operation is associated with.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.OprQty:int = obj["OprQty"]
      """  The total operation quantity. This is a calculated field.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master Code - Links the JobOper  record with a OpMaster record.  Default is given from WrkCenter.OpCode.  Must be valid in the OpMaster file.  """  
      self.EstSetHours:int = obj["EstSetHours"]
      """  Total estimated set up hours.  Calculated as EstSetHoursPerMch * Machines.  It is set to zero if operation qty is zero.  This is maintained via the JobOper write trigger.  """  
      self.EstProdHours:int = obj["EstProdHours"]
      """   The estimated Production run hours for internal operations (JobOper.Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to  recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (JobOper.RunQty / Std).
If StdFormat = "PM" then (JobOper.RunQty / Std ) / 60.
If StdFormat = "OH" then (JobOper.RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((JobOper.RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (JobOPer.RunQty/Basis) X Std.
If StdFormat = "MP" then ((JobOper.RunQty/Basis) X Std) / 60.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  """  
      self.SchedCode:str = obj["SchedCode"]
      """  Scheduling Code.  SchedCode references a record in the SchedPri table.  """  
      self.SetupLoadHrs:int = obj["SetupLoadHrs"]
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  """  
      self.ProdLoadHrs:int = obj["ProdLoadHrs"]
      self.OpsPerPart:int = obj["OpsPerPart"]
      """  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  """  
      self.RegionCode:int = obj["RegionCode"]
      """  1=CurrentWork, 2=AvailableWork, 3=ExpectedWork  """  
      self.StartDate:str = obj["StartDate"]
      """  Scheduled production start date. Not directly maintainable, updated via the scheduling process.  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  """  
      self.DueDate:str = obj["DueDate"]
      """  Scheduled production due date. Not directly maintainable, updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  """  
      self.SortDate:str = obj["SortDate"]
      self.WIPQty:int = obj["WIPQty"]
      self.CrewCount:int = obj["CrewCount"]
      """  Number Of Employees Now Working On This Operation  """  
      self.QtyLeft:int = obj["QtyLeft"]
      self.SetupLeft:int = obj["SetupLeft"]
      self.WIPQtyDetails:bool = obj["WIPQtyDetails"]
      """  TRUE indicates there are WIP Qty Details available (i.e. the Staged Details button should be enabled)  """  
      self.Machines:int = obj["Machines"]
      """  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  """  
      self.CanRequest:bool = obj["CanRequest"]
      """  TRUE indicates the current employee is authorized to Request Material  """  
      self.CanSelect:bool = obj["CanSelect"]
      """  TRUE indicates the current employee can select this operation to work on (i.e. the Select For Work button should be enabled).  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to setup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.JobHeadPartNum:str = obj["JobHeadPartNum"]
      """  Part number of the manufactured item.  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  """  
      self.JobHeadPartDescription:str = obj["JobHeadPartDescription"]
      """  The description of the part that is to be manufactured.  """  
      self.QtyCompleted:int = obj["QtyCompleted"]
      """   For Non Subcontract operations: A summary of labor transaction detail. (LaborDtl.LaborQty). Labor entry/collection maintains this field.  Only the LaborQty for transactions that are Production labor ( LaborType = P ) and Not rework (LaborDtl.Rework = No) are included in this summary.
This quantity is used to reduce shop load when the system is configured to reduce load based on quantity completed. (JCSyst.RemoveLoad = Q)
For Subcontract Operations this field is updated by the Purchased Receipt process. The detail records are in the PartTran file.  """  
      self.OprCommentText:str = obj["OprCommentText"]
      """  Editor widget for Job operation comments.  """  
      self.AsmCommentText:str = obj["AsmCommentText"]
      """  Editor widget for Job header comments.  """  
      self.JobHeadCommentText:str = obj["JobHeadCommentText"]
      """  Editor widget for Job header comments.  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  """  
      self.RegionDescription:str = obj["RegionDescription"]
      """  "Current Work", "Available Work", or "Expected Work" as indicated by the RegionCode.  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  Uniquely identifies an OpDtl.  System assigned.  """  
      self.OpDtlDescription:str = obj["OpDtlDescription"]
      """  Description is initially created when the JobOpDtl is created.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum to be shipped to the subcontract. Default the JobHead.PartNum or JobAsmbl.PartNum depending on the JobMtl.AssemblySeq.  """  
      self.OpDtlType:str = obj["OpDtlType"]
      """  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "Setup", "Production", or "Both".  """  
      self.Description:str = obj["Description"]
      """  Description used only for subcontract operations  """  
      self.SortHour:int = obj["SortHour"]
      """  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job operation comments.  """  
      self.Selected:bool = obj["Selected"]
      """  Used by the UI to allow selection of rows  """  
      self.RunQty:int = obj["RunQty"]
      """   The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0.
This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Description for PartNum  """  
      self.SchResourceList:str = obj["SchResourceList"]
      """  Delimited list of resources oper is schedueld to  """  
      self.CurQty:int = obj["CurQty"]
      """  Current Production Qty (for user reporting qty)  """  
      self.LaborQty:int = obj["LaborQty"]
      """  Qty currently being completed  """  
      self.ScrapQty:int = obj["ScrapQty"]
      """  Scrap Qty currently being entered  """  
      self.DiscrepQty:int = obj["DiscrepQty"]
      """  Discrep Qty currently being entered  """  
      self.DiscrepRsnCode:str = obj["DiscrepRsnCode"]
      """  Reason code for discrep qty currently being entered  """  
      self.ScrapRsnCode:str = obj["ScrapRsnCode"]
      """  Reason code for scrap currently being entered  """  
      self.ScrapRsnDesc:str = obj["ScrapRsnDesc"]
      """  Description for ScrapRsnCode  """  
      self.DiscrepRsnDesc:str = obj["DiscrepRsnDesc"]
      """  Description for DescrepRsnCode  """  
      self.Complete:bool = obj["Complete"]
      """  Operation complete  """  
      self.ResourceID:str = obj["ResourceID"]
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  """  
      self.FirstCustNum:int = obj["FirstCustNum"]
      """  CustNum from first order  """  
      self.FirstCustID:str = obj["FirstCustID"]
      self.FirstCustName:str = obj["FirstCustName"]
      self.FirstShipViaCode:str = obj["FirstShipViaCode"]
      self.FirstShipViaDesc:str = obj["FirstShipViaDesc"]
      self.SetupGrpDesc:str = obj["SetupGrpDesc"]
      self.SetupGroup:str = obj["SetupGroup"]
      """  Used to group operation to save on setups.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RequestMove:bool = obj["RequestMove"]
      """  RequestMove  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      self.SetupOrProd:str = obj["SetupOrProd"]
      self.StartDateNullCheck:bool = obj["StartDateNullCheck"]
      """  Used to checks if the StartDate has a value or is null to later permit a Sorting of the records By the StartDate field , positioning the null values at the end.  """  
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.CheckBox05:bool = obj["CheckBox05"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.Date01:str = obj["Date01"]
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.PageNum:int = obj["PageNum"]
      """  Used for caching pagination in UI  """  
      self.TotalRecords:int = obj["TotalRecords"]
      """  Used for caching pagination in UI  """  
      self.MorePages:bool = obj["MorePages"]
      """  Used for caching pagination in UI  """  
      self.LaborEntryMethodDesc:str = obj["LaborEntryMethodDesc"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) , "B" - Backflush or "X" - Time and Backflush Qty.  """  
      self.EnableLaborQty:bool = obj["EnableLaborQty"]
      self.EnableScrapQty:bool = obj["EnableScrapQty"]
      self.EnableDiscrepQty:bool = obj["EnableDiscrepQty"]
      self.ResourceGrpDesc:str = obj["ResourceGrpDesc"]
      """  Resource Group Description.  """  
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      """  Operation Code Description.  """  
      self.LaborUOM:str = obj["LaborUOM"]
      """  Unit of Measure used for editable quantity fields on the WorkQueue.  """  
      self.LaborType:str = obj["LaborType"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   jobNum
   assemblySeq
   oprSeq
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.oprSeq:int = obj["oprSeq"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class EndActivity_input:
   """ Required : 
   ds
   ipBaqID
   ipResourceGrpID
   ipEmpID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WorkQueueTableset] = obj["ds"]
      self.ipBaqID:str = obj["ipBaqID"]
      """  BAQ query ID to execute when returning results  """  
      self.ipResourceGrpID:str = obj["ipResourceGrpID"]
      """  Resource Group ID  """  
      self.ipEmpID:str = obj["ipEmpID"]
      """  Employee ID  """  
      pass

class EndActivity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WorkQueueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_LaborOperActionRow:
   def __init__(self, obj):
      self.ActionDesc:str = obj["ActionDesc"]
      """  Description of Action.  """  
      self.ActionSeq:int = obj["ActionSeq"]
      """  A sequence number which uniquely identifies action record within the operation set.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number which uniquely identifies the assembly record within the method.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Completed:bool = obj["Completed"]
      """  Indicates if this Action was completed.  """  
      self.CompletedBy:str = obj["CompletedBy"]
      """  The number of the employee that performed the work.  """  
      self.CompletedByName:str = obj["CompletedByName"]
      """  Name of the user ID in CompletedBy  """  
      self.CompletedOn:str = obj["CompletedOn"]
      """  Date the Action was completed.  """  
      self.JobNum:str = obj["JobNum"]
      """  JobNum  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  Used as the foreign key to the LaborDtl record.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborDtl record.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the method.  """  
      self.Required:bool = obj["Required"]
      """  Indicated if this Action must be completed before Operation can be completed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartWipOpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of item in the container.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that the part allocated to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence which may be on the next assembly sequence.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  job operation sequence number that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  The MtlSeq of the related JobMtl record.  Pertains only to  Raw Materials (TrackType = "R")  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """   Warehouse Code of the warehouse where the container of parts are currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutWhse of the workcenter that created the parts.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the parts.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the parts.  """  
      self.BinNum:str = obj["BinNum"]
      """   Warehouse Bin where the container is currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutBinNum of the workcenter that created the parts.  """  
      self.TrackType:str = obj["TrackType"]
      """   Internal flag to distiguish between tracking of issued raw material, and the actual manufactured product.
"R" - Raw Material a part which was issued to the job.
"M" - Manufactured Part. The part that is being manufactured.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group of the related operation.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation code of the related job operation.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.Quantity:int = obj["Quantity"]
      """  Part Quantity balance for a  Job/Asm/Opr at a warehouse/bin location.  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure of items in the container.  """  
      self.FromAssemblySeq:int = obj["FromAssemblySeq"]
      """  Assembly Sequence # which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  """  
      self.FromOprSeq:int = obj["FromOprSeq"]
      """  Operation Sequence # which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  """  
      self.FromResourceGrpID:str = obj["FromResourceGrpID"]
      """  Resource Group which created the parts allocated to this operation.  This only pertains to semi-finished manufactured parts (TrackType = M)  """  
      self.FromOpCode:str = obj["FromOpCode"]
      """  Operation Code which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  """  
      self.LastActivityDate:str = obj["LastActivityDate"]
      """  Last Activity Date.  """  
      self.LastActivityTime:int = obj["LastActivityTime"]
      """  Time of last activity expressed in seconds from midnight.  """  
      self.FinalOp:bool = obj["FinalOp"]
      """  Indicates if the completed (OutPut) quantity is for the final operation.  It is used as a filter in Part Tracker to find completed quantities that have not been moved off the job.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.UpdateStageQty:str = obj["UpdateStageQty"]
      """  Used in the PartWip write trigger to control update to JobMtl.QtyStagedToDate field. Only transactions which  move the material in/out of the staging area update this field.  This field will contain the transaction type that moved the material. For example; STK-MTL(issue of stock), PUR-MTL( movement of purchased material), MTL-STK( Returns to stock).  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.TrackTypeDesc:str = obj["TrackTypeDesc"]
      self.PartDescription:str = obj["PartDescription"]
      self.PageNum:int = obj["PageNum"]
      """  Used for caching pagination in UI  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtWorkQueueTableset:
   def __init__(self, obj):
      self.WorkQueue:list[Erp_Tablesets_WorkQueueRow] = obj["WorkQueue"]
      self.LaborOperAction:list[Erp_Tablesets_LaborOperActionRow] = obj["LaborOperAction"]
      self.PartWipOp:list[Erp_Tablesets_PartWipOpRow] = obj["PartWipOp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WorkQueueListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JCDept:str = obj["JCDept"]
      """  The Key ID of the Home Department for this Resource Group.  This is a foreign key to the JCDept table.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence # that this Operation is associated with.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.OprQty:int = obj["OprQty"]
      """  The total operation quantity. This is a calculated field.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master Code - Links the JobOper  record with a OpMaster record.  Default is given from WrkCenter.OpCode.  Must be valid in the OpMaster file.  """  
      self.EstSetHours:int = obj["EstSetHours"]
      """  Total estimated set up hours.  Calculated as EstSetHoursPerMch * Machines.  It is set to zero if operation qty is zero.  This is maintained via the JobOper write trigger.  """  
      self.EstProdHours:int = obj["EstProdHours"]
      """   The estimated Production run hours for internal operations (JobOper.Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to  recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (JobOper.RunQty / Std).
If StdFormat = "PM" then (JobOper.RunQty / Std ) / 60.
If StdFormat = "OH" then (JobOper.RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((JobOper.RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (JobOPer.RunQty/Basis) X Std.
If StdFormat = "MP" then ((JobOper.RunQty/Basis) X Std) / 60.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  """  
      self.SchedCode:str = obj["SchedCode"]
      """  Scheduling Code.  SchedCode references a record in the SchedPri table.  """  
      self.SetupLoadHrs:int = obj["SetupLoadHrs"]
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  """  
      self.ProdLoadHrs:int = obj["ProdLoadHrs"]
      self.RegionCode:int = obj["RegionCode"]
      """  1=CurrentWork, 2=AvailableWork, 3=ExpectedWork  """  
      self.OpsPerPart:int = obj["OpsPerPart"]
      """  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  """  
      self.StartDate:str = obj["StartDate"]
      """  Scheduled production start date. Not directly maintainable, updated via the scheduling process.  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  """  
      self.DueDate:str = obj["DueDate"]
      """  Scheduled production due date. Not directly maintainable, updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  """  
      self.SortDate:str = obj["SortDate"]
      self.WIPQty:int = obj["WIPQty"]
      self.CrewCount:int = obj["CrewCount"]
      """  Number Of Employees Now Working On This Operation  """  
      self.QtyLeft:int = obj["QtyLeft"]
      self.SetupLeft:int = obj["SetupLeft"]
      self.WIPQtyDetails:bool = obj["WIPQtyDetails"]
      """  TRUE indicates there are WIP Qty Details available (i.e. the Staged Details button should be enabled)  """  
      self.Machines:int = obj["Machines"]
      """  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  """  
      self.CanRequest:bool = obj["CanRequest"]
      """  TRUE indicates the current employee is authorized to Request Material  """  
      self.CanSelect:bool = obj["CanSelect"]
      """  TRUE indicates the current employee can select this operation to work on (i.e. the Select For Work button should be enabled).  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to setup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.JobHeadPartNum:str = obj["JobHeadPartNum"]
      """  Part number of the manufactured item.  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  """  
      self.JobHeadPartDescription:str = obj["JobHeadPartDescription"]
      """  The description of the part that is to be manufactured.  """  
      self.OprCommentText:str = obj["OprCommentText"]
      """  Editor widget for Job operation comments.  """  
      self.AsmCommentText:str = obj["AsmCommentText"]
      """  Editor widget for Job header comments.  """  
      self.JobHeadCommentText:str = obj["JobHeadCommentText"]
      """  Editor widget for Job header comments.  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  """  
      self.RegionDescription:str = obj["RegionDescription"]
      """  "Current Work", "Available Work", or "Expected Work" as indicated by the RegionCode.  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  Uniquely identifies an OpDtl.  System assigned.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum to be shipped to the subcontract. Default the JobHead.PartNum or JobAsmbl.PartNum depending on the JobMtl.AssemblySeq.  """  
      self.OpDtlDescription:str = obj["OpDtlDescription"]
      """  Description is initially created when the JobOpDtl is created.  """  
      self.OpDtlType:str = obj["OpDtlType"]
      """  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "Setup", "Production", or "Both".  """  
      self.Description:str = obj["Description"]
      """  Description used only for subcontract operations  """  
      self.SortHour:int = obj["SortHour"]
      """  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job operation comments.  """  
      self.Selected:bool = obj["Selected"]
      """  Used by the UI to allow selection of rows  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Description for PartNum  """  
      self.RunQty:int = obj["RunQty"]
      """   The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0.
This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  """  
      self.SchResourceList:str = obj["SchResourceList"]
      """  Delimited list of resources oper is schedueld to  """  
      self.CurQty:int = obj["CurQty"]
      """  Current Production Qty (for user reporting qty)  """  
      self.LaborQty:int = obj["LaborQty"]
      """  Qty currently being completed  """  
      self.ScrapQty:int = obj["ScrapQty"]
      """  Scrap Qty currently being entered  """  
      self.DiscrepQty:int = obj["DiscrepQty"]
      """  Discrep Qty currently being entered  """  
      self.DiscrepRsnCode:str = obj["DiscrepRsnCode"]
      """  Reason code for discrep qty currently being entered  """  
      self.ScrapRsnCode:str = obj["ScrapRsnCode"]
      """  Reason code for scrap currently being entered  """  
      self.ScrapRsnDesc:str = obj["ScrapRsnDesc"]
      """  Description for ScrapRsnCode  """  
      self.DiscrepRsnDesc:str = obj["DiscrepRsnDesc"]
      """  Description for DescrepRsnCode  """  
      self.Complete:bool = obj["Complete"]
      """  Operation complete  """  
      self.ResourceID:str = obj["ResourceID"]
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  """  
      self.FirstCustNum:int = obj["FirstCustNum"]
      """  CustNum from first order  """  
      self.FirstCustID:str = obj["FirstCustID"]
      self.FirstCustName:str = obj["FirstCustName"]
      self.FirstShipViaCode:str = obj["FirstShipViaCode"]
      self.FirstShipViaDesc:str = obj["FirstShipViaDesc"]
      self.SetupGrpDesc:str = obj["SetupGrpDesc"]
      self.SetupGroup:str = obj["SetupGroup"]
      """  Used to group operation to save on setups.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.Date01:str = obj["Date01"]
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WorkQueueListTableset:
   def __init__(self, obj):
      self.WorkQueueList:list[Erp_Tablesets_WorkQueueListRow] = obj["WorkQueueList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WorkQueueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JCDept:str = obj["JCDept"]
      """  The Key ID of the Home Department for this Resource Group.  This is a foreign key to the JCDept table.  """  
      self.OpComplete:bool = obj["OpComplete"]
      """   Indicates if this operation is completed. This is normally set to complete via labor entry transactions.   Not maintainable by Job Entry. It can't be reset to "No" if the JobHead.Complete = Yes.
Labor entry setting logic is: If SetUpComplete = Yes and  EstProdHours = 0 or ProdComplete = Yes and EstSetHours = 0 or both ProdComplete = Yes and SetupComplete = Yes  then OpComplete = Yes.
This field is also set by PO receipt entry "issue complete" for subcontract operations.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence # that this Operation is associated with.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.OprQty:int = obj["OprQty"]
      """  The total operation quantity. This is a calculated field.  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master Code - Links the JobOper  record with a OpMaster record.  Default is given from WrkCenter.OpCode.  Must be valid in the OpMaster file.  """  
      self.EstSetHours:int = obj["EstSetHours"]
      """  Total estimated set up hours.  Calculated as EstSetHoursPerMch * Machines.  It is set to zero if operation qty is zero.  This is maintained via the JobOper write trigger.  """  
      self.EstProdHours:int = obj["EstProdHours"]
      """   The estimated Production run hours for internal operations (JobOper.Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to  recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (JobOper.RunQty / Std).
If StdFormat = "PM" then (JobOper.RunQty / Std ) / 60.
If StdFormat = "OH" then (JobOper.RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((JobOper.RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (JobOPer.RunQty/Basis) X Std.
If StdFormat = "MP" then ((JobOper.RunQty/Basis) X Std) / 60.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  """  
      self.SchedCode:str = obj["SchedCode"]
      """  Scheduling Code.  SchedCode references a record in the SchedPri table.  """  
      self.SetupLoadHrs:int = obj["SetupLoadHrs"]
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  """  
      self.ProdLoadHrs:int = obj["ProdLoadHrs"]
      self.OpsPerPart:int = obj["OpsPerPart"]
      """  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  """  
      self.RegionCode:int = obj["RegionCode"]
      """  1=CurrentWork, 2=AvailableWork, 3=ExpectedWork  """  
      self.StartDate:str = obj["StartDate"]
      """  Scheduled production start date. Not directly maintainable, updated via the scheduling process.  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  """  
      self.DueDate:str = obj["DueDate"]
      """  Scheduled production due date. Not directly maintainable, updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  """  
      self.SortDate:str = obj["SortDate"]
      self.WIPQty:int = obj["WIPQty"]
      self.CrewCount:int = obj["CrewCount"]
      """  Number Of Employees Now Working On This Operation  """  
      self.QtyLeft:int = obj["QtyLeft"]
      self.SetupLeft:int = obj["SetupLeft"]
      self.WIPQtyDetails:bool = obj["WIPQtyDetails"]
      """  TRUE indicates there are WIP Qty Details available (i.e. the Staged Details button should be enabled)  """  
      self.Machines:int = obj["Machines"]
      """  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  """  
      self.CanRequest:bool = obj["CanRequest"]
      """  TRUE indicates the current employee is authorized to Request Material  """  
      self.CanSelect:bool = obj["CanSelect"]
      """  TRUE indicates the current employee can select this operation to work on (i.e. the Select For Work button should be enabled).  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to setup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.JobHeadPartNum:str = obj["JobHeadPartNum"]
      """  Part number of the manufactured item.  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  """  
      self.JobHeadPartDescription:str = obj["JobHeadPartDescription"]
      """  The description of the part that is to be manufactured.  """  
      self.QtyCompleted:int = obj["QtyCompleted"]
      """   For Non Subcontract operations: A summary of labor transaction detail. (LaborDtl.LaborQty). Labor entry/collection maintains this field.  Only the LaborQty for transactions that are Production labor ( LaborType = P ) and Not rework (LaborDtl.Rework = No) are included in this summary.
This quantity is used to reduce shop load when the system is configured to reduce load based on quantity completed. (JCSyst.RemoveLoad = Q)
For Subcontract Operations this field is updated by the Purchased Receipt process. The detail records are in the PartTran file.  """  
      self.OprCommentText:str = obj["OprCommentText"]
      """  Editor widget for Job operation comments.  """  
      self.AsmCommentText:str = obj["AsmCommentText"]
      """  Editor widget for Job header comments.  """  
      self.JobHeadCommentText:str = obj["JobHeadCommentText"]
      """  Editor widget for Job header comments.  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  """  
      self.RegionDescription:str = obj["RegionDescription"]
      """  "Current Work", "Available Work", or "Expected Work" as indicated by the RegionCode.  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  Uniquely identifies an OpDtl.  System assigned.  """  
      self.OpDtlDescription:str = obj["OpDtlDescription"]
      """  Description is initially created when the JobOpDtl is created.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum to be shipped to the subcontract. Default the JobHead.PartNum or JobAsmbl.PartNum depending on the JobMtl.AssemblySeq.  """  
      self.OpDtlType:str = obj["OpDtlType"]
      """  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "Setup", "Production", or "Both".  """  
      self.Description:str = obj["Description"]
      """  Description used only for subcontract operations  """  
      self.SortHour:int = obj["SortHour"]
      """  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job operation comments.  """  
      self.Selected:bool = obj["Selected"]
      """  Used by the UI to allow selection of rows  """  
      self.RunQty:int = obj["RunQty"]
      """   The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0.
This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Description for PartNum  """  
      self.SchResourceList:str = obj["SchResourceList"]
      """  Delimited list of resources oper is schedueld to  """  
      self.CurQty:int = obj["CurQty"]
      """  Current Production Qty (for user reporting qty)  """  
      self.LaborQty:int = obj["LaborQty"]
      """  Qty currently being completed  """  
      self.ScrapQty:int = obj["ScrapQty"]
      """  Scrap Qty currently being entered  """  
      self.DiscrepQty:int = obj["DiscrepQty"]
      """  Discrep Qty currently being entered  """  
      self.DiscrepRsnCode:str = obj["DiscrepRsnCode"]
      """  Reason code for discrep qty currently being entered  """  
      self.ScrapRsnCode:str = obj["ScrapRsnCode"]
      """  Reason code for scrap currently being entered  """  
      self.ScrapRsnDesc:str = obj["ScrapRsnDesc"]
      """  Description for ScrapRsnCode  """  
      self.DiscrepRsnDesc:str = obj["DiscrepRsnDesc"]
      """  Description for DescrepRsnCode  """  
      self.Complete:bool = obj["Complete"]
      """  Operation complete  """  
      self.ResourceID:str = obj["ResourceID"]
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  """  
      self.FirstCustNum:int = obj["FirstCustNum"]
      """  CustNum from first order  """  
      self.FirstCustID:str = obj["FirstCustID"]
      self.FirstCustName:str = obj["FirstCustName"]
      self.FirstShipViaCode:str = obj["FirstShipViaCode"]
      self.FirstShipViaDesc:str = obj["FirstShipViaDesc"]
      self.SetupGrpDesc:str = obj["SetupGrpDesc"]
      self.SetupGroup:str = obj["SetupGroup"]
      """  Used to group operation to save on setups.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RequestMove:bool = obj["RequestMove"]
      """  RequestMove  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      self.SetupOrProd:str = obj["SetupOrProd"]
      self.StartDateNullCheck:bool = obj["StartDateNullCheck"]
      """  Used to checks if the StartDate has a value or is null to later permit a Sorting of the records By the StartDate field , positioning the null values at the end.  """  
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.CheckBox05:bool = obj["CheckBox05"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.Date01:str = obj["Date01"]
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.PageNum:int = obj["PageNum"]
      """  Used for caching pagination in UI  """  
      self.TotalRecords:int = obj["TotalRecords"]
      """  Used for caching pagination in UI  """  
      self.MorePages:bool = obj["MorePages"]
      """  Used for caching pagination in UI  """  
      self.LaborEntryMethodDesc:str = obj["LaborEntryMethodDesc"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) , "B" - Backflush or "X" - Time and Backflush Qty.  """  
      self.EnableLaborQty:bool = obj["EnableLaborQty"]
      self.EnableScrapQty:bool = obj["EnableScrapQty"]
      self.EnableDiscrepQty:bool = obj["EnableDiscrepQty"]
      self.ResourceGrpDesc:str = obj["ResourceGrpDesc"]
      """  Resource Group Description.  """  
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      """  Operation Code Description.  """  
      self.LaborUOM:str = obj["LaborUOM"]
      """  Unit of Measure used for editable quantity fields on the WorkQueue.  """  
      self.LaborType:str = obj["LaborType"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WorkQueueTableset:
   def __init__(self, obj):
      self.WorkQueue:list[Erp_Tablesets_WorkQueueRow] = obj["WorkQueue"]
      self.LaborOperAction:list[Erp_Tablesets_LaborOperActionRow] = obj["LaborOperAction"]
      self.PartWipOp:list[Erp_Tablesets_PartWipOpRow] = obj["PartWipOp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   jobNum
   assemblySeq
   oprSeq
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.oprSeq:int = obj["oprSeq"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WorkQueueTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_WorkQueueTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_WorkQueueTableset] = obj["returnObj"]
      pass

class GetLaborOperActionDS_input:
   """ Required : 
   ds
   jobNum
   assySeq
   oprSeq
   empNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WorkQueueTableset] = obj["ds"]
      self.jobNum:str = obj["jobNum"]
      """  The employee Code of the current employee.  """  
      self.assySeq:int = obj["assySeq"]
      """  The employee Code of the current employee.  """  
      self.oprSeq:int = obj["oprSeq"]
      """  The employee Code of the current employee.  """  
      self.empNum:str = obj["empNum"]
      """  The employee Code of the current employee.  """  
      pass

class GetLaborOperActionDS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WorkQueueTableset] = obj["ds"]
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
      self.returnObj:list[Erp_Tablesets_WorkQueueListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPartWipOp_input:
   """ Required : 
   ds
   plant
   partNum
   jobNum
   assemblySeq
   oprSeq
   wareHouseCode
   binNum
   lotNum
   dimCode
   trackType
   mtlSeq
   attributeSetID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WorkQueueTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      self.partNum:str = obj["partNum"]
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      self.oprSeq:int = obj["oprSeq"]
      self.wareHouseCode:str = obj["wareHouseCode"]
      self.binNum:str = obj["binNum"]
      self.lotNum:str = obj["lotNum"]
      self.dimCode:str = obj["dimCode"]
      self.trackType:str = obj["trackType"]
      self.mtlSeq:int = obj["mtlSeq"]
      self.attributeSetID:int = obj["attributeSetID"]
      pass

class GetNewPartWipOp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WorkQueueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewWorkQueue_input:
   """ Required : 
   ds
   jobNum
   assemblySeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WorkQueueTableset] = obj["ds"]
      self.jobNum:str = obj["jobNum"]
      self.assemblySeq:int = obj["assemblySeq"]
      pass

class GetNewWorkQueue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WorkQueueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetOpsInResourceGroupWithBaq_input:
   """ Required : 
   ipBaqID
   ipResourceGrpID
   ipEmpID
   ipLaborType
   ipStartDate
   ipJobNum
   ipAssemblySeq
   ipOpCode
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ipBaqID:str = obj["ipBaqID"]
      """  BAQ Query ID  """  
      self.ipResourceGrpID:str = obj["ipResourceGrpID"]
      """  Resource Group ID  """  
      self.ipEmpID:str = obj["ipEmpID"]
      """  Employee ID  """  
      self.ipLaborType:str = obj["ipLaborType"]
      """  Labor Type  """  
      self.ipStartDate:str = obj["ipStartDate"]
      """  Start Date to cut off from  """  
      self.ipJobNum:str = obj["ipJobNum"]
      """  Job, empty will exclude from filter  """  
      self.ipAssemblySeq:str = obj["ipAssemblySeq"]
      """  Assembly Seq, empty will exclude from filter  """  
      self.ipOpCode:str = obj["ipOpCode"]
      """  Operation Code, empty will exclude from filter  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetOpsInResourceGroupWithBaq_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WorkQueueTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      self.opTotalWorkQueueRecords:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetOpsInResourceGroup_input:
   """ Required : 
   pcResourceGrpID
   pcEmpID
   pageSize
   absolutePage
   LaborType
   clearCache
   filterParameters
   """  
   def __init__(self, obj):
      self.pcResourceGrpID:str = obj["pcResourceGrpID"]
      """  The Code of the Resource Group for which the operations should be retrieved.  """  
      self.pcEmpID:str = obj["pcEmpID"]
      """  The employee Code of the current employee.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      self.LaborType:str = obj["LaborType"]
      """  Labor Type  """  
      self.clearCache:bool = obj["clearCache"]
      """  Clear CACHE: true/false  """  
      self.filterParameters:str = obj["filterParameters"]
      """  Concatenated string of filters, Start Date in ISO Format YYYYMMDD, Job Number, Assembly Seq and Operation Description. Ex '20151231~2031~0~DEBUR'  """  
      pass

class GetOpsInResourceGroup_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WorkQueueTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      self.totalWorkQueueRecords:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseWorkQueue
   whereClauseLaborOperAction
   whereClausePartWipOp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseWorkQueue:str = obj["whereClauseWorkQueue"]
      self.whereClauseLaborOperAction:str = obj["whereClauseLaborOperAction"]
      self.whereClausePartWipOp:str = obj["whereClausePartWipOp"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WorkQueueTableset] = obj["returnObj"]
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

class RefreshSelectedRecords_input:
   """ Required : 
   ds
   ipBaqID
   ipResourceGrpID
   ipEmpID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WorkQueueTableset] = obj["ds"]
      self.ipBaqID:str = obj["ipBaqID"]
      """  BAQ query ID to execute when returning results  """  
      self.ipResourceGrpID:str = obj["ipResourceGrpID"]
      """  Resource Group ID  """  
      self.ipEmpID:str = obj["ipEmpID"]
      """  Employee ID  """  
      pass

class RefreshSelectedRecords_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WorkQueueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtWorkQueueTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtWorkQueueTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WorkQueueTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WorkQueueTableset] = obj["ds"]
      pass

      """  output parameters  """  

