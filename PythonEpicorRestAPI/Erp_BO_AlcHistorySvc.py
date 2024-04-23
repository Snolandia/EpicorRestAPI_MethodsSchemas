import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.AlcHistorySvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistories(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlcHistories items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHistories
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories",headers=creds) as resp:
           return await resp.json()

async def post_AlcHistories(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHistories
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHistRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHistRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlcHistories_Company_BatchID_RunNbr_AllocID(Company, BatchID, RunNbr, AllocID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcHistory item
   Description: Calls GetByID to retrieve the AlcHistory item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistory
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlcHistories_Company_BatchID_RunNbr_AllocID(Company, BatchID, RunNbr, AllocID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlcHistory for the service
   Description: Calls UpdateExt to update AlcHistory. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHistory
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHistRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlcHistories_Company_BatchID_RunNbr_AllocID(Company, BatchID, RunNbr, AllocID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlcHistory item
   Description: Call UpdateExt to delete AlcHistory item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHistory
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistories_Company_BatchID_RunNbr_AllocID_AHGLJrnDtls(Company, BatchID, RunNbr, AllocID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AHGLJrnDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AHGLJrnDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AHGLJrnDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AHGLJrnDtls",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistories_Company_BatchID_RunNbr_AllocID_AHGLJrnDtls_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_Reverse(Company, BatchID, RunNbr, AllocID, AllocTgtNbr, AllocTgtSeq, Reverse, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AHGLJrnDtl item
   Description: Calls GetByID to retrieve the AHGLJrnDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AHGLJrnDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocTgtNbr: Desc: AllocTgtNbr   Required: True
      :param AllocTgtSeq: Desc: AllocTgtSeq   Required: True
      :param Reverse: Desc: Reverse   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AHGLJrnDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AHGLJrnDtls(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + Reverse + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistories_Company_BatchID_RunNbr_AllocID_AHGLJrnDtlSims(Company, BatchID, RunNbr, AllocID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AHGLJrnDtlSims items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AHGLJrnDtlSims1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AHGLJrnDtlSimRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AHGLJrnDtlSims",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistories_Company_BatchID_RunNbr_AllocID_AHGLJrnDtlSims_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_Reverse(Company, BatchID, RunNbr, AllocID, AllocTgtNbr, AllocTgtSeq, Reverse, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AHGLJrnDtlSim item
   Description: Calls GetByID to retrieve the AHGLJrnDtlSim item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AHGLJrnDtlSim1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocTgtNbr: Desc: AllocTgtNbr   Required: True
      :param AllocTgtSeq: Desc: AllocTgtSeq   Required: True
      :param Reverse: Desc: Reverse   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AHGLJrnDtlSimRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AHGLJrnDtlSims(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + Reverse + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistAccts(Company, BatchID, RunNbr, AllocID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AlcHistAccts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcHistAccts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistAccts",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistAccts_Company_BatchID_RunNbr_AllocID_ParamNbr_AllocGLAcct(Company, BatchID, RunNbr, AllocID, ParamNbr, AllocGLAcct, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcHistAcct item
   Description: Calls GetByID to retrieve the AlcHistAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistAcct1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param AllocGLAcct: Desc: AllocGLAcct   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistAccts(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistActCats(Company, BatchID, RunNbr, AllocID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AlcHistActCats items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcHistActCats1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistActCatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistActCats",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistActCats_Company_BatchID_RunNbr_AllocID_ParamNbr_CategoryID(Company, BatchID, RunNbr, AllocID, ParamNbr, CategoryID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcHistActCat item
   Description: Calls GetByID to retrieve the AlcHistActCat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistActCat1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param CategoryID: Desc: CategoryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistActCatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistActCats(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistDtls(Company, BatchID, RunNbr, AllocID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AlcHistDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcHistDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistDtls",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistDtls_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq(Company, BatchID, RunNbr, AllocID, AllocTgtNbr, AllocTgtSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcHistDtl item
   Description: Calls GetByID to retrieve the AlcHistDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocTgtNbr: Desc: AllocTgtNbr   Required: True
      :param AllocTgtSeq: Desc: AllocTgtSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistDtls(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistJrnCds(Company, BatchID, RunNbr, AllocID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AlcHistJrnCds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcHistJrnCds1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistJrnCdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistJrnCds",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistJrnCds_Company_BatchID_RunNbr_AllocID_ParamNbr_JournalCode(Company, BatchID, RunNbr, AllocID, ParamNbr, JournalCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcHistJrnCd item
   Description: Calls GetByID to retrieve the AlcHistJrnCd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistJrnCd1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistJrnCdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistJrnCds(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistParams(Company, BatchID, RunNbr, AllocID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AlcHistParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcHistParams1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistParamsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistParams",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr(Company, BatchID, RunNbr, AllocID, ParamNbr, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcHistParam item
   Description: Calls GetByID to retrieve the AlcHistParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistParam1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistParamsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistRanges(Company, BatchID, RunNbr, AllocID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AlcHistRanges items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcHistRanges1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistRangeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistRanges",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistories_Company_BatchID_RunNbr_AllocID_AlcHistRanges_Company_BatchID_RunNbr_AllocID_ParamNbr_SegmentNbr(Company, BatchID, RunNbr, AllocID, ParamNbr, SegmentNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcHistRange item
   Description: Calls GetByID to retrieve the AlcHistRange item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistRange1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistRangeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistories(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + ")/AlcHistRanges(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_AHGLJrnDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AHGLJrnDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AHGLJrnDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AHGLJrnDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AHGLJrnDtls",headers=creds) as resp:
           return await resp.json()

async def post_AHGLJrnDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AHGLJrnDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AHGLJrnDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AHGLJrnDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AHGLJrnDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AHGLJrnDtls_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_Reverse(Company, BatchID, RunNbr, AllocID, AllocTgtNbr, AllocTgtSeq, Reverse, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AHGLJrnDtl item
   Description: Calls GetByID to retrieve the AHGLJrnDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AHGLJrnDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocTgtNbr: Desc: AllocTgtNbr   Required: True
      :param AllocTgtSeq: Desc: AllocTgtSeq   Required: True
      :param Reverse: Desc: Reverse   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AHGLJrnDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AHGLJrnDtls(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + Reverse + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AHGLJrnDtls_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_Reverse(Company, BatchID, RunNbr, AllocID, AllocTgtNbr, AllocTgtSeq, Reverse, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AHGLJrnDtl for the service
   Description: Calls UpdateExt to update AHGLJrnDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AHGLJrnDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocTgtNbr: Desc: AllocTgtNbr   Required: True
      :param AllocTgtSeq: Desc: AllocTgtSeq   Required: True
      :param Reverse: Desc: Reverse   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AHGLJrnDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AHGLJrnDtls(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + Reverse + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AHGLJrnDtls_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_Reverse(Company, BatchID, RunNbr, AllocID, AllocTgtNbr, AllocTgtSeq, Reverse, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AHGLJrnDtl item
   Description: Call UpdateExt to delete AHGLJrnDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AHGLJrnDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocTgtNbr: Desc: AllocTgtNbr   Required: True
      :param AllocTgtSeq: Desc: AllocTgtSeq   Required: True
      :param Reverse: Desc: Reverse   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AHGLJrnDtls(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + Reverse + ")",headers=creds) as resp:
           return await resp.json()

async def get_AHGLJrnDtlSims(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AHGLJrnDtlSims items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AHGLJrnDtlSims
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AHGLJrnDtlSimRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AHGLJrnDtlSims",headers=creds) as resp:
           return await resp.json()

async def post_AHGLJrnDtlSims(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AHGLJrnDtlSims
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AHGLJrnDtlSimRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AHGLJrnDtlSimRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AHGLJrnDtlSims", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AHGLJrnDtlSims_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_Reverse(Company, BatchID, RunNbr, AllocID, AllocTgtNbr, AllocTgtSeq, Reverse, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AHGLJrnDtlSim item
   Description: Calls GetByID to retrieve the AHGLJrnDtlSim item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AHGLJrnDtlSim
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocTgtNbr: Desc: AllocTgtNbr   Required: True
      :param AllocTgtSeq: Desc: AllocTgtSeq   Required: True
      :param Reverse: Desc: Reverse   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AHGLJrnDtlSimRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AHGLJrnDtlSims(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + Reverse + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AHGLJrnDtlSims_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_Reverse(Company, BatchID, RunNbr, AllocID, AllocTgtNbr, AllocTgtSeq, Reverse, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AHGLJrnDtlSim for the service
   Description: Calls UpdateExt to update AHGLJrnDtlSim. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AHGLJrnDtlSim
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocTgtNbr: Desc: AllocTgtNbr   Required: True
      :param AllocTgtSeq: Desc: AllocTgtSeq   Required: True
      :param Reverse: Desc: Reverse   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AHGLJrnDtlSimRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AHGLJrnDtlSims(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + Reverse + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AHGLJrnDtlSims_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_Reverse(Company, BatchID, RunNbr, AllocID, AllocTgtNbr, AllocTgtSeq, Reverse, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AHGLJrnDtlSim item
   Description: Call UpdateExt to delete AHGLJrnDtlSim item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AHGLJrnDtlSim
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocTgtNbr: Desc: AllocTgtNbr   Required: True
      :param AllocTgtSeq: Desc: AllocTgtSeq   Required: True
      :param Reverse: Desc: Reverse   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AHGLJrnDtlSims(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + Reverse + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistAccts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlcHistAccts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHistAccts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistAccts",headers=creds) as resp:
           return await resp.json()

async def post_AlcHistAccts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHistAccts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHistAcctRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHistAcctRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistAccts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlcHistAccts_Company_BatchID_RunNbr_AllocID_ParamNbr_AllocGLAcct(Company, BatchID, RunNbr, AllocID, ParamNbr, AllocGLAcct, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcHistAcct item
   Description: Calls GetByID to retrieve the AlcHistAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param AllocGLAcct: Desc: AllocGLAcct   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistAccts(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlcHistAccts_Company_BatchID_RunNbr_AllocID_ParamNbr_AllocGLAcct(Company, BatchID, RunNbr, AllocID, ParamNbr, AllocGLAcct, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlcHistAcct for the service
   Description: Calls UpdateExt to update AlcHistAcct. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHistAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param AllocGLAcct: Desc: AllocGLAcct   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHistAcctRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistAccts(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlcHistAccts_Company_BatchID_RunNbr_AllocID_ParamNbr_AllocGLAcct(Company, BatchID, RunNbr, AllocID, ParamNbr, AllocGLAcct, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlcHistAcct item
   Description: Call UpdateExt to delete AlcHistAcct item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHistAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param AllocGLAcct: Desc: AllocGLAcct   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistAccts(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistActCats(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlcHistActCats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHistActCats
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistActCatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistActCats",headers=creds) as resp:
           return await resp.json()

async def post_AlcHistActCats(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHistActCats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHistActCatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHistActCatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistActCats", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlcHistActCats_Company_BatchID_RunNbr_AllocID_ParamNbr_CategoryID(Company, BatchID, RunNbr, AllocID, ParamNbr, CategoryID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcHistActCat item
   Description: Calls GetByID to retrieve the AlcHistActCat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistActCat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param CategoryID: Desc: CategoryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistActCatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistActCats(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlcHistActCats_Company_BatchID_RunNbr_AllocID_ParamNbr_CategoryID(Company, BatchID, RunNbr, AllocID, ParamNbr, CategoryID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlcHistActCat for the service
   Description: Calls UpdateExt to update AlcHistActCat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHistActCat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param CategoryID: Desc: CategoryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHistActCatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistActCats(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlcHistActCats_Company_BatchID_RunNbr_AllocID_ParamNbr_CategoryID(Company, BatchID, RunNbr, AllocID, ParamNbr, CategoryID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlcHistActCat item
   Description: Call UpdateExt to delete AlcHistActCat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHistActCat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param CategoryID: Desc: CategoryID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistActCats(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlcHistDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHistDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistDtls",headers=creds) as resp:
           return await resp.json()

async def post_AlcHistDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHistDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHistDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHistDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlcHistDtls_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq(Company, BatchID, RunNbr, AllocID, AllocTgtNbr, AllocTgtSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcHistDtl item
   Description: Calls GetByID to retrieve the AlcHistDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocTgtNbr: Desc: AllocTgtNbr   Required: True
      :param AllocTgtSeq: Desc: AllocTgtSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistDtls(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlcHistDtls_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq(Company, BatchID, RunNbr, AllocID, AllocTgtNbr, AllocTgtSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlcHistDtl for the service
   Description: Calls UpdateExt to update AlcHistDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHistDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocTgtNbr: Desc: AllocTgtNbr   Required: True
      :param AllocTgtSeq: Desc: AllocTgtSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHistDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistDtls(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlcHistDtls_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq(Company, BatchID, RunNbr, AllocID, AllocTgtNbr, AllocTgtSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlcHistDtl item
   Description: Call UpdateExt to delete AlcHistDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHistDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocTgtNbr: Desc: AllocTgtNbr   Required: True
      :param AllocTgtSeq: Desc: AllocTgtSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistDtls(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistJrnCds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlcHistJrnCds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHistJrnCds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistJrnCdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistJrnCds",headers=creds) as resp:
           return await resp.json()

async def post_AlcHistJrnCds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHistJrnCds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHistJrnCdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHistJrnCdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistJrnCds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlcHistJrnCds_Company_BatchID_RunNbr_AllocID_ParamNbr_JournalCode(Company, BatchID, RunNbr, AllocID, ParamNbr, JournalCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcHistJrnCd item
   Description: Calls GetByID to retrieve the AlcHistJrnCd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistJrnCd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistJrnCdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistJrnCds(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlcHistJrnCds_Company_BatchID_RunNbr_AllocID_ParamNbr_JournalCode(Company, BatchID, RunNbr, AllocID, ParamNbr, JournalCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlcHistJrnCd for the service
   Description: Calls UpdateExt to update AlcHistJrnCd. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHistJrnCd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHistJrnCdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistJrnCds(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlcHistJrnCds_Company_BatchID_RunNbr_AllocID_ParamNbr_JournalCode(Company, BatchID, RunNbr, AllocID, ParamNbr, JournalCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlcHistJrnCd item
   Description: Call UpdateExt to delete AlcHistJrnCd item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHistJrnCd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistJrnCds(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistParams(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlcHistParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHistParams
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistParamsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams",headers=creds) as resp:
           return await resp.json()

async def post_AlcHistParams(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHistParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHistParamsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHistParamsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr(Company, BatchID, RunNbr, AllocID, ParamNbr, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcHistParam item
   Description: Calls GetByID to retrieve the AlcHistParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistParamsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr(Company, BatchID, RunNbr, AllocID, ParamNbr, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlcHistParam for the service
   Description: Calls UpdateExt to update AlcHistParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHistParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHistParamsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr(Company, BatchID, RunNbr, AllocID, ParamNbr, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlcHistParam item
   Description: Call UpdateExt to delete AlcHistParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHistParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_AlcHistParamsBAQs(Company, BatchID, RunNbr, AllocID, ParamNbr, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AlcHistParamsBAQs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcHistParamsBAQs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistParamsBAQRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/AlcHistParamsBAQs",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_AlcHistParamsBAQs_Company_BatchID_RunNbr_AllocID_ParamNbr_BAQExportID_BAQParamValNbr(Company, BatchID, RunNbr, AllocID, ParamNbr, BAQExportID, BAQParamValNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcHistParamsBAQ item
   Description: Calls GetByID to retrieve the AlcHistParamsBAQ item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistParamsBAQ1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param BAQExportID: Desc: BAQExportID   Required: True   Allow empty value : True
      :param BAQParamValNbr: Desc: BAQParamValNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistParamsBAQRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/AlcHistParamsBAQs(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + BAQExportID + "," + BAQParamValNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_AlcHistNFSrcs(Company, BatchID, RunNbr, AllocID, ParamNbr, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AlcHistNFSrcs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlcHistNFSrcs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistNFSrcRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/AlcHistNFSrcs",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_AlcHistNFSrcs_Company_BatchID_RunNbr_AllocID_ParamNbr_SrcSeqNbr(Company, BatchID, RunNbr, AllocID, ParamNbr, SrcSeqNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcHistNFSrc item
   Description: Calls GetByID to retrieve the AlcHistNFSrc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistNFSrc1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param SrcSeqNbr: Desc: SrcSeqNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistNFSrcRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/AlcHistNFSrcs(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SrcSeqNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_PAlcHistAccts(Company, BatchID, RunNbr, AllocID, ParamNbr, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PAlcHistAccts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PAlcHistAccts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PAlcHistAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/PAlcHistAccts",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_PAlcHistAccts_Company_BatchID_RunNbr_AllocID_ParamNbr_AllocGLAcct(Company, BatchID, RunNbr, AllocID, ParamNbr, AllocGLAcct, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PAlcHistAcct item
   Description: Calls GetByID to retrieve the PAlcHistAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PAlcHistAcct1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param AllocGLAcct: Desc: AllocGLAcct   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PAlcHistAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/PAlcHistAccts(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_PAlcHistActCats(Company, BatchID, RunNbr, AllocID, ParamNbr, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PAlcHistActCats items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PAlcHistActCats1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PAlcHistActCatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/PAlcHistActCats",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_PAlcHistActCats_Company_BatchID_RunNbr_AllocID_ParamNbr_CategoryID(Company, BatchID, RunNbr, AllocID, ParamNbr, CategoryID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PAlcHistActCat item
   Description: Calls GetByID to retrieve the PAlcHistActCat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PAlcHistActCat1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param CategoryID: Desc: CategoryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PAlcHistActCatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/PAlcHistActCats(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_PAlcHistJrnCds(Company, BatchID, RunNbr, AllocID, ParamNbr, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PAlcHistJrnCds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PAlcHistJrnCds1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PAlcHistJrnCdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/PAlcHistJrnCds",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_PAlcHistJrnCds_Company_BatchID_RunNbr_AllocID_ParamNbr_JournalCode(Company, BatchID, RunNbr, AllocID, ParamNbr, JournalCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PAlcHistJrnCd item
   Description: Calls GetByID to retrieve the PAlcHistJrnCd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PAlcHistJrnCd1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PAlcHistJrnCdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/PAlcHistJrnCds(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_PAlcHistRanges(Company, BatchID, RunNbr, AllocID, ParamNbr, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PAlcHistRanges items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PAlcHistRanges1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PAlcHistRangeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/PAlcHistRanges",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistParams_Company_BatchID_RunNbr_AllocID_ParamNbr_PAlcHistRanges_Company_BatchID_RunNbr_AllocID_ParamNbr_SegmentNbr(Company, BatchID, RunNbr, AllocID, ParamNbr, SegmentNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PAlcHistRange item
   Description: Calls GetByID to retrieve the PAlcHistRange item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PAlcHistRange1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PAlcHistRangeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + ")/PAlcHistRanges(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistParamsBAQs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlcHistParamsBAQs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHistParamsBAQs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistParamsBAQRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParamsBAQs",headers=creds) as resp:
           return await resp.json()

async def post_AlcHistParamsBAQs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHistParamsBAQs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHistParamsBAQRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHistParamsBAQRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParamsBAQs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlcHistParamsBAQs_Company_BatchID_RunNbr_AllocID_ParamNbr_BAQExportID_BAQParamValNbr(Company, BatchID, RunNbr, AllocID, ParamNbr, BAQExportID, BAQParamValNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcHistParamsBAQ item
   Description: Calls GetByID to retrieve the AlcHistParamsBAQ item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistParamsBAQ
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param BAQExportID: Desc: BAQExportID   Required: True   Allow empty value : True
      :param BAQParamValNbr: Desc: BAQParamValNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistParamsBAQRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParamsBAQs(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + BAQExportID + "," + BAQParamValNbr + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlcHistParamsBAQs_Company_BatchID_RunNbr_AllocID_ParamNbr_BAQExportID_BAQParamValNbr(Company, BatchID, RunNbr, AllocID, ParamNbr, BAQExportID, BAQParamValNbr, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlcHistParamsBAQ for the service
   Description: Calls UpdateExt to update AlcHistParamsBAQ. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHistParamsBAQ
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param BAQExportID: Desc: BAQExportID   Required: True   Allow empty value : True
      :param BAQParamValNbr: Desc: BAQParamValNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHistParamsBAQRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParamsBAQs(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + BAQExportID + "," + BAQParamValNbr + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlcHistParamsBAQs_Company_BatchID_RunNbr_AllocID_ParamNbr_BAQExportID_BAQParamValNbr(Company, BatchID, RunNbr, AllocID, ParamNbr, BAQExportID, BAQParamValNbr, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlcHistParamsBAQ item
   Description: Call UpdateExt to delete AlcHistParamsBAQ item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHistParamsBAQ
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param BAQExportID: Desc: BAQExportID   Required: True   Allow empty value : True
      :param BAQParamValNbr: Desc: BAQParamValNbr   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistParamsBAQs(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + BAQExportID + "," + BAQParamValNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistNFSrcs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlcHistNFSrcs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHistNFSrcs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistNFSrcRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistNFSrcs",headers=creds) as resp:
           return await resp.json()

async def post_AlcHistNFSrcs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHistNFSrcs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHistNFSrcRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHistNFSrcRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistNFSrcs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlcHistNFSrcs_Company_BatchID_RunNbr_AllocID_ParamNbr_SrcSeqNbr(Company, BatchID, RunNbr, AllocID, ParamNbr, SrcSeqNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcHistNFSrc item
   Description: Calls GetByID to retrieve the AlcHistNFSrc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistNFSrc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param SrcSeqNbr: Desc: SrcSeqNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistNFSrcRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistNFSrcs(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SrcSeqNbr + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlcHistNFSrcs_Company_BatchID_RunNbr_AllocID_ParamNbr_SrcSeqNbr(Company, BatchID, RunNbr, AllocID, ParamNbr, SrcSeqNbr, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlcHistNFSrc for the service
   Description: Calls UpdateExt to update AlcHistNFSrc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHistNFSrc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param SrcSeqNbr: Desc: SrcSeqNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHistNFSrcRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistNFSrcs(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SrcSeqNbr + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlcHistNFSrcs_Company_BatchID_RunNbr_AllocID_ParamNbr_SrcSeqNbr(Company, BatchID, RunNbr, AllocID, ParamNbr, SrcSeqNbr, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlcHistNFSrc item
   Description: Call UpdateExt to delete AlcHistNFSrc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHistNFSrc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param SrcSeqNbr: Desc: SrcSeqNbr   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistNFSrcs(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SrcSeqNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_PAlcHistAccts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PAlcHistAccts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PAlcHistAccts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PAlcHistAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistAccts",headers=creds) as resp:
           return await resp.json()

async def post_PAlcHistAccts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PAlcHistAccts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PAlcHistAcctRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PAlcHistAcctRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistAccts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PAlcHistAccts_Company_BatchID_RunNbr_AllocID_ParamNbr_AllocGLAcct(Company, BatchID, RunNbr, AllocID, ParamNbr, AllocGLAcct, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PAlcHistAcct item
   Description: Calls GetByID to retrieve the PAlcHistAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PAlcHistAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param AllocGLAcct: Desc: AllocGLAcct   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PAlcHistAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistAccts(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PAlcHistAccts_Company_BatchID_RunNbr_AllocID_ParamNbr_AllocGLAcct(Company, BatchID, RunNbr, AllocID, ParamNbr, AllocGLAcct, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PAlcHistAcct for the service
   Description: Calls UpdateExt to update PAlcHistAcct. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PAlcHistAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param AllocGLAcct: Desc: AllocGLAcct   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PAlcHistAcctRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistAccts(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PAlcHistAccts_Company_BatchID_RunNbr_AllocID_ParamNbr_AllocGLAcct(Company, BatchID, RunNbr, AllocID, ParamNbr, AllocGLAcct, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PAlcHistAcct item
   Description: Call UpdateExt to delete PAlcHistAcct item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PAlcHistAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param AllocGLAcct: Desc: AllocGLAcct   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistAccts(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + AllocGLAcct + ")",headers=creds) as resp:
           return await resp.json()

async def get_PAlcHistActCats(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PAlcHistActCats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PAlcHistActCats
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PAlcHistActCatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistActCats",headers=creds) as resp:
           return await resp.json()

async def post_PAlcHistActCats(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PAlcHistActCats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PAlcHistActCatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PAlcHistActCatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistActCats", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PAlcHistActCats_Company_BatchID_RunNbr_AllocID_ParamNbr_CategoryID(Company, BatchID, RunNbr, AllocID, ParamNbr, CategoryID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PAlcHistActCat item
   Description: Calls GetByID to retrieve the PAlcHistActCat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PAlcHistActCat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param CategoryID: Desc: CategoryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PAlcHistActCatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistActCats(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PAlcHistActCats_Company_BatchID_RunNbr_AllocID_ParamNbr_CategoryID(Company, BatchID, RunNbr, AllocID, ParamNbr, CategoryID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PAlcHistActCat for the service
   Description: Calls UpdateExt to update PAlcHistActCat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PAlcHistActCat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param CategoryID: Desc: CategoryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PAlcHistActCatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistActCats(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PAlcHistActCats_Company_BatchID_RunNbr_AllocID_ParamNbr_CategoryID(Company, BatchID, RunNbr, AllocID, ParamNbr, CategoryID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PAlcHistActCat item
   Description: Call UpdateExt to delete PAlcHistActCat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PAlcHistActCat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param CategoryID: Desc: CategoryID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistActCats(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + CategoryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PAlcHistJrnCds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PAlcHistJrnCds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PAlcHistJrnCds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PAlcHistJrnCdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistJrnCds",headers=creds) as resp:
           return await resp.json()

async def post_PAlcHistJrnCds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PAlcHistJrnCds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PAlcHistJrnCdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PAlcHistJrnCdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistJrnCds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PAlcHistJrnCds_Company_BatchID_RunNbr_AllocID_ParamNbr_JournalCode(Company, BatchID, RunNbr, AllocID, ParamNbr, JournalCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PAlcHistJrnCd item
   Description: Calls GetByID to retrieve the PAlcHistJrnCd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PAlcHistJrnCd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PAlcHistJrnCdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistJrnCds(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PAlcHistJrnCds_Company_BatchID_RunNbr_AllocID_ParamNbr_JournalCode(Company, BatchID, RunNbr, AllocID, ParamNbr, JournalCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PAlcHistJrnCd for the service
   Description: Calls UpdateExt to update PAlcHistJrnCd. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PAlcHistJrnCd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PAlcHistJrnCdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistJrnCds(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PAlcHistJrnCds_Company_BatchID_RunNbr_AllocID_ParamNbr_JournalCode(Company, BatchID, RunNbr, AllocID, ParamNbr, JournalCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PAlcHistJrnCd item
   Description: Call UpdateExt to delete PAlcHistJrnCd item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PAlcHistJrnCd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistJrnCds(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + JournalCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_PAlcHistRanges(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PAlcHistRanges items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PAlcHistRanges
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PAlcHistRangeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistRanges",headers=creds) as resp:
           return await resp.json()

async def post_PAlcHistRanges(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PAlcHistRanges
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PAlcHistRangeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PAlcHistRangeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistRanges", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PAlcHistRanges_Company_BatchID_RunNbr_AllocID_ParamNbr_SegmentNbr(Company, BatchID, RunNbr, AllocID, ParamNbr, SegmentNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PAlcHistRange item
   Description: Calls GetByID to retrieve the PAlcHistRange item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PAlcHistRange
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PAlcHistRangeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistRanges(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PAlcHistRanges_Company_BatchID_RunNbr_AllocID_ParamNbr_SegmentNbr(Company, BatchID, RunNbr, AllocID, ParamNbr, SegmentNbr, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PAlcHistRange for the service
   Description: Calls UpdateExt to update PAlcHistRange. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PAlcHistRange
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PAlcHistRangeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistRanges(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PAlcHistRanges_Company_BatchID_RunNbr_AllocID_ParamNbr_SegmentNbr(Company, BatchID, RunNbr, AllocID, ParamNbr, SegmentNbr, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PAlcHistRange item
   Description: Call UpdateExt to delete PAlcHistRange item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PAlcHistRange
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/PAlcHistRanges(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistRanges(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlcHistRanges items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHistRanges
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistRangeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistRanges",headers=creds) as resp:
           return await resp.json()

async def post_AlcHistRanges(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHistRanges
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHistRangeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHistRangeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistRanges", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlcHistRanges_Company_BatchID_RunNbr_AllocID_ParamNbr_SegmentNbr(Company, BatchID, RunNbr, AllocID, ParamNbr, SegmentNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcHistRange item
   Description: Calls GetByID to retrieve the AlcHistRange item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistRange
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistRangeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistRanges(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlcHistRanges_Company_BatchID_RunNbr_AllocID_ParamNbr_SegmentNbr(Company, BatchID, RunNbr, AllocID, ParamNbr, SegmentNbr, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlcHistRange for the service
   Description: Calls UpdateExt to update AlcHistRange. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHistRange
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHistRangeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistRanges(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlcHistRanges_Company_BatchID_RunNbr_AllocID_ParamNbr_SegmentNbr(Company, BatchID, RunNbr, AllocID, ParamNbr, SegmentNbr, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlcHistRange item
   Description: Call UpdateExt to delete AlcHistRange item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHistRange
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistRanges(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + ParamNbr + "," + SegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistResParams(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlcHistResParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHistResParams
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistResParamsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistResParams",headers=creds) as resp:
           return await resp.json()

async def post_AlcHistResParams(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHistResParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHistResParamsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHistResParamsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistResParams", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlcHistResParams_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_ParamNbr(Company, BatchID, RunNbr, AllocID, AllocTgtNbr, AllocTgtSeq, ParamNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcHistResParam item
   Description: Calls GetByID to retrieve the AlcHistResParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistResParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocTgtNbr: Desc: AllocTgtNbr   Required: True
      :param AllocTgtSeq: Desc: AllocTgtSeq   Required: True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistResParamsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistResParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + ParamNbr + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlcHistResParams_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_ParamNbr(Company, BatchID, RunNbr, AllocID, AllocTgtNbr, AllocTgtSeq, ParamNbr, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlcHistResParam for the service
   Description: Calls UpdateExt to update AlcHistResParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHistResParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocTgtNbr: Desc: AllocTgtNbr   Required: True
      :param AllocTgtSeq: Desc: AllocTgtSeq   Required: True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHistResParamsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistResParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + ParamNbr + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlcHistResParams_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_ParamNbr(Company, BatchID, RunNbr, AllocID, AllocTgtNbr, AllocTgtSeq, ParamNbr, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlcHistResParam item
   Description: Call UpdateExt to delete AlcHistResParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHistResParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocTgtNbr: Desc: AllocTgtNbr   Required: True
      :param AllocTgtSeq: Desc: AllocTgtSeq   Required: True
      :param ParamNbr: Desc: ParamNbr   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistResParams(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + ParamNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlcHistResParamsSims(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlcHistResParamsSims items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlcHistResParamsSims
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistResParamsSimRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistResParamsSims",headers=creds) as resp:
           return await resp.json()

async def post_AlcHistResParamsSims(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlcHistResParamsSims
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlcHistResParamsSimRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlcHistResParamsSimRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistResParamsSims", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlcHistResParamsSims_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_ParamNbr(Company, BatchID, RunNbr, AllocID, AllocTgtNbr, AllocTgtSeq, ParamNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlcHistResParamsSim item
   Description: Calls GetByID to retrieve the AlcHistResParamsSim item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlcHistResParamsSim
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocTgtNbr: Desc: AllocTgtNbr   Required: True
      :param AllocTgtSeq: Desc: AllocTgtSeq   Required: True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlcHistResParamsSimRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistResParamsSims(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + ParamNbr + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlcHistResParamsSims_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_ParamNbr(Company, BatchID, RunNbr, AllocID, AllocTgtNbr, AllocTgtSeq, ParamNbr, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlcHistResParamsSim for the service
   Description: Calls UpdateExt to update AlcHistResParamsSim. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlcHistResParamsSim
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocTgtNbr: Desc: AllocTgtNbr   Required: True
      :param AllocTgtSeq: Desc: AllocTgtSeq   Required: True
      :param ParamNbr: Desc: ParamNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlcHistResParamsSimRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistResParamsSims(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + ParamNbr + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlcHistResParamsSims_Company_BatchID_RunNbr_AllocID_AllocTgtNbr_AllocTgtSeq_ParamNbr(Company, BatchID, RunNbr, AllocID, AllocTgtNbr, AllocTgtSeq, ParamNbr, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlcHistResParamsSim item
   Description: Call UpdateExt to delete AlcHistResParamsSim item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlcHistResParamsSim
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BatchID: Desc: BatchID   Required: True   Allow empty value : True
      :param RunNbr: Desc: RunNbr   Required: True
      :param AllocID: Desc: AllocID   Required: True   Allow empty value : True
      :param AllocTgtNbr: Desc: AllocTgtNbr   Required: True
      :param AllocTgtSeq: Desc: AllocTgtSeq   Required: True
      :param ParamNbr: Desc: ParamNbr   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/AlcHistResParamsSims(" + Company + "," + BatchID + "," + RunNbr + "," + AllocID + "," + AllocTgtNbr + "," + AllocTgtSeq + "," + ParamNbr + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlcHistListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseAlcHist, whereClauseAHGLJrnDtl, whereClauseAlcHistResParams, whereClauseAHGLJrnDtlSim, whereClauseAlcHistResParamsSim, whereClauseAlcHistAcct, whereClauseAlcHistActCat, whereClauseAlcHistDtl, whereClauseAlcHistJrnCd, whereClauseAlcHistParams, whereClauseAlcHistParamsBAQ, whereClauseAlcHistNFSrc, whereClausePAlcHistAcct, whereClausePAlcHistActCat, whereClausePAlcHistJrnCd, whereClausePAlcHistRange, whereClauseAlcHistRange, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "whereClauseAlcHist=" + whereClauseAlcHist
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAHGLJrnDtl=" + whereClauseAHGLJrnDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlcHistResParams=" + whereClauseAlcHistResParams
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAHGLJrnDtlSim=" + whereClauseAHGLJrnDtlSim
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlcHistResParamsSim=" + whereClauseAlcHistResParamsSim
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlcHistAcct=" + whereClauseAlcHistAcct
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlcHistActCat=" + whereClauseAlcHistActCat
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlcHistDtl=" + whereClauseAlcHistDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlcHistJrnCd=" + whereClauseAlcHistJrnCd
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlcHistParams=" + whereClauseAlcHistParams
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlcHistParamsBAQ=" + whereClauseAlcHistParamsBAQ
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlcHistNFSrc=" + whereClauseAlcHistNFSrc
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePAlcHistAcct=" + whereClausePAlcHistAcct
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePAlcHistActCat=" + whereClausePAlcHistActCat
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePAlcHistJrnCd=" + whereClausePAlcHistJrnCd
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePAlcHistRange=" + whereClausePAlcHistRange
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlcHistRange=" + whereClauseAlcHistRange
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(batchID, runNbr, allocID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
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
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "runNbr=" + runNbr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "allocID=" + allocID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetByBatchIDRunNbr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByBatchIDRunNbr
   Description: Wrapper method for GetRows with BatchID and RunNbr filters
   OperationID: GetByBatchIDRunNbr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByBatchIDRunNbr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByBatchIDRunNbr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListByBatchID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListByBatchID
   Description: One AlcHist record for each BatchID.  Call normal GetList method.
   OperationID: GetListByBatchID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListByBatchID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListByBatchID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcHistoryFilter(epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcHistoryFilter
   Description: This method creates a new AlcHistoryFilter record.
   OperationID: GetNewAlcHistoryFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHistoryFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBookID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBookID
   Description: This method is called when the BookID is changed.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFiscalYearOrSuffix(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFiscalYearOrSuffix
   Description: Verifies selected start\end period and updates if year doesn't contain current values.
   OperationID: OnChangeFiscalYearOrSuffix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFiscalYearOrSuffix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFiscalYearOrSuffix_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcHist(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcHist
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHist_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAHGLJrnDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAHGLJrnDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAHGLJrnDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAHGLJrnDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAHGLJrnDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcHistResParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcHistResParams
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHistResParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHistResParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHistResParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAHGLJrnDtlSim(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAHGLJrnDtlSim
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAHGLJrnDtlSim
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAHGLJrnDtlSim_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAHGLJrnDtlSim_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcHistResParamsSim(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcHistResParamsSim
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHistResParamsSim
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHistResParamsSim_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHistResParamsSim_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcHistAcct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcHistAcct
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHistAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHistAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHistAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcHistActCat(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcHistActCat
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHistActCat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHistActCat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHistActCat_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcHistDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcHistDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHistDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHistDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHistDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcHistJrnCd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcHistJrnCd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHistJrnCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHistJrnCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHistJrnCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcHistParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcHistParams
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHistParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHistParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHistParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcHistParamsBAQ(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcHistParamsBAQ
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHistParamsBAQ
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHistParamsBAQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHistParamsBAQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcHistNFSrc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcHistNFSrc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHistNFSrc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHistNFSrc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHistNFSrc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPAlcHistAcct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPAlcHistAcct
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPAlcHistAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPAlcHistAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPAlcHistAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPAlcHistActCat(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPAlcHistActCat
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPAlcHistActCat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPAlcHistActCat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPAlcHistActCat_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPAlcHistJrnCd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPAlcHistJrnCd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPAlcHistJrnCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPAlcHistJrnCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPAlcHistJrnCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPAlcHistRange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPAlcHistRange
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPAlcHistRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPAlcHistRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPAlcHistRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlcHistRange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlcHistRange
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlcHistRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlcHistRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlcHistRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlcHistorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AHGLJrnDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AHGLJrnDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AHGLJrnDtlSimRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AHGLJrnDtlSimRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistAcctRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcHistAcctRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistActCatRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcHistActCatRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcHistDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistJrnCdRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcHistJrnCdRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcHistListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistNFSrcRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcHistNFSrcRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistParamsBAQRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcHistParamsBAQRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistParamsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcHistParamsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistRangeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcHistRangeRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistResParamsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcHistResParamsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistResParamsSimRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcHistResParamsSimRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlcHistRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlcHistRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistAcctRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PAlcHistAcctRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistActCatRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PAlcHistActCatRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistJrnCdRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PAlcHistJrnCdRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PAlcHistRangeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PAlcHistRangeRow] = obj["value"]
      pass

class Erp_Tablesets_AHGLJrnDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year that entry applies to.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  """  
      self.Description:str = obj["Description"]
      """  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  """  
      self.JEDate:str = obj["JEDate"]
      """  Date for this journal transaction entry.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period that this journal entry applies to.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  User ID that posted this translation.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date that this transaction was posted to the G/L files.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this entry has been posted to the G/L master balance files. Unposted entries are excluded from all G/L reports.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctId of the BankAcct master that this check was drawn  against.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number.  """  
      self.CRHeadNum:int = obj["CRHeadNum"]
      """  Cash Receipts reference field.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  """  
      self.BankTranNum:int = obj["BankTranNum"]
      """  Bank Transaction Number.  Used when a transaction is a direct transfer from one bank account to another.  """  
      self.BankSlip:str = obj["BankSlip"]
      """   The identifier of the Bank Slip document (bank statement).  The user enters a bank slip during the reconciliation process.  This is then written into the related GLJrnDtl records.
Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.ExtRefType:str = obj["ExtRefType"]
      """  Multi-Company G/L Reference Type from the external company.  This is used by the Multi-Company Journal.  """  
      self.ExtRefCode:str = obj["ExtRefCode"]
      """  Multi-Company G/L Reference Code from the external company.  This is used by the Multi-Company Journal.  """  
      self.GlbJournalNum:int = obj["GlbJournalNum"]
      """  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalLine:int = obj["GlbJournalLine"]
      """  The Journal Line assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalCode:str = obj["GlbJournalCode"]
      """  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor number.  Used by Multi-Company Journal.  """  
      self.GlbAPInvoiceNum:str = obj["GlbAPInvoiceNum"]
      """  Global AP Invoice identifier.  Used by Multi-Company Journal.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Flag to indicate that a separate journal entry will be created at the target company for the Multi-Company G/L Account entered in this journal line.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to a Multi-Company Journal.  """  
      self.CommentText:str = obj["CommentText"]
      """  Extended text to describe the journal line entry.  Defaults from GLJrnHed.CommentText.  """  
      self.GlbCompanyID:str = obj["GlbCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.GlbFiscalYear:int = obj["GlbFiscalYear"]
      """  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  """  
      self.GlbFiscalPeriod:int = obj["GlbFiscalPeriod"]
      """  Fiscal period from the external company that this journal entry applies to.  """  
      self.GlbGroupID:str = obj["GlbGroupID"]
      """  The data entry Group from the external company that the journal entry is assigned to.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.ExtGLAccount:str = obj["ExtGLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.ExtSegValue1:str = obj["ExtSegValue1"]
      """  External Segment Value 1  """  
      self.ExtSegValue2:str = obj["ExtSegValue2"]
      """  External Segment Value 2  """  
      self.ExtSegValue3:str = obj["ExtSegValue3"]
      """  External Segment Value 3  """  
      self.ExtSegValue4:str = obj["ExtSegValue4"]
      """  External Segment Value 4  """  
      self.ExtSegValue5:str = obj["ExtSegValue5"]
      """  External Segment Value 5  """  
      self.ExtSegValue6:str = obj["ExtSegValue6"]
      """  External Segment Value 6  """  
      self.ExtSegValue7:str = obj["ExtSegValue7"]
      """  External Segment Value 7  """  
      self.ExtSegValue8:str = obj["ExtSegValue8"]
      """  External Segment Value 8  """  
      self.ExtSegValue9:str = obj["ExtSegValue9"]
      """  External Segment Value 9  """  
      self.ExtSegValue10:str = obj["ExtSegValue10"]
      """  External Segment Value 10  """  
      self.ExtSegValue11:str = obj["ExtSegValue11"]
      """  External Segment Value 11  """  
      self.ExtSegValue12:str = obj["ExtSegValue12"]
      """  External Segment Value 12  """  
      self.ExtSegValue13:str = obj["ExtSegValue13"]
      """  External Segment Value 13  """  
      self.ExtSegValue14:str = obj["ExtSegValue14"]
      """  External Segment Value 14  """  
      self.ExtSegValue15:str = obj["ExtSegValue15"]
      """  External Segment Value 15  """  
      self.ExtSegValue16:str = obj["ExtSegValue16"]
      """  External Segment Value 16  """  
      self.ExtSegValue17:str = obj["ExtSegValue17"]
      """  External Segment Value 17  """  
      self.ExtSegValue18:str = obj["ExtSegValue18"]
      """  External Segment Value 18  """  
      self.ExtSegValue19:str = obj["ExtSegValue19"]
      """  External Segment Value 19  """  
      self.ExtSegValue20:str = obj["ExtSegValue20"]
      """  External Segment Value 20  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number of source document  """  
      self.PerBalFlag:bool = obj["PerBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.TBFlag:bool = obj["TBFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.DailyBalFlag:bool = obj["DailyBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GlbFiscalYearSuffix:str = obj["GlbFiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.GlbFiscalCalendarID:str = obj["GlbFiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.IntermediateProc:bool = obj["IntermediateProc"]
      """  Identifies the journal entry as one processed by consolidation posting mode where the data transfer is immediate and an intermediate book is used.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calculated sequence number not inteneded for external use.  """  
      self.SrcCompany:str = obj["SrcCompany"]
      """  Source Company Identifier.  Identifies the company where this GLJrnDtl originated from.  """  
      self.SrcBook:str = obj["SrcBook"]
      """  Unique Book Identifier  This is the book that is being consolidated into a target book.  """  
      self.SrcGLAccount:str = obj["SrcGLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SrcJrnlCode:str = obj["SrcJrnlCode"]
      """  Source Journal Code  """  
      self.SrcJournalNum:int = obj["SrcJournalNum"]
      """  Source Journal Number  """  
      self.SrcJournalLine:int = obj["SrcJournalLine"]
      """  Source Journal Line  """  
      self.SrcType:str = obj["SrcType"]
      """   P = derived from Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.
A = derived from Advanced Allocations.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equas ABTUID which was created during posting  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  This field shows Debit value of transaction  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  This field shows Credit value of transaction  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  """  
      self.ParentRUID:str = obj["ParentRUID"]
      """  If the current line is reversal, then this field is used for link with original journal line. It equals SysRowID of original line.  """  
      self.HasReverseLine:bool = obj["HasReverseLine"]
      """  if has reverse line  """  
      self.BalanceAcct:str = obj["BalanceAcct"]
      """  This is the resolved balance account the period balance, currency balance and/or daily balance records were written under for this GL Journal Detail GL Account.  """  
      self.TrialAcct:str = obj["TrialAcct"]
      """  This is the resolved balance account the trial balance records were written under for this GL Journal Detail GL Account.  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.AllocationStamp:str = obj["AllocationStamp"]
      """  This is the last allocation stamp that affected this GLJrnDtl.  """  
      self.BatchID:str = obj["BatchID"]
      """  Identifies the allocation batch this journal entry was processed under.  """  
      self.AllocID:str = obj["AllocID"]
      """  This is the allocation id that processed this journal entry.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  The allocation run number is a unique sequential number that identifies which run of an allocation batch this journal entry was created under.  """  
      self.AllocRunNbr:int = obj["AllocRunNbr"]
      """  Intended for internal use only.  Updated by the Advanced Allocations Engine.  This identifies the last allocation run number that used this GLJrnDtl as a source record.  """  
      self.AllocTgtNbr:int = obj["AllocTgtNbr"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.AllocTgtSeq:int = obj["AllocTgtSeq"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.ExtCOACode:str = obj["ExtCOACode"]
      """  External COA Code  """  
      self.MatchCode:str = obj["MatchCode"]
      """  MatchCode is used to match two or more journal detail records together.  """  
      self.MatchDate:str = obj["MatchDate"]
      """  MatchDate is set when the journal detail record is matched to other journal detail records.  """  
      self.Reconciled:bool = obj["Reconciled"]
      """  Indicates whether or not the transaction has been flagged as reconciled.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Sequence:int = obj["Sequence"]
      """  Journal Sequence Number  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.CustNum:int = obj["CustNum"]
      """  The Internal CustNum that ties back to the Customer master file.  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  CloseFiscalPeriod  """  
      self.SourcePlant:str = obj["SourcePlant"]
      """  SourcePlant  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.ExtSysType:str = obj["ExtSysType"]
      """  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  """  
      self.ExtSysURL:str = obj["ExtSysURL"]
      """  URL for drill back to an integrated external system  """  
      self.StatAmount:int = obj["StatAmount"]
      self.BitFlag:int = obj["BitFlag"]
      self.AHGLJrnDtlAlcHedTier:int = obj["AHGLJrnDtlAlcHedTier"]
      self.StatUOMStatUOMDesc:str = obj["StatUOMStatUOMDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AHGLJrnDtlSimRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year that entry applies to.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  """  
      self.Description:str = obj["Description"]
      """  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  """  
      self.JEDate:str = obj["JEDate"]
      """  Date for this journal transaction entry.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period that this journal entry applies to.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  User ID that posted this translation.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date that this transaction was posted to the G/L files.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this entry has been posted to the G/L master balance files. Unposted entries are excluded from all G/L reports.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctId of the BankAcct master that this check was drawn  against.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number.  """  
      self.CRHeadNum:int = obj["CRHeadNum"]
      """  Cash Receipts reference field.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  """  
      self.BankTranNum:int = obj["BankTranNum"]
      """  Bank Transaction Number.  Used when a transaction is a direct transfer from one bank account to another.  """  
      self.BankSlip:str = obj["BankSlip"]
      """   The identifier of the Bank Slip document (bank statement).  The user enters a bank slip during the reconciliation process.  This is then written into the related GLJrnDtl records.
Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.ExtRefType:str = obj["ExtRefType"]
      """  Multi-Company G/L Reference Type from the external company.  This is used by the Multi-Company Journal.  """  
      self.ExtRefCode:str = obj["ExtRefCode"]
      """  Multi-Company G/L Reference Code from the external company.  This is used by the Multi-Company Journal.  """  
      self.GlbJournalNum:int = obj["GlbJournalNum"]
      """  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalLine:int = obj["GlbJournalLine"]
      """  The Journal Line assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalCode:str = obj["GlbJournalCode"]
      """  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor number.  Used by Multi-Company Journal.  """  
      self.GlbAPInvoiceNum:str = obj["GlbAPInvoiceNum"]
      """  Global AP Invoice identifier.  Used by Multi-Company Journal.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Flag to indicate that a separate journal entry will be created at the target company for the Multi-Company G/L Account entered in this journal line.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to a Multi-Company Journal.  """  
      self.CommentText:str = obj["CommentText"]
      """  Extended text to describe the journal line entry.  Defaults from GLJrnHed.CommentText.  """  
      self.GlbCompanyID:str = obj["GlbCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.GlbFiscalYear:int = obj["GlbFiscalYear"]
      """  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  """  
      self.GlbFiscalPeriod:int = obj["GlbFiscalPeriod"]
      """  Fiscal period from the external company that this journal entry applies to.  """  
      self.GlbGroupID:str = obj["GlbGroupID"]
      """  The data entry Group from the external company that the journal entry is assigned to.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.ExtGLAccount:str = obj["ExtGLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.ExtSegValue1:str = obj["ExtSegValue1"]
      """  External Segment Value 1  """  
      self.ExtSegValue2:str = obj["ExtSegValue2"]
      """  External Segment Value 2  """  
      self.ExtSegValue3:str = obj["ExtSegValue3"]
      """  External Segment Value 3  """  
      self.ExtSegValue4:str = obj["ExtSegValue4"]
      """  External Segment Value 4  """  
      self.ExtSegValue5:str = obj["ExtSegValue5"]
      """  External Segment Value 5  """  
      self.ExtSegValue6:str = obj["ExtSegValue6"]
      """  External Segment Value 6  """  
      self.ExtSegValue7:str = obj["ExtSegValue7"]
      """  External Segment Value 7  """  
      self.ExtSegValue8:str = obj["ExtSegValue8"]
      """  External Segment Value 8  """  
      self.ExtSegValue9:str = obj["ExtSegValue9"]
      """  External Segment Value 9  """  
      self.ExtSegValue10:str = obj["ExtSegValue10"]
      """  External Segment Value 10  """  
      self.ExtSegValue11:str = obj["ExtSegValue11"]
      """  External Segment Value 11  """  
      self.ExtSegValue12:str = obj["ExtSegValue12"]
      """  External Segment Value 12  """  
      self.ExtSegValue13:str = obj["ExtSegValue13"]
      """  External Segment Value 13  """  
      self.ExtSegValue14:str = obj["ExtSegValue14"]
      """  External Segment Value 14  """  
      self.ExtSegValue15:str = obj["ExtSegValue15"]
      """  External Segment Value 15  """  
      self.ExtSegValue16:str = obj["ExtSegValue16"]
      """  External Segment Value 16  """  
      self.ExtSegValue17:str = obj["ExtSegValue17"]
      """  External Segment Value 17  """  
      self.ExtSegValue18:str = obj["ExtSegValue18"]
      """  External Segment Value 18  """  
      self.ExtSegValue19:str = obj["ExtSegValue19"]
      """  External Segment Value 19  """  
      self.ExtSegValue20:str = obj["ExtSegValue20"]
      """  External Segment Value 20  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number of source document  """  
      self.SummaryBalFlag:bool = obj["SummaryBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.DetailBalFlag:bool = obj["DetailBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.DailyBalFlag:bool = obj["DailyBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GlbFiscalYearSuffix:str = obj["GlbFiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.GlbFiscalCalendarID:str = obj["GlbFiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.IntermediateProc:bool = obj["IntermediateProc"]
      """  Identifies the journal entry as one processed by consolidation posting mode where the data transfer is immediate and an intermediate book is used.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calcualted sequence number not inteneded for external use.  """  
      self.SrcCompany:str = obj["SrcCompany"]
      """  Source Company Identifier.  Identifies the company where this GLJrnDtl originated from.  """  
      self.SrcBook:str = obj["SrcBook"]
      """  Unique Book Identifier  This is the book that is being consolidated into a target book.  """  
      self.SrcGLAccount:str = obj["SrcGLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SrcJrnlCode:str = obj["SrcJrnlCode"]
      """  Source Journal Code  """  
      self.SrcJournalNum:int = obj["SrcJournalNum"]
      """  Source Journal Number  """  
      self.SrcJournalLine:int = obj["SrcJournalLine"]
      """  Source Journal Line  """  
      self.SrcType:str = obj["SrcType"]
      """   P = derived from Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equas ABTUID which was created during posting  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  This field shows Debit value of transaction  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  This field shows Credit value of transaction  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  """  
      self.ParentRUID:str = obj["ParentRUID"]
      """  If the current line is reversal, then this field is used for link with original journal line. It equals SysRowID of original line.  """  
      self.HasReverseLine:bool = obj["HasReverseLine"]
      """  if has reverse line  """  
      self.BalanceAcct:str = obj["BalanceAcct"]
      """  This is the resolved balance account the period balance, currency balance and/or daily balance records were written under for this GL Journal Detail GL Account.  """  
      self.SummaryAcct:str = obj["SummaryAcct"]
      """  This is the resolved balance account the trial balance records were written under for this GL Journal Detail GL Account.  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.AllocationStamp:str = obj["AllocationStamp"]
      """  This is the allocation stamp that processed this journal entry.  Allocation Marks are entered on an Allocation Code.  """  
      self.BatchID:str = obj["BatchID"]
      """  Identifies the allocation batch this journal entry was processed under.  """  
      self.AllocID:str = obj["AllocID"]
      """  This is the allocation id that processed this journal entry.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  The allocation run number is a unique sequential number that identifies which run of an allocation batch this journal entry was processed under.  """  
      self.AllocRunNbr:int = obj["AllocRunNbr"]
      """  Intended for internal use only.  Updated by the Advanced Allocations Engine.  This identifies the last allocation run number that used this GLJrnDtl as a source record.  """  
      self.AllocTgtNbr:int = obj["AllocTgtNbr"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.AllocTgtSeq:int = obj["AllocTgtSeq"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Internal CustNum that ties back to the Customer master file.  """  
      self.StatAmount:int = obj["StatAmount"]
      self.BitFlag:int = obj["BitFlag"]
      self.AHGLJrnDtlSimAlcHedTier:int = obj["AHGLJrnDtlSimAlcHedTier"]
      self.StatUOMStatUOMDesc:str = obj["StatUOMStatUOMDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistAcctRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.AllocGLAcct:str = obj["AllocGLAcct"]
      """  GL Account or GL Account mask  """  
      self.AllocSegValue1:str = obj["AllocSegValue1"]
      """  Allocation Segment Value 1  """  
      self.AllocSegValue2:str = obj["AllocSegValue2"]
      """  Allocation Segment Value 2  """  
      self.AllocSegValue3:str = obj["AllocSegValue3"]
      """  Allocation Segment Value 3  """  
      self.AllocSegValue4:str = obj["AllocSegValue4"]
      """  Allocation Segment Value 4  """  
      self.AllocSegValue5:str = obj["AllocSegValue5"]
      """  Allocation Segment Value 5  """  
      self.AllocSegValue6:str = obj["AllocSegValue6"]
      """  Allocation Segment Value 6  """  
      self.AllocSegValue7:str = obj["AllocSegValue7"]
      """  Allocation Segment Value 7  """  
      self.AllocSegValue8:str = obj["AllocSegValue8"]
      """  Allocation Segment Value 8  """  
      self.AllocSegValue9:str = obj["AllocSegValue9"]
      """  Allocation Segment Value 9  """  
      self.AllocSegValue10:str = obj["AllocSegValue10"]
      """  Allocation Segment Value 10  """  
      self.AllocSegValue11:str = obj["AllocSegValue11"]
      """  Allocation Segment Value 11  """  
      self.AllocSegValue12:str = obj["AllocSegValue12"]
      """  Allocation Segment Value 12  """  
      self.AllocSegValue13:str = obj["AllocSegValue13"]
      """  Allocation Segment Value 13  """  
      self.AllocSegValue14:str = obj["AllocSegValue14"]
      """  Allocation Segment Value 14  """  
      self.AllocSegValue15:str = obj["AllocSegValue15"]
      """  Allocation Segment Value 15  """  
      self.AllocSegValue16:str = obj["AllocSegValue16"]
      """  Allocation Segment Value 16  """  
      self.AllocSegValue17:str = obj["AllocSegValue17"]
      """  Allocation Segment Value 17  """  
      self.AllocSegValue18:str = obj["AllocSegValue18"]
      """  Allocation Segment Value 18  """  
      self.AllocSegValue19:str = obj["AllocSegValue19"]
      """  Allocation Segment Value 19  """  
      self.AllocSegValue20:str = obj["AllocSegValue20"]
      """  Allocation Segment Value 20  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AllocGLAcctGLShortAcct:str = obj["AllocGLAcctGLShortAcct"]
      self.AllocGLAcctAccountDesc:str = obj["AllocGLAcctAccountDesc"]
      self.AllocGLAcctGLAcctDisp:str = obj["AllocGLAcctGLAcctDisp"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistActCatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.CategoryID:str = obj["CategoryID"]
      """  Unique identifier of this category of accounts.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.AllocTgtNbr:int = obj["AllocTgtNbr"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.AllocTgtSeq:int = obj["AllocTgtSeq"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.WriteOff:bool = obj["WriteOff"]
      """  Yes indicates this record contains information about the amount written off against the source account.  NO indicates this record contains information about the amount allocated.  """  
      self.SourceInitBalance:int = obj["SourceInitBalance"]
      """  Initial balance of the write off account.  Only updated when WriteOff = yes.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SourceAccount:str = obj["SourceAccount"]
      """  Source GL Account or Balance Account.  """  
      self.TargetAccount:str = obj["TargetAccount"]
      """  Account the source amount was allocated to.  """  
      self.ResolvedAccount:str = obj["ResolvedAccount"]
      """  REsolved GL Account.  This is the same as the target account if the target account does not have any mask characters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.AllocOption:int = obj["AllocOption"]
      """  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  """  
      self.AllocUnits:int = obj["AllocUnits"]
      """   The relative  number of units used to allocate to this account.
Allocation units / Total Allocation units is used to distribute the amount. Total Allocation units are calculated for a given AllocID and not stored.  """  
      self.RatioValue:int = obj["RatioValue"]
      """  Postive, fractional value indicating how much of an allocation is applied to this target.  """  
      self.RatioFormula:str = obj["RatioFormula"]
      """  Formula entered by the user used to calculate the allocation amount.  Only valid if the allocation option = 2.  """  
      self.ResolvedFormula:str = obj["ResolvedFormula"]
      """  Resolved Formula based upon the Ratio Formula.  Only valid if the allocation option = 2.  """  
      self.ReversingEntry:bool = obj["ReversingEntry"]
      """  Yes indicates this entry is a reversing entry.  No indicates it is not a reversing entry.  """  
      self.TgtSegVal1:str = obj["TgtSegVal1"]
      """  Target Segment Value 1  """  
      self.TgtSegVal2:str = obj["TgtSegVal2"]
      """  Target Segment Value 2  """  
      self.TgtSegVal3:str = obj["TgtSegVal3"]
      """  Target Segment Value 3  """  
      self.TgtSegVal4:str = obj["TgtSegVal4"]
      """  Target Segment Value 4  """  
      self.TgtSegVal5:str = obj["TgtSegVal5"]
      """  Target Segment Value 5  """  
      self.TgtSegVal6:str = obj["TgtSegVal6"]
      """  Target Segment Value 6  """  
      self.TgtSegVal7:str = obj["TgtSegVal7"]
      """  Target Segment Value 7  """  
      self.TgtSegVal8:str = obj["TgtSegVal8"]
      """  Target Segment Value 8  """  
      self.TgtSegVal9:str = obj["TgtSegVal9"]
      """  Target Segment Value 9  """  
      self.TgtSegVal10:str = obj["TgtSegVal10"]
      """  Target Segment Value 10  """  
      self.TgtSegVal11:str = obj["TgtSegVal11"]
      """  Target Segment Value 11  """  
      self.TgtSegVal12:str = obj["TgtSegVal12"]
      """  Target Segment Value 12  """  
      self.TgtSegVal13:str = obj["TgtSegVal13"]
      """  Target Segment Value 13  """  
      self.TgtSegVal14:str = obj["TgtSegVal14"]
      """  Target Segment Value 14  """  
      self.TgtSegVal15:str = obj["TgtSegVal15"]
      """  Target Segment Value 15  """  
      self.TgtSegVal16:str = obj["TgtSegVal16"]
      """  Target Segment Value 16  """  
      self.TgtSegVal17:str = obj["TgtSegVal17"]
      """  Target Segment Value 17  """  
      self.TgtSegVal18:str = obj["TgtSegVal18"]
      """  Target Segment Value 18  """  
      self.TgtSegVal19:str = obj["TgtSegVal19"]
      """  Target Segment Value 19  """  
      self.TgtSegVal20:str = obj["TgtSegVal20"]
      """  Target Segment Value 20  """  
      self.SrcSegVal1:str = obj["SrcSegVal1"]
      """  Source Segment Value 1  """  
      self.SrcSegVal2:str = obj["SrcSegVal2"]
      """  Source Segment Value 2  """  
      self.SrcSegVal3:str = obj["SrcSegVal3"]
      """  Source Segment Value 3  """  
      self.SrcSegVal4:str = obj["SrcSegVal4"]
      """  Source Segment Value 4  """  
      self.SrcSegVal5:str = obj["SrcSegVal5"]
      """  Source Segment Value 5  """  
      self.SrcSegVal6:str = obj["SrcSegVal6"]
      """  Source Segment Value 6  """  
      self.SrcSegVal7:str = obj["SrcSegVal7"]
      """  Source Segment Value 7  """  
      self.SrcSegVal8:str = obj["SrcSegVal8"]
      """  Source Segment Value 8  """  
      self.SrcSegVal9:str = obj["SrcSegVal9"]
      """  Source Segment Value 9  """  
      self.SrcSegVal10:str = obj["SrcSegVal10"]
      """  Source Segment Value 10  """  
      self.SrcSegVal11:str = obj["SrcSegVal11"]
      """  Source Segment Value 11  """  
      self.SrcSegVal12:str = obj["SrcSegVal12"]
      """  Source Segment Value 12  """  
      self.SrcSegVal13:str = obj["SrcSegVal13"]
      """  Source Segment Value 13  """  
      self.SrcSegVal14:str = obj["SrcSegVal14"]
      """  Source Segment Value 14  """  
      self.SrcSegVal15:str = obj["SrcSegVal15"]
      """  Source Segment Value 15  """  
      self.SrcSegVal16:str = obj["SrcSegVal16"]
      """  Source Segment Value 16  """  
      self.SrcSegVal17:str = obj["SrcSegVal17"]
      """  Source Segment Value 17  """  
      self.SrcSegVal18:str = obj["SrcSegVal18"]
      """  Source Segment Value 18  """  
      self.SrcSegVal19:str = obj["SrcSegVal19"]
      """  Source Segment Value 19  """  
      self.SrcSegVal20:str = obj["SrcSegVal20"]
      """  Source Segment Value 20  """  
      self.ResSegVal1:str = obj["ResSegVal1"]
      """  Resolved Segment Value 1  """  
      self.ResSegVal2:str = obj["ResSegVal2"]
      """  Resolved Segment Value 2  """  
      self.ResSegVal3:str = obj["ResSegVal3"]
      """  Resolved Segment Value 3  """  
      self.ResSegVal4:str = obj["ResSegVal4"]
      """  Resolved Segment Value 4  """  
      self.ResSegVal5:str = obj["ResSegVal5"]
      """  Resolved Segment Value 5  """  
      self.ResSegVal6:str = obj["ResSegVal6"]
      """  Resolved Segment Value 6  """  
      self.ResSegVal7:str = obj["ResSegVal7"]
      """  Resolved Segment Value 7  """  
      self.ResSegVal8:str = obj["ResSegVal8"]
      """  Resolved Segment Value 8  """  
      self.ResSegVal9:str = obj["ResSegVal9"]
      """  Resolved Segment Value 9  """  
      self.ResSegVal10:str = obj["ResSegVal10"]
      """  Resolved Segment Value 10  """  
      self.ResSegVal11:str = obj["ResSegVal11"]
      """  Resolved Segment Value 11  """  
      self.ResSegVal12:str = obj["ResSegVal12"]
      """  Resolved Segment Value 12  """  
      self.ResSegVal13:str = obj["ResSegVal13"]
      """  Resolved Segment Value 13  """  
      self.ResSegVal14:str = obj["ResSegVal14"]
      """  Resolved Segment Value 14  """  
      self.ResSegVal15:str = obj["ResSegVal15"]
      """  Resolved Segment Value 15  """  
      self.ResSegVal16:str = obj["ResSegVal16"]
      """  Resolved Segment Value 16  """  
      self.ResSegVal17:str = obj["ResSegVal17"]
      """  Resolved Segment Value 17  """  
      self.ResSegVal18:str = obj["ResSegVal18"]
      """  Resolved Segment Value 18  """  
      self.ResSegVal19:str = obj["ResSegVal19"]
      """  Resolved Segment Value 19  """  
      self.ResSegVal20:str = obj["ResSegVal20"]
      """  Resolved Segment Value 20  """  
      self.ReverseFY:int = obj["ReverseFY"]
      """  The reversed fiscal year.  This is updated by reverse allocation run logic.  """  
      self.ReverseFYS:str = obj["ReverseFYS"]
      """   The reversed fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.
This is updated by reverse allocation run logic.  """  
      self.ReverseJournalNum:int = obj["ReverseJournalNum"]
      """   Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.
This is updated by reverse allocation run logic.  """  
      self.ReverseJournalLine:int = obj["ReverseJournalLine"]
      """   A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a
.specific Company/FiscalYear/JournalNum combination and adding 1.This is updated by reverse allocation run logic  """  
      self.SrcDebitAmount:int = obj["SrcDebitAmount"]
      """  Source amount applied to the formula/percentage during an allocation.  """  
      self.SrcCreditAmount:int = obj["SrcCreditAmount"]
      """  Source amount applied to the formula/percentage during an allocation.  """  
      self.RevEntryFY:int = obj["RevEntryFY"]
      """  The reversed entry fiscal year.  This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is created.  """  
      self.RevEntryFYS:str = obj["RevEntryFYS"]
      """   The reversed fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is created.  """  
      self.RevEntryJrnlNum:int = obj["RevEntryJrnlNum"]
      """   Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is created.  """  
      self.RevEntryJrnlLine:int = obj["RevEntryJrnlLine"]
      """   A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a .specific Company/FiscalYear/JournalNum combination and adding 1.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is created.  """  
      self.RevReverseFY:int = obj["RevReverseFY"]
      """  The reversed entry reversing fiscal year.  This is updated when an allocation batch has the reversing entry option set to yes and the reversing journal entry is reversed.  """  
      self.RevReverseFYS:str = obj["RevReverseFYS"]
      """   The reversed reversing entry fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is reversed.  """  
      self.RevReverseJrnlNum:int = obj["RevReverseJrnlNum"]
      """   Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is reversed.  """  
      self.RevReverseJrnlLine:int = obj["RevReverseJrnlLine"]
      """   A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a .specific Company/FiscalYear/JournalNum combination and adding 1.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is reversed.  """  
      self.CycleUID:int = obj["CycleUID"]
      """  Cycle unique ID.  This is not intended for external use.  """  
      self.CycleNumber:int = obj["CycleNumber"]
      """  Cycle number.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GLAccount:str = obj["GLAccount"]
      self.CreditAmount:int = obj["CreditAmount"]
      self.DebitAmount:int = obj["DebitAmount"]
      self.JEDate:str = obj["JEDate"]
      self.BitFlag:int = obj["BitFlag"]
      self.AlcHistDtlAlcHedTier:int = obj["AlcHistDtlAlcHedTier"]
      self.AlcHistDtlJrnlCdJrnlDescription:str = obj["AlcHistDtlJrnlCdJrnlDescription"]
      self.ResolvedGLAcctDispGLShortAcct:str = obj["ResolvedGLAcctDispGLShortAcct"]
      self.ResolvedGLAcctDispGLAcctDisp:str = obj["ResolvedGLAcctDispGLAcctDisp"]
      self.ResolvedGLAcctDispAccountDesc:str = obj["ResolvedGLAcctDispAccountDesc"]
      self.SourceAccountAccountDesc:str = obj["SourceAccountAccountDesc"]
      self.SourceAccountGLShortAcct:str = obj["SourceAccountGLShortAcct"]
      self.SourceAccountGLAcctDisp:str = obj["SourceAccountGLAcctDisp"]
      self.TargetAccountAccountDesc:str = obj["TargetAccountAccountDesc"]
      self.TargetAccountGLShortAcct:str = obj["TargetAccountGLShortAcct"]
      self.TargetAccountGLAcctDisp:str = obj["TargetAccountGLAcctDisp"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistJrnCdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Unique identifier of the journal used to group entries. The user can create their own journal codes to be used instead of the default codes.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.JrnlCodeJrnlDescription:str = obj["JrnlCodeJrnlDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.RunDate:str = obj["RunDate"]
      """  Date the batch was run.  """  
      self.RunTime:int = obj["RunTime"]
      """  Time the allocaiton batch run started.  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.Simulation:bool = obj["Simulation"]
      """  Indicates if this is simulation history record or General Ledger history record.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date for journal transactions.  """  
      self.ApplyDateRev:str = obj["ApplyDateRev"]
      """  Date used for reversing entries.  """  
      self.StartDate:str = obj["StartDate"]
      """  Starting date for record selection.  Defaults to the fiscal period start date.  """  
      self.EndDate:str = obj["EndDate"]
      """  Ending date for record seletion.  Defaults to fiscal period end date.  """  
      self.SchedDate:str = obj["SchedDate"]
      """  Date when the allocation batch is due to be run.  """  
      self.BatchDesc:str = obj["BatchDesc"]
      """  Batch Description  """  
      self.Tier:int = obj["Tier"]
      """  Allocation tier.  """  
      self.SchedNum:int = obj["SchedNum"]
      """  Internal next number used to keep the schedule records unique.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates whether or not reversing transactions are generated at the time a journal entry is allocated.  Yes indicates reversing entries are generated.  No indicates reversing entries are not generated.  """  
      self.YTDAlloc:bool = obj["YTDAlloc"]
      """  Indicates if the allocation run started at the beginning of the current fiscal year.  """  
      self.AllocReversed:bool = obj["AllocReversed"]
      """  Indicates if the allocation run has been reversed.  """  
      self.PriorTgtStamp:str = obj["PriorTgtStamp"]
      """  Identifies the allocation stamp to which this allocation is to be applied.  """  
      self.TgtStamp:str = obj["TgtStamp"]
      """  Identifies the allocation stamp that is to to be stamped on the GLJrnDtls.  """  
      self.SrcAllocStamp:str = obj["SrcAllocStamp"]
      """  Identifies the allocation stamp that was processed by this allocation.  """  
      self.IgnoreStamp:bool = obj["IgnoreStamp"]
      """  When Yes the Allocation Engine ignores the allocation stamp assigned to the GLJrnDtl when determining if a entry is subject to allocations for the current allocation code.  """  
      self.UseAllStamps:bool = obj["UseAllStamps"]
      """  Yes indicates that all allocation stamps are valid for the allocation code.  """  
      self.AllocOption:int = obj["AllocOption"]
      """  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  """  
      self.PercentToAlloc:int = obj["PercentToAlloc"]
      """  Postive, fractional value indicating how much of a source is allocated.  Default value is 100.00.  """  
      self.UseAllocUnits:bool = obj["UseAllocUnits"]
      """  Indicates if the allocation units are used.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RunTypeDesc:str = obj["RunTypeDesc"]
      self.AlcHistFiscalCalDescription:str = obj["AlcHistFiscalCalDescription"]
      """  Calendar description.  """  
      self.AlcHistGLBookCurrencyCode:str = obj["AlcHistGLBookCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.AlcHistGLBookDescription:str = obj["AlcHistGLBookDescription"]
      """  Descripiton of Book  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistNFSrcRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique. The value of ParamNbr identifies the parameter number the record is defined for.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.LookupTblMapUID_obsolete:int = obj["LookupTblMapUID_obsolete"]
      """  LookupTblMapUID_obsolete  """  
      self.TgtSeqNbr_obsolete:int = obj["TgtSeqNbr_obsolete"]
      """  TgtSeqNbr_obsolete  """  
      self.LinkUID_obsolete:int = obj["LinkUID_obsolete"]
      """  LinkUID_obsolete  """  
      self.SrcFieldName:str = obj["SrcFieldName"]
      """  Source field name.  """  
      self.ParamOpt:int = obj["ParamOpt"]
      """   Identifes the option for the non-financial parameter.
1 = Use Target Account Segment.  
2 = Use Source Account Segment
3 = Use Allocation Run Start Date
4 = Use allocation Run End Date  """  
      self.ParamSegmentNbr:int = obj["ParamSegmentNbr"]
      """  Identifies the segment number to use to determine the segment code that will be used to look up the result value in the lookup table.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.EntryType:int = obj["EntryType"]
      """  Identifies if the parameter is an actual value or an option.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SrcSeqNbr:int = obj["SrcSeqNbr"]
      """  SrcSeqNbr  """  
      self.SrcCodeID:str = obj["SrcCodeID"]
      """  SrcCodeID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistParamsBAQRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique.  """  
      self.BAQExportID:str = obj["BAQExportID"]
      """  BAQ ID, the unique identifier for this Query table within the company  """  
      self.BAQParamValNbr:int = obj["BAQParamValNbr"]
      """  Intended for internal use only to keep the records unique.  """  
      self.ParameterName:str = obj["ParameterName"]
      self.BAQParamCode:str = obj["BAQParamCode"]
      """  Specific baq parameter value.  """  
      self.ParamOpt:int = obj["ParamOpt"]
      """   Identifes the option for the non-financial parameter.
1 = Use Target Account Segment.  
2 = Use Source Account Segment
3 = Use Allocation Run Start Date
4 = Use allocation Run End Date  """  
      self.ParamSegmentNbr:int = obj["ParamSegmentNbr"]
      """  Identifies the segment number to use to determine the segment code that will be used to look up the result value in the lookup table.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.EntryType:int = obj["EntryType"]
      """  Identifies if the parameter is an actual value or an option.  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistParamsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.ParamName:str = obj["ParamName"]
      """  The name assigned to a parameter.  This name must be unique.  """  
      self.ParamType:int = obj["ParamType"]
      """  Identifies the type of parameter used in the allocation logic.  1 = Account Balances, 2 = Summarized balances and 3 = BAQ.  """  
      self.ParamDesc:str = obj["ParamDesc"]
      """  Text that describes the parameter.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.AcctBalAcct:str = obj["AcctBalAcct"]
      """  Account balance account.  Only valid when the formula type = 1.  """  
      self.AcctBalSegVal1:str = obj["AcctBalSegVal1"]
      """  Account Segment Value 1  """  
      self.AcctBalSegVal2:str = obj["AcctBalSegVal2"]
      """  Account Segment Value 2  """  
      self.AcctBalSegVal3:str = obj["AcctBalSegVal3"]
      """  Account Segment Value 3  """  
      self.AcctBalSegVal4:str = obj["AcctBalSegVal4"]
      """  Account Segment Value 4  """  
      self.AcctBalSegVal5:str = obj["AcctBalSegVal5"]
      """  Account Segment Value 5  """  
      self.AcctBalSegVal6:str = obj["AcctBalSegVal6"]
      """  Account Segment Value 6  """  
      self.AcctBalSegVal7:str = obj["AcctBalSegVal7"]
      """  Account Segment Value 7  """  
      self.AcctBalSegVal8:str = obj["AcctBalSegVal8"]
      """  Account Segment Value 8  """  
      self.AcctBalSegVal9:str = obj["AcctBalSegVal9"]
      """  Account Segment Value 9  """  
      self.AcctBalSegVal10:str = obj["AcctBalSegVal10"]
      """  Account Segment Value 10  """  
      self.AcctBalSegVal11:str = obj["AcctBalSegVal11"]
      """  Account Segment Value 11  """  
      self.AcctBalSegVal12:str = obj["AcctBalSegVal12"]
      """  Account Segment Value 12  """  
      self.AcctBalSegVal13:str = obj["AcctBalSegVal13"]
      """  Account Segment Value 13  """  
      self.AcctBalSegVal14:str = obj["AcctBalSegVal14"]
      """  Account Segment Value 14  """  
      self.AcctBalSegVal15:str = obj["AcctBalSegVal15"]
      """  Account Segment Value 15  """  
      self.AcctBalSegVal16:str = obj["AcctBalSegVal16"]
      """  Account Segment Value 16  """  
      self.AcctBalSegVal17:str = obj["AcctBalSegVal17"]
      """  Account Segment Value 17  """  
      self.AcctBalSegVal18:str = obj["AcctBalSegVal18"]
      """  Account Segment Value 18  """  
      self.AcctBalSegVal19:str = obj["AcctBalSegVal19"]
      """  Account Segment Value 19  """  
      self.AcctBalSegVal20:str = obj["AcctBalSegVal20"]
      """  Account Segment Value 20  """  
      self.UseTgtAcct:bool = obj["UseTgtAcct"]
      """  Yes indictes the target account's balance is taken and the AcctBalAcct is set equal to the AlcTarget.TgtGLAcct.  This only only valid when the formula type = Account Balances.  """  
      self.BAQExportID:str = obj["BAQExportID"]
      """  BAQ  ID, the unique identifier for the query table within the company  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.AcctParamValSrc:int = obj["AcctParamValSrc"]
      """  Indicates the source data for the value of a parameter value when the parameter is of type Account Balance.  """  
      self.SumParamValSrc:int = obj["SumParamValSrc"]
      """  Indicates the source data for the value of a parameter value when the parameter is of type Summarized.  """  
      self.Reversed:bool = obj["Reversed"]
      """  Indicates if the allocation run was reversed.  """  
      self.ReversedDate:str = obj["ReversedDate"]
      """  Date used to reverse the allocation run.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NFSrcMapUID:int = obj["NFSrcMapUID"]
      """  NFSrcMapUID  """  
      self.NFTgtSeqNbr:int = obj["NFTgtSeqNbr"]
      """  NFTgtSeqNbr  """  
      self.YTDBalance:bool = obj["YTDBalance"]
      """  YTDBalance  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AcctBalAcctGLAcctDispAccountDesc:str = obj["AcctBalAcctGLAcctDispAccountDesc"]
      self.AcctBalAcctGLAcctDispGLShortAcct:str = obj["AcctBalAcctGLAcctDispGLShortAcct"]
      self.AcctBalAcctGLAcctDispGLAcctDisp:str = obj["AcctBalAcctGLAcctDispGLAcctDisp"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistRangeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.MinValue:str = obj["MinValue"]
      """  Minimum vale for range selection.  """  
      self.MaxValue:str = obj["MaxValue"]
      """  Maximum value for range selection.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COASegmentSegmentName:str = obj["COASegmentSegmentName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistResParamsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.AllocTgtNbr:int = obj["AllocTgtNbr"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.AllocTgtSeq:int = obj["AllocTgtSeq"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique.  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.ActualValue:int = obj["ActualValue"]
      """  Actual calculated value.  """  
      self.ResBalAcct:str = obj["ResBalAcct"]
      """  Account balance account.  Only valid when the formula type = 1.  This is the gl account with all mask characters resolved.  """  
      self.ResBalSegVal1:str = obj["ResBalSegVal1"]
      """  Resolved  Segment Value 1  """  
      self.ResBalSegVal2:str = obj["ResBalSegVal2"]
      """  Resolved  Segment Value 2  """  
      self.ResBalSegVal3:str = obj["ResBalSegVal3"]
      """  Resolved  Segment Value 3  """  
      self.ResBalSegVal4:str = obj["ResBalSegVal4"]
      """  Resolved Segment Value 4  """  
      self.ResBalSegVal5:str = obj["ResBalSegVal5"]
      """  Resolved  Segment Value 5  """  
      self.ResBalSegVal6:str = obj["ResBalSegVal6"]
      """  Resolved  Segment Value 6  """  
      self.ResBalSegVal7:str = obj["ResBalSegVal7"]
      """  Resolved Segment Value 7  """  
      self.ResBalSegVal8:str = obj["ResBalSegVal8"]
      """  Resolved  Segment Value 8  """  
      self.ResBalSegVal9:str = obj["ResBalSegVal9"]
      """  Resolved  Segment Value 9  """  
      self.ResBalSegVal10:str = obj["ResBalSegVal10"]
      """  Resolved Segment Value 10  """  
      self.ResBalSegVal11:str = obj["ResBalSegVal11"]
      """  Resolved Segment Value 11  """  
      self.ResBalSegVal12:str = obj["ResBalSegVal12"]
      """  Resolved  Segment Value 12  """  
      self.ResBalSegVal13:str = obj["ResBalSegVal13"]
      """  Resolved  Segment Value 13  """  
      self.ResBalSegVal14:str = obj["ResBalSegVal14"]
      """  Resolved  Segment Value 14  """  
      self.ResBalSegVal15:str = obj["ResBalSegVal15"]
      """  Resolved Segment Value 15  """  
      self.ResBalSegVal16:str = obj["ResBalSegVal16"]
      """  Resolved  Segment Value 16  """  
      self.ResBalSegVal17:str = obj["ResBalSegVal17"]
      """  Resolved  Segment Value 17  """  
      self.ResBalSegVal18:str = obj["ResBalSegVal18"]
      """  Resolved  Segment Value 18  """  
      self.ResBalSegVal19:str = obj["ResBalSegVal19"]
      """  Resolved Segment Value 19  """  
      self.ResBalSegVal20:str = obj["ResBalSegVal20"]
      """  Resolved  Segment Value 20  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.CycleUID:int = obj["CycleUID"]
      """  Cycle unique ID.  This is not intended for external use.  """  
      self.CycleNumber:int = obj["CycleNumber"]
      """  Cycle number.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.YTDBalance:bool = obj["YTDBalance"]
      """  YTDBalance  """  
      self.AcctBalAcct:str = obj["AcctBalAcct"]
      self.UseTgtAcct:bool = obj["UseTgtAcct"]
      self.BAQExportID:str = obj["BAQExportID"]
      self.AcctParamValSrc:int = obj["AcctParamValSrc"]
      self.SumParamValSrc:int = obj["SumParamValSrc"]
      self.TgtGLAcct:str = obj["TgtGLAcct"]
      self.BitFlag:int = obj["BitFlag"]
      self.AlcHistParamsParamType:int = obj["AlcHistParamsParamType"]
      self.AlcHistParamsAcctParamValSrc:int = obj["AlcHistParamsAcctParamValSrc"]
      self.AlcHistParamsUseTgtAcct:bool = obj["AlcHistParamsUseTgtAcct"]
      self.AlcHistParamsParamName:str = obj["AlcHistParamsParamName"]
      self.AlcHistParamsSumParamValSrc:int = obj["AlcHistParamsSumParamValSrc"]
      self.AlcHistParamsBAQExportID:str = obj["AlcHistParamsBAQExportID"]
      self.AlcHistParamsAcctBalAcct:str = obj["AlcHistParamsAcctBalAcct"]
      self.AlcHistParamsParamDesc:str = obj["AlcHistParamsParamDesc"]
      self.ResAcctDispGLShortAcct:str = obj["ResAcctDispGLShortAcct"]
      self.ResAcctDispGLAcctDisp:str = obj["ResAcctDispGLAcctDisp"]
      self.ResAcctDispAccountDesc:str = obj["ResAcctDispAccountDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistResParamsSimRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.AllocTgtNbr:int = obj["AllocTgtNbr"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.AllocTgtSeq:int = obj["AllocTgtSeq"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique.  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.ActualValue:int = obj["ActualValue"]
      """  Actual calculated value.  """  
      self.ResBalAcct:str = obj["ResBalAcct"]
      """  Account balance account.  Only valid when the formula type = 1.  This is the gl account with all mask characters resolved.  """  
      self.ResBalSegVal1:str = obj["ResBalSegVal1"]
      """  Resolved  Segment Value 1  """  
      self.ResBalSegVal2:str = obj["ResBalSegVal2"]
      """  Resolved  Segment Value 2  """  
      self.ResBalSegVal3:str = obj["ResBalSegVal3"]
      """  Resolved  Segment Value 3  """  
      self.ResBalSegVal4:str = obj["ResBalSegVal4"]
      """  Resolved Segment Value 4  """  
      self.ResBalSegVal5:str = obj["ResBalSegVal5"]
      """  Resolved  Segment Value 5  """  
      self.ResBalSegVal6:str = obj["ResBalSegVal6"]
      """  Resolved  Segment Value 6  """  
      self.ResBalSegVal7:str = obj["ResBalSegVal7"]
      """  Resolved Segment Value 7  """  
      self.ResBalSegVal8:str = obj["ResBalSegVal8"]
      """  Resolved  Segment Value 8  """  
      self.ResBalSegVal9:str = obj["ResBalSegVal9"]
      """  Resolved  Segment Value 9  """  
      self.ResBalSegVal10:str = obj["ResBalSegVal10"]
      """  Resolved Segment Value 10  """  
      self.ResBalSegVal11:str = obj["ResBalSegVal11"]
      """  Resolved Segment Value 11  """  
      self.ResBalSegVal12:str = obj["ResBalSegVal12"]
      """  Resolved  Segment Value 12  """  
      self.ResBalSegVal13:str = obj["ResBalSegVal13"]
      """  Resolved  Segment Value 13  """  
      self.ResBalSegVal14:str = obj["ResBalSegVal14"]
      """  Resolved  Segment Value 14  """  
      self.ResBalSegVal15:str = obj["ResBalSegVal15"]
      """  Resolved Segment Value 15  """  
      self.ResBalSegVal16:str = obj["ResBalSegVal16"]
      """  Resolved  Segment Value 16  """  
      self.ResBalSegVal17:str = obj["ResBalSegVal17"]
      """  Resolved  Segment Value 17  """  
      self.ResBalSegVal18:str = obj["ResBalSegVal18"]
      """  Resolved  Segment Value 18  """  
      self.ResBalSegVal19:str = obj["ResBalSegVal19"]
      """  Resolved Segment Value 19  """  
      self.ResBalSegVal20:str = obj["ResBalSegVal20"]
      """  Resolved  Segment Value 20  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.CycleUID:int = obj["CycleUID"]
      """  Cycle unique ID.  This is not intended for external use.  """  
      self.CycleNumber:int = obj["CycleNumber"]
      """  Cycle number.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.YTDBalance:bool = obj["YTDBalance"]
      """  YTDBalance  """  
      self.TgtGLAcct:str = obj["TgtGLAcct"]
      self.BitFlag:int = obj["BitFlag"]
      self.AlcHistParamsSimSumParamValSrc:int = obj["AlcHistParamsSimSumParamValSrc"]
      self.AlcHistParamsSimParamName:str = obj["AlcHistParamsSimParamName"]
      self.AlcHistParamsSimParamType:int = obj["AlcHistParamsSimParamType"]
      self.AlcHistParamsSimAcctBalAcct:str = obj["AlcHistParamsSimAcctBalAcct"]
      self.AlcHistParamsSimParamDesc:str = obj["AlcHistParamsSimParamDesc"]
      self.AlcHistParamsSimUseTgtAcct:bool = obj["AlcHistParamsSimUseTgtAcct"]
      self.AlcHistParamsSimAcctParamValSrc:int = obj["AlcHistParamsSimAcctParamValSrc"]
      self.ResAcctDispSimGLAcctDisp:str = obj["ResAcctDispSimGLAcctDisp"]
      self.ResAcctDispSimGLShortAcct:str = obj["ResAcctDispSimGLShortAcct"]
      self.ResAcctDispSimAccountDesc:str = obj["ResAcctDispSimAccountDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.RunDate:str = obj["RunDate"]
      """  Date the batch was run.  """  
      self.RunTime:int = obj["RunTime"]
      """  Time the allocaiton batch run started.  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.Simulation:bool = obj["Simulation"]
      """  Indicates if this is simulation history record or General Ledger history record.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date for journal transactions.  """  
      self.ApplyDateRev:str = obj["ApplyDateRev"]
      """  Date used for reversing entries.  """  
      self.StartDate:str = obj["StartDate"]
      """  Starting date for record selection.  Defaults to the fiscal period start date.  """  
      self.EndDate:str = obj["EndDate"]
      """  Ending date for record seletion.  Defaults to fiscal period end date.  """  
      self.SchedDate:str = obj["SchedDate"]
      """  Date when the allocation batch is due to be run.  """  
      self.BatchDesc:str = obj["BatchDesc"]
      """  Batch Description  """  
      self.Tier:int = obj["Tier"]
      """  Allocation tier.  """  
      self.SchedNum:int = obj["SchedNum"]
      """  Internal next number used to keep the schedule records unique.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates whether or not reversing transactions are generated at the time a journal entry is allocated.  Yes indicates reversing entries are generated.  No indicates reversing entries are not generated.  """  
      self.YTDAlloc:bool = obj["YTDAlloc"]
      """  Indicates if the allocation run started at the beginning of the current fiscal year.  """  
      self.AllocReversed:bool = obj["AllocReversed"]
      """  Indicates if the allocation run has been reversed.  """  
      self.PriorTgtStamp:str = obj["PriorTgtStamp"]
      """  Identifies the allocation stamp to which this allocation is to be applied.  """  
      self.TgtStamp:str = obj["TgtStamp"]
      """  Identifies the allocation stamp that is to to be stamped on the GLJrnDtls.  """  
      self.SrcAllocStamp:str = obj["SrcAllocStamp"]
      """  Identifies the allocation stamp that was processed by this allocation.  """  
      self.IgnoreStamp:bool = obj["IgnoreStamp"]
      """  When Yes the Allocation Engine ignores the allocation stamp assigned to the GLJrnDtl when determining if a entry is subject to allocations for the current allocation code.  """  
      self.UseAllStamps:bool = obj["UseAllStamps"]
      """  Yes indicates that all allocation stamps are valid for the allocation code.  """  
      self.AllocOption:int = obj["AllocOption"]
      """  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  """  
      self.PercentToAlloc:int = obj["PercentToAlloc"]
      """  Postive, fractional value indicating how much of a source is allocated.  Default value is 100.00.  """  
      self.UseAllocUnits:bool = obj["UseAllocUnits"]
      """  Indicates if the allocation units are used.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.StatBalAsAllocUnits:bool = obj["StatBalAsAllocUnits"]
      """  StatBalAsAllocUnits  """  
      self.RunTypeDesc:str = obj["RunTypeDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.AlcHistFiscalCalDescription:str = obj["AlcHistFiscalCalDescription"]
      self.AlcHistGLBookCurrencyCode:str = obj["AlcHistGLBookCurrencyCode"]
      self.AlcHistGLBookDescription:str = obj["AlcHistGLBookDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PAlcHistAcctRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.AllocGLAcct:str = obj["AllocGLAcct"]
      """  GL Account or GL Account mask  """  
      self.AllocSegValue1:str = obj["AllocSegValue1"]
      """  Allocation Segment Value 1  """  
      self.AllocSegValue2:str = obj["AllocSegValue2"]
      """  Allocation Segment Value 2  """  
      self.AllocSegValue3:str = obj["AllocSegValue3"]
      """  Allocation Segment Value 3  """  
      self.AllocSegValue4:str = obj["AllocSegValue4"]
      """  Allocation Segment Value 4  """  
      self.AllocSegValue5:str = obj["AllocSegValue5"]
      """  Allocation Segment Value 5  """  
      self.AllocSegValue6:str = obj["AllocSegValue6"]
      """  Allocation Segment Value 6  """  
      self.AllocSegValue7:str = obj["AllocSegValue7"]
      """  Allocation Segment Value 7  """  
      self.AllocSegValue8:str = obj["AllocSegValue8"]
      """  Allocation Segment Value 8  """  
      self.AllocSegValue9:str = obj["AllocSegValue9"]
      """  Allocation Segment Value 9  """  
      self.AllocSegValue10:str = obj["AllocSegValue10"]
      """  Allocation Segment Value 10  """  
      self.AllocSegValue11:str = obj["AllocSegValue11"]
      """  Allocation Segment Value 11  """  
      self.AllocSegValue12:str = obj["AllocSegValue12"]
      """  Allocation Segment Value 12  """  
      self.AllocSegValue13:str = obj["AllocSegValue13"]
      """  Allocation Segment Value 13  """  
      self.AllocSegValue14:str = obj["AllocSegValue14"]
      """  Allocation Segment Value 14  """  
      self.AllocSegValue15:str = obj["AllocSegValue15"]
      """  Allocation Segment Value 15  """  
      self.AllocSegValue16:str = obj["AllocSegValue16"]
      """  Allocation Segment Value 16  """  
      self.AllocSegValue17:str = obj["AllocSegValue17"]
      """  Allocation Segment Value 17  """  
      self.AllocSegValue18:str = obj["AllocSegValue18"]
      """  Allocation Segment Value 18  """  
      self.AllocSegValue19:str = obj["AllocSegValue19"]
      """  Allocation Segment Value 19  """  
      self.AllocSegValue20:str = obj["AllocSegValue20"]
      """  Allocation Segment Value 20  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PAllocGLAccountGLAcctDisp:str = obj["PAllocGLAccountGLAcctDisp"]
      self.PAllocGLAccountGLShortAcct:str = obj["PAllocGLAccountGLShortAcct"]
      self.PAllocGLAccountAccountDesc:str = obj["PAllocGLAccountAccountDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PAlcHistActCatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.CategoryID:str = obj["CategoryID"]
      """  Unique identifier of this category of accounts.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PAlcHistJrnCdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Unique identifier of the journal used to group entries. The user can create their own journal codes to be used instead of the default codes.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PHistJrnlCodeJrnlDescription:str = obj["PHistJrnlCodeJrnlDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PAlcHistRangeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.MinValue:str = obj["MinValue"]
      """  Minimum vale for range selection.  """  
      self.MaxValue:str = obj["MaxValue"]
      """  Maximum value for range selection.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PCOASegmentSegmentName:str = obj["PCOASegmentSegmentName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   batchID
   runNbr
   allocID
   """  
   def __init__(self, obj):
      self.batchID:str = obj["batchID"]
      self.runNbr:int = obj["runNbr"]
      self.allocID:str = obj["allocID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_AHGLJrnDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year that entry applies to.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  """  
      self.Description:str = obj["Description"]
      """  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  """  
      self.JEDate:str = obj["JEDate"]
      """  Date for this journal transaction entry.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period that this journal entry applies to.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  User ID that posted this translation.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date that this transaction was posted to the G/L files.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this entry has been posted to the G/L master balance files. Unposted entries are excluded from all G/L reports.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctId of the BankAcct master that this check was drawn  against.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number.  """  
      self.CRHeadNum:int = obj["CRHeadNum"]
      """  Cash Receipts reference field.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  """  
      self.BankTranNum:int = obj["BankTranNum"]
      """  Bank Transaction Number.  Used when a transaction is a direct transfer from one bank account to another.  """  
      self.BankSlip:str = obj["BankSlip"]
      """   The identifier of the Bank Slip document (bank statement).  The user enters a bank slip during the reconciliation process.  This is then written into the related GLJrnDtl records.
Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.ExtRefType:str = obj["ExtRefType"]
      """  Multi-Company G/L Reference Type from the external company.  This is used by the Multi-Company Journal.  """  
      self.ExtRefCode:str = obj["ExtRefCode"]
      """  Multi-Company G/L Reference Code from the external company.  This is used by the Multi-Company Journal.  """  
      self.GlbJournalNum:int = obj["GlbJournalNum"]
      """  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalLine:int = obj["GlbJournalLine"]
      """  The Journal Line assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalCode:str = obj["GlbJournalCode"]
      """  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor number.  Used by Multi-Company Journal.  """  
      self.GlbAPInvoiceNum:str = obj["GlbAPInvoiceNum"]
      """  Global AP Invoice identifier.  Used by Multi-Company Journal.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Flag to indicate that a separate journal entry will be created at the target company for the Multi-Company G/L Account entered in this journal line.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to a Multi-Company Journal.  """  
      self.CommentText:str = obj["CommentText"]
      """  Extended text to describe the journal line entry.  Defaults from GLJrnHed.CommentText.  """  
      self.GlbCompanyID:str = obj["GlbCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.GlbFiscalYear:int = obj["GlbFiscalYear"]
      """  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  """  
      self.GlbFiscalPeriod:int = obj["GlbFiscalPeriod"]
      """  Fiscal period from the external company that this journal entry applies to.  """  
      self.GlbGroupID:str = obj["GlbGroupID"]
      """  The data entry Group from the external company that the journal entry is assigned to.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.ExtGLAccount:str = obj["ExtGLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.ExtSegValue1:str = obj["ExtSegValue1"]
      """  External Segment Value 1  """  
      self.ExtSegValue2:str = obj["ExtSegValue2"]
      """  External Segment Value 2  """  
      self.ExtSegValue3:str = obj["ExtSegValue3"]
      """  External Segment Value 3  """  
      self.ExtSegValue4:str = obj["ExtSegValue4"]
      """  External Segment Value 4  """  
      self.ExtSegValue5:str = obj["ExtSegValue5"]
      """  External Segment Value 5  """  
      self.ExtSegValue6:str = obj["ExtSegValue6"]
      """  External Segment Value 6  """  
      self.ExtSegValue7:str = obj["ExtSegValue7"]
      """  External Segment Value 7  """  
      self.ExtSegValue8:str = obj["ExtSegValue8"]
      """  External Segment Value 8  """  
      self.ExtSegValue9:str = obj["ExtSegValue9"]
      """  External Segment Value 9  """  
      self.ExtSegValue10:str = obj["ExtSegValue10"]
      """  External Segment Value 10  """  
      self.ExtSegValue11:str = obj["ExtSegValue11"]
      """  External Segment Value 11  """  
      self.ExtSegValue12:str = obj["ExtSegValue12"]
      """  External Segment Value 12  """  
      self.ExtSegValue13:str = obj["ExtSegValue13"]
      """  External Segment Value 13  """  
      self.ExtSegValue14:str = obj["ExtSegValue14"]
      """  External Segment Value 14  """  
      self.ExtSegValue15:str = obj["ExtSegValue15"]
      """  External Segment Value 15  """  
      self.ExtSegValue16:str = obj["ExtSegValue16"]
      """  External Segment Value 16  """  
      self.ExtSegValue17:str = obj["ExtSegValue17"]
      """  External Segment Value 17  """  
      self.ExtSegValue18:str = obj["ExtSegValue18"]
      """  External Segment Value 18  """  
      self.ExtSegValue19:str = obj["ExtSegValue19"]
      """  External Segment Value 19  """  
      self.ExtSegValue20:str = obj["ExtSegValue20"]
      """  External Segment Value 20  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number of source document  """  
      self.PerBalFlag:bool = obj["PerBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.TBFlag:bool = obj["TBFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.DailyBalFlag:bool = obj["DailyBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GlbFiscalYearSuffix:str = obj["GlbFiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.GlbFiscalCalendarID:str = obj["GlbFiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.IntermediateProc:bool = obj["IntermediateProc"]
      """  Identifies the journal entry as one processed by consolidation posting mode where the data transfer is immediate and an intermediate book is used.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calculated sequence number not inteneded for external use.  """  
      self.SrcCompany:str = obj["SrcCompany"]
      """  Source Company Identifier.  Identifies the company where this GLJrnDtl originated from.  """  
      self.SrcBook:str = obj["SrcBook"]
      """  Unique Book Identifier  This is the book that is being consolidated into a target book.  """  
      self.SrcGLAccount:str = obj["SrcGLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SrcJrnlCode:str = obj["SrcJrnlCode"]
      """  Source Journal Code  """  
      self.SrcJournalNum:int = obj["SrcJournalNum"]
      """  Source Journal Number  """  
      self.SrcJournalLine:int = obj["SrcJournalLine"]
      """  Source Journal Line  """  
      self.SrcType:str = obj["SrcType"]
      """   P = derived from Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.
A = derived from Advanced Allocations.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equas ABTUID which was created during posting  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  This field shows Debit value of transaction  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  This field shows Credit value of transaction  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  """  
      self.ParentRUID:str = obj["ParentRUID"]
      """  If the current line is reversal, then this field is used for link with original journal line. It equals SysRowID of original line.  """  
      self.HasReverseLine:bool = obj["HasReverseLine"]
      """  if has reverse line  """  
      self.BalanceAcct:str = obj["BalanceAcct"]
      """  This is the resolved balance account the period balance, currency balance and/or daily balance records were written under for this GL Journal Detail GL Account.  """  
      self.TrialAcct:str = obj["TrialAcct"]
      """  This is the resolved balance account the trial balance records were written under for this GL Journal Detail GL Account.  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.AllocationStamp:str = obj["AllocationStamp"]
      """  This is the last allocation stamp that affected this GLJrnDtl.  """  
      self.BatchID:str = obj["BatchID"]
      """  Identifies the allocation batch this journal entry was processed under.  """  
      self.AllocID:str = obj["AllocID"]
      """  This is the allocation id that processed this journal entry.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  The allocation run number is a unique sequential number that identifies which run of an allocation batch this journal entry was created under.  """  
      self.AllocRunNbr:int = obj["AllocRunNbr"]
      """  Intended for internal use only.  Updated by the Advanced Allocations Engine.  This identifies the last allocation run number that used this GLJrnDtl as a source record.  """  
      self.AllocTgtNbr:int = obj["AllocTgtNbr"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.AllocTgtSeq:int = obj["AllocTgtSeq"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.ExtCOACode:str = obj["ExtCOACode"]
      """  External COA Code  """  
      self.MatchCode:str = obj["MatchCode"]
      """  MatchCode is used to match two or more journal detail records together.  """  
      self.MatchDate:str = obj["MatchDate"]
      """  MatchDate is set when the journal detail record is matched to other journal detail records.  """  
      self.Reconciled:bool = obj["Reconciled"]
      """  Indicates whether or not the transaction has been flagged as reconciled.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Sequence:int = obj["Sequence"]
      """  Journal Sequence Number  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.CustNum:int = obj["CustNum"]
      """  The Internal CustNum that ties back to the Customer master file.  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  CloseFiscalPeriod  """  
      self.SourcePlant:str = obj["SourcePlant"]
      """  SourcePlant  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.ExtSysType:str = obj["ExtSysType"]
      """  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  """  
      self.ExtSysURL:str = obj["ExtSysURL"]
      """  URL for drill back to an integrated external system  """  
      self.StatAmount:int = obj["StatAmount"]
      self.BitFlag:int = obj["BitFlag"]
      self.AHGLJrnDtlAlcHedTier:int = obj["AHGLJrnDtlAlcHedTier"]
      self.StatUOMStatUOMDesc:str = obj["StatUOMStatUOMDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AHGLJrnDtlSimRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year that entry applies to.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  """  
      self.Description:str = obj["Description"]
      """  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  """  
      self.JEDate:str = obj["JEDate"]
      """  Date for this journal transaction entry.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period that this journal entry applies to.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  User ID that posted this translation.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date that this transaction was posted to the G/L files.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this entry has been posted to the G/L master balance files. Unposted entries are excluded from all G/L reports.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctId of the BankAcct master that this check was drawn  against.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number.  """  
      self.CRHeadNum:int = obj["CRHeadNum"]
      """  Cash Receipts reference field.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  """  
      self.BankTranNum:int = obj["BankTranNum"]
      """  Bank Transaction Number.  Used when a transaction is a direct transfer from one bank account to another.  """  
      self.BankSlip:str = obj["BankSlip"]
      """   The identifier of the Bank Slip document (bank statement).  The user enters a bank slip during the reconciliation process.  This is then written into the related GLJrnDtl records.
Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.ExtRefType:str = obj["ExtRefType"]
      """  Multi-Company G/L Reference Type from the external company.  This is used by the Multi-Company Journal.  """  
      self.ExtRefCode:str = obj["ExtRefCode"]
      """  Multi-Company G/L Reference Code from the external company.  This is used by the Multi-Company Journal.  """  
      self.GlbJournalNum:int = obj["GlbJournalNum"]
      """  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalLine:int = obj["GlbJournalLine"]
      """  The Journal Line assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalCode:str = obj["GlbJournalCode"]
      """  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor number.  Used by Multi-Company Journal.  """  
      self.GlbAPInvoiceNum:str = obj["GlbAPInvoiceNum"]
      """  Global AP Invoice identifier.  Used by Multi-Company Journal.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Flag to indicate that a separate journal entry will be created at the target company for the Multi-Company G/L Account entered in this journal line.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to a Multi-Company Journal.  """  
      self.CommentText:str = obj["CommentText"]
      """  Extended text to describe the journal line entry.  Defaults from GLJrnHed.CommentText.  """  
      self.GlbCompanyID:str = obj["GlbCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.GlbFiscalYear:int = obj["GlbFiscalYear"]
      """  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  """  
      self.GlbFiscalPeriod:int = obj["GlbFiscalPeriod"]
      """  Fiscal period from the external company that this journal entry applies to.  """  
      self.GlbGroupID:str = obj["GlbGroupID"]
      """  The data entry Group from the external company that the journal entry is assigned to.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.ExtGLAccount:str = obj["ExtGLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.ExtSegValue1:str = obj["ExtSegValue1"]
      """  External Segment Value 1  """  
      self.ExtSegValue2:str = obj["ExtSegValue2"]
      """  External Segment Value 2  """  
      self.ExtSegValue3:str = obj["ExtSegValue3"]
      """  External Segment Value 3  """  
      self.ExtSegValue4:str = obj["ExtSegValue4"]
      """  External Segment Value 4  """  
      self.ExtSegValue5:str = obj["ExtSegValue5"]
      """  External Segment Value 5  """  
      self.ExtSegValue6:str = obj["ExtSegValue6"]
      """  External Segment Value 6  """  
      self.ExtSegValue7:str = obj["ExtSegValue7"]
      """  External Segment Value 7  """  
      self.ExtSegValue8:str = obj["ExtSegValue8"]
      """  External Segment Value 8  """  
      self.ExtSegValue9:str = obj["ExtSegValue9"]
      """  External Segment Value 9  """  
      self.ExtSegValue10:str = obj["ExtSegValue10"]
      """  External Segment Value 10  """  
      self.ExtSegValue11:str = obj["ExtSegValue11"]
      """  External Segment Value 11  """  
      self.ExtSegValue12:str = obj["ExtSegValue12"]
      """  External Segment Value 12  """  
      self.ExtSegValue13:str = obj["ExtSegValue13"]
      """  External Segment Value 13  """  
      self.ExtSegValue14:str = obj["ExtSegValue14"]
      """  External Segment Value 14  """  
      self.ExtSegValue15:str = obj["ExtSegValue15"]
      """  External Segment Value 15  """  
      self.ExtSegValue16:str = obj["ExtSegValue16"]
      """  External Segment Value 16  """  
      self.ExtSegValue17:str = obj["ExtSegValue17"]
      """  External Segment Value 17  """  
      self.ExtSegValue18:str = obj["ExtSegValue18"]
      """  External Segment Value 18  """  
      self.ExtSegValue19:str = obj["ExtSegValue19"]
      """  External Segment Value 19  """  
      self.ExtSegValue20:str = obj["ExtSegValue20"]
      """  External Segment Value 20  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number of source document  """  
      self.SummaryBalFlag:bool = obj["SummaryBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.DetailBalFlag:bool = obj["DetailBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.DailyBalFlag:bool = obj["DailyBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GlbFiscalYearSuffix:str = obj["GlbFiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.GlbFiscalCalendarID:str = obj["GlbFiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.IntermediateProc:bool = obj["IntermediateProc"]
      """  Identifies the journal entry as one processed by consolidation posting mode where the data transfer is immediate and an intermediate book is used.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calcualted sequence number not inteneded for external use.  """  
      self.SrcCompany:str = obj["SrcCompany"]
      """  Source Company Identifier.  Identifies the company where this GLJrnDtl originated from.  """  
      self.SrcBook:str = obj["SrcBook"]
      """  Unique Book Identifier  This is the book that is being consolidated into a target book.  """  
      self.SrcGLAccount:str = obj["SrcGLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SrcJrnlCode:str = obj["SrcJrnlCode"]
      """  Source Journal Code  """  
      self.SrcJournalNum:int = obj["SrcJournalNum"]
      """  Source Journal Number  """  
      self.SrcJournalLine:int = obj["SrcJournalLine"]
      """  Source Journal Line  """  
      self.SrcType:str = obj["SrcType"]
      """   P = derived from Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equas ABTUID which was created during posting  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  This field shows Debit value of transaction  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  This field shows Credit value of transaction  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  """  
      self.ParentRUID:str = obj["ParentRUID"]
      """  If the current line is reversal, then this field is used for link with original journal line. It equals SysRowID of original line.  """  
      self.HasReverseLine:bool = obj["HasReverseLine"]
      """  if has reverse line  """  
      self.BalanceAcct:str = obj["BalanceAcct"]
      """  This is the resolved balance account the period balance, currency balance and/or daily balance records were written under for this GL Journal Detail GL Account.  """  
      self.SummaryAcct:str = obj["SummaryAcct"]
      """  This is the resolved balance account the trial balance records were written under for this GL Journal Detail GL Account.  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.AllocationStamp:str = obj["AllocationStamp"]
      """  This is the allocation stamp that processed this journal entry.  Allocation Marks are entered on an Allocation Code.  """  
      self.BatchID:str = obj["BatchID"]
      """  Identifies the allocation batch this journal entry was processed under.  """  
      self.AllocID:str = obj["AllocID"]
      """  This is the allocation id that processed this journal entry.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  The allocation run number is a unique sequential number that identifies which run of an allocation batch this journal entry was processed under.  """  
      self.AllocRunNbr:int = obj["AllocRunNbr"]
      """  Intended for internal use only.  Updated by the Advanced Allocations Engine.  This identifies the last allocation run number that used this GLJrnDtl as a source record.  """  
      self.AllocTgtNbr:int = obj["AllocTgtNbr"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.AllocTgtSeq:int = obj["AllocTgtSeq"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Internal CustNum that ties back to the Customer master file.  """  
      self.StatAmount:int = obj["StatAmount"]
      self.BitFlag:int = obj["BitFlag"]
      self.AHGLJrnDtlSimAlcHedTier:int = obj["AHGLJrnDtlSimAlcHedTier"]
      self.StatUOMStatUOMDesc:str = obj["StatUOMStatUOMDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistAcctRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.AllocGLAcct:str = obj["AllocGLAcct"]
      """  GL Account or GL Account mask  """  
      self.AllocSegValue1:str = obj["AllocSegValue1"]
      """  Allocation Segment Value 1  """  
      self.AllocSegValue2:str = obj["AllocSegValue2"]
      """  Allocation Segment Value 2  """  
      self.AllocSegValue3:str = obj["AllocSegValue3"]
      """  Allocation Segment Value 3  """  
      self.AllocSegValue4:str = obj["AllocSegValue4"]
      """  Allocation Segment Value 4  """  
      self.AllocSegValue5:str = obj["AllocSegValue5"]
      """  Allocation Segment Value 5  """  
      self.AllocSegValue6:str = obj["AllocSegValue6"]
      """  Allocation Segment Value 6  """  
      self.AllocSegValue7:str = obj["AllocSegValue7"]
      """  Allocation Segment Value 7  """  
      self.AllocSegValue8:str = obj["AllocSegValue8"]
      """  Allocation Segment Value 8  """  
      self.AllocSegValue9:str = obj["AllocSegValue9"]
      """  Allocation Segment Value 9  """  
      self.AllocSegValue10:str = obj["AllocSegValue10"]
      """  Allocation Segment Value 10  """  
      self.AllocSegValue11:str = obj["AllocSegValue11"]
      """  Allocation Segment Value 11  """  
      self.AllocSegValue12:str = obj["AllocSegValue12"]
      """  Allocation Segment Value 12  """  
      self.AllocSegValue13:str = obj["AllocSegValue13"]
      """  Allocation Segment Value 13  """  
      self.AllocSegValue14:str = obj["AllocSegValue14"]
      """  Allocation Segment Value 14  """  
      self.AllocSegValue15:str = obj["AllocSegValue15"]
      """  Allocation Segment Value 15  """  
      self.AllocSegValue16:str = obj["AllocSegValue16"]
      """  Allocation Segment Value 16  """  
      self.AllocSegValue17:str = obj["AllocSegValue17"]
      """  Allocation Segment Value 17  """  
      self.AllocSegValue18:str = obj["AllocSegValue18"]
      """  Allocation Segment Value 18  """  
      self.AllocSegValue19:str = obj["AllocSegValue19"]
      """  Allocation Segment Value 19  """  
      self.AllocSegValue20:str = obj["AllocSegValue20"]
      """  Allocation Segment Value 20  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AllocGLAcctGLShortAcct:str = obj["AllocGLAcctGLShortAcct"]
      self.AllocGLAcctAccountDesc:str = obj["AllocGLAcctAccountDesc"]
      self.AllocGLAcctGLAcctDisp:str = obj["AllocGLAcctGLAcctDisp"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistActCatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.CategoryID:str = obj["CategoryID"]
      """  Unique identifier of this category of accounts.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.AllocTgtNbr:int = obj["AllocTgtNbr"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.AllocTgtSeq:int = obj["AllocTgtSeq"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.WriteOff:bool = obj["WriteOff"]
      """  Yes indicates this record contains information about the amount written off against the source account.  NO indicates this record contains information about the amount allocated.  """  
      self.SourceInitBalance:int = obj["SourceInitBalance"]
      """  Initial balance of the write off account.  Only updated when WriteOff = yes.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SourceAccount:str = obj["SourceAccount"]
      """  Source GL Account or Balance Account.  """  
      self.TargetAccount:str = obj["TargetAccount"]
      """  Account the source amount was allocated to.  """  
      self.ResolvedAccount:str = obj["ResolvedAccount"]
      """  REsolved GL Account.  This is the same as the target account if the target account does not have any mask characters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.AllocOption:int = obj["AllocOption"]
      """  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  """  
      self.AllocUnits:int = obj["AllocUnits"]
      """   The relative  number of units used to allocate to this account.
Allocation units / Total Allocation units is used to distribute the amount. Total Allocation units are calculated for a given AllocID and not stored.  """  
      self.RatioValue:int = obj["RatioValue"]
      """  Postive, fractional value indicating how much of an allocation is applied to this target.  """  
      self.RatioFormula:str = obj["RatioFormula"]
      """  Formula entered by the user used to calculate the allocation amount.  Only valid if the allocation option = 2.  """  
      self.ResolvedFormula:str = obj["ResolvedFormula"]
      """  Resolved Formula based upon the Ratio Formula.  Only valid if the allocation option = 2.  """  
      self.ReversingEntry:bool = obj["ReversingEntry"]
      """  Yes indicates this entry is a reversing entry.  No indicates it is not a reversing entry.  """  
      self.TgtSegVal1:str = obj["TgtSegVal1"]
      """  Target Segment Value 1  """  
      self.TgtSegVal2:str = obj["TgtSegVal2"]
      """  Target Segment Value 2  """  
      self.TgtSegVal3:str = obj["TgtSegVal3"]
      """  Target Segment Value 3  """  
      self.TgtSegVal4:str = obj["TgtSegVal4"]
      """  Target Segment Value 4  """  
      self.TgtSegVal5:str = obj["TgtSegVal5"]
      """  Target Segment Value 5  """  
      self.TgtSegVal6:str = obj["TgtSegVal6"]
      """  Target Segment Value 6  """  
      self.TgtSegVal7:str = obj["TgtSegVal7"]
      """  Target Segment Value 7  """  
      self.TgtSegVal8:str = obj["TgtSegVal8"]
      """  Target Segment Value 8  """  
      self.TgtSegVal9:str = obj["TgtSegVal9"]
      """  Target Segment Value 9  """  
      self.TgtSegVal10:str = obj["TgtSegVal10"]
      """  Target Segment Value 10  """  
      self.TgtSegVal11:str = obj["TgtSegVal11"]
      """  Target Segment Value 11  """  
      self.TgtSegVal12:str = obj["TgtSegVal12"]
      """  Target Segment Value 12  """  
      self.TgtSegVal13:str = obj["TgtSegVal13"]
      """  Target Segment Value 13  """  
      self.TgtSegVal14:str = obj["TgtSegVal14"]
      """  Target Segment Value 14  """  
      self.TgtSegVal15:str = obj["TgtSegVal15"]
      """  Target Segment Value 15  """  
      self.TgtSegVal16:str = obj["TgtSegVal16"]
      """  Target Segment Value 16  """  
      self.TgtSegVal17:str = obj["TgtSegVal17"]
      """  Target Segment Value 17  """  
      self.TgtSegVal18:str = obj["TgtSegVal18"]
      """  Target Segment Value 18  """  
      self.TgtSegVal19:str = obj["TgtSegVal19"]
      """  Target Segment Value 19  """  
      self.TgtSegVal20:str = obj["TgtSegVal20"]
      """  Target Segment Value 20  """  
      self.SrcSegVal1:str = obj["SrcSegVal1"]
      """  Source Segment Value 1  """  
      self.SrcSegVal2:str = obj["SrcSegVal2"]
      """  Source Segment Value 2  """  
      self.SrcSegVal3:str = obj["SrcSegVal3"]
      """  Source Segment Value 3  """  
      self.SrcSegVal4:str = obj["SrcSegVal4"]
      """  Source Segment Value 4  """  
      self.SrcSegVal5:str = obj["SrcSegVal5"]
      """  Source Segment Value 5  """  
      self.SrcSegVal6:str = obj["SrcSegVal6"]
      """  Source Segment Value 6  """  
      self.SrcSegVal7:str = obj["SrcSegVal7"]
      """  Source Segment Value 7  """  
      self.SrcSegVal8:str = obj["SrcSegVal8"]
      """  Source Segment Value 8  """  
      self.SrcSegVal9:str = obj["SrcSegVal9"]
      """  Source Segment Value 9  """  
      self.SrcSegVal10:str = obj["SrcSegVal10"]
      """  Source Segment Value 10  """  
      self.SrcSegVal11:str = obj["SrcSegVal11"]
      """  Source Segment Value 11  """  
      self.SrcSegVal12:str = obj["SrcSegVal12"]
      """  Source Segment Value 12  """  
      self.SrcSegVal13:str = obj["SrcSegVal13"]
      """  Source Segment Value 13  """  
      self.SrcSegVal14:str = obj["SrcSegVal14"]
      """  Source Segment Value 14  """  
      self.SrcSegVal15:str = obj["SrcSegVal15"]
      """  Source Segment Value 15  """  
      self.SrcSegVal16:str = obj["SrcSegVal16"]
      """  Source Segment Value 16  """  
      self.SrcSegVal17:str = obj["SrcSegVal17"]
      """  Source Segment Value 17  """  
      self.SrcSegVal18:str = obj["SrcSegVal18"]
      """  Source Segment Value 18  """  
      self.SrcSegVal19:str = obj["SrcSegVal19"]
      """  Source Segment Value 19  """  
      self.SrcSegVal20:str = obj["SrcSegVal20"]
      """  Source Segment Value 20  """  
      self.ResSegVal1:str = obj["ResSegVal1"]
      """  Resolved Segment Value 1  """  
      self.ResSegVal2:str = obj["ResSegVal2"]
      """  Resolved Segment Value 2  """  
      self.ResSegVal3:str = obj["ResSegVal3"]
      """  Resolved Segment Value 3  """  
      self.ResSegVal4:str = obj["ResSegVal4"]
      """  Resolved Segment Value 4  """  
      self.ResSegVal5:str = obj["ResSegVal5"]
      """  Resolved Segment Value 5  """  
      self.ResSegVal6:str = obj["ResSegVal6"]
      """  Resolved Segment Value 6  """  
      self.ResSegVal7:str = obj["ResSegVal7"]
      """  Resolved Segment Value 7  """  
      self.ResSegVal8:str = obj["ResSegVal8"]
      """  Resolved Segment Value 8  """  
      self.ResSegVal9:str = obj["ResSegVal9"]
      """  Resolved Segment Value 9  """  
      self.ResSegVal10:str = obj["ResSegVal10"]
      """  Resolved Segment Value 10  """  
      self.ResSegVal11:str = obj["ResSegVal11"]
      """  Resolved Segment Value 11  """  
      self.ResSegVal12:str = obj["ResSegVal12"]
      """  Resolved Segment Value 12  """  
      self.ResSegVal13:str = obj["ResSegVal13"]
      """  Resolved Segment Value 13  """  
      self.ResSegVal14:str = obj["ResSegVal14"]
      """  Resolved Segment Value 14  """  
      self.ResSegVal15:str = obj["ResSegVal15"]
      """  Resolved Segment Value 15  """  
      self.ResSegVal16:str = obj["ResSegVal16"]
      """  Resolved Segment Value 16  """  
      self.ResSegVal17:str = obj["ResSegVal17"]
      """  Resolved Segment Value 17  """  
      self.ResSegVal18:str = obj["ResSegVal18"]
      """  Resolved Segment Value 18  """  
      self.ResSegVal19:str = obj["ResSegVal19"]
      """  Resolved Segment Value 19  """  
      self.ResSegVal20:str = obj["ResSegVal20"]
      """  Resolved Segment Value 20  """  
      self.ReverseFY:int = obj["ReverseFY"]
      """  The reversed fiscal year.  This is updated by reverse allocation run logic.  """  
      self.ReverseFYS:str = obj["ReverseFYS"]
      """   The reversed fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.
This is updated by reverse allocation run logic.  """  
      self.ReverseJournalNum:int = obj["ReverseJournalNum"]
      """   Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.
This is updated by reverse allocation run logic.  """  
      self.ReverseJournalLine:int = obj["ReverseJournalLine"]
      """   A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a
.specific Company/FiscalYear/JournalNum combination and adding 1.This is updated by reverse allocation run logic  """  
      self.SrcDebitAmount:int = obj["SrcDebitAmount"]
      """  Source amount applied to the formula/percentage during an allocation.  """  
      self.SrcCreditAmount:int = obj["SrcCreditAmount"]
      """  Source amount applied to the formula/percentage during an allocation.  """  
      self.RevEntryFY:int = obj["RevEntryFY"]
      """  The reversed entry fiscal year.  This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is created.  """  
      self.RevEntryFYS:str = obj["RevEntryFYS"]
      """   The reversed fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is created.  """  
      self.RevEntryJrnlNum:int = obj["RevEntryJrnlNum"]
      """   Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is created.  """  
      self.RevEntryJrnlLine:int = obj["RevEntryJrnlLine"]
      """   A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a .specific Company/FiscalYear/JournalNum combination and adding 1.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is created.  """  
      self.RevReverseFY:int = obj["RevReverseFY"]
      """  The reversed entry reversing fiscal year.  This is updated when an allocation batch has the reversing entry option set to yes and the reversing journal entry is reversed.  """  
      self.RevReverseFYS:str = obj["RevReverseFYS"]
      """   The reversed reversing entry fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is reversed.  """  
      self.RevReverseJrnlNum:int = obj["RevReverseJrnlNum"]
      """   Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is reversed.  """  
      self.RevReverseJrnlLine:int = obj["RevReverseJrnlLine"]
      """   A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a .specific Company/FiscalYear/JournalNum combination and adding 1.
This is updated when an allocation batch has the reversing entry option set to yes and a reversing journal entry is reversed.  """  
      self.CycleUID:int = obj["CycleUID"]
      """  Cycle unique ID.  This is not intended for external use.  """  
      self.CycleNumber:int = obj["CycleNumber"]
      """  Cycle number.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GLAccount:str = obj["GLAccount"]
      self.CreditAmount:int = obj["CreditAmount"]
      self.DebitAmount:int = obj["DebitAmount"]
      self.JEDate:str = obj["JEDate"]
      self.BitFlag:int = obj["BitFlag"]
      self.AlcHistDtlAlcHedTier:int = obj["AlcHistDtlAlcHedTier"]
      self.AlcHistDtlJrnlCdJrnlDescription:str = obj["AlcHistDtlJrnlCdJrnlDescription"]
      self.ResolvedGLAcctDispGLShortAcct:str = obj["ResolvedGLAcctDispGLShortAcct"]
      self.ResolvedGLAcctDispGLAcctDisp:str = obj["ResolvedGLAcctDispGLAcctDisp"]
      self.ResolvedGLAcctDispAccountDesc:str = obj["ResolvedGLAcctDispAccountDesc"]
      self.SourceAccountAccountDesc:str = obj["SourceAccountAccountDesc"]
      self.SourceAccountGLShortAcct:str = obj["SourceAccountGLShortAcct"]
      self.SourceAccountGLAcctDisp:str = obj["SourceAccountGLAcctDisp"]
      self.TargetAccountAccountDesc:str = obj["TargetAccountAccountDesc"]
      self.TargetAccountGLShortAcct:str = obj["TargetAccountGLShortAcct"]
      self.TargetAccountGLAcctDisp:str = obj["TargetAccountGLAcctDisp"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistJrnCdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Unique identifier of the journal used to group entries. The user can create their own journal codes to be used instead of the default codes.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.JrnlCodeJrnlDescription:str = obj["JrnlCodeJrnlDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.RunDate:str = obj["RunDate"]
      """  Date the batch was run.  """  
      self.RunTime:int = obj["RunTime"]
      """  Time the allocaiton batch run started.  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.Simulation:bool = obj["Simulation"]
      """  Indicates if this is simulation history record or General Ledger history record.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date for journal transactions.  """  
      self.ApplyDateRev:str = obj["ApplyDateRev"]
      """  Date used for reversing entries.  """  
      self.StartDate:str = obj["StartDate"]
      """  Starting date for record selection.  Defaults to the fiscal period start date.  """  
      self.EndDate:str = obj["EndDate"]
      """  Ending date for record seletion.  Defaults to fiscal period end date.  """  
      self.SchedDate:str = obj["SchedDate"]
      """  Date when the allocation batch is due to be run.  """  
      self.BatchDesc:str = obj["BatchDesc"]
      """  Batch Description  """  
      self.Tier:int = obj["Tier"]
      """  Allocation tier.  """  
      self.SchedNum:int = obj["SchedNum"]
      """  Internal next number used to keep the schedule records unique.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates whether or not reversing transactions are generated at the time a journal entry is allocated.  Yes indicates reversing entries are generated.  No indicates reversing entries are not generated.  """  
      self.YTDAlloc:bool = obj["YTDAlloc"]
      """  Indicates if the allocation run started at the beginning of the current fiscal year.  """  
      self.AllocReversed:bool = obj["AllocReversed"]
      """  Indicates if the allocation run has been reversed.  """  
      self.PriorTgtStamp:str = obj["PriorTgtStamp"]
      """  Identifies the allocation stamp to which this allocation is to be applied.  """  
      self.TgtStamp:str = obj["TgtStamp"]
      """  Identifies the allocation stamp that is to to be stamped on the GLJrnDtls.  """  
      self.SrcAllocStamp:str = obj["SrcAllocStamp"]
      """  Identifies the allocation stamp that was processed by this allocation.  """  
      self.IgnoreStamp:bool = obj["IgnoreStamp"]
      """  When Yes the Allocation Engine ignores the allocation stamp assigned to the GLJrnDtl when determining if a entry is subject to allocations for the current allocation code.  """  
      self.UseAllStamps:bool = obj["UseAllStamps"]
      """  Yes indicates that all allocation stamps are valid for the allocation code.  """  
      self.AllocOption:int = obj["AllocOption"]
      """  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  """  
      self.PercentToAlloc:int = obj["PercentToAlloc"]
      """  Postive, fractional value indicating how much of a source is allocated.  Default value is 100.00.  """  
      self.UseAllocUnits:bool = obj["UseAllocUnits"]
      """  Indicates if the allocation units are used.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RunTypeDesc:str = obj["RunTypeDesc"]
      self.AlcHistFiscalCalDescription:str = obj["AlcHistFiscalCalDescription"]
      """  Calendar description.  """  
      self.AlcHistGLBookCurrencyCode:str = obj["AlcHistGLBookCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.AlcHistGLBookDescription:str = obj["AlcHistGLBookDescription"]
      """  Descripiton of Book  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistListTableset:
   def __init__(self, obj):
      self.AlcHistList:list[Erp_Tablesets_AlcHistListRow] = obj["AlcHistList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_AlcHistNFSrcRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique. The value of ParamNbr identifies the parameter number the record is defined for.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.LookupTblMapUID_obsolete:int = obj["LookupTblMapUID_obsolete"]
      """  LookupTblMapUID_obsolete  """  
      self.TgtSeqNbr_obsolete:int = obj["TgtSeqNbr_obsolete"]
      """  TgtSeqNbr_obsolete  """  
      self.LinkUID_obsolete:int = obj["LinkUID_obsolete"]
      """  LinkUID_obsolete  """  
      self.SrcFieldName:str = obj["SrcFieldName"]
      """  Source field name.  """  
      self.ParamOpt:int = obj["ParamOpt"]
      """   Identifes the option for the non-financial parameter.
1 = Use Target Account Segment.  
2 = Use Source Account Segment
3 = Use Allocation Run Start Date
4 = Use allocation Run End Date  """  
      self.ParamSegmentNbr:int = obj["ParamSegmentNbr"]
      """  Identifies the segment number to use to determine the segment code that will be used to look up the result value in the lookup table.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.EntryType:int = obj["EntryType"]
      """  Identifies if the parameter is an actual value or an option.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SrcSeqNbr:int = obj["SrcSeqNbr"]
      """  SrcSeqNbr  """  
      self.SrcCodeID:str = obj["SrcCodeID"]
      """  SrcCodeID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistParamsBAQRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique.  """  
      self.BAQExportID:str = obj["BAQExportID"]
      """  BAQ ID, the unique identifier for this Query table within the company  """  
      self.BAQParamValNbr:int = obj["BAQParamValNbr"]
      """  Intended for internal use only to keep the records unique.  """  
      self.ParameterName:str = obj["ParameterName"]
      self.BAQParamCode:str = obj["BAQParamCode"]
      """  Specific baq parameter value.  """  
      self.ParamOpt:int = obj["ParamOpt"]
      """   Identifes the option for the non-financial parameter.
1 = Use Target Account Segment.  
2 = Use Source Account Segment
3 = Use Allocation Run Start Date
4 = Use allocation Run End Date  """  
      self.ParamSegmentNbr:int = obj["ParamSegmentNbr"]
      """  Identifies the segment number to use to determine the segment code that will be used to look up the result value in the lookup table.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.EntryType:int = obj["EntryType"]
      """  Identifies if the parameter is an actual value or an option.  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistParamsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.ParamName:str = obj["ParamName"]
      """  The name assigned to a parameter.  This name must be unique.  """  
      self.ParamType:int = obj["ParamType"]
      """  Identifies the type of parameter used in the allocation logic.  1 = Account Balances, 2 = Summarized balances and 3 = BAQ.  """  
      self.ParamDesc:str = obj["ParamDesc"]
      """  Text that describes the parameter.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.AcctBalAcct:str = obj["AcctBalAcct"]
      """  Account balance account.  Only valid when the formula type = 1.  """  
      self.AcctBalSegVal1:str = obj["AcctBalSegVal1"]
      """  Account Segment Value 1  """  
      self.AcctBalSegVal2:str = obj["AcctBalSegVal2"]
      """  Account Segment Value 2  """  
      self.AcctBalSegVal3:str = obj["AcctBalSegVal3"]
      """  Account Segment Value 3  """  
      self.AcctBalSegVal4:str = obj["AcctBalSegVal4"]
      """  Account Segment Value 4  """  
      self.AcctBalSegVal5:str = obj["AcctBalSegVal5"]
      """  Account Segment Value 5  """  
      self.AcctBalSegVal6:str = obj["AcctBalSegVal6"]
      """  Account Segment Value 6  """  
      self.AcctBalSegVal7:str = obj["AcctBalSegVal7"]
      """  Account Segment Value 7  """  
      self.AcctBalSegVal8:str = obj["AcctBalSegVal8"]
      """  Account Segment Value 8  """  
      self.AcctBalSegVal9:str = obj["AcctBalSegVal9"]
      """  Account Segment Value 9  """  
      self.AcctBalSegVal10:str = obj["AcctBalSegVal10"]
      """  Account Segment Value 10  """  
      self.AcctBalSegVal11:str = obj["AcctBalSegVal11"]
      """  Account Segment Value 11  """  
      self.AcctBalSegVal12:str = obj["AcctBalSegVal12"]
      """  Account Segment Value 12  """  
      self.AcctBalSegVal13:str = obj["AcctBalSegVal13"]
      """  Account Segment Value 13  """  
      self.AcctBalSegVal14:str = obj["AcctBalSegVal14"]
      """  Account Segment Value 14  """  
      self.AcctBalSegVal15:str = obj["AcctBalSegVal15"]
      """  Account Segment Value 15  """  
      self.AcctBalSegVal16:str = obj["AcctBalSegVal16"]
      """  Account Segment Value 16  """  
      self.AcctBalSegVal17:str = obj["AcctBalSegVal17"]
      """  Account Segment Value 17  """  
      self.AcctBalSegVal18:str = obj["AcctBalSegVal18"]
      """  Account Segment Value 18  """  
      self.AcctBalSegVal19:str = obj["AcctBalSegVal19"]
      """  Account Segment Value 19  """  
      self.AcctBalSegVal20:str = obj["AcctBalSegVal20"]
      """  Account Segment Value 20  """  
      self.UseTgtAcct:bool = obj["UseTgtAcct"]
      """  Yes indictes the target account's balance is taken and the AcctBalAcct is set equal to the AlcTarget.TgtGLAcct.  This only only valid when the formula type = Account Balances.  """  
      self.BAQExportID:str = obj["BAQExportID"]
      """  BAQ  ID, the unique identifier for the query table within the company  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.AcctParamValSrc:int = obj["AcctParamValSrc"]
      """  Indicates the source data for the value of a parameter value when the parameter is of type Account Balance.  """  
      self.SumParamValSrc:int = obj["SumParamValSrc"]
      """  Indicates the source data for the value of a parameter value when the parameter is of type Summarized.  """  
      self.Reversed:bool = obj["Reversed"]
      """  Indicates if the allocation run was reversed.  """  
      self.ReversedDate:str = obj["ReversedDate"]
      """  Date used to reverse the allocation run.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NFSrcMapUID:int = obj["NFSrcMapUID"]
      """  NFSrcMapUID  """  
      self.NFTgtSeqNbr:int = obj["NFTgtSeqNbr"]
      """  NFTgtSeqNbr  """  
      self.YTDBalance:bool = obj["YTDBalance"]
      """  YTDBalance  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AcctBalAcctGLAcctDispAccountDesc:str = obj["AcctBalAcctGLAcctDispAccountDesc"]
      self.AcctBalAcctGLAcctDispGLShortAcct:str = obj["AcctBalAcctGLAcctDispGLShortAcct"]
      self.AcctBalAcctGLAcctDispGLAcctDisp:str = obj["AcctBalAcctGLAcctDispGLAcctDisp"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistRangeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.MinValue:str = obj["MinValue"]
      """  Minimum vale for range selection.  """  
      self.MaxValue:str = obj["MaxValue"]
      """  Maximum value for range selection.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COASegmentSegmentName:str = obj["COASegmentSegmentName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistResParamsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.AllocTgtNbr:int = obj["AllocTgtNbr"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.AllocTgtSeq:int = obj["AllocTgtSeq"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique.  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.ActualValue:int = obj["ActualValue"]
      """  Actual calculated value.  """  
      self.ResBalAcct:str = obj["ResBalAcct"]
      """  Account balance account.  Only valid when the formula type = 1.  This is the gl account with all mask characters resolved.  """  
      self.ResBalSegVal1:str = obj["ResBalSegVal1"]
      """  Resolved  Segment Value 1  """  
      self.ResBalSegVal2:str = obj["ResBalSegVal2"]
      """  Resolved  Segment Value 2  """  
      self.ResBalSegVal3:str = obj["ResBalSegVal3"]
      """  Resolved  Segment Value 3  """  
      self.ResBalSegVal4:str = obj["ResBalSegVal4"]
      """  Resolved Segment Value 4  """  
      self.ResBalSegVal5:str = obj["ResBalSegVal5"]
      """  Resolved  Segment Value 5  """  
      self.ResBalSegVal6:str = obj["ResBalSegVal6"]
      """  Resolved  Segment Value 6  """  
      self.ResBalSegVal7:str = obj["ResBalSegVal7"]
      """  Resolved Segment Value 7  """  
      self.ResBalSegVal8:str = obj["ResBalSegVal8"]
      """  Resolved  Segment Value 8  """  
      self.ResBalSegVal9:str = obj["ResBalSegVal9"]
      """  Resolved  Segment Value 9  """  
      self.ResBalSegVal10:str = obj["ResBalSegVal10"]
      """  Resolved Segment Value 10  """  
      self.ResBalSegVal11:str = obj["ResBalSegVal11"]
      """  Resolved Segment Value 11  """  
      self.ResBalSegVal12:str = obj["ResBalSegVal12"]
      """  Resolved  Segment Value 12  """  
      self.ResBalSegVal13:str = obj["ResBalSegVal13"]
      """  Resolved  Segment Value 13  """  
      self.ResBalSegVal14:str = obj["ResBalSegVal14"]
      """  Resolved  Segment Value 14  """  
      self.ResBalSegVal15:str = obj["ResBalSegVal15"]
      """  Resolved Segment Value 15  """  
      self.ResBalSegVal16:str = obj["ResBalSegVal16"]
      """  Resolved  Segment Value 16  """  
      self.ResBalSegVal17:str = obj["ResBalSegVal17"]
      """  Resolved  Segment Value 17  """  
      self.ResBalSegVal18:str = obj["ResBalSegVal18"]
      """  Resolved  Segment Value 18  """  
      self.ResBalSegVal19:str = obj["ResBalSegVal19"]
      """  Resolved Segment Value 19  """  
      self.ResBalSegVal20:str = obj["ResBalSegVal20"]
      """  Resolved  Segment Value 20  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.CycleUID:int = obj["CycleUID"]
      """  Cycle unique ID.  This is not intended for external use.  """  
      self.CycleNumber:int = obj["CycleNumber"]
      """  Cycle number.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.YTDBalance:bool = obj["YTDBalance"]
      """  YTDBalance  """  
      self.AcctBalAcct:str = obj["AcctBalAcct"]
      self.UseTgtAcct:bool = obj["UseTgtAcct"]
      self.BAQExportID:str = obj["BAQExportID"]
      self.AcctParamValSrc:int = obj["AcctParamValSrc"]
      self.SumParamValSrc:int = obj["SumParamValSrc"]
      self.TgtGLAcct:str = obj["TgtGLAcct"]
      self.BitFlag:int = obj["BitFlag"]
      self.AlcHistParamsParamType:int = obj["AlcHistParamsParamType"]
      self.AlcHistParamsAcctParamValSrc:int = obj["AlcHistParamsAcctParamValSrc"]
      self.AlcHistParamsUseTgtAcct:bool = obj["AlcHistParamsUseTgtAcct"]
      self.AlcHistParamsParamName:str = obj["AlcHistParamsParamName"]
      self.AlcHistParamsSumParamValSrc:int = obj["AlcHistParamsSumParamValSrc"]
      self.AlcHistParamsBAQExportID:str = obj["AlcHistParamsBAQExportID"]
      self.AlcHistParamsAcctBalAcct:str = obj["AlcHistParamsAcctBalAcct"]
      self.AlcHistParamsParamDesc:str = obj["AlcHistParamsParamDesc"]
      self.ResAcctDispGLShortAcct:str = obj["ResAcctDispGLShortAcct"]
      self.ResAcctDispGLAcctDisp:str = obj["ResAcctDispGLAcctDisp"]
      self.ResAcctDispAccountDesc:str = obj["ResAcctDispAccountDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistResParamsSimRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.AllocTgtNbr:int = obj["AllocTgtNbr"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.AllocTgtSeq:int = obj["AllocTgtSeq"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique.  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.ActualValue:int = obj["ActualValue"]
      """  Actual calculated value.  """  
      self.ResBalAcct:str = obj["ResBalAcct"]
      """  Account balance account.  Only valid when the formula type = 1.  This is the gl account with all mask characters resolved.  """  
      self.ResBalSegVal1:str = obj["ResBalSegVal1"]
      """  Resolved  Segment Value 1  """  
      self.ResBalSegVal2:str = obj["ResBalSegVal2"]
      """  Resolved  Segment Value 2  """  
      self.ResBalSegVal3:str = obj["ResBalSegVal3"]
      """  Resolved  Segment Value 3  """  
      self.ResBalSegVal4:str = obj["ResBalSegVal4"]
      """  Resolved Segment Value 4  """  
      self.ResBalSegVal5:str = obj["ResBalSegVal5"]
      """  Resolved  Segment Value 5  """  
      self.ResBalSegVal6:str = obj["ResBalSegVal6"]
      """  Resolved  Segment Value 6  """  
      self.ResBalSegVal7:str = obj["ResBalSegVal7"]
      """  Resolved Segment Value 7  """  
      self.ResBalSegVal8:str = obj["ResBalSegVal8"]
      """  Resolved  Segment Value 8  """  
      self.ResBalSegVal9:str = obj["ResBalSegVal9"]
      """  Resolved  Segment Value 9  """  
      self.ResBalSegVal10:str = obj["ResBalSegVal10"]
      """  Resolved Segment Value 10  """  
      self.ResBalSegVal11:str = obj["ResBalSegVal11"]
      """  Resolved Segment Value 11  """  
      self.ResBalSegVal12:str = obj["ResBalSegVal12"]
      """  Resolved  Segment Value 12  """  
      self.ResBalSegVal13:str = obj["ResBalSegVal13"]
      """  Resolved  Segment Value 13  """  
      self.ResBalSegVal14:str = obj["ResBalSegVal14"]
      """  Resolved  Segment Value 14  """  
      self.ResBalSegVal15:str = obj["ResBalSegVal15"]
      """  Resolved Segment Value 15  """  
      self.ResBalSegVal16:str = obj["ResBalSegVal16"]
      """  Resolved  Segment Value 16  """  
      self.ResBalSegVal17:str = obj["ResBalSegVal17"]
      """  Resolved  Segment Value 17  """  
      self.ResBalSegVal18:str = obj["ResBalSegVal18"]
      """  Resolved  Segment Value 18  """  
      self.ResBalSegVal19:str = obj["ResBalSegVal19"]
      """  Resolved Segment Value 19  """  
      self.ResBalSegVal20:str = obj["ResBalSegVal20"]
      """  Resolved  Segment Value 20  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.CycleUID:int = obj["CycleUID"]
      """  Cycle unique ID.  This is not intended for external use.  """  
      self.CycleNumber:int = obj["CycleNumber"]
      """  Cycle number.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.YTDBalance:bool = obj["YTDBalance"]
      """  YTDBalance  """  
      self.TgtGLAcct:str = obj["TgtGLAcct"]
      self.BitFlag:int = obj["BitFlag"]
      self.AlcHistParamsSimSumParamValSrc:int = obj["AlcHistParamsSimSumParamValSrc"]
      self.AlcHistParamsSimParamName:str = obj["AlcHistParamsSimParamName"]
      self.AlcHistParamsSimParamType:int = obj["AlcHistParamsSimParamType"]
      self.AlcHistParamsSimAcctBalAcct:str = obj["AlcHistParamsSimAcctBalAcct"]
      self.AlcHistParamsSimParamDesc:str = obj["AlcHistParamsSimParamDesc"]
      self.AlcHistParamsSimUseTgtAcct:bool = obj["AlcHistParamsSimUseTgtAcct"]
      self.AlcHistParamsSimAcctParamValSrc:int = obj["AlcHistParamsSimAcctParamValSrc"]
      self.ResAcctDispSimGLAcctDisp:str = obj["ResAcctDispSimGLAcctDisp"]
      self.ResAcctDispSimGLShortAcct:str = obj["ResAcctDispSimGLShortAcct"]
      self.ResAcctDispSimAccountDesc:str = obj["ResAcctDispSimAccountDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.RunDate:str = obj["RunDate"]
      """  Date the batch was run.  """  
      self.RunTime:int = obj["RunTime"]
      """  Time the allocaiton batch run started.  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.Simulation:bool = obj["Simulation"]
      """  Indicates if this is simulation history record or General Ledger history record.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date for journal transactions.  """  
      self.ApplyDateRev:str = obj["ApplyDateRev"]
      """  Date used for reversing entries.  """  
      self.StartDate:str = obj["StartDate"]
      """  Starting date for record selection.  Defaults to the fiscal period start date.  """  
      self.EndDate:str = obj["EndDate"]
      """  Ending date for record seletion.  Defaults to fiscal period end date.  """  
      self.SchedDate:str = obj["SchedDate"]
      """  Date when the allocation batch is due to be run.  """  
      self.BatchDesc:str = obj["BatchDesc"]
      """  Batch Description  """  
      self.Tier:int = obj["Tier"]
      """  Allocation tier.  """  
      self.SchedNum:int = obj["SchedNum"]
      """  Internal next number used to keep the schedule records unique.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates whether or not reversing transactions are generated at the time a journal entry is allocated.  Yes indicates reversing entries are generated.  No indicates reversing entries are not generated.  """  
      self.YTDAlloc:bool = obj["YTDAlloc"]
      """  Indicates if the allocation run started at the beginning of the current fiscal year.  """  
      self.AllocReversed:bool = obj["AllocReversed"]
      """  Indicates if the allocation run has been reversed.  """  
      self.PriorTgtStamp:str = obj["PriorTgtStamp"]
      """  Identifies the allocation stamp to which this allocation is to be applied.  """  
      self.TgtStamp:str = obj["TgtStamp"]
      """  Identifies the allocation stamp that is to to be stamped on the GLJrnDtls.  """  
      self.SrcAllocStamp:str = obj["SrcAllocStamp"]
      """  Identifies the allocation stamp that was processed by this allocation.  """  
      self.IgnoreStamp:bool = obj["IgnoreStamp"]
      """  When Yes the Allocation Engine ignores the allocation stamp assigned to the GLJrnDtl when determining if a entry is subject to allocations for the current allocation code.  """  
      self.UseAllStamps:bool = obj["UseAllStamps"]
      """  Yes indicates that all allocation stamps are valid for the allocation code.  """  
      self.AllocOption:int = obj["AllocOption"]
      """  Identifies how allocations are applied.  1 = Fixed ratio value.  2 = Formula.  """  
      self.PercentToAlloc:int = obj["PercentToAlloc"]
      """  Postive, fractional value indicating how much of a source is allocated.  Default value is 100.00.  """  
      self.UseAllocUnits:bool = obj["UseAllocUnits"]
      """  Indicates if the allocation units are used.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.StatBalAsAllocUnits:bool = obj["StatBalAsAllocUnits"]
      """  StatBalAsAllocUnits  """  
      self.RunTypeDesc:str = obj["RunTypeDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.AlcHistFiscalCalDescription:str = obj["AlcHistFiscalCalDescription"]
      self.AlcHistGLBookCurrencyCode:str = obj["AlcHistGLBookCurrencyCode"]
      self.AlcHistGLBookDescription:str = obj["AlcHistGLBookDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistoryFilterRow:
   def __init__(self, obj):
      self.BookID:str = obj["BookID"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.StartPeriod:int = obj["StartPeriod"]
      self.EndPeriod:int = obj["EndPeriod"]
      self.RunType:int = obj["RunType"]
      self.RunTypeDesc:str = obj["RunTypeDesc"]
      self.BookDesc:str = obj["BookDesc"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlcHistoryFilterTableset:
   def __init__(self, obj):
      self.AlcHistoryFilter:list[Erp_Tablesets_AlcHistoryFilterRow] = obj["AlcHistoryFilter"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_AlcHistoryTableset:
   def __init__(self, obj):
      self.AlcHist:list[Erp_Tablesets_AlcHistRow] = obj["AlcHist"]
      self.AHGLJrnDtl:list[Erp_Tablesets_AHGLJrnDtlRow] = obj["AHGLJrnDtl"]
      self.AlcHistResParams:list[Erp_Tablesets_AlcHistResParamsRow] = obj["AlcHistResParams"]
      self.AHGLJrnDtlSim:list[Erp_Tablesets_AHGLJrnDtlSimRow] = obj["AHGLJrnDtlSim"]
      self.AlcHistResParamsSim:list[Erp_Tablesets_AlcHistResParamsSimRow] = obj["AlcHistResParamsSim"]
      self.AlcHistAcct:list[Erp_Tablesets_AlcHistAcctRow] = obj["AlcHistAcct"]
      self.AlcHistActCat:list[Erp_Tablesets_AlcHistActCatRow] = obj["AlcHistActCat"]
      self.AlcHistDtl:list[Erp_Tablesets_AlcHistDtlRow] = obj["AlcHistDtl"]
      self.AlcHistJrnCd:list[Erp_Tablesets_AlcHistJrnCdRow] = obj["AlcHistJrnCd"]
      self.AlcHistParams:list[Erp_Tablesets_AlcHistParamsRow] = obj["AlcHistParams"]
      self.AlcHistParamsBAQ:list[Erp_Tablesets_AlcHistParamsBAQRow] = obj["AlcHistParamsBAQ"]
      self.AlcHistNFSrc:list[Erp_Tablesets_AlcHistNFSrcRow] = obj["AlcHistNFSrc"]
      self.PAlcHistAcct:list[Erp_Tablesets_PAlcHistAcctRow] = obj["PAlcHistAcct"]
      self.PAlcHistActCat:list[Erp_Tablesets_PAlcHistActCatRow] = obj["PAlcHistActCat"]
      self.PAlcHistJrnCd:list[Erp_Tablesets_PAlcHistJrnCdRow] = obj["PAlcHistJrnCd"]
      self.PAlcHistRange:list[Erp_Tablesets_PAlcHistRangeRow] = obj["PAlcHistRange"]
      self.AlcHistRange:list[Erp_Tablesets_AlcHistRangeRow] = obj["AlcHistRange"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PAlcHistAcctRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.AllocGLAcct:str = obj["AllocGLAcct"]
      """  GL Account or GL Account mask  """  
      self.AllocSegValue1:str = obj["AllocSegValue1"]
      """  Allocation Segment Value 1  """  
      self.AllocSegValue2:str = obj["AllocSegValue2"]
      """  Allocation Segment Value 2  """  
      self.AllocSegValue3:str = obj["AllocSegValue3"]
      """  Allocation Segment Value 3  """  
      self.AllocSegValue4:str = obj["AllocSegValue4"]
      """  Allocation Segment Value 4  """  
      self.AllocSegValue5:str = obj["AllocSegValue5"]
      """  Allocation Segment Value 5  """  
      self.AllocSegValue6:str = obj["AllocSegValue6"]
      """  Allocation Segment Value 6  """  
      self.AllocSegValue7:str = obj["AllocSegValue7"]
      """  Allocation Segment Value 7  """  
      self.AllocSegValue8:str = obj["AllocSegValue8"]
      """  Allocation Segment Value 8  """  
      self.AllocSegValue9:str = obj["AllocSegValue9"]
      """  Allocation Segment Value 9  """  
      self.AllocSegValue10:str = obj["AllocSegValue10"]
      """  Allocation Segment Value 10  """  
      self.AllocSegValue11:str = obj["AllocSegValue11"]
      """  Allocation Segment Value 11  """  
      self.AllocSegValue12:str = obj["AllocSegValue12"]
      """  Allocation Segment Value 12  """  
      self.AllocSegValue13:str = obj["AllocSegValue13"]
      """  Allocation Segment Value 13  """  
      self.AllocSegValue14:str = obj["AllocSegValue14"]
      """  Allocation Segment Value 14  """  
      self.AllocSegValue15:str = obj["AllocSegValue15"]
      """  Allocation Segment Value 15  """  
      self.AllocSegValue16:str = obj["AllocSegValue16"]
      """  Allocation Segment Value 16  """  
      self.AllocSegValue17:str = obj["AllocSegValue17"]
      """  Allocation Segment Value 17  """  
      self.AllocSegValue18:str = obj["AllocSegValue18"]
      """  Allocation Segment Value 18  """  
      self.AllocSegValue19:str = obj["AllocSegValue19"]
      """  Allocation Segment Value 19  """  
      self.AllocSegValue20:str = obj["AllocSegValue20"]
      """  Allocation Segment Value 20  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PAllocGLAccountGLAcctDisp:str = obj["PAllocGLAccountGLAcctDisp"]
      self.PAllocGLAccountGLShortAcct:str = obj["PAllocGLAccountGLShortAcct"]
      self.PAllocGLAccountAccountDesc:str = obj["PAllocGLAccountAccountDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PAlcHistActCatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.CategoryID:str = obj["CategoryID"]
      """  Unique identifier of this category of accounts.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PAlcHistJrnCdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Unique identifier of the journal used to group entries. The user can create their own journal codes to be used instead of the default codes.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PHistJrnlCodeJrnlDescription:str = obj["PHistJrnlCodeJrnlDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PAlcHistRangeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BatchID:str = obj["BatchID"]
      """  The batch code is the identifier of a group of allocation codes scheduled to run together.  """  
      self.AllocID:str = obj["AllocID"]
      """  Allocation Code.  """  
      self.ParamNbr:int = obj["ParamNbr"]
      """  Intended for internal use only to keep the records unique. Source selection criteria are identified by a 0.  Parameter selection criteria have a parameter number equal to the parameter they are defined for.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  System generated next number used to keep data unique for allocation batch runs.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.RunType:int = obj["RunType"]
      """  1 = General Ledger, 2 = Simulation  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.MinValue:str = obj["MinValue"]
      """  Minimum vale for range selection.  """  
      self.MaxValue:str = obj["MaxValue"]
      """  Maximum value for range selection.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PCOASegmentSegmentName:str = obj["PCOASegmentSegmentName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtAlcHistoryTableset:
   def __init__(self, obj):
      self.AlcHist:list[Erp_Tablesets_AlcHistRow] = obj["AlcHist"]
      self.AHGLJrnDtl:list[Erp_Tablesets_AHGLJrnDtlRow] = obj["AHGLJrnDtl"]
      self.AlcHistResParams:list[Erp_Tablesets_AlcHistResParamsRow] = obj["AlcHistResParams"]
      self.AHGLJrnDtlSim:list[Erp_Tablesets_AHGLJrnDtlSimRow] = obj["AHGLJrnDtlSim"]
      self.AlcHistResParamsSim:list[Erp_Tablesets_AlcHistResParamsSimRow] = obj["AlcHistResParamsSim"]
      self.AlcHistAcct:list[Erp_Tablesets_AlcHistAcctRow] = obj["AlcHistAcct"]
      self.AlcHistActCat:list[Erp_Tablesets_AlcHistActCatRow] = obj["AlcHistActCat"]
      self.AlcHistDtl:list[Erp_Tablesets_AlcHistDtlRow] = obj["AlcHistDtl"]
      self.AlcHistJrnCd:list[Erp_Tablesets_AlcHistJrnCdRow] = obj["AlcHistJrnCd"]
      self.AlcHistParams:list[Erp_Tablesets_AlcHistParamsRow] = obj["AlcHistParams"]
      self.AlcHistParamsBAQ:list[Erp_Tablesets_AlcHistParamsBAQRow] = obj["AlcHistParamsBAQ"]
      self.AlcHistNFSrc:list[Erp_Tablesets_AlcHistNFSrcRow] = obj["AlcHistNFSrc"]
      self.PAlcHistAcct:list[Erp_Tablesets_PAlcHistAcctRow] = obj["PAlcHistAcct"]
      self.PAlcHistActCat:list[Erp_Tablesets_PAlcHistActCatRow] = obj["PAlcHistActCat"]
      self.PAlcHistJrnCd:list[Erp_Tablesets_PAlcHistJrnCdRow] = obj["PAlcHistJrnCd"]
      self.PAlcHistRange:list[Erp_Tablesets_PAlcHistRangeRow] = obj["PAlcHistRange"]
      self.AlcHistRange:list[Erp_Tablesets_AlcHistRangeRow] = obj["AlcHistRange"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByBatchIDRunNbr_input:
   """ Required : 
   batchID
   runNbr
   """  
   def __init__(self, obj):
      self.batchID:str = obj["batchID"]
      self.runNbr:int = obj["runNbr"]
      pass

class GetByBatchIDRunNbr_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AlcHistoryTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   batchID
   runNbr
   allocID
   """  
   def __init__(self, obj):
      self.batchID:str = obj["batchID"]
      self.runNbr:int = obj["runNbr"]
      self.allocID:str = obj["allocID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AlcHistoryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AlcHistoryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AlcHistoryTableset] = obj["returnObj"]
      pass

class GetListByBatchID_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Whereclause.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetListByBatchID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AlcHistListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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
      self.returnObj:list[Erp_Tablesets_AlcHistListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewAHGLJrnDtlSim_input:
   """ Required : 
   ds
   batchID
   runNbr
   allocID
   allocTgtNbr
   allocTgtSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      self.batchID:str = obj["batchID"]
      self.runNbr:int = obj["runNbr"]
      self.allocID:str = obj["allocID"]
      self.allocTgtNbr:int = obj["allocTgtNbr"]
      self.allocTgtSeq:int = obj["allocTgtSeq"]
      pass

class GetNewAHGLJrnDtlSim_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAHGLJrnDtl_input:
   """ Required : 
   ds
   batchID
   runNbr
   allocID
   allocTgtNbr
   allocTgtSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      self.batchID:str = obj["batchID"]
      self.runNbr:int = obj["runNbr"]
      self.allocID:str = obj["allocID"]
      self.allocTgtNbr:int = obj["allocTgtNbr"]
      self.allocTgtSeq:int = obj["allocTgtSeq"]
      pass

class GetNewAHGLJrnDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcHistAcct_input:
   """ Required : 
   ds
   batchID
   runNbr
   allocID
   paramNbr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      self.batchID:str = obj["batchID"]
      self.runNbr:int = obj["runNbr"]
      self.allocID:str = obj["allocID"]
      self.paramNbr:int = obj["paramNbr"]
      pass

class GetNewAlcHistAcct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcHistActCat_input:
   """ Required : 
   ds
   batchID
   runNbr
   allocID
   paramNbr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      self.batchID:str = obj["batchID"]
      self.runNbr:int = obj["runNbr"]
      self.allocID:str = obj["allocID"]
      self.paramNbr:int = obj["paramNbr"]
      pass

class GetNewAlcHistActCat_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcHistDtl_input:
   """ Required : 
   ds
   batchID
   runNbr
   allocID
   allocTgtNbr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      self.batchID:str = obj["batchID"]
      self.runNbr:int = obj["runNbr"]
      self.allocID:str = obj["allocID"]
      self.allocTgtNbr:int = obj["allocTgtNbr"]
      pass

class GetNewAlcHistDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcHistJrnCd_input:
   """ Required : 
   ds
   batchID
   runNbr
   allocID
   paramNbr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      self.batchID:str = obj["batchID"]
      self.runNbr:int = obj["runNbr"]
      self.allocID:str = obj["allocID"]
      self.paramNbr:int = obj["paramNbr"]
      pass

class GetNewAlcHistJrnCd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcHistNFSrc_input:
   """ Required : 
   ds
   batchID
   runNbr
   allocID
   paramNbr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      self.batchID:str = obj["batchID"]
      self.runNbr:int = obj["runNbr"]
      self.allocID:str = obj["allocID"]
      self.paramNbr:int = obj["paramNbr"]
      pass

class GetNewAlcHistNFSrc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcHistParamsBAQ_input:
   """ Required : 
   ds
   batchID
   runNbr
   allocID
   paramNbr
   baQExportID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      self.batchID:str = obj["batchID"]
      self.runNbr:int = obj["runNbr"]
      self.allocID:str = obj["allocID"]
      self.paramNbr:int = obj["paramNbr"]
      self.baQExportID:str = obj["baQExportID"]
      pass

class GetNewAlcHistParamsBAQ_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcHistParams_input:
   """ Required : 
   ds
   batchID
   runNbr
   allocID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      self.batchID:str = obj["batchID"]
      self.runNbr:int = obj["runNbr"]
      self.allocID:str = obj["allocID"]
      pass

class GetNewAlcHistParams_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcHistRange_input:
   """ Required : 
   ds
   batchID
   runNbr
   allocID
   paramNbr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      self.batchID:str = obj["batchID"]
      self.runNbr:int = obj["runNbr"]
      self.allocID:str = obj["allocID"]
      self.paramNbr:int = obj["paramNbr"]
      pass

class GetNewAlcHistRange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcHistResParamsSim_input:
   """ Required : 
   ds
   batchID
   runNbr
   allocID
   allocTgtNbr
   allocTgtSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      self.batchID:str = obj["batchID"]
      self.runNbr:int = obj["runNbr"]
      self.allocID:str = obj["allocID"]
      self.allocTgtNbr:int = obj["allocTgtNbr"]
      self.allocTgtSeq:int = obj["allocTgtSeq"]
      pass

class GetNewAlcHistResParamsSim_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcHistResParams_input:
   """ Required : 
   ds
   batchID
   runNbr
   allocID
   allocTgtNbr
   allocTgtSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      self.batchID:str = obj["batchID"]
      self.runNbr:int = obj["runNbr"]
      self.allocID:str = obj["allocID"]
      self.allocTgtNbr:int = obj["allocTgtNbr"]
      self.allocTgtSeq:int = obj["allocTgtSeq"]
      pass

class GetNewAlcHistResParams_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcHist_input:
   """ Required : 
   ds
   batchID
   runNbr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      self.batchID:str = obj["batchID"]
      self.runNbr:int = obj["runNbr"]
      pass

class GetNewAlcHist_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlcHistoryFilter_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AlcHistoryFilterTableset] = obj["returnObj"]
      pass

class GetNewPAlcHistAcct_input:
   """ Required : 
   ds
   batchID
   runNbr
   allocID
   paramNbr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      self.batchID:str = obj["batchID"]
      self.runNbr:int = obj["runNbr"]
      self.allocID:str = obj["allocID"]
      self.paramNbr:int = obj["paramNbr"]
      pass

class GetNewPAlcHistAcct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPAlcHistActCat_input:
   """ Required : 
   ds
   batchID
   runNbr
   allocID
   paramNbr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      self.batchID:str = obj["batchID"]
      self.runNbr:int = obj["runNbr"]
      self.allocID:str = obj["allocID"]
      self.paramNbr:int = obj["paramNbr"]
      pass

class GetNewPAlcHistActCat_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPAlcHistJrnCd_input:
   """ Required : 
   ds
   batchID
   runNbr
   allocID
   paramNbr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      self.batchID:str = obj["batchID"]
      self.runNbr:int = obj["runNbr"]
      self.allocID:str = obj["allocID"]
      self.paramNbr:int = obj["paramNbr"]
      pass

class GetNewPAlcHistJrnCd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPAlcHistRange_input:
   """ Required : 
   ds
   batchID
   runNbr
   allocID
   paramNbr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      self.batchID:str = obj["batchID"]
      self.runNbr:int = obj["runNbr"]
      self.allocID:str = obj["allocID"]
      self.paramNbr:int = obj["paramNbr"]
      pass

class GetNewPAlcHistRange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseAlcHist
   whereClauseAHGLJrnDtl
   whereClauseAlcHistResParams
   whereClauseAHGLJrnDtlSim
   whereClauseAlcHistResParamsSim
   whereClauseAlcHistAcct
   whereClauseAlcHistActCat
   whereClauseAlcHistDtl
   whereClauseAlcHistJrnCd
   whereClauseAlcHistParams
   whereClauseAlcHistParamsBAQ
   whereClauseAlcHistNFSrc
   whereClausePAlcHistAcct
   whereClausePAlcHistActCat
   whereClausePAlcHistJrnCd
   whereClausePAlcHistRange
   whereClauseAlcHistRange
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAlcHist:str = obj["whereClauseAlcHist"]
      self.whereClauseAHGLJrnDtl:str = obj["whereClauseAHGLJrnDtl"]
      self.whereClauseAlcHistResParams:str = obj["whereClauseAlcHistResParams"]
      self.whereClauseAHGLJrnDtlSim:str = obj["whereClauseAHGLJrnDtlSim"]
      self.whereClauseAlcHistResParamsSim:str = obj["whereClauseAlcHistResParamsSim"]
      self.whereClauseAlcHistAcct:str = obj["whereClauseAlcHistAcct"]
      self.whereClauseAlcHistActCat:str = obj["whereClauseAlcHistActCat"]
      self.whereClauseAlcHistDtl:str = obj["whereClauseAlcHistDtl"]
      self.whereClauseAlcHistJrnCd:str = obj["whereClauseAlcHistJrnCd"]
      self.whereClauseAlcHistParams:str = obj["whereClauseAlcHistParams"]
      self.whereClauseAlcHistParamsBAQ:str = obj["whereClauseAlcHistParamsBAQ"]
      self.whereClauseAlcHistNFSrc:str = obj["whereClauseAlcHistNFSrc"]
      self.whereClausePAlcHistAcct:str = obj["whereClausePAlcHistAcct"]
      self.whereClausePAlcHistActCat:str = obj["whereClausePAlcHistActCat"]
      self.whereClausePAlcHistJrnCd:str = obj["whereClausePAlcHistJrnCd"]
      self.whereClausePAlcHistRange:str = obj["whereClausePAlcHistRange"]
      self.whereClauseAlcHistRange:str = obj["whereClauseAlcHistRange"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AlcHistoryTableset] = obj["returnObj"]
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

class OnChangeBookID_input:
   """ Required : 
   cInBookID
   """  
   def __init__(self, obj):
      self.cInBookID:str = obj["cInBookID"]
      """  Proposed BookID  """  
      pass

class OnChangeBookID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.fiscalCalendarID:str = obj["parameters"]
      self.iOutFiscalYear:int = obj["parameters"]
      self.cOutFiscalYearSuffix:str = obj["parameters"]
      self.iOutStartPeriod:int = obj["parameters"]
      self.iOutEndPeriod:int = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeFiscalYearOrSuffix_input:
   """ Required : 
   bookID
   fiscalYear
   fiscalYearSuffix
   selectedStartPeriod
   selectedEndPeriod
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.selectedStartPeriod:int = obj["selectedStartPeriod"]
      self.selectedEndPeriod:int = obj["selectedEndPeriod"]
      pass

class OnChangeFiscalYearOrSuffix_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.startPeriod:int = obj["parameters"]
      self.endPeriod:int = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAlcHistoryTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAlcHistoryTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlcHistoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

