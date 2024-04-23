import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.EngWorkBenchSvc
# Description: Engineering Workbench Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_EngWorkBenches(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EngWorkBenches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EngWorkBenches
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/EngWorkBenches",headers=creds) as resp:
           return await resp.json()

async def post_EngWorkBenches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EngWorkBenches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOGroupRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOGroupRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/EngWorkBenches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EngWorkBenches_Company_GroupID(Company, GroupID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EngWorkBench item
   Description: Calls GetByID to retrieve the EngWorkBench item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EngWorkBench
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/EngWorkBenches(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EngWorkBenches_Company_GroupID(Company, GroupID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EngWorkBench for the service
   Description: Calls UpdateExt to update EngWorkBench. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EngWorkBench
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOGroupRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/EngWorkBenches(" + Company + "," + GroupID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EngWorkBenches_Company_GroupID(Company, GroupID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EngWorkBench item
   Description: Call UpdateExt to delete EngWorkBench item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EngWorkBench
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/EngWorkBenches(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EngWorkBenches_Company_GroupID_ECORevs(Company, GroupID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECORevs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECORevs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECORevRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/EngWorkBenches(" + Company + "," + GroupID + ")/ECORevs",headers=creds) as resp:
           return await resp.json()

async def get_EngWorkBenches_Company_GroupID_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECORev item
   Description: Calls GetByID to retrieve the ECORev item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECORev1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECORevRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/EngWorkBenches(" + Company + "," + GroupID + ")/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EngWorkBenches_Company_GroupID_ECOGroupAttches(Company, GroupID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECOGroupAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOGroupAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOGroupAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/EngWorkBenches(" + Company + "," + GroupID + ")/ECOGroupAttches",headers=creds) as resp:
           return await resp.json()

async def get_EngWorkBenches_Company_GroupID_ECOGroupAttches_Company_GroupID_DrawingSeq(Company, GroupID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOGroupAttch item
   Description: Calls GetByID to retrieve the ECOGroupAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOGroupAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOGroupAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/EngWorkBenches(" + Company + "," + GroupID + ")/ECOGroupAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECORevs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECORevs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECORevs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECORevRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs",headers=creds) as resp:
           return await resp.json()

async def post_ECORevs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECORevs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECORevRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECORevRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECORev item
   Description: Calls GetByID to retrieve the ECORev item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECORev
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECORevRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECORev for the service
   Description: Calls UpdateExt to update ECORev. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECORev
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECORevRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECORev item
   Description: Call UpdateExt to delete ECORev item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECORev
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_ECOCOParts(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECOCOParts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOCOParts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOCOPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")/ECOCOParts",headers=creds) as resp:
           return await resp.json()

async def get_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_ECOCOParts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_CoPartNum(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, CoPartNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOCOPart item
   Description: Calls GetByID to retrieve the ECOCOPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOCOPart1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param CoPartNum: Desc: CoPartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOCOPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")/ECOCOParts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + CoPartNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_ECOMtls(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECOMtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOMtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")/ECOMtls",headers=creds) as resp:
           return await resp.json()

async def get_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOMtl item
   Description: Calls GetByID to retrieve the ECOMtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_ECOOprs(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECOOprs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOOprs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")/ECOOprs",headers=creds) as resp:
           return await resp.json()

async def get_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOOpr item
   Description: Calls GetByID to retrieve the ECOOpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOpr1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_ECORevAttches(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECORevAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECORevAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECORevAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")/ECORevAttches",headers=creds) as resp:
           return await resp.json()

async def get_ECORevs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_ECORevAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_DrawingSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECORevAttch item
   Description: Calls GetByID to retrieve the ECORevAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECORevAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECORevAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")/ECORevAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOCOParts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECOCOParts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOCOParts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOCOPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOCOParts",headers=creds) as resp:
           return await resp.json()

async def post_ECOCOParts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOCOParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOCOPartRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOCOPartRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOCOParts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECOCOParts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_CoPartNum(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, CoPartNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOCOPart item
   Description: Calls GetByID to retrieve the ECOCOPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOCOPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param CoPartNum: Desc: CoPartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOCOPartRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOCOParts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + CoPartNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECOCOParts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_CoPartNum(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, CoPartNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECOCOPart for the service
   Description: Calls UpdateExt to update ECOCOPart. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOCOPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param CoPartNum: Desc: CoPartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOCOPartRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOCOParts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + CoPartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECOCOParts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_CoPartNum(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, CoPartNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECOCOPart item
   Description: Call UpdateExt to delete ECOCOPart item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOCOPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param CoPartNum: Desc: CoPartNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOCOParts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + CoPartNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOMtls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECOMtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOMtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls",headers=creds) as resp:
           return await resp.json()

async def post_ECOMtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOMtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOMtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOMtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOMtl item
   Description: Calls GetByID to retrieve the ECOMtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECOMtl for the service
   Description: Calls UpdateExt to update ECOMtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOMtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOMtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECOMtl item
   Description: Call UpdateExt to delete ECOMtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOMtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_ECOMtlInsps(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECOMtlInsps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOMtlInsps1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")/ECOMtlInsps",headers=creds) as resp:
           return await resp.json()

async def get_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_ECOMtlInsps_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_PlanSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, PlanSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOMtlInsp item
   Description: Calls GetByID to retrieve the ECOMtlInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtlInsp1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")/ECOMtlInsps(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + PlanSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_ECOMtlRefDes(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECOMtlRefDes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOMtlRefDes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlRefDesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")/ECOMtlRefDes",headers=creds) as resp:
           return await resp.json()

async def get_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_ECOMtlRefDes_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RefDesSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, RefDesSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOMtlRefDe item
   Description: Calls GetByID to retrieve the ECOMtlRefDe item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtlRefDe1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param RefDesSeq: Desc: RefDesSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlRefDesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")/ECOMtlRefDes(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RefDesSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_ECOMtlRestrictions(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECOMtlRestrictions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOMtlRestrictions1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlRestrictionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")/ECOMtlRestrictions",headers=creds) as resp:
           return await resp.json()

async def get_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_ECOMtlRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RestrictionTypeID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, RestrictionTypeID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOMtlRestriction item
   Description: Calls GetByID to retrieve the ECOMtlRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtlRestriction1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlRestrictionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")/ECOMtlRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RestrictionTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_ECOMtlAttches(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECOMtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOMtlAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")/ECOMtlAttches",headers=creds) as resp:
           return await resp.json()

async def get_ECOMtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_ECOMtlAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_DrawingSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOMtlAttch item
   Description: Calls GetByID to retrieve the ECOMtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtlAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + ")/ECOMtlAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOMtlInsps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECOMtlInsps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOMtlInsps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlInsps",headers=creds) as resp:
           return await resp.json()

async def post_ECOMtlInsps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOMtlInsps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOMtlInspRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOMtlInspRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlInsps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECOMtlInsps_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_PlanSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, PlanSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOMtlInsp item
   Description: Calls GetByID to retrieve the ECOMtlInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtlInsp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlInsps(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + PlanSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECOMtlInsps_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_PlanSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, PlanSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECOMtlInsp for the service
   Description: Calls UpdateExt to update ECOMtlInsp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOMtlInsp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOMtlInspRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlInsps(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + PlanSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECOMtlInsps_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_PlanSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, PlanSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECOMtlInsp item
   Description: Call UpdateExt to delete ECOMtlInsp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOMtlInsp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlInsps(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + PlanSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOMtlRefDes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECOMtlRefDes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOMtlRefDes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlRefDesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRefDes",headers=creds) as resp:
           return await resp.json()

async def post_ECOMtlRefDes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOMtlRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOMtlRefDesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOMtlRefDesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRefDes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECOMtlRefDes_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RefDesSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, RefDesSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOMtlRefDe item
   Description: Calls GetByID to retrieve the ECOMtlRefDe item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtlRefDe
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param RefDesSeq: Desc: RefDesSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlRefDesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRefDes(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RefDesSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECOMtlRefDes_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RefDesSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, RefDesSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECOMtlRefDe for the service
   Description: Calls UpdateExt to update ECOMtlRefDe. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOMtlRefDe
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param RefDesSeq: Desc: RefDesSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOMtlRefDesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRefDes(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RefDesSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECOMtlRefDes_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RefDesSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, RefDesSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECOMtlRefDe item
   Description: Call UpdateExt to delete ECOMtlRefDe item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOMtlRefDe
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param RefDesSeq: Desc: RefDesSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRefDes(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RefDesSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOMtlRestrictions(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECOMtlRestrictions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOMtlRestrictions
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlRestrictionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictions",headers=creds) as resp:
           return await resp.json()

async def post_ECOMtlRestrictions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOMtlRestrictions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOMtlRestrictionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOMtlRestrictionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECOMtlRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RestrictionTypeID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, RestrictionTypeID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOMtlRestriction item
   Description: Calls GetByID to retrieve the ECOMtlRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtlRestriction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlRestrictionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RestrictionTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECOMtlRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RestrictionTypeID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, RestrictionTypeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECOMtlRestriction for the service
   Description: Calls UpdateExt to update ECOMtlRestriction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOMtlRestriction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOMtlRestrictionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RestrictionTypeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECOMtlRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RestrictionTypeID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, RestrictionTypeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECOMtlRestriction item
   Description: Call UpdateExt to delete ECOMtlRestriction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOMtlRestriction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RestrictionTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOMtlRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RestrictionTypeID_ECOMtlRestrictSubsts(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, RestrictionTypeID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECOMtlRestrictSubsts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOMtlRestrictSubsts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlRestrictSubstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RestrictionTypeID + ")/ECOMtlRestrictSubsts",headers=creds) as resp:
           return await resp.json()

async def get_ECOMtlRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RestrictionTypeID_ECOMtlRestrictSubsts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RestrictionTypeID_SubstanceID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, RestrictionTypeID, SubstanceID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOMtlRestrictSubst item
   Description: Calls GetByID to retrieve the ECOMtlRestrictSubst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtlRestrictSubst1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param SubstanceID: Desc: SubstanceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlRestrictSubstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RestrictionTypeID + ")/ECOMtlRestrictSubsts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RestrictionTypeID + "," + SubstanceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOMtlRestrictSubsts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECOMtlRestrictSubsts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOMtlRestrictSubsts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlRestrictSubstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictSubsts",headers=creds) as resp:
           return await resp.json()

async def post_ECOMtlRestrictSubsts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOMtlRestrictSubsts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOMtlRestrictSubstRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOMtlRestrictSubstRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictSubsts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECOMtlRestrictSubsts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RestrictionTypeID_SubstanceID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, RestrictionTypeID, SubstanceID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOMtlRestrictSubst item
   Description: Calls GetByID to retrieve the ECOMtlRestrictSubst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtlRestrictSubst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param SubstanceID: Desc: SubstanceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlRestrictSubstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictSubsts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RestrictionTypeID + "," + SubstanceID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECOMtlRestrictSubsts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RestrictionTypeID_SubstanceID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, RestrictionTypeID, SubstanceID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECOMtlRestrictSubst for the service
   Description: Calls UpdateExt to update ECOMtlRestrictSubst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOMtlRestrictSubst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param SubstanceID: Desc: SubstanceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOMtlRestrictSubstRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictSubsts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RestrictionTypeID + "," + SubstanceID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECOMtlRestrictSubsts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_RestrictionTypeID_SubstanceID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, RestrictionTypeID, SubstanceID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECOMtlRestrictSubst item
   Description: Call UpdateExt to delete ECOMtlRestrictSubst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOMtlRestrictSubst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param SubstanceID: Desc: SubstanceID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlRestrictSubsts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + RestrictionTypeID + "," + SubstanceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOMtlAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECOMtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOMtlAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOMtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlAttches",headers=creds) as resp:
           return await resp.json()

async def post_ECOMtlAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOMtlAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOMtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOMtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECOMtlAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_DrawingSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOMtlAttch item
   Description: Calls GetByID to retrieve the ECOMtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOMtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOMtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECOMtlAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_DrawingSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECOMtlAttch for the service
   Description: Calls UpdateExt to update ECOMtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOMtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOMtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECOMtlAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_MtlSeq_DrawingSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, MtlSeq, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECOMtlAttch item
   Description: Call UpdateExt to delete ECOMtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOMtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param MtlSeq: Desc: MtlSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOMtlAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + MtlSeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECOOprs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOOprs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs",headers=creds) as resp:
           return await resp.json()

async def post_ECOOprs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOOprs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOOprRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOOprRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOOpr item
   Description: Calls GetByID to retrieve the ECOOpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECOOpr for the service
   Description: Calls UpdateExt to update ECOOpr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOOpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOOprRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECOOpr item
   Description: Call UpdateExt to delete ECOOpr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOOpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOprActions(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECOOprActions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOOprActions1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOprActions",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOprActions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ActionSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, ActionSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOOprAction item
   Description: Calls GetByID to retrieve the ECOOprAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprAction1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOprActions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + ActionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOprInsps(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECOOprInsps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOOprInsps1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOprInsps",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOprInsps_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_PlanSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, PlanSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOOprInsp item
   Description: Calls GetByID to retrieve the ECOOprInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprInsp1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOprInsps(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + PlanSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOprMachParams(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECOOprMachParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOOprMachParams1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprMachParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOprMachParams",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOprMachParams_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_MachParamSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, MachParamSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOOprMachParam item
   Description: Calls GetByID to retrieve the ECOOprMachParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprMachParam1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param MachParamSeq: Desc: MachParamSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprMachParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOprMachParams(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + MachParamSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOpDtls(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECOOpDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOOpDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOpDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOpDtls",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOpDtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_OpDtlSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, OpDtlSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOOpDtl item
   Description: Calls GetByID to retrieve the ECOOpDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOpDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param OpDtlSeq: Desc: OpDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOpDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOpDtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + OpDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOprRestrictions(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECOOprRestrictions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOOprRestrictions1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprRestrictionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOprRestrictions",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOprRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_RestrictionTypeID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, RestrictionTypeID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOOprRestriction item
   Description: Calls GetByID to retrieve the ECOOprRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprRestriction1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprRestrictionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOprRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + RestrictionTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOprAttches(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECOOprAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOOprAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOprAttches",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprs_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ECOOprAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_DrawingSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOOprAttch item
   Description: Calls GetByID to retrieve the ECOOprAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprs(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + ")/ECOOprAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprActions(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECOOprActions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOOprActions
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActions",headers=creds) as resp:
           return await resp.json()

async def post_ECOOprActions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOOprActions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOOprActionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOOprActionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECOOprActions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ActionSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, ActionSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOOprAction item
   Description: Calls GetByID to retrieve the ECOOprAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprAction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + ActionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECOOprActions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ActionSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, ActionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECOOprAction for the service
   Description: Calls UpdateExt to update ECOOprAction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOOprAction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOOprActionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + ActionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECOOprActions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ActionSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, ActionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECOOprAction item
   Description: Call UpdateExt to delete ECOOprAction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOOprAction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ActionSeq: Desc: ActionSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + ActionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprActions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ActionSeq_ECOOprActionParams(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, ActionSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECOOprActionParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOOprActionParams1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprActionParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + ActionSeq + ")/ECOOprActionParams",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprActions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ActionSeq_ECOOprActionParams_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ActionSeq_ActionParamSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, ActionSeq, ActionParamSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOOprActionParam item
   Description: Calls GetByID to retrieve the ECOOprActionParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprActionParam1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param ActionParamSeq: Desc: ActionParamSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprActionParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + ActionSeq + ")/ECOOprActionParams(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + ActionSeq + "," + ActionParamSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprActionParams(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECOOprActionParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOOprActionParams
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprActionParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActionParams",headers=creds) as resp:
           return await resp.json()

async def post_ECOOprActionParams(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOOprActionParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOOprActionParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOOprActionParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActionParams", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECOOprActionParams_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ActionSeq_ActionParamSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, ActionSeq, ActionParamSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOOprActionParam item
   Description: Calls GetByID to retrieve the ECOOprActionParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprActionParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param ActionParamSeq: Desc: ActionParamSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprActionParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActionParams(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + ActionSeq + "," + ActionParamSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECOOprActionParams_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ActionSeq_ActionParamSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, ActionSeq, ActionParamSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECOOprActionParam for the service
   Description: Calls UpdateExt to update ECOOprActionParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOOprActionParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param ActionParamSeq: Desc: ActionParamSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOOprActionParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActionParams(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + ActionSeq + "," + ActionParamSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECOOprActionParams_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_ActionSeq_ActionParamSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, ActionSeq, ActionParamSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECOOprActionParam item
   Description: Call UpdateExt to delete ECOOprActionParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOOprActionParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param ActionParamSeq: Desc: ActionParamSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprActionParams(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + ActionSeq + "," + ActionParamSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprInsps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECOOprInsps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOOprInsps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprInsps",headers=creds) as resp:
           return await resp.json()

async def post_ECOOprInsps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOOprInsps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOOprInspRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOOprInspRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprInsps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECOOprInsps_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_PlanSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, PlanSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOOprInsp item
   Description: Calls GetByID to retrieve the ECOOprInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprInsp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprInsps(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + PlanSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECOOprInsps_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_PlanSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, PlanSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECOOprInsp for the service
   Description: Calls UpdateExt to update ECOOprInsp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOOprInsp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOOprInspRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprInsps(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + PlanSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECOOprInsps_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_PlanSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, PlanSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECOOprInsp item
   Description: Call UpdateExt to delete ECOOprInsp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOOprInsp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param PlanSeq: Desc: PlanSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprInsps(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + PlanSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprMachParams(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECOOprMachParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOOprMachParams
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprMachParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprMachParams",headers=creds) as resp:
           return await resp.json()

async def post_ECOOprMachParams(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOOprMachParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOOprMachParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOOprMachParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprMachParams", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECOOprMachParams_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_MachParamSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, MachParamSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOOprMachParam item
   Description: Calls GetByID to retrieve the ECOOprMachParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprMachParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param MachParamSeq: Desc: MachParamSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprMachParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprMachParams(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + MachParamSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECOOprMachParams_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_MachParamSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, MachParamSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECOOprMachParam for the service
   Description: Calls UpdateExt to update ECOOprMachParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOOprMachParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param MachParamSeq: Desc: MachParamSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOOprMachParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprMachParams(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + MachParamSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECOOprMachParams_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_MachParamSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, MachParamSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECOOprMachParam item
   Description: Call UpdateExt to delete ECOOprMachParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOOprMachParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param MachParamSeq: Desc: MachParamSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprMachParams(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + MachParamSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOOpDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECOOpDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOOpDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOpDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOpDtls",headers=creds) as resp:
           return await resp.json()

async def post_ECOOpDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOOpDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOOpDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOOpDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOpDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECOOpDtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_OpDtlSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, OpDtlSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOOpDtl item
   Description: Calls GetByID to retrieve the ECOOpDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOpDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param OpDtlSeq: Desc: OpDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOpDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOpDtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + OpDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECOOpDtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_OpDtlSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, OpDtlSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECOOpDtl for the service
   Description: Calls UpdateExt to update ECOOpDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOOpDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param OpDtlSeq: Desc: OpDtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOOpDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOpDtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + OpDtlSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECOOpDtls_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_OpDtlSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, OpDtlSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECOOpDtl item
   Description: Call UpdateExt to delete ECOOpDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOOpDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param OpDtlSeq: Desc: OpDtlSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOpDtls(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + OpDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprRestrictions(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECOOprRestrictions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOOprRestrictions
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprRestrictionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictions",headers=creds) as resp:
           return await resp.json()

async def post_ECOOprRestrictions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOOprRestrictions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOOprRestrictionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOOprRestrictionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECOOprRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_RestrictionTypeID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, RestrictionTypeID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOOprRestriction item
   Description: Calls GetByID to retrieve the ECOOprRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprRestriction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprRestrictionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + RestrictionTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECOOprRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_RestrictionTypeID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, RestrictionTypeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECOOprRestriction for the service
   Description: Calls UpdateExt to update ECOOprRestriction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOOprRestriction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOOprRestrictionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + RestrictionTypeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECOOprRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_RestrictionTypeID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, RestrictionTypeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECOOprRestriction item
   Description: Call UpdateExt to delete ECOOprRestriction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOOprRestriction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + RestrictionTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_RestrictionTypeID_ECOOprRestrictSubsts(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, RestrictionTypeID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ECOOprRestrictSubsts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ECOOprRestrictSubsts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprRestrictSubstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + RestrictionTypeID + ")/ECOOprRestrictSubsts",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprRestrictions_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_RestrictionTypeID_ECOOprRestrictSubsts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_RestrictionTypeID_SubstanceID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, RestrictionTypeID, SubstanceID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOOprRestrictSubst item
   Description: Calls GetByID to retrieve the ECOOprRestrictSubst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprRestrictSubst1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param SubstanceID: Desc: SubstanceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprRestrictSubstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictions(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + RestrictionTypeID + ")/ECOOprRestrictSubsts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + RestrictionTypeID + "," + SubstanceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprRestrictSubsts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECOOprRestrictSubsts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOOprRestrictSubsts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprRestrictSubstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictSubsts",headers=creds) as resp:
           return await resp.json()

async def post_ECOOprRestrictSubsts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOOprRestrictSubsts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOOprRestrictSubstRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOOprRestrictSubstRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictSubsts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECOOprRestrictSubsts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_RestrictionTypeID_SubstanceID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, RestrictionTypeID, SubstanceID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOOprRestrictSubst item
   Description: Calls GetByID to retrieve the ECOOprRestrictSubst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprRestrictSubst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param SubstanceID: Desc: SubstanceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprRestrictSubstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictSubsts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + RestrictionTypeID + "," + SubstanceID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECOOprRestrictSubsts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_RestrictionTypeID_SubstanceID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, RestrictionTypeID, SubstanceID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECOOprRestrictSubst for the service
   Description: Calls UpdateExt to update ECOOprRestrictSubst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOOprRestrictSubst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param SubstanceID: Desc: SubstanceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOOprRestrictSubstRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictSubsts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + RestrictionTypeID + "," + SubstanceID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECOOprRestrictSubsts_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_RestrictionTypeID_SubstanceID(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, RestrictionTypeID, SubstanceID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECOOprRestrictSubst item
   Description: Call UpdateExt to delete ECOOprRestrictSubst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOOprRestrictSubst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param SubstanceID: Desc: SubstanceID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprRestrictSubsts(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + RestrictionTypeID + "," + SubstanceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOOprAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECOOprAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOOprAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOOprAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprAttches",headers=creds) as resp:
           return await resp.json()

async def post_ECOOprAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOOprAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOOprAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOOprAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECOOprAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_DrawingSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOOprAttch item
   Description: Calls GetByID to retrieve the ECOOprAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOOprAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOOprAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECOOprAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_DrawingSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECOOprAttch for the service
   Description: Calls UpdateExt to update ECOOprAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOOprAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOOprAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECOOprAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_OprSeq_DrawingSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, OprSeq, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECOOprAttch item
   Description: Call UpdateExt to delete ECOOprAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOOprAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param OprSeq: Desc: OprSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOOprAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + OprSeq + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECORevAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECORevAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECORevAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECORevAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevAttches",headers=creds) as resp:
           return await resp.json()

async def post_ECORevAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECORevAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECORevAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECORevAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECORevAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_DrawingSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECORevAttch item
   Description: Calls GetByID to retrieve the ECORevAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECORevAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECORevAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECORevAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_DrawingSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECORevAttch for the service
   Description: Calls UpdateExt to update ECORevAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECORevAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECORevAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECORevAttches_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_DrawingSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECORevAttch item
   Description: Call UpdateExt to delete ECORevAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECORevAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECORevAttches(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOGroupAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECOGroupAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOGroupAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOGroupAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOGroupAttches",headers=creds) as resp:
           return await resp.json()

async def post_ECOGroupAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOGroupAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOGroupAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOGroupAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOGroupAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECOGroupAttches_Company_GroupID_DrawingSeq(Company, GroupID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOGroupAttch item
   Description: Calls GetByID to retrieve the ECOGroupAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOGroupAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOGroupAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOGroupAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECOGroupAttches_Company_GroupID_DrawingSeq(Company, GroupID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECOGroupAttch for the service
   Description: Calls UpdateExt to update ECOGroupAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOGroupAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOGroupAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOGroupAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECOGroupAttches_Company_GroupID_DrawingSeq(Company, GroupID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECOGroupAttch item
   Description: Call UpdateExt to delete ECOGroupAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOGroupAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOGroupAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOImports(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECOImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOImports
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOImports",headers=creds) as resp:
           return await resp.json()

async def post_ECOImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECOImports_PartNum(PartNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOImport item
   Description: Calls GetByID to retrieve the ECOImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOImport
      :param PartNum: Desc: PartNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOImports(" + PartNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECOImports_PartNum(PartNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECOImport for the service
   Description: Calls UpdateExt to update ECOImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOImport
      :param PartNum: Desc: PartNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOImports(" + PartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECOImports_PartNum(PartNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECOImport item
   Description: Call UpdateExt to delete ECOImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOImport
      :param PartNum: Desc: PartNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOImports(" + PartNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ECOStages(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ECOStages items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ECOStages
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOStageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOStages",headers=creds) as resp:
           return await resp.json()

async def post_ECOStages(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ECOStages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ECOStageRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ECOStageRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOStages", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ECOStages_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_StageSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, StageSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ECOStage item
   Description: Calls GetByID to retrieve the ECOStage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ECOStage
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param StageSeq: Desc: StageSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ECOStageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOStages(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + StageSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ECOStages_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_StageSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, StageSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ECOStage for the service
   Description: Calls UpdateExt to update ECOStage. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ECOStage
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param StageSeq: Desc: StageSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ECOStageRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOStages(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + StageSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ECOStages_Company_GroupID_PartNum_RevisionNum_AltMethod_ProcessMfgID_StageSeq(Company, GroupID, PartNum, RevisionNum, AltMethod, ProcessMfgID, StageSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ECOStage item
   Description: Call UpdateExt to delete ECOStage item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ECOStage
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param StageSeq: Desc: StageSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/ECOStages(" + Company + "," + GroupID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + "," + StageSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ECOGroupListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseECOGroup, whereClauseECOGroupAttch, whereClauseECORev, whereClauseECORevAttch, whereClauseECOCOPart, whereClauseECOMtl, whereClauseECOMtlAttch, whereClauseECOMtlInsp, whereClauseECOMtlRefDes, whereClauseECOMtlRestriction, whereClauseECOMtlRestrictSubst, whereClauseECOOpr, whereClauseECOOprAttch, whereClauseECOOprAction, whereClauseECOOprActionParam, whereClauseECOOprInsp, whereClauseECOOprMachParam, whereClauseECOOpDtl, whereClauseECOOprRestriction, whereClauseECOOprRestrictSubst, whereClauseECOImport, whereClauseECOStage, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseECOGroup=" + whereClauseECOGroup
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECOGroupAttch=" + whereClauseECOGroupAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECORev=" + whereClauseECORev
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECORevAttch=" + whereClauseECORevAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECOCOPart=" + whereClauseECOCOPart
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECOMtl=" + whereClauseECOMtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECOMtlAttch=" + whereClauseECOMtlAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECOMtlInsp=" + whereClauseECOMtlInsp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECOMtlRefDes=" + whereClauseECOMtlRefDes
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECOMtlRestriction=" + whereClauseECOMtlRestriction
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECOMtlRestrictSubst=" + whereClauseECOMtlRestrictSubst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECOOpr=" + whereClauseECOOpr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECOOprAttch=" + whereClauseECOOprAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECOOprAction=" + whereClauseECOOprAction
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECOOprActionParam=" + whereClauseECOOprActionParam
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECOOprInsp=" + whereClauseECOOprInsp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECOOprMachParam=" + whereClauseECOOprMachParam
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECOOpDtl=" + whereClauseECOOpDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECOOprRestriction=" + whereClauseECOOprRestriction
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECOOprRestrictSubst=" + whereClauseECOOprRestrictSubst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECOImport=" + whereClauseECOImport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseECOStage=" + whereClauseECOStage
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupID, epicorHeaders = None):
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
   params += "groupID=" + groupID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_UnLockAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnLockAll
   Description: This method unlocks all the revisions in a group.
This method runs the logic behind the old Vantage 6.1 Group>Lock All menu option.
   OperationID: UnLockAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnLockAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnLockAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnLockAllAndRefresh(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnLockAllAndRefresh
   Description: This Invokes UnLockAll() to lock all revisions followed by GetECOGroupECORevAndCheckUpdateLock() to refresh the data
   OperationID: UnLockAllAndRefresh
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnLockAllAndRefresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnLockAllAndRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateBill(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateBill
   Description: This method validate the bill for the revision.
This method runs the logic behind the old Vantage 6.1 Revision>Validate Bill menu option.
   OperationID: ValidateBill
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateBill_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBill_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateInspection(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateInspection
   Description: Method to validate the Inspection control fields. (EQM)
   OperationID: ValidateInspection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateInspection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateInspection_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateRefDes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateRefDes
   Description: Verify that there are no other ECOMtlRefDes records in the revision having the
same RefDes value if the ECORev.ValRefDes = true. Check the number of reference
designators are equal to the Required Ref Designators defined on ECOMtl.
   OperationID: ValidateRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateRefDes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRefDes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ViewCosts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ViewCosts
   Description: This method will return the data need to display Part Rev costs.
   OperationID: ViewCosts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ViewCosts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ViewCosts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateECORev(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateECORev
   OperationID: UpdateECORev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateECORev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateECORev_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateCurrentECORev(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateCurrentECORev
   OperationID: UpdateCurrentECORev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateCurrentECORev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCurrentECORev_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdatePartECORev(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdatePartECORev
   Description: UpdatePartECORev method used for PLM REST workflow
   OperationID: UpdatePartECORev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePartECORev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePartECORev_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateCurrentPartECORev(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateCurrentPartECORev
   Description: UpdateCurrentPartECORev method used for PLM REST workflow
   OperationID: UpdateCurrentPartECORev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateCurrentPartECORev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCurrentPartECORev_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetIfCurrentSiteHasExternalMES(epicorHeaders = None):
   """  
   Summary: Invoke method GetIfCurrentSiteHasExternalMES
   Description: Purpose:
Parameters:  none
Notes:
   OperationID: GetIfCurrentSiteHasExternalMES
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIfCurrentSiteHasExternalMES_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_RequestApproveExternalMESValidation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RequestApproveExternalMESValidation
   Description: MES Approval Validation
   OperationID: RequestApproveExternalMESValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RequestApproveExternalMESValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RequestApproveExternalMESValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsTopPartSalesKit(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsTopPartSalesKit
   Description: Checks if the top part is a Sales Kit
   OperationID: IsTopPartSalesKit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsTopPartSalesKit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsTopPartSalesKit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckRulesBeforeDelete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckRulesBeforeDelete
   Description: Validate if exists rules to display a warning that rules may be deleted
   OperationID: CheckRulesBeforeDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRulesBeforeDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRulesBeforeDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsWithCustomsBOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsWithCustomsBOM
   Description: Returns a Rows Dataset, which contains ECORev table filtered with PartRev.CNCustomsBOM=1 And not linked to CNCustomsHandbookHeader
   OperationID: GetRowsWithCustomsBOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsWithCustomsBOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsWithCustomsBOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingProcessMfgType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingProcessMfgType
   Description: Logic for when the recipe type is changing
   OperationID: OnChangingProcessMfgType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingProcessMfgType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingProcessMfgType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEcoMtlMtlAttributeSetID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEcoMtlMtlAttributeSetID
   OperationID: ChangeEcoMtlMtlAttributeSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEcoMtlMtlAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEcoMtlMtlAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingNumberOfPieces(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Logic for when the number of pieces is changing
   OperationID: OnChangingNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingSalvageNumberOfPieces(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingSalvageNumberOfPieces
   Description: Logic for when the salvage number of pieces is changing
   OperationID: OnChangingSalvageNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingSalvageNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSalvageNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEcoRevPartTypeCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEcoRevPartTypeCode
   Description: Returns the part's Type Code
   OperationID: GetEcoRevPartTypeCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEcoRevPartTypeCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEcoRevPartTypeCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTreeStructure(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTreeStructure
   Description: Returns TreeStructure for recipe
   OperationID: GetTreeStructure
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTreeStructure_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTreeStructure_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEcoMtlSalvageAttributeSetID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEcoMtlSalvageAttributeSetID
   OperationID: ChangeEcoMtlSalvageAttributeSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEcoMtlSalvageAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEcoMtlSalvageAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEcoOprAttributeSetID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEcoOprAttributeSetID
   OperationID: ChangeEcoOprAttributeSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEcoOprAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEcoOprAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessMassCheckout(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessMassCheckout
   Description: Process MassCheckout - loop to possibly create new revisions and
checkout for multiple parts
   OperationID: ProcessMassCheckout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessMassCheckout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessMassCheckout_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMassCheckout(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMassCheckout
   Description: Gets the default values for the MassCheck data table based on the part
number entered.
   OperationID: GetMassCheckout
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMassCheckout_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMassCheckout_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingMassCheckoutCreateNewRev(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingMassCheckoutCreateNewRev
   Description: Call this method when the CreateNewRev changes in MassCheckout
   OperationID: OnChangingMassCheckoutCreateNewRev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingMassCheckoutCreateNewRev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingMassCheckoutCreateNewRev_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingMassCheckoutRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingMassCheckoutRevisionNum
   Description: Call this method when either Revision changes in MassCheckout
   OperationID: OnChangingMassCheckoutRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingMassCheckoutRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingMassCheckoutRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingMtlRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingMtlRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingMtlRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingMtlRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingMtlRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingSalvageRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingSalvageRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingSalvageRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingSalvageRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSalvageRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingSubRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingSubRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingSubRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingSubRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSubRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECOGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECOGroup
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECOGroupAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECOGroupAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOGroupAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOGroupAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOGroupAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECORev(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECORev
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECORev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECORev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECORev_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECORevAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECORevAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECORevAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECORevAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECORevAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECOCOPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECOCOPart
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOCOPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOCOPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOCOPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECOMtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECOMtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECOMtlAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECOMtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOMtlAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOMtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOMtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECOMtlInsp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECOMtlInsp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOMtlInsp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOMtlInsp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOMtlInsp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECOMtlRefDes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECOMtlRefDes
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOMtlRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOMtlRefDes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOMtlRefDes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECOMtlRestriction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECOMtlRestriction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOMtlRestriction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOMtlRestriction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOMtlRestriction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECOMtlRestrictSubst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECOMtlRestrictSubst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOMtlRestrictSubst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOMtlRestrictSubst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOMtlRestrictSubst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECOOpr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECOOpr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECOOprAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECOOprAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOOprAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOOprAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOOprAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECOOprAction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECOOprAction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOOprAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOOprAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOOprAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECOOprActionParam(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECOOprActionParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOOprActionParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOOprActionParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOOprActionParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECOOprInsp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECOOprInsp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOOprInsp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOOprInsp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOOprInsp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECOOprMachParam(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECOOprMachParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOOprMachParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOOprMachParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOOprMachParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECOOpDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECOOpDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOOpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECOOprRestriction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECOOprRestriction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOOprRestriction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOOprRestriction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOOprRestriction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECOOprRestrictSubst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECOOprRestrictSubst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOOprRestrictSubst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOOprRestrictSubst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOOprRestrictSubst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECOStage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECOStage
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewECOStage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOStage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOStage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSchedulingBlocks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSchedulingBlocks
   OperationID: GetSchedulingBlocks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSchedulingBlocks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSchedulingBlocks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_getNextOpDtlSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method getNextOpDtlSeq
   OperationID: getNextOpDtlSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getNextOpDtlSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getNextOpDtlSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECOOprByStageNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECOOprByStageNumber
   Description: Inserts a new ECOOpr row in the DataSet with defaults populated, based on Stage Number.
   OperationID: GetNewECOOprByStageNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOOprByStageNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOOprByStageNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECOMtlByStageNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECOMtlByStageNumber
   Description: Inserts a new ECOMtl row in the DataSet with defaults populated, based on Stage Number.
   OperationID: GetNewECOMtlByStageNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECOMtlByStageNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECOMtlByStageNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddRefDesRange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddRefDesRange
   Description: Creates new ECOMtlRefDes records based on the ECOMtl dataset fields.
   OperationID: AddRefDesRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddRefDesRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddRefDesRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AllowApproveMethod(epicorHeaders = None):
   """  
   Summary: Invoke method AllowApproveMethod
   Description: This method exists soley for the purpose of allowing security for
approving a method to be defined
   OperationID: AllowApproveMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllowApproveMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_AllowUnapproveMethod(epicorHeaders = None):
   """  
   Summary: Invoke method AllowUnapproveMethod
   Description: This method exists soley for the purpose of allowing security for
unapproving a method to be defined
   OperationID: AllowUnapproveMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllowUnapproveMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ApproveAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ApproveAll
   Description: This methods approves all revisions within an ECOGroup and returns a results string
and returns an updated dataset if the user chooses to.
This method runs the logic behind the Vantage 6.1 Group>Approve All menu option.
   OperationID: ApproveAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApproveAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ApproveAllAndRefresh(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ApproveAllAndRefresh
   Description: Invokes ApproveAll() followed by GetECOGroupECORevAndCheckUpdateLock() to refresh the data
   OperationID: ApproveAllAndRefresh
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApproveAllAndRefresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveAllAndRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ApproveAndCheckInAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ApproveAndCheckInAll
   Description: This methods approves and checks in all revisions within an ECOGroup and returns a results string
and returns an updated dataset if the user chooses to.
This method runs the logic behind the Group>Approve and Check In All menu option.
   OperationID: ApproveAndCheckInAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApproveAndCheckInAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveAndCheckInAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOCoPartPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOCoPartPartNum
   Description: This method validates the ECOCoPart.CoPartNum and defaults fields associated with the partnum.
This method should run when the ECOCoPart.CoPartNum field changes.
   OperationID: ChangeECOCoPartPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOCoPartPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOCoPartPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOGroupGroupClosed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOGroupGroupClosed
   Description: This methods assigns fields associated with ECOGroup.GroupClosed changing.
If ECOGroup.GroupClosed changes to true, ClosedBy, ClosedDate, and ClosedTime gets populated.
This method should run before/at the time ECOGroup.GroupClosed field changes.
   OperationID: ChangeECOGroupGroupClosed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOGroupGroupClosed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOGroupGroupClosed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOGroupWorkflowGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOGroupWorkflowGroup
   Description: This methods assigns fields associated with ECOGroup.WFGroupID changing.
If ECOGroup.WFGroupID changes, verify and check if there is a default TaskSetID
associated with the WFGroupID and if so, populate ECOGroup.TaskSetID.
This method should run before/at the time ECOGroup.WFGroupID field changes.
   OperationID: ChangeECOGroupWorkflowGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOGroupWorkflowGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOGroupWorkflowGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOMtlFixedQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOMtlFixedQty
   Description: This methods assigns ECOMtl.EstScrap field when ECOMtl.FixedQty changes.
This method should run when the ECOMtl.FixedQty changes.
   OperationID: ChangeECOMtlFixedQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlFixedQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlFixedQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEcoMtlInspPlan(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEcoMtlInspPlan
   OperationID: ChangeEcoMtlInspPlan
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEcoMtlInspPlan_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEcoMtlInspPlan_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOMtlMtlPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOMtlMtlPartNum
   Description: This method assigns the associated fields when the ECOMtl.MtlPartNum field changes.
This method should run when changing the ECOMtl.MtlPartNum.
   OperationID: ChangeECOMtlMtlPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlMtlPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlMtlPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOMtlMtlSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOMtlMtlSeq
   Description: This method create a new ttECOMtl record and delete the existing one when changing
this component of the primary unique index and update the ecomtl.qq.
This method should run before changing the ECOMtl.MtlSeq.
   OperationID: ChangeECOMtlMtlSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlMtlSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlMtlSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOMtlPlanAsAsm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOMtlPlanAsAsm
   Description: This method assigns the associated fields when the ECOMtl.MtlPartNum field changes.
This method should run when changing the ECOMtl.MtlPartNum.
   OperationID: ChangeECOMtlPlanAsAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlPlanAsAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlPlanAsAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOMtlPullAsAsm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOMtlPullAsAsm
   Description: This method assigns the associated fields when the ECOMtl.MtlPartNum field changes.
This method should run when changing the ECOMtl.MtlPartNum.
   OperationID: ChangeECOMtlPullAsAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlPullAsAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlPullAsAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOMtlQtyPer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOMtlQtyPer
   Description: This methods assigns ECOMtl.ReqRefDes and ECOMtl.RDEndNum fields
when ECOMtl.QtyPer changes. This method should run when the ECOMtl.QtyPer changes.
   OperationID: ChangeECOMtlQtyPer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlQtyPer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlQtyPer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOMtlSalvageQtyPer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOMtlSalvageQtyPer
   Description: This methods updates ECOMtl Salvage Number of Pieces when ECOMtl.SalvageQtyPer changes.
This method should run when the ECOMtl.SalvageQtyPer changes.
   OperationID: ChangeECOMtlSalvageQtyPer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlSalvageQtyPer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlSalvageQtyPer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOMtlSalvageUM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOMtlSalvageUM
   Description: This methods updates ECOMtl Salvage Number of Pieces when ECOMtl.SalvageUM changes.
This method should run when the ECOMtl.SalvageUM changes.
   OperationID: ChangeECOMtlSalvageUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlSalvageUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlSalvageUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOMtlReassignSNAsm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOMtlReassignSNAsm
   Description: Validates that there is no other material with ReassignSNAsm field to TRUE
   OperationID: ChangeECOMtlReassignSNAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlReassignSNAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlReassignSNAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOMtlRelatedOperation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOMtlRelatedOperation
   Description: This methods assigns associated fields when ECOMtl.RelatedOperation changes.
This method should run when the ECOMtl.RelatedOperation changes.
   OperationID: ChangeECOMtlRelatedOperation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlRelatedOperation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlRelatedOperation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOMtlRelatedStage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOMtlRelatedStage
   Description: This methods assigns associated fields when ECOMtl.RelatedStage changes.
This method should run when the ECOMtl.RelatedStage changes.
   OperationID: ChangeECOMtlRelatedStage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlRelatedStage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlRelatedStage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOMtlReqRefDes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOMtlReqRefDes
   Description: This methods assigns ECOMtl.RDEndNum field when ECOMtl.ReqRefDes changes.
This method should run when the ECOMtl.ReqRefDes changes.
   OperationID: ChangeECOMtlReqRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlReqRefDes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlReqRefDes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOMtlRestriction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOMtlRestriction
   Description: This methods assigns associated fields when ECOMtlRestriction.RestrictionTypeID changes.
   OperationID: ChangeECOMtlRestriction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlRestriction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlRestriction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOMtlRFQNeeded(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOMtlRFQNeeded
   Description: This methods assigns ECOMtl.RFQVendQuotes field when ECOMtl.RFQNeeded changes.
This method should run when the ECOMtl.RFQNeeded changes.
   OperationID: ChangeECOMtlRFQNeeded
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlRFQNeeded_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlRFQNeeded_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOMtlSalvageMtlBurRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOMtlSalvageMtlBurRate
   Description: This methods assigns ECOMtl.SalvageEstMtlBurUnitCredit field when ECOMtl.SalvageMtlBurRate changes.
This method should run when the ECOMtl.SalvageMtlBurRate changes.
   OperationID: ChangeECOMtlSalvageMtlBurRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlSalvageMtlBurRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlSalvageMtlBurRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOMtlSalvagePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOMtlSalvagePartNum
   Description: This methods assigns associated fields when ECOMtl.SalvagePartNum changes.
This method should run when the ECOMtl.SalvagePartNum changes.
   OperationID: ChangeECOMtlSalvagePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlSalvagePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlSalvagePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOMtlSalvageUnitCredit(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOMtlSalvageUnitCredit
   Description: This methods assigns ECOMtl.SalvageEstMtlBurUnitCredit field when ECOMtl.SalvageUnitCredit changes.
This method should run when the ECOMtl.SalvageMtlBurRate changes.
   OperationID: ChangeECOMtlSalvageUnitCredit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlSalvageUnitCredit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlSalvageUnitCredit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOMtlSubstance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOMtlSubstance
   Description: This methods assigns associated fields when ECOMtlRestrictSubst.SubstanceID changes.
   OperationID: ChangeECOMtlSubstance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOMtlSubstance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOMtlSubstance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOOpDtlCapability(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOOpDtlCapability
   Description: Method to call when changing the Capability ID.  This method will update ECOOpDtl
to see if the labor and burden rates need to be reset.  Blank is a valid entry for
Capability ID.
   OperationID: ChangeECOOpDtlCapability
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOpDtlCapability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOpDtlCapability_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOOpDtlResourceGrpID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOOpDtlResourceGrpID
   Description: Method to call when changing the Resource Group ID.  Blank is a valid
entry for Resource Group ID.
   OperationID: ChangeECOOpDtlResourceGrpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOpDtlResourceGrpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOpDtlResourceGrpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOOpDtlResourceID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOOpDtlResourceID
   Description: Method to call when changing the Resource ID.  Blank is a valid entry for Resource ID.
   OperationID: ChangeECOOpDtlResourceID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOpDtlResourceID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOpDtlResourceID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOOprAutoReceive(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOOprAutoReceive
   Description: This method also returns a list of values/descriptions for the LaborEntryMethod dropdown
based on the value of the ECOOpr.AutoReceive field.  This does not change the actual
value of the ECOOpr.LaborEntryMethod field, just returns values for its dropdown list.
This method should run before/at the time ECOGroup.GroupClosed field changes.
   OperationID: ChangeECOOprAutoReceive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprAutoReceive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprAutoReceive_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOOprLaborEntryMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOOprLaborEntryMethod
   Description: Verification when changing the LaborEntryMethod field
   OperationID: ChangeECOOprLaborEntryMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprLaborEntryMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprLaborEntryMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOOprOpCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOOprOpCode
   Description: This method defaults/resets specific fields related to the new operation code.
This method should run when the ECOOpr.OpCode field changes.
   OperationID: ChangeECOOprOpCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprOpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprOpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOOprOprSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOOprOprSeq
   Description: This method will update all of the associated records to the ECOOpr if the
OprSeq field is changing.
This method should run before changing the ECOOpr.OprSeq.
   OperationID: ChangeECOOprOprSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOOprOpStdID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOOprOpStdID
   Description: This method defaults/resets the production standards when selecting an
Operation Standard
This method should run when the ECOOpr.OpStdID field changes.
   OperationID: ChangeECOOprOpStdID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprOpStdID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprOpStdID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOOprPrimaryProdOpDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOOprPrimaryProdOpDtl
   Description: This method defaults/resets the production standards when selecting Primary
Production Operation Detail.
This method should run when the ECOOpr.PrimaryProdOpDtl field changes.
   OperationID: ChangeECOOprPrimaryProdOpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprPrimaryProdOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprPrimaryProdOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOOprPrimarySetupOpDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOOprPrimarySetupOpDtl
   Description: This method defaults/resets the setup values when selecting Primary
Setup Operation Detail.
This method should run when the ECOOpr.PrimarySetupOpDtl field changes.
   OperationID: ChangeECOOprPrimarySetupOpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprPrimarySetupOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprPrimarySetupOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOOprRestriction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOOprRestriction
   Description: This methods assigns associated fields when ECOOprRestriction.RestrictionTypeID changes.
   OperationID: ChangeECOOprRestriction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprRestriction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprRestriction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOOprRFQNeeded(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOOprRFQNeeded
   Description: This methods assigns ECOOpr.RFQVendQuotes field when ECOOpr.RFQNeeded changes.
This method should run when the ECOOpr.RFQNeeded changes.
   OperationID: ChangeECOOprRFQNeeded
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprRFQNeeded_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprRFQNeeded_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOOprSNRequiredOpr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOOprSNRequiredOpr
   Description: Validates SNRequiredOpr flag to avoid to set it false if the prior operation has the flag set to true
The flag cannot be set to true if the part is not serial tracked also.
   OperationID: ChangeECOOprSNRequiredOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprSNRequiredOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprSNRequiredOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOOprStdFormat(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOOprStdFormat
   Description: This methods assigns ECOOpr.OpsPerPart a default value based on the StdFormat value.
   OperationID: ChangeECOOprStdFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprStdFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprStdFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOOprSubPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOOprSubPartNum
   Description: This methods assigns associated fields when ECOOpr.SubPartNum changes.
This method should run when the ECOOpr.SubPartNum changes.
   OperationID: ChangeECOOprSubPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprSubPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprSubPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOOprSubstance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOOprSubstance
   Description: This methods assigns associated fields when ECOOprRestrictSubst.SubstanceID changes.
   OperationID: ChangeECOOprSubstance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprSubstance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprSubstance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOOprVendorNumVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOOprVendorNumVendorID
   Description: This methods assigns associated fields when ECOOpr.VendorNumVendorID changes.
This method should run when the ECOOpr.VendorNumVendorID changes.
   OperationID: ChangeECOOprVendorNumVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOOprVendorNumVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOOprVendorNumVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECORevApproved(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECORevApproved
   Description: This methods assigns fields associated with ECORev.Approved changing.
This method should run before ECOGroup.Approved field changes.
   OperationID: ChangeECORevApproved
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECORevApproved_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECORevApproved_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangingECOOprAutoReceive(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangingECOOprAutoReceive
   Description: Verification when changing the AutoReceive field
   OperationID: ChangingECOOprAutoReceive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangingECOOprAutoReceive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangingECOOprAutoReceive_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckECOMtlMtlPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckECOMtlMtlPartNum
   Description: This methods checks the ECOMtl.MtlPartNum when it changes to see if any messages when
validating it arise.  Messages could be from the analysis code or if the user is trying to
use the parent part as a component of itself.
This method should run before changing the ECOMtl.MtlPartNum.
   OperationID: CheckECOMtlMtlPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECOMtlMtlPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECOMtlMtlPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPrePartInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPrePartInfo
   Description: The method is to be run on drag/drop of a part.
   OperationID: CheckPrePartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPrePartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPrePartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckChangeECOMtlMtlSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckChangeECOMtlMtlSeq
   Description: This method is called when ECOMtl MtlSeq is changed. It will validate the MtlSeq and, if this is not an added row,
it will delete and recreate the ECOMtl record and associated child records
   OperationID: CheckChangeECOMtlMtlSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckChangeECOMtlMtlSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckChangeECOMtlMtlSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckChangeECOOprOprSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckChangeECOOprOprSeq
   Description: This method is called when ECOOpr OprSeq is changed. It will validate the OprSeq and, if this is not an added row,
it will delete and recreate the ECOOpr record and associated child records
   OperationID: CheckChangeECOOprOprSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckChangeECOOprOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckChangeECOOprOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeECOStageStageSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeECOStageStageSeq
   Description: This method is called when ECOStage StageSeq is changed. It will validate the Stage and, if this is not an added row,
it will delete and recreate the Stage record and associated child records
   OperationID: ChangeECOStageStageSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeECOStageStageSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeECOStageStageSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckECOMtlMtlSeqRelatedOperation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckECOMtlMtlSeqRelatedOperation
   Description: This methods checks to see if the ECOMtl.MtlSeq has changed from the original ECOMtl.MtlSeq or
if the ECOMtl.RelatedOperation has changed from the original ECOMtl.RelatedOperation or
the ECOMtl.RelatedStage has changed from the original ECOMMtl.RelatedStage
and provides a message asking the user if they would like to set the current configuration
to unapproved if the MtlSeq, RelatedOperation or RelatedStage did change.  This method does not actually validate the
ECOMtl.MtlSeq, ECOMtl.RelatedOperation or ECOMtl.RelatedStage.
For RelatedOperation and RelatedStage, it is one or the other, i.e. both a RelatedOperation
and a RelatedStage should not be passed in.  The value to pass in is based on ECORev.UseStaging.
If this value is true, RelatedStage is used, otherwise RelatedOperation is used.
Actual validation is handle in the beforeupdate logic in a private method.
This method should run before changing the ECOMtl.MtlSeq or ECOMtl.RelatedOperation
   OperationID: CheckECOMtlMtlSeqRelatedOperation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECOMtlMtlSeqRelatedOperation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECOMtlMtlSeqRelatedOperation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckECOMtlPlanAsAsm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckECOMtlPlanAsAsm
   Description: This methods checks the ECOMtl.PlanAsAsm when it changes to see if any messages when
validating it arise.  Messages could be from the analysis code
This method should run before changing the ECOMtl.PlanAsAsm.
   OperationID: CheckECOMtlPlanAsAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECOMtlPlanAsAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECOMtlPlanAsAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckECOMtlPullAsAsm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckECOMtlPullAsAsm
   Description: This methods checks the ECOMtl.PullAsAsm when it changes to see if any messages when
validating it arise.  Messages could be from the analysis code
This method should run before changing the ECOMtl.PullAsAsm.
   OperationID: CheckECOMtlPullAsAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECOMtlPullAsAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECOMtlPullAsAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckECOMtlViewAsAsm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckECOMtlViewAsAsm
   Description: This methods checks the ECOMtl.ViewAsAsm when it changes to see if any messages when
validating it arise. This method should run before changing the ECOMtl.ViewAsAsm.
   OperationID: CheckECOMtlViewAsAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECOMtlViewAsAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECOMtlViewAsAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckECOOprOprSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckECOOprOprSeq
   Description: This methods checks to see if the ECOOpr.OprSeq has changed from the original ECOOpr.OprSeq
and provides a message asking the user if they would like to set the current configuration
to unapproved if the OprSeq did change.  This method does not actually validate the ECOOpr.OprSeq.
Actual validation is handle in the beforeupdate logic in a private method.
This method should run before changing the ECOOpr.OprSeq.
   OperationID: CheckECOOprOprSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECOOprOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECOOprOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckECOOprPrimaryProdOpDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckECOOprPrimaryProdOpDtl
   Description: This method validated the value of Primary Production Operation Detail.
This method should run when the ECOOpr.PrimaryProdOpDtl field changes.
   OperationID: CheckECOOprPrimaryProdOpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECOOprPrimaryProdOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECOOprPrimaryProdOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckECOOprPrimarySetupOpDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckECOOprPrimarySetupOpDtl
   Description: This method validated the value of Primary Setup Operation Detail.
This method should run when the ECOOpr.PrimarySetupOpDtl field changes.
   OperationID: CheckECOOprPrimarySetupOpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECOOprPrimarySetupOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECOOprPrimarySetupOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckECOOprPurPoint(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckECOOprPurPoint
   Description: This methods checks to see if the new ECOOpr.PurPoint has changed from the original
ECOOpr.PurPoint and validates the value.
This method should run before changing the ECOOpr.PurPoint.
   OperationID: CheckECOOprPurPoint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECOOprPurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECOOprPurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckECOOprVendorNumVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckECOOprVendorNumVendorID
   Description: This methods checks to see if the new ECOOpr.VendorNumVendorID has changed from the original
ECOOpr.VendorNumVendorID and validates the value.
This method should run before changing the ECOOpr.VendorNumVendorID.
   OperationID: CheckECOOprVendorNumVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECOOprVendorNumVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECOOprVendorNumVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckECORevApproved(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckECORevApproved
   Description: This methods checks if the BMSyst.VerifyPassword flag is set, and verifies a password
before the user is able to approve this revision.
This method should run before the ECORev.Approved field changes (ChangeECORevApproved).
   OperationID: CheckECORevApproved
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECORevApproved_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECORevApproved_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckChangeECORevApproved(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckChangeECORevApproved
   Description: This method is called when ECORev Approved flag is changed.  It will run the following methods:
CheckECORevApprovedChanging, CheckECORevApproved, ChangeECORevApproved
   OperationID: CheckChangeECORevApproved
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckChangeECORevApproved_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckChangeECORevApproved_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckECORevValRefDes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckECORevValRefDes
   Description: Verify that there are no other ECOMtlRefDes records in the revision having
the same RefDes value if the ECORev.ValRefDes = true. This method should
run before changing the ECORev.ValRefDes.
   OperationID: CheckECORevValRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECORevValRefDes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECORevValRefDes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckECORevApprovedChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckECORevApprovedChanging
   Description: Verify that there are no other EcoMtl or EcoOpr records in the revision with  missing or invalid attributes
This method should run before changing the ECORev.Approved.
   OperationID: CheckECORevApprovedChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckECORevApprovedChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckECORevApprovedChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckIn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckIn
   Description: This method checks in a single revision.
This method runs the logic behind the old Vantage 6.1 Revision>Check In menu option.
   OperationID: CheckIn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckIn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckInAndRefresh(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckInAndRefresh
   Description: Invokes CheckIn() followed by GetECOGroupECORevAndCheckUpdateLock() to refresh the data.
   OperationID: CheckInAndRefresh
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckInAndRefresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckInAndRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckInAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckInAll
   Description: This methods checks in all revisions within an ECOGroup and returns a results string
and returns an updated dataset if the user chooses to.
This method runs the logic behind the Vantage 6.1 Group>Check In All menu option.
   OperationID: CheckInAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckInAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckInAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckOut(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckOut
   Description: This method checks out a single revision
This method runs the logic behind the old Vantage 6.1 Revision>Check Out menu option.
   OperationID: CheckOut
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckOut_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOut_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckOutAndRefresh(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckOutAndRefresh
   Description: Invokes CheckOut() followed by GetECOGroupECORevAndCheckUpdateLock() to refresh the data.
   OperationID: CheckOutAndRefresh
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckOutAndRefresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOutAndRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckChangeECOCoPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckChangeECOCoPartNum
   Description: The method is called when ECOCOPart CoPartNum is changed.   It will run methods CheckPreECOCoPartInfo and ChangeECOCoPartPartNum
   OperationID: CheckChangeECOCoPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckChangeECOCoPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckChangeECOCoPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPreECOCoPartInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPreECOCoPartInfo
   Description: This method validates the ECOCoPart.CoPartNum is not serial tracked or a configured part.
   OperationID: CheckPreECOCoPartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPreECOCoPartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPreECOCoPartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClearAll
   Description: This method will delete all ECOMtl, ECOOpr and ECOOpDtl associated with the ECORev to clear all for.
When the method is finished running, it will run a GetById based on the
inputted Group ID. This will cause a refreshing of the dataset to reflect all of the changes.
   OperationID: ClearAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteRefDesRange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteRefDesRange
   Description: Deletes ECOMtlRefDes records based on the ECOMtl dataset fields.
   OperationID: DeleteRefDesRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteRefDesRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRefDesRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ECOGroupExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ECOGroupExists
   Description: This method accepts a ECOGroup.ECOGroupID and determines if the ECOGroupID exists
as a valid record in the database.
   OperationID: ECOGroupExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ECOGroupExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ECOGroupExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EcoOprInitSNReqSubConShip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EcoOprInitSNReqSubConShip
   Description: Method required to set the initial value of ECOOpr.SNRequiredSubConShip
   OperationID: EcoOprInitSNReqSubConShip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EcoOprInitSNReqSubConShip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EcoOprInitSNReqSubConShip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewECORevForProcessMfg(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewECORevForProcessMfg
   Description: Inserts a new ECORev row in the DataSet
   OperationID: GetNewECORevForProcessMfg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewECORevForProcessMfg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewECORevForProcessMfg_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportToPLM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportToPLM
   Description: This method accepts a ECOGroup.ECOGroupID and sends a xml message describing the ECO to PLM
   OperationID: ExportToPLM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportToPLM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportToPLM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExpressPartCheckOut(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExpressPartCheckOut
   Description: This method will generate an ECOGroup for the user to check out the part to if
an ECOGroup doesn't already exist for the user.  Once the ECOGroup is properly
created, the inputted part information will be checked out to the ECOGroup that was
created or to the one that already exists for the user.
   OperationID: ExpressPartCheckOut
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExpressPartCheckOut_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExpressPartCheckOut_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTaskSets(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTaskSets
   Description: This method gets the available TaskSets for the TaskSet combo in the
EngineeringWorkbenchEntry.
   OperationID: GetAvailTaskSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTaskSets_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetDatasetForTreeByRef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDatasetForTreeByRef
   Description: Same as GetDataSetForTree but expects ref EngWorkbenchTableset to improve performance within kinetic when merging large volumes of data.
            
This methods will return a dataset that will include PartRev, PartOpr, PartMtl and PartOpDtl if those
records exist for a ECOMtl and there is no ECORev, ECOOpr, ECOMtl and ECOOpDtl associated with it.
These added "Part" records will be able to be determined by the associated tables "IsPartRev",
"IsPartOpr", "IsPartMtl" or "IsPartOpDtl" field.  If this field is checked then the record in the dataset
was copied from the associated "part" table.  These "part" records will not be maintable as they
will not be "real" database records, just a picture of the "part" record for display purposes.
This method will also allow you to return the whole dataset or allow the user to specify how
far down the tree they would like to return possible "part" records for.
This method is different from the "GetRows" or "GetById" methods.  Those methods only return
maintainable "ECO" records.
   OperationID: GetDatasetForTreeByRef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDatasetForTreeByRef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatasetForTreeByRef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDatasetForTree(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDatasetForTree
   Description: This methods will return a dataset that will include PartRev, PartOpr, PartMtl and PartOpDtl if those
records exist for a ECOMtl and there is no ECORev, ECOOpr, ECOMtl and ECOOpDtl associated with it.
These added "Part" records will be able to be determined by the associated tables "IsPartRev",
"IsPartOpr", "IsPartMtl" or "IsPartOpDtl" field.  If this field is checked then the record in the dataset
was copied from the associated "part" table.  These "part" records will not be maintable as they
will not be "real" database records, just a picture of the "part" record for display purposes.
This method will also allow you to return the whole dataset or allow the user to specify how
far down the tree they would like to return possible "part" records for.
This method is different from the "GetRows" or "GetById" methods.  Those methods only return
maintainable "ECO" records.
   OperationID: GetDatasetForTree
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDatasetForTree_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatasetForTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDetailsFromImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDetailsFromImport
   Description: This method gets the details from an import file
This method runs the logic behind the old Vantage 6.1 Revision>Get Details>Import menu option
   OperationID: GetDetailsFromImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDetailsFromImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDetailsFromImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDetailsFromJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDetailsFromJob
   Description: This method gets the details from a job assembly.
This method runs the logic behind the old Vantage 6.1 Revision>Get Details>
Get From Job menu option.
   OperationID: GetDetailsFromJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDetailsFromJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDetailsFromJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDetailsFromMethods(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDetailsFromMethods
   Description: This method gets the details from a method.
This method runs the logic behind the old Vantage 6.1 Revision>Get Details>
Get From Methods menu option.
   OperationID: GetDetailsFromMethods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDetailsFromMethods_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDetailsFromMethods_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDetailsFromQuotes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDetailsFromQuotes
   Description: This method gets the details from a quote assembly.
This method runs the logic behind the old Vantage 6.1 Revision>Get Details>
Get From Quote menu option.
   OperationID: GetDetailsFromQuotes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDetailsFromQuotes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDetailsFromQuotes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDetailsOperations(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDetailsOperations
   Description: This method gets the details from operations for a revision.
This method runs the logic behind the old Vantage 6.1 Revision>Get Details>
Get Operations Details menu option.
   OperationID: GetDetailsOperations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDetailsOperations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDetailsOperations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetECORevData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetECORevData
   Description: This method returns the ECOGroup record and all associated ECORev records
based on the inputted GroupID and ipCheckOutStatus (yes = checked out, no = not checked out).
In some UI cases, this method will be used to replace the base GetByID.  This method
should improve the performance because it will not be bringing back a complete
dataset.
   OperationID: GetECORevData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetECORevData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetECORevData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetECOGroupAndECORev(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetECOGroupAndECORev
   Description: This method returns the ECOGroup record and all associated ECORev records
based on the inputted GroupID and ipCheckOutStatus (yes = checked out, no = not checked out).
In some UI cases, this method will be used to replace the base GetByID.  This method
should improve the performance because it will not be bringing back a complete
dataset.
   OperationID: GetECOGroupAndECORev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetECOGroupAndECORev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetECOGroupAndECORev_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetProjectRoles(epicorHeaders = None):
   """  
   Summary: Invoke method GetProjectRoles
   OperationID: GetProjectRoles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetProjectRoles_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GroupLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GroupLock
   Description: This method checks if a group doesn't have a lock and locks a group
   OperationID: GroupLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GroupLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GroupLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GroupUnLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GroupUnLock
   Description: This method deletes a lock on the group and revisions within a group.
   OperationID: GroupUnLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GroupUnLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GroupUnLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertBOMMtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertBOMMtl
   Description: This methods allows for the insertion of an engineering material for drag/drop functionality,
validates an ECORev record exists and can be updated.
   OperationID: InsertBOMMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertBOMMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertBOMMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertBOMMtlWithStageNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertBOMMtlWithStageNumber
   Description: This methods allows for the insertion of an engineering material for drag/drop functionality,
validates an ECORev record exists and can be updated.
   OperationID: InsertBOMMtlWithStageNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertBOMMtlWithStageNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertBOMMtlWithStageNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertBOMOpr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertBOMOpr
   Description: This methods allows for the insertion of an engineering operation for drag/drop functionality,
validates an ECORev record exists and can be updated.
   OperationID: InsertBOMOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertBOMOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertBOMOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertBOMOprWithStageNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertBOMOprWithStageNumber
   Description: This methods allows for the insertion of an engineering operation with stage number for drag/drop functionality,
validates an ECORev record exists and can be updated.
   OperationID: InsertBOMOprWithStageNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertBOMOprWithStageNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertBOMOprWithStageNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertMaterialDemilitedList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertMaterialDemilitedList
   Description: Method processes list of parts for drag/drop functionality,
method inserts parts which don't need a dialog and outputs list of the parts for UI dialog
   OperationID: InsertMaterialDemilitedList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertMaterialDemilitedList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertMaterialDemilitedList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertMaterialWithStageNumberDemilitedList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertMaterialWithStageNumberDemilitedList
   Description: Method processes list of parts for drag/drop functionality,
method inserts parts which don't need a dialog and outputs list of the parts for UI dialog
   OperationID: InsertMaterialWithStageNumberDemilitedList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertMaterialWithStageNumberDemilitedList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertMaterialWithStageNumberDemilitedList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertMaterialList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertMaterialList
   OperationID: InsertMaterialList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertMaterialList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertMaterialList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertMaterial(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertMaterial
   Description: This methods allows for the insertion on a part for drag/drop functionality,
validates a ECORev record exists and the part is valid.
   OperationID: InsertMaterial
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertMaterial_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertMaterial_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertOpDtlCapability(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertOpDtlCapability
   Description: This method allows for the insertion of Capability on an operation to create
ECOOpDtl for drag/drop functionality.
   OperationID: InsertOpDtlCapability
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOpDtlCapability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOpDtlCapability_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertOpDtlResGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertOpDtlResGroup
   Description: This method allows for the insertion of Resource Group on an operation to create
ECOOpDtl for drag/drop functionality.
   OperationID: InsertOpDtlResGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOpDtlResGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOpDtlResGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertOpDtlResource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertOpDtlResource
   Description: This method allows for the insertion of Resource on an operation to create
ECOOpDtl for drag/drop functionality.
   OperationID: InsertOpDtlResource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOpDtlResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOpDtlResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertOperationOP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertOperationOP
   Description: This methods allows for the insertion on an operation for drag/drop functionality
   OperationID: InsertOperationOP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOperationOP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOperationOP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertOperationOPWithStageNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertOperationOPWithStageNumber
   Description: This methods allows for the insertion on an operation for drag/drop functionality
   OperationID: InsertOperationOPWithStageNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOperationOPWithStageNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOperationOPWithStageNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertOprCapability(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertOprCapability
   Description: This method allows for the insertion of Capability on a revision to create
ECOOpr/ECOOpDtl for drag/drop functionality.
   OperationID: InsertOprCapability
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOprCapability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOprCapability_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertOprResGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertOprResGroup
   Description: This method allows for the insertion of ResourceGroup on a revision to create
ECOOpr/ECOOpDtl for drag/drop functionality.
   OperationID: InsertOprResGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOprResGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOprResGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertOprResource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertOprResource
   Description: This method allows for the insertion of Resource on a revision to create
ECOOpr/ECOOpDtl for drag/drop functionality.
   OperationID: InsertOprResource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertOprResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertOprResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadFileAndGetDetailsFromImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadFileAndGetDetailsFromImport
   Description: This method loads the imported CSV and invokes GetDetailsFromImport()
   OperationID: LoadFileAndGetDetailsFromImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadFileAndGetDetailsFromImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadFileAndGetDetailsFromImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LockAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LockAll
   Description: This method locks all the revisions in a group.
This method runs the logic behind the old Vantage 6.1 Group>Lock All menu option.
   OperationID: LockAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LockAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LockAllAndRefresh(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LockAllAndRefresh
   Description: This Invokes LockAll() to lock all revisions followed by GetECOGroupECORevAndCheckUpdateLock() to refresh the data
   OperationID: LockAllAndRefresh
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LockAllAndRefresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockAllAndRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MassAssign(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MassAssign
   Description: This method will mass assign ECOGroup.Description, ECOGroup.ECO, and ECOGRoup.EffectiveDate
to associated ECORev records and their ECORev.RevShortDesc, ECORev.ECO, and ECORev.EffectiveDate
fields respectively.
This method will assign values based on external fields in the ECOGroup dataset.
This method should run from the menu/task "Group>Mass Assign as it was in the old
Vantage 6.1.  When the method is finished running, it will run a GetById based on the
inputted Group ID. This will cause a refreshing of the dataset to reflect all of the changes.
   OperationID: MassAssign
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MassAssign_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassAssign_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MassAssignAndRefresh(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MassAssignAndRefresh
   Description: Invokes MassAssign() followed by GetECOGroupECORevAndCheckUpdateLock() to refresh the data
   OperationID: MassAssignAndRefresh
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MassAssignAndRefresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassAssignAndRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreGetDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreGetDetails
   Description: This method should be called right before the GetDetailsFromMethod method.  If a configured
part is entered, and the Prompt to Get Details from Resulting Configuration is checked
in the product configurator designer, a question should be displayed to the user asking
if they want to configure the part
   OperationID: PreGetDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreGetDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreGetDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreGetDetailsAndReturnConfigType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreGetDetailsAndReturnConfigType
   Description: This method should be called right before the GetDetailsFromMethod method when you need the config type returned.  If a configured
part is entered, and the Prompt to Get Details from Resulting Configuration is checked
in the product configurator designer, a question should be displayed to the user asking
if they want to configure the part
   OperationID: PreGetDetailsAndReturnConfigType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreGetDetailsAndReturnConfigType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreGetDetailsAndReturnConfigType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PromptForPassword(epicorHeaders = None):
   """  
   Summary: Invoke method PromptForPassword
   Description: This method checks the BMSyst record to see if a password should prompted for and then
validated by the ValidatePassword method in UserFile BO.  Run this before ApproveAll,
CheckECORevApproved, CheckIn, CheckInAll, and CheckOut.
   OperationID: PromptForPassword
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/PromptForPassword_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ResequenceMaterials(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ResequenceMaterials
   Description: This method will resequence the operations, update theECOMtl records.
This method should run from the menu/task "Material>Resequence" as it was in the old
Vantage 6.1.  When the method is finished running, it will run a GetById based on the
inputted Group ID. This will cause a refreshing of the dataset to reflect all of the changes.
   OperationID: ResequenceMaterials
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResequenceMaterials_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResequenceMaterials_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ResequenceOperations(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ResequenceOperations
   Description: This method will resequence the operations, update the ECORev and ECOMtl records.
This method should run from the menu/task "Operation>Resequence" as it was in the old
Vantage 6.1.  When the method is finished running, it will run a GetById based on the
inputted Group ID. This will cause a refreshing of the dataset to reflect all of the changes.
   OperationID: ResequenceOperations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResequenceOperations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResequenceOperations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RevisionLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RevisionLock
   Description: This method locks a single revision
This method runs the logic behind the old Vantage 6.1 Revision>Lock Revision menu option.
   OperationID: RevisionLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RevisionLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RevisionLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RevisionUnLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RevisionUnLock
   Description: This method unlocks a single revision
This method runs the logic behind the old Vantage 6.1 Revision>Unlock Revision menu option.
   OperationID: RevisionUnLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RevisionUnLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RevisionUnLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UndoCheckOut(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UndoCheckOut
   Description: This method undoes the check out of a revision
This method runs the logic behind the old Vantage 6.1 Revision>Undo Check Out menu option.
   OperationID: UndoCheckOut
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UndoCheckOut_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UndoCheckOut_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EngWorkBenchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOCOPartRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOCOPartRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOGroupAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOGroupAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOGroupListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOGroupListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOGroupRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOGroupRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOImportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOImportRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOMtlAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlInspRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOMtlInspRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRefDesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOMtlRefDesRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRestrictSubstRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOMtlRestrictSubstRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRestrictionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOMtlRestrictionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOMtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOMtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOpDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOOpDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprActionParamRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOOprActionParamRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprActionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOOprActionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOOprAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprInspRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOOprInspRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprMachParamRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOOprMachParamRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprRestrictSubstRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOOprRestrictSubstRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprRestrictionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOOprRestrictionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOOprRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOOprRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECORevAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECORevAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECORevRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECORevRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ECOStageRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ECOStageRow] = obj["value"]
      pass

class Erp_Tablesets_ECOCOPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID for the ECO Group to which this ECORev belongs.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.CoPartNum:str = obj["CoPartNum"]
      """  Companion PartNum identifies the Part that is manufactured along with the main part (ex: Right and Left parts)  """  
      self.CoRevisionNum:str = obj["CoRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the companion part, and is used as part of the primary key  """  
      self.PartsPerOp:int = obj["PartsPerOp"]
      """   Part Per Operation. Active only for Concurrent process
Jobs. Otherwise set to 1.  """  
      self.LbrCostBase:int = obj["LbrCostBase"]
      """   Defines an integer value which is used to calculate a
ratio for prorating the labor costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  """  
      self.MtlCostBase:int = obj["MtlCostBase"]
      """   Defines an integer value which is used to calculate a
ratio for prorating the material costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  """  
      self.IUM:str = obj["IUM"]
      """  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.PreventSugg:bool = obj["PreventSugg"]
      """  If true, MRP will not generate change suggestions for the co-part  """  
      self.PrimaryCost:bool = obj["PrimaryCost"]
      """  Indicates if the parent Part should be used as the primary costing method for the co-part  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.PartMasterPart:bool = obj["PartMasterPart"]
      self.ProcessMode:str = obj["ProcessMode"]
      self.EnablePreventSugg:bool = obj["EnablePreventSugg"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOGroupAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:str = obj["GroupID"]
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

class Erp_Tablesets_ECOGroupListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.Description:str = obj["Description"]
      """  The text description of the ECO Group  """  
      self.GroupClosed:bool = obj["GroupClosed"]
      """  Determines if the ECO group is closed or open.  """  
      self.CommentText:str = obj["CommentText"]
      """  ECO Group comments.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this ECO Group will become effective.  """  
      self.CompletionDate:str = obj["CompletionDate"]
      """  Date which this ECO Group was completed.  """  
      self.DueDate:str = obj["DueDate"]
      """  Date which this ECO group is due to be completed.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date which this ECO group was created.  Not maintainable by the user.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  UserID who created the ECO group.  Not maintainable by the user.  """  
      self.CreatedTime:int = obj["CreatedTime"]
      """  The time (in milliseconds) that the ECO group was created.  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  Date which this ECO group was closed.  Not maintainable by the user.  """  
      self.ClosedBy:str = obj["ClosedBy"]
      """  UserID who closed the ECO group.  Not maintainable by the user.  """  
      self.ClosedTime:int = obj["ClosedTime"]
      """  The time (in milliseconds) that the ECO group was closed.  """  
      self.ECO:str = obj["ECO"]
      """  Engineering Change Order Number. An optional field for reference.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set.  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  The identifier of the workflow stage.  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active milestone task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.CheckInAllowed:bool = obj["CheckInAllowed"]
      """  If FALSE then revisions in this group may not be checked in.  """  
      self.PrimeSalesRepCode:str = obj["PrimeSalesRepCode"]
      """  The primary workflow person associated with the group.  The people are stored in the SalesRep table.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group  """  
      self.CheckOutAllowed:bool = obj["CheckOutAllowed"]
      """  If false then check outs to the ECO Group are not allowed.  This is modified by workflow.  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  This indicates if the workflow for this group is complete.  """  
      self.SingleUser:bool = obj["SingleUser"]
      """  If TRUE then the Engineering Workbench is limited to one user per ECO Group.  If FALSE then individual revisions within a group can be locked.  """  
      self.GrpLocked:bool = obj["GrpLocked"]
      """  Indicates if this ECO Group is locked.  """  
      self.GrpLockedBy:str = obj["GrpLockedBy"]
      """  UserID that has the ECOGroup record locked  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MassAssignDesc:bool = obj["MassAssignDesc"]
      """  Logical to mass assign description to ecorevs  """  
      self.MassAssignECO:bool = obj["MassAssignECO"]
      """  Flag to mass assign ECO to ecorevs  """  
      self.MassAssignEffectiveDate:bool = obj["MassAssignEffectiveDate"]
      """  Flag to mass assign effective date across ecorevs  """  
      self.CanApproveAll:bool = obj["CanApproveAll"]
      """  Flag if Approve All is allowed for this group.  """  
      self.MultiBOMAllowed:bool = obj["MultiBOMAllowed"]
      """  Flag if Multi-BOM is Allowed based off of if mfgsys = VS then value of DCD-BM  """  
      self.CanCheckInAll:bool = obj["CanCheckInAll"]
      """  Flag if Check In All is allowed for this group  """  
      self.WFGroupIDDesc:str = obj["WFGroupIDDesc"]
      """  Description for the WFGroupID.  Based on the hardcoding of workflowtype, foreign link not available.  """  
      self.UseMethodForPartsInTree:bool = obj["UseMethodForPartsInTree"]
      """  If true use method for all parts in tree, otherwise use the part's default method  """  
      self.CurrentWFStageDesc:str = obj["CurrentWFStageDesc"]
      self.EnableCheckInAll:bool = obj["EnableCheckInAll"]
      """  Used for enable/disable the check in all option.  """  
      self.TaskSetIDTaskSetDescription:str = obj["TaskSetIDTaskSetDescription"]
      """  Description of the task set.  """  
      self.TaskSetIDWorkflowType:str = obj["TaskSetIDWorkflowType"]
      """  The type of workflow of this task set.  Possible values are "CRM" - CRM related tasks and "ECO" - ECO tasks  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOGroupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.Description:str = obj["Description"]
      """  The text description of the ECO Group  """  
      self.GroupClosed:bool = obj["GroupClosed"]
      """  Determines if the ECO group is closed or open.  """  
      self.CommentText:str = obj["CommentText"]
      """  ECO Group comments.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this ECO Group will become effective.  """  
      self.CompletionDate:str = obj["CompletionDate"]
      """  Date which this ECO Group was completed.  """  
      self.DueDate:str = obj["DueDate"]
      """  Date which this ECO group is due to be completed.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date which this ECO group was created.  Not maintainable by the user.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  UserID who created the ECO group.  Not maintainable by the user.  """  
      self.CreatedTime:int = obj["CreatedTime"]
      """  The time (in milliseconds) that the ECO group was created.  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  Date which this ECO group was closed.  Not maintainable by the user.  """  
      self.ClosedBy:str = obj["ClosedBy"]
      """  UserID who closed the ECO group.  Not maintainable by the user.  """  
      self.ClosedTime:int = obj["ClosedTime"]
      """  The time (in milliseconds) that the ECO group was closed.  """  
      self.ECO:str = obj["ECO"]
      """  Engineering Change Order Number. An optional field for reference.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set.  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  The identifier of the workflow stage.  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active milestone task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.CheckInAllowed:bool = obj["CheckInAllowed"]
      """  If FALSE then revisions in this group may not be checked in.  """  
      self.PrimeSalesRepCode:str = obj["PrimeSalesRepCode"]
      """  The primary workflow person associated with the group.  The people are stored in the SalesRep table.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group  """  
      self.CheckOutAllowed:bool = obj["CheckOutAllowed"]
      """  If false then check outs to the ECO Group are not allowed.  This is modified by workflow.  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  This indicates if the workflow for this group is complete.  """  
      self.SingleUser:bool = obj["SingleUser"]
      """  If TRUE then the Engineering Workbench is limited to one user per ECO Group.  If FALSE then individual revisions within a group can be locked.  """  
      self.GrpLocked:bool = obj["GrpLocked"]
      """  Indicates if this ECO Group is locked.  """  
      self.GrpLockedBy:str = obj["GrpLockedBy"]
      """  UserID that has the ECOGroup record locked  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MassAssignDesc:bool = obj["MassAssignDesc"]
      """  Logical to mass assign description to ecorevs  """  
      self.MassAssignECO:bool = obj["MassAssignECO"]
      """  Flag to mass assign ECO to ecorevs  """  
      self.MassAssignEffectiveDate:bool = obj["MassAssignEffectiveDate"]
      """  Flag to mass assign effective date across ecorevs  """  
      self.CanApproveAll:bool = obj["CanApproveAll"]
      """  Flag if Approve All is allowed for this group.  """  
      self.MultiBOMAllowed:bool = obj["MultiBOMAllowed"]
      """  Flag if Multi-BOM is Allowed based off of if mfgsys = VS then value of DCD-BM  """  
      self.CanCheckInAll:bool = obj["CanCheckInAll"]
      """  Flag if Check In All is allowed for this group  """  
      self.WFGroupIDDesc:str = obj["WFGroupIDDesc"]
      """  Description for the WFGroupID.  Based on the hardcoding of workflowtype, foreign link not available.  """  
      self.UseMethodForPartsInTree:bool = obj["UseMethodForPartsInTree"]
      """  If true use method for all parts in tree, otherwise use the part's default method  """  
      self.CurrentWFStageDesc:str = obj["CurrentWFStageDesc"]
      self.EnableCheckInAll:bool = obj["EnableCheckInAll"]
      """  Used for enable/disable the check in all option.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaskSetIDWorkflowType:str = obj["TaskSetIDWorkflowType"]
      self.TaskSetIDTaskSetDescription:str = obj["TaskSetIDTaskSetDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOImportRow:
   def __init__(self, obj):
      self.PartNum:str = obj["PartNum"]
      """  The part number.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part number.  """  
      self.TypeCode:str = obj["TypeCode"]
      """  The type code.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  The quantity per.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOMtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:str = obj["GroupID"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.AltMethod:str = obj["AltMethod"]
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      self.MtlSeq:int = obj["MtlSeq"]
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

class Erp_Tablesets_ECOMtlInspRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.PartNum:str = obj["PartNum"]
      """  Parent Part number to which this material item is a component of  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number of the part that this material item is a component of.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material record within a specific Job/Lot/Assembly. This is system assigned. The next available # is determined by reading last JobMtl record on the Job/Lot/Assembly and then adding one to it.  """  
      self.PlanSeq:int = obj["PlanSeq"]
      """  A sequence number that uniquely identifies the ECOMtlInsp record within the ECO material  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number).  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID.  Must be valid in the SpecHed table.  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      """  The original material sequence number at the time of check out. If this record was not created during check out this should remain 0.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOMtlRefDesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.RefDes:str = obj["RefDes"]
      """  Identifier of Reference Designator  """  
      self.RefDesSeq:int = obj["RefDesSeq"]
      """  Unique identifies the reference designator with the material sequence.  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The Part Number of the component material record for the related Parent Part.  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      """  The original material sequence number at the time of check out. If this record was not created during check out this should remain 0.  """  
      self.Side:str = obj["Side"]
      """  Free form side location. (Top, Bottom, Both, Level, etc)  """  
      self.XLocation:int = obj["XLocation"]
      """  X Coordinate of the reference designator  """  
      self.YLocation:int = obj["YLocation"]
      """  Y Coordinate of the reference designator  """  
      self.ZLocation:int = obj["ZLocation"]
      """  Z Coordinate of the reference designator  """  
      self.Rotation:int = obj["Rotation"]
      """  Rotation of the reference designator. Max value = 360.000  """  
      self.Description:str = obj["Description"]
      """  Designator Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOMtlRestrictSubstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.SubstanceID:str = obj["SubstanceID"]
      """  Substance identification.  """  
      self.Weight:int = obj["Weight"]
      """  Default weight of the substance per primary part of UOM  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  By default the primary UOM of the part.  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      """  The original material sequence number at the time of check out. If this record was not created during check out this should remain 0.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.Exempt:bool = obj["Exempt"]
      self.ExemptDate:str = obj["ExemptDate"]
      self.ExemptCertificate:str = obj["ExemptCertificate"]
      self.Manual:bool = obj["Manual"]
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The Part Number of the component material record for the related Parent Part.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.RestrictionDescription:str = obj["RestrictionDescription"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumPartDescription:str = obj["RevisionNumPartDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.SubstanceDescription:str = obj["SubstanceDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOMtlRestrictionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The Part Number of the component material record for the related Parent Part.  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      """  The original material sequence number at the time of check out. If this record was not created during check out this should remain 0.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.Weight:bool = obj["Weight"]
      """  Yes to display when the part has no net weight or when one or more of the selected has no weight.  """  
      self.Manual:bool = obj["Manual"]
      self.ComplianceDate:str = obj["ComplianceDate"]
      self.LastRollUp:str = obj["LastRollUp"]
      self.RollUpType:str = obj["RollUpType"]
      self.BitFlag:int = obj["BitFlag"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.RestrictionDescription:str = obj["RestrictionDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.RevisionNumPartDescription:str = obj["RevisionNumPartDescription"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOMtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Parent Part number to which this material item is a component of  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number of the part that this material item is a component of.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material record within a specific Job/Lot/Assembly. This is system assigned. The next available # is determined by reading last JobMtl record on the Job/Lot/Assembly and then adding one to it.  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The Part Number of the component material record for the related Parent Part.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Quantity Per Parent  """  
      self.FixedQty:bool = obj["FixedQty"]
      """  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   A material record can be related to a specific operation. This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job. The related operation is also used to calculate the JobMtl.ReqDate based on the operations scheduled start date and materials lead time.  """  
      self.SalvagePartNum:str = obj["SalvagePartNum"]
      """  Part number for Salvageable scrap from this material record.  An optional field. This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via Salvage receipt process.  """  
      self.SalvageDescription:str = obj["SalvageDescription"]
      """  Description of Salvageable material. Use Part.Description for a default.  """  
      self.SalvageQtyPer:int = obj["SalvageQtyPer"]
      """  A factor that multiplied by the QtyPer results in the expected total salvage quantity.  """  
      self.SalvageUM:str = obj["SalvageUM"]
      """  Default Unit of measure for the Salvaged Part. Default from the Part.IUM.  """  
      self.SalvageUnitCredit:int = obj["SalvageUnitCredit"]
      """  Estimated Salvage Unit Credit. Use the appropriate cost from the Part master as a default.  """  
      self.MfgComment:str = obj["MfgComment"]
      """  Material comments specific to this manufacturing process. These comments copied to Jobs/Quotes when pulled from BOM.  """  
      self.OverRideMfgComments:bool = obj["OverRideMfgComments"]
      """  Indicates if these comments should override the comments defined in the part master. It controls how the MfgComments are created when this record is pulled into a Job or Quote.  If "Yes" then the comments that are defined in the Part master are NOT copied. If "No" then the ECOMtl.MfgComments will be appended on to the Part.MfgComments when written to the Job/Quote material record.  """  
      self.PurComment:str = obj["PurComment"]
      """   Material comments specific to a manufacturing process. These comments (and optionally the comments from Part Master) are  copied to Jobs/Quotes when the BOM is pulled.
( See OverRidePurComments )  """  
      self.OverRidePurComments:bool = obj["OverRidePurComments"]
      """  Indicates if these comments should override the comments defined in the part master. It controls how the PurComments are created when this record is pulled into a Job or Quote.  If "Yes" then the comments that are defined in the Part master are NOT copied. If "No" then the ECOMtl.PurComments will be appended on to the Part.PurComments when written to the Job/Quote material record.  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of required quantity.  """  
      self.PullAsAsm:bool = obj["PullAsAsm"]
      """  This is relevant for assemblies (Part.Method = Yes). Indicates that if this assembly should be pulled from stock or manufactured as part of the job it is pulled into. If PullAsAsm = No only the assembly record will be pulled into the job/quote (as a material), the related material and operations will not be pulled over.  """  
      self.FindNum:str = obj["FindNum"]
      """  Characters used on the drawing to show where material is used.  """  
      self.ViewAsAsm:bool = obj["ViewAsAsm"]
      """   This is relevant for assemblies (Part.Method = Yes). Indicates that if this assembly when shown in ABOM indented views or on reports it should be shown either as a subassembly or material requirement.  If Yes then the assemblies components will be shown else it is shown as a single material requirement line. Similar to the PullAsAsm flag however this is used to control how subassemblies appear in the ABOM module.
NOTE: AS OF 2.70.400 this function is not implemented.  Pending further analysis. It has been added to the schema to make it easier to implement when decision has been reached.  """  
      self.APSSchedulerName:str = obj["APSSchedulerName"]
      """  Indicates which APS Scheduler module the assembly is scheduled in.  """  
      self.APSSLDate:str = obj["APSSLDate"]
      """  APS Start Limit date.  Prevents APS from scheduling before this date.  """  
      self.APSSLTime:int = obj["APSSLTime"]
      """  APS Start Limit time.  Time, in decimal hours, that APS will not schedule before.  Only valid if APSSLDate is valid.  """  
      self.APSInsertDirection:str = obj["APSInsertDirection"]
      """  Schedule direction.  Valid options are: F=Forward, B=Backward, C=dynamic Constraint based, W=minimum WIP, E=End of work, S=Split longest duration, X=use the direction specified in task entry in APS.  """  
      self.APSInsertCriteria:str = obj["APSInsertCriteria"]
      """  Method of insertion into schedule.  Valid values are: T=best Time, G=same Group, N=uNscheduled, F=Force Insert, I=without resource assignment.  """  
      self.APSAttrib1:int = obj["APSAttrib1"]
      """  Used to calculated setup time during optimization.  """  
      self.APSAttrib2:int = obj["APSAttrib2"]
      """  Used to calculated setup time during optimization.  """  
      self.APSAttrib3:int = obj["APSAttrib3"]
      """  Used to calculated setup time during optimization.  """  
      self.APSAttrib4:int = obj["APSAttrib4"]
      """  Used to calculated setup time during optimization.  """  
      self.APSAddResType:str = obj["APSAddResType"]
      """   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  """  
      self.SalvageMtlBurRate:int = obj["SalvageMtlBurRate"]
      """  The salvage material burden rate for this Part Material.  """  
      self.SalvageEstMtlBurUnitCredit:int = obj["SalvageEstMtlBurUnitCredit"]
      """  Estimated salvage Mtl Burden Unit Credit.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this Part Material.  """  
      self.EstMtlBurUnitCost:int = obj["EstMtlBurUnitCost"]
      """  Estimated Mtl Burden Unit Cost.  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this part material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this part material.  Can be zero if RFQ(s) are not required.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      """  The original material sequence number from the PartMtl record at the time of check out. If this record was not created during check out this should remain 0.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.RelatedStage:str = obj["RelatedStage"]
      """  A material record can be related to a specific operation by stage. This field contains the StageNumber of the operation that it is related to.  """  
      self.BaseMethodOverridden:bool = obj["BaseMethodOverridden"]
      """  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  Parent Alternate Routing method for the part material.  """  
      self.ParentMtlSeq:int = obj["ParentMtlSeq"]
      """  Indicates the parent material sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the Material requirement.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.Weight:int = obj["Weight"]
      """  Material Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Material Weight UOM defaulted from Part Master.  """  
      self.RuleTag:str = obj["RuleTag"]
      """  Rule Tag. Used in the configurator.  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.PlanAsAsm:bool = obj["PlanAsAsm"]
      """  This is relevant for assemblies (Part.Method = Yes). Indicates if the sub-assemby can be spawned off to a different job.  Can be true only if PullAsAsm = true.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReassignSNAsm:bool = obj["ReassignSNAsm"]
      """  flag used to designate if the serial numbers from the job material/subassembly can be reassigned as the serial number of the parent assembly (top assembly or n deep subassembly) being reworked using a job.  """  
      self.LocationView:bool = obj["LocationView"]
      """  Controls if this material record is viewable in Location Management or the web.  """  
      self.CNWeightMeasurement:bool = obj["CNWeightMeasurement"]
      """  Weight Measurement  """  
      self.CNRequiredQty:int = obj["CNRequiredQty"]
      """  Required Quantity  """  
      self.CNConsumedQty:int = obj["CNConsumedQty"]
      """  Consumed Quantity  """  
      self.CNUOM:str = obj["CNUOM"]
      """  UOM  """  
      self.MtlAttributeSetID:int = obj["MtlAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.SalvageAttributeSetID:int = obj["SalvageAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SalvagePlanningNumberOfPieces:int = obj["SalvagePlanningNumberOfPieces"]
      """  Salvage planning number of pieces for this attribute set.  """  
      self.SalvagePlanningAttributeSetID:int = obj["SalvagePlanningAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningPct:int = obj["PlanningPct"]
      """  Planning Percent  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.MtlRevisionNum:str = obj["MtlRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SalvageRevisionNum:str = obj["SalvageRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.RevisionNumPartDescription:str = obj["RevisionNumPartDescription"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.AnswerMtlPartNumQuestion:bool = obj["AnswerMtlPartNumQuestion"]
      """  The user's response to potential question for analysis code on mtlpartnum validation.  """  
      self.CNAttritionRate:int = obj["CNAttritionRate"]
      """  Attrition Rate  """  
      self.EnablePartInsp:bool = obj["EnablePartInsp"]
      """  Used to Enable Part Inspection fields on UI  """  
      self.EnablePullAsAsm:bool = obj["EnablePullAsAsm"]
      """  Should pullasasm be enabled on the UI?  """  
      self.EnableViewAsAsm:bool = obj["EnableViewAsAsm"]
      """  Should viewasasm be enabled on the UI?  """  
      self.ExpandTree:bool = obj["ExpandTree"]
      self.IsPartMtl:bool = obj["IsPartMtl"]
      """  Is this a PartMtl record?  Used for build of tree to display PartMtl as ECOMtl.  """  
      self.IsTopPartSalesKit:bool = obj["IsTopPartSalesKit"]
      """  A boolean value to determine if the Material is the Top part sales kit  """  
      self.MtlPartNumMfgComment:str = obj["MtlPartNumMfgComment"]
      """  Used to enter comments for manufacturing when this part is referenced on a job.  """  
      self.MtlPartNumPurComment:str = obj["MtlPartNumPurComment"]
      """  Part Comments that will be used as a default for purchasing.  """  
      self.MtlRevExists:bool = obj["MtlRevExists"]
      """  Is there a revision for the MtlPartNum component of the parent partnum?  """  
      self.OpDesc:str = obj["OpDesc"]
      """  The related operation description  """  
      self.RDEndNum:int = obj["RDEndNum"]
      """  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  """  
      self.RDPrefix:str = obj["RDPrefix"]
      """  The prefix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  """  
      self.RDStartNum:int = obj["RDStartNum"]
      """  This number will be used to create reference designators. This field will be defaulted to ?1?  """  
      self.RDSuffix:str = obj["RDSuffix"]
      """  The suffix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  """  
      self.RelatedECOOprOprSeq:int = obj["RelatedECOOprOprSeq"]
      self.SalvageBaseUOM:str = obj["SalvageBaseUOM"]
      """  Salvage Base Unit of Measure  """  
      self.SalvagePartTrackMulti:bool = obj["SalvagePartTrackMulti"]
      """  Salvage Part Number Track Multi UOM  """  
      self.UseStaging:bool = obj["UseStaging"]
      """  The value of ecorev.usestaging for UI purposes.  """  
      self.AnswerPlanAsAsmQuestion:bool = obj["AnswerPlanAsAsmQuestion"]
      """  The user's response to potential question for analysis code on planasasm validation.  """  
      self.AnswerPullAsAsmQuestion:bool = obj["AnswerPullAsAsmQuestion"]
      """  The user's response to potential question for analysis code on pullasasm validation.  """  
      self.DspUnitMeasure:str = obj["DspUnitMeasure"]
      """  The display unit of measure for the qty/parent field.  """  
      self.EnableFixedQty:bool = obj["EnableFixedQty"]
      """  External field used to control the flag over the FixedQty field on UI screens.  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.SalvEnableAttSetSearch:bool = obj["SalvEnableAttSetSearch"]
      self.PlanningNumberOfPiecesDisp:int = obj["PlanningNumberOfPiecesDisp"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.SalvagePlanningNumberOfPiecesDisp:int = obj["SalvagePlanningNumberOfPiecesDisp"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.APSSchedulerNameAPSSchedulerName:str = obj["APSSchedulerNameAPSSchedulerName"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.MtlPartNumTrackInventoryByRevision:bool = obj["MtlPartNumTrackInventoryByRevision"]
      self.MtlPartNumAttrClassID:str = obj["MtlPartNumAttrClassID"]
      self.MtlPartNumTrackInventoryAttributes:bool = obj["MtlPartNumTrackInventoryAttributes"]
      self.MtlPartNumTrackLots:bool = obj["MtlPartNumTrackLots"]
      self.MtlPartNumTrackDimension:bool = obj["MtlPartNumTrackDimension"]
      self.MtlPartNumSellingFactor:int = obj["MtlPartNumSellingFactor"]
      self.MtlPartNumIUM:str = obj["MtlPartNumIUM"]
      self.MtlPartNumPricePerCode:str = obj["MtlPartNumPricePerCode"]
      self.MtlPartNumTrackSerialNum:bool = obj["MtlPartNumTrackSerialNum"]
      self.MtlPartNumPartDescription:str = obj["MtlPartNumPartDescription"]
      self.MtlPartNumSalesUM:str = obj["MtlPartNumSalesUM"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.SalvagePartNumTrackInventoryByRevision:bool = obj["SalvagePartNumTrackInventoryByRevision"]
      self.SalvagePartNumPricePerCode:str = obj["SalvagePartNumPricePerCode"]
      self.SalvagePartNumSalesUM:str = obj["SalvagePartNumSalesUM"]
      self.SalvagePartNumTrackDimension:bool = obj["SalvagePartNumTrackDimension"]
      self.SalvagePartNumPartDescription:str = obj["SalvagePartNumPartDescription"]
      self.SalvagePartNumTrackLots:bool = obj["SalvagePartNumTrackLots"]
      self.SalvagePartNumIUM:str = obj["SalvagePartNumIUM"]
      self.SalvagePartNumSellingFactor:int = obj["SalvagePartNumSellingFactor"]
      self.SalvagePartNumAttrClassID:str = obj["SalvagePartNumAttrClassID"]
      self.SalvagePartNumTrackInventoryAttributes:bool = obj["SalvagePartNumTrackInventoryAttributes"]
      self.SalvagePartNumTrackSerialNum:bool = obj["SalvagePartNumTrackSerialNum"]
      self.SalvDynAttrValueSetShortDescription:str = obj["SalvDynAttrValueSetShortDescription"]
      self.SalvDynAttrValueSetDescription:str = obj["SalvDynAttrValueSetDescription"]
      self.StageNoDescription:str = obj["StageNoDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOOpDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  Uniquely identifies an OpDtl.  System assigned.  """  
      self.CapabilityID:str = obj["CapabilityID"]
      """  The user can select the capability the operation is to perform.  The system will select the resource.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  The user can select a Resource Group for the operation to be performed on.  The system will select the actual resource.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource for this operation to be performed on.  """  
      self.SetupHours:int = obj["SetupHours"]
      """  The standard setup hours for the operation.   This is the setup time required for each machine.  """  
      self.ProdHours:int = obj["ProdHours"]
      """  Production hours for this operation.  It is the total hours, as though the operation were running on a single machine.  """  
      self.NumResources:int = obj["NumResources"]
      """  This is the number of resources the operation can run on.  If multiple resources can perform the required Capability, then up to this many will be employed.  This determines the number of setups the system will allow for the operation.  However, the number of setups cannot exceed the number of operations.  The idea being that once a part is on a machine you will complete the operation on that resource.  """  
      self.SetupOrProd:str = obj["SetupOrProd"]
      """  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "S", indicating the resource is RequiredFor the Setup phase of this operation, "P" for Production phase, or "B" meaning Both setup and production phase.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.OpDtlDesc:str = obj["OpDtlDesc"]
      """  Description is initially created when the ECOOpDtl is created.   If the ECOOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  Parent Alternate Routing method of this part operation.  """  
      self.ParentOprSeq:int = obj["ParentOprSeq"]
      """  Indicates the parent operation sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  """  
      self.ParentOpDtlSeq:int = obj["ParentOpDtlSeq"]
      """  Indicates the parent operation detail sequence.  """  
      self.BaseMethodOverridden:bool = obj["BaseMethodOverridden"]
      """  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  """  
      self.OrigOpDtlSeq:int = obj["OrigOpDtlSeq"]
      """  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  """  
      self.OrigOprSeq:int = obj["OrigOprSeq"]
      """  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  """  
      self.ConcurrentCapacity:int = obj["ConcurrentCapacity"]
      """  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  """  
      self.DailyProdRate:int = obj["DailyProdRate"]
      """  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Duplicated from ECOOpr.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Duplicated from ECOOpr.SetupCrewSize. Its the number of people it physically takes to se tup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.PrimaryProd:bool = obj["PrimaryProd"]
      """  Indicates if primary production operation.  """  
      self.PrimarySetup:bool = obj["PrimarySetup"]
      """  Indicates if primary setup operation.  """  
      self.CapabilityDesc:str = obj["CapabilityDesc"]
      """  Capability description  """  
      self.ResourceDesc:str = obj["ResourceDesc"]
      """  Resource description  """  
      self.ResourceGrpDesc:str = obj["ResourceGrpDesc"]
      """  Resource Group description  """  
      self.IsPartOpDtl:bool = obj["IsPartOpDtl"]
      """  Is this a PartOpDtl?  Used when building the tree to show PartOpDtl as ECOOpDtl.  """  
      self.SubContract:bool = obj["SubContract"]
      """  Flag for sub contract  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CapabilityIDDescription:str = obj["CapabilityIDDescription"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOOprActionParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID for the ECO Group to which this ECORev belongs.  """  
      self.PartNum:str = obj["PartNum"]
      """  The user's Internal Part number used to identify line item part. It can be blank if using Process Manufacturing.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part or process manufacture.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The ID of Process Manufacturing revision.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the method.  """  
      self.ActionSeq:int = obj["ActionSeq"]
      """  A sequence number which uniquely identifies action record within the operation set.  """  
      self.ActionParamSeq:int = obj["ActionParamSeq"]
      """  A sequence number which uniquely identifies parameter within the Operation/Action set.  """  
      self.ActionParamFieldDataType:str = obj["ActionParamFieldDataType"]
      """  Data type of Action Parameter  """  
      self.ActionParamValueCharacter:str = obj["ActionParamValueCharacter"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueDate:str = obj["ActionParamValueDate"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueDecimal:int = obj["ActionParamValueDecimal"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueInteger:int = obj["ActionParamValueInteger"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueLogical:bool = obj["ActionParamValueLogical"]
      """  Value of Action Parameter.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOOprActionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID for the ECO Group to which this ECORev belongs.  """  
      self.PartNum:str = obj["PartNum"]
      """  The user's Internal Part number used to identify line item part. It can be blank if using Process Manufacturing.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part or process manufacture.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The ID of Process Manufacturing revision.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the method.  """  
      self.ActionSeq:int = obj["ActionSeq"]
      """  A sequence number which uniquely identifies action record within the operation set.  """  
      self.ActionDesc:str = obj["ActionDesc"]
      """  Description of Action.  """  
      self.Required:bool = obj["Required"]
      """  Indicated if this action must be completed before Operation can be completed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOOprAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:str = obj["GroupID"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.AltMethod:str = obj["AltMethod"]
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      self.OprSeq:int = obj["OprSeq"]
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

class Erp_Tablesets_ECOOprInspRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.PartNum:str = obj["PartNum"]
      """  Parent Part number to which this material item is a component of  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number of the part that this material item is a component of.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.PlanSeq:int = obj["PlanSeq"]
      """  A sequence number that uniquely identifies the ECOOprInsp ecord within the ECO operation  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number).  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID.  Must be valid in the SpecHed table.  """  
      self.OrigOprSeq:int = obj["OrigOprSeq"]
      """  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOOprMachParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  RevisionNum  """  
      self.AltMethod:str = obj["AltMethod"]
      """  AltMethod  """  
      self.OprSeq:int = obj["OprSeq"]
      """  OprSeq  """  
      self.MachParamSeq:int = obj["MachParamSeq"]
      """  MachParamSeq  """  
      self.RequestCode:str = obj["RequestCode"]
      """  RequestCode  """  
      self.MachineNum:str = obj["MachineNum"]
      """  MachineNum  """  
      self.ToolNum:str = obj["ToolNum"]
      """  ToolNum  """  
      self.ParamNum:int = obj["ParamNum"]
      """  ParamNum  """  
      self.ParamUpperLimit:int = obj["ParamUpperLimit"]
      """  ParamUpperLimit  """  
      self.ParamNominalValue:int = obj["ParamNominalValue"]
      """  ParamNominalValue  """  
      self.ParamLowerLimit:int = obj["ParamLowerLimit"]
      """  ParamLowerLimit  """  
      self.ParamDelayValue:int = obj["ParamDelayValue"]
      """  ParamDelayValue  """  
      self.SpecEnable:bool = obj["SpecEnable"]
      """  SpecEnable  """  
      self.SpecControlAlarm:bool = obj["SpecControlAlarm"]
      """  SpecControlAlarm  """  
      self.SpecRunAlarm:bool = obj["SpecRunAlarm"]
      """  SpecRunAlarm  """  
      self.ProcSpecAlarm:bool = obj["ProcSpecAlarm"]
      """  ProcSpecAlarm  """  
      self.ProcControlAlarm:bool = obj["ProcControlAlarm"]
      """  ProcControlAlarm  """  
      self.PartQualSpecEnable:bool = obj["PartQualSpecEnable"]
      """  PartQualSpecEnable  """  
      self.PartQualControlEnable:bool = obj["PartQualControlEnable"]
      """  PartQualControlEnable  """  
      self.OrigOprSeq:int = obj["OrigOprSeq"]
      """  OrigOprSeq  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOOprRestrictSubstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.SubstanceID:str = obj["SubstanceID"]
      """  Substance identification.  """  
      self.Weight:int = obj["Weight"]
      """  Defaulted from Operation Master Substances.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Defaulted from Operation Master Substances.  """  
      self.OrigOprSeq:int = obj["OrigOprSeq"]
      """  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Exempt:bool = obj["Exempt"]
      self.ExemptDate:str = obj["ExemptDate"]
      self.ExemptCertificate:str = obj["ExemptCertificate"]
      self.Manual:bool = obj["Manual"]
      self.BitFlag:int = obj["BitFlag"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.RestrictionDescription:str = obj["RestrictionDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumPartDescription:str = obj["RevisionNumPartDescription"]
      self.SubstanceDescription:str = obj["SubstanceDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOOprRestrictionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.OrigOprSeq:int = obj["OrigOprSeq"]
      """  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.Weight:bool = obj["Weight"]
      """  Yes to display when the part has no net weight or when one or more of the selected has no weight.  """  
      self.Manual:bool = obj["Manual"]
      self.ComplianceDate:str = obj["ComplianceDate"]
      self.BitFlag:int = obj["BitFlag"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.RestrictionDescription:str = obj["RestrictionDescription"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.RevisionNumPartDescription:str = obj["RevisionNumPartDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOOprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Master Code - Links the JobOper  record with a OpMaster record. Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  """  
      self.OpStdID:str = obj["OpStdID"]
      """   The Operation standard ID. This links the JobOPer to the OpStd master file. This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.
Valid for "inside operations" only.  """  
      self.EstSetHours:int = obj["EstSetHours"]
      """  The estimated set up hours. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours.  """  
      self.EstProdHours:int = obj["EstProdHours"]
      """   The estimated Production run hours for internal operations (Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (RunQty / Std).
If StdFormat = "PM" then (RunQty / Std ) / 60.
If StdFormat = "OH" then (RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (RunQty/Basis) X Std.
If StdFormat = "MP" then ((RunQty/Basis) X Std) / 60.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """   The production standard for the operation. It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours. A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  """  
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  """  
      self.OpsPerPart:int = obj["OpsPerPart"]
      """  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Production Quantity per one of the Parent Item.  """  
      self.Machines:int = obj["Machines"]
      """  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to se tup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  Inventory UOM  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  Estimated Unit Cost for the SubContract operation.  Defaults from the Part table if valid PartNum.  """  
      self.DaysOut:int = obj["DaysOut"]
      """  Hours required is calculated as days * 8.  """  
      self.SubPartNum:str = obj["SubPartNum"]
      """  The PartNum to be shipped to the subcontract. Defaults as the Part number of the method to which it belongs (ECOOpr.PartNum).  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job operation comments.  """  
      self.SchedRelation:str = obj["SchedRelation"]
      """   Indicates the scheduling relationship between this and the preceding operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  """  
      self.RunQty:int = obj["RunQty"]
      """  The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0. This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  """  
      self.AddlSetupHours:int = obj["AddlSetupHours"]
      """  Additional Setup Hours that will be required after a certain quantity has been run for this operation. The quantity at which this occurs is established in AddSetupQty field. The system determines the setup hours as SetupHrs + (Max((RunQty - AddlSetupQty,0))/AddlSetUpQty) * AddlSetupHours. Any fractional results of the AddlSetUpQty calculations are rounded up to the next whole number before multiplying by the AddlSetUpHours.  """  
      self.AddlSetUpQty:int = obj["AddlSetUpQty"]
      """  Additional Setup quantity indicates the quantity at which additional setup time will be incurred.  """  
      self.APSPrepOp:int = obj["APSPrepOp"]
      """  Indicates the operation that must precede this operation.  Mainly used to model one to many routing structures.  """  
      self.APSNextOp:int = obj["APSNextOp"]
      """  This is the next operation in the routing.  -1 makes this operation the last one in the routing so far; -2 makes it the first one in the routing so far; 0 means no successor.  """  
      self.APSAltOp:int = obj["APSAltOp"]
      """  Specifies the operation for which this is an alternate.  """  
      self.APSSpecificResource:str = obj["APSSpecificResource"]
      """  Used to assign an operation to a specific resource so that APS does not schedule it elsewhere.  Overrides APSCapability.  """  
      self.APSCycleTime:int = obj["APSCycleTime"]
      """   Cycles per minute.
SQL:  IIF(CINT(JobOper.RunQty) = 0 OR JobOper.SubContract = TRUE, "0", JobOper.EstProdHours * 60 /  JobOper.RunQty)  """  
      self.APSConstantTime:int = obj["APSConstantTime"]
      """   Fixed time, in decimal minutes, to be added to the operation.  Can be used to represent cleanup time or model outsource time.
SQL: IFF(JobOper.SubContract = TRUE, (JobOper.DaysOut * 1440), "0")  """  
      self.APSSetupGroup:int = obj["APSSetupGroup"]
      """  Used to group operations to save on setups.  """  
      self.APSMakeFactor:int = obj["APSMakeFactor"]
      """  Quantity of Part per cycle.  """  
      self.APSContainerSize:int = obj["APSContainerSize"]
      """  Quantity that must be completed before the next operation can start (for overlap); quantity per batch (for batch resources); Auxiliary resource quantity.  """  
      self.APSSchedulerName:str = obj["APSSchedulerName"]
      """  Name of the APS Scheduler Module in which to schedule this operation.  """  
      self.APSMaxLength:int = obj["APSMaxLength"]
      """  If the scheduled time exceeds this value then the operation is split into operations which do not exceed this length.  """  
      self.APSTransferTime:int = obj["APSTransferTime"]
      """  Time between the end of this operation and the start time of the successor operation.  """  
      self.APSEffectiveness:int = obj["APSEffectiveness"]
      """  Cycle time and constant times are divided by this value to get schedule times.  Zeros disable this feature.  """  
      self.APSOperationClass:str = obj["APSOperationClass"]
      """  Type of Operation: P for Prep, D for Processing (Dispatchable in APS terminology).  """  
      self.APSAuxResource:str = obj["APSAuxResource"]
      """  Auxiliary resource requirements.   This is a comma and tilde delimited list of APSAuxResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  """  
      self.APSAddResource:str = obj["APSAddResource"]
      """  Additional resource requirements.   This is a comma and tilde delimited list of APSAddResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  For Additional Resources the Duration = 5 (entire Operation).  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  """  
      self.FAQty:int = obj["FAQty"]
      """  The quantity requested for first article inspection.  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this part operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this part subcontract operation.  Can be zero if RFQ(s) are not required.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.OrigOprSeq:int = obj["OrigOprSeq"]
      """  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  """  
      self.SetupGroup:str = obj["SetupGroup"]
      """  Used to group operation to save on setups.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PrimarySetupOpDtl:int = obj["PrimarySetupOpDtl"]
      """   Identifies the primary ECOOpDtl to be used for setup.  The setup time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = S or B.  """  
      self.PrimaryProdOpDtl:int = obj["PrimaryProdOpDtl"]
      """   Identifies the primary ECOOpDtl to be used for production.  The production run time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = P or B.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Operation Description.  """  
      self.StageNumber:str = obj["StageNumber"]
      """  The stage number of the operations.  Entered only when the related PartRev.UseStaging flag is true.  """  
      self.BaseMethodOverridden:bool = obj["BaseMethodOverridden"]
      """  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  Parent Alternate Routing method of this part operation.  """  
      self.ParentOprSeq:int = obj["ParentOprSeq"]
      """  Indicates the parent operation sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  """  
      self.BrkQty01:int = obj["BrkQty01"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty02:int = obj["BrkQty02"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty03:int = obj["BrkQty03"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty04:int = obj["BrkQty04"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty05:int = obj["BrkQty05"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty06:int = obj["BrkQty06"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty07:int = obj["BrkQty07"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty08:int = obj["BrkQty08"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty09:int = obj["BrkQty09"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty10:int = obj["BrkQty10"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.PBrkCost01:int = obj["PBrkCost01"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost02:int = obj["PBrkCost02"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost03:int = obj["PBrkCost03"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost04:int = obj["PBrkCost04"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost05:int = obj["PBrkCost05"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost06:int = obj["PBrkCost06"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost07:int = obj["PBrkCost07"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost08:int = obj["PBrkCost08"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost09:int = obj["PBrkCost09"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost10:int = obj["PBrkCost10"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkStdRate01:int = obj["PBrkStdRate01"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate02:int = obj["PBrkStdRate02"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate03:int = obj["PBrkStdRate03"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate04:int = obj["PBrkStdRate04"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate05:int = obj["PBrkStdRate05"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate06:int = obj["PBrkStdRate06"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate07:int = obj["PBrkStdRate07"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate08:int = obj["PBrkStdRate08"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate09:int = obj["PBrkStdRate09"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate10:int = obj["PBrkStdRate10"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.SNRequiredOpr:bool = obj["SNRequiredOpr"]
      """  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  """  
      self.SNRequiredSubConShip:bool = obj["SNRequiredSubConShip"]
      """  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  """  
      self.Weight:int = obj["Weight"]
      """  Operation Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Operation Weight UOM defaulted from Part Master.  """  
      self.SendAheadType:str = obj["SendAheadType"]
      """   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  """  
      self.SendAheadOffset:int = obj["SendAheadOffset"]
      """   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  """  
      self.PrjRoleList:str = obj["PrjRoleList"]
      """  Delimited list of PrjRoleCd codes that are allowed for this operation.  """  
      self.UseAllRoles:bool = obj["UseAllRoles"]
      """  Allow use all Roles  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.PctReg:int = obj["PctReg"]
      """  PctReg  """  
      self.SetupMaterial:int = obj["SetupMaterial"]
      """  SetupMaterial  """  
      self.MaterialColorRating:int = obj["MaterialColorRating"]
      """  MaterialColorRating  """  
      self.MiscInfo1:str = obj["MiscInfo1"]
      """  MiscInfo1  """  
      self.MiscInfo2:str = obj["MiscInfo2"]
      """  MiscInfo2  """  
      self.SetupURL:str = obj["SetupURL"]
      """  SetupURL  """  
      self.ExpPctUp:int = obj["ExpPctUp"]
      """  ExpPctUp  """  
      self.ExpCycTm:int = obj["ExpCycTm"]
      """  ExpCycTm  """  
      self.ExpGood:int = obj["ExpGood"]
      """  ExpGood  """  
      self.NonProdLimit:int = obj["NonProdLimit"]
      """  NonProdLimit  """  
      self.AutoSpcEnable:bool = obj["AutoSpcEnable"]
      """  AutoSpcEnable  """  
      self.AutoSpcPeriod:int = obj["AutoSpcPeriod"]
      """  AutoSpcPeriod  """  
      self.PartQualEnable:bool = obj["PartQualEnable"]
      """  PartQualEnable  """  
      self.AutoSpcSubgroup:int = obj["AutoSpcSubgroup"]
      """  AutoSpcSubgroup  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PulsesPerCycle:int = obj["PulsesPerCycle"]
      """  PulsesPerCycle  """  
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.TemplateID:str = obj["TemplateID"]
      """  TemplateID  """  
      self.SubRevisionNum:str = obj["SubRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.PrimaryProdOpDtlOpDtlDesc:str = obj["PrimaryProdOpDtlOpDtlDesc"]
      self.PrimarySetupOpDtlOpDtlDesc:str = obj["PrimarySetupOpDtlOpDtlDesc"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumPartDescription:str = obj["RevisionNumPartDescription"]
      self.DspBillAddr:str = obj["DspBillAddr"]
      """  The vendor's name and bill to address  """  
      self.EnableSNReqSubConShip:bool = obj["EnableSNReqSubConShip"]
      """  Field used to control the flag on SNRequiredSubConShip field on UI screens.  """  
      self.EnableSNRequiredOpr:bool = obj["EnableSNRequiredOpr"]
      """  Used as a flag to enable controls on UI screens  """  
      self.FinalOpr:bool = obj["FinalOpr"]
      """  The final operation field  """  
      self.HasPriceBreaks:bool = obj["HasPriceBreaks"]
      """  Flag to let you know if you have price breaks.  """  
      self.IsPartOpr:bool = obj["IsPartOpr"]
      """  Is this a PartOpr?  Used when building the tree to show PartOpr as ECOOpr.  """  
      self.OldOprSeq:int = obj["OldOprSeq"]
      """  The original or old OprSeq.  Used when changing the OprSeq.  """  
      self.OpStdDescription:str = obj["OpStdDescription"]
      self.PLMChar03:str = obj["PLMChar03"]
      """  PML ID  """  
      self.PrimaryResourceGrpDesc:str = obj["PrimaryResourceGrpDesc"]
      """  Primary Resource Group description  """  
      self.PrimaryResourceGrpID:str = obj["PrimaryResourceGrpID"]
      """  The Resource Group ID of the primary production operation detail.  """  
      self.RefreshResources:bool = obj["RefreshResources"]
      """  Indicates if the scheduling resources should be refreshed when the op code changes.  """  
      self.SetHoursPerMach:int = obj["SetHoursPerMach"]
      """  The setup hours per machines.  """  
      self.StdFrmtDesc:str = obj["StdFrmtDesc"]
      """  The standard format description.  """  
      self.UseStaging:bool = obj["UseStaging"]
      """  The value of the ecorev.usestaging field for UI purposes  """  
      self.AutoReceive:bool = obj["AutoReceive"]
      """  The auto receive field  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.PrimaryProdOpDtlDesc:str = obj["PrimaryProdOpDtlDesc"]
      self.PrimarySetupOpDtlDesc:str = obj["PrimarySetupOpDtlDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.APSSchedulerNameAPSSchedulerName:str = obj["APSSchedulerNameAPSSchedulerName"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.SetupGroupDescription:str = obj["SetupGroupDescription"]
      self.StageNoDescription:str = obj["StageNoDescription"]
      self.SubPartNumTrackInventoryAttributes:bool = obj["SubPartNumTrackInventoryAttributes"]
      self.SubPartNumPricePerCode:str = obj["SubPartNumPricePerCode"]
      self.SubPartNumTrackDimension:bool = obj["SubPartNumTrackDimension"]
      self.SubPartNumTrackSerialNum:bool = obj["SubPartNumTrackSerialNum"]
      self.SubPartNumSellingFactor:int = obj["SubPartNumSellingFactor"]
      self.SubPartNumTrackLots:bool = obj["SubPartNumTrackLots"]
      self.SubPartNumSalesUM:str = obj["SubPartNumSalesUM"]
      self.SubPartNumPartDescription:str = obj["SubPartNumPartDescription"]
      self.SubPartNumIUM:str = obj["SubPartNumIUM"]
      self.SubPartNumAttrClassID:str = obj["SubPartNumAttrClassID"]
      self.SubPartNumTrackInventoryByRevision:bool = obj["SubPartNumTrackInventoryByRevision"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECORevAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:str = obj["GroupID"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.AltMethod:str = obj["AltMethod"]
      self.ProcessMfgID:str = obj["ProcessMfgID"]
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

class Erp_Tablesets_ECORevRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID for the ECO Group to which this ECORev belongs.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.RevShortDesc:str = obj["RevShortDesc"]
      """  Short description of the revision. This is NOT the Part description.  """  
      self.RevDescription:str = obj["RevDescription"]
      """  Used to enter a full description of the revision.  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  """  
      self.TLRLaborCost:int = obj["TLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRBurdenCost:int = obj["TLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.TLRMaterialCost:int = obj["TLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSubcontractCost:int = obj["TLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRMtlBurCost:int = obj["TLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSetupLaborCost:int = obj["TLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRSetupBurdenCost:int = obj["TLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRLaborCost:int = obj["LLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRBurdenCost:int = obj["LLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRMaterialCost:int = obj["LLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSubcontractCost:int = obj["LLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRMtlBurCost:int = obj["LLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSetupLaborCost:int = obj["LLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRSetupBurdenCost:int = obj["LLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.RollupDate:str = obj["RollupDate"]
      """  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.ECO:str = obj["ECO"]
      """  Engineering Change Order Number. An optional field for reference.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part revision contains Method of Manufacture details (ECOMtl/ECOOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number ECOOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.CheckInRevisionNum:str = obj["CheckInRevisionNum"]
      """  Revision number which will be used to check in the part.  This will only be used if the CheckIn Revision Number is different from the main RevisionNum field.  """  
      self.CheckInDate:str = obj["CheckInDate"]
      """  The date that the revision is checked in.  """  
      self.CheckedOut:bool = obj["CheckedOut"]
      """  This flag determines if the ECORev record is currently checked out.  There should only be one checked out ECORev record for each Company-Part-Rev.  """  
      self.CheckOutDate:str = obj["CheckOutDate"]
      """  The date that the Part-Rev was last checked out to the group.  """  
      self.CheckedOutBy:str = obj["CheckedOutBy"]
      """  UserID who checked out the revision.  Not maintainable by the user.  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The PartDescription from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.RevLocked:bool = obj["RevLocked"]
      """  Indicates if this ECO Revision is locked.  """  
      self.RevLockedBy:str = obj["RevLockedBy"]
      """  UserID that has the ECORev record locked.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  The alternate method of the parent this method inherits from.  """  
      self.UseStaging:bool = obj["UseStaging"]
      """  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  """  
      self.UseAltRevForParts:bool = obj["UseAltRevForParts"]
      """  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  """  
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """  Identifies whether the co-parts are to be produced concurrently or sequentially. The default is sequential. The selected value determines quantity reporting and costing.  """  
      self.AltMethodDesc:str = obj["AltMethodDesc"]
      """  AltMethodDesc  """  
      self.CNCustomsItemNum:str = obj["CNCustomsItemNum"]
      """  Customs Item Number  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.ProcessMfgType:str = obj["ProcessMfgType"]
      """  Type of Process Manufacturing this revision is for: Cleaning, General, Master and Site.  """  
      self.ProcessMfgDescription:str = obj["ProcessMfgDescription"]
      """  Description of Process Manufacturing revision.  """  
      self.ImageID:str = obj["ImageID"]
      """  ID of Revision Image.  """  
      self.UseAdvancedStaging:bool = obj["UseAdvancedStaging"]
      """  Indicates if this revision is to use Advanced Staging.  """  
      self.ECPCEnabled:bool = obj["ECPCEnabled"]
      """  Only Part Revisions marked as Connected Process Control (CPC) enable will be send to CPC.  """  
      self.PartRevCreatedBy:str = obj["PartRevCreatedBy"]
      self.PartRevCreatedOn:str = obj["PartRevCreatedOn"]
      self.PartRevApproved:bool = obj["PartRevApproved"]
      self.Configured:bool = obj["Configured"]
      self.CNCustomsBOM:bool = obj["CNCustomsBOM"]
      self.EnableGetDetails:bool = obj["EnableGetDetails"]
      """  Should the GetDetails menu options be enabled?  """  
      self.EnableUnLock:bool = obj["EnableUnLock"]
      """  Should the UnLock menu option be enabled?  """  
      self.EnableUpdateable:bool = obj["EnableUpdateable"]
      """  Is the revision updateable?  Used for menu options.  """  
      self.HasCoParts:bool = obj["HasCoParts"]
      self.IsPartRev:bool = obj["IsPartRev"]
      """  Is this a PartRev record?  Used for build of tree to display PartRevs as ECORev.  """  
      self.EnableLock:bool = obj["EnableLock"]
      """  Should the Lock menu option be enabled?  """  
      self.CNHandbookLine:str = obj["CNHandbookLine"]
      """  Handbook Line  """  
      self.CNHandbookCode:str = obj["CNHandbookCode"]
      self.isFromPartRevision:bool = obj["isFromPartRevision"]
      self.AltMethodDisplay:str = obj["AltMethodDisplay"]
      """  AltMethod string with label for kinetic tree binding in EngWorkBenchEntry  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTypeCode:str = obj["PartNumTypeCode"]
      self.PlantName:str = obj["PlantName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOStageRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID for the ECO Group to which this ECORev belongs.  """  
      self.PartNum:str = obj["PartNum"]
      """  The user's Internal Part number used to identify line item part. It can be blank if using Process Manufacturing.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part or process manufacture.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The ID of Process Manufacturing revision.  """  
      self.StageSeq:int = obj["StageSeq"]
      """  A sequence number which uniquely identifies stage record within the stage set.  """  
      self.StageNumber:str = obj["StageNumber"]
      """  The identification of related StageNo.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.GeneralRequirements:str = obj["GeneralRequirements"]
      """  High-level descriptions of General Requirements for Stage.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.StageNumberDescription:str = obj["StageNumberDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddRefDesRange_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipMtlSeq
   ipPrefix
   ipStartNum
   ipEndNum
   ipSuffix
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID  """  
      self.ipMtlSeq:int = obj["ipMtlSeq"]
      """  The ECO Material Seq  """  
      self.ipPrefix:str = obj["ipPrefix"]
      """  The Prefix to be used to create Reference Designators  """  
      self.ipStartNum:int = obj["ipStartNum"]
      """  The Starting Number to create Reference Designators  """  
      self.ipEndNum:int = obj["ipEndNum"]
      """  The Ending Number to create Reference Designators  """  
      self.ipSuffix:str = obj["ipSuffix"]
      """  The Suffix to be used to create Reference Designators  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class AddRefDesRange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AllowApproveMethod_output:
   def __init__(self, obj):
      pass

class AllowUnapproveMethod_output:
   def __init__(self, obj):
      pass

class ApproveAllAndRefresh_input:
   """ Required : 
   ipGroupID
   ipValidPassword
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The ECOGroup.GroupID to approve all for  """  
      self.ipValidPassword:bool = obj["ipValidPassword"]
      """  Did the user supply a valid password to run this functionality?
             The value for this parameter should come from running the ValidatePassword method in the
             UserFile BO.  """  
      pass

class ApproveAllAndRefresh_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opResultString:str = obj["parameters"]
      pass

      """  output parameters  """  

class ApproveAll_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   ipValidPassword
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The ECOGroup.GroupID to approve all for  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  Used for GetDatasetForTree, The Part Number to return data for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  Used for GetDatasetForTree, The Revision Number to return data for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  Used for GetDatasetForTree, The Alternate Method to return data for.  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  Used for GetDatasetForTree, The Process Manufacturing ID to return data for.  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical to determine if you would like the dataset refreshed and brought back  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      self.ipValidPassword:bool = obj["ipValidPassword"]
      """  Did the user supply a valid password to run this functionality?
             The value for this parameter should come from running the ValidatePassword method in the
             UserFile BO.  """  
      pass

class ApproveAll_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opResultString:str = obj["parameters"]
      pass

      """  output parameters  """  

class ApproveAndCheckInAll_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   ipValidPassword
   ipAuditText
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The ECOGroup.GroupID to approve all for  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  Used for GetDatasetForTree, The Part Number to return data for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  Used for GetDatasetForTree, The Revision Number to return data for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  Used for GetDatasetForTree, The Alternate Method to return data for.  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  Used for GetDatasetForTree, The Process Manufacturing ID to return data for.  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical to determine if you would like the dataset refreshed and brought back  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false use the part's default method.  """  
      self.ipValidPassword:bool = obj["ipValidPassword"]
      """  Did the user supply a valid password to run this functionality?  The value for this parameter should come from running the ValidatePassword method in the UserFile BO.  """  
      self.ipAuditText:str = obj["ipAuditText"]
      """  The text to write to the audit record(s).  """  
      pass

class ApproveAndCheckInAll_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opResultString:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeECOCoPartPartNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOCoPartPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOGroupGroupClosed_input:
   """ Required : 
   ipProposedGroupClosed
   ds
   """  
   def __init__(self, obj):
      self.ipProposedGroupClosed:bool = obj["ipProposedGroupClosed"]
      """  The new proposed ECOGroup.GroupClosed value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOGroupGroupClosed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOGroupWorkflowGroup_input:
   """ Required : 
   ipProposedWFGroupID
   ds
   """  
   def __init__(self, obj):
      self.ipProposedWFGroupID:str = obj["ipProposedWFGroupID"]
      """  The new proposed ECOGroup.WFGroupID value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOGroupWorkflowGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOMtlFixedQty_input:
   """ Required : 
   ipProposedFixedQty
   ds
   """  
   def __init__(self, obj):
      self.ipProposedFixedQty:bool = obj["ipProposedFixedQty"]
      """  The new proposed ECOMtl.FixedQty value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOMtlFixedQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOMtlMtlPartNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOMtlMtlPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOMtlMtlSeq_input:
   """ Required : 
   ipProposedMtlSeq
   ds
   """  
   def __init__(self, obj):
      self.ipProposedMtlSeq:int = obj["ipProposedMtlSeq"]
      """  The new proposed ECOMtl.MtlSeq value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOMtlMtlSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOMtlPlanAsAsm_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOMtlPlanAsAsm_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOMtlPullAsAsm_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOMtlPullAsAsm_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOMtlQtyPer_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOMtlQtyPer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOMtlRFQNeeded_input:
   """ Required : 
   ipProposedRFQNeeded
   ds
   """  
   def __init__(self, obj):
      self.ipProposedRFQNeeded:bool = obj["ipProposedRFQNeeded"]
      """  The new proposed ECOMtl.RFQNeeded value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOMtlRFQNeeded_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOMtlReassignSNAsm_input:
   """ Required : 
   proposedReassignSNAsm
   ds
   """  
   def __init__(self, obj):
      self.proposedReassignSNAsm:bool = obj["proposedReassignSNAsm"]
      """  Proposed value for Reassign SN Asm  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOMtlReassignSNAsm_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOMtlRelatedOperation_input:
   """ Required : 
   ipProposedRelatedOperation
   ds
   """  
   def __init__(self, obj):
      self.ipProposedRelatedOperation:int = obj["ipProposedRelatedOperation"]
      """  The new proposed ECOMtl.RFQNeeded value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOMtlRelatedOperation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOMtlRelatedStage_input:
   """ Required : 
   ipProposedRelatedStage
   ds
   """  
   def __init__(self, obj):
      self.ipProposedRelatedStage:str = obj["ipProposedRelatedStage"]
      """  The new proposed ECOMtl.RFQNeeded value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOMtlRelatedStage_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOMtlReqRefDes_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOMtlReqRefDes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOMtlRestriction_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOMtlRestriction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOMtlSalvageMtlBurRate_input:
   """ Required : 
   ipProposedSalvageMtlBurRate
   ds
   """  
   def __init__(self, obj):
      self.ipProposedSalvageMtlBurRate:int = obj["ipProposedSalvageMtlBurRate"]
      """  The new proposed ECOMtl.SalvageMtlBurRate value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOMtlSalvageMtlBurRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOMtlSalvagePartNum_input:
   """ Required : 
   ipProposedSalvagePartNum
   ds
   """  
   def __init__(self, obj):
      self.ipProposedSalvagePartNum:str = obj["ipProposedSalvagePartNum"]
      """  The new proposed ECOMtl.SalvagePartNum value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOMtlSalvagePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOMtlSalvageQtyPer_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOMtlSalvageQtyPer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOMtlSalvageUM_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOMtlSalvageUM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOMtlSalvageUnitCredit_input:
   """ Required : 
   ipProposedSalvageUnitCredit
   ds
   """  
   def __init__(self, obj):
      self.ipProposedSalvageUnitCredit:int = obj["ipProposedSalvageUnitCredit"]
      """  The new proposed ECOMtl.SalvageUnitCredit value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOMtlSalvageUnitCredit_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOMtlSubstance_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOMtlSubstance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOOpDtlCapability_input:
   """ Required : 
   proposedCapID
   ds
   """  
   def __init__(self, obj):
      self.proposedCapID:str = obj["proposedCapID"]
      """  The proposed Capability ID  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOOpDtlCapability_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOOpDtlResourceGrpID_input:
   """ Required : 
   proposedResGrpID
   ds
   """  
   def __init__(self, obj):
      self.proposedResGrpID:str = obj["proposedResGrpID"]
      """  The proposed Resource Group ID  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOOpDtlResourceGrpID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOOpDtlResourceID_input:
   """ Required : 
   proposedResourceID
   ds
   """  
   def __init__(self, obj):
      self.proposedResourceID:str = obj["proposedResourceID"]
      """  The proposed Resource ID  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOOpDtlResourceID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOOprAutoReceive_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOOprAutoReceive_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opLaborEntryMethodList:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOOprLaborEntryMethod_input:
   """ Required : 
   iLaborEntryMethod
   ds
   """  
   def __init__(self, obj):
      self.iLaborEntryMethod:str = obj["iLaborEntryMethod"]
      """  Proposed value for LaborEntryMethod field  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOOprLaborEntryMethod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOOprOpCode_input:
   """ Required : 
   proposedOpCode
   ds
   """  
   def __init__(self, obj):
      self.proposedOpCode:str = obj["proposedOpCode"]
      """  The proposed Operation Code  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOOprOpCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.refreshMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOOprOpStdID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOOprOpStdID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOOprOprSeq_input:
   """ Required : 
   ipProposedOprSeq
   ds
   """  
   def __init__(self, obj):
      self.ipProposedOprSeq:int = obj["ipProposedOprSeq"]
      """  The new proposed ECOOpr.OprSeq value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOOprOprSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOOprPrimaryProdOpDtl_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOOprPrimaryProdOpDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOOprPrimarySetupOpDtl_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOOprPrimarySetupOpDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOOprRFQNeeded_input:
   """ Required : 
   ipProposedRFQNeeded
   ds
   """  
   def __init__(self, obj):
      self.ipProposedRFQNeeded:bool = obj["ipProposedRFQNeeded"]
      """  The new proposed ECOGroup.RFQNeeded value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOOprRFQNeeded_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOOprRestriction_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOOprRestriction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOOprSNRequiredOpr_input:
   """ Required : 
   ipProposedSNRequired
   ds
   """  
   def __init__(self, obj):
      self.ipProposedSNRequired:bool = obj["ipProposedSNRequired"]
      """  The new proposed ECOGroup.SNRequiredOpr value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOOprSNRequiredOpr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOOprStdFormat_input:
   """ Required : 
   ipProposedStdFormat
   ds
   """  
   def __init__(self, obj):
      self.ipProposedStdFormat:str = obj["ipProposedStdFormat"]
      """  The new proposed ECOOpr.StdFormat value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOOprStdFormat_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOOprSubPartNum_input:
   """ Required : 
   ipProposedSubPartNum
   ds
   """  
   def __init__(self, obj):
      self.ipProposedSubPartNum:str = obj["ipProposedSubPartNum"]
      """  The new proposed ECOGroup.SubPartNum value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOOprSubPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOOprSubstance_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOOprSubstance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOOprVendorNumVendorID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOOprVendorNumVendorID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECORevApproved_input:
   """ Required : 
   ipProposedApproved
   ds
   """  
   def __init__(self, obj):
      self.ipProposedApproved:bool = obj["ipProposedApproved"]
      """  The new proposed ipProposedApproved value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECORevApproved_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeECOStageStageSeq_input:
   """ Required : 
   ipProposedStageSeq
   ds
   """  
   def __init__(self, obj):
      self.ipProposedStageSeq:int = obj["ipProposedStageSeq"]
      """  Proposed OprSeq  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeECOStageStageSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEcoMtlInspPlan_input:
   """ Required : 
   ipProposedInspPlan
   ipProposedSpecId
   """  
   def __init__(self, obj):
      self.ipProposedInspPlan:str = obj["ipProposedInspPlan"]
      """  The new proposed ECOMtl.InspPlanPartNum value  """  
      self.ipProposedSpecId:str = obj["ipProposedSpecId"]
      """  The new proposed ECOMtl.SpecID value  """  
      pass

class ChangeEcoMtlInspPlan_output:
   def __init__(self, obj):
      pass

class ChangeEcoMtlMtlAttributeSetID_input:
   """ Required : 
   mtlAttributeSetID
   ds
   """  
   def __init__(self, obj):
      self.mtlAttributeSetID:int = obj["mtlAttributeSetID"]
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeEcoMtlMtlAttributeSetID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEcoMtlSalvageAttributeSetID_input:
   """ Required : 
   salvAttributeSetID
   ds
   """  
   def __init__(self, obj):
      self.salvAttributeSetID:int = obj["salvAttributeSetID"]
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeEcoMtlSalvageAttributeSetID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEcoOprAttributeSetID_input:
   """ Required : 
   attributeSetID
   ds
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangeEcoOprAttributeSetID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangingECOOprAutoReceive_input:
   """ Required : 
   iAutoReceive
   ds
   """  
   def __init__(self, obj):
      self.iAutoReceive:bool = obj["iAutoReceive"]
      """  Proposed value for AutoReceive field  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ChangingECOOprAutoReceive_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckChangeECOCoPartNum_input:
   """ Required : 
   ipProposedPartNum
   ds
   """  
   def __init__(self, obj):
      self.ipProposedPartNum:str = obj["ipProposedPartNum"]
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class CheckChangeECOCoPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckChangeECOMtlMtlSeq_input:
   """ Required : 
   ipProposedMtlSeq
   doCheck
   ds
   """  
   def __init__(self, obj):
      self.ipProposedMtlSeq:int = obj["ipProposedMtlSeq"]
      """  Proposed MtlSeq  """  
      self.doCheck:bool = obj["doCheck"]
      """  True to perform validation, false if the user has accepted the validation message  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class CheckChangeECOMtlMtlSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.opMsgType:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckChangeECOOprOprSeq_input:
   """ Required : 
   ipProposedOprSeq
   doCheck
   ds
   """  
   def __init__(self, obj):
      self.ipProposedOprSeq:int = obj["ipProposedOprSeq"]
      """  Proposed OprSeq  """  
      self.doCheck:bool = obj["doCheck"]
      """  True to perform validation, false if the user has accepted the validation message  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class CheckChangeECOOprOprSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.opMsgType:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckChangeECORevApproved_input:
   """ Required : 
   ipProposedApproved
   ipValidPassword
   ds
   """  
   def __init__(self, obj):
      self.ipProposedApproved:bool = obj["ipProposedApproved"]
      """  The proposed Approved value  """  
      self.ipValidPassword:bool = obj["ipValidPassword"]
      """  A valid password has been sent  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class CheckChangeECORevApproved_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckECOMtlMtlPartNum_input:
   """ Required : 
   ipProposedMtlPartNum
   ds
   """  
   def __init__(self, obj):
      self.ipProposedMtlPartNum:str = obj["ipProposedMtlPartNum"]
      """  The new proposed ttECOMtl.PartNum value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class CheckECOMtlMtlPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.opMsgType:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckECOMtlMtlSeqRelatedOperation_input:
   """ Required : 
   ipProposedMtlSeq
   ipProposedRelatedOperation
   ipProposedRelatedStage
   ds
   """  
   def __init__(self, obj):
      self.ipProposedMtlSeq:int = obj["ipProposedMtlSeq"]
      """  The new proposed ECOMtl.MtlSeq value  """  
      self.ipProposedRelatedOperation:int = obj["ipProposedRelatedOperation"]
      """  The new proposed ECOMtl.RelatedOperation value  """  
      self.ipProposedRelatedStage:str = obj["ipProposedRelatedStage"]
      """  The new proposed ECOMtl.RelatedStage value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class CheckECOMtlMtlSeqRelatedOperation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.opMsgType:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckECOMtlPlanAsAsm_input:
   """ Required : 
   ipProposedPlanAsAsm
   ds
   """  
   def __init__(self, obj):
      self.ipProposedPlanAsAsm:bool = obj["ipProposedPlanAsAsm"]
      """  The new proposed ECOMtl.PlanAsAsm value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class CheckECOMtlPlanAsAsm_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.opMsgType:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckECOMtlPullAsAsm_input:
   """ Required : 
   ipProposedPullAsAsm
   ds
   """  
   def __init__(self, obj):
      self.ipProposedPullAsAsm:bool = obj["ipProposedPullAsAsm"]
      """  The new proposed ECOMtl.PullAsAsm value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class CheckECOMtlPullAsAsm_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.opMsgType:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckECOMtlViewAsAsm_input:
   """ Required : 
   ipProposedViewAsAsm
   ds
   """  
   def __init__(self, obj):
      self.ipProposedViewAsAsm:bool = obj["ipProposedViewAsAsm"]
      """  The new proposed ECOMtl.ViewAsAsm value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class CheckECOMtlViewAsAsm_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckECOOprOprSeq_input:
   """ Required : 
   ipProposedOprSeq
   ds
   """  
   def __init__(self, obj):
      self.ipProposedOprSeq:int = obj["ipProposedOprSeq"]
      """  The new proposed ECOOpr.OprSeq value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class CheckECOOprOprSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.opMsgType:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckECOOprPrimaryProdOpDtl_input:
   """ Required : 
   ds
   ipPrimaryProdOpDtl
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.ipPrimaryProdOpDtl:int = obj["ipPrimaryProdOpDtl"]
      """  The new PrimaryProdOpDtl value to change to  """  
      pass

class CheckECOOprPrimaryProdOpDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckECOOprPrimarySetupOpDtl_input:
   """ Required : 
   ds
   ipPrimarySetupOpDtl
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.ipPrimarySetupOpDtl:int = obj["ipPrimarySetupOpDtl"]
      """  The new PrimarySetupOpDtl value to change to  """  
      pass

class CheckECOOprPrimarySetupOpDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckECOOprPurPoint_input:
   """ Required : 
   ipProposedPurPoint
   ds
   """  
   def __init__(self, obj):
      self.ipProposedPurPoint:str = obj["ipProposedPurPoint"]
      """  The new proposed ECOOpr.PurPoint value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class CheckECOOprPurPoint_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckECOOprVendorNumVendorID_input:
   """ Required : 
   ipProposedVendorNumVendorID
   ds
   """  
   def __init__(self, obj):
      self.ipProposedVendorNumVendorID:str = obj["ipProposedVendorNumVendorID"]
      """  The new proposed ECOOpr.VendorNumVendorID value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class CheckECOOprVendorNumVendorID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckECORevApprovedChanging_input:
   """ Required : 
   ipProposedApproved
   ds
   """  
   def __init__(self, obj):
      self.ipProposedApproved:bool = obj["ipProposedApproved"]
      """  The new proposed ECORev.Approved value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class CheckECORevApprovedChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckECORevApproved_input:
   """ Required : 
   ipProposedApproved
   ipValidPassword
   ds
   """  
   def __init__(self, obj):
      self.ipProposedApproved:bool = obj["ipProposedApproved"]
      """  The new proposed ECOGroup.Approved value  """  
      self.ipValidPassword:bool = obj["ipValidPassword"]
      """  Did the user supply a valid password to run this functionality?
            The value for this parameter should come from running the ValidatePassword method in the
            UserFile BO.  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class CheckECORevApproved_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckECORevValRefDes_input:
   """ Required : 
   ipProposedValResDes
   ds
   """  
   def __init__(self, obj):
      self.ipProposedValResDes:bool = obj["ipProposedValResDes"]
      """  The new proposed ECORev.ValRefDes value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class CheckECORevValRefDes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckInAll_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   ipValidPassword
   ipAuditText
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The ECOGroup.GroupID to check in all for  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  Used for GetDatasetForTree, The Part Number to return data for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  Used for GetDatasetForTree, The Revision Number to return data for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  Used for GetDatasetForTree, The Alternate Method to return data for.  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  Used for GetDatasetForTree, The Process Manufacturing ID to return data for.  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical to determine if you would like the dataset refreshed and brought back  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      self.ipValidPassword:bool = obj["ipValidPassword"]
      """  Did the user supply a valid password to run this functionality?
             The value for this parameter should come from running the ValidatePassword method in the
             UserFile BO.  """  
      self.ipAuditText:str = obj["ipAuditText"]
      """  The text to write to the audit record(s).  """  
      pass

class CheckInAll_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opResultString:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckInAndRefresh_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipValidPassword
   ipAuditText
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID to return costs for.  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to return costs for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to return costs for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The Alternate Method to return costs for.  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID  """  
      self.ipValidPassword:bool = obj["ipValidPassword"]
      """  Did the user supply a valid password to run this functionality?
             The value for this parameter should come from running the ValidatePassword method in the
             UserFile BO.  """  
      self.ipAuditText:str = obj["ipAuditText"]
      """  The text to write to the audit record.  """  
      pass

class CheckInAndRefresh_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckIn_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipValidPassword
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   ipAuditText
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID to return costs for.  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to return costs for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to return costs for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The Alternate Method to return costs for.  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipValidPassword:bool = obj["ipValidPassword"]
      """  Did the user supply a valid password to run this functionality?
             The value for this parameter should come from running the ValidatePassword method in the
             UserFile BO.  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical to determine if you would like the dataset refreshed and brought back  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      self.ipAuditText:str = obj["ipAuditText"]
      """  The text to write to the audit record.  """  
      pass

class CheckIn_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckOutAndRefresh_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipValidPassword
   ipCalledFromRecipe
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID to check out for.  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to check out for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to check out for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The Alternate Method to check out for.  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The Process Manufacturing ID to check out for.  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  The As Of Date to check out for.  """  
      self.ipValidPassword:bool = obj["ipValidPassword"]
      """  Did the user supply a valid password to run this functionality?
            The value for this parameter should come from running the ValidatePassword method in the
            UserFile BO.  """  
      self.ipCalledFromRecipe:bool = obj["ipCalledFromRecipe"]
      """  Parameter to be used to know if the method is called from Engineering Workbench or Recipe Entry.  """  
      pass

class CheckOutAndRefresh_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opECORevSysRowID:str = obj["parameters"]
      self.altMethodMsg:str = obj["parameters"]
      self.altMethodFlg:bool = obj["altMethodFlg"]
      pass

      """  output parameters  """  

class CheckOut_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipValidPassword
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID to check out for.  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to check out for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to check out for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The Alternate Method to check out for.  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to check out for.  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  The As Of Date to check out for.  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipValidPassword:bool = obj["ipValidPassword"]
      """  Did the user supply a valid password to run this functionality?
             The value for this parameter should come from running the ValidatePassword method in the
             UserFile BO.  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical to determine if you would like the dataset refreshed and brought back  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      pass

class CheckOut_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opCheckedOutRevisionNum:str = obj["parameters"]
      self.altMethodMsg:str = obj["parameters"]
      self.altMethodFlg:bool = obj["altMethodFlg"]
      pass

      """  output parameters  """  

class CheckPreECOCoPartInfo_input:
   """ Required : 
   ipProposedPartNum
   ds
   """  
   def __init__(self, obj):
      self.ipProposedPartNum:str = obj["ipProposedPartNum"]
      """  The new proposed ECOCoPart.CoPartNum value  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class CheckPreECOCoPartInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPrePartInfo_input:
   """ Required : 
   partNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  The new PartNum if a substitute part is found, partNum will be the substitute part  """  
      pass

class CheckPrePartInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.vMessage:str = obj["parameters"]
      self.vSubAvail:bool = obj["vSubAvail"]
      self.vMsgType:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckRulesBeforeDelete_input:
   """ Required : 
   partNum
   revisionNum
   altMethod
   opSeq
   mtlSeq
   opDtlSeq
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.opSeq:int = obj["opSeq"]
      self.mtlSeq:int = obj["mtlSeq"]
      self.opDtlSeq:int = obj["opDtlSeq"]
      pass

class CheckRulesBeforeDelete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

class ClearAll_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID to clear all for  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to clear all for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to clear all for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The Alternate Method to clear all for.  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The Process Manufacturing ID to clear all for.  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical to determine if you would like the dataset refreshed and brought back  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      pass

class ClearAll_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteRefDesRange_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipMtlSeq
   ipPrefix
   ipStartNum
   ipEndNum
   ipSuffix
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID  """  
      self.ipMtlSeq:int = obj["ipMtlSeq"]
      """  The ECO Material Seq  """  
      self.ipPrefix:str = obj["ipPrefix"]
      """  The Prefix to be used to delete Reference Designators  """  
      self.ipStartNum:int = obj["ipStartNum"]
      """  The Starting Number to delete Reference Designators  """  
      self.ipEndNum:int = obj["ipEndNum"]
      """  The Ending Number to delete Reference Designators  """  
      self.ipSuffix:str = obj["ipSuffix"]
      """  The Suffix to be used to delete Reference Designators  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class DeleteRefDesRange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ECOGroupExists_input:
   """ Required : 
   ipGroupID
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID to check if it exists in the database.  """  
      pass

class ECOGroupExists_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opECOGroupExists:bool = obj["opECOGroupExists"]
      pass

      """  output parameters  """  

class EcoOprInitSNReqSubConShip_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class EcoOprInitSNReqSubConShip_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_ECOCOPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID for the ECO Group to which this ECORev belongs.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.CoPartNum:str = obj["CoPartNum"]
      """  Companion PartNum identifies the Part that is manufactured along with the main part (ex: Right and Left parts)  """  
      self.CoRevisionNum:str = obj["CoRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the companion part, and is used as part of the primary key  """  
      self.PartsPerOp:int = obj["PartsPerOp"]
      """   Part Per Operation. Active only for Concurrent process
Jobs. Otherwise set to 1.  """  
      self.LbrCostBase:int = obj["LbrCostBase"]
      """   Defines an integer value which is used to calculate a
ratio for prorating the labor costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  """  
      self.MtlCostBase:int = obj["MtlCostBase"]
      """   Defines an integer value which is used to calculate a
ratio for prorating the material costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  """  
      self.IUM:str = obj["IUM"]
      """  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.PreventSugg:bool = obj["PreventSugg"]
      """  If true, MRP will not generate change suggestions for the co-part  """  
      self.PrimaryCost:bool = obj["PrimaryCost"]
      """  Indicates if the parent Part should be used as the primary costing method for the co-part  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.PartMasterPart:bool = obj["PartMasterPart"]
      self.ProcessMode:str = obj["ProcessMode"]
      self.EnablePreventSugg:bool = obj["EnablePreventSugg"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOGroupAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:str = obj["GroupID"]
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

class Erp_Tablesets_ECOGroupListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.Description:str = obj["Description"]
      """  The text description of the ECO Group  """  
      self.GroupClosed:bool = obj["GroupClosed"]
      """  Determines if the ECO group is closed or open.  """  
      self.CommentText:str = obj["CommentText"]
      """  ECO Group comments.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this ECO Group will become effective.  """  
      self.CompletionDate:str = obj["CompletionDate"]
      """  Date which this ECO Group was completed.  """  
      self.DueDate:str = obj["DueDate"]
      """  Date which this ECO group is due to be completed.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date which this ECO group was created.  Not maintainable by the user.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  UserID who created the ECO group.  Not maintainable by the user.  """  
      self.CreatedTime:int = obj["CreatedTime"]
      """  The time (in milliseconds) that the ECO group was created.  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  Date which this ECO group was closed.  Not maintainable by the user.  """  
      self.ClosedBy:str = obj["ClosedBy"]
      """  UserID who closed the ECO group.  Not maintainable by the user.  """  
      self.ClosedTime:int = obj["ClosedTime"]
      """  The time (in milliseconds) that the ECO group was closed.  """  
      self.ECO:str = obj["ECO"]
      """  Engineering Change Order Number. An optional field for reference.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set.  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  The identifier of the workflow stage.  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active milestone task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.CheckInAllowed:bool = obj["CheckInAllowed"]
      """  If FALSE then revisions in this group may not be checked in.  """  
      self.PrimeSalesRepCode:str = obj["PrimeSalesRepCode"]
      """  The primary workflow person associated with the group.  The people are stored in the SalesRep table.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group  """  
      self.CheckOutAllowed:bool = obj["CheckOutAllowed"]
      """  If false then check outs to the ECO Group are not allowed.  This is modified by workflow.  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  This indicates if the workflow for this group is complete.  """  
      self.SingleUser:bool = obj["SingleUser"]
      """  If TRUE then the Engineering Workbench is limited to one user per ECO Group.  If FALSE then individual revisions within a group can be locked.  """  
      self.GrpLocked:bool = obj["GrpLocked"]
      """  Indicates if this ECO Group is locked.  """  
      self.GrpLockedBy:str = obj["GrpLockedBy"]
      """  UserID that has the ECOGroup record locked  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MassAssignDesc:bool = obj["MassAssignDesc"]
      """  Logical to mass assign description to ecorevs  """  
      self.MassAssignECO:bool = obj["MassAssignECO"]
      """  Flag to mass assign ECO to ecorevs  """  
      self.MassAssignEffectiveDate:bool = obj["MassAssignEffectiveDate"]
      """  Flag to mass assign effective date across ecorevs  """  
      self.CanApproveAll:bool = obj["CanApproveAll"]
      """  Flag if Approve All is allowed for this group.  """  
      self.MultiBOMAllowed:bool = obj["MultiBOMAllowed"]
      """  Flag if Multi-BOM is Allowed based off of if mfgsys = VS then value of DCD-BM  """  
      self.CanCheckInAll:bool = obj["CanCheckInAll"]
      """  Flag if Check In All is allowed for this group  """  
      self.WFGroupIDDesc:str = obj["WFGroupIDDesc"]
      """  Description for the WFGroupID.  Based on the hardcoding of workflowtype, foreign link not available.  """  
      self.UseMethodForPartsInTree:bool = obj["UseMethodForPartsInTree"]
      """  If true use method for all parts in tree, otherwise use the part's default method  """  
      self.CurrentWFStageDesc:str = obj["CurrentWFStageDesc"]
      self.EnableCheckInAll:bool = obj["EnableCheckInAll"]
      """  Used for enable/disable the check in all option.  """  
      self.TaskSetIDTaskSetDescription:str = obj["TaskSetIDTaskSetDescription"]
      """  Description of the task set.  """  
      self.TaskSetIDWorkflowType:str = obj["TaskSetIDWorkflowType"]
      """  The type of workflow of this task set.  Possible values are "CRM" - CRM related tasks and "ECO" - ECO tasks  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOGroupListTableset:
   def __init__(self, obj):
      self.ECOGroupList:list[Erp_Tablesets_ECOGroupListRow] = obj["ECOGroupList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ECOGroupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.Description:str = obj["Description"]
      """  The text description of the ECO Group  """  
      self.GroupClosed:bool = obj["GroupClosed"]
      """  Determines if the ECO group is closed or open.  """  
      self.CommentText:str = obj["CommentText"]
      """  ECO Group comments.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this ECO Group will become effective.  """  
      self.CompletionDate:str = obj["CompletionDate"]
      """  Date which this ECO Group was completed.  """  
      self.DueDate:str = obj["DueDate"]
      """  Date which this ECO group is due to be completed.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date which this ECO group was created.  Not maintainable by the user.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  UserID who created the ECO group.  Not maintainable by the user.  """  
      self.CreatedTime:int = obj["CreatedTime"]
      """  The time (in milliseconds) that the ECO group was created.  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  Date which this ECO group was closed.  Not maintainable by the user.  """  
      self.ClosedBy:str = obj["ClosedBy"]
      """  UserID who closed the ECO group.  Not maintainable by the user.  """  
      self.ClosedTime:int = obj["ClosedTime"]
      """  The time (in milliseconds) that the ECO group was closed.  """  
      self.ECO:str = obj["ECO"]
      """  Engineering Change Order Number. An optional field for reference.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set.  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  The identifier of the workflow stage.  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active milestone task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.CheckInAllowed:bool = obj["CheckInAllowed"]
      """  If FALSE then revisions in this group may not be checked in.  """  
      self.PrimeSalesRepCode:str = obj["PrimeSalesRepCode"]
      """  The primary workflow person associated with the group.  The people are stored in the SalesRep table.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group  """  
      self.CheckOutAllowed:bool = obj["CheckOutAllowed"]
      """  If false then check outs to the ECO Group are not allowed.  This is modified by workflow.  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  This indicates if the workflow for this group is complete.  """  
      self.SingleUser:bool = obj["SingleUser"]
      """  If TRUE then the Engineering Workbench is limited to one user per ECO Group.  If FALSE then individual revisions within a group can be locked.  """  
      self.GrpLocked:bool = obj["GrpLocked"]
      """  Indicates if this ECO Group is locked.  """  
      self.GrpLockedBy:str = obj["GrpLockedBy"]
      """  UserID that has the ECOGroup record locked  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MassAssignDesc:bool = obj["MassAssignDesc"]
      """  Logical to mass assign description to ecorevs  """  
      self.MassAssignECO:bool = obj["MassAssignECO"]
      """  Flag to mass assign ECO to ecorevs  """  
      self.MassAssignEffectiveDate:bool = obj["MassAssignEffectiveDate"]
      """  Flag to mass assign effective date across ecorevs  """  
      self.CanApproveAll:bool = obj["CanApproveAll"]
      """  Flag if Approve All is allowed for this group.  """  
      self.MultiBOMAllowed:bool = obj["MultiBOMAllowed"]
      """  Flag if Multi-BOM is Allowed based off of if mfgsys = VS then value of DCD-BM  """  
      self.CanCheckInAll:bool = obj["CanCheckInAll"]
      """  Flag if Check In All is allowed for this group  """  
      self.WFGroupIDDesc:str = obj["WFGroupIDDesc"]
      """  Description for the WFGroupID.  Based on the hardcoding of workflowtype, foreign link not available.  """  
      self.UseMethodForPartsInTree:bool = obj["UseMethodForPartsInTree"]
      """  If true use method for all parts in tree, otherwise use the part's default method  """  
      self.CurrentWFStageDesc:str = obj["CurrentWFStageDesc"]
      self.EnableCheckInAll:bool = obj["EnableCheckInAll"]
      """  Used for enable/disable the check in all option.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaskSetIDWorkflowType:str = obj["TaskSetIDWorkflowType"]
      self.TaskSetIDTaskSetDescription:str = obj["TaskSetIDTaskSetDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOImportRow:
   def __init__(self, obj):
      self.PartNum:str = obj["PartNum"]
      """  The part number.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part number.  """  
      self.TypeCode:str = obj["TypeCode"]
      """  The type code.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  The quantity per.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOMtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:str = obj["GroupID"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.AltMethod:str = obj["AltMethod"]
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      self.MtlSeq:int = obj["MtlSeq"]
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

class Erp_Tablesets_ECOMtlInspRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.PartNum:str = obj["PartNum"]
      """  Parent Part number to which this material item is a component of  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number of the part that this material item is a component of.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material record within a specific Job/Lot/Assembly. This is system assigned. The next available # is determined by reading last JobMtl record on the Job/Lot/Assembly and then adding one to it.  """  
      self.PlanSeq:int = obj["PlanSeq"]
      """  A sequence number that uniquely identifies the ECOMtlInsp record within the ECO material  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number).  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID.  Must be valid in the SpecHed table.  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      """  The original material sequence number at the time of check out. If this record was not created during check out this should remain 0.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOMtlRefDesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.RefDes:str = obj["RefDes"]
      """  Identifier of Reference Designator  """  
      self.RefDesSeq:int = obj["RefDesSeq"]
      """  Unique identifies the reference designator with the material sequence.  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The Part Number of the component material record for the related Parent Part.  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      """  The original material sequence number at the time of check out. If this record was not created during check out this should remain 0.  """  
      self.Side:str = obj["Side"]
      """  Free form side location. (Top, Bottom, Both, Level, etc)  """  
      self.XLocation:int = obj["XLocation"]
      """  X Coordinate of the reference designator  """  
      self.YLocation:int = obj["YLocation"]
      """  Y Coordinate of the reference designator  """  
      self.ZLocation:int = obj["ZLocation"]
      """  Z Coordinate of the reference designator  """  
      self.Rotation:int = obj["Rotation"]
      """  Rotation of the reference designator. Max value = 360.000  """  
      self.Description:str = obj["Description"]
      """  Designator Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOMtlRestrictSubstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.SubstanceID:str = obj["SubstanceID"]
      """  Substance identification.  """  
      self.Weight:int = obj["Weight"]
      """  Default weight of the substance per primary part of UOM  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  By default the primary UOM of the part.  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      """  The original material sequence number at the time of check out. If this record was not created during check out this should remain 0.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.Exempt:bool = obj["Exempt"]
      self.ExemptDate:str = obj["ExemptDate"]
      self.ExemptCertificate:str = obj["ExemptCertificate"]
      self.Manual:bool = obj["Manual"]
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The Part Number of the component material record for the related Parent Part.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.RestrictionDescription:str = obj["RestrictionDescription"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumPartDescription:str = obj["RevisionNumPartDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.SubstanceDescription:str = obj["SubstanceDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOMtlRestrictionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The Part Number of the component material record for the related Parent Part.  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      """  The original material sequence number at the time of check out. If this record was not created during check out this should remain 0.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.Weight:bool = obj["Weight"]
      """  Yes to display when the part has no net weight or when one or more of the selected has no weight.  """  
      self.Manual:bool = obj["Manual"]
      self.ComplianceDate:str = obj["ComplianceDate"]
      self.LastRollUp:str = obj["LastRollUp"]
      self.RollUpType:str = obj["RollUpType"]
      self.BitFlag:int = obj["BitFlag"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.RestrictionDescription:str = obj["RestrictionDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.RevisionNumPartDescription:str = obj["RevisionNumPartDescription"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOMtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Parent Part number to which this material item is a component of  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number of the part that this material item is a component of.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material record within a specific Job/Lot/Assembly. This is system assigned. The next available # is determined by reading last JobMtl record on the Job/Lot/Assembly and then adding one to it.  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The Part Number of the component material record for the related Parent Part.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Quantity Per Parent  """  
      self.FixedQty:bool = obj["FixedQty"]
      """  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   A material record can be related to a specific operation. This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job. The related operation is also used to calculate the JobMtl.ReqDate based on the operations scheduled start date and materials lead time.  """  
      self.SalvagePartNum:str = obj["SalvagePartNum"]
      """  Part number for Salvageable scrap from this material record.  An optional field. This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via Salvage receipt process.  """  
      self.SalvageDescription:str = obj["SalvageDescription"]
      """  Description of Salvageable material. Use Part.Description for a default.  """  
      self.SalvageQtyPer:int = obj["SalvageQtyPer"]
      """  A factor that multiplied by the QtyPer results in the expected total salvage quantity.  """  
      self.SalvageUM:str = obj["SalvageUM"]
      """  Default Unit of measure for the Salvaged Part. Default from the Part.IUM.  """  
      self.SalvageUnitCredit:int = obj["SalvageUnitCredit"]
      """  Estimated Salvage Unit Credit. Use the appropriate cost from the Part master as a default.  """  
      self.MfgComment:str = obj["MfgComment"]
      """  Material comments specific to this manufacturing process. These comments copied to Jobs/Quotes when pulled from BOM.  """  
      self.OverRideMfgComments:bool = obj["OverRideMfgComments"]
      """  Indicates if these comments should override the comments defined in the part master. It controls how the MfgComments are created when this record is pulled into a Job or Quote.  If "Yes" then the comments that are defined in the Part master are NOT copied. If "No" then the ECOMtl.MfgComments will be appended on to the Part.MfgComments when written to the Job/Quote material record.  """  
      self.PurComment:str = obj["PurComment"]
      """   Material comments specific to a manufacturing process. These comments (and optionally the comments from Part Master) are  copied to Jobs/Quotes when the BOM is pulled.
( See OverRidePurComments )  """  
      self.OverRidePurComments:bool = obj["OverRidePurComments"]
      """  Indicates if these comments should override the comments defined in the part master. It controls how the PurComments are created when this record is pulled into a Job or Quote.  If "Yes" then the comments that are defined in the Part master are NOT copied. If "No" then the ECOMtl.PurComments will be appended on to the Part.PurComments when written to the Job/Quote material record.  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of required quantity.  """  
      self.PullAsAsm:bool = obj["PullAsAsm"]
      """  This is relevant for assemblies (Part.Method = Yes). Indicates that if this assembly should be pulled from stock or manufactured as part of the job it is pulled into. If PullAsAsm = No only the assembly record will be pulled into the job/quote (as a material), the related material and operations will not be pulled over.  """  
      self.FindNum:str = obj["FindNum"]
      """  Characters used on the drawing to show where material is used.  """  
      self.ViewAsAsm:bool = obj["ViewAsAsm"]
      """   This is relevant for assemblies (Part.Method = Yes). Indicates that if this assembly when shown in ABOM indented views or on reports it should be shown either as a subassembly or material requirement.  If Yes then the assemblies components will be shown else it is shown as a single material requirement line. Similar to the PullAsAsm flag however this is used to control how subassemblies appear in the ABOM module.
NOTE: AS OF 2.70.400 this function is not implemented.  Pending further analysis. It has been added to the schema to make it easier to implement when decision has been reached.  """  
      self.APSSchedulerName:str = obj["APSSchedulerName"]
      """  Indicates which APS Scheduler module the assembly is scheduled in.  """  
      self.APSSLDate:str = obj["APSSLDate"]
      """  APS Start Limit date.  Prevents APS from scheduling before this date.  """  
      self.APSSLTime:int = obj["APSSLTime"]
      """  APS Start Limit time.  Time, in decimal hours, that APS will not schedule before.  Only valid if APSSLDate is valid.  """  
      self.APSInsertDirection:str = obj["APSInsertDirection"]
      """  Schedule direction.  Valid options are: F=Forward, B=Backward, C=dynamic Constraint based, W=minimum WIP, E=End of work, S=Split longest duration, X=use the direction specified in task entry in APS.  """  
      self.APSInsertCriteria:str = obj["APSInsertCriteria"]
      """  Method of insertion into schedule.  Valid values are: T=best Time, G=same Group, N=uNscheduled, F=Force Insert, I=without resource assignment.  """  
      self.APSAttrib1:int = obj["APSAttrib1"]
      """  Used to calculated setup time during optimization.  """  
      self.APSAttrib2:int = obj["APSAttrib2"]
      """  Used to calculated setup time during optimization.  """  
      self.APSAttrib3:int = obj["APSAttrib3"]
      """  Used to calculated setup time during optimization.  """  
      self.APSAttrib4:int = obj["APSAttrib4"]
      """  Used to calculated setup time during optimization.  """  
      self.APSAddResType:str = obj["APSAddResType"]
      """   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  """  
      self.SalvageMtlBurRate:int = obj["SalvageMtlBurRate"]
      """  The salvage material burden rate for this Part Material.  """  
      self.SalvageEstMtlBurUnitCredit:int = obj["SalvageEstMtlBurUnitCredit"]
      """  Estimated salvage Mtl Burden Unit Credit.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this Part Material.  """  
      self.EstMtlBurUnitCost:int = obj["EstMtlBurUnitCost"]
      """  Estimated Mtl Burden Unit Cost.  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this part material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this part material.  Can be zero if RFQ(s) are not required.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      """  The original material sequence number from the PartMtl record at the time of check out. If this record was not created during check out this should remain 0.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.RelatedStage:str = obj["RelatedStage"]
      """  A material record can be related to a specific operation by stage. This field contains the StageNumber of the operation that it is related to.  """  
      self.BaseMethodOverridden:bool = obj["BaseMethodOverridden"]
      """  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  Parent Alternate Routing method for the part material.  """  
      self.ParentMtlSeq:int = obj["ParentMtlSeq"]
      """  Indicates the parent material sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the Material requirement.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.Weight:int = obj["Weight"]
      """  Material Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Material Weight UOM defaulted from Part Master.  """  
      self.RuleTag:str = obj["RuleTag"]
      """  Rule Tag. Used in the configurator.  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.PlanAsAsm:bool = obj["PlanAsAsm"]
      """  This is relevant for assemblies (Part.Method = Yes). Indicates if the sub-assemby can be spawned off to a different job.  Can be true only if PullAsAsm = true.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReassignSNAsm:bool = obj["ReassignSNAsm"]
      """  flag used to designate if the serial numbers from the job material/subassembly can be reassigned as the serial number of the parent assembly (top assembly or n deep subassembly) being reworked using a job.  """  
      self.LocationView:bool = obj["LocationView"]
      """  Controls if this material record is viewable in Location Management or the web.  """  
      self.CNWeightMeasurement:bool = obj["CNWeightMeasurement"]
      """  Weight Measurement  """  
      self.CNRequiredQty:int = obj["CNRequiredQty"]
      """  Required Quantity  """  
      self.CNConsumedQty:int = obj["CNConsumedQty"]
      """  Consumed Quantity  """  
      self.CNUOM:str = obj["CNUOM"]
      """  UOM  """  
      self.MtlAttributeSetID:int = obj["MtlAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.SalvageAttributeSetID:int = obj["SalvageAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SalvagePlanningNumberOfPieces:int = obj["SalvagePlanningNumberOfPieces"]
      """  Salvage planning number of pieces for this attribute set.  """  
      self.SalvagePlanningAttributeSetID:int = obj["SalvagePlanningAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningPct:int = obj["PlanningPct"]
      """  Planning Percent  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.MtlRevisionNum:str = obj["MtlRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SalvageRevisionNum:str = obj["SalvageRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.AnswerMtlPartNumQuestion:bool = obj["AnswerMtlPartNumQuestion"]
      """  The user's response to potential question for analysis code on mtlpartnum validation.  """  
      self.CNAttritionRate:int = obj["CNAttritionRate"]
      """  Attrition Rate  """  
      self.EnablePartInsp:bool = obj["EnablePartInsp"]
      """  Used to Enable Part Inspection fields on UI  """  
      self.EnablePullAsAsm:bool = obj["EnablePullAsAsm"]
      """  Should pullasasm be enabled on the UI?  """  
      self.EnableViewAsAsm:bool = obj["EnableViewAsAsm"]
      """  Should viewasasm be enabled on the UI?  """  
      self.ExpandTree:bool = obj["ExpandTree"]
      self.IsPartMtl:bool = obj["IsPartMtl"]
      """  Is this a PartMtl record?  Used for build of tree to display PartMtl as ECOMtl.  """  
      self.IsTopPartSalesKit:bool = obj["IsTopPartSalesKit"]
      """  A boolean value to determine if the Material is the Top part sales kit  """  
      self.MtlPartNumMfgComment:str = obj["MtlPartNumMfgComment"]
      """  Used to enter comments for manufacturing when this part is referenced on a job.  """  
      self.MtlPartNumPurComment:str = obj["MtlPartNumPurComment"]
      """  Part Comments that will be used as a default for purchasing.  """  
      self.MtlRevExists:bool = obj["MtlRevExists"]
      """  Is there a revision for the MtlPartNum component of the parent partnum?  """  
      self.OpDesc:str = obj["OpDesc"]
      """  The related operation description  """  
      self.RDEndNum:int = obj["RDEndNum"]
      """  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  """  
      self.RDPrefix:str = obj["RDPrefix"]
      """  The prefix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  """  
      self.RDStartNum:int = obj["RDStartNum"]
      """  This number will be used to create reference designators. This field will be defaulted to ?1?  """  
      self.RDSuffix:str = obj["RDSuffix"]
      """  The suffix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  """  
      self.RelatedECOOprOprSeq:int = obj["RelatedECOOprOprSeq"]
      self.SalvageBaseUOM:str = obj["SalvageBaseUOM"]
      """  Salvage Base Unit of Measure  """  
      self.SalvagePartTrackMulti:bool = obj["SalvagePartTrackMulti"]
      """  Salvage Part Number Track Multi UOM  """  
      self.UseStaging:bool = obj["UseStaging"]
      """  The value of ecorev.usestaging for UI purposes.  """  
      self.AnswerPlanAsAsmQuestion:bool = obj["AnswerPlanAsAsmQuestion"]
      """  The user's response to potential question for analysis code on planasasm validation.  """  
      self.AnswerPullAsAsmQuestion:bool = obj["AnswerPullAsAsmQuestion"]
      """  The user's response to potential question for analysis code on pullasasm validation.  """  
      self.DspUnitMeasure:str = obj["DspUnitMeasure"]
      """  The display unit of measure for the qty/parent field.  """  
      self.EnableFixedQty:bool = obj["EnableFixedQty"]
      """  External field used to control the flag over the FixedQty field on UI screens.  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.SalvEnableAttSetSearch:bool = obj["SalvEnableAttSetSearch"]
      self.PlanningNumberOfPiecesDisp:int = obj["PlanningNumberOfPiecesDisp"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.SalvagePlanningNumberOfPiecesDisp:int = obj["SalvagePlanningNumberOfPiecesDisp"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.APSSchedulerNameAPSSchedulerName:str = obj["APSSchedulerNameAPSSchedulerName"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.MtlPartNumTrackInventoryByRevision:bool = obj["MtlPartNumTrackInventoryByRevision"]
      self.MtlPartNumAttrClassID:str = obj["MtlPartNumAttrClassID"]
      self.MtlPartNumTrackInventoryAttributes:bool = obj["MtlPartNumTrackInventoryAttributes"]
      self.MtlPartNumTrackLots:bool = obj["MtlPartNumTrackLots"]
      self.MtlPartNumTrackDimension:bool = obj["MtlPartNumTrackDimension"]
      self.MtlPartNumSellingFactor:int = obj["MtlPartNumSellingFactor"]
      self.MtlPartNumIUM:str = obj["MtlPartNumIUM"]
      self.MtlPartNumPricePerCode:str = obj["MtlPartNumPricePerCode"]
      self.MtlPartNumTrackSerialNum:bool = obj["MtlPartNumTrackSerialNum"]
      self.MtlPartNumPartDescription:str = obj["MtlPartNumPartDescription"]
      self.MtlPartNumSalesUM:str = obj["MtlPartNumSalesUM"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.RevisionNumPartDescription:str = obj["RevisionNumPartDescription"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.SalvagePartNumTrackInventoryByRevision:bool = obj["SalvagePartNumTrackInventoryByRevision"]
      self.SalvagePartNumPricePerCode:str = obj["SalvagePartNumPricePerCode"]
      self.SalvagePartNumSalesUM:str = obj["SalvagePartNumSalesUM"]
      self.SalvagePartNumTrackDimension:bool = obj["SalvagePartNumTrackDimension"]
      self.SalvagePartNumPartDescription:str = obj["SalvagePartNumPartDescription"]
      self.SalvagePartNumTrackLots:bool = obj["SalvagePartNumTrackLots"]
      self.SalvagePartNumIUM:str = obj["SalvagePartNumIUM"]
      self.SalvagePartNumSellingFactor:int = obj["SalvagePartNumSellingFactor"]
      self.SalvagePartNumAttrClassID:str = obj["SalvagePartNumAttrClassID"]
      self.SalvagePartNumTrackInventoryAttributes:bool = obj["SalvagePartNumTrackInventoryAttributes"]
      self.SalvagePartNumTrackSerialNum:bool = obj["SalvagePartNumTrackSerialNum"]
      self.SalvDynAttrValueSetShortDescription:str = obj["SalvDynAttrValueSetShortDescription"]
      self.SalvDynAttrValueSetDescription:str = obj["SalvDynAttrValueSetDescription"]
      self.StageNoDescription:str = obj["StageNoDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOOpDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  Uniquely identifies an OpDtl.  System assigned.  """  
      self.CapabilityID:str = obj["CapabilityID"]
      """  The user can select the capability the operation is to perform.  The system will select the resource.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  The user can select a Resource Group for the operation to be performed on.  The system will select the actual resource.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource for this operation to be performed on.  """  
      self.SetupHours:int = obj["SetupHours"]
      """  The standard setup hours for the operation.   This is the setup time required for each machine.  """  
      self.ProdHours:int = obj["ProdHours"]
      """  Production hours for this operation.  It is the total hours, as though the operation were running on a single machine.  """  
      self.NumResources:int = obj["NumResources"]
      """  This is the number of resources the operation can run on.  If multiple resources can perform the required Capability, then up to this many will be employed.  This determines the number of setups the system will allow for the operation.  However, the number of setups cannot exceed the number of operations.  The idea being that once a part is on a machine you will complete the operation on that resource.  """  
      self.SetupOrProd:str = obj["SetupOrProd"]
      """  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "S", indicating the resource is RequiredFor the Setup phase of this operation, "P" for Production phase, or "B" meaning Both setup and production phase.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.OpDtlDesc:str = obj["OpDtlDesc"]
      """  Description is initially created when the ECOOpDtl is created.   If the ECOOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  Parent Alternate Routing method of this part operation.  """  
      self.ParentOprSeq:int = obj["ParentOprSeq"]
      """  Indicates the parent operation sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  """  
      self.ParentOpDtlSeq:int = obj["ParentOpDtlSeq"]
      """  Indicates the parent operation detail sequence.  """  
      self.BaseMethodOverridden:bool = obj["BaseMethodOverridden"]
      """  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  """  
      self.OrigOpDtlSeq:int = obj["OrigOpDtlSeq"]
      """  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  """  
      self.OrigOprSeq:int = obj["OrigOprSeq"]
      """  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  """  
      self.ConcurrentCapacity:int = obj["ConcurrentCapacity"]
      """  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  """  
      self.DailyProdRate:int = obj["DailyProdRate"]
      """  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Duplicated from ECOOpr.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Duplicated from ECOOpr.SetupCrewSize. Its the number of people it physically takes to se tup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.PrimaryProd:bool = obj["PrimaryProd"]
      """  Indicates if primary production operation.  """  
      self.PrimarySetup:bool = obj["PrimarySetup"]
      """  Indicates if primary setup operation.  """  
      self.CapabilityDesc:str = obj["CapabilityDesc"]
      """  Capability description  """  
      self.ResourceDesc:str = obj["ResourceDesc"]
      """  Resource description  """  
      self.ResourceGrpDesc:str = obj["ResourceGrpDesc"]
      """  Resource Group description  """  
      self.IsPartOpDtl:bool = obj["IsPartOpDtl"]
      """  Is this a PartOpDtl?  Used when building the tree to show PartOpDtl as ECOOpDtl.  """  
      self.SubContract:bool = obj["SubContract"]
      """  Flag for sub contract  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CapabilityIDDescription:str = obj["CapabilityIDDescription"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOOprActionParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID for the ECO Group to which this ECORev belongs.  """  
      self.PartNum:str = obj["PartNum"]
      """  The user's Internal Part number used to identify line item part. It can be blank if using Process Manufacturing.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part or process manufacture.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The ID of Process Manufacturing revision.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the method.  """  
      self.ActionSeq:int = obj["ActionSeq"]
      """  A sequence number which uniquely identifies action record within the operation set.  """  
      self.ActionParamSeq:int = obj["ActionParamSeq"]
      """  A sequence number which uniquely identifies parameter within the Operation/Action set.  """  
      self.ActionParamFieldDataType:str = obj["ActionParamFieldDataType"]
      """  Data type of Action Parameter  """  
      self.ActionParamValueCharacter:str = obj["ActionParamValueCharacter"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueDate:str = obj["ActionParamValueDate"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueDecimal:int = obj["ActionParamValueDecimal"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueInteger:int = obj["ActionParamValueInteger"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueLogical:bool = obj["ActionParamValueLogical"]
      """  Value of Action Parameter.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOOprActionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID for the ECO Group to which this ECORev belongs.  """  
      self.PartNum:str = obj["PartNum"]
      """  The user's Internal Part number used to identify line item part. It can be blank if using Process Manufacturing.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part or process manufacture.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The ID of Process Manufacturing revision.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the method.  """  
      self.ActionSeq:int = obj["ActionSeq"]
      """  A sequence number which uniquely identifies action record within the operation set.  """  
      self.ActionDesc:str = obj["ActionDesc"]
      """  Description of Action.  """  
      self.Required:bool = obj["Required"]
      """  Indicated if this action must be completed before Operation can be completed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOOprAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:str = obj["GroupID"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.AltMethod:str = obj["AltMethod"]
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      self.OprSeq:int = obj["OprSeq"]
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

class Erp_Tablesets_ECOOprInspRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.PartNum:str = obj["PartNum"]
      """  Parent Part number to which this material item is a component of  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number of the part that this material item is a component of.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.PlanSeq:int = obj["PlanSeq"]
      """  A sequence number that uniquely identifies the ECOOprInsp ecord within the ECO operation  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number).  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID.  Must be valid in the SpecHed table.  """  
      self.OrigOprSeq:int = obj["OrigOprSeq"]
      """  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOOprMachParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  RevisionNum  """  
      self.AltMethod:str = obj["AltMethod"]
      """  AltMethod  """  
      self.OprSeq:int = obj["OprSeq"]
      """  OprSeq  """  
      self.MachParamSeq:int = obj["MachParamSeq"]
      """  MachParamSeq  """  
      self.RequestCode:str = obj["RequestCode"]
      """  RequestCode  """  
      self.MachineNum:str = obj["MachineNum"]
      """  MachineNum  """  
      self.ToolNum:str = obj["ToolNum"]
      """  ToolNum  """  
      self.ParamNum:int = obj["ParamNum"]
      """  ParamNum  """  
      self.ParamUpperLimit:int = obj["ParamUpperLimit"]
      """  ParamUpperLimit  """  
      self.ParamNominalValue:int = obj["ParamNominalValue"]
      """  ParamNominalValue  """  
      self.ParamLowerLimit:int = obj["ParamLowerLimit"]
      """  ParamLowerLimit  """  
      self.ParamDelayValue:int = obj["ParamDelayValue"]
      """  ParamDelayValue  """  
      self.SpecEnable:bool = obj["SpecEnable"]
      """  SpecEnable  """  
      self.SpecControlAlarm:bool = obj["SpecControlAlarm"]
      """  SpecControlAlarm  """  
      self.SpecRunAlarm:bool = obj["SpecRunAlarm"]
      """  SpecRunAlarm  """  
      self.ProcSpecAlarm:bool = obj["ProcSpecAlarm"]
      """  ProcSpecAlarm  """  
      self.ProcControlAlarm:bool = obj["ProcControlAlarm"]
      """  ProcControlAlarm  """  
      self.PartQualSpecEnable:bool = obj["PartQualSpecEnable"]
      """  PartQualSpecEnable  """  
      self.PartQualControlEnable:bool = obj["PartQualControlEnable"]
      """  PartQualControlEnable  """  
      self.OrigOprSeq:int = obj["OrigOprSeq"]
      """  OrigOprSeq  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOOprRestrictSubstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.SubstanceID:str = obj["SubstanceID"]
      """  Substance identification.  """  
      self.Weight:int = obj["Weight"]
      """  Defaulted from Operation Master Substances.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Defaulted from Operation Master Substances.  """  
      self.OrigOprSeq:int = obj["OrigOprSeq"]
      """  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Exempt:bool = obj["Exempt"]
      self.ExemptDate:str = obj["ExemptDate"]
      self.ExemptCertificate:str = obj["ExemptCertificate"]
      self.Manual:bool = obj["Manual"]
      self.BitFlag:int = obj["BitFlag"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.RestrictionDescription:str = obj["RestrictionDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumPartDescription:str = obj["RevisionNumPartDescription"]
      self.SubstanceDescription:str = obj["SubstanceDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOOprRestrictionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.OrigOprSeq:int = obj["OrigOprSeq"]
      """  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.Weight:bool = obj["Weight"]
      """  Yes to display when the part has no net weight or when one or more of the selected has no weight.  """  
      self.Manual:bool = obj["Manual"]
      self.ComplianceDate:str = obj["ComplianceDate"]
      self.BitFlag:int = obj["BitFlag"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.RestrictionDescription:str = obj["RestrictionDescription"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.RevisionNumPartDescription:str = obj["RevisionNumPartDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOOprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Master Code - Links the JobOper  record with a OpMaster record. Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  """  
      self.OpStdID:str = obj["OpStdID"]
      """   The Operation standard ID. This links the JobOPer to the OpStd master file. This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.
Valid for "inside operations" only.  """  
      self.EstSetHours:int = obj["EstSetHours"]
      """  The estimated set up hours. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours.  """  
      self.EstProdHours:int = obj["EstProdHours"]
      """   The estimated Production run hours for internal operations (Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (RunQty / Std).
If StdFormat = "PM" then (RunQty / Std ) / 60.
If StdFormat = "OH" then (RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (RunQty/Basis) X Std.
If StdFormat = "MP" then ((RunQty/Basis) X Std) / 60.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """   The production standard for the operation. It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours. A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  """  
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  """  
      self.OpsPerPart:int = obj["OpsPerPart"]
      """  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Production Quantity per one of the Parent Item.  """  
      self.Machines:int = obj["Machines"]
      """  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to se tup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  Inventory UOM  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  Estimated Unit Cost for the SubContract operation.  Defaults from the Part table if valid PartNum.  """  
      self.DaysOut:int = obj["DaysOut"]
      """  Hours required is calculated as days * 8.  """  
      self.SubPartNum:str = obj["SubPartNum"]
      """  The PartNum to be shipped to the subcontract. Defaults as the Part number of the method to which it belongs (ECOOpr.PartNum).  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job operation comments.  """  
      self.SchedRelation:str = obj["SchedRelation"]
      """   Indicates the scheduling relationship between this and the preceding operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  """  
      self.RunQty:int = obj["RunQty"]
      """  The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0. This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  """  
      self.AddlSetupHours:int = obj["AddlSetupHours"]
      """  Additional Setup Hours that will be required after a certain quantity has been run for this operation. The quantity at which this occurs is established in AddSetupQty field. The system determines the setup hours as SetupHrs + (Max((RunQty - AddlSetupQty,0))/AddlSetUpQty) * AddlSetupHours. Any fractional results of the AddlSetUpQty calculations are rounded up to the next whole number before multiplying by the AddlSetUpHours.  """  
      self.AddlSetUpQty:int = obj["AddlSetUpQty"]
      """  Additional Setup quantity indicates the quantity at which additional setup time will be incurred.  """  
      self.APSPrepOp:int = obj["APSPrepOp"]
      """  Indicates the operation that must precede this operation.  Mainly used to model one to many routing structures.  """  
      self.APSNextOp:int = obj["APSNextOp"]
      """  This is the next operation in the routing.  -1 makes this operation the last one in the routing so far; -2 makes it the first one in the routing so far; 0 means no successor.  """  
      self.APSAltOp:int = obj["APSAltOp"]
      """  Specifies the operation for which this is an alternate.  """  
      self.APSSpecificResource:str = obj["APSSpecificResource"]
      """  Used to assign an operation to a specific resource so that APS does not schedule it elsewhere.  Overrides APSCapability.  """  
      self.APSCycleTime:int = obj["APSCycleTime"]
      """   Cycles per minute.
SQL:  IIF(CINT(JobOper.RunQty) = 0 OR JobOper.SubContract = TRUE, "0", JobOper.EstProdHours * 60 /  JobOper.RunQty)  """  
      self.APSConstantTime:int = obj["APSConstantTime"]
      """   Fixed time, in decimal minutes, to be added to the operation.  Can be used to represent cleanup time or model outsource time.
SQL: IFF(JobOper.SubContract = TRUE, (JobOper.DaysOut * 1440), "0")  """  
      self.APSSetupGroup:int = obj["APSSetupGroup"]
      """  Used to group operations to save on setups.  """  
      self.APSMakeFactor:int = obj["APSMakeFactor"]
      """  Quantity of Part per cycle.  """  
      self.APSContainerSize:int = obj["APSContainerSize"]
      """  Quantity that must be completed before the next operation can start (for overlap); quantity per batch (for batch resources); Auxiliary resource quantity.  """  
      self.APSSchedulerName:str = obj["APSSchedulerName"]
      """  Name of the APS Scheduler Module in which to schedule this operation.  """  
      self.APSMaxLength:int = obj["APSMaxLength"]
      """  If the scheduled time exceeds this value then the operation is split into operations which do not exceed this length.  """  
      self.APSTransferTime:int = obj["APSTransferTime"]
      """  Time between the end of this operation and the start time of the successor operation.  """  
      self.APSEffectiveness:int = obj["APSEffectiveness"]
      """  Cycle time and constant times are divided by this value to get schedule times.  Zeros disable this feature.  """  
      self.APSOperationClass:str = obj["APSOperationClass"]
      """  Type of Operation: P for Prep, D for Processing (Dispatchable in APS terminology).  """  
      self.APSAuxResource:str = obj["APSAuxResource"]
      """  Auxiliary resource requirements.   This is a comma and tilde delimited list of APSAuxResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  """  
      self.APSAddResource:str = obj["APSAddResource"]
      """  Additional resource requirements.   This is a comma and tilde delimited list of APSAddResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  For Additional Resources the Duration = 5 (entire Operation).  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  """  
      self.FAQty:int = obj["FAQty"]
      """  The quantity requested for first article inspection.  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this part operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this part subcontract operation.  Can be zero if RFQ(s) are not required.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID is the unique identifier for the ECO Group  """  
      self.OrigOprSeq:int = obj["OrigOprSeq"]
      """  The original sequence number of the record at the time of check out.  If this record was not created due to a check out then it will be 0.  """  
      self.SetupGroup:str = obj["SetupGroup"]
      """  Used to group operation to save on setups.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PrimarySetupOpDtl:int = obj["PrimarySetupOpDtl"]
      """   Identifies the primary ECOOpDtl to be used for setup.  The setup time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = S or B.  """  
      self.PrimaryProdOpDtl:int = obj["PrimaryProdOpDtl"]
      """   Identifies the primary ECOOpDtl to be used for production.  The production run time for the operation is determined on the ECOOpDtl.
If <> 0, must identify a valid ECOOpDtl.  The ECOOpDtl needs to have a RequiredFor = P or B.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Operation Description.  """  
      self.StageNumber:str = obj["StageNumber"]
      """  The stage number of the operations.  Entered only when the related PartRev.UseStaging flag is true.  """  
      self.BaseMethodOverridden:bool = obj["BaseMethodOverridden"]
      """  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  Parent Alternate Routing method of this part operation.  """  
      self.ParentOprSeq:int = obj["ParentOprSeq"]
      """  Indicates the parent operation sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  """  
      self.BrkQty01:int = obj["BrkQty01"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty02:int = obj["BrkQty02"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty03:int = obj["BrkQty03"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty04:int = obj["BrkQty04"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty05:int = obj["BrkQty05"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty06:int = obj["BrkQty06"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty07:int = obj["BrkQty07"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty08:int = obj["BrkQty08"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty09:int = obj["BrkQty09"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty10:int = obj["BrkQty10"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.PBrkCost01:int = obj["PBrkCost01"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost02:int = obj["PBrkCost02"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost03:int = obj["PBrkCost03"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost04:int = obj["PBrkCost04"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost05:int = obj["PBrkCost05"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost06:int = obj["PBrkCost06"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost07:int = obj["PBrkCost07"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost08:int = obj["PBrkCost08"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost09:int = obj["PBrkCost09"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost10:int = obj["PBrkCost10"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkStdRate01:int = obj["PBrkStdRate01"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate02:int = obj["PBrkStdRate02"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate03:int = obj["PBrkStdRate03"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate04:int = obj["PBrkStdRate04"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate05:int = obj["PBrkStdRate05"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate06:int = obj["PBrkStdRate06"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate07:int = obj["PBrkStdRate07"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate08:int = obj["PBrkStdRate08"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate09:int = obj["PBrkStdRate09"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate10:int = obj["PBrkStdRate10"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.SNRequiredOpr:bool = obj["SNRequiredOpr"]
      """  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  """  
      self.SNRequiredSubConShip:bool = obj["SNRequiredSubConShip"]
      """  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  """  
      self.Weight:int = obj["Weight"]
      """  Operation Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Operation Weight UOM defaulted from Part Master.  """  
      self.SendAheadType:str = obj["SendAheadType"]
      """   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  """  
      self.SendAheadOffset:int = obj["SendAheadOffset"]
      """   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  """  
      self.PrjRoleList:str = obj["PrjRoleList"]
      """  Delimited list of PrjRoleCd codes that are allowed for this operation.  """  
      self.UseAllRoles:bool = obj["UseAllRoles"]
      """  Allow use all Roles  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.PctReg:int = obj["PctReg"]
      """  PctReg  """  
      self.SetupMaterial:int = obj["SetupMaterial"]
      """  SetupMaterial  """  
      self.MaterialColorRating:int = obj["MaterialColorRating"]
      """  MaterialColorRating  """  
      self.MiscInfo1:str = obj["MiscInfo1"]
      """  MiscInfo1  """  
      self.MiscInfo2:str = obj["MiscInfo2"]
      """  MiscInfo2  """  
      self.SetupURL:str = obj["SetupURL"]
      """  SetupURL  """  
      self.ExpPctUp:int = obj["ExpPctUp"]
      """  ExpPctUp  """  
      self.ExpCycTm:int = obj["ExpCycTm"]
      """  ExpCycTm  """  
      self.ExpGood:int = obj["ExpGood"]
      """  ExpGood  """  
      self.NonProdLimit:int = obj["NonProdLimit"]
      """  NonProdLimit  """  
      self.AutoSpcEnable:bool = obj["AutoSpcEnable"]
      """  AutoSpcEnable  """  
      self.AutoSpcPeriod:int = obj["AutoSpcPeriod"]
      """  AutoSpcPeriod  """  
      self.PartQualEnable:bool = obj["PartQualEnable"]
      """  PartQualEnable  """  
      self.AutoSpcSubgroup:int = obj["AutoSpcSubgroup"]
      """  AutoSpcSubgroup  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PulsesPerCycle:int = obj["PulsesPerCycle"]
      """  PulsesPerCycle  """  
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.TemplateID:str = obj["TemplateID"]
      """  TemplateID  """  
      self.SubRevisionNum:str = obj["SubRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.DspBillAddr:str = obj["DspBillAddr"]
      """  The vendor's name and bill to address  """  
      self.EnableSNReqSubConShip:bool = obj["EnableSNReqSubConShip"]
      """  Field used to control the flag on SNRequiredSubConShip field on UI screens.  """  
      self.EnableSNRequiredOpr:bool = obj["EnableSNRequiredOpr"]
      """  Used as a flag to enable controls on UI screens  """  
      self.FinalOpr:bool = obj["FinalOpr"]
      """  The final operation field  """  
      self.HasPriceBreaks:bool = obj["HasPriceBreaks"]
      """  Flag to let you know if you have price breaks.  """  
      self.IsPartOpr:bool = obj["IsPartOpr"]
      """  Is this a PartOpr?  Used when building the tree to show PartOpr as ECOOpr.  """  
      self.OldOprSeq:int = obj["OldOprSeq"]
      """  The original or old OprSeq.  Used when changing the OprSeq.  """  
      self.OpStdDescription:str = obj["OpStdDescription"]
      self.PLMChar03:str = obj["PLMChar03"]
      """  PML ID  """  
      self.PrimaryResourceGrpDesc:str = obj["PrimaryResourceGrpDesc"]
      """  Primary Resource Group description  """  
      self.PrimaryResourceGrpID:str = obj["PrimaryResourceGrpID"]
      """  The Resource Group ID of the primary production operation detail.  """  
      self.RefreshResources:bool = obj["RefreshResources"]
      """  Indicates if the scheduling resources should be refreshed when the op code changes.  """  
      self.SetHoursPerMach:int = obj["SetHoursPerMach"]
      """  The setup hours per machines.  """  
      self.StdFrmtDesc:str = obj["StdFrmtDesc"]
      """  The standard format description.  """  
      self.UseStaging:bool = obj["UseStaging"]
      """  The value of the ecorev.usestaging field for UI purposes  """  
      self.AutoReceive:bool = obj["AutoReceive"]
      """  The auto receive field  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.PrimaryProdOpDtlDesc:str = obj["PrimaryProdOpDtlDesc"]
      self.PrimarySetupOpDtlDesc:str = obj["PrimarySetupOpDtlDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.APSSchedulerNameAPSSchedulerName:str = obj["APSSchedulerNameAPSSchedulerName"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PrimaryProdOpDtlOpDtlDesc:str = obj["PrimaryProdOpDtlOpDtlDesc"]
      self.PrimarySetupOpDtlOpDtlDesc:str = obj["PrimarySetupOpDtlOpDtlDesc"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumPartDescription:str = obj["RevisionNumPartDescription"]
      self.SetupGroupDescription:str = obj["SetupGroupDescription"]
      self.StageNoDescription:str = obj["StageNoDescription"]
      self.SubPartNumTrackInventoryAttributes:bool = obj["SubPartNumTrackInventoryAttributes"]
      self.SubPartNumPricePerCode:str = obj["SubPartNumPricePerCode"]
      self.SubPartNumTrackDimension:bool = obj["SubPartNumTrackDimension"]
      self.SubPartNumTrackSerialNum:bool = obj["SubPartNumTrackSerialNum"]
      self.SubPartNumSellingFactor:int = obj["SubPartNumSellingFactor"]
      self.SubPartNumTrackLots:bool = obj["SubPartNumTrackLots"]
      self.SubPartNumSalesUM:str = obj["SubPartNumSalesUM"]
      self.SubPartNumPartDescription:str = obj["SubPartNumPartDescription"]
      self.SubPartNumIUM:str = obj["SubPartNumIUM"]
      self.SubPartNumAttrClassID:str = obj["SubPartNumAttrClassID"]
      self.SubPartNumTrackInventoryByRevision:bool = obj["SubPartNumTrackInventoryByRevision"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECORevAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupID:str = obj["GroupID"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.AltMethod:str = obj["AltMethod"]
      self.ProcessMfgID:str = obj["ProcessMfgID"]
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

class Erp_Tablesets_ECORevRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID for the ECO Group to which this ECORev belongs.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.RevShortDesc:str = obj["RevShortDesc"]
      """  Short description of the revision. This is NOT the Part description.  """  
      self.RevDescription:str = obj["RevDescription"]
      """  Used to enter a full description of the revision.  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  """  
      self.TLRLaborCost:int = obj["TLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRBurdenCost:int = obj["TLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.TLRMaterialCost:int = obj["TLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSubcontractCost:int = obj["TLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRMtlBurCost:int = obj["TLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSetupLaborCost:int = obj["TLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRSetupBurdenCost:int = obj["TLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRLaborCost:int = obj["LLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRBurdenCost:int = obj["LLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRMaterialCost:int = obj["LLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSubcontractCost:int = obj["LLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRMtlBurCost:int = obj["LLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSetupLaborCost:int = obj["LLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRSetupBurdenCost:int = obj["LLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.RollupDate:str = obj["RollupDate"]
      """  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.ECO:str = obj["ECO"]
      """  Engineering Change Order Number. An optional field for reference.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part revision contains Method of Manufacture details (ECOMtl/ECOOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number ECOOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.CheckInRevisionNum:str = obj["CheckInRevisionNum"]
      """  Revision number which will be used to check in the part.  This will only be used if the CheckIn Revision Number is different from the main RevisionNum field.  """  
      self.CheckInDate:str = obj["CheckInDate"]
      """  The date that the revision is checked in.  """  
      self.CheckedOut:bool = obj["CheckedOut"]
      """  This flag determines if the ECORev record is currently checked out.  There should only be one checked out ECORev record for each Company-Part-Rev.  """  
      self.CheckOutDate:str = obj["CheckOutDate"]
      """  The date that the Part-Rev was last checked out to the group.  """  
      self.CheckedOutBy:str = obj["CheckedOutBy"]
      """  UserID who checked out the revision.  Not maintainable by the user.  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The PartDescription from the Part table to be used for ECO Part searches.  This is copied over during a checkout.  The write trigger on the Part table will sync this field for any currently checked out ECOPartRev.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.RevLocked:bool = obj["RevLocked"]
      """  Indicates if this ECO Revision is locked.  """  
      self.RevLockedBy:str = obj["RevLockedBy"]
      """  UserID that has the ECORev record locked.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  The alternate method of the parent this method inherits from.  """  
      self.UseStaging:bool = obj["UseStaging"]
      """  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  """  
      self.UseAltRevForParts:bool = obj["UseAltRevForParts"]
      """  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  """  
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """  Identifies whether the co-parts are to be produced concurrently or sequentially. The default is sequential. The selected value determines quantity reporting and costing.  """  
      self.AltMethodDesc:str = obj["AltMethodDesc"]
      """  AltMethodDesc  """  
      self.CNCustomsItemNum:str = obj["CNCustomsItemNum"]
      """  Customs Item Number  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.ProcessMfgType:str = obj["ProcessMfgType"]
      """  Type of Process Manufacturing this revision is for: Cleaning, General, Master and Site.  """  
      self.ProcessMfgDescription:str = obj["ProcessMfgDescription"]
      """  Description of Process Manufacturing revision.  """  
      self.ImageID:str = obj["ImageID"]
      """  ID of Revision Image.  """  
      self.UseAdvancedStaging:bool = obj["UseAdvancedStaging"]
      """  Indicates if this revision is to use Advanced Staging.  """  
      self.ECPCEnabled:bool = obj["ECPCEnabled"]
      """  Only Part Revisions marked as Connected Process Control (CPC) enable will be send to CPC.  """  
      self.Configured:bool = obj["Configured"]
      self.EnableGetDetails:bool = obj["EnableGetDetails"]
      """  Should the GetDetails menu options be enabled?  """  
      self.EnableUnLock:bool = obj["EnableUnLock"]
      """  Should the UnLock menu option be enabled?  """  
      self.EnableUpdateable:bool = obj["EnableUpdateable"]
      """  Is the revision updateable?  Used for menu options.  """  
      self.HasCoParts:bool = obj["HasCoParts"]
      self.IsPartRev:bool = obj["IsPartRev"]
      """  Is this a PartRev record?  Used for build of tree to display PartRevs as ECORev.  """  
      self.EnableLock:bool = obj["EnableLock"]
      """  Should the Lock menu option be enabled?  """  
      self.CNHandbookLine:str = obj["CNHandbookLine"]
      """  Handbook Line  """  
      self.CNHandbookCode:str = obj["CNHandbookCode"]
      self.CNCustomsBOM:bool = obj["CNCustomsBOM"]
      self.isFromPartRevision:bool = obj["isFromPartRevision"]
      self.AltMethodDisplay:str = obj["AltMethodDisplay"]
      """  AltMethod string with label for kinetic tree binding in EngWorkBenchEntry  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GroupIDDescription:str = obj["GroupIDDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTypeCode:str = obj["PartNumTypeCode"]
      self.PartRevCreatedBy:str = obj["PartRevCreatedBy"]
      self.PartRevCreatedOn:str = obj["PartRevCreatedOn"]
      self.PartRevApproved:bool = obj["PartRevApproved"]
      self.PlantName:str = obj["PlantName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ECOStageRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group ID for the ECO Group to which this ECORev belongs.  """  
      self.PartNum:str = obj["PartNum"]
      """  The user's Internal Part number used to identify line item part. It can be blank if using Process Manufacturing.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part or process manufacture.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The ID of Process Manufacturing revision.  """  
      self.StageSeq:int = obj["StageSeq"]
      """  A sequence number which uniquely identifies stage record within the stage set.  """  
      self.StageNumber:str = obj["StageNumber"]
      """  The identification of related StageNo.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.GeneralRequirements:str = obj["GeneralRequirements"]
      """  High-level descriptions of General Requirements for Stage.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.StageNumberDescription:str = obj["StageNumberDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EngWorkBenchCostsTableset:
   def __init__(self, obj):
      self.PartRevCosts:list[Erp_Tablesets_PartRevCostsRow] = obj["PartRevCosts"]
      self.PartRevCostsDetail:list[Erp_Tablesets_PartRevCostsDetailRow] = obj["PartRevCostsDetail"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_EngWorkBenchTableset:
   def __init__(self, obj):
      self.ECOGroup:list[Erp_Tablesets_ECOGroupRow] = obj["ECOGroup"]
      self.ECOGroupAttch:list[Erp_Tablesets_ECOGroupAttchRow] = obj["ECOGroupAttch"]
      self.ECORev:list[Erp_Tablesets_ECORevRow] = obj["ECORev"]
      self.ECORevAttch:list[Erp_Tablesets_ECORevAttchRow] = obj["ECORevAttch"]
      self.ECOCOPart:list[Erp_Tablesets_ECOCOPartRow] = obj["ECOCOPart"]
      self.ECOMtl:list[Erp_Tablesets_ECOMtlRow] = obj["ECOMtl"]
      self.ECOMtlAttch:list[Erp_Tablesets_ECOMtlAttchRow] = obj["ECOMtlAttch"]
      self.ECOMtlInsp:list[Erp_Tablesets_ECOMtlInspRow] = obj["ECOMtlInsp"]
      self.ECOMtlRefDes:list[Erp_Tablesets_ECOMtlRefDesRow] = obj["ECOMtlRefDes"]
      self.ECOMtlRestriction:list[Erp_Tablesets_ECOMtlRestrictionRow] = obj["ECOMtlRestriction"]
      self.ECOMtlRestrictSubst:list[Erp_Tablesets_ECOMtlRestrictSubstRow] = obj["ECOMtlRestrictSubst"]
      self.ECOOpr:list[Erp_Tablesets_ECOOprRow] = obj["ECOOpr"]
      self.ECOOprAttch:list[Erp_Tablesets_ECOOprAttchRow] = obj["ECOOprAttch"]
      self.ECOOprAction:list[Erp_Tablesets_ECOOprActionRow] = obj["ECOOprAction"]
      self.ECOOprActionParam:list[Erp_Tablesets_ECOOprActionParamRow] = obj["ECOOprActionParam"]
      self.ECOOprInsp:list[Erp_Tablesets_ECOOprInspRow] = obj["ECOOprInsp"]
      self.ECOOprMachParam:list[Erp_Tablesets_ECOOprMachParamRow] = obj["ECOOprMachParam"]
      self.ECOOpDtl:list[Erp_Tablesets_ECOOpDtlRow] = obj["ECOOpDtl"]
      self.ECOOprRestriction:list[Erp_Tablesets_ECOOprRestrictionRow] = obj["ECOOprRestriction"]
      self.ECOOprRestrictSubst:list[Erp_Tablesets_ECOOprRestrictSubstRow] = obj["ECOOprRestrictSubst"]
      self.ECOImport:list[Erp_Tablesets_ECOImportRow] = obj["ECOImport"]
      self.ECOStage:list[Erp_Tablesets_ECOStageRow] = obj["ECOStage"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MassCheckoutRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CreateNewRev:bool = obj["CreateNewRev"]
      """   Yes - create new revision     
No - do not create new revision  """  
      self.PartNum:str = obj["PartNum"]
      """  Part to checkout and/or create new revision for.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The Revision number to checkout or create.  """  
      self.SourcePartNum:str = obj["SourcePartNum"]
      """  The part number to get details from.  """  
      self.SourceRevisionNum:str = obj["SourceRevisionNum"]
      """  The revision to get details from.  """  
      self.GroupID:str = obj["GroupID"]
      self.RevShortDesc:str = obj["RevShortDesc"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MassCheckoutTableset:
   def __init__(self, obj):
      self.MassCheckout:list[Erp_Tablesets_MassCheckoutRow] = obj["MassCheckout"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartRevCostsDetailRow:
   def __init__(self, obj):
      self.PartNum:str = obj["PartNum"]
      """  The part number.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number  """  
      self.Quantity:int = obj["Quantity"]
      """  The quantity  """  
      self.Approved:bool = obj["Approved"]
      """  Is this approved?  """  
      self.BOMType:str = obj["BOMType"]
      """  The BOM type  """  
      self.BOMLevel:int = obj["BOMLevel"]
      """  The BOM Level  """  
      self.MtlRevision:str = obj["MtlRevision"]
      """  Revision number of the Material Component Part.  The revision is picked based on effectivity dates.  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The Part Number of the component material record for the related Parent Part.  """  
      self.MaterialCost:int = obj["MaterialCost"]
      """  The material cost  """  
      self.LaborCost:int = obj["LaborCost"]
      """  The labor cost  """  
      self.BurdenCost:int = obj["BurdenCost"]
      """  The burden cost  """  
      self.SubcontractCost:int = obj["SubcontractCost"]
      """  The subcontract cost  """  
      self.MaterialBurdenCost:int = obj["MaterialBurdenCost"]
      """  The material burden cost  """  
      self.TotalCost:int = obj["TotalCost"]
      """  The total cost  """  
      self.MaterialUnitCost:int = obj["MaterialUnitCost"]
      """  The material unit cost  """  
      self.LaborUnitCost:int = obj["LaborUnitCost"]
      """  The labor unit cost  """  
      self.BurdenUnitCost:int = obj["BurdenUnitCost"]
      """  The burden unit cost  """  
      self.SubcontractUnitCost:int = obj["SubcontractUnitCost"]
      """  The subcontract unit cost  """  
      self.MaterialBurdenUnitCost:int = obj["MaterialBurdenUnitCost"]
      """  The material burden unit cost  """  
      self.TotalUnitCost:int = obj["TotalUnitCost"]
      """  The total unit cost  """  
      self.QtyPer:int = obj["QtyPer"]
      """  The quantity per parent  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  The required quantity  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  The effective date  """  
      self.BomSequence:int = obj["BomSequence"]
      """  The BOM Sequence  """  
      self.Company:str = obj["Company"]
      """  The company id.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  The Alternate Method  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartRevCostsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The company id.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  The effective date  """  
      self.MaxLevel:int = obj["MaxLevel"]
      """  The maximum level  """  
      self.AssembliesOnly:bool = obj["AssembliesOnly"]
      """  Assemblies Only flag  """  
      self.Quantity:int = obj["Quantity"]
      """  The quantity  """  
      self.MaterialTotalCost:int = obj["MaterialTotalCost"]
      """  The material total cost.  """  
      self.MaterialUnitCost:int = obj["MaterialUnitCost"]
      """  The material unit cost  """  
      self.MaterialPartCost:int = obj["MaterialPartCost"]
      """  The material part cost  """  
      self.LaborTotalCost:int = obj["LaborTotalCost"]
      """  The labor total cost  """  
      self.LaborUnitCost:int = obj["LaborUnitCost"]
      """  The unit cost of labor  """  
      self.LaborPartCost:int = obj["LaborPartCost"]
      """  The part cost of labor  """  
      self.BurdenTotalCost:int = obj["BurdenTotalCost"]
      """  The burden total cost  """  
      self.BurdenUnitCost:int = obj["BurdenUnitCost"]
      """  The burden unit cost  """  
      self.BurdenPartCost:int = obj["BurdenPartCost"]
      """  The burden part cost  """  
      self.SubcontractTotalCost:int = obj["SubcontractTotalCost"]
      """  The subcontract total cost  """  
      self.SubcontractUnitCost:int = obj["SubcontractUnitCost"]
      """  The subcontract unit cost  """  
      self.SubcontractPartCost:int = obj["SubcontractPartCost"]
      """  The subcontract part cost  """  
      self.MtlBurdenTotalCost:int = obj["MtlBurdenTotalCost"]
      """  The material burden total cost  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  The material burden unit cost  """  
      self.MtlBurdenPartCost:int = obj["MtlBurdenPartCost"]
      """  The material burden part cost  """  
      self.CostMethodLabel:str = obj["CostMethodLabel"]
      """  The cost method label  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  The alternate method  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtEngWorkBenchTableset:
   def __init__(self, obj):
      self.ECOGroup:list[Erp_Tablesets_ECOGroupRow] = obj["ECOGroup"]
      self.ECOGroupAttch:list[Erp_Tablesets_ECOGroupAttchRow] = obj["ECOGroupAttch"]
      self.ECORev:list[Erp_Tablesets_ECORevRow] = obj["ECORev"]
      self.ECORevAttch:list[Erp_Tablesets_ECORevAttchRow] = obj["ECORevAttch"]
      self.ECOCOPart:list[Erp_Tablesets_ECOCOPartRow] = obj["ECOCOPart"]
      self.ECOMtl:list[Erp_Tablesets_ECOMtlRow] = obj["ECOMtl"]
      self.ECOMtlAttch:list[Erp_Tablesets_ECOMtlAttchRow] = obj["ECOMtlAttch"]
      self.ECOMtlInsp:list[Erp_Tablesets_ECOMtlInspRow] = obj["ECOMtlInsp"]
      self.ECOMtlRefDes:list[Erp_Tablesets_ECOMtlRefDesRow] = obj["ECOMtlRefDes"]
      self.ECOMtlRestriction:list[Erp_Tablesets_ECOMtlRestrictionRow] = obj["ECOMtlRestriction"]
      self.ECOMtlRestrictSubst:list[Erp_Tablesets_ECOMtlRestrictSubstRow] = obj["ECOMtlRestrictSubst"]
      self.ECOOpr:list[Erp_Tablesets_ECOOprRow] = obj["ECOOpr"]
      self.ECOOprAttch:list[Erp_Tablesets_ECOOprAttchRow] = obj["ECOOprAttch"]
      self.ECOOprAction:list[Erp_Tablesets_ECOOprActionRow] = obj["ECOOprAction"]
      self.ECOOprActionParam:list[Erp_Tablesets_ECOOprActionParamRow] = obj["ECOOprActionParam"]
      self.ECOOprInsp:list[Erp_Tablesets_ECOOprInspRow] = obj["ECOOprInsp"]
      self.ECOOprMachParam:list[Erp_Tablesets_ECOOprMachParamRow] = obj["ECOOprMachParam"]
      self.ECOOpDtl:list[Erp_Tablesets_ECOOpDtlRow] = obj["ECOOpDtl"]
      self.ECOOprRestriction:list[Erp_Tablesets_ECOOprRestrictionRow] = obj["ECOOprRestriction"]
      self.ECOOprRestrictSubst:list[Erp_Tablesets_ECOOprRestrictSubstRow] = obj["ECOOprRestrictSubst"]
      self.ECOImport:list[Erp_Tablesets_ECOImportRow] = obj["ECOImport"]
      self.ECOStage:list[Erp_Tablesets_ECOStageRow] = obj["ECOStage"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExportToPLM_input:
   """ Required : 
   ipGroupID
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The GroupID of the ECOGroup to export.  """  
      pass

class ExportToPLM_output:
   def __init__(self, obj):
      pass

class ExpressPartCheckOut_input:
   """ Required : 
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipValidPassword
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to check out for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to check out for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The Alternate Method to check out for.  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The Process Manufacturing ID to check out for.  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  The As Of Date to check out for.  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipValidPassword:bool = obj["ipValidPassword"]
      """  Did the user supply a valid password to run this functionality?
             The value for this parameter should come from running the ValidatePassword method in the
             UserFile BO.  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical to determine if you would like the dataset refreshed and brought back  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      pass

class ExpressPartCheckOut_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opCheckedOutRevisionNum:str = obj["parameters"]
      self.opGroupID:str = obj["parameters"]
      self.altMethodMsg:str = obj["parameters"]
      self.altMethodFlg:bool = obj["altMethodFlg"]
      pass

      """  output parameters  """  

class GetAvailTaskSets_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDatasetForTreeByRef_input:
   """ Required : 
   ds
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group Id to return data for.  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to return data for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to return data for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The Alternate Method to return data for.  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to return data for.  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to retun a complete dataset for this group?  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      pass

class GetDatasetForTreeByRef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDatasetForTree_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group Id to return data for.  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to return data for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to return data for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The Alternate Method to return data for.  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to return data for.  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to retun a complete dataset for this group?  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
            use the part's default method.  """  
      pass

class GetDatasetForTree_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

class GetDetailsFromImport_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipFileName
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of revision to get details for  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of revision to get details for  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to get details for  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The Alternate Method to get details for  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The Process Manufacturing ID to get details for.  """  
      self.ipFileName:str = obj["ipFileName"]
      """  The filename to import from. This file should reside on the client side.  Used for messages.  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class GetDetailsFromImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.altMethodMsg:str = obj["parameters"]
      self.altMethodFlg:bool = obj["altMethodFlg"]
      pass

      """  output parameters  """  

class GetDetailsFromJob_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipJobNum
   ipAssemblySeq
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of revision to get details for  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of revision to get details for  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to get details for  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The Alternate Method to get details for  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to get details for  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipJobNum:str = obj["ipJobNum"]
      """  The job number to get details from  """  
      self.ipAssemblySeq:int = obj["ipAssemblySeq"]
      """  The assembly sequence to get details from  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical to determine if you would like the dataset refreshed and brought back  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      pass

class GetDetailsFromJob_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

class GetDetailsFromMethods_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipPartRevPartNum
   ipPartRevRevisionNum
   ipPartRevAltMethod
   ipPartRevProcessMfgID
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   ipCopyConfiguration
   ipGetFromConfig
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision to get details for  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision to get details for  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number to get details for  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method to get details for  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to get details for  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipPartRevPartNum:str = obj["ipPartRevPartNum"]
      """  The Part Number of part revision to get details from  """  
      self.ipPartRevRevisionNum:str = obj["ipPartRevRevisionNum"]
      """  The Part Revision Number to get details from  """  
      self.ipPartRevAltMethod:str = obj["ipPartRevAltMethod"]
      """  The Part Alternate method to get details from  """  
      self.ipPartRevProcessMfgID:str = obj["ipPartRevProcessMfgID"]
      """  The Part Process Manufacturing ID to get details from  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical to determine if you would like the dataset refreshed and brought back  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
            refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
            use the part's default method.  """  
      self.ipCopyConfiguration:bool = obj["ipCopyConfiguration"]
      """  Logical to specify to copy the configuration  """  
      self.ipGetFromConfig:bool = obj["ipGetFromConfig"]
      """  Logical to specify to copy the methods from resulting configuration  """  
      pass

class GetDetailsFromMethods_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

class GetDetailsFromQuotes_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipQuoteNum
   ipQuoteLine
   ipAssemblySeq
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision to get details for  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision to get details for  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number to get details for  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method to get details for  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to get details for  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipQuoteNum:int = obj["ipQuoteNum"]
      """  The quote number of the QuoteAsm to get details from  """  
      self.ipQuoteLine:int = obj["ipQuoteLine"]
      """  The quote line of the QuoteAsm to get details from  """  
      self.ipAssemblySeq:int = obj["ipAssemblySeq"]
      """  The assemblyseq of the QuoteAsm to get details from  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical to determine if you would like the dataset refreshed and brought back  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      pass

class GetDetailsFromQuotes_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

class GetDetailsOperations_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipPartRevPartNum
   ipPartRevRevisionNum
   ipPartRevAltMethod
   ipPartRevProcessMfgID
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision to get details for  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision to get details for  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number to get details for  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method to get details for  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to get details for  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipPartRevPartNum:str = obj["ipPartRevPartNum"]
      """  The Part Number of part revision to get details from  """  
      self.ipPartRevRevisionNum:str = obj["ipPartRevRevisionNum"]
      """  The Part Revision Number to get details from  """  
      self.ipPartRevAltMethod:str = obj["ipPartRevAltMethod"]
      """  The Part Alternate method to get details from  """  
      self.ipPartRevProcessMfgID:str = obj["ipPartRevProcessMfgID"]
      """  The Part Process Manufacturing ID to get details from  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical to determine if you would like the dataset refreshed and brought back  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
            refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
            use the part's default method.  """  
      pass

class GetDetailsOperations_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

class GetECOGroupAndECORev_input:
   """ Required : 
   ipGroupID
   ipCheckOutStatus
   CheckUpdateLock
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID to return data for.  """  
      self.ipCheckOutStatus:bool = obj["ipCheckOutStatus"]
      """  Return Checked Out ECORev?  """  
      self.CheckUpdateLock:bool = obj["CheckUpdateLock"]
      """  Check and Update Lock?  """  
      pass

class GetECOGroupAndECORev_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.LockedMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetECORevData_input:
   """ Required : 
   ipGroupID
   ipCheckOutStatus
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID to return data for.  """  
      self.ipCheckOutStatus:bool = obj["ipCheckOutStatus"]
      """  Return Checked Out ECORev?  """  
      pass

class GetECORevData_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

class GetEcoRevPartTypeCode_input:
   """ Required : 
   PartNum
   """  
   def __init__(self, obj):
      self.PartNum:str = obj["PartNum"]
      pass

class GetEcoRevPartTypeCode_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetIfCurrentSiteHasExternalMES_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ECOGroupListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMassCheckout_input:
   """ Required : 
   ds
   groupID
   partNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MassCheckoutTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      """  Group ID  """  
      self.partNum:str = obj["partNum"]
      """  Part number to checkout.  """  
      pass

class GetMassCheckout_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassCheckoutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECOCOPart_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      pass

class GetNewECOCOPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECOGroupAttch_input:
   """ Required : 
   ds
   groupID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      pass

class GetNewECOGroupAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECOGroup_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class GetNewECOGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECOMtlAttch_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   mtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      self.mtlSeq:int = obj["mtlSeq"]
      pass

class GetNewECOMtlAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECOMtlByStageNumber_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   stageNumber
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      self.stageNumber:str = obj["stageNumber"]
      pass

class GetNewECOMtlByStageNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECOMtlInsp_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   mtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      self.mtlSeq:int = obj["mtlSeq"]
      pass

class GetNewECOMtlInsp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECOMtlRefDes_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   mtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      self.mtlSeq:int = obj["mtlSeq"]
      pass

class GetNewECOMtlRefDes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECOMtlRestrictSubst_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   mtlSeq
   restrictionTypeID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      self.mtlSeq:int = obj["mtlSeq"]
      self.restrictionTypeID:str = obj["restrictionTypeID"]
      pass

class GetNewECOMtlRestrictSubst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECOMtlRestriction_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   mtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      self.mtlSeq:int = obj["mtlSeq"]
      pass

class GetNewECOMtlRestriction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECOMtl_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      pass

class GetNewECOMtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECOOpDtl_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   oprSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      self.oprSeq:int = obj["oprSeq"]
      pass

class GetNewECOOpDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECOOprActionParam_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   oprSeq
   actionSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      self.oprSeq:int = obj["oprSeq"]
      self.actionSeq:int = obj["actionSeq"]
      pass

class GetNewECOOprActionParam_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECOOprAction_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   oprSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      self.oprSeq:int = obj["oprSeq"]
      pass

class GetNewECOOprAction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECOOprAttch_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   oprSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      self.oprSeq:int = obj["oprSeq"]
      pass

class GetNewECOOprAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECOOprByStageNumber_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   stageNumber
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      self.stageNumber:str = obj["stageNumber"]
      pass

class GetNewECOOprByStageNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECOOprInsp_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   oprSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      self.oprSeq:int = obj["oprSeq"]
      pass

class GetNewECOOprInsp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECOOprMachParam_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   oprSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      self.oprSeq:int = obj["oprSeq"]
      pass

class GetNewECOOprMachParam_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECOOprRestrictSubst_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   oprSeq
   restrictionTypeID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      self.oprSeq:int = obj["oprSeq"]
      self.restrictionTypeID:str = obj["restrictionTypeID"]
      pass

class GetNewECOOprRestrictSubst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECOOprRestriction_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   oprSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      self.oprSeq:int = obj["oprSeq"]
      pass

class GetNewECOOprRestriction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECOOpr_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      pass

class GetNewECOOpr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECORevAttch_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      pass

class GetNewECORevAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECORevForProcessMfg_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   processType
   plant
   recipeDesc
   revShortDesc
   revNotes
   effectiveDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      self.processType:str = obj["processType"]
      self.plant:str = obj["plant"]
      self.recipeDesc:str = obj["recipeDesc"]
      self.revShortDesc:str = obj["revShortDesc"]
      self.revNotes:str = obj["revNotes"]
      self.effectiveDate:str = obj["effectiveDate"]
      pass

class GetNewECORevForProcessMfg_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECORev_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      pass

class GetNewECORev_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewECOStage_input:
   """ Required : 
   ds
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      pass

class GetNewECOStage_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetProjectRoles_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetRowsWithCustomsBOM_input:
   """ Required : 
   whereClauseECOGroup
   whereClauseECORev
   whereClauseECOMtl
   cnHandbookCode
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseECOGroup:str = obj["whereClauseECOGroup"]
      self.whereClauseECORev:str = obj["whereClauseECORev"]
      self.whereClauseECOMtl:str = obj["whereClauseECOMtl"]
      self.cnHandbookCode:str = obj["cnHandbookCode"]
      """  current CNHandbookCode, the corresponding ECORevs will be excluded from search result  """  
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsWithCustomsBOM_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseECOGroup
   whereClauseECOGroupAttch
   whereClauseECORev
   whereClauseECORevAttch
   whereClauseECOCOPart
   whereClauseECOMtl
   whereClauseECOMtlAttch
   whereClauseECOMtlInsp
   whereClauseECOMtlRefDes
   whereClauseECOMtlRestriction
   whereClauseECOMtlRestrictSubst
   whereClauseECOOpr
   whereClauseECOOprAttch
   whereClauseECOOprAction
   whereClauseECOOprActionParam
   whereClauseECOOprInsp
   whereClauseECOOprMachParam
   whereClauseECOOpDtl
   whereClauseECOOprRestriction
   whereClauseECOOprRestrictSubst
   whereClauseECOImport
   whereClauseECOStage
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseECOGroup:str = obj["whereClauseECOGroup"]
      self.whereClauseECOGroupAttch:str = obj["whereClauseECOGroupAttch"]
      self.whereClauseECORev:str = obj["whereClauseECORev"]
      self.whereClauseECORevAttch:str = obj["whereClauseECORevAttch"]
      self.whereClauseECOCOPart:str = obj["whereClauseECOCOPart"]
      self.whereClauseECOMtl:str = obj["whereClauseECOMtl"]
      self.whereClauseECOMtlAttch:str = obj["whereClauseECOMtlAttch"]
      self.whereClauseECOMtlInsp:str = obj["whereClauseECOMtlInsp"]
      self.whereClauseECOMtlRefDes:str = obj["whereClauseECOMtlRefDes"]
      self.whereClauseECOMtlRestriction:str = obj["whereClauseECOMtlRestriction"]
      self.whereClauseECOMtlRestrictSubst:str = obj["whereClauseECOMtlRestrictSubst"]
      self.whereClauseECOOpr:str = obj["whereClauseECOOpr"]
      self.whereClauseECOOprAttch:str = obj["whereClauseECOOprAttch"]
      self.whereClauseECOOprAction:str = obj["whereClauseECOOprAction"]
      self.whereClauseECOOprActionParam:str = obj["whereClauseECOOprActionParam"]
      self.whereClauseECOOprInsp:str = obj["whereClauseECOOprInsp"]
      self.whereClauseECOOprMachParam:str = obj["whereClauseECOOprMachParam"]
      self.whereClauseECOOpDtl:str = obj["whereClauseECOOpDtl"]
      self.whereClauseECOOprRestriction:str = obj["whereClauseECOOprRestriction"]
      self.whereClauseECOOprRestrictSubst:str = obj["whereClauseECOOprRestrictSubst"]
      self.whereClauseECOImport:str = obj["whereClauseECOImport"]
      self.whereClauseECOStage:str = obj["whereClauseECOStage"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSchedulingBlocks_input:
   """ Required : 
   OpCode
   iPlant
   """  
   def __init__(self, obj):
      self.OpCode:str = obj["OpCode"]
      self.iPlant:str = obj["iPlant"]
      pass

class GetSchedulingBlocks_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class GetTreeStructure_input:
   """ Required : 
   ProcessMfgType
   """  
   def __init__(self, obj):
      self.ProcessMfgType:str = obj["ProcessMfgType"]
      pass

class GetTreeStructure_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GroupLock_input:
   """ Required : 
   ipGroupID
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ecogroup to lock  """  
      pass

class GroupLock_output:
   def __init__(self, obj):
      pass

class GroupUnLock_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ecogroup to lock  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  Used for GetDatasetForTree, The Part Number to return data for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  Used for GetDatasetForTree, The Revision Number to return data for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  Used for GetDatasetForTree, The Alternate Method to return data for.  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  Used for GetDatasetForTree, The Process Manufacturing ID to return data for.  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical to determine if you would like the dataset refreshed and brought back  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class GroupUnLock_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
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

class InsertBOMMtlWithStageNumber_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipSourceRowid
   ipOperSeq
   ipMtlSeq
   ipBeforeMtlRowid
   ipDroppedAs
   ipStageNumber
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision to drop materials to  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision to drop materials to  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number to drop materials to  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method to drop materials to  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to drop materials for  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipSourceRowid:str = obj["ipSourceRowid"]
      """  The rowid of source record could be jobasmbl, jobmtl, or quotemtl, partmtl to be added to the parent ECORev  """  
      self.ipOperSeq:int = obj["ipOperSeq"]
      """  The related operation seq (or 0 if unrelated)  """  
      self.ipMtlSeq:int = obj["ipMtlSeq"]
      """  The material seq to use  """  
      self.ipBeforeMtlRowid:str = obj["ipBeforeMtlRowid"]
      """  The material rowid to insert material before  """  
      self.ipDroppedAs:str = obj["ipDroppedAs"]
      """  The character value to determine where to drop and to drop as what.
             valid values: PartMtl, JobMtl, JobAsmbl, QuoteMtl, QuoteAsm  """  
      self.ipStageNumber:str = obj["ipStageNumber"]
      """  The related stage number  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      pass

class InsertBOMMtlWithStageNumber_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

class InsertBOMMtl_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipSourceRowid
   ipOperSeq
   ipMtlSeq
   ipBeforeMtlRowid
   ipDroppedAs
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision to drop materials to  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision to drop materials to  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number to drop materials to  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method to drop materials to  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to drop materials for  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipSourceRowid:str = obj["ipSourceRowid"]
      """  The rowid of source record could be jobasmbl, jobmtl, or quotemtl, partmtl to be added to the parent ECORev  """  
      self.ipOperSeq:int = obj["ipOperSeq"]
      """  The related operation seq (or 0 if unrelated)  """  
      self.ipMtlSeq:int = obj["ipMtlSeq"]
      """  The material seq to use  """  
      self.ipBeforeMtlRowid:str = obj["ipBeforeMtlRowid"]
      """  The material rowid to insert material before  """  
      self.ipDroppedAs:str = obj["ipDroppedAs"]
      """  The character value to determine where to drop and to drop as what.
             valid values: PartMtl, JobMtl, JobAsmbl, QuoteMtl, QuoteAsm  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      pass

class InsertBOMMtl_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

class InsertBOMOprWithStageNumber_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipSourceRowid
   ipNewOperSeq
   ipBeforeOperRowid
   ipDroppedAs
   ipStageNumber
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision to drop operations to  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision to drop operations to  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number to drop operations to  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method to drop operations to  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to drop operations to  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipSourceRowid:str = obj["ipSourceRowid"]
      """  The rowid of source record could be partopr, joboper, or
             quoteopr to be added to the parent ECORev  """  
      self.ipNewOperSeq:int = obj["ipNewOperSeq"]
      """  The new operation sequence  """  
      self.ipBeforeOperRowid:str = obj["ipBeforeOperRowid"]
      """  The material rowid to insert material before  """  
      self.ipDroppedAs:str = obj["ipDroppedAs"]
      """  The character value to determine where to drop and to drop as what.
             valid values: PartOpr, JobOper, QuoteOpr  """  
      self.ipStageNumber:str = obj["ipStageNumber"]
      """  The stage number the operation is associated to  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      pass

class InsertBOMOprWithStageNumber_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

class InsertBOMOpr_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipSourceRowid
   ipNewOperSeq
   ipBeforeOperRowid
   ipDroppedAs
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision to drop operations to  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision to drop operations to  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number to drop operations to  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method to drop operations to  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to drop operations to  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipSourceRowid:str = obj["ipSourceRowid"]
      """  The rowid of source record could be partopr, joboper, or
             quoteopr to be added to the parent ECORev  """  
      self.ipNewOperSeq:int = obj["ipNewOperSeq"]
      """  The new operation sequence  """  
      self.ipBeforeOperRowid:str = obj["ipBeforeOperRowid"]
      """  The material rowid to insert material before  """  
      self.ipDroppedAs:str = obj["ipDroppedAs"]
      """  The character value to determine where to drop and to drop as what.
             valid values: PartOpr, JobOper, QuoteOpr  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      pass

class InsertBOMOpr_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

class InsertMaterialDemilitedList_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipPartNumMtlDelimList
   ipOperSeq
   ipBeforeMtlRowid
   ipReturn
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision to drop part to  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision to drop part to  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number to drop part to  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method to drop part to  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to drop part to  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipPartNumMtlDelimList:str = obj["ipPartNumMtlDelimList"]
      """  The delimited list of part numbers being added from the part table  """  
      self.ipOperSeq:int = obj["ipOperSeq"]
      """  The related operation seq (or 0 if unrelated)  """  
      self.ipBeforeMtlRowid:str = obj["ipBeforeMtlRowid"]
      """  The material rowid to insert part before  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false  """  
      pass

class InsertMaterialDemilitedList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ipPartNumAskDelimList:str = obj["parameters"]
      pass

      """  output parameters  """  

class InsertMaterialList_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipPartNumMtlList
   ipOperSeq
   ipBeforeMtlRowid
   ipReturn
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      self.ipPartNum:str = obj["ipPartNum"]
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      self.ipAltMethod:str = obj["ipAltMethod"]
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      self.ipPartNumMtlList:str = obj["ipPartNumMtlList"]
      self.ipOperSeq:int = obj["ipOperSeq"]
      self.ipBeforeMtlRowid:str = obj["ipBeforeMtlRowid"]
      self.ipReturn:bool = obj["ipReturn"]
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      pass

class InsertMaterialList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ipPartNumAskList:list = obj[any]
      pass

      """  output parameters  """  

class InsertMaterialWithStageNumberDemilitedList_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipPartNumMtlDelimList
   ipOperSeq
   ipBeforeMtlRowid
   ipReturn
   ipUseMethodForParts
   ipStageNumber
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision to drop part to  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision to drop part to  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number to drop part to  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method to drop part to  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to drop part to  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipPartNumMtlDelimList:str = obj["ipPartNumMtlDelimList"]
      """  The delimited list of part numbers being added from the part table  """  
      self.ipOperSeq:int = obj["ipOperSeq"]
      """  The related operation seq (or 0 if unrelated)  """  
      self.ipBeforeMtlRowid:str = obj["ipBeforeMtlRowid"]
      """  The material rowid to insert part before  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false  """  
      self.ipStageNumber:str = obj["ipStageNumber"]
      """  The related stage for recipe  """  
      pass

class InsertMaterialWithStageNumberDemilitedList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ipPartNumAskDelimList:str = obj["parameters"]
      pass

      """  output parameters  """  

class InsertMaterial_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipPartPartNum
   ipOperSeq
   ipMtlSeq
   ipBeforeMtlRowid
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision to drop part to  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision to drop part to  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number to drop part to  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method to drop part to  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to drop part to  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipPartPartNum:str = obj["ipPartPartNum"]
      """  The part number being added from the part table  """  
      self.ipOperSeq:int = obj["ipOperSeq"]
      """  The related operation seq (or 0 if unrelated)  """  
      self.ipMtlSeq:int = obj["ipMtlSeq"]
      """  The material seq to use  """  
      self.ipBeforeMtlRowid:str = obj["ipBeforeMtlRowid"]
      """  The material rowid to insert part before  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      pass

class InsertMaterial_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

class InsertOpDtlCapability_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipOprSeq
   ipAsOfDate
   ipCompleteTree
   ipCapabilityID
   ipNewOpDtlSeq
   ipBeforeOpDtlRowid
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision to drop operation detail to  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision to drop operation detail to  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number to drop operation detail to  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method to drop operation detail to  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to drop operation detail to  """  
      self.ipOprSeq:int = obj["ipOprSeq"]
      """  The ECO Operation Sequence to drop operation detail to  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipCapabilityID:str = obj["ipCapabilityID"]
      """  The Capability ID being added  """  
      self.ipNewOpDtlSeq:int = obj["ipNewOpDtlSeq"]
      """  The new operation detail seq  """  
      self.ipBeforeOpDtlRowid:str = obj["ipBeforeOpDtlRowid"]
      """  The operation detail rowid to insert operation detail before  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      pass

class InsertOpDtlCapability_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

class InsertOpDtlResGroup_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipOprSeq
   ipAsOfDate
   ipCompleteTree
   ipResourceGrpID
   ipNewOpDtlSeq
   ipBeforeOpDtlRowid
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision to drop operation detail to  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision to drop operation detail to  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number to drop operation detail to  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method to drop operation detail to  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to drop operation detail to  """  
      self.ipOprSeq:int = obj["ipOprSeq"]
      """  The ECO Operation Sequence to drop operation detail to  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipResourceGrpID:str = obj["ipResourceGrpID"]
      """  The Resource Group ID being added  """  
      self.ipNewOpDtlSeq:int = obj["ipNewOpDtlSeq"]
      """  The new operation detail seq  """  
      self.ipBeforeOpDtlRowid:str = obj["ipBeforeOpDtlRowid"]
      """  The operation detail rowid to insert operation detail before  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      pass

class InsertOpDtlResGroup_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

class InsertOpDtlResource_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipOprSeq
   ipAsOfDate
   ipCompleteTree
   ipResourceID
   ipNewOpDtlSeq
   ipBeforeOpDtlRowid
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision to drop operation detail to  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision to drop operation detail to  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number to drop operation detail to  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method to drop operation detail to  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to drop operation to  """  
      self.ipOprSeq:int = obj["ipOprSeq"]
      """  The ECO Operation Sequence to drop operation detail to  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipResourceID:str = obj["ipResourceID"]
      """  The Resource ID being added  """  
      self.ipNewOpDtlSeq:int = obj["ipNewOpDtlSeq"]
      """  The new operation detail seq  """  
      self.ipBeforeOpDtlRowid:str = obj["ipBeforeOpDtlRowid"]
      """  The operation detail rowid to insert operation detail before  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      pass

class InsertOpDtlResource_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

class InsertOperationOPWithStageNumber_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipOpCode
   ipNewOperSeq
   ipBeforeOperRowid
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   ipStageNumber
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision to drop operations to  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision to drop operations to  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number to drop operations to  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method to drop operations to  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to drop operations to  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipOpCode:str = obj["ipOpCode"]
      self.ipNewOperSeq:int = obj["ipNewOperSeq"]
      """  The new operation seq  """  
      self.ipBeforeOperRowid:str = obj["ipBeforeOperRowid"]
      """  The operation rowid to insert operation before  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
            refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
            use the part's default method.  """  
      self.ipStageNumber:str = obj["ipStageNumber"]
      pass

class InsertOperationOPWithStageNumber_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class InsertOperationOP_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipOpCode
   ipNewOperSeq
   ipBeforeOperRowid
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision to drop operations to  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision to drop operations to  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number to drop operations to  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method to drop operations to  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to drop operations to  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipOpCode:str = obj["ipOpCode"]
      self.ipNewOperSeq:int = obj["ipNewOperSeq"]
      """  The new operation seq  """  
      self.ipBeforeOperRowid:str = obj["ipBeforeOperRowid"]
      """  The operation rowid to insert operation before  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      pass

class InsertOperationOP_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class InsertOprCapability_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipCapabilityID
   ipNewOperSeq
   ipBeforeOperRowid
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision to drop operations to  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision to drop operations to  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number to drop operations to  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method to drop operations to  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to drop operations to  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipCapabilityID:str = obj["ipCapabilityID"]
      """  The Capability ID being added  """  
      self.ipNewOperSeq:int = obj["ipNewOperSeq"]
      """  The new operation seq  """  
      self.ipBeforeOperRowid:str = obj["ipBeforeOperRowid"]
      """  The operation rowid to insert operation before  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      pass

class InsertOprCapability_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class InsertOprResGroup_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipResourceGrpID
   ipNewOperSeq
   ipBeforeOperRowid
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision to drop operations to  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision to drop operations to  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number to drop operations to  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method to drop operations to  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to drop operations to  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipResourceGrpID:str = obj["ipResourceGrpID"]
      """  The Resource Group ID being added  """  
      self.ipNewOperSeq:int = obj["ipNewOperSeq"]
      """  The new operation seq  """  
      self.ipBeforeOperRowid:str = obj["ipBeforeOperRowid"]
      """  The operation rowid to insert operation before  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      pass

class InsertOprResGroup_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class InsertOprResource_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipResourceID
   ipNewOperSeq
   ipBeforeOperRowid
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision to drop operations to  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision to drop operations to  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number to drop operations to  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method to drop operations to  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to drop operations to  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipResourceID:str = obj["ipResourceID"]
      """  The Resource ID being added  """  
      self.ipNewOperSeq:int = obj["ipNewOperSeq"]
      """  The new operation seq  """  
      self.ipBeforeOperRowid:str = obj["ipBeforeOperRowid"]
      """  The operation rowid to insert operation before  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      pass

class InsertOprResource_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class IsTopPartSalesKit_input:
   """ Required : 
   partNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  PartNum will be searched in PartMtl.MtlPartNum  """  
      pass

class IsTopPartSalesKit_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class LoadFileAndGetDetailsFromImport_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipUseMethodForParts
   ipFileName
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of revision to get details for  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of revision to get details for  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to get details for  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The Alternate Method to get details for  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The Process Manufacturing ID to get details for.  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false use the part's default method.  """  
      self.ipFileName:str = obj["ipFileName"]
      """  The filename to import from. This file should have been uploaded to server  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class LoadFileAndGetDetailsFromImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LockAllAndRefresh_input:
   """ Required : 
   ipGroupID
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID to lock for.  """  
      pass

class LockAllAndRefresh_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opResultString:str = obj["parameters"]
      pass

      """  output parameters  """  

class LockAll_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID to lock for.  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  Used for GetDatasetForTree, The Part Number to return data for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  Used for GetDatasetForTree, The Revision Number to return data for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  Used for GetDatasetForTree, The Alternate Method to return data for.  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  Used for GetDatasetForTree, The Process Manufacturing ID to return data for.  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical to determine if you would like the dataset refreshed and brought back  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class LockAll_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opResultString:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MassAssignAndRefresh_input:
   """ Required : 
   ipGroupID
   ipMassAssignDesc
   ipMassAssignECO
   ipMassAssignEffectiveDate
   ipMADescription
   ipMAECO
   ipMAEffectiveDate
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID to mass assign for.  """  
      self.ipMassAssignDesc:bool = obj["ipMassAssignDesc"]
      """  Do you want to mass assign Description? Value comes from external ECOGroup.MassAssignDesc  """  
      self.ipMassAssignECO:bool = obj["ipMassAssignECO"]
      """  Do you want to mass assign ECO?  Value comes from external ECOGroup.MassAssignECO.  """  
      self.ipMassAssignEffectiveDate:bool = obj["ipMassAssignEffectiveDate"]
      """  Do you want to mass assign Effective Date? Value comes from external ECOGroup.MassAssignEffectiveDate.  """  
      self.ipMADescription:str = obj["ipMADescription"]
      """  The value of the new description to be mass assigned.  """  
      self.ipMAECO:str = obj["ipMAECO"]
      """  The value of the new ECO to be mass assigned.  """  
      self.ipMAEffectiveDate:str = obj["ipMAEffectiveDate"]
      """  The value of the new Effective Date to be mass assigned.  """  
      pass

class MassAssignAndRefresh_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

class MassAssign_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipMassAssignDesc
   ipMassAssignECO
   ipMassAssignEffectiveDate
   ipMADescription
   ipMAECO
   ipMAEffectiveDate
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID to mass assign for.  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  Used for GetDatasetForTree, The Part Number to return data for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  Used for GetDatasetForTree, The Revision Number to return data for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  Used for GetDatasetForTree, The Alternate Method to return data for.  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  Used for GetDatasetForTree, The Process Manufacturing ID to return data for.  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipMassAssignDesc:bool = obj["ipMassAssignDesc"]
      """  Do you want to mass assign Description? Value comes from external ECOGroup.MassAssignDesc  """  
      self.ipMassAssignECO:bool = obj["ipMassAssignECO"]
      """  Do you want to mass assign ECO?  Value comes from external ECOGroup.MassAssignECO.  """  
      self.ipMassAssignEffectiveDate:bool = obj["ipMassAssignEffectiveDate"]
      """  Do you want to mass assign Effective Date? Value comes from external ECOGroup.MassAssignEffectiveDate.  """  
      self.ipMADescription:str = obj["ipMADescription"]
      """  The value of the new description to be mass assigned.  """  
      self.ipMAECO:str = obj["ipMAECO"]
      """  The value of the new ECO to be mass assigned.  """  
      self.ipMAEffectiveDate:str = obj["ipMAEffectiveDate"]
      """  The value fo the new Effective Date to be mass assigned.  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical to determine if you would like the dataset refreshed and brought back  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class MassAssign_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingMassCheckoutCreateNewRev_input:
   """ Required : 
   sysRowID
   ipCreateNewRev
   ds
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      """  current row  """  
      self.ipCreateNewRev:bool = obj["ipCreateNewRev"]
      """  create new rev yes or no  """  
      self.ds:list[Erp_Tablesets_MassCheckoutTableset] = obj["ds"]
      pass

class OnChangingMassCheckoutCreateNewRev_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassCheckoutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingMassCheckoutRevisionNum_input:
   """ Required : 
   sysRowID
   checkoutRev
   ipProposedRevisionNum
   ds
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      """  current row  """  
      self.checkoutRev:bool = obj["checkoutRev"]
      """  True = checkout part revision, false = details revision  """  
      self.ipProposedRevisionNum:str = obj["ipProposedRevisionNum"]
      self.ds:list[Erp_Tablesets_MassCheckoutTableset] = obj["ds"]
      pass

class OnChangingMassCheckoutRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassCheckoutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingMtlRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class OnChangingMtlRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingNumberOfPieces_input:
   """ Required : 
   numberOfPieces
   ds
   """  
   def __init__(self, obj):
      self.numberOfPieces:int = obj["numberOfPieces"]
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class OnChangingNumberOfPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingProcessMfgType_input:
   """ Required : 
   processMfgType
   ds
   """  
   def __init__(self, obj):
      self.processMfgType:str = obj["processMfgType"]
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class OnChangingProcessMfgType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingSalvageNumberOfPieces_input:
   """ Required : 
   salvageNumberOfPieces
   ds
   """  
   def __init__(self, obj):
      self.salvageNumberOfPieces:int = obj["salvageNumberOfPieces"]
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class OnChangingSalvageNumberOfPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingSalvageRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class OnChangingSalvageRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingSubRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class OnChangingSubRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PreGetDetailsAndReturnConfigType_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipPartRevPartNum
   ipPartRevRevisionNum
   ipPartRevAltMethod
   ipPartRevProcessMfgID
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision to get details for  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision to get details for  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number to get details for  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method to get details for  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to get details for  """  
      self.ipPartRevPartNum:str = obj["ipPartRevPartNum"]
      """  The Part Number of part revision to get details from  """  
      self.ipPartRevRevisionNum:str = obj["ipPartRevRevisionNum"]
      """  The Part Revision Number to get details from  """  
      self.ipPartRevAltMethod:str = obj["ipPartRevAltMethod"]
      """  The Part Alternate method to get details from  """  
      self.ipPartRevProcessMfgID:str = obj["ipPartRevProcessMfgID"]
      """  The Part Process Manufacturing ID to get details from  """  
      pass

class PreGetDetailsAndReturnConfigType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      self.configType:str = obj["parameters"]
      self.configURL:str = obj["parameters"]
      self.configID:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreGetDetails_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipPartRevPartNum
   ipPartRevRevisionNum
   ipPartRevAltMethod
   ipPartRevProcessMfgID
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision to get details for  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision to get details for  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number to get details for  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method to get details for  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID to get details for  """  
      self.ipPartRevPartNum:str = obj["ipPartRevPartNum"]
      """  The Part Number of part revision to get details from  """  
      self.ipPartRevRevisionNum:str = obj["ipPartRevRevisionNum"]
      """  The Part Revision Number to get details from  """  
      self.ipPartRevAltMethod:str = obj["ipPartRevAltMethod"]
      """  The Part Alternate method to get details from  """  
      self.ipPartRevProcessMfgID:str = obj["ipPartRevProcessMfgID"]
      """  The Part Process Manufacturing ID to get details from  """  
      pass

class PreGetDetails_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ProcessMassCheckout_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MassCheckoutTableset] = obj["ds"]
      pass

class ProcessMassCheckout_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MassCheckoutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PromptForPassword_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPromptForPassword:bool = obj["opPromptForPassword"]
      pass

      """  output parameters  """  

class RequestApproveExternalMESValidation_input:
   """ Required : 
   groupID
   partNum
   revisionNum
   altMethod
   processMfgID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  The Group ID of ECO revision  """  
      self.partNum:str = obj["partNum"]
      """  The Part Number of ECO revision  """  
      self.revisionNum:str = obj["revisionNum"]
      """  The ECO Revision Number  """  
      self.altMethod:str = obj["altMethod"]
      """  The ECO Alternate Method  """  
      self.processMfgID:str = obj["processMfgID"]
      """  The ECO Process Manufacturing ID  """  
      pass

class RequestApproveExternalMESValidation_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ResequenceMaterials_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipResequenceBy
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID to resequence for.  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to resequence for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to resequence for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The Alternate Method to resequence for.  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The Process Manufacturing ID to resequence for  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipResequenceBy:str = obj["ipResequenceBy"]
      """  The way the user wants the material resequenced by.
             Valid Values: Material, Part, Item  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical to determine if you would like the dataset refreshed and brought back  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      pass

class ResequenceMaterials_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

class ResequenceOperations_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID to resequence for.  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to resequence for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to resequence for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The Alternate Method to resequence for.  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The Process Manufacturing ID to resequence for  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical to determine if you would like the dataset refreshed and brought back  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      pass

class ResequenceOperations_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

class RevisionLock_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of revision to lock  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of revision to lock  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to lock  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The Alternate Method to lock  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The Process Manufacturing ID to lock for  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical to determine if you would like the dataset refreshed and brought back  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class RevisionLock_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RevisionUnLock_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of revision to unlock  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of revision to unlock  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to unlock  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The Alternate Method to unlock  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The Process Manufacturing ID to unlock  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical to determine if you would like the dataset refreshed and brought back  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class RevisionUnLock_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UnLockAllAndRefresh_input:
   """ Required : 
   ipGroupID
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID to unlock for.  """  
      pass

class UnLockAllAndRefresh_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opResultString:str = obj["parameters"]
      pass

      """  output parameters  """  

class UnLockAll_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID to unlock for.  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  Used for GetDatasetForTree, The Part Number to return data for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  Used for GetDatasetForTree, The Revision Number to return data for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  Used for GetDatasetForTree, The Alternate Method to return data for.  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  Used for GetDatasetForTree, The Process Manufacturing ID to return data for.  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical to determine if you would like the dataset refreshed and brought back  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class UnLockAll_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opResultString:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UndoCheckOut_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID to check out for.  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to check out for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to check out for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The Alternate Method to check out for.  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The Process Manufacturing ID to check out for.  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  The As Of Date to check out for.  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical to determine if you would like the dataset refreshed and brought back  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class UndoCheckOut_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateCurrentECORev_input:
   """ Required : 
   EngWorkBenchData
   """  
   def __init__(self, obj):
      self.EngWorkBenchData      #schema had no properties on an object.
      pass

class UpdateCurrentECORev_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.EngWorkBenchData: UNKNOW TYPE(error 2338) = obj["EngWorkBenchData"]
      pass

      """  output parameters  """  

class UpdateCurrentPartECORev_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class UpdateCurrentPartECORev_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateECORev_input:
   """ Required : 
   EngWorkBenchData
   """  
   def __init__(self, obj):
      self.EngWorkBenchData      #schema had no properties on an object.
      pass

class UpdateECORev_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.EngWorkBenchData: UNKNOW TYPE(error 2338) = obj["EngWorkBenchData"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtEngWorkBenchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtEngWorkBenchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdatePartECORev_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class UpdatePartECORev_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateBill_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipCompleteTree
   ipReturn
   ipGetDatasetForTree
   ipUseMethodForParts
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID to return costs for.  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to return costs for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to return costs for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The Alternate Method to return costs for.  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The Process Manufacturing ID to return costs for  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Used for GetDatasetForTree, The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Used for GetDatasetForTree, Would you like to retun a complete dataset for this group?  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical to determine if you would like the dataset refreshed and brought back  """  
      self.ipGetDatasetForTree:bool = obj["ipGetDatasetForTree"]
      """  If ipReturn=True then Logical to determine if you would like the dataset
             refreshed by GetDatasetForTree?  True = call GetDatasetFor, False = call GetByID  """  
      self.ipUseMethodForParts:bool = obj["ipUseMethodForParts"]
      """  If true use the method passed in for all parts in the tree, if false
             use the part's default method.  """  
      pass

class ValidateBill_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateInspection_input:
   """ Required : 
   ipProposedInspPlan
   ipProposedSpecId
   iptable
   ds
   """  
   def __init__(self, obj):
      self.ipProposedInspPlan:str = obj["ipProposedInspPlan"]
      """  The new proposed InspPlanPartNum value  """  
      self.ipProposedSpecId:str = obj["ipProposedSpecId"]
      """  The new proposed SpecID value  """  
      self.iptable:str = obj["iptable"]
      """  table name  """  
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

class ValidateInspection_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EngWorkBenchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateRefDes_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID of ECO revision  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number of ECO revision  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The ECO Revision Number  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The ECO Alternate Method  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The ECO Process Manufacturing ID  """  
      pass

class ValidateRefDes_output:
   def __init__(self, obj):
      pass

class ViewCosts_input:
   """ Required : 
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipAsOfDate
   ipQuantity
   ipMaxLevel
   ipAssembliesOnly
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID to return costs for.  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to return costs for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to return costs for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The Alternate method to return costs for.  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The Process Manufacturing ID to return costs for.  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  The As of Date to return costs for.  """  
      self.ipQuantity:int = obj["ipQuantity"]
      """  The Quantity to return costs for.  """  
      self.ipMaxLevel:int = obj["ipMaxLevel"]
      """  The Max Level to return costs for.  """  
      self.ipAssembliesOnly:bool = obj["ipAssembliesOnly"]
      """  Assemblies only?  """  
      pass

class ViewCosts_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EngWorkBenchCostsTableset] = obj["returnObj"]
      pass

class getNextOpDtlSeq_input:
   """ Required : 
   ipCompany
   ipGroupID
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipOprSeq
   """  
   def __init__(self, obj):
      self.ipCompany:str = obj["ipCompany"]
      self.ipGroupID:str = obj["ipGroupID"]
      self.ipPartNum:str = obj["ipPartNum"]
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      self.ipAltMethod:str = obj["ipAltMethod"]
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      self.ipOprSeq:int = obj["ipOprSeq"]
      pass

class getNextOpDtlSeq_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

