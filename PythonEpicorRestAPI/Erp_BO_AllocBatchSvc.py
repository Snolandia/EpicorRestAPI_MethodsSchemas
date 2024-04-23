import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.AllocBatchSvc
# Description: Allocation Batch Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_AllocBatches(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AllocBatches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AllocBatches
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcBatchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/AllocBatches",headers=creds) as resp:
           return await resp.json()

async def post_AllocBatches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AllocBatches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcBatchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcBatchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/AllocBatches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AllocBatches_Company_BatchID(Company, BatchID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AllocBatch item
   Description: Calls GetByID to retrieve the AllocBatch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AllocBatch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcBatchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/AllocBatches(" + Company + "," + BatchID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AllocBatches_Company_BatchID(Company, BatchID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AllocBatch for the service
   Description: Calls UpdateExt to update AllocBatch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AllocBatch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcBatchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/AllocBatches(" + Company + "," + BatchID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AllocBatches_Company_BatchID(Company, BatchID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AllocBatch item
   Description: Call UpdateExt to delete AllocBatch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AllocBatch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/AllocBatches(" + Company + "," + BatchID + ")",headers=creds) as resp:
           return await resp.json()

async def get_AllocBatches_Company_BatchID_AlcBatchCDs(Company, BatchID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AlcBatchCDs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcBatchCDs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcBatchCDRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/AllocBatches(" + Company + "," + BatchID + ")/AlcBatchCDs",headers=creds) as resp:
           return await resp.json()

async def get_AllocBatches_Company_BatchID_AlcBatchCDs_Company_BatchID_AllocID(Company, BatchID, AllocID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcBatchCD item
   Description: Calls GetByID to retrieve the AlcBatchCD item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcBatchCD1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcBatchCDRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/AllocBatches(" + Company + "," + BatchID + ")/AlcBatchCDs(" + Company + "," + BatchID + "," + AllocID + ")",headers=creds) as resp:
           return await resp.json()

async def get_AllocBatches_Company_BatchID_AlcBatchScheds(Company, BatchID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AlcBatchScheds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcBatchScheds1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcBatchSchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/AllocBatches(" + Company + "," + BatchID + ")/AlcBatchScheds",headers=creds) as resp:
           return await resp.json()

async def get_AllocBatches_Company_BatchID_AlcBatchScheds_Company_BatchID_SchedNum(Company, BatchID, SchedNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcBatchSched item
   Description: Calls GetByID to retrieve the AlcBatchSched item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcBatchSched1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param SchedNum: Desc: SchedNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcBatchSchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/AllocBatches(" + Company + "," + BatchID + ")/AlcBatchScheds(" + Company + "," + BatchID + "," + SchedNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcBatchCDs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlcBatchCDs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcBatchCDs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcBatchCDRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/AlcBatchCDs",headers=creds) as resp:
           return await resp.json()

async def post_AlcBatchCDs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcBatchCDs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcBatchCDRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcBatchCDRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/AlcBatchCDs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlcBatchCDs_Company_BatchID_AllocID(Company, BatchID, AllocID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcBatchCD item
   Description: Calls GetByID to retrieve the AlcBatchCD item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcBatchCD
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcBatchCDRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/AlcBatchCDs(" + Company + "," + BatchID + "," + AllocID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlcBatchCDs_Company_BatchID_AllocID(Company, BatchID, AllocID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlcBatchCD for the service
   Description: Calls UpdateExt to update AlcBatchCD. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcBatchCD
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcBatchCDRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/AlcBatchCDs(" + Company + "," + BatchID + "," + AllocID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlcBatchCDs_Company_BatchID_AllocID(Company, BatchID, AllocID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlcBatchCD item
   Description: Call UpdateExt to delete AlcBatchCD item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcBatchCD
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/AlcBatchCDs(" + Company + "," + BatchID + "," + AllocID + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcBatchScheds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlcBatchScheds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcBatchScheds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcBatchSchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/AlcBatchScheds",headers=creds) as resp:
           return await resp.json()

async def post_AlcBatchScheds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcBatchScheds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcBatchSchedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcBatchSchedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/AlcBatchScheds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlcBatchScheds_Company_BatchID_SchedNum(Company, BatchID, SchedNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcBatchSched item
   Description: Calls GetByID to retrieve the AlcBatchSched item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcBatchSched
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param SchedNum: Desc: SchedNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcBatchSchedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/AlcBatchScheds(" + Company + "," + BatchID + "," + SchedNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlcBatchScheds_Company_BatchID_SchedNum(Company, BatchID, SchedNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlcBatchSched for the service
   Description: Calls UpdateExt to update AlcBatchSched. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcBatchSched
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param SchedNum: Desc: SchedNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcBatchSchedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/AlcBatchScheds(" + Company + "," + BatchID + "," + SchedNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlcBatchScheds_Company_BatchID_SchedNum(Company, BatchID, SchedNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlcBatchSched item
   Description: Call UpdateExt to delete AlcBatchSched item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcBatchSched
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param SchedNum: Desc: SchedNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/AlcBatchScheds(" + Company + "," + BatchID + "," + SchedNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcBatchListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseAlcBatch, whereClauseAlcBatchCD, whereClauseAlcBatchSched, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseAlcBatch=" + whereClauseAlcBatch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlcBatchCD=" + whereClauseAlcBatchCD
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlcBatchSched=" + whereClauseAlcBatchSched
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(batchID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "batchID=" + batchID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_DeleteSchedule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteSchedule
   Description: This method deletes AlcBatchSched records given a fiscal year.
   OperationID: DeleteSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateSchedule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateSchedule
   Description: This method creates AlcBatchSched records given a fiscal year.
   OperationID: GenerateSchedule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateSchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateSchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAlcBatchSchedDel(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAlcBatchSchedDel
   Description: This method returns the AlcBatchSchedGen dataset.
   OperationID: GetAlcBatchSchedDel
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAlcBatchSchedDel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAlcBatchSchedDel_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAlcBatchSchedGen(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAlcBatchSchedGen
   Description: This method returns the AlcBatchSchedGen dataset.
   OperationID: GetAlcBatchSchedGen
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAlcBatchSchedGen_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAlcBatchSchedGen_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAllocID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAllocID
   Description: Method to call when changing the AlcBatchCD.AllocID field.
   OperationID: OnChangeAllocID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAllocID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAllocID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeApplyDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeApplyDate
   Description: Method to call when changing the AlcBatchSched.ApplyDate field.
   OperationID: OnChangeApplyDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBookID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBookID
   Description: Method to call when changing the AlcBatch.BookID field.
   OperationID: OnChangeBookID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBookID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBookID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeReverse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeReverse
   Description: Purpose:  Null out reverse apply date for every unallocated schedule
Parameters:
<param name="ipBatchID">Allocation Batch ID to schedule all periods</param><param name="ipReverseFlag">reverse flag</param>
Notes:
   OperationID: OnChangeReverse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeReverse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeReverse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSchedDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSchedDate
   Description: Method to call when changing the AlcBatchSched.SchedDate field.
   OperationID: OnChangeSchedDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSchedDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSchedDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeScheduled(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeScheduled
   Description: Method to call when changing the AlcBatchSched.scheduled field.
   OperationID: OnChangeScheduled
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeScheduled_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeScheduled_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeStatus
   Description: Method to call when changing the AlcBatchSched.SchedDate field.
   OperationID: OnChangeStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ScheduleAllPeriods(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ScheduleAllPeriods
   Description: Purpose:  Schedule all periods that have not been allocated
Parameters:
<param name="ipBatchID">Allocation Batch ID to schedule all periods</param>
Notes:
   OperationID: ScheduleAllPeriods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ScheduleAllPeriods_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ScheduleAllPeriods_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcBatch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcBatch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcBatch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcBatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcBatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcBatchCD(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcBatchCD
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcBatchCD
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcBatchCD_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcBatchCD_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcBatchSched(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcBatchSched
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcBatchSched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcBatchSched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcBatchSched_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AllocBatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcBatchCDRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcBatchCDRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcBatchListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcBatchListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcBatchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcBatchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcBatchSchedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcBatchSchedRow] = obj["value"]
      pass

class Erp_Tablesets_AlcBatchCDRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.Tier:int = obj["Tier"]
      """  Allocation tier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllocTypeDesc:str = obj["AllocTypeDesc"]
      self.BookID:str = obj["BookID"]
      self.BitFlag:int = obj["BitFlag"]
      self.AlcHedDescription:str = obj["AlcHedDescription"]
      self.AlcHedAllocationType:int = obj["AlcHedAllocationType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcBatchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates whether or not reversing transactions are generated at the time a journal entry is allocated.  Yes indicates reversing entries are generated.  No indicates reversing entries are not generated.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Unique identifier of the journal used to group entries. This is the journal code used during allocation processing.  """  
      self.Cycle:bool = obj["Cycle"]
      """  Indicates if the allocation batch is allocated in a cyclical manner until a specific threshold.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FiscalCalendar:str = obj["FiscalCalendar"]
      """  Fiscal Calendar  """  
      self.ProcessRunning:bool = obj["ProcessRunning"]
      self.FiscalCalDesc:str = obj["FiscalCalDesc"]
      self.GLBookFiscalCalendarID:str = obj["GLBookFiscalCalendarID"]
      """  Identifier for the Fiscal Calendar assigned to the book  """  
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.GLBookDescription:str = obj["GLBookDescription"]
      """  Descripiton of Book  """  
      self.JrnlCodeJrnlDescription:str = obj["JrnlCodeJrnlDescription"]
      """  Journal  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcBatchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates whether or not reversing transactions are generated at the time a journal entry is allocated.  Yes indicates reversing entries are generated.  No indicates reversing entries are not generated.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Unique identifier of the journal used to group entries. This is the journal code used during allocation processing.  """  
      self.Cycle:bool = obj["Cycle"]
      """  Indicates if the allocation batch is allocated in a cyclical manner until a specific threshold.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FiscalCalendar:str = obj["FiscalCalendar"]
      """  Fiscal Calendar  """  
      self.ProcessRunning:bool = obj["ProcessRunning"]
      self.FiscalCalDesc:str = obj["FiscalCalDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookFiscalCalendarID:str = obj["GLBookFiscalCalendarID"]
      self.JrnlCodeJrnlDescription:str = obj["JrnlCodeJrnlDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcBatchSchedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.SchedNum:int = obj["SchedNum"]
      """  Internal next number used to keep the schedule records unique.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date  """  
      self.ApplyDateRev:str = obj["ApplyDateRev"]
      """  Reverse Apply Date  """  
      self.SchedDate:str = obj["SchedDate"]
      """  Date when the allocation batch is due to be run.  """  
      self.AllocStatus:int = obj["AllocStatus"]
      """  Indicates the status of the batch schedule.  """  
      self.LastSchedDate:str = obj["LastSchedDate"]
      """  Last date this schedule was allocated.  If null the schedule has not yet been allcoated.  If not null it identifies to the 'Run Allocations' procdess that the allocation was previously run.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  CloseFiscalPeriod  """  
      self.AllocStatusDesc:str = obj["AllocStatusDesc"]
      self.Scheduled:bool = obj["Scheduled"]
      """  External field used to set the allocation status to 'scheduled'.  The end-user is only permitted to set the status to 'scheduled' or 'not scheduled'.  The 'allocated' and 'reversed' status are used by the allocations engine.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.FiscalCalendarDescription:str = obj["FiscalCalendarDescription"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   batchID
   """  
   def __init__(self, obj):
      self.batchID:str = obj["batchID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteSchedule_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcBatchSchedGenTableset] = obj["ds"]
      pass

class DeleteSchedule_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AllocBatchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcBatchSchedGenTableset] = obj["ds"]
      self.cOutMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_AlcBatchCDRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.Tier:int = obj["Tier"]
      """  Allocation tier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllocTypeDesc:str = obj["AllocTypeDesc"]
      self.BookID:str = obj["BookID"]
      self.BitFlag:int = obj["BitFlag"]
      self.AlcHedDescription:str = obj["AlcHedDescription"]
      self.AlcHedAllocationType:int = obj["AlcHedAllocationType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcBatchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates whether or not reversing transactions are generated at the time a journal entry is allocated.  Yes indicates reversing entries are generated.  No indicates reversing entries are not generated.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Unique identifier of the journal used to group entries. This is the journal code used during allocation processing.  """  
      self.Cycle:bool = obj["Cycle"]
      """  Indicates if the allocation batch is allocated in a cyclical manner until a specific threshold.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FiscalCalendar:str = obj["FiscalCalendar"]
      """  Fiscal Calendar  """  
      self.ProcessRunning:bool = obj["ProcessRunning"]
      self.FiscalCalDesc:str = obj["FiscalCalDesc"]
      self.GLBookFiscalCalendarID:str = obj["GLBookFiscalCalendarID"]
      """  Identifier for the Fiscal Calendar assigned to the book  """  
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.GLBookDescription:str = obj["GLBookDescription"]
      """  Descripiton of Book  """  
      self.JrnlCodeJrnlDescription:str = obj["JrnlCodeJrnlDescription"]
      """  Journal  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcBatchListTableset:
   def __init__(self, obj):
      self.AlcBatchList:list[Erp_Tablesets_AlcBatchListRow] = obj["AlcBatchList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_AlcBatchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates whether or not reversing transactions are generated at the time a journal entry is allocated.  Yes indicates reversing entries are generated.  No indicates reversing entries are not generated.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Unique identifier of the journal used to group entries. This is the journal code used during allocation processing.  """  
      self.Cycle:bool = obj["Cycle"]
      """  Indicates if the allocation batch is allocated in a cyclical manner until a specific threshold.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FiscalCalendar:str = obj["FiscalCalendar"]
      """  Fiscal Calendar  """  
      self.ProcessRunning:bool = obj["ProcessRunning"]
      self.FiscalCalDesc:str = obj["FiscalCalDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookFiscalCalendarID:str = obj["GLBookFiscalCalendarID"]
      self.JrnlCodeJrnlDescription:str = obj["JrnlCodeJrnlDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcBatchSchedGenRow:
   def __init__(self, obj):
      self.BatchID:str = obj["BatchID"]
      self.BookID:str = obj["BookID"]
      self.CalendarDescription:str = obj["CalendarDescription"]
      self.Company:str = obj["Company"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.Reverse:bool = obj["Reverse"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcBatchSchedGenTableset:
   def __init__(self, obj):
      self.AlcBatchSchedGen:list[Erp_Tablesets_AlcBatchSchedGenRow] = obj["AlcBatchSchedGen"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_AlcBatchSchedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.SchedNum:int = obj["SchedNum"]
      """  Internal next number used to keep the schedule records unique.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date  """  
      self.ApplyDateRev:str = obj["ApplyDateRev"]
      """  Reverse Apply Date  """  
      self.SchedDate:str = obj["SchedDate"]
      """  Date when the allocation batch is due to be run.  """  
      self.AllocStatus:int = obj["AllocStatus"]
      """  Indicates the status of the batch schedule.  """  
      self.LastSchedDate:str = obj["LastSchedDate"]
      """  Last date this schedule was allocated.  If null the schedule has not yet been allcoated.  If not null it identifies to the 'Run Allocations' procdess that the allocation was previously run.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  CloseFiscalPeriod  """  
      self.AllocStatusDesc:str = obj["AllocStatusDesc"]
      self.Scheduled:bool = obj["Scheduled"]
      """  External field used to set the allocation status to 'scheduled'.  The end-user is only permitted to set the status to 'scheduled' or 'not scheduled'.  The 'allocated' and 'reversed' status are used by the allocations engine.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.FiscalCalendarDescription:str = obj["FiscalCalendarDescription"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AllocBatchTableset:
   def __init__(self, obj):
      self.AlcBatch:list[Erp_Tablesets_AlcBatchRow] = obj["AlcBatch"]
      self.AlcBatchCD:list[Erp_Tablesets_AlcBatchCDRow] = obj["AlcBatchCD"]
      self.AlcBatchSched:list[Erp_Tablesets_AlcBatchSchedRow] = obj["AlcBatchSched"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtAllocBatchTableset:
   def __init__(self, obj):
      self.AlcBatch:list[Erp_Tablesets_AlcBatchRow] = obj["AlcBatch"]
      self.AlcBatchCD:list[Erp_Tablesets_AlcBatchCDRow] = obj["AlcBatchCD"]
      self.AlcBatchSched:list[Erp_Tablesets_AlcBatchSchedRow] = obj["AlcBatchSched"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenerateSchedule_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcBatchSchedGenTableset] = obj["ds"]
      pass

class GenerateSchedule_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AllocBatchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcBatchSchedGenTableset] = obj["ds"]
      self.cOutMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetAlcBatchSchedDel_input:
   """ Required : 
   inBatchID
   """  
   def __init__(self, obj):
      self.inBatchID:str = obj["inBatchID"]
      """  The AlcBatch BatchID  """  
      pass

class GetAlcBatchSchedDel_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AlcBatchSchedGenTableset] = obj["returnObj"]
      pass

class GetAlcBatchSchedGen_input:
   """ Required : 
   inBatchID
   """  
   def __init__(self, obj):
      self.inBatchID:str = obj["inBatchID"]
      """  The AlcBatch BatchID  """  
      pass

class GetAlcBatchSchedGen_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AlcBatchSchedGenTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   batchID
   """  
   def __init__(self, obj):
      self.batchID:str = obj["batchID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AllocBatchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AllocBatchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AllocBatchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AlcBatchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewAlcBatchCD_input:
   """ Required : 
   ds
   batchID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AllocBatchTableset] = obj["ds"]
      self.batchID:str = obj["batchID"]
      pass

class GetNewAlcBatchCD_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AllocBatchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcBatchSched_input:
   """ Required : 
   ds
   batchID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AllocBatchTableset] = obj["ds"]
      self.batchID:str = obj["batchID"]
      pass

class GetNewAlcBatchSched_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AllocBatchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcBatch_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AllocBatchTableset] = obj["ds"]
      pass

class GetNewAlcBatch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AllocBatchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseAlcBatch
   whereClauseAlcBatchCD
   whereClauseAlcBatchSched
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAlcBatch:str = obj["whereClauseAlcBatch"]
      self.whereClauseAlcBatchCD:str = obj["whereClauseAlcBatchCD"]
      self.whereClauseAlcBatchSched:str = obj["whereClauseAlcBatchSched"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AllocBatchTableset] = obj["returnObj"]
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

class OnChangeAllocID_input:
   """ Required : 
   proposedAllocID
   ds
   """  
   def __init__(self, obj):
      self.proposedAllocID:str = obj["proposedAllocID"]
      """  The proposed Allocation ID  """  
      self.ds:list[Erp_Tablesets_AllocBatchTableset] = obj["ds"]
      pass

class OnChangeAllocID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AllocBatchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeApplyDate_input:
   """ Required : 
   proposedApplyDate
   ds
   """  
   def __init__(self, obj):
      self.proposedApplyDate:str = obj["proposedApplyDate"]
      """  Proposed Apply Date  """  
      self.ds:list[Erp_Tablesets_AllocBatchTableset] = obj["ds"]
      pass

class OnChangeApplyDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AllocBatchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBookID_input:
   """ Required : 
   proposedBookID
   ds
   """  
   def __init__(self, obj):
      self.proposedBookID:str = obj["proposedBookID"]
      """  The proposed book  """  
      self.ds:list[Erp_Tablesets_AllocBatchTableset] = obj["ds"]
      pass

class OnChangeBookID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AllocBatchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeReverse_input:
   """ Required : 
   ipBatchID
   ipReverseFlag
   """  
   def __init__(self, obj):
      self.ipBatchID:str = obj["ipBatchID"]
      self.ipReverseFlag:bool = obj["ipReverseFlag"]
      pass

class OnChangeReverse_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AllocBatchTableset] = obj["returnObj"]
      pass

class OnChangeSchedDate_input:
   """ Required : 
   proposedApplyDate
   ds
   """  
   def __init__(self, obj):
      self.proposedApplyDate:str = obj["proposedApplyDate"]
      """  Proposed Schedule Date  """  
      self.ds:list[Erp_Tablesets_AllocBatchTableset] = obj["ds"]
      pass

class OnChangeSchedDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AllocBatchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeScheduled_input:
   """ Required : 
   ipScheduled
   ds
   """  
   def __init__(self, obj):
      self.ipScheduled:bool = obj["ipScheduled"]
      """  Proposed Scheduled  """  
      self.ds:list[Erp_Tablesets_AllocBatchTableset] = obj["ds"]
      pass

class OnChangeScheduled_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AllocBatchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeStatus_input:
   """ Required : 
   proposedStatus
   """  
   def __init__(self, obj):
      self.proposedStatus:int = obj["proposedStatus"]
      """  Proposed Schedule Date  """  
      pass

class OnChangeStatus_output:
   def __init__(self, obj):
      pass

class ScheduleAllPeriods_input:
   """ Required : 
   ipBatchID
   """  
   def __init__(self, obj):
      self.ipBatchID:str = obj["ipBatchID"]
      pass

class ScheduleAllPeriods_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AllocBatchTableset] = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAllocBatchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAllocBatchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AllocBatchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AllocBatchTableset] = obj["ds"]
      pass

      """  output parameters  """  

