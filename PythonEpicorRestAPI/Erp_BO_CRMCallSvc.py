import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CRMCallSvc
# Description: CRMCall Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CRMCalls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CRMCalls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CRMCalls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CRMCallRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCalls",headers=creds) as resp:
           return await resp.json()

async def post_CRMCalls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CRMCalls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CRMCallRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CRMCallRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCalls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CRMCalls_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum(Company, RelatedToFile, Key1, Key2, Key3, CallSeqNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CRMCall item
   Description: Calls GetByID to retrieve the CRMCall item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CRMCall
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param CallSeqNum: Desc: CallSeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CRMCallRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCalls(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CRMCalls_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum(Company, RelatedToFile, Key1, Key2, Key3, CallSeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CRMCall for the service
   Description: Calls UpdateExt to update CRMCall. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CRMCall
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param CallSeqNum: Desc: CallSeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CRMCallRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCalls(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CRMCalls_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum(Company, RelatedToFile, Key1, Key2, Key3, CallSeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CRMCall item
   Description: Call UpdateExt to delete CRMCall item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CRMCall
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param CallSeqNum: Desc: CallSeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCalls(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_CRMCalls_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_CRMCallCnts(Company, RelatedToFile, Key1, Key2, Key3, CallSeqNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CRMCallCnts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CRMCallCnts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param CallSeqNum: Desc: CallSeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CRMCallCntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCalls(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")/CRMCallCnts",headers=creds) as resp:
           return await resp.json()

async def get_CRMCalls_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_CRMCallCnts_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_PerConLnkRowID(Company, RelatedToFile, Key1, Key2, Key3, CallSeqNum, PerConLnkRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CRMCallCnt item
   Description: Calls GetByID to retrieve the CRMCallCnt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CRMCallCnt1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param CallSeqNum: Desc: CallSeqNum   Required: True
      :param PerConLnkRowID: Desc: PerConLnkRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CRMCallCntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCalls(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")/CRMCallCnts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + "," + PerConLnkRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CRMCalls_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_CRMCallHistories(Company, RelatedToFile, Key1, Key2, Key3, CallSeqNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CRMCallHistories items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CRMCallHistories1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param CallSeqNum: Desc: CallSeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CRMCallHistoryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCalls(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")/CRMCallHistories",headers=creds) as resp:
           return await resp.json()

async def get_CRMCalls_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_CRMCallHistories_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum(Company, RelatedToFile, Key1, Key2, Key3, CallSeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CRMCallHistory item
   Description: Calls GetByID to retrieve the CRMCallHistory item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CRMCallHistory1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param CallSeqNum: Desc: CallSeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CRMCallHistoryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCalls(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")/CRMCallHistories(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_CRMCalls_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_CRMCallAttches(Company, RelatedToFile, Key1, Key2, Key3, CallSeqNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CRMCallAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CRMCallAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param CallSeqNum: Desc: CallSeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CRMCallAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCalls(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")/CRMCallAttches",headers=creds) as resp:
           return await resp.json()

async def get_CRMCalls_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_CRMCallAttches_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_DrawingSeq(Company, RelatedToFile, Key1, Key2, Key3, CallSeqNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CRMCallAttch item
   Description: Calls GetByID to retrieve the CRMCallAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CRMCallAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param CallSeqNum: Desc: CallSeqNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CRMCallAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCalls(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")/CRMCallAttches(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_CRMCallCnts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CRMCallCnts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CRMCallCnts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CRMCallCntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallCnts",headers=creds) as resp:
           return await resp.json()

async def post_CRMCallCnts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CRMCallCnts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CRMCallCntRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CRMCallCntRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallCnts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CRMCallCnts_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_PerConLnkRowID(Company, RelatedToFile, Key1, Key2, Key3, CallSeqNum, PerConLnkRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CRMCallCnt item
   Description: Calls GetByID to retrieve the CRMCallCnt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CRMCallCnt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param CallSeqNum: Desc: CallSeqNum   Required: True
      :param PerConLnkRowID: Desc: PerConLnkRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CRMCallCntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallCnts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + "," + PerConLnkRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CRMCallCnts_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_PerConLnkRowID(Company, RelatedToFile, Key1, Key2, Key3, CallSeqNum, PerConLnkRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CRMCallCnt for the service
   Description: Calls UpdateExt to update CRMCallCnt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CRMCallCnt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param CallSeqNum: Desc: CallSeqNum   Required: True
      :param PerConLnkRowID: Desc: PerConLnkRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CRMCallCntRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallCnts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + "," + PerConLnkRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CRMCallCnts_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_PerConLnkRowID(Company, RelatedToFile, Key1, Key2, Key3, CallSeqNum, PerConLnkRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CRMCallCnt item
   Description: Call UpdateExt to delete CRMCallCnt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CRMCallCnt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param CallSeqNum: Desc: CallSeqNum   Required: True
      :param PerConLnkRowID: Desc: PerConLnkRowID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallCnts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + "," + PerConLnkRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CRMCallHistories(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CRMCallHistories items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CRMCallHistories
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CRMCallHistoryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallHistories",headers=creds) as resp:
           return await resp.json()

async def post_CRMCallHistories(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CRMCallHistories
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CRMCallHistoryRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CRMCallHistoryRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallHistories", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CRMCallHistories_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum(Company, RelatedToFile, Key1, Key2, Key3, CallSeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CRMCallHistory item
   Description: Calls GetByID to retrieve the CRMCallHistory item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CRMCallHistory
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param CallSeqNum: Desc: CallSeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CRMCallHistoryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallHistories(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CRMCallHistories_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum(Company, RelatedToFile, Key1, Key2, Key3, CallSeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CRMCallHistory for the service
   Description: Calls UpdateExt to update CRMCallHistory. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CRMCallHistory
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param CallSeqNum: Desc: CallSeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CRMCallHistoryRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallHistories(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CRMCallHistories_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum(Company, RelatedToFile, Key1, Key2, Key3, CallSeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CRMCallHistory item
   Description: Call UpdateExt to delete CRMCallHistory item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CRMCallHistory
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param CallSeqNum: Desc: CallSeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallHistories(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_CRMCallAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CRMCallAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CRMCallAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CRMCallAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallAttches",headers=creds) as resp:
           return await resp.json()

async def post_CRMCallAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CRMCallAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CRMCallAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CRMCallAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CRMCallAttches_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_DrawingSeq(Company, RelatedToFile, Key1, Key2, Key3, CallSeqNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CRMCallAttch item
   Description: Calls GetByID to retrieve the CRMCallAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CRMCallAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param CallSeqNum: Desc: CallSeqNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CRMCallAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallAttches(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CRMCallAttches_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_DrawingSeq(Company, RelatedToFile, Key1, Key2, Key3, CallSeqNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CRMCallAttch for the service
   Description: Calls UpdateExt to update CRMCallAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CRMCallAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param CallSeqNum: Desc: CallSeqNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CRMCallAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallAttches(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CRMCallAttches_Company_RelatedToFile_Key1_Key2_Key3_CallSeqNum_DrawingSeq(Company, RelatedToFile, Key1, Key2, Key3, CallSeqNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CRMCallAttch item
   Description: Call UpdateExt to delete CRMCallAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CRMCallAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param CallSeqNum: Desc: CallSeqNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/CRMCallAttches(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + CallSeqNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CRMCallListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCRMCall, whereClauseCRMCallAttch, whereClauseCRMCallCnt, whereClauseCRMCallHistory, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseCRMCall=" + whereClauseCRMCall
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCRMCallAttch=" + whereClauseCRMCallAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCRMCallCnt=" + whereClauseCRMCallCnt
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCRMCallHistory=" + whereClauseCRMCallHistory
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(relatedToFile, key1, key2, key3, callSeqNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "relatedToFile=" + relatedToFile
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key1=" + key1
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key2=" + key2
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key3=" + key3
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "callSeqNum=" + callSeqNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeConName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeConName
   Description: Update CRMCallCnt information when the contact Name is changed.
   OperationID: ChangeConName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeConName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeConName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeConPerConLnkRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeConPerConLnkRowID
   Description: Update CRMCallCnt information when the contact PerConLnkRowID is changed.
   OperationID: ChangeConPerConLnkRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeConPerConLnkRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeConPerConLnkRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCustomerID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCustomerID
   Description: Update CRMCall information when the CustomerId is changed.
   OperationID: ChangeCustomerID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCustomerID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustomerID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFSCallNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFSCallNum
   Description: Update CRMCall information when the FSCall Number is changed.
   OperationID: ChangeFSCallNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFSCallNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFSCallNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHDCaseNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHDCaseNum
   Description: Update CRMCall information when the Case Number is changed.
   OperationID: ChangeHDCaseNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHDCaseNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHDCaseNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeInvoiceNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeInvoiceNum
   Description: Update CRMCall information when the AR Invoice Number is changed.
   OperationID: ChangeInvoiceNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOrderNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOrderNum
   Description: Update CRMCall information when the Order Number is changed.
   OperationID: ChangeOrderNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOrderNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOrderNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePurPoint(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePurPoint
   Description: Update CRMCall information when the Purchase Point is changed.
   OperationID: ChangePurPoint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuoteNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuoteNum
   Description: Update CRMCall information when the Quote Number is changed.
   OperationID: ChangeQuoteNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuoteNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuoteNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeProjectID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeProjectID
   Description: Update CRMCall information when the Project ID is changed.
   OperationID: ChangeProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRMANum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRMANum
   Description: Update CRMCall information when the RMA Number is changed.
   OperationID: ChangeRMANum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRMANum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRMANum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeShipToNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeShipToNum
   Description: Update CRMCall information when the ShipToNum is changed.
   OperationID: ChangeShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTaskID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTaskID
   Description: Update CRMCall information when the Task ID is changed.
   OperationID: ChangeTaskID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaskID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaskID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendorID
   Description: Update CRMCall information when the VendorID (Supplier ID) is changed.
   OperationID: ChangeVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCRMCallBySysRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCRMCallBySysRowID
   Description: Get CRMCall by SysRowID after refresh.
   OperationID: GetCRMCallBySysRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCRMCallBySysRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCRMCallBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultContactFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultContactFields
   Description: Update CRMCall information when the contact is changed.
   OperationID: DefaultContactFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultContactFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultContactFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultSupplierCntFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultSupplierCntFields
   Description: Update CRMCall information when the supplier contact is changed.
   OperationID: DefaultSupplierCntFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultSupplierCntFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultSupplierCntFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCRMCallsToShow(epicorHeaders = None):
   """  
   Summary: Invoke method GetCRMCallsToShow
   Description: Gets the number of CRM Calls to show at startup according to the Company settings.
   OperationID: GetCRMCallsToShow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCRMCallsToShow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetRowsContactTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsContactTracker
   Description: Called from Contact tracker for better performance.
   OperationID: GetRowsContactTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsContactTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsContactTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustomerTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustomerTracker
   Description: Called from Customer tracker for better performance.
   OperationID: GetRowsCustomerTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomerTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomerTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForPerson(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForPerson
   Description: Gets the list of calls where the DcdUserID is an authorized user for the Workforce specified in the call.
   OperationID: GetRowsForPerson
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForPerson_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForPerson_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFilteredRowsForPerson(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFilteredRowsForPerson
   Description: Gets the list of calls where the DcdUserID is an authorized user for the Workforce specified in the call.
   OperationID: GetFilteredRowsForPerson
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFilteredRowsForPerson_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFilteredRowsForPerson_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SortByData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SortByData
   Description: Return a list of the sort by options based on the data passed in.
   OperationID: SortByData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SortByData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SortByData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UserIsAuthorized(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UserIsAuthorized
   Description: Checks if user is authorized
   OperationID: UserIsAuthorized
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UserIsAuthorized_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UserIsAuthorized_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCRMSummarize(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCRMSummarize
   Description: Summarizes CRM call text/description for the rows in the input dataset
   OperationID: GetCRMSummarize
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCRMSummarize_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCRMSummarize_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCRMCall(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCRMCall
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCRMCall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCRMCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCRMCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCRMCallAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCRMCallAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCRMCallAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCRMCallAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCRMCallAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCRMCallCnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCRMCallCnt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCRMCallCnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCRMCallCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCRMCallCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCRMCallHistory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCRMCallHistory
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCRMCallHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCRMCallHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCRMCallHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CRMCallSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CRMCallAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallCntRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CRMCallCntRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallHistoryRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CRMCallHistoryRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CRMCallListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRMCallRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CRMCallRow] = obj["value"]
      pass

class Erp_Tablesets_CRMCallAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RelatedToFile:str = obj["RelatedToFile"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.CallSeqNum:int = obj["CallSeqNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CRMCallCntRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   The master file to which the PCE is related to. This field is used to properly isolate PCE's to the master table they are related to.
records.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "QuotHed"  PCE this field would contain the related Quote Number,  for a "Customer" PCE it contains the Customers CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
For example: For a "QuoteDtl"  memo this field would contain the Quote Line # of the related Quote detail record.  The usage of this field is dependent on the type of record the memo is related to.  For example "QuoteHed" memo's do not use this field.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
For example: For a "OrderQty"  memo this field would contain the Quote Qty # of the related Quote Qty record.  The usage of this field is dependent on the type of record the memo is related to.  """  
      self.CallSeqNum:int = obj["CallSeqNum"]
      """  Used to uniquely identify the record.  Used so more than 1 PCE can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  """  
      self.PerConLnkRowID:str = obj["PerConLnkRowID"]
      """  The SysRowId of the linked PerConLnk.  """  
      self.Primary:bool = obj["Primary"]
      """  Primary contact for each Context type. Only one allowed per context type.  The primary contact for each context type is shown on the detail sheet.  """  
      self.Comment:str = obj["Comment"]
      """  User entered comments.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.BuyerID:str = obj["BuyerID"]
      self.BuyerName:str = obj["BuyerName"]
      self.City:str = obj["City"]
      self.ContextLink:str = obj["ContextLink"]
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.EmpID:str = obj["EmpID"]
      self.EmpName:str = obj["EmpName"]
      self.Name:str = obj["Name"]
      self.PurPoint:str = obj["PurPoint"]
      self.PurPointName:str = obj["PurPointName"]
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.State:str = obj["State"]
      self.VendorID:str = obj["VendorID"]
      self.VendorName:str = obj["VendorName"]
      self.Zip:str = obj["Zip"]
      self.PerConID:int = obj["PerConID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CRMCallHistoryRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   The master file to which the PCE is related to.  This field is used to properly  isolate PCE's to the master table they are related to.
records.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "QuotHed"  PCE this field would contain the related Quote Number,  for a "Customer" PCE it contains the Customers CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
For example: For a "QuoteDtl"  memo this field would contain the Quote Line # of the related Quote detail record.  The usage of this field is dependent on the type of record the memo is related to.  For example "QuoteHed" memo's do not use this field.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
For example: For a "OrderQty"  memo this field would contain the Quote Qty # of the related Quote Qty record.  The usage of this field is dependent on the type of record the memo is related to.  """  
      self.CallSeqNum:int = obj["CallSeqNum"]
      """  Used to uniquely identify the record.  Used so more than 1 PCE can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  """  
      self.CallDesc:str = obj["CallDesc"]
      """  An abbreviated description of what the Call is about.  """  
      self.CallText:str = obj["CallText"]
      """  Call Text contains the textual content of the Call. Intended to be used as internal online storage of text information related to a specific master. They do get pulled into other database records.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The Salesperson that owns this PCE  """  
      self.CallTypeCode:str = obj["CallTypeCode"]
      """  CallType code from the CallType table.  Identifies what type of communication this is. For example email, phone, visit, etc.  """  
      self.CallContactType:str = obj["CallContactType"]
      """   indicates if the contact is a "Customer", "Vendor" or "SalesRep".
Default is based on related to field.  If its a QOL then Customer will default.   If its a Marketing event then vendor. Values can be "Customer", "Vendor", "SalesRep"  """  
      self.CallCustNum:int = obj["CallCustNum"]
      """  The unique internal number assigned to the customer for which the contact is related to. Used when CallContactType is "Customer"  """  
      self.CallShipToNum:str = obj["CallShipToNum"]
      """  The number that the user assigned to the ship to that this contact is related to.  Note that this field is blank for contacts related to the customer only.  Blank when there is no ship to.  """  
      self.CallConNum:int = obj["CallConNum"]
      """  A system generated number used to uniquely identify the contact record for the related customer or ship to.  """  
      self.CallVendorNum:int = obj["CallVendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.CallPurPoint:str = obj["CallPurPoint"]
      """  Purchase point of linked Vendor  """  
      self.CallVConNum:int = obj["CallVConNum"]
      """  Used to uniquely identify the contact record for the related vendor or purchase point.  """  
      self.OrigDcdUserID:str = obj["OrigDcdUserID"]
      """  The DCD user ID that created the record  """  
      self.LastDcdUserID:str = obj["LastDcdUserID"]
      """  The DCD user ID that last updated the record  """  
      self.OrigDate:str = obj["OrigDate"]
      """  The date the PCE was created.  """  
      self.OrigTime:int = obj["OrigTime"]
      """  The time the PCE was created.  """  
      self.LastDate:str = obj["LastDate"]
      """  The date the PCE was last modified.  """  
      self.LastTime:int = obj["LastTime"]
      """  The time the PCE was last modified.  """  
      self.CallQuoteNum:int = obj["CallQuoteNum"]
      """  The Quote that this call is related to.  """  
      self.CallQuoteLine:int = obj["CallQuoteLine"]
      """  The Quote line that this Call is related to.  """  
      self.CallTypeDescription:str = obj["CallTypeDescription"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ContactName:str = obj["ContactName"]
      self.ContactEmail:str = obj["ContactEmail"]
      self.ContactPhone:str = obj["ContactPhone"]
      self.ContactFax:str = obj["ContactFax"]
      self.TaskDescription:str = obj["TaskDescription"]
      self.HistorySeqNum:int = obj["HistorySeqNum"]
      self.HistoryCallSeqNum:int = obj["HistoryCallSeqNum"]
      self.HistoryRelatedToFile:str = obj["HistoryRelatedToFile"]
      self.DispOrigTime:str = obj["DispOrigTime"]
      self.DispLastTime:str = obj["DispLastTime"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CallCustNumName:str = obj["CallCustNumName"]
      self.CallCustNumCustID:str = obj["CallCustNumCustID"]
      self.CallCustNumBTName:str = obj["CallCustNumBTName"]
      self.CallTypeCodeCallTypeDesc:str = obj["CallTypeCodeCallTypeDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CRMCallListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   The master file to which the PCE is related to.  This field is used to properly  isolate PCE's to the master table they are related to.
records.  """  
      self.DisplayOrigTime:str = obj["DisplayOrigTime"]
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "QuotHed"  PCE this field would contain the related Quote Number,  for a "Customer" PCE it contains the Customers CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
For example: For a "QuoteDtl"  memo this field would contain the Quote Line # of the related Quote detail record.  The usage of this field is dependent on the type of record the memo is related to.  For example "QuoteHed" memo's do not use this field.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
For example: For a "OrderQty"  memo this field would contain the Quote Qty # of the related Quote Qty record.  The usage of this field is dependent on the type of record the memo is related to.  """  
      self.CallSeqNum:int = obj["CallSeqNum"]
      """  Used to uniquely identify the record.  Used so more than 1 PCE can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  """  
      self.CallDesc:str = obj["CallDesc"]
      """  An abbreviated description of what the Call is about.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The Salesperson that owns this PCE  """  
      self.SalesRepName:str = obj["SalesRepName"]
      self.CallTypeCode:str = obj["CallTypeCode"]
      """  CallType code from the CallType table.  Identifies what type of communication this is. For example email, phone, visit, etc.  """  
      self.TaskDescription:str = obj["TaskDescription"]
      self.OrigDcdUserID:str = obj["OrigDcdUserID"]
      """  The DCD user ID that created the record  """  
      self.LastDcdUserID:str = obj["LastDcdUserID"]
      """  The DCD user ID that last updated the record  """  
      self.OrigDate:str = obj["OrigDate"]
      """  The date the PCE was created.  """  
      self.OrigTime:int = obj["OrigTime"]
      """  The time the PCE was created.  """  
      self.LastDate:str = obj["LastDate"]
      """  The date the PCE was last modified.  """  
      self.CallQuoteNum:int = obj["CallQuoteNum"]
      """  The Quote that this call is related to.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CallTypeCodeCallTypeDesc:str = obj["CallTypeCodeCallTypeDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CRMCallRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   The master file to which the PCE is related to.  This field is used to properly  isolate PCE's to the master table they are related to.
records.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "QuotHed"  PCE this field would contain the related Quote Number,  for a "Customer" PCE it contains the Customers CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
For example: For a "QuoteDtl"  memo this field would contain the Quote Line # of the related Quote detail record.  The usage of this field is dependent on the type of record the memo is related to.  For example "QuoteHed" memo's do not use this field.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
For example: For a "OrderQty"  memo this field would contain the Quote Qty # of the related Quote Qty record.  The usage of this field is dependent on the type of record the memo is related to.  """  
      self.CallSeqNum:int = obj["CallSeqNum"]
      """  Used to uniquely identify the record.  Used so more than 1 PCE can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  """  
      self.CallDesc:str = obj["CallDesc"]
      """  An abbreviated description of what the Call is about.  """  
      self.CallText:str = obj["CallText"]
      """  Call Text contains the textual content of the Call. Intended to be used as internal online storage of text information related to a specific master. They do get pulled into other database records.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The Salesperson that owns this PCE  """  
      self.CallTypeCode:str = obj["CallTypeCode"]
      """  CallType code from the CallType table.  Identifies what type of communication this is. For example email, phone, visit, etc.  """  
      self.CallContactType:str = obj["CallContactType"]
      """   indicates if the contact is a "Customer", "Vendor" or "SalesRep".
Default is based on related to field.  If its a QOL then Customer will default.   If its a Marketing event then vendor. Values can be "Customer", "Vendor", "SalesRep"  """  
      self.CallCustNum:int = obj["CallCustNum"]
      """  The unique internal number assigned to the customer for which the contact is related to. Used when CallContactType is "Customer"  """  
      self.CallShipToNum:str = obj["CallShipToNum"]
      """  The number that the user assigned to the ship to that this contact is related to.  Note that this field is blank for contacts related to the customer only.  Blank when there is no ship to.  """  
      self.CallConNum:int = obj["CallConNum"]
      """  A system generated number used to uniquely identify the contact record for the related customer or ship to.  """  
      self.CallVendorNum:int = obj["CallVendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.CallPurPoint:str = obj["CallPurPoint"]
      """  Purchase point of linked Vendor  """  
      self.CallVConNum:int = obj["CallVConNum"]
      """  Used to uniquely identify the contact record for the related vendor or purchase point.  """  
      self.OrigDcdUserID:str = obj["OrigDcdUserID"]
      """  The DCD user ID that created the record  """  
      self.LastDcdUserID:str = obj["LastDcdUserID"]
      """  The DCD user ID that last updated the record  """  
      self.OrigDate:str = obj["OrigDate"]
      """  The date the PCE was created.  """  
      self.OrigTime:int = obj["OrigTime"]
      """  The time the PCE was created.  """  
      self.LastDate:str = obj["LastDate"]
      """  The date the PCE was last modified.  """  
      self.LastTime:int = obj["LastTime"]
      """  The time the PCE was last modified.  """  
      self.CallQuoteNum:int = obj["CallQuoteNum"]
      """  The Quote that this call is related to.  """  
      self.CallQuoteLine:int = obj["CallQuoteLine"]
      """  The Quote line that this Call is related to.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.CallEmpID:str = obj["CallEmpID"]
      """  Unique identifier of the primary Employee contact.  """  
      self.CallBuyerID:str = obj["CallBuyerID"]
      """  Unique identifier of the primary Buyer contact.  """  
      self.CallOrderNum:int = obj["CallOrderNum"]
      """  The sales order the call is related to.  """  
      self.CallInvoiceNum:int = obj["CallInvoiceNum"]
      """  The invoice the call is related to.  """  
      self.CallRMANum:int = obj["CallRMANum"]
      """  The RMA this call is related to.  """  
      self.CallFSCallNum:int = obj["CallFSCallNum"]
      """  The field service call this CRM call is related to.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.CallHDCaseNum:int = obj["CallHDCaseNum"]
      """  CallHDCaseNum  """  
      self.CallTaskID:str = obj["CallTaskID"]
      """  CallTaskID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CallPerConID:int = obj["CallPerConID"]
      """  CallPerConID  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  RelatedToSysRowID  """  
      self.CallProjectID:str = obj["CallProjectID"]
      """  CallProjectID  """  
      self.CallPurPointName:str = obj["CallPurPointName"]
      """  Name of the purchase point.  """  
      self.CallShipToName:str = obj["CallShipToName"]
      """  The name for the ship to location.  """  
      self.CallTaskDescription:str = obj["CallTaskDescription"]
      self.CallTypeDescription:str = obj["CallTypeDescription"]
      self.ContactEmail:str = obj["ContactEmail"]
      self.ContactFax:str = obj["ContactFax"]
      self.ContactName:str = obj["ContactName"]
      """  The contact's name.  """  
      self.ContactPhone:str = obj["ContactPhone"]
      self.DispLastTime:str = obj["DispLastTime"]
      self.DispOrigTime:str = obj["DispOrigTime"]
      self.NextRelatedTo:str = obj["NextRelatedTo"]
      self.SalesRepName:str = obj["SalesRepName"]
      """  Name of the sales representative.  """  
      self.TaskDescription:str = obj["TaskDescription"]
      self.VContactEmail:str = obj["VContactEmail"]
      self.VContactFax:str = obj["VContactFax"]
      self.VContactName:str = obj["VContactName"]
      self.VContactPhone:str = obj["VContactPhone"]
      self.CallKeys:str = obj["CallKeys"]
      self.BitFlag:int = obj["BitFlag"]
      self.CallCustNumInactive:bool = obj["CallCustNumInactive"]
      self.CallCustNumBTName:str = obj["CallCustNumBTName"]
      self.CallCustNumName:str = obj["CallCustNumName"]
      self.CallCustNumCustID:str = obj["CallCustNumCustID"]
      self.CallShipToNumInactive:bool = obj["CallShipToNumInactive"]
      self.CallTypeCodeCallTypeDesc:str = obj["CallTypeCodeCallTypeDesc"]
      self.CallVendorNumDefaultFOB:str = obj["CallVendorNumDefaultFOB"]
      self.CallVendorNumVendorID:str = obj["CallVendorNumVendorID"]
      self.CallVendorNumAddress1:str = obj["CallVendorNumAddress1"]
      self.CallVendorNumZIP:str = obj["CallVendorNumZIP"]
      self.CallVendorNumState:str = obj["CallVendorNumState"]
      self.CallVendorNumCurrencyCode:str = obj["CallVendorNumCurrencyCode"]
      self.CallVendorNumTermsCode:str = obj["CallVendorNumTermsCode"]
      self.CallVendorNumAddress3:str = obj["CallVendorNumAddress3"]
      self.CallVendorNumCity:str = obj["CallVendorNumCity"]
      self.CallVendorNumAddress2:str = obj["CallVendorNumAddress2"]
      self.CallVendorNumName:str = obj["CallVendorNumName"]
      self.CallVendorNumCountry:str = obj["CallVendorNumCountry"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeConName_input:
   """ Required : 
   pName
   ds
   """  
   def __init__(self, obj):
      self.pName:str = obj["pName"]
      """  Proposed Name  """  
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

class ChangeConName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeConPerConLnkRowID_input:
   """ Required : 
   pPerConLnkRowID
   ds
   """  
   def __init__(self, obj):
      self.pPerConLnkRowID:str = obj["pPerConLnkRowID"]
      """  Proposed PerConLnkRowID  """  
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

class ChangeConPerConLnkRowID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCustomerID_input:
   """ Required : 
   pCustomerId
   ds
   """  
   def __init__(self, obj):
      self.pCustomerId:str = obj["pCustomerId"]
      """  Proposed Customer ID  """  
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

class ChangeCustomerID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFSCallNum_input:
   """ Required : 
   pFSCallNum
   ds
   """  
   def __init__(self, obj):
      self.pFSCallNum:int = obj["pFSCallNum"]
      """  Proposed FSCall Number  """  
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

class ChangeFSCallNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHDCaseNum_input:
   """ Required : 
   pHDCaseNum
   ds
   """  
   def __init__(self, obj):
      self.pHDCaseNum:int = obj["pHDCaseNum"]
      """  Proposed Case Number  """  
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

class ChangeHDCaseNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeInvoiceNum_input:
   """ Required : 
   pInvoiceNum
   ds
   """  
   def __init__(self, obj):
      self.pInvoiceNum:int = obj["pInvoiceNum"]
      """  Proposed Invoice Number  """  
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

class ChangeInvoiceNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOrderNum_input:
   """ Required : 
   pOrderNum
   ds
   """  
   def __init__(self, obj):
      self.pOrderNum:int = obj["pOrderNum"]
      """  Proposed Order Number  """  
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

class ChangeOrderNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeProjectID_input:
   """ Required : 
   projectID
   ds
   """  
   def __init__(self, obj):
      self.projectID:str = obj["projectID"]
      """  Proposed Project ID  """  
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

class ChangeProjectID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePurPoint_input:
   """ Required : 
   pVendorNum
   pPurPoint
   ds
   """  
   def __init__(self, obj):
      self.pVendorNum:int = obj["pVendorNum"]
      """  Proposed Supplier number.  """  
      self.pPurPoint:str = obj["pPurPoint"]
      """  Proposed purchase point..  """  
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

class ChangePurPoint_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuoteNum_input:
   """ Required : 
   pQuoteNum
   ds
   """  
   def __init__(self, obj):
      self.pQuoteNum:int = obj["pQuoteNum"]
      """  Proposed Quote Number  """  
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

class ChangeQuoteNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRMANum_input:
   """ Required : 
   pRMANum
   ds
   """  
   def __init__(self, obj):
      self.pRMANum:int = obj["pRMANum"]
      """  Proposed RMA Number  """  
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

class ChangeRMANum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeShipToNum_input:
   """ Required : 
   pCustNum
   pShipToNum
   ds
   """  
   def __init__(self, obj):
      self.pCustNum:int = obj["pCustNum"]
      """  Proposed Customer number.  """  
      self.pShipToNum:str = obj["pShipToNum"]
      """  Proposed Ship To number.  """  
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

class ChangeShipToNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTaskID_input:
   """ Required : 
   pTaskID
   ds
   """  
   def __init__(self, obj):
      self.pTaskID:str = obj["pTaskID"]
      """  Proposed Task ID  """  
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

class ChangeTaskID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVendorID_input:
   """ Required : 
   pVendorID
   ds
   """  
   def __init__(self, obj):
      self.pVendorID:str = obj["pVendorID"]
      """  Proposed Supplier ID  """  
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

class ChangeVendorID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultContactFields_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

class DefaultContactFields_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultSupplierCntFields_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

class DefaultSupplierCntFields_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   relatedToFile
   key1
   key2
   key3
   callSeqNum
   """  
   def __init__(self, obj):
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.callSeqNum:int = obj["callSeqNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CRMCallAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RelatedToFile:str = obj["RelatedToFile"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.CallSeqNum:int = obj["CallSeqNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CRMCallCntRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   The master file to which the PCE is related to. This field is used to properly isolate PCE's to the master table they are related to.
records.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "QuotHed"  PCE this field would contain the related Quote Number,  for a "Customer" PCE it contains the Customers CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
For example: For a "QuoteDtl"  memo this field would contain the Quote Line # of the related Quote detail record.  The usage of this field is dependent on the type of record the memo is related to.  For example "QuoteHed" memo's do not use this field.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
For example: For a "OrderQty"  memo this field would contain the Quote Qty # of the related Quote Qty record.  The usage of this field is dependent on the type of record the memo is related to.  """  
      self.CallSeqNum:int = obj["CallSeqNum"]
      """  Used to uniquely identify the record.  Used so more than 1 PCE can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  """  
      self.PerConLnkRowID:str = obj["PerConLnkRowID"]
      """  The SysRowId of the linked PerConLnk.  """  
      self.Primary:bool = obj["Primary"]
      """  Primary contact for each Context type. Only one allowed per context type.  The primary contact for each context type is shown on the detail sheet.  """  
      self.Comment:str = obj["Comment"]
      """  User entered comments.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.BuyerID:str = obj["BuyerID"]
      self.BuyerName:str = obj["BuyerName"]
      self.City:str = obj["City"]
      self.ContextLink:str = obj["ContextLink"]
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.EmpID:str = obj["EmpID"]
      self.EmpName:str = obj["EmpName"]
      self.Name:str = obj["Name"]
      self.PurPoint:str = obj["PurPoint"]
      self.PurPointName:str = obj["PurPointName"]
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.State:str = obj["State"]
      self.VendorID:str = obj["VendorID"]
      self.VendorName:str = obj["VendorName"]
      self.Zip:str = obj["Zip"]
      self.PerConID:int = obj["PerConID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CRMCallHistoryRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   The master file to which the PCE is related to.  This field is used to properly  isolate PCE's to the master table they are related to.
records.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "QuotHed"  PCE this field would contain the related Quote Number,  for a "Customer" PCE it contains the Customers CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
For example: For a "QuoteDtl"  memo this field would contain the Quote Line # of the related Quote detail record.  The usage of this field is dependent on the type of record the memo is related to.  For example "QuoteHed" memo's do not use this field.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
For example: For a "OrderQty"  memo this field would contain the Quote Qty # of the related Quote Qty record.  The usage of this field is dependent on the type of record the memo is related to.  """  
      self.CallSeqNum:int = obj["CallSeqNum"]
      """  Used to uniquely identify the record.  Used so more than 1 PCE can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  """  
      self.CallDesc:str = obj["CallDesc"]
      """  An abbreviated description of what the Call is about.  """  
      self.CallText:str = obj["CallText"]
      """  Call Text contains the textual content of the Call. Intended to be used as internal online storage of text information related to a specific master. They do get pulled into other database records.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The Salesperson that owns this PCE  """  
      self.CallTypeCode:str = obj["CallTypeCode"]
      """  CallType code from the CallType table.  Identifies what type of communication this is. For example email, phone, visit, etc.  """  
      self.CallContactType:str = obj["CallContactType"]
      """   indicates if the contact is a "Customer", "Vendor" or "SalesRep".
Default is based on related to field.  If its a QOL then Customer will default.   If its a Marketing event then vendor. Values can be "Customer", "Vendor", "SalesRep"  """  
      self.CallCustNum:int = obj["CallCustNum"]
      """  The unique internal number assigned to the customer for which the contact is related to. Used when CallContactType is "Customer"  """  
      self.CallShipToNum:str = obj["CallShipToNum"]
      """  The number that the user assigned to the ship to that this contact is related to.  Note that this field is blank for contacts related to the customer only.  Blank when there is no ship to.  """  
      self.CallConNum:int = obj["CallConNum"]
      """  A system generated number used to uniquely identify the contact record for the related customer or ship to.  """  
      self.CallVendorNum:int = obj["CallVendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.CallPurPoint:str = obj["CallPurPoint"]
      """  Purchase point of linked Vendor  """  
      self.CallVConNum:int = obj["CallVConNum"]
      """  Used to uniquely identify the contact record for the related vendor or purchase point.  """  
      self.OrigDcdUserID:str = obj["OrigDcdUserID"]
      """  The DCD user ID that created the record  """  
      self.LastDcdUserID:str = obj["LastDcdUserID"]
      """  The DCD user ID that last updated the record  """  
      self.OrigDate:str = obj["OrigDate"]
      """  The date the PCE was created.  """  
      self.OrigTime:int = obj["OrigTime"]
      """  The time the PCE was created.  """  
      self.LastDate:str = obj["LastDate"]
      """  The date the PCE was last modified.  """  
      self.LastTime:int = obj["LastTime"]
      """  The time the PCE was last modified.  """  
      self.CallQuoteNum:int = obj["CallQuoteNum"]
      """  The Quote that this call is related to.  """  
      self.CallQuoteLine:int = obj["CallQuoteLine"]
      """  The Quote line that this Call is related to.  """  
      self.CallTypeDescription:str = obj["CallTypeDescription"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ContactName:str = obj["ContactName"]
      self.ContactEmail:str = obj["ContactEmail"]
      self.ContactPhone:str = obj["ContactPhone"]
      self.ContactFax:str = obj["ContactFax"]
      self.TaskDescription:str = obj["TaskDescription"]
      self.HistorySeqNum:int = obj["HistorySeqNum"]
      self.HistoryCallSeqNum:int = obj["HistoryCallSeqNum"]
      self.HistoryRelatedToFile:str = obj["HistoryRelatedToFile"]
      self.DispOrigTime:str = obj["DispOrigTime"]
      self.DispLastTime:str = obj["DispLastTime"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CallCustNumName:str = obj["CallCustNumName"]
      self.CallCustNumCustID:str = obj["CallCustNumCustID"]
      self.CallCustNumBTName:str = obj["CallCustNumBTName"]
      self.CallTypeCodeCallTypeDesc:str = obj["CallTypeCodeCallTypeDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CRMCallListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   The master file to which the PCE is related to.  This field is used to properly  isolate PCE's to the master table they are related to.
records.  """  
      self.DisplayOrigTime:str = obj["DisplayOrigTime"]
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "QuotHed"  PCE this field would contain the related Quote Number,  for a "Customer" PCE it contains the Customers CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
For example: For a "QuoteDtl"  memo this field would contain the Quote Line # of the related Quote detail record.  The usage of this field is dependent on the type of record the memo is related to.  For example "QuoteHed" memo's do not use this field.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
For example: For a "OrderQty"  memo this field would contain the Quote Qty # of the related Quote Qty record.  The usage of this field is dependent on the type of record the memo is related to.  """  
      self.CallSeqNum:int = obj["CallSeqNum"]
      """  Used to uniquely identify the record.  Used so more than 1 PCE can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  """  
      self.CallDesc:str = obj["CallDesc"]
      """  An abbreviated description of what the Call is about.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The Salesperson that owns this PCE  """  
      self.SalesRepName:str = obj["SalesRepName"]
      self.CallTypeCode:str = obj["CallTypeCode"]
      """  CallType code from the CallType table.  Identifies what type of communication this is. For example email, phone, visit, etc.  """  
      self.TaskDescription:str = obj["TaskDescription"]
      self.OrigDcdUserID:str = obj["OrigDcdUserID"]
      """  The DCD user ID that created the record  """  
      self.LastDcdUserID:str = obj["LastDcdUserID"]
      """  The DCD user ID that last updated the record  """  
      self.OrigDate:str = obj["OrigDate"]
      """  The date the PCE was created.  """  
      self.OrigTime:int = obj["OrigTime"]
      """  The time the PCE was created.  """  
      self.LastDate:str = obj["LastDate"]
      """  The date the PCE was last modified.  """  
      self.CallQuoteNum:int = obj["CallQuoteNum"]
      """  The Quote that this call is related to.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CallTypeCodeCallTypeDesc:str = obj["CallTypeCodeCallTypeDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CRMCallListTableset:
   def __init__(self, obj):
      self.CRMCallList:list[Erp_Tablesets_CRMCallListRow] = obj["CRMCallList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CRMCallRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   The master file to which the PCE is related to.  This field is used to properly  isolate PCE's to the master table they are related to.
records.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "QuotHed"  PCE this field would contain the related Quote Number,  for a "Customer" PCE it contains the Customers CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
For example: For a "QuoteDtl"  memo this field would contain the Quote Line # of the related Quote detail record.  The usage of this field is dependent on the type of record the memo is related to.  For example "QuoteHed" memo's do not use this field.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
For example: For a "OrderQty"  memo this field would contain the Quote Qty # of the related Quote Qty record.  The usage of this field is dependent on the type of record the memo is related to.  """  
      self.CallSeqNum:int = obj["CallSeqNum"]
      """  Used to uniquely identify the record.  Used so more than 1 PCE can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  """  
      self.CallDesc:str = obj["CallDesc"]
      """  An abbreviated description of what the Call is about.  """  
      self.CallText:str = obj["CallText"]
      """  Call Text contains the textual content of the Call. Intended to be used as internal online storage of text information related to a specific master. They do get pulled into other database records.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The Salesperson that owns this PCE  """  
      self.CallTypeCode:str = obj["CallTypeCode"]
      """  CallType code from the CallType table.  Identifies what type of communication this is. For example email, phone, visit, etc.  """  
      self.CallContactType:str = obj["CallContactType"]
      """   indicates if the contact is a "Customer", "Vendor" or "SalesRep".
Default is based on related to field.  If its a QOL then Customer will default.   If its a Marketing event then vendor. Values can be "Customer", "Vendor", "SalesRep"  """  
      self.CallCustNum:int = obj["CallCustNum"]
      """  The unique internal number assigned to the customer for which the contact is related to. Used when CallContactType is "Customer"  """  
      self.CallShipToNum:str = obj["CallShipToNum"]
      """  The number that the user assigned to the ship to that this contact is related to.  Note that this field is blank for contacts related to the customer only.  Blank when there is no ship to.  """  
      self.CallConNum:int = obj["CallConNum"]
      """  A system generated number used to uniquely identify the contact record for the related customer or ship to.  """  
      self.CallVendorNum:int = obj["CallVendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.CallPurPoint:str = obj["CallPurPoint"]
      """  Purchase point of linked Vendor  """  
      self.CallVConNum:int = obj["CallVConNum"]
      """  Used to uniquely identify the contact record for the related vendor or purchase point.  """  
      self.OrigDcdUserID:str = obj["OrigDcdUserID"]
      """  The DCD user ID that created the record  """  
      self.LastDcdUserID:str = obj["LastDcdUserID"]
      """  The DCD user ID that last updated the record  """  
      self.OrigDate:str = obj["OrigDate"]
      """  The date the PCE was created.  """  
      self.OrigTime:int = obj["OrigTime"]
      """  The time the PCE was created.  """  
      self.LastDate:str = obj["LastDate"]
      """  The date the PCE was last modified.  """  
      self.LastTime:int = obj["LastTime"]
      """  The time the PCE was last modified.  """  
      self.CallQuoteNum:int = obj["CallQuoteNum"]
      """  The Quote that this call is related to.  """  
      self.CallQuoteLine:int = obj["CallQuoteLine"]
      """  The Quote line that this Call is related to.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.CallEmpID:str = obj["CallEmpID"]
      """  Unique identifier of the primary Employee contact.  """  
      self.CallBuyerID:str = obj["CallBuyerID"]
      """  Unique identifier of the primary Buyer contact.  """  
      self.CallOrderNum:int = obj["CallOrderNum"]
      """  The sales order the call is related to.  """  
      self.CallInvoiceNum:int = obj["CallInvoiceNum"]
      """  The invoice the call is related to.  """  
      self.CallRMANum:int = obj["CallRMANum"]
      """  The RMA this call is related to.  """  
      self.CallFSCallNum:int = obj["CallFSCallNum"]
      """  The field service call this CRM call is related to.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.CallHDCaseNum:int = obj["CallHDCaseNum"]
      """  CallHDCaseNum  """  
      self.CallTaskID:str = obj["CallTaskID"]
      """  CallTaskID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CallPerConID:int = obj["CallPerConID"]
      """  CallPerConID  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  RelatedToSysRowID  """  
      self.CallProjectID:str = obj["CallProjectID"]
      """  CallProjectID  """  
      self.CallPurPointName:str = obj["CallPurPointName"]
      """  Name of the purchase point.  """  
      self.CallShipToName:str = obj["CallShipToName"]
      """  The name for the ship to location.  """  
      self.CallTaskDescription:str = obj["CallTaskDescription"]
      self.CallTypeDescription:str = obj["CallTypeDescription"]
      self.ContactEmail:str = obj["ContactEmail"]
      self.ContactFax:str = obj["ContactFax"]
      self.ContactName:str = obj["ContactName"]
      """  The contact's name.  """  
      self.ContactPhone:str = obj["ContactPhone"]
      self.DispLastTime:str = obj["DispLastTime"]
      self.DispOrigTime:str = obj["DispOrigTime"]
      self.NextRelatedTo:str = obj["NextRelatedTo"]
      self.SalesRepName:str = obj["SalesRepName"]
      """  Name of the sales representative.  """  
      self.TaskDescription:str = obj["TaskDescription"]
      self.VContactEmail:str = obj["VContactEmail"]
      self.VContactFax:str = obj["VContactFax"]
      self.VContactName:str = obj["VContactName"]
      self.VContactPhone:str = obj["VContactPhone"]
      self.CallKeys:str = obj["CallKeys"]
      self.BitFlag:int = obj["BitFlag"]
      self.CallCustNumInactive:bool = obj["CallCustNumInactive"]
      self.CallCustNumBTName:str = obj["CallCustNumBTName"]
      self.CallCustNumName:str = obj["CallCustNumName"]
      self.CallCustNumCustID:str = obj["CallCustNumCustID"]
      self.CallShipToNumInactive:bool = obj["CallShipToNumInactive"]
      self.CallTypeCodeCallTypeDesc:str = obj["CallTypeCodeCallTypeDesc"]
      self.CallVendorNumDefaultFOB:str = obj["CallVendorNumDefaultFOB"]
      self.CallVendorNumVendorID:str = obj["CallVendorNumVendorID"]
      self.CallVendorNumAddress1:str = obj["CallVendorNumAddress1"]
      self.CallVendorNumZIP:str = obj["CallVendorNumZIP"]
      self.CallVendorNumState:str = obj["CallVendorNumState"]
      self.CallVendorNumCurrencyCode:str = obj["CallVendorNumCurrencyCode"]
      self.CallVendorNumTermsCode:str = obj["CallVendorNumTermsCode"]
      self.CallVendorNumAddress3:str = obj["CallVendorNumAddress3"]
      self.CallVendorNumCity:str = obj["CallVendorNumCity"]
      self.CallVendorNumAddress2:str = obj["CallVendorNumAddress2"]
      self.CallVendorNumName:str = obj["CallVendorNumName"]
      self.CallVendorNumCountry:str = obj["CallVendorNumCountry"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CRMCallTableset:
   def __init__(self, obj):
      self.CRMCall:list[Erp_Tablesets_CRMCallRow] = obj["CRMCall"]
      self.CRMCallAttch:list[Erp_Tablesets_CRMCallAttchRow] = obj["CRMCallAttch"]
      self.CRMCallCnt:list[Erp_Tablesets_CRMCallCntRow] = obj["CRMCallCnt"]
      self.CRMCallHistory:list[Erp_Tablesets_CRMCallHistoryRow] = obj["CRMCallHistory"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCRMCallTableset:
   def __init__(self, obj):
      self.CRMCall:list[Erp_Tablesets_CRMCallRow] = obj["CRMCall"]
      self.CRMCallAttch:list[Erp_Tablesets_CRMCallAttchRow] = obj["CRMCallAttch"]
      self.CRMCallCnt:list[Erp_Tablesets_CRMCallCntRow] = obj["CRMCallCnt"]
      self.CRMCallHistory:list[Erp_Tablesets_CRMCallHistoryRow] = obj["CRMCallHistory"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   relatedToFile
   key1
   key2
   key3
   callSeqNum
   """  
   def __init__(self, obj):
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.callSeqNum:int = obj["callSeqNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CRMCallTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CRMCallTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CRMCallTableset] = obj["returnObj"]
      pass

class GetCRMCallBySysRowID_input:
   """ Required : 
   sysRowID
   ds
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      """  SysRowID  """  
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

class GetCRMCallBySysRowID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetCRMCallsToShow_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.crmCallsToShow:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetCRMSummarize_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

class GetCRMSummarize_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.summarizedString:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetFilteredRowsForPerson_input:
   """ Required : 
   whereClause
   startingAt
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.startingAt:str = obj["startingAt"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetFilteredRowsForPerson_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CRMCallTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CRMCallListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCRMCallAttch_input:
   """ Required : 
   ds
   relatedToFile
   key1
   key2
   key3
   callSeqNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.callSeqNum:int = obj["callSeqNum"]
      pass

class GetNewCRMCallAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCRMCallCnt_input:
   """ Required : 
   ds
   relatedToFile
   key1
   key2
   key3
   callSeqNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.callSeqNum:int = obj["callSeqNum"]
      pass

class GetNewCRMCallCnt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCRMCallHistory_input:
   """ Required : 
   ds
   relatedToFile
   key1
   key2
   key3
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      pass

class GetNewCRMCallHistory_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCRMCall_input:
   """ Required : 
   ds
   relatedToFile
   key1
   key2
   key3
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      pass

class GetNewCRMCall_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsContactTracker_input:
   """ Required : 
   whereClauseCRMCall
   whereClauseCRMCallHistory
   contactName
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCRMCall:str = obj["whereClauseCRMCall"]
      """  Whereclause for CRMCall table.  """  
      self.whereClauseCRMCallHistory:str = obj["whereClauseCRMCallHistory"]
      """  Whereclause for CRMCallHistory table.  """  
      self.contactName:str = obj["contactName"]
      """  The contact to return data for.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsContactTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CRMCallTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCustomerTracker_input:
   """ Required : 
   whereClauseCRMCall
   whereClauseCRMCallHistory
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCRMCall:str = obj["whereClauseCRMCall"]
      """  Whereclause for CRMCall table.  """  
      self.whereClauseCRMCallHistory:str = obj["whereClauseCRMCallHistory"]
      """  Whereclause for CRMCallHistory table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsCustomerTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CRMCallTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsForPerson_input:
   """ Required : 
   whereClause
   startingAt
   hDCaseNum
   pageSize
   absolutePage
   orderBy
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.startingAt:str = obj["startingAt"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.hDCaseNum:int = obj["hDCaseNum"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      self.orderBy:str = obj["orderBy"]
      pass

class GetRowsForPerson_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CRMCallTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCRMCall
   whereClauseCRMCallAttch
   whereClauseCRMCallCnt
   whereClauseCRMCallHistory
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCRMCall:str = obj["whereClauseCRMCall"]
      self.whereClauseCRMCallAttch:str = obj["whereClauseCRMCallAttch"]
      self.whereClauseCRMCallCnt:str = obj["whereClauseCRMCallCnt"]
      self.whereClauseCRMCallHistory:str = obj["whereClauseCRMCallHistory"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CRMCallTableset] = obj["returnObj"]
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

class SortByData_input:
   """ Required : 
   cTableName
   iCustNum
   iQuoteNum
   iVendorNum
   """  
   def __init__(self, obj):
      self.cTableName:str = obj["cTableName"]
      """  The table name to base the sort by on.  Valid values are:
            Customer, QuoteHed, Task  """  
      self.iCustNum:int = obj["iCustNum"]
      """  The Customer ID if available.  Can be blank.  """  
      self.iQuoteNum:int = obj["iQuoteNum"]
      """  The Quote Number if available.  Can be zero.  """  
      self.iVendorNum:int = obj["iVendorNum"]
      """  The Vendor ID if available.  Can be blank.  """  
      pass

class SortByData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cSortByList:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCRMCallTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCRMCallTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CRMCallTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UserIsAuthorized_input:
   """ Required : 
   cSalesRepCode
   """  
   def __init__(self, obj):
      self.cSalesRepCode:str = obj["cSalesRepCode"]
      """  The SalesRep code  """  
      pass

class UserIsAuthorized_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

