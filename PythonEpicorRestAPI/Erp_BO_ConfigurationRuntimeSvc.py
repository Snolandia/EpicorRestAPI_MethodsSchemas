import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ConfigurationRuntimeSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ConfigurationRuntimes(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ConfigurationRuntimes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConfigurationRuntimes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcValueGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ConfigurationRuntimes",headers=creds) as resp:
           return await resp.json()

async def post_ConfigurationRuntimes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConfigurationRuntimes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcValueGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcValueGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ConfigurationRuntimes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ConfigurationRuntimes_Company_GroupSeq(Company, GroupSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConfigurationRuntime item
   Description: Calls GetByID to retrieve the ConfigurationRuntime item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConfigurationRuntime
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupSeq: Desc: GroupSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcValueGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ConfigurationRuntimes(" + Company + "," + GroupSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ConfigurationRuntimes_Company_GroupSeq(Company, GroupSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ConfigurationRuntime for the service
   Description: Calls UpdateExt to update ConfigurationRuntime. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConfigurationRuntime
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupSeq: Desc: GroupSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcValueGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ConfigurationRuntimes(" + Company + "," + GroupSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ConfigurationRuntimes_Company_GroupSeq(Company, GroupSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ConfigurationRuntime item
   Description: Call UpdateExt to delete ConfigurationRuntime item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConfigurationRuntime
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupSeq: Desc: GroupSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ConfigurationRuntimes(" + Company + "," + GroupSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ConfigurationRuntimes_Company_GroupSeq_PcValueHeads(Company, GroupSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PcValueHeads items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcValueHeads1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupSeq: Desc: GroupSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcValueHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ConfigurationRuntimes(" + Company + "," + GroupSeq + ")/PcValueHeads",headers=creds) as resp:
           return await resp.json()

async def get_ConfigurationRuntimes_Company_GroupSeq_PcValueHeads_Company_GroupSeq_HeadNum(Company, GroupSeq, HeadNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcValueHead item
   Description: Calls GetByID to retrieve the PcValueHead item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcValueHead1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupSeq: Desc: GroupSeq   Required: True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcValueHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/ConfigurationRuntimes(" + Company + "," + GroupSeq + ")/PcValueHeads(" + Company + "," + GroupSeq + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcValueHeads(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcValueHeads items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcValueHeads
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcValueHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueHeads",headers=creds) as resp:
           return await resp.json()

async def post_PcValueHeads(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcValueHeads
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcValueHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcValueHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueHeads", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcValueHeads_Company_GroupSeq_HeadNum(Company, GroupSeq, HeadNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcValueHead item
   Description: Calls GetByID to retrieve the PcValueHead item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcValueHead
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupSeq: Desc: GroupSeq   Required: True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcValueHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueHeads(" + Company + "," + GroupSeq + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcValueHeads_Company_GroupSeq_HeadNum(Company, GroupSeq, HeadNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcValueHead for the service
   Description: Calls UpdateExt to update PcValueHead. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcValueHead
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupSeq: Desc: GroupSeq   Required: True
      :param HeadNum: Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcValueHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueHeads(" + Company + "," + GroupSeq + "," + HeadNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcValueHeads_Company_GroupSeq_HeadNum(Company, GroupSeq, HeadNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcValueHead item
   Description: Call UpdateExt to delete PcValueHead item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcValueHead
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupSeq: Desc: GroupSeq   Required: True
      :param HeadNum: Desc: HeadNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueHeads(" + Company + "," + GroupSeq + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcConfigurationParams(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcConfigurationParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcConfigurationParams
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcConfigurationParamsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcConfigurationParams",headers=creds) as resp:
           return await resp.json()

async def post_PcConfigurationParams(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcConfigurationParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcConfigurationParamsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcConfigurationParamsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcConfigurationParams", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcConfigurationParams_Company_UniqueID(Company, UniqueID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcConfigurationParam item
   Description: Calls GetByID to retrieve the PcConfigurationParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcConfigurationParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param UniqueID: Desc: UniqueID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcConfigurationParamsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcConfigurationParams(" + Company + "," + UniqueID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcConfigurationParams_Company_UniqueID(Company, UniqueID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcConfigurationParam for the service
   Description: Calls UpdateExt to update PcConfigurationParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcConfigurationParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param UniqueID: Desc: UniqueID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcConfigurationParamsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcConfigurationParams(" + Company + "," + UniqueID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcConfigurationParams_Company_UniqueID(Company, UniqueID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcConfigurationParam item
   Description: Call UpdateExt to delete PcConfigurationParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcConfigurationParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param UniqueID: Desc: UniqueID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcConfigurationParams(" + Company + "," + UniqueID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcConfiguredDrawings(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcConfiguredDrawings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcConfiguredDrawings
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcConfiguredDrawingsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcConfiguredDrawings",headers=creds) as resp:
           return await resp.json()

async def post_PcConfiguredDrawings(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcConfiguredDrawings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcConfiguredDrawingsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcConfiguredDrawingsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcConfiguredDrawings", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcConfiguredDrawings_Company_GroupSeq_HeadNum_InputName(Company, GroupSeq, HeadNum, InputName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcConfiguredDrawing item
   Description: Calls GetByID to retrieve the PcConfiguredDrawing item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcConfiguredDrawing
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupSeq: Desc: GroupSeq   Required: True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcConfiguredDrawingsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcConfiguredDrawings(" + Company + "," + GroupSeq + "," + HeadNum + "," + InputName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcConfiguredDrawings_Company_GroupSeq_HeadNum_InputName(Company, GroupSeq, HeadNum, InputName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcConfiguredDrawing for the service
   Description: Calls UpdateExt to update PcConfiguredDrawing. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcConfiguredDrawing
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupSeq: Desc: GroupSeq   Required: True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcConfiguredDrawingsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcConfiguredDrawings(" + Company + "," + GroupSeq + "," + HeadNum + "," + InputName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcConfiguredDrawings_Company_GroupSeq_HeadNum_InputName(Company, GroupSeq, HeadNum, InputName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcConfiguredDrawing item
   Description: Call UpdateExt to delete PcConfiguredDrawing item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcConfiguredDrawing
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupSeq: Desc: GroupSeq   Required: True
      :param HeadNum: Desc: HeadNum   Required: True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcConfiguredDrawings(" + Company + "," + GroupSeq + "," + HeadNum + "," + InputName + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcContextProperties(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcContextProperties items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcContextProperties
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcContextPropertiesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcContextProperties",headers=creds) as resp:
           return await resp.json()

async def post_PcContextProperties(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcContextProperties
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcContextPropertiesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcContextPropertiesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcContextProperties", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcContextProperties_ConfigurationID_CompanyID(ConfigurationID, CompanyID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcContextProperty item
   Description: Calls GetByID to retrieve the PcContextProperty item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcContextProperty
      :param ConfigurationID: Desc: ConfigurationID   Required: True   Allow empty value : True
      :param CompanyID: Desc: CompanyID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcContextPropertiesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcContextProperties(" + ConfigurationID + "," + CompanyID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcContextProperties_ConfigurationID_CompanyID(ConfigurationID, CompanyID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcContextProperty for the service
   Description: Calls UpdateExt to update PcContextProperty. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcContextProperty
      :param ConfigurationID: Desc: ConfigurationID   Required: True   Allow empty value : True
      :param CompanyID: Desc: CompanyID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcContextPropertiesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcContextProperties(" + ConfigurationID + "," + CompanyID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcContextProperties_ConfigurationID_CompanyID(ConfigurationID, CompanyID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcContextProperty item
   Description: Call UpdateExt to delete PcContextProperty item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcContextProperty
      :param ConfigurationID: Desc: ConfigurationID   Required: True   Allow empty value : True
      :param CompanyID: Desc: CompanyID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcContextProperties(" + ConfigurationID + "," + CompanyID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcInputsLayerDetails(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcInputsLayerDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputsLayerDetails
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsLayerDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsLayerDetails",headers=creds) as resp:
           return await resp.json()

async def post_PcInputsLayerDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputsLayerDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsLayerDetails", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcInputsLayerDetails_Company_ConfigID_InputName_ImageLayerID_LayerSeq(Company, ConfigID, InputName, ImageLayerID, LayerSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcInputsLayerDetail item
   Description: Calls GetByID to retrieve the PcInputsLayerDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsLayerDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param LayerSeq: Desc: LayerSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsLayerDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsLayerDetails(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + "," + LayerSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcInputsLayerDetails_Company_ConfigID_InputName_ImageLayerID_LayerSeq(Company, ConfigID, InputName, ImageLayerID, LayerSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcInputsLayerDetail for the service
   Description: Calls UpdateExt to update PcInputsLayerDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInputsLayerDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param LayerSeq: Desc: LayerSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsLayerDetails(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + "," + LayerSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcInputsLayerDetails_Company_ConfigID_InputName_ImageLayerID_LayerSeq(Company, ConfigID, InputName, ImageLayerID, LayerSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcInputsLayerDetail item
   Description: Call UpdateExt to delete PcInputsLayerDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInputsLayerDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param LayerSeq: Desc: LayerSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsLayerDetails(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + "," + LayerSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcInputsLayerHeaders(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcInputsLayerHeaders items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputsLayerHeaders
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsLayerHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsLayerHeaders",headers=creds) as resp:
           return await resp.json()

async def post_PcInputsLayerHeaders(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputsLayerHeaders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerHeaderRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerHeaderRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsLayerHeaders", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcInputsLayerHeaders_Company_ConfigID_InputName_ImageLayerID(Company, ConfigID, InputName, ImageLayerID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcInputsLayerHeader item
   Description: Calls GetByID to retrieve the PcInputsLayerHeader item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsLayerHeader
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsLayerHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsLayerHeaders(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcInputsLayerHeaders_Company_ConfigID_InputName_ImageLayerID(Company, ConfigID, InputName, ImageLayerID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcInputsLayerHeader for the service
   Description: Calls UpdateExt to update PcInputsLayerHeader. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInputsLayerHeader
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerHeaderRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsLayerHeaders(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcInputsLayerHeaders_Company_ConfigID_InputName_ImageLayerID(Company, ConfigID, InputName, ImageLayerID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcInputsLayerHeader item
   Description: Call UpdateExt to delete PcInputsLayerHeader item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInputsLayerHeader
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsLayerHeaders(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcInputsPublishToDocParams(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcInputsPublishToDocParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputsPublishToDocParams
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsPublishToDocParamsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsPublishToDocParams",headers=creds) as resp:
           return await resp.json()

async def post_PcInputsPublishToDocParams(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputsPublishToDocParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputsPublishToDocParamsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputsPublishToDocParamsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsPublishToDocParams", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcInputsPublishToDocParams_Company_Key(Company, Key, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcInputsPublishToDocParam item
   Description: Calls GetByID to retrieve the PcInputsPublishToDocParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsPublishToDocParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key: Desc: Key   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsPublishToDocParamsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsPublishToDocParams(" + Company + "," + Key + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcInputsPublishToDocParams_Company_Key(Company, Key, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcInputsPublishToDocParam for the service
   Description: Calls UpdateExt to update PcInputsPublishToDocParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInputsPublishToDocParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key: Desc: Key   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputsPublishToDocParamsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsPublishToDocParams(" + Company + "," + Key + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcInputsPublishToDocParams_Company_Key(Company, Key, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcInputsPublishToDocParam item
   Description: Call UpdateExt to delete PcInputsPublishToDocParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInputsPublishToDocParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key: Desc: Key   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputsPublishToDocParams(" + Company + "," + Key + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcInputVars(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcInputVars items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputVars
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputVarRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputVars",headers=creds) as resp:
           return await resp.json()

async def post_PcInputVars(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputVars
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputVarRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputVarRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputVars", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcInputVars_Company_VarName(Company, VarName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcInputVar item
   Description: Calls GetByID to retrieve the PcInputVar item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputVar
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VarName: Desc: VarName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputVarRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputVars(" + Company + "," + VarName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcInputVars_Company_VarName(Company, VarName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcInputVar for the service
   Description: Calls UpdateExt to update PcInputVar. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInputVar
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VarName: Desc: VarName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputVarRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputVars(" + Company + "," + VarName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcInputVars_Company_VarName(Company, VarName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcInputVar item
   Description: Call UpdateExt to delete PcInputVar item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInputVar
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VarName: Desc: VarName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcInputVars(" + Company + "," + VarName + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcValueInputLayerDetails(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcValueInputLayerDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcValueInputLayerDetails
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcValueInputLayerDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueInputLayerDetails",headers=creds) as resp:
           return await resp.json()

async def post_PcValueInputLayerDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcValueInputLayerDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcValueInputLayerDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcValueInputLayerDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueInputLayerDetails", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcValueInputLayerDetails_Company_GroupSeq_HeadNum_ConfigID_InputName_ImageLayerID_LayerSeq(Company, GroupSeq, HeadNum, ConfigID, InputName, ImageLayerID, LayerSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcValueInputLayerDetail item
   Description: Calls GetByID to retrieve the PcValueInputLayerDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcValueInputLayerDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupSeq: Desc: GroupSeq   Required: True
      :param HeadNum: Desc: HeadNum   Required: True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param LayerSeq: Desc: LayerSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcValueInputLayerDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueInputLayerDetails(" + Company + "," + GroupSeq + "," + HeadNum + "," + ConfigID + "," + InputName + "," + ImageLayerID + "," + LayerSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcValueInputLayerDetails_Company_GroupSeq_HeadNum_ConfigID_InputName_ImageLayerID_LayerSeq(Company, GroupSeq, HeadNum, ConfigID, InputName, ImageLayerID, LayerSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcValueInputLayerDetail for the service
   Description: Calls UpdateExt to update PcValueInputLayerDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcValueInputLayerDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupSeq: Desc: GroupSeq   Required: True
      :param HeadNum: Desc: HeadNum   Required: True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param LayerSeq: Desc: LayerSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcValueInputLayerDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueInputLayerDetails(" + Company + "," + GroupSeq + "," + HeadNum + "," + ConfigID + "," + InputName + "," + ImageLayerID + "," + LayerSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcValueInputLayerDetails_Company_GroupSeq_HeadNum_ConfigID_InputName_ImageLayerID_LayerSeq(Company, GroupSeq, HeadNum, ConfigID, InputName, ImageLayerID, LayerSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcValueInputLayerDetail item
   Description: Call UpdateExt to delete PcValueInputLayerDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcValueInputLayerDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupSeq: Desc: GroupSeq   Required: True
      :param HeadNum: Desc: HeadNum   Required: True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param LayerSeq: Desc: LayerSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueInputLayerDetails(" + Company + "," + GroupSeq + "," + HeadNum + "," + ConfigID + "," + InputName + "," + ImageLayerID + "," + LayerSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcValueInputLayerHeaders(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcValueInputLayerHeaders items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcValueInputLayerHeaders
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcValueInputLayerHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueInputLayerHeaders",headers=creds) as resp:
           return await resp.json()

async def post_PcValueInputLayerHeaders(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcValueInputLayerHeaders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcValueInputLayerHeaderRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcValueInputLayerHeaderRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueInputLayerHeaders", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcValueInputLayerHeaders_Company_GroupSeq_HeadNum_ConfigID_InputName_ImageLayerID(Company, GroupSeq, HeadNum, ConfigID, InputName, ImageLayerID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcValueInputLayerHeader item
   Description: Calls GetByID to retrieve the PcValueInputLayerHeader item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcValueInputLayerHeader
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupSeq: Desc: GroupSeq   Required: True
      :param HeadNum: Desc: HeadNum   Required: True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcValueInputLayerHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueInputLayerHeaders(" + Company + "," + GroupSeq + "," + HeadNum + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcValueInputLayerHeaders_Company_GroupSeq_HeadNum_ConfigID_InputName_ImageLayerID(Company, GroupSeq, HeadNum, ConfigID, InputName, ImageLayerID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcValueInputLayerHeader for the service
   Description: Calls UpdateExt to update PcValueInputLayerHeader. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcValueInputLayerHeader
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupSeq: Desc: GroupSeq   Required: True
      :param HeadNum: Desc: HeadNum   Required: True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcValueInputLayerHeaderRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueInputLayerHeaders(" + Company + "," + GroupSeq + "," + HeadNum + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcValueInputLayerHeaders_Company_GroupSeq_HeadNum_ConfigID_InputName_ImageLayerID(Company, GroupSeq, HeadNum, ConfigID, InputName, ImageLayerID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcValueInputLayerHeader item
   Description: Call UpdateExt to delete PcValueInputLayerHeader item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcValueInputLayerHeader
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupSeq: Desc: GroupSeq   Required: True
      :param HeadNum: Desc: HeadNum   Required: True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/PcValueInputLayerHeaders(" + Company + "," + GroupSeq + "," + HeadNum + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QBuildMappings(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QBuildMappings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QBuildMappings
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QBuildMappingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/QBuildMappings",headers=creds) as resp:
           return await resp.json()

async def post_QBuildMappings(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QBuildMappings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QBuildMappingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QBuildMappingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/QBuildMappings", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QBuildMappings_Company_ConfigID_InputName_ObjName_ObjParameter(Company, ConfigID, InputName, ObjName, ObjParameter, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QBuildMapping item
   Description: Calls GetByID to retrieve the QBuildMapping item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QBuildMapping
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ObjName: Desc: ObjName   Required: True   Allow empty value : True
      :param ObjParameter: Desc: ObjParameter   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QBuildMappingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/QBuildMappings(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + "," + ObjParameter + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QBuildMappings_Company_ConfigID_InputName_ObjName_ObjParameter(Company, ConfigID, InputName, ObjName, ObjParameter, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QBuildMapping for the service
   Description: Calls UpdateExt to update QBuildMapping. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QBuildMapping
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ObjName: Desc: ObjName   Required: True   Allow empty value : True
      :param ObjParameter: Desc: ObjParameter   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QBuildMappingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/QBuildMappings(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + "," + ObjParameter + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QBuildMappings_Company_ConfigID_InputName_ObjName_ObjParameter(Company, ConfigID, InputName, ObjName, ObjParameter, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QBuildMapping item
   Description: Call UpdateExt to delete QBuildMapping item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QBuildMapping
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ObjName: Desc: ObjName   Required: True   Allow empty value : True
      :param ObjParameter: Desc: ObjParameter   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/QBuildMappings(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + "," + ObjParameter + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcValueGrpListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePcValueGrp, whereClausePcValueHead, whereClausePcConfigurationParams, whereClausePcConfiguredDrawings, whereClausePcContextProperties, whereClausePcInputsLayerDetail, whereClausePcInputsLayerHeader, whereClausePcInputsPublishToDocParams, whereClausePcInputVar, whereClausePcValueInputLayerDetail, whereClausePcValueInputLayerHeader, whereClauseQBuildMapping, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePcValueGrp=" + whereClausePcValueGrp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcValueHead=" + whereClausePcValueHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcConfigurationParams=" + whereClausePcConfigurationParams
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcConfiguredDrawings=" + whereClausePcConfiguredDrawings
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcContextProperties=" + whereClausePcContextProperties
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcInputsLayerDetail=" + whereClausePcInputsLayerDetail
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcInputsLayerHeader=" + whereClausePcInputsLayerHeader
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcInputsPublishToDocParams=" + whereClausePcInputsPublishToDocParams
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcInputVar=" + whereClausePcInputVar
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcValueInputLayerDetail=" + whereClausePcValueInputLayerDetail
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcValueInputLayerHeader=" + whereClausePcValueInputLayerHeader
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQBuildMapping=" + whereClauseQBuildMapping
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupSeq, epicorHeaders = None):
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
   params += "groupSeq=" + groupSeq

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetGeneratedClient(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGeneratedClient
   Description: Returns the generated source code to compile the client code of a configuration
   OperationID: GetGeneratedClient
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGeneratedClient_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGeneratedClient_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreStartConfiguration(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreStartConfiguration
   Description: Perform any logic that needs to be executed before starting a configuration
   OperationID: PreStartConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreStartConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreStartConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StartPcValueConfiguration(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StartPcValueConfiguration
   Description: Starts a configuration given a configuration sequence (PcStruct) record and the source and target information.
For Keep When process:
* If PcValueHead does not exists State will be Added
   OperationID: StartPcValueConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartPcValueConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartPcValueConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StartConfiguration(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StartConfiguration
   Description: Starts a configuration given a configuration sequence (PcStruct) record and the source and target information.
For Keep When process:
* If PcValueHead does not exists State will be Added
   OperationID: StartConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SavePcValueConfiguration(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SavePcValueConfiguration
   Description: Saves a single level configuration.
   OperationID: SavePcValueConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SavePcValueConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SavePcValueConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SavePcValueConfigurationMulti(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SavePcValueConfigurationMulti
   Description: Saves a multi level configuration from kinetic.
   OperationID: SavePcValueConfigurationMulti
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SavePcValueConfigurationMulti_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SavePcValueConfigurationMulti_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SaveConfiguration(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SaveConfiguration
   Description: Saves a single level configuration.
   OperationID: SaveConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SaveMultiConfiguration(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SaveMultiConfiguration
   Description: Saves a multi-level configuration.
For Keep When process:
* For all configurators that KeepIt are false will not be saved
* Identify all configurators KeepIt are false to delete PcValueHead and PcValueSet
   OperationID: SaveMultiConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveMultiConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveMultiConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteAssembliesInTestMode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteAssembliesInTestMode
   Description: Method is executed when the customer X-es out of the configurator instead of pressing save and they are in test mode
   OperationID: DeleteAssembliesInTestMode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteAssembliesInTestMode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteAssembliesInTestMode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessNoInputsConfigurator(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessNoInputsConfigurator
   Description: Process the no inputs configurator for Kinetic screens.
The method uses the parameters to build the Tablesets needed to invoke the ProcessNICDocumentRules.
   OperationID: ProcessNoInputsConfigurator
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessNoInputsConfigurator_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessNoInputsConfigurator_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessNICDocumentRules(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessNICDocumentRules
   Description: Process NIC  document rules
   OperationID: ProcessNICDocumentRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessNICDocumentRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessNICDocumentRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessDocumentRules(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessDocumentRules
   Description: Process document rules
   OperationID: ProcessDocumentRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessDocumentRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessDocumentRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessKeepWhen(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessKeepWhen
   Description: Objective: Run methods rules to determine if assemblies should be keep it or not to hide or show the corresponding configuration.
This process will be executed when:
* When is clicked next page and changes to next configurator
* Is multiconfigurator
* If current part revision has rules set(OPR or ASM)
   OperationID: ProcessKeepWhen
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessKeepWhen_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessKeepWhen_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteSubConfiguration(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteSubConfiguration
   Description: DeleteSubConfiguration
   OperationID: DeleteSubConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteSubConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteSubConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckServerSyntax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckServerSyntax
   Description: Provides ability to check server side syntax
   OperationID: CheckServerSyntax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckServerSyntax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckServerSyntax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TestNICRules(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TestNICRules
   Description: Call this method when you want to test the rules of a No Inputs Configurator
   OperationID: TestNICRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestNICRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestNICRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EWCTestRules(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EWCTestRules
   Description: Call this method to retrieve the Test Rules results dataset that is temporarily stored in the FileStore for EWC configurators.
   OperationID: EWCTestRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EWCTestRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EWCTestRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EDIDemandConfiguration(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EDIDemandConfiguration
   Description: Receives configuration values on a smart string and processes it completely.
   OperationID: EDIDemandConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EDIDemandConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EDIDemandConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EDIValidateSmartString(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EDIValidateSmartString
   Description: Validate the smart string against inputs
   OperationID: EDIValidateSmartString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EDIValidateSmartString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EDIValidateSmartString_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PartExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PartExists
   Description: Part exists.
   OperationID: PartExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PartRevExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PartRevExists
   Description: Determines if the part rev exists
   OperationID: PartRevExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartRevExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartRevExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTargetEntityValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTargetEntityValues
   Description: Get AllowRecordCreation and IncomingSmartString columns to process before the configuration is saved for the first time.
These values were obtained but only after the configuration was saved for the first time.
   OperationID: GetTargetEntityValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTargetEntityValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTargetEntityValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SuggestSmartString(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SuggestSmartString
   Description: Original logic to suggest a smart string.  This is called from Win client and EWA.  It cannot be called from EWC.
   OperationID: SuggestSmartString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SuggestSmartString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SuggestSmartString_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EWCSuggestSmartString(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EWCSuggestSmartString
   Description: Call this method when you need to suggest a smart string value and you are not calling from EWA or your ConfigType is EWC.
   OperationID: EWCSuggestSmartString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EWCSuggestSmartString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EWCSuggestSmartString_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddUserDenfinedParameterString(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddUserDenfinedParameterString
   Description: Purpose: Adds a row and populates the string value in the User Defined Table used to pass parameters
from the client to the server for Server Side UDMethods.
<param name="methodName">The name of the server side UDmethod the parameter is being added for.</param><param name="parameterName">The name of the Parameter being added.</param><param name="configID">The ID of the configurator the UDmethod is tied to.</param><param name="paramSeq">The position the parameter is in the signature of the UDMethod.</param><param name="newValue">This holds the string value being passed for string parameters.</param><param name="pcValueDS">The name of the server side UDmethod parameter is being added for.</param>
   OperationID: AddUserDenfinedParameterString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddUserDenfinedParameterString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddUserDenfinedParameterString_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddUserDenfinedParameterInt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddUserDenfinedParameterInt
   Description: Purpose: Adds a row and populates the int value in the User Defined Table used to pass parameters
from the client to the server for Server Side UDMethods.
<param name="methodName">The name of the server side UDmethod the parameter is being added for.</param><param name="parameterName">The name of the Parameter being added.</param><param name="configID">The ID of the configurator the UDmethod is tied to.</param><param name="paramSeq">The position the parameter is in the signature of the UDMethod.</param><param name="newValue">This holds the int value being passed for string parameters.</param><param name="pcValueDS">The name of the server side UDmethod parameter is being added for.</param>
   OperationID: AddUserDenfinedParameterInt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddUserDenfinedParameterInt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddUserDenfinedParameterInt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddUserDenfinedParameterDecimal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddUserDenfinedParameterDecimal
   Description: Purpose: Adds a row and populates the decimal value in the User Defined Table used to pass parameters
from the client to the server for Server Side UDMethods.
<param name="methodName">The name of the server side UDmethod the parameter is being added for.</param><param name="parameterName">The name of the Parameter being added.</param><param name="configID">The ID of the configurator the UDmethod is tied to.</param><param name="paramSeq">The position the parameter is in the signature of the UDMethod.</param><param name="newValue">This holds the decimal value being passed for string parameters.</param><param name="pcValueDS">The name of the server side UDmethod parameter is being added for.</param>
   OperationID: AddUserDenfinedParameterDecimal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddUserDenfinedParameterDecimal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddUserDenfinedParameterDecimal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddUserDenfinedParameterDateTime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddUserDenfinedParameterDateTime
   Description: Purpose: Adds a row and populates the DateTime value in the User Defined Table used to pass parameters
from the client to the server for Server Side UDMethods.
<param name="methodName">The name of the server side UDmethod the parameter is being added for.</param><param name="parameterName">The name of the Parameter being added.</param><param name="configID">The ID of the configurator the UDmethod is tied to.</param><param name="paramSeq">The position the parameter is in the signature of the UDMethod.</param><param name="newValue">This holds the DateTime value being passed for string parameters.</param><param name="pcValueDS">The name of the server side UDmethod parameter is being added for.</param>
   OperationID: AddUserDenfinedParameterDateTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddUserDenfinedParameterDateTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddUserDenfinedParameterDateTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddUserDenfinedParameterBool(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddUserDenfinedParameterBool
   Description: Purpose: Adds a row and populates the bool value in the User Defined Table used to pass parameters
from the client to the server for Server Side UDMethods.
<param name="methodName">The name of the server side UDmethod the parameter is being added for.</param><param name="parameterName">The name of the Parameter being added.</param><param name="configID">The ID of the configurator the UDmethod is tied to.</param><param name="paramSeq">The position the parameter is in the signature of the UDMethod.</param><param name="newValue">This holds the bool value being passed for string parameters.</param><param name="pcValueDS">The name of the server side UDmethod parameter is being added for.</param>
   OperationID: AddUserDenfinedParameterBool
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddUserDenfinedParameterBool_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddUserDenfinedParameterBool_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearUDMethodParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClearUDMethodParams
   Description: Purpose: Clears the Rows in PcUserDefinedMethodParameters.  Rows should be cleared before and after calling
a server side UDMethod.
   OperationID: ClearUDMethodParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearUDMethodParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearUDMethodParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExecuteGenerateImageLayerScriptCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExecuteGenerateImageLayerScriptCode
   Description: Used to generate Image Layer script code for the given Image Layer ID
   OperationID: ExecuteGenerateImageLayerScriptCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExecuteGenerateImageLayerScriptCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExecuteGenerateImageLayerScriptCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExecuteGenerateSingleImageLayerScriptCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExecuteGenerateSingleImageLayerScriptCode
   Description: Used to generate Image Layer script code for the given Image Layer ID
   OperationID: ExecuteGenerateSingleImageLayerScriptCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExecuteGenerateSingleImageLayerScriptCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExecuteGenerateSingleImageLayerScriptCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExecuteGenerateFullImageLayerScriptCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExecuteGenerateFullImageLayerScriptCode
   OperationID: ExecuteGenerateFullImageLayerScriptCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExecuteGenerateFullImageLayerScriptCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExecuteGenerateFullImageLayerScriptCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExecuteUserDefinedWithArrayReturn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExecuteUserDefinedWithArrayReturn
   Description: Need to execute this method to execute server-side UDmethods that will return an array of objects.
   OperationID: ExecuteUserDefinedWithArrayReturn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExecuteUserDefinedWithArrayReturn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExecuteUserDefinedWithArrayReturn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExecuteUserDefined(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExecuteUserDefined
   Description: Need to execute this method to execute server side UDmethods from the client out other API.
<param name="methodName">The name of the server-side UDmethod to execute.</param><param name="configID">The ID of the configurator the UDmethod is tied to.</param><param name="testID">When executing under a test (Test Inputs/Rules) this parameter should contain a valid System.Guid, otherwise it can be System.Guid.Empty</param><param name="pcValueDS">Values from  current configurator.</param>
   OperationID: ExecuteUserDefined
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExecuteUserDefined_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExecuteUserDefined_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExecuteDataLookup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExecuteDataLookup
   Description: Purpose: Executes DataLookup functiosn from the client side.
   OperationID: ExecuteDataLookup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExecuteDataLookup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExecuteDataLookup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExecutePageOnLoadEvents(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExecutePageOnLoadEvents
   Description: Purpose: Call from the client to execute Page OnLoad events.
<param name="pageLoadEvent">The name of the page load event wanting to execute.</param><param name="configID">The ID of the configurator the UDmethod is tied to.</param><param name="testID"></param><param name="pcValueDS"></param>
   OperationID: ExecutePageOnLoadEvents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExecutePageOnLoadEvents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExecutePageOnLoadEvents_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPictureBoxImage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPictureBoxImage
   Description: GetPictureBoxImage
   OperationID: GetPictureBoxImage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPictureBoxImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPictureBoxImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAllImages(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAllImages
   Description: Retrieve all picture box images and 2D Viewer drawings in one trip to the server and send the data back in a tableset
   OperationID: GetAllImages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllImages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllImages_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAllPictureBoxImages(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAllPictureBoxImages
   Description: Retrieves the images for a page in a configurator
   OperationID: GetAllPictureBoxImages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllPictureBoxImages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllPictureBoxImages_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcConfigParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcConfigParams
   Description: GetNewPcConfigParams
   OperationID: GetNewPcConfigParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcConfigParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcConfigParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcInputsPublishToDoc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcInputsPublishToDoc
   Description: GetNewPcInputsPublishToDoc
   OperationID: GetNewPcInputsPublishToDoc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputsPublishToDoc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputsPublishToDoc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DataColumnLookupList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DataColumnLookupList
   Description: DataColumnLookupList
   OperationID: DataColumnLookupList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DataColumnLookupList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DataColumnLookupList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DataColumnList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DataColumnList
   Description: DataColumnList
   OperationID: DataColumnList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DataColumnList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DataColumnList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DataColumnListNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DataColumnListNum
   Description: DataColumnListNum
   OperationID: DataColumnListNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DataColumnListNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DataColumnListNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DataColumnRange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DataColumnRange
   Description: DataColumnRange
   OperationID: DataColumnRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DataColumnRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DataColumnRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DataRowList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DataRowList
   Description: DataRowList
   OperationID: DataRowList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DataRowList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DataRowList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DataRowListNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DataRowListNum
   Description: DataRowListNum
   OperationID: DataRowListNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DataRowListNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DataRowListNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DataRowRange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DataRowRange
   Description: DataRowRange
   OperationID: DataRowRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DataRowRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DataRowRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DataRowLookup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DataRowLookup
   Description: DataRowLookup
   OperationID: DataRowLookup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DataRowLookup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DataRowLookup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DataLookup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DataLookup
   Description: DataLookup
   OperationID: DataLookup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DataLookup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DataLookup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EWCInitializeRuntime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EWCInitializeRuntime
   Description: Method to initialize the EWC runtime site files for the specific config ID.
   OperationID: EWCInitializeRuntime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EWCInitializeRuntime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EWCInitializeRuntime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EWCReadAllBytesIfNewer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EWCReadAllBytesIfNewer
   Description: Return the EWC Runtime files from the FileStore ConfigID.zip for the current Tenant and Company.
   OperationID: EWCReadAllBytesIfNewer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EWCReadAllBytesIfNewer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EWCReadAllBytesIfNewer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTenantID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTenantID
   Description: Return the Tenant ID from the current Company.
   OperationID: GetTenantID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTenantID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTenantID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EWCWriteOrCreateAllBytes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EWCWriteOrCreateAllBytes
   Description: Write or create the byte array to the FileStore for the current company, tenant.
   OperationID: EWCWriteOrCreateAllBytes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EWCWriteOrCreateAllBytes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EWCWriteOrCreateAllBytes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPCTransportTableset(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPCTransportTableset
   Description: Returns the configuration specific data in the transport table for use in Question and Answer sessions not controlled by the
E10 client side run time engine.  This must be called once for every configurator involved in a configuration session.
   OperationID: GetPCTransportTableset
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPCTransportTableset_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPCTransportTableset_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SavePCTransportConfiguration(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SavePCTransportConfiguration
   Description: Method to save a configuration session to be used by Epicor Web
   OperationID: SavePCTransportConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SavePCTransportConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SavePCTransportConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteTestInputsFileStoreEntry(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteTestInputsFileStoreEntry
   Description: Remove the temporary file storeS entry for Test Inputs
   OperationID: DeleteTestInputsFileStoreEntry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteTestInputsFileStoreEntry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteTestInputsFileStoreEntry_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrepareEWCRequirements(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrepareEWCRequirements
   Description: This method retrieves the token and for enterprise configurators when in the sales company verifies the configurator has been deployed to EWC in that company and if not
executes the deploy logic so the end user is able to configure.
   OperationID: PrepareEWCRequirements
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrepareEWCRequirements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrepareEWCRequirements_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetECCConfigurator(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetECCConfigurator
   Description: Get ECC Part configurator initial data and process to return configuration setup to display Kinetic Configurator
   OperationID: GetECCConfigurator
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetECCConfigurator_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetECCConfigurator_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcValueGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcValueGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcValueGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcValueGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcValueGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcValueHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcValueHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcValueHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcValueHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcValueHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcInputsLayerDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcInputsLayerDetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcInputsLayerDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputsLayerDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputsLayerDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcInputsLayerHeader(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcInputsLayerHeader
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcInputsLayerHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputsLayerHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputsLayerHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcInputVar(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcInputVar
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcInputVar
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputVar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputVar_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcValueInputLayerDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcValueInputLayerDetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcValueInputLayerDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcValueInputLayerDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcValueInputLayerDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcValueInputLayerHeader(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcValueInputLayerHeader
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcValueInputLayerHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcValueInputLayerHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcValueInputLayerHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQBuildMapping(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQBuildMapping
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQBuildMapping
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQBuildMapping_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQBuildMapping_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationRuntimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcConfigurationParamsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcConfigurationParamsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcConfiguredDrawingsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcConfiguredDrawingsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcContextPropertiesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcContextPropertiesRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputVarRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcInputVarRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsLayerDetailRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcInputsLayerDetailRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsLayerHeaderRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcInputsLayerHeaderRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsPublishToDocParamsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcInputsPublishToDocParamsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcValueGrpListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcValueGrpListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcValueGrpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcValueGrpRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcValueHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcValueHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcValueInputLayerDetailRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcValueInputLayerDetailRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcValueInputLayerHeaderRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcValueInputLayerHeaderRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QBuildMappingRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QBuildMappingRow] = obj["value"]
      pass

class Erp_Tablesets_PcConfigurationParamsRow:
   def __init__(self, obj):
      self.ForeignTableName:str = obj["ForeignTableName"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.TgtStructTag:str = obj["TgtStructTag"]
      self.StructID:int = obj["StructID"]
      self.InSmartString:str = obj["InSmartString"]
      self.IsTestPlan:bool = obj["IsTestPlan"]
      self.SpecID:str = obj["SpecID"]
      self.SpecRevNum:str = obj["SpecRevNum"]
      self.InspType:str = obj["InspType"]
      self.RunningStateOverride:str = obj["RunningStateOverride"]
      self.EqmPassed:str = obj["EqmPassed"]
      self.EqmFailDesc:str = obj["EqmFailDesc"]
      self.EqmOverride:bool = obj["EqmOverride"]
      self.RelatedToTable:str = obj["RelatedToTable"]
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      self.SourceTable:str = obj["SourceTable"]
      self.TestID:str = obj["TestID"]
      self.TestMode:str = obj["TestMode"]
      self.AppServerID:str = obj["AppServerID"]
      self.PcStatusSysRowID:str = obj["PcStatusSysRowID"]
      self.ConfigVersion:int = obj["ConfigVersion"]
      self.UniqueID:str = obj["UniqueID"]
      self.ConfigID:str = obj["ConfigID"]
      self.Company:str = obj["Company"]
      self.InputPricingSet:bool = obj["InputPricingSet"]
      self.OrderPrice:int = obj["OrderPrice"]
      self.QuotePrice:int = obj["QuotePrice"]
      self.DemandPrice:int = obj["DemandPrice"]
      self.PurchasePrice:int = obj["PurchasePrice"]
      self.WebOrderBasketPrice:int = obj["WebOrderBasketPrice"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.AltMethod:str = obj["AltMethod"]
      self.InitialStructTag:str = obj["InitialStructTag"]
      self.InitialRuleTag:str = obj["InitialRuleTag"]
      self.TrackerMode:bool = obj["TrackerMode"]
      """  Determines if a configuration was opened from a tracker.  """  
      self.ConfigType:str = obj["ConfigType"]
      self.EWCConfiguratorURL:str = obj["EWCConfiguratorURL"]
      """  This is the web address to call when launching an Epicor Web configurtor.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcConfiguredDrawingsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ConfigID:str = obj["ConfigID"]
      self.GroupSeq:int = obj["GroupSeq"]
      self.HeadNum:int = obj["HeadNum"]
      self.InputName:str = obj["InputName"]
      self.ImageID:str = obj["ImageID"]
      self.Content:str = obj["Content"]
      self.PageSeq:int = obj["PageSeq"]
      self.QBuildObjExist:bool = obj["QBuildObjExist"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcContextPropertiesRow:
   def __init__(self, obj):
      self.AttributeID:str = obj["AttributeID"]
      self.CompanyID:str = obj["CompanyID"]
      self.ConfigurationID:str = obj["ConfigurationID"]
      self.Currency:str = obj["Currency"]
      self.CustomerID:str = obj["CustomerID"]
      self.DemandHeadNumber:int = obj["DemandHeadNumber"]
      self.DemandLineNumber:int = obj["DemandLineNumber"]
      self.Entity:str = obj["Entity"]
      self.JobNumber:str = obj["JobNumber"]
      self.OrderDetailNumber:int = obj["OrderDetailNumber"]
      self.OrderNumber:int = obj["OrderNumber"]
      self.PackSlip:str = obj["PackSlip"]
      self.PartNumber:str = obj["PartNumber"]
      self.PartRevisionNumber:str = obj["PartRevisionNumber"]
      self.PODetailNumber:int = obj["PODetailNumber"]
      self.PONumber:int = obj["PONumber"]
      self.QuoteLineNumber:int = obj["QuoteLineNumber"]
      self.QuoteNumber:int = obj["QuoteNumber"]
      self.SpecificationID:str = obj["SpecificationID"]
      self.SpecificationRevision:str = obj["SpecificationRevision"]
      self.SupplierID:str = obj["SupplierID"]
      self.UserID:str = obj["UserID"]
      self.NonConfID:str = obj["NonConfID"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.RMALine:int = obj["RMALine"]
      self.PackLine:int = obj["PackLine"]
      self.SiteID:str = obj["SiteID"]
      self.ECCQuoteNum:str = obj["ECCQuoteNum"]
      self.CustomerNumber:int = obj["CustomerNumber"]
      self.SupplierNumber:int = obj["SupplierNumber"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputVarRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.VarName:str = obj["VarName"]
      """  VarName  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.InitValue:str = obj["InitValue"]
      """  InitValue  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.InitString:str = obj["InitString"]
      self.InitDecimal:int = obj["InitDecimal"]
      self.InitLogical:bool = obj["InitLogical"]
      self.InitDate:str = obj["InitDate"]
      self.InUse:bool = obj["InUse"]
      """  Determines if the variable is being used by an input.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsLayerDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.InputName:str = obj["InputName"]
      """  InputName  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  ImageLayerID  """  
      self.LayerSeq:int = obj["LayerSeq"]
      """  LayerSeq  """  
      self.LayerName:str = obj["LayerName"]
      """  LayerName  """  
      self.LayerDesc:str = obj["LayerDesc"]
      """  LayerDesc  """  
      self.ZIndex:int = obj["ZIndex"]
      """  Order in which layers are placed on the base image.  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.FileType:str = obj["FileType"]
      """  Png type is supported.  """  
      self.Category:str = obj["Category"]
      """  Free form text enabling users to categorize layers  """  
      self.Width:int = obj["Width"]
      """  Width of image  """  
      self.Height:int = obj["Height"]
      """  Height of image  """  
      self.xPos:int = obj["xPos"]
      """  Reserved for Future Development  """  
      self.yPos:int = obj["yPos"]
      """  Reserved for Future Development  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsLayerHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.InputName:str = obj["InputName"]
      """  Input name this header is assigned.  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  Image Layer ID.  """  
      self.ImageID:str = obj["ImageID"]
      """  File name of the image to be retrieved from the Image URL.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ImageURL:str = obj["ImageURL"]
      """  The URL location of the image.  """  
      self.FileType:str = obj["FileType"]
      """  File types png and jpg are supported.  """  
      self.Width:int = obj["Width"]
      """  Image Width  """  
      self.Height:int = obj["Height"]
      """  Image height  """  
      self.Version:int = obj["Version"]
      """  Internal next number indicating the current version. Thi is is used by Verfiy Configuration to identify when a warning message is to be written to the log.  """  
      self.xPos:int = obj["xPos"]
      """  Reserved for future development  """  
      self.yPos:int = obj["yPos"]
      """  Reserved for future development  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsPublishToDocParamsRow:
   def __init__(self, obj):
      self.Key:str = obj["Key"]
      self.Value:str = obj["Value"]
      self.Company:str = obj["Company"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcValueGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  RelatedToTableName  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  RelatedToSysRowID  """  
      self.CreateDate:str = obj["CreateDate"]
      """  CreateDate  """  
      self.CreateUserID:str = obj["CreateUserID"]
      """  CreateUserID  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  LastUpdated  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  LastUpdatedBy  """  
      self.ConfigStatus:str = obj["ConfigStatus"]
      """  ConfigStatus  """  
      self.SIValues:bool = obj["SIValues"]
      """  SIValues  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcValueGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  RelatedToTableName  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  RelatedToSysRowID  """  
      self.CreateDate:str = obj["CreateDate"]
      """  CreateDate  """  
      self.CreateUserID:str = obj["CreateUserID"]
      """  CreateUserID  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  LastUpdated  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  LastUpdatedBy  """  
      self.ConfigStatus:str = obj["ConfigStatus"]
      """  ConfigStatus  """  
      self.SIValues:bool = obj["SIValues"]
      """  SIValues  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DisplaySummary:bool = obj["DisplaySummary"]
      self.IncomingSmartString:bool = obj["IncomingSmartString"]
      self.TestID:str = obj["TestID"]
      """  Indicates if this value group was created because of a test (test inputs or test rules).  """  
      self.TestMode:str = obj["TestMode"]
      """  Indicates the test mode of this value group, note that TestID should be populated with a non empty Guid to make sure that all programs are generated as a test. Then this column will indicate if rules or anything else should be tested too.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcValueHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum  """  
      self.StructTag:str = obj["StructTag"]
      """  StructTag  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.RevolvingSeq:int = obj["RevolvingSeq"]
      """  RevolvingSeq  """  
      self.ForeignTableName:str = obj["ForeignTableName"]
      """  ForeignTableName  """  
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      """  ForeignSysRowID  """  
      self.SourceTableName:str = obj["SourceTableName"]
      """  SourceTableName  """  
      self.SourceSysRowID:str = obj["SourceSysRowID"]
      """  SourceSysRowID  """  
      self.ConfigType:str = obj["ConfigType"]
      """  ConfigType  """  
      self.ConfigVersion:int = obj["ConfigVersion"]
      """  ConfigVersion  """  
      self.DisplayTag:str = obj["DisplayTag"]
      """  DisplayTag  """  
      self.RuleTag:str = obj["RuleTag"]
      """  RuleTag  """  
      self.ExtConfig:bool = obj["ExtConfig"]
      """  ExtConfig  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  ExtCompany  """  
      self.AllowRecordCreation:bool = obj["AllowRecordCreation"]
      """  AllowRecordCreation  """  
      self.AllowPricing:bool = obj["AllowPricing"]
      """  AllowPricing  """  
      self.PromptForConfig:bool = obj["PromptForConfig"]
      """  PromptForConfig  """  
      self.InSmartString:bool = obj["InSmartString"]
      """  InSmartString  """  
      self.DisplaySummary:bool = obj["DisplaySummary"]
      """  DisplaySummary  """  
      self.AllowReconfig:bool = obj["AllowReconfig"]
      """  AllowReconfig  """  
      self.IsMainForeign:bool = obj["IsMainForeign"]
      """  IsMainForeign  """  
      self.NewPartNum:str = obj["NewPartNum"]
      """  NewPartNum  """  
      self.NewSmartString:str = obj["NewSmartString"]
      """  NewSmartString  """  
      self.SIValues:bool = obj["SIValues"]
      """  SIValues  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SIValuesGroupSeq:int = obj["SIValuesGroupSeq"]
      self.TestID:str = obj["TestID"]
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  Copied from the parent PcValueGrp record  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  Value is brought from the parent PcValueGroup record.  """  
      self.SIValuesHeadNum:int = obj["SIValuesHeadNum"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcValueInputLayerDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.InputName:str = obj["InputName"]
      """  Input Name  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  Image Layer ID  """  
      self.LayerSeq:int = obj["LayerSeq"]
      """  Programmatically calculated value used to keep the rows unique.  """  
      self.LayerName:str = obj["LayerName"]
      """  LayerName  """  
      self.LayerDesc:str = obj["LayerDesc"]
      """  LayerDesc  """  
      self.ZIndex:int = obj["ZIndex"]
      """  ZIndex  """  
      self.ImageID:str = obj["ImageID"]
      """  Image ID  """  
      self.FileType:str = obj["FileType"]
      """  Png file types are supported  """  
      self.Width:int = obj["Width"]
      """  Width  """  
      self.Height:int = obj["Height"]
      """  Height  """  
      self.Category:str = obj["Category"]
      """  Free form text  """  
      self.xPos:int = obj["xPos"]
      """  Reserved for future development  """  
      self.yPos:int = obj["yPos"]
      """  Reserved for future development  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcValueInputLayerHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.InputName:str = obj["InputName"]
      """  Input Name  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  Image Layer ID  """  
      self.ImageID:str = obj["ImageID"]
      """  Image ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ImageURL:str = obj["ImageURL"]
      """  Location of Image  """  
      self.FileType:str = obj["FileType"]
      """  FileType  """  
      self.Width:int = obj["Width"]
      """  Width  """  
      self.Height:int = obj["Height"]
      """  Height  """  
      self.Version:int = obj["Version"]
      """  Used by Verify Configuration to identify changes in the layer definition.  """  
      self.xPos:int = obj["xPos"]
      """  Reserved for future development  """  
      self.yPos:int = obj["yPos"]
      """  Reserved for future development  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QBuildMappingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.InputName:str = obj["InputName"]
      """  Input Name  """  
      self.ObjName:str = obj["ObjName"]
      """  This is the object name.  """  
      self.ObjParameter:str = obj["ObjParameter"]
      """  This is the name of the object parameter.  """  
      self.MappedInputName:str = obj["MappedInputName"]
      """  Name of the input mapped to this object parameter.  """  
      self.ObjParameterDataType:str = obj["ObjParameterDataType"]
      """  This is the data type of the object parameter.  """  
      self.ObjParameterInitValue:str = obj["ObjParameterInitValue"]
      """  This is the initial value of the object parameter as it was defined in the designer.  This is reserved for future development.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DataType:str = obj["DataType"]
      self.PageSeq:int = obj["PageSeq"]
      self.BitFlag:int = obj["BitFlag"]
      self.QBuildObjObjType:str = obj["QBuildObjObjType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddUserDenfinedParameterBool_input:
   """ Required : 
   methodName
   parameterName
   configID
   paramSeq
   newValue
   pcValueDS
   """  
   def __init__(self, obj):
      self.methodName:str = obj["methodName"]
      self.parameterName:str = obj["parameterName"]
      self.configID:str = obj["configID"]
      self.paramSeq:int = obj["paramSeq"]
      self.newValue:bool = obj["newValue"]
      self.pcValueDS:list[Erp_Tablesets_PcValueTableset] = obj["pcValueDS"]
      pass

class AddUserDenfinedParameterBool_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcValueDS:list[Erp_Tablesets_PcValueTableset] = obj["pcValueDS"]
      pass

      """  output parameters  """  

class AddUserDenfinedParameterDateTime_input:
   """ Required : 
   methodName
   parameterName
   configID
   paramSeq
   newValue
   pcValueDS
   """  
   def __init__(self, obj):
      self.methodName:str = obj["methodName"]
      self.parameterName:str = obj["parameterName"]
      self.configID:str = obj["configID"]
      self.paramSeq:int = obj["paramSeq"]
      self.newValue:str = obj["newValue"]
      self.pcValueDS:list[Erp_Tablesets_PcValueTableset] = obj["pcValueDS"]
      pass

class AddUserDenfinedParameterDateTime_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcValueDS:list[Erp_Tablesets_PcValueTableset] = obj["pcValueDS"]
      pass

      """  output parameters  """  

class AddUserDenfinedParameterDecimal_input:
   """ Required : 
   methodName
   parameterName
   configID
   paramSeq
   newValue
   pcValueDS
   """  
   def __init__(self, obj):
      self.methodName:str = obj["methodName"]
      self.parameterName:str = obj["parameterName"]
      self.configID:str = obj["configID"]
      self.paramSeq:int = obj["paramSeq"]
      self.newValue:int = obj["newValue"]
      self.pcValueDS:list[Erp_Tablesets_PcValueTableset] = obj["pcValueDS"]
      pass

class AddUserDenfinedParameterDecimal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcValueDS:list[Erp_Tablesets_PcValueTableset] = obj["pcValueDS"]
      pass

      """  output parameters  """  

class AddUserDenfinedParameterInt_input:
   """ Required : 
   methodName
   parameterName
   configID
   paramSeq
   newValue
   pcValueDS
   """  
   def __init__(self, obj):
      self.methodName:str = obj["methodName"]
      self.parameterName:str = obj["parameterName"]
      self.configID:str = obj["configID"]
      self.paramSeq:int = obj["paramSeq"]
      self.newValue:int = obj["newValue"]
      self.pcValueDS:list[Erp_Tablesets_PcValueTableset] = obj["pcValueDS"]
      pass

class AddUserDenfinedParameterInt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcValueDS:list[Erp_Tablesets_PcValueTableset] = obj["pcValueDS"]
      pass

      """  output parameters  """  

class AddUserDenfinedParameterString_input:
   """ Required : 
   methodName
   parameterName
   configID
   paramSeq
   newValue
   pcValueDS
   """  
   def __init__(self, obj):
      self.methodName:str = obj["methodName"]
      self.parameterName:str = obj["parameterName"]
      self.configID:str = obj["configID"]
      self.paramSeq:int = obj["paramSeq"]
      self.newValue:str = obj["newValue"]
      self.pcValueDS:list[Erp_Tablesets_PcValueTableset] = obj["pcValueDS"]
      pass

class AddUserDenfinedParameterString_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcValueDS:list[Erp_Tablesets_PcValueTableset] = obj["pcValueDS"]
      pass

      """  output parameters  """  

class CheckServerSyntax_input:
   """ Required : 
   configID
   docRuleCheckSyntaxArgs
   serverEventCheckSyntaxArgs
   methodRuleCheckSyntaxArgs
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      self.docRuleCheckSyntaxArgs:list[Erp_Shared_Lib_Configurator_DocRuleCheckSyntaxArgs] = obj["docRuleCheckSyntaxArgs"]
      self.serverEventCheckSyntaxArgs:list[Erp_Shared_Lib_Configurator_ServerEventCheckSyntaxArgs] = obj["serverEventCheckSyntaxArgs"]
      self.methodRuleCheckSyntaxArgs:list[Erp_Shared_Lib_Configurator_MethodRuleCheckSyntaxArgs] = obj["methodRuleCheckSyntaxArgs"]
      pass

class CheckServerSyntax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.syntaxErrors:str = obj["parameters"]
      pass

      """  output parameters  """  

class ClearUDMethodParams_input:
   """ Required : 
   pcValueDS
   """  
   def __init__(self, obj):
      self.pcValueDS:list[Erp_Tablesets_PcValueTableset] = obj["pcValueDS"]
      pass

class ClearUDMethodParams_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcValueDS:list[Erp_Tablesets_PcValueTableset] = obj["pcValueDS"]
      pass

      """  output parameters  """  

class DataColumnListNum_input:
   """ Required : 
   configId
   testId
   lookupTableID
   colName
   """  
   def __init__(self, obj):
      self.configId:str = obj["configId"]
      """  The configuration ID  """  
      self.testId:str = obj["testId"]
      """  The test ID  """  
      self.lookupTableID:str = obj["lookupTableID"]
      """  The lookup table name  """  
      self.colName:str = obj["colName"]
      """  The column name  """  
      pass

class DataColumnListNum_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class DataColumnList_input:
   """ Required : 
   configId
   testId
   lookupTableID
   colName
   """  
   def __init__(self, obj):
      self.configId:str = obj["configId"]
      """  The configuration ID  """  
      self.testId:str = obj["testId"]
      """  The test ID  """  
      self.lookupTableID:str = obj["lookupTableID"]
      """  The lookup table name  """  
      self.colName:str = obj["colName"]
      """  The column name  """  
      pass

class DataColumnList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class DataColumnLookupList_input:
   """ Required : 
   configId
   testId
   lookupTblID
   colName
   searchValue
   """  
   def __init__(self, obj):
      self.configId:str = obj["configId"]
      """  The configuration ID  """  
      self.testId:str = obj["testId"]
      """  The test ID  """  
      self.lookupTblID:str = obj["lookupTblID"]
      """  The lookup table name  """  
      self.colName:str = obj["colName"]
      """  The column name  """  
      self.searchValue:str = obj["searchValue"]
      pass

class DataColumnLookupList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class DataColumnRange_input:
   """ Required : 
   configId
   testId
   lookupTableID
   colName
   startRow
   endRow
   """  
   def __init__(self, obj):
      self.configId:str = obj["configId"]
      """  The configuration ID  """  
      self.testId:str = obj["testId"]
      """  The test ID  """  
      self.lookupTableID:str = obj["lookupTableID"]
      """  The lookup table name  """  
      self.colName:str = obj["colName"]
      """  The column name  """  
      self.startRow:str = obj["startRow"]
      """  The Start row  """  
      self.endRow:str = obj["endRow"]
      """  The end row  """  
      pass

class DataColumnRange_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class DataLookup_input:
   """ Required : 
   configId
   testId
   lookupTblID
   rowName
   colName
   """  
   def __init__(self, obj):
      self.configId:str = obj["configId"]
      """  The configuration ID  """  
      self.testId:str = obj["testId"]
      """  The test ID  """  
      self.lookupTblID:str = obj["lookupTblID"]
      """  The lookup table name  """  
      self.rowName:str = obj["rowName"]
      """  The row name  """  
      self.colName:str = obj["colName"]
      """  The column name  """  
      pass

class DataLookup_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class DataRowListNum_input:
   """ Required : 
   configId
   testId
   lookupTableID
   rowName
   """  
   def __init__(self, obj):
      self.configId:str = obj["configId"]
      """  The configuration ID  """  
      self.testId:str = obj["testId"]
      """  The test ID  """  
      self.lookupTableID:str = obj["lookupTableID"]
      """  The lookup table name  """  
      self.rowName:str = obj["rowName"]
      """  The row name  """  
      pass

class DataRowListNum_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class DataRowList_input:
   """ Required : 
   configId
   testId
   lookupTableID
   rowName
   """  
   def __init__(self, obj):
      self.configId:str = obj["configId"]
      """  The configuration ID  """  
      self.testId:str = obj["testId"]
      """  The test ID  """  
      self.lookupTableID:str = obj["lookupTableID"]
      """  The lookup table name  """  
      self.rowName:str = obj["rowName"]
      """  The row name  """  
      pass

class DataRowList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class DataRowLookup_input:
   """ Required : 
   configId
   testId
   lookupTblID
   rowName
   searchValue
   """  
   def __init__(self, obj):
      self.configId:str = obj["configId"]
      """  The configuration ID  """  
      self.testId:str = obj["testId"]
      """  The test ID  """  
      self.lookupTblID:str = obj["lookupTblID"]
      """  The lookup table name  """  
      self.rowName:str = obj["rowName"]
      """  The row name  """  
      self.searchValue:str = obj["searchValue"]
      """  The value to search  """  
      pass

class DataRowLookup_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class DataRowRange_input:
   """ Required : 
   configId
   testId
   lookupTableID
   rowName
   startCol
   endCol
   """  
   def __init__(self, obj):
      self.configId:str = obj["configId"]
      """  The configuration ID  """  
      self.testId:str = obj["testId"]
      """  The test ID  """  
      self.lookupTableID:str = obj["lookupTableID"]
      """  The lookup table name  """  
      self.rowName:str = obj["rowName"]
      """  The row name  """  
      self.startCol:str = obj["startCol"]
      """  The start column  """  
      self.endCol:str = obj["endCol"]
      """  The end column.  """  
      pass

class DataRowRange_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class DeleteAssembliesInTestMode_input:
   """ Required : 
   configSequenceDS
   testID
   """  
   def __init__(self, obj):
      self.configSequenceDS:list[Erp_Tablesets_ConfigurationSequenceTableset] = obj["configSequenceDS"]
      self.testID:str = obj["testID"]
      """  Test Guid  """  
      pass

class DeleteAssembliesInTestMode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.configSequenceDS:list[Erp_Tablesets_ConfigurationSequenceTableset] = obj["configSequenceDS"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   groupSeq
   """  
   def __init__(self, obj):
      self.groupSeq:int = obj["groupSeq"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteSubConfiguration_input:
   """ Required : 
   ttPcValueGrpRow
   ttPcStructRow
   """  
   def __init__(self, obj):
      self.ttPcValueGrpRow:list[Erp_Tablesets_PcValueGrpRow] = obj["ttPcValueGrpRow"]
      self.ttPcStructRow:list[Erp_Tablesets_PcStructRow] = obj["ttPcStructRow"]
      pass

class DeleteSubConfiguration_output:
   def __init__(self, obj):
      pass

class DeleteTestInputsFileStoreEntry_input:
   """ Required : 
   testInputsFileName
   """  
   def __init__(self, obj):
      self.testInputsFileName:str = obj["testInputsFileName"]
      """  file to delete  """  
      pass

class DeleteTestInputsFileStoreEntry_output:
   def __init__(self, obj):
      pass

class EDIDemandConfiguration_input:
   """ Required : 
   parentMfgCompID
   iDemandContractNum
   iDemandHeadSeq
   iDemandDtlSeq
   iSmartString
   """  
   def __init__(self, obj):
      self.parentMfgCompID:str = obj["parentMfgCompID"]
      """  Parent Manufacturing Company ID  """  
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  Demand Contract Number  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  Demand Head Sequence that contains the configurable line  """  
      self.iDemandDtlSeq:int = obj["iDemandDtlSeq"]
      """  Demand Detail Sequence that contains the configurable part  """  
      self.iSmartString:str = obj["iSmartString"]
      """  Smart String value  """  
      pass

class EDIDemandConfiguration_output:
   def __init__(self, obj):
      pass

class EDIValidateSmartString_input:
   """ Required : 
   partNum
   revisionNum
   ipSmartString
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  The part num being used.  """  
      self.revisionNum:str = obj["revisionNum"]
      """  The revision num being used.  """  
      self.ipSmartString:str = obj["ipSmartString"]
      """  Smart String value  """  
      pass

class EDIValidateSmartString_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ssLogText:str = obj["parameters"]
      pass

      """  output parameters  """  

class EWCInitializeRuntime_input:
   """ Required : 
   ConfigId
   RelatedToTable
   RelatedToRowID
   PartNum
   PartRev
   ECCUser
   ECCPwd
   ReturnURL
   TestInputMode
   """  
   def __init__(self, obj):
      self.ConfigId:str = obj["ConfigId"]
      """  The ConfigID to run  """  
      self.RelatedToTable:str = obj["RelatedToTable"]
      """  The related to table name  """  
      self.RelatedToRowID:str = obj["RelatedToRowID"]
      """  The related to SysRowID  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number to configure  """  
      self.PartRev:str = obj["PartRev"]
      """  The revision to configure  """  
      self.ECCUser:str = obj["ECCUser"]
      """  The encrypted ECC user  """  
      self.ECCPwd:str = obj["ECCPwd"]
      """  The encrypted ECC password  """  
      self.ReturnURL:str = obj["ReturnURL"]
      """  The return URL  """  
      self.TestInputMode:bool = obj["TestInputMode"]
      """  True of running test inputs, else false for runtime  """  
      pass

class EWCInitializeRuntime_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Path to index.html  """  
      pass

   def parameters(self, obj):
      self.AccessToken:str = obj["parameters"]
      self.ExpiresIn:int = obj["parameters"]
      pass

      """  output parameters  """  

class EWCReadAllBytesIfNewer_input:
   """ Required : 
   FileName
   LastModifiedUTCDateTime
   """  
   def __init__(self, obj):
      self.FileName:str = obj["FileName"]
      """  The EWC runtime file name  """  
      self.LastModifiedUTCDateTime:str = obj["LastModifiedUTCDateTime"]
      """  Only return the file if the UTC DateTime is greater than this parameter  """  
      pass

class EWCReadAllBytesIfNewer_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The file as a byte array  """  
      pass

class EWCSuggestSmartString_input:
   """ Required : 
   configID
   testMode
   ipRelatedToTable
   ipRelatedToSysRowID
   smartStringValues
   subPartNum
   basePartNum
   partNum
   subBasePartNum
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration ID  """  
      self.testMode:bool = obj["testMode"]
      """  Test Inputs true/false  """  
      self.ipRelatedToTable:str = obj["ipRelatedToTable"]
      """  Target entity this call is related to  """  
      self.ipRelatedToSysRowID:str = obj["ipRelatedToSysRowID"]
      """  The SysRowID of the target Entity  """  
      self.smartStringValues:list[System_Collections_Generic_KeyValuePair_System_String_System_String] = obj["smartStringValues"]
      """  Collection of current input values gathered so far during the configuration session.  """  
      self.subPartNum:str = obj["subPartNum"]
      self.basePartNum:str = obj["basePartNum"]
      self.partNum:str = obj["partNum"]
      self.subBasePartNum:str = obj["subBasePartNum"]
      pass

class EWCSuggestSmartString_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.outSmartString:str = obj["parameters"]
      pass

      """  output parameters  """  

class EWCTestRules_input:
   """ Required : 
   partNum
   revisionNum
   configID
   testRulesResultsDS
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  part number Test Rules was executed for  """  
      self.revisionNum:str = obj["revisionNum"]
      """  revision number Test Rules was executed for  """  
      self.configID:str = obj["configID"]
      """  Configuration ID Test Rules was executed for  """  
      self.testRulesResultsDS:list[Erp_Tablesets_PcTestResultsTableset] = obj["testRulesResultsDS"]
      pass

class EWCTestRules_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.testRulesResultsDS:list[Erp_Tablesets_PcTestResultsTableset] = obj["testRulesResultsDS"]
      pass

      """  output parameters  """  

class EWCWriteOrCreateAllBytes_input:
   """ Required : 
   FileName
   Bytes
   """  
   def __init__(self, obj):
      self.FileName:str = obj["FileName"]
      """  The name of the file.  """  
      self.Bytes:str = obj["Bytes"]
      """  The file contents  """  
      pass

class EWCWriteOrCreateAllBytes_output:
   def __init__(self, obj):
      pass

class Erp_Shared_Lib_Configurator_ClientCheckSyntaxArgs:
   def __init__(self, obj):
      self.checkContext:int = obj["checkContext"]
      self.tableName:str = obj["tableName"]
      self.inputName:str = obj["inputName"]
      self.pageNumber:int = obj["pageNumber"]
      self.syntaxCode:str = obj["syntaxCode"]
      self.eventName:str = obj["eventName"]
      self.generateCSharpForEWC:bool = obj["generateCSharpForEWC"]
      pass

class Erp_Shared_Lib_Configurator_DocRuleCheckSyntaxArgs:
   def __init__(self, obj):
      self.docRuleContext:int = obj["docRuleContext"]
      self.ruleNum:int = obj["ruleNum"]
      self.actionNum:int = obj["actionNum"]
      self.docRuleType:int = obj["docRuleType"]
      self.commandType:str = obj["commandType"]
      self.lValue:str = obj["lValue"]
      self.rValue:str = obj["rValue"]
      self.rValueType:str = obj["rValueType"]
      self.syntaxCode:str = obj["syntaxCode"]
      self.DocVarNum:int = obj["DocVarNum"]
      pass

class Erp_Shared_Lib_Configurator_MethodRuleCheckSyntaxArgs:
   def __init__(self, obj):
      self.ruleSetID:int = obj["ruleSetID"]
      self.ruleNum:int = obj["ruleNum"]
      self.ruleTag:str = obj["ruleTag"]
      self.ruleType:int = obj["ruleType"]
      self.expressionType:str = obj["expressionType"]
      self.syntaxCode:str = obj["syntaxCode"]
      self.KeepWhenType:str = obj["KeepWhenType"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.AltMethod:str = obj["AltMethod"]
      self.SeqNum:int = obj["SeqNum"]
      self.VarNum:int = obj["VarNum"]
      pass

class Erp_Shared_Lib_Configurator_PCKeyValuePair_System_String_System_String:
   def __init__(self, obj):
      self.Key:str = obj["Key"]
      self.Value:str = obj["Value"]
      pass

class Erp_Shared_Lib_Configurator_ServerEventCheckSyntaxArgs:
   def __init__(self, obj):
      self.serverEventTable:int = obj["serverEventTable"]
      self.serverMethodName:str = obj["serverMethodName"]
      self.expressionType:str = obj["expressionType"]
      self.syntaxCode:str = obj["syntaxCode"]
      pass

class Erp_Tablesets_ConfigurationRuntimeListTableset:
   def __init__(self, obj):
      self.PcValueGrpList:list[Erp_Tablesets_PcValueGrpListRow] = obj["PcValueGrpList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ConfigurationRuntimeTableset:
   def __init__(self, obj):
      self.PcValueGrp:list[Erp_Tablesets_PcValueGrpRow] = obj["PcValueGrp"]
      self.PcValueHead:list[Erp_Tablesets_PcValueHeadRow] = obj["PcValueHead"]
      self.PcConfigurationParams:list[Erp_Tablesets_PcConfigurationParamsRow] = obj["PcConfigurationParams"]
      self.PcConfiguredDrawings:list[Erp_Tablesets_PcConfiguredDrawingsRow] = obj["PcConfiguredDrawings"]
      self.PcContextProperties:list[Erp_Tablesets_PcContextPropertiesRow] = obj["PcContextProperties"]
      self.PcInputsLayerDetail:list[Erp_Tablesets_PcInputsLayerDetailRow] = obj["PcInputsLayerDetail"]
      self.PcInputsLayerHeader:list[Erp_Tablesets_PcInputsLayerHeaderRow] = obj["PcInputsLayerHeader"]
      self.PcInputsPublishToDocParams:list[Erp_Tablesets_PcInputsPublishToDocParamsRow] = obj["PcInputsPublishToDocParams"]
      self.PcInputVar:list[Erp_Tablesets_PcInputVarRow] = obj["PcInputVar"]
      self.PcValueInputLayerDetail:list[Erp_Tablesets_PcValueInputLayerDetailRow] = obj["PcValueInputLayerDetail"]
      self.PcValueInputLayerHeader:list[Erp_Tablesets_PcValueInputLayerHeaderRow] = obj["PcValueInputLayerHeader"]
      self.QBuildMapping:list[Erp_Tablesets_QBuildMappingRow] = obj["QBuildMapping"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ConfigurationSequenceTableset:
   def __init__(self, obj):
      self.PcStruct:list[Erp_Tablesets_PcStructRow] = obj["PcStruct"]
      self.PcConfigSmartString:list[Erp_Tablesets_PcConfigSmartStringRow] = obj["PcConfigSmartString"]
      self.PcStrComp:list[Erp_Tablesets_PcStrCompRow] = obj["PcStrComp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ConfigurationSummaryRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.QuoteLine:int = obj["QuoteLine"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.JobNum:str = obj["JobNum"]
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      self.DocConfigUnitPrice:int = obj["DocConfigUnitPrice"]
      self.DocConfigBaseUnitPrice:int = obj["DocConfigBaseUnitPrice"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.LastConfigDate:str = obj["LastConfigDate"]
      self.LastConfigTime:int = obj["LastConfigTime"]
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      self.Rpt1ConfigBaseUnitPrice:int = obj["Rpt1ConfigBaseUnitPrice"]
      self.Rpt2ConfigBaseUnitPrice:int = obj["Rpt2ConfigBaseUnitPrice"]
      self.Rpt3ConfigBaseUnitPrice:int = obj["Rpt3ConfigBaseUnitPrice"]
      self.Rpt1ConfigUnitPrice:int = obj["Rpt1ConfigUnitPrice"]
      self.Rpt2ConfigUnitPrice:int = obj["Rpt2ConfigUnitPrice"]
      self.Rpt3ConfigUnitPrice:int = obj["Rpt3ConfigUnitPrice"]
      self.Rpt1DocConfigBaseUnitPrice:int = obj["Rpt1DocConfigBaseUnitPrice"]
      self.Rpt2DocConfigBaseUnitPrice:int = obj["Rpt2DocConfigBaseUnitPrice"]
      self.Rpt3DocConfigBaseUnitPrice:int = obj["Rpt3DocConfigBaseUnitPrice"]
      self.Rpt1DocConfigUnitPrice:int = obj["Rpt1DocConfigUnitPrice"]
      self.Rpt2DocConfigUnitPrice:int = obj["Rpt2DocConfigUnitPrice"]
      self.Rpt3DocConfigUnitPrice:int = obj["Rpt3DocConfigUnitPrice"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.CurrencyID:str = obj["CurrencyID"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      self.ConfigID:str = obj["ConfigID"]
      self.SmartString:str = obj["SmartString"]
      self.BasePartNum:str = obj["BasePartNum"]
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      self.GroupSeq:int = obj["GroupSeq"]
      self.HeadNum:int = obj["HeadNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConfigurationSummaryTableset:
   def __init__(self, obj):
      self.ConfigurationSummary:list[Erp_Tablesets_ConfigurationSummaryRow] = obj["ConfigurationSummary"]
      self.PcInputValue:list[Erp_Tablesets_PcInputValueRow] = obj["PcInputValue"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MethodsListRow:
   def __init__(self, obj):
      self.SeqNum:int = obj["SeqNum"]
      """  Original AssemblySeq  """  
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.AltMethod:str = obj["AltMethod"]
      self.BomLevel:int = obj["BomLevel"]
      self.GeneratedRuleTag:str = obj["GeneratedRuleTag"]
      self.IsConfig:bool = obj["IsConfig"]
      self.TestType:str = obj["TestType"]
      self.Processed:bool = obj["Processed"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcActionResultRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RuleSetID:int = obj["RuleSetID"]
      self.RuleSeq:int = obj["RuleSeq"]
      self.SeqNum:int = obj["SeqNum"]
      self.ExprType:str = obj["ExprType"]
      self.RuleTag:str = obj["RuleTag"]
      self.ExpressionText:str = obj["ExpressionText"]
      self.ExprResult:str = obj["ExprResult"]
      self.TestType:str = obj["TestType"]
      self.ActionResult:str = obj["ActionResult"]
      self.ExprToolTip:str = obj["ExprToolTip"]
      self.BOMElementSysRowID:str = obj["BOMElementSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcAsmResultRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TestType:str = obj["TestType"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.AltMethod:str = obj["AltMethod"]
      self.Description:str = obj["Description"]
      self.RuleTag:str = obj["RuleTag"]
      self.ParentAsmSeq:int = obj["ParentAsmSeq"]
      self.ParentRuleTag:str = obj["ParentRuleTag"]
      self.RelatedOperation:int = obj["RelatedOperation"]
      self.HasRuleSet:bool = obj["HasRuleSet"]
      self.IsKept:bool = obj["IsKept"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcConfigSmartStringRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ConfigID:str = obj["ConfigID"]
      self.StringStyle:str = obj["StringStyle"]
      self.PrefacePart:bool = obj["PrefacePart"]
      self.CrtCustPart:bool = obj["CrtCustPart"]
      """  Reserved for future development  """  
      self.Separator:str = obj["Separator"]
      self.NumberFormat:str = obj["NumberFormat"]
      """  Reserved for future development  """  
      self.StartNumber:int = obj["StartNumber"]
      self.TargetEntityForSmartString:str = obj["TargetEntityForSmartString"]
      """  Reserved for future development  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcConfigurationParamsRow:
   def __init__(self, obj):
      self.ForeignTableName:str = obj["ForeignTableName"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.TgtStructTag:str = obj["TgtStructTag"]
      self.StructID:int = obj["StructID"]
      self.InSmartString:str = obj["InSmartString"]
      self.IsTestPlan:bool = obj["IsTestPlan"]
      self.SpecID:str = obj["SpecID"]
      self.SpecRevNum:str = obj["SpecRevNum"]
      self.InspType:str = obj["InspType"]
      self.RunningStateOverride:str = obj["RunningStateOverride"]
      self.EqmPassed:str = obj["EqmPassed"]
      self.EqmFailDesc:str = obj["EqmFailDesc"]
      self.EqmOverride:bool = obj["EqmOverride"]
      self.RelatedToTable:str = obj["RelatedToTable"]
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      self.SourceTable:str = obj["SourceTable"]
      self.TestID:str = obj["TestID"]
      self.TestMode:str = obj["TestMode"]
      self.AppServerID:str = obj["AppServerID"]
      self.PcStatusSysRowID:str = obj["PcStatusSysRowID"]
      self.ConfigVersion:int = obj["ConfigVersion"]
      self.UniqueID:str = obj["UniqueID"]
      self.ConfigID:str = obj["ConfigID"]
      self.Company:str = obj["Company"]
      self.InputPricingSet:bool = obj["InputPricingSet"]
      self.OrderPrice:int = obj["OrderPrice"]
      self.QuotePrice:int = obj["QuotePrice"]
      self.DemandPrice:int = obj["DemandPrice"]
      self.PurchasePrice:int = obj["PurchasePrice"]
      self.WebOrderBasketPrice:int = obj["WebOrderBasketPrice"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.AltMethod:str = obj["AltMethod"]
      self.InitialStructTag:str = obj["InitialStructTag"]
      self.InitialRuleTag:str = obj["InitialRuleTag"]
      self.TrackerMode:bool = obj["TrackerMode"]
      """  Determines if a configuration was opened from a tracker.  """  
      self.ConfigType:str = obj["ConfigType"]
      self.EWCConfiguratorURL:str = obj["EWCConfiguratorURL"]
      """  This is the web address to call when launching an Epicor Web configurtor.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcConfiguredDrawingsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ConfigID:str = obj["ConfigID"]
      self.GroupSeq:int = obj["GroupSeq"]
      self.HeadNum:int = obj["HeadNum"]
      self.InputName:str = obj["InputName"]
      self.ImageID:str = obj["ImageID"]
      self.Content:str = obj["Content"]
      self.PageSeq:int = obj["PageSeq"]
      self.QBuildObjExist:bool = obj["QBuildObjExist"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcContextPropertiesRow:
   def __init__(self, obj):
      self.AttributeID:str = obj["AttributeID"]
      self.CompanyID:str = obj["CompanyID"]
      self.ConfigurationID:str = obj["ConfigurationID"]
      self.Currency:str = obj["Currency"]
      self.CustomerID:str = obj["CustomerID"]
      self.DemandHeadNumber:int = obj["DemandHeadNumber"]
      self.DemandLineNumber:int = obj["DemandLineNumber"]
      self.Entity:str = obj["Entity"]
      self.JobNumber:str = obj["JobNumber"]
      self.OrderDetailNumber:int = obj["OrderDetailNumber"]
      self.OrderNumber:int = obj["OrderNumber"]
      self.PackSlip:str = obj["PackSlip"]
      self.PartNumber:str = obj["PartNumber"]
      self.PartRevisionNumber:str = obj["PartRevisionNumber"]
      self.PODetailNumber:int = obj["PODetailNumber"]
      self.PONumber:int = obj["PONumber"]
      self.QuoteLineNumber:int = obj["QuoteLineNumber"]
      self.QuoteNumber:int = obj["QuoteNumber"]
      self.SpecificationID:str = obj["SpecificationID"]
      self.SpecificationRevision:str = obj["SpecificationRevision"]
      self.SupplierID:str = obj["SupplierID"]
      self.UserID:str = obj["UserID"]
      self.NonConfID:str = obj["NonConfID"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.RMALine:int = obj["RMALine"]
      self.PackLine:int = obj["PackLine"]
      self.SiteID:str = obj["SiteID"]
      self.ECCQuoteNum:str = obj["ECCQuoteNum"]
      self.CustomerNumber:int = obj["CustomerNumber"]
      self.SupplierNumber:int = obj["SupplierNumber"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcFieldPropertiesTransportRow:
   def __init__(self, obj):
      self.AttributeID:str = obj["AttributeID"]
      self.GroupSeq:int = obj["GroupSeq"]
      self.HeadNum:int = obj["HeadNum"]
      self.Height:int = obj["Height"]
      self.Increment:int = obj["Increment"]
      self.InitialValue:str = obj["InitialValue"]
      self.InputName:str = obj["InputName"]
      self.Invisible:bool = obj["Invisible"]
      self.Label:str = obj["Label"]
      self.MaximumDate:str = obj["MaximumDate"]
      self.MaximumDecimal:int = obj["MaximumDecimal"]
      self.MinimumDate:str = obj["MinimumDate"]
      self.MinimumDecimal:int = obj["MinimumDecimal"]
      self.PageSeq:int = obj["PageSeq"]
      self.ReadOnly:bool = obj["ReadOnly"]
      self.Required:bool = obj["Required"]
      self.ToolTip:str = obj["ToolTip"]
      self.ValidList:str = obj["ValidList"]
      self.ValueSetSeq:int = obj["ValueSetSeq"]
      self.Width:int = obj["Width"]
      self.XPosition:int = obj["XPosition"]
      self.YPosition:int = obj["YPosition"]
      self.ControlType:str = obj["ControlType"]
      self.DataType:str = obj["DataType"]
      self.AutoSizeList:bool = obj["AutoSizeList"]
      self.ListWidth:int = obj["ListWidth"]
      self.Description:str = obj["Description"]
      self.ImageSource:str = obj["ImageSource"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcImagesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ConfigID:str = obj["ConfigID"]
      self.ImageID:str = obj["ImageID"]
      self.Content:str = obj["Content"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcImagesTableset:
   def __init__(self, obj):
      self.PcImages:list[Erp_Tablesets_PcImagesRow] = obj["PcImages"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PcInputValueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GroupSeq:int = obj["GroupSeq"]
      self.PageSeq:int = obj["PageSeq"]
      self.SubTableName:str = obj["SubTableName"]
      self.InputName:str = obj["InputName"]
      self.InputValue:str = obj["InputValue"]
      self.HeadNum:int = obj["HeadNum"]
      self.ReadOnly:bool = obj["ReadOnly"]
      self.NoDispSummary:bool = obj["NoDispSummary"]
      self.SideLabel:str = obj["SideLabel"]
      self.SummaryLabel:str = obj["SummaryLabel"]
      self.ConfigID:str = obj["ConfigID"]
      self.TabOrder:int = obj["TabOrder"]
      self.PageTitle:str = obj["PageTitle"]
      self.DspPageSeq:int = obj["DspPageSeq"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputVarRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.VarName:str = obj["VarName"]
      """  VarName  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.InitValue:str = obj["InitValue"]
      """  InitValue  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.InitString:str = obj["InitString"]
      self.InitDecimal:int = obj["InitDecimal"]
      self.InitLogical:bool = obj["InitLogical"]
      self.InitDate:str = obj["InitDate"]
      self.InUse:bool = obj["InUse"]
      """  Determines if the variable is being used by an input.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsLayerDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.InputName:str = obj["InputName"]
      """  InputName  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  ImageLayerID  """  
      self.LayerSeq:int = obj["LayerSeq"]
      """  LayerSeq  """  
      self.LayerName:str = obj["LayerName"]
      """  LayerName  """  
      self.LayerDesc:str = obj["LayerDesc"]
      """  LayerDesc  """  
      self.ZIndex:int = obj["ZIndex"]
      """  Order in which layers are placed on the base image.  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.FileType:str = obj["FileType"]
      """  Png type is supported.  """  
      self.Category:str = obj["Category"]
      """  Free form text enabling users to categorize layers  """  
      self.Width:int = obj["Width"]
      """  Width of image  """  
      self.Height:int = obj["Height"]
      """  Height of image  """  
      self.xPos:int = obj["xPos"]
      """  Reserved for Future Development  """  
      self.yPos:int = obj["yPos"]
      """  Reserved for Future Development  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsLayerHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.InputName:str = obj["InputName"]
      """  Input name this header is assigned.  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  Image Layer ID.  """  
      self.ImageID:str = obj["ImageID"]
      """  File name of the image to be retrieved from the Image URL.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ImageURL:str = obj["ImageURL"]
      """  The URL location of the image.  """  
      self.FileType:str = obj["FileType"]
      """  File types png and jpg are supported.  """  
      self.Width:int = obj["Width"]
      """  Image Width  """  
      self.Height:int = obj["Height"]
      """  Image height  """  
      self.Version:int = obj["Version"]
      """  Internal next number indicating the current version. Thi is is used by Verfiy Configuration to identify when a warning message is to be written to the log.  """  
      self.xPos:int = obj["xPos"]
      """  Reserved for future development  """  
      self.yPos:int = obj["yPos"]
      """  Reserved for future development  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsPublishToDocParamsRow:
   def __init__(self, obj):
      self.Key:str = obj["Key"]
      self.Value:str = obj["Value"]
      self.Company:str = obj["Company"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcJobAsmblRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if the Job is complete.  This is a mirror image of JobHead.JobComplete.  Not directly maintainable.  When Job is complete, then all assembly records are also marked complete.  This is used to make database access to open assembly records more efficient.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  """  
      self.Description:str = obj["Description"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  The production quantity required for this assembly per one of it's parent part.  """  
      self.IUM:str = obj["IUM"]
      """  The internal unit of measure for this assembly.  Use the Part.IUM as a default.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """   This is how many of the assemblies are required to produce the END ITEM.  This is a calculated field.  Calculated as the (( Parents RequiredQty - Parents PullQty) X QtyPer) + OverRunQty.
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer, or Overrun fields are changed. The refresh may also occur if the structure of the assemblies is changed.
The production quantity for the assembly which will drive raw material requirements and estimated production times can be determined by ( RequiredQty - PullQty).  """  
      self.PullQty:int = obj["PullQty"]
      """  This indicates a quantity that will be pulled from inventory for this assembly instead of being manufactured. This is a fixed quantity and is not affected by  QtyPer type changes. If this a valid Part, then it must update the PartWhse.AllocQty.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  This is the warehouse that the material is allocated against.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this Job Assembly.  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  The estimated unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  """  
      self.EstMtlBurUnitCost:int = obj["EstMtlBurUnitCost"]
      """  The estimated Mtl burden unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  """  
      self.OverRunQty:int = obj["OverRunQty"]
      """  This value indicates a quantity that is planned to be overrun and put into inventory. This is kept as a separate field so that is does not distort the BOM requirement relationships. This increases the total production quantity for the assembly.  This is a FIXED quantity and is not affected by structure or qty/per type changes.  """  
      self.StartDate:str = obj["StartDate"]
      """  Scheduled start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process.  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  """  
      self.DueDate:str = obj["DueDate"]
      """  The scheduled due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling.  It represents the  "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  """  
      self.Parent:int = obj["Parent"]
      """  Sequence number of the Parent Assembly.  """  
      self.PriorPeer:int = obj["PriorPeer"]
      """   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the NextPeer is -1.  Then NextPeer of that assembly gets updated with this assemblies sequence number and this assembly gets its PriorPeer field updated with the sequence number from the assembly which was found.  """  
      self.NextPeer:int = obj["NextPeer"]
      """   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the PriorPeer is -1.  Then the PriorPeer of that assembly is updated with this assemblies sequence number and then this assemblies NextPeer gets updated with the sequence number from the assembly that was found.  """  
      self.Child:int = obj["Child"]
      """  Sequence number of this assemblies very first subassembly.  This is known as the Child assembly.  Automatically maintained by the maintenance programs.  The logic is to find the Parent assembly record and if its child is -1, update it with this assemblies sequence number.  """  
      self.TotalCost:int = obj["TotalCost"]
      """  Total cost to date, of this component that was issued from stock.  """  
      self.MtlBurCost:int = obj["MtlBurCost"]
      """  Total material burden cost to date, of this component that was issued from stock.  """  
      self.IssuedQty:int = obj["IssuedQty"]
      """  This quantity is a summary of all Issue Transactions that were issued to meet this assemblies PullQty requirements.  This is not directly maintainable.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Optional field for Engineering Drawing Number.  Defaulted from BomHead.DrawNum during methods pull functions.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """  Indicates if the pull quantity has been issued complete.  If "yes" then this record is NOT part of the PartWhse.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job Assembly comments.  """  
      self.InCopyList:bool = obj["InCopyList"]
      """  Indicates if this assembly is to be included in the browse of assemblies in the  "get details" function.  The user can use this option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly, it just keeps it out of the browse.  """  
      self.BomSequence:int = obj["BomSequence"]
      """  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  """  
      self.BomLevel:int = obj["BomLevel"]
      """  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Scheduled "What If" start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling.  It represents the What-If  "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  The scheduled "What-If" due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  """  
      self.TLALaborCost:int = obj["TLALaborCost"]
      """  This Level Actual Labor Cost.  """  
      self.TLABurdenCost:int = obj["TLABurdenCost"]
      """  This Level Actual Burden Cost.  """  
      self.TLAMaterialCost:int = obj["TLAMaterialCost"]
      """  This Level Actual Material Cost.  """  
      self.TLASubcontractCost:int = obj["TLASubcontractCost"]
      """  This Level Actual Subcontract Cost.  """  
      self.TLAMtlBurCost:int = obj["TLAMtlBurCost"]
      """  This Level Actual Material Burden Cost.  """  
      self.TLASetupHours:int = obj["TLASetupHours"]
      """  This Level Actual Setup Hours.  """  
      self.TLAProdHours:int = obj["TLAProdHours"]
      """  This Level Actual Production Hours.  """  
      self.TLELaborCost:int = obj["TLELaborCost"]
      """  This Level Estimated Labor Cost.  """  
      self.TLEBurdenCost:int = obj["TLEBurdenCost"]
      """  This Level Estimated Burden Cost.  """  
      self.TLEMaterialCost:int = obj["TLEMaterialCost"]
      """  This Level Estimated Material Cost.  """  
      self.TLESubcontractCost:int = obj["TLESubcontractCost"]
      """  This Level Estimated Subcontract Cost.  """  
      self.TLEMtlBurCost:int = obj["TLEMtlBurCost"]
      """  This Level Estimated Material Burden Cost.  """  
      self.TLESetupHours:int = obj["TLESetupHours"]
      """  This Level Estimated Setup Hours.  """  
      self.TLEProdHours:int = obj["TLEProdHours"]
      """  This Level Estimated Production Hours.  """  
      self.LLALaborCost:int = obj["LLALaborCost"]
      """  Lower Level Actual Labor Cost.  """  
      self.LLABurdenCost:int = obj["LLABurdenCost"]
      """  Lower Level Burden Labor Cost.  """  
      self.LLAMaterialCost:int = obj["LLAMaterialCost"]
      """  Lower Level Actual Material Cost.  """  
      self.LLASubcontractCost:int = obj["LLASubcontractCost"]
      """  Lower Level Actual Subcontractor Cost.  """  
      self.LLAMtlBurCost:int = obj["LLAMtlBurCost"]
      """  Lower Level Actual Material Burden Cost.  """  
      self.LLASetupHours:int = obj["LLASetupHours"]
      """  Lower Level Actual Setup Hours.  """  
      self.LLAProdHours:int = obj["LLAProdHours"]
      """  Lower Level Actual Production Hours.  """  
      self.LLELaborCost:int = obj["LLELaborCost"]
      """  Lower Level Estimated Labor Cost.  """  
      self.LLEBurdenCost:int = obj["LLEBurdenCost"]
      """  Lower Level Estimated Burden Cost.  """  
      self.LLEMaterialCost:int = obj["LLEMaterialCost"]
      """  Lower Level Estimated Material Cost.  """  
      self.LLESubcontractCost:int = obj["LLESubcontractCost"]
      """  Lower Level Estimated Subcontract Cost.  """  
      self.LLEMtlBurCost:int = obj["LLEMtlBurCost"]
      """  Lower Level Estimated Material Burden Cost.  """  
      self.LLESetupHours:int = obj["LLESetupHours"]
      """  Lower Level Estimated Setup Hours.  """  
      self.LLEProdHours:int = obj["LLEProdHours"]
      """  Lower Level Estimated Production Hours.  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number (JobOper.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable.  Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.FindNum:str = obj["FindNum"]
      """  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  """  
      self.ReceivedToStock:int = obj["ReceivedToStock"]
      """  Total received to stock.  This pertains receiving an OverRun quantity.  Used to update the PartDtl file for expected production quantity.  PartDtl is OverRun - ReceivedToStock.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Direct:bool = obj["Direct"]
      """  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified..  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   An assembly record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  """  
      self.TLAMaterialLabCost:int = obj["TLAMaterialLabCost"]
      """  This Level Actual Material Labor Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialLabCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.TLAMaterialMtlCost:int = obj["TLAMaterialMtlCost"]
      """  This Level Actual Issued Material Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialMtlCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.TLAMaterialSubCost:int = obj["TLAMaterialSubCost"]
      """  This Level Actual Material Subcontract Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialSubCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.TLAMaterialBurCost:int = obj["TLAMaterialBurCost"]
      """  This Level Actual Material Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialBurCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  """  
      self.LLAMaterialLabCost:int = obj["LLAMaterialLabCost"]
      """  Lower Level Actual Material Labor Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialLabCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.LLAMaterialMtlCost:int = obj["LLAMaterialMtlCost"]
      """  Lower Level Actual Material Material Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialMtlCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.LLAMaterialSubCost:int = obj["LLAMaterialSubCost"]
      """  Lower Level Actual Material Subcontract Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialSubCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.LLAMaterialBurCost:int = obj["LLAMaterialBurCost"]
      """  Lower Level Actual Material Burden Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialBurCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  """  
      self.TotalMtlMtlCost:int = obj["TotalMtlMtlCost"]
      """  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  """  
      self.TotalMtlLabCost:int = obj["TotalMtlLabCost"]
      """  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.TotalMtlSubCost:int = obj["TotalMtlSubCost"]
      """  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.TotalMtlBurCost:int = obj["TotalMtlBurCost"]
      """  Total Burden cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this assembly belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this assembly relates to.  """  
      self.RestoreFlag:str = obj["RestoreFlag"]
      """  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.OrigRequiredQty:int = obj["OrigRequiredQty"]
      """  This field will be set to the value of the JobAsmbl.RequiredQty at the time the JobHead.Engineered flag is set to true.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      """  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  """  
      self.TLAMaterialMtlBurCost:int = obj["TLAMaterialMtlBurCost"]
      """  This Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for this level.  Otherwise, TLAMaterialMtlBurCost may be populated but is not included in the calculation of TLAMaterialCost.  """  
      self.LLAMaterialMtlBurCost:int = obj["LLAMaterialMtlBurCost"]
      """  Lower Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for the lower level.  Otherwise, LLAMaterialMtlBurCost may be populated but is not included in the calculation of LLAMaterialCost.  """  
      self.TLAMfgCompLabCost:int = obj["TLAMfgCompLabCost"]
      """  This Level Actual Component Labor Cost.  This is the Total Labor costs of all manufactured parts issued as material for this level. Unlike TLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompMtlCost:int = obj["TLAMfgCompMtlCost"]
      """  This Level Actual Component Material Cost.  This is the Total Material costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompSubCost:int = obj["TLAMfgCompSubCost"]
      """  This Level Actual Component Subcontract Cost.  This is the Total Subcontract costs of all manufactured parts issued as material for this level. Unlike TLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompBurCost:int = obj["TLAMfgCompBurCost"]
      """  This Level Actual Component Burden Cost.  This is the Total Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.TLAMfgCompMtlBurCost:int = obj["TLAMfgCompMtlBurCost"]
      """  This Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  """  
      self.LLAMfgCompLabCost:int = obj["LLAMfgCompLabCost"]
      """  Lower Level Actual Component Labor Cost. This is the Total Labor costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompMtlCost:int = obj["LLAMfgCompMtlCost"]
      """  Lower Level Actual Component Material Cost. This is the Total Material costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompSubCost:int = obj["LLAMfgCompSubCost"]
      """  Lower Level Actual Component Subcontract Cost. This is the Total Subcontract costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompBurCost:int = obj["LLAMfgCompBurCost"]
      """  Lower Level Actual Component Burden Cost. This is the Total Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.LLAMfgCompMtlBurCost:int = obj["LLAMfgCompMtlBurCost"]
      """  Lower Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  """  
      self.Weight:int = obj["Weight"]
      """  Assembly Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Assembly Weight UOM defaulted from Part Master.  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      """  Original Material Sequence. Used in the configurator.  """  
      self.OrigRuleTag:str = obj["OrigRuleTag"]
      """  Original Rule Tag. Used in the Configurator.  """  
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  Base Part Number. Used in the configurator to identify the configurator part Number.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  """  
      self.EstMtlUnitCost:int = obj["EstMtlUnitCost"]
      """   The estimated material unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.EstLbrUnitCost:int = obj["EstLbrUnitCost"]
      """   The estimated labor unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.EstBurUnitCost:int = obj["EstBurUnitCost"]
      """   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.EstSubUnitCost:int = obj["EstSubUnitCost"]
      """   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  """  
      self.PlanAsAsm:bool = obj["PlanAsAsm"]
      """  Indicates if the sub-assemby can be spawned off to a different job.  This can occur during the firming up of a job.  """  
      self.PAARef:str = obj["PAARef"]
      """  Plan as assembly reference.  Used to link related subassemblies together when multiple assemblies are created for the same part due to PartSite lot size values.  """  
      self.PAAFirm:bool = obj["PAAFirm"]
      """  Used only on Plan As Assembly records.  Indicates the sub assembly will be split of from the the current job and a separate job for the assembly will be created.  """  
      self.EstScrap:int = obj["EstScrap"]
      """  EstScrap =  a number representing either a scrap qty or a scrap percent depending on the value of EstScrapType field.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.ReassignSNAsm:bool = obj["ReassignSNAsm"]
      """  Reassign Serial Numbers Assembly  """  
      self.TLAODCCost:int = obj["TLAODCCost"]
      """  This Level Actual Other Direct Cost.  """  
      self.AssemblyMatch:str = obj["AssemblyMatch"]
      """  AssemblyMatch  """  
      self.JdfStatus:str = obj["JdfStatus"]
      """  JdfStatus  """  
      self.PressDevice:str = obj["PressDevice"]
      """  PressDevice  """  
      self.DigitalFileName:str = obj["DigitalFileName"]
      """  DigitalFileName  """  
      self.PrepressJobName:str = obj["PrepressJobName"]
      """  PrepressJobName  """  
      self.JdfPrepressAction:str = obj["JdfPrepressAction"]
      """  JdfPrepressAction  """  
      self.SendToPress:bool = obj["SendToPress"]
      """  SendToPress  """  
      self.RemovedFromPlan:bool = obj["RemovedFromPlan"]
      """  RemovedFromPlan  """  
      self.SendToPressInitiator:int = obj["SendToPressInitiator"]
      """  SendToPressInitiator  """  
      self.OperationType:int = obj["OperationType"]
      """  OperationType  """  
      self.SendToPrePress:bool = obj["SendToPrePress"]
      """  SendToPrePress  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartPlanInfo:str = obj["PartPlanInfo"]
      """  PartPlanInfo  """  
      self.OrigStructTag:str = obj["OrigStructTag"]
      """  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcJobHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobClosed:bool = obj["JobClosed"]
      """  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  Date the Job was closed.  Defaults as the system but can be overridden.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  """  
      self.JobCompletionDate:str = obj["JobCompletionDate"]
      """  The date that production was completed for this Job.  Maintained via Job Completion Processing.  """  
      self.JobEngineered:bool = obj["JobEngineered"]
      """  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  """  
      self.CheckOff1:bool = obj["CheckOff1"]
      """   Optional Job check off number 1.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff2:bool = obj["CheckOff2"]
      """   Optional Job check off number 2.  The label for this field is found in JCSyst. If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff3:bool = obj["CheckOff3"]
      """   Optional Job check off number 3.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff4:bool = obj["CheckOff4"]
      """  Optional Job check off number 4.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff5:bool = obj["CheckOff5"]
      """  Optional Job check off number 5.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.JobReleased:bool = obj["JobReleased"]
      """  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  """  
      self.JobHeld:bool = obj["JobHeld"]
      """  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  """  
      self.SchedStatus:str = obj["SchedStatus"]
      """  Scheduling Status Control (R-Required, P-Pending, A-Active, C-Complete).  NOT CURRENTLY IMPLEMENTED.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  """  
      self.PartNum:str = obj["PartNum"]
      """   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.ProdQty:int = obj["ProdQty"]
      """  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  """  
      self.IUM:str = obj["IUM"]
      """  The unit of measure for the job.  Defaulted from Part.IUM.  """  
      self.StartDate:str = obj["StartDate"]
      """  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.DueDate:str = obj["DueDate"]
      """  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.ReqDueDate:str = obj["ReqDueDate"]
      """  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  """  
      self.JobCode:str = obj["JobCode"]
      """  An optional user defined code.  This will be used for report selections and views of job headers.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Contains the quote line number reference. (see QuoteNum )  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.UserChar1:str = obj["UserChar1"]
      """  UserChar1  """  
      self.UserChar2:str = obj["UserChar2"]
      """  UserChar2  """  
      self.UserChar3:str = obj["UserChar3"]
      """  UserChar3  """  
      self.UserChar4:str = obj["UserChar4"]
      """  UserChar4  """  
      self.UserDate1:str = obj["UserDate1"]
      """  UserDate1  """  
      self.UserDate2:str = obj["UserDate2"]
      """  UserDate2  """  
      self.UserDate3:str = obj["UserDate3"]
      """  UserDate3  """  
      self.UserDate4:str = obj["UserDate4"]
      """  UserDate4  """  
      self.UserDecimal1:int = obj["UserDecimal1"]
      """  UserDecimal1  """  
      self.UserDecimal2:int = obj["UserDecimal2"]
      """  UserDecimal2  """  
      self.UserInteger1:int = obj["UserInteger1"]
      """  UserInteger1  """  
      self.UserInteger2:int = obj["UserInteger2"]
      """  UserInteger2  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job header comments.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  """  
      self.InCopyList:bool = obj["InCopyList"]
      """  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  """  
      self.WIName:str = obj["WIName"]
      """   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Scheduled "What If" finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.Candidate:bool = obj["Candidate"]
      """   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  """  
      self.SchedCode:str = obj["SchedCode"]
      """  Scheduling Code.  SchedCode references a record in the SchedPri table.  """  
      self.SchedLocked:bool = obj["SchedLocked"]
      """  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the JobHead with a project in the Project table.  This can be blank.  """  
      self.WIPCleared:bool = obj["WIPCleared"]
      """  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  """  
      self.JobFirm:bool = obj["JobFirm"]
      """  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  """  
      self.PersonList:str = obj["PersonList"]
      """  A LIST-DELIM delimited list of people.  """  
      self.PersonID:str = obj["PersonID"]
      """   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  """  
      self.ProdTeamID:str = obj["ProdTeamID"]
      """  Production Team for the Job.  Associates the JobHead with a ProdTeam.  """  
      self.QtyCompleted:int = obj["QtyCompleted"]
      """   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.DatePurged:str = obj["DatePurged"]
      """  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  """  
      self.TravelerReadyToPrint:bool = obj["TravelerReadyToPrint"]
      """  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  """  
      self.TravelerLastPrinted:str = obj["TravelerLastPrinted"]
      """  The last date the job traveler was mass printed.  """  
      self.StatusReadyToPrint:bool = obj["StatusReadyToPrint"]
      """  Indicates if the Status can be printed. Print functions are not available if this is = No.  """  
      self.StatusLastPrinted:str = obj["StatusLastPrinted"]
      """  The last date the job status was mass printed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is linked to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is linked to.  """  
      self.JobType:str = obj["JobType"]
      """  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  """  
      self.RestoreFlag:str = obj["RestoreFlag"]
      """  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.LockQty:bool = obj["LockQty"]
      """  Indicates that the quantity on this job is locked  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this job.  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """   Values: S(Sequential) or C(Concurrent).
Defaults as S. Must have Advanced Production License to change. Controls how the operations and material requirements are developed. Concurrent jobs are used where the production time is based on the number of machine operations performed and not on the number of parts created. For example, a stamping operation where each cycle of the machine stamps out x number of parts. A further extension of this is that the operation can yield multiple different parts from each cycle of the machine.  Identification of these parts and there associated PPO (parts per operation) is define in the JobPart table.  """  
      self.PlannedActionDate:str = obj["PlannedActionDate"]
      """  The planned date when the job needs to be actioned by the production department to make sure that the job is ready on the planned completion date.  """  
      self.PlannedKitDate:str = obj["PlannedKitDate"]
      """  The date that the job needs to be ready for the warehouse to kit to make sure that it is ready for the job start date.  """  
      self.MSPTaskID:str = obj["MSPTaskID"]
      """  The task ID that is returned from Microsoft Project.  """  
      self.MSPPredecessor:str = obj["MSPPredecessor"]
      """  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back an alpha numeric string.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.ProductionYield:bool = obj["ProductionYield"]
      """  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  """  
      self.OrigProdQty:int = obj["OrigProdQty"]
      """  This field will be set to the value of the JobHead.ProdQty at the time the JobHead.Engineered flag is set to true.  """  
      self.PreserveOrigQtys:bool = obj["PreserveOrigQtys"]
      """  This field is used to indicate whether the original quantities should be reset in the job header and its assemblies at JobHead update if JobHead.JobEngineered has been changed from false to true. Generally the orig qtys will be reset, unless this flag is set to true because the user was asked if they wanted to reset the orig qtys and they answered yes.  """  
      self.NoAutoCompletion:bool = obj["NoAutoCompletion"]
      """  If set to yes then exclude this job from the Job Auto-Completion process. Not directly maintainable.  """  
      self.NoAutoClosing:bool = obj["NoAutoClosing"]
      """  No Auto Closing. If set to yes then exclude this job from the Job Auto-Closing process.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user that created this Job.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date that this Job was created.  """  
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      """  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of PDM parts.  """  
      self.ExportRequested:str = obj["ExportRequested"]
      """  This field is used to store a code that represents the external system that the Job is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  """  
      self.SplitMfgCostElements:bool = obj["SplitMfgCostElements"]
      """  Flag to indicate how to split the manufacturing cost elements when a manufactured material is issued to the job.  If flag is set to true, the cost of the issued material will be split into individual manufacturing cost elements. If set to false, the cost of the issued material is added to the manufacturing material cost element only.  This is defaulted from the JCSyst.SplitMfgCostElements and is not user maintainable.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Cross Reference Part Num. Used for alternate serial mask support.  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """   Cross Reference Part Type. Used for alternate serial mask support.

I=Internal Cross Reference / C = Customer Part  """  
      self.XRefCustNum:int = obj["XRefCustNum"]
      """  Customer Number XRefPartNum is related to if it is a customer part. Used for alternate serial number mask support.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  Base Part Number. Used in the configurator to identify the configurator part Number.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  """  
      self.RoughCutScheduled:bool = obj["RoughCutScheduled"]
      """  Indicates if the job was rough cut scheduled.  """  
      self.EquipID:str = obj["EquipID"]
      """   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  """  
      self.PlanNum:int = obj["PlanNum"]
      """   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  """  
      self.MaintPriority:str = obj["MaintPriority"]
      """  Maintenance Job Priority. Valid values: H - High, M - Medium, L - Low.  M is default or if created from a Maint Request then MaintReq.Priority is used as default.  """  
      self.SplitJob:bool = obj["SplitJob"]
      """  Internal field indicating this job was created by a job split.  Assigned true when a job has been split due to start minimum lot size quantity processing.  """  
      self.NumberSource:bool = obj["NumberSource"]
      """  Indicates the type of prefix which is used for create jobs in MRP  """  
      self.CloseMeterReading:int = obj["CloseMeterReading"]
      """  The Meter Reading value entered at time of Job Closing.  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  """  
      self.IssueTopicID2:str = obj["IssueTopicID2"]
      """  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  """  
      self.IssueTopicID3:str = obj["IssueTopicID3"]
      """  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  """  
      self.IssueTopicID4:str = obj["IssueTopicID4"]
      """  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  """  
      self.IssueTopicID5:str = obj["IssueTopicID5"]
      """  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  """  
      self.IssueTopicID6:str = obj["IssueTopicID6"]
      """  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  """  
      self.IssueTopicID7:str = obj["IssueTopicID7"]
      """  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  """  
      self.IssueTopicID8:str = obj["IssueTopicID8"]
      """  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  """  
      self.IssueTopicID9:str = obj["IssueTopicID9"]
      """  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  """  
      self.IssueTopicID10:str = obj["IssueTopicID10"]
      """  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  """  
      self.IssueTopics:str = obj["IssueTopics"]
      """  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  """  
      self.ResTopicID1:str = obj["ResTopicID1"]
      """  Maintenance Resolution Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  """  
      self.ResTopicID2:str = obj["ResTopicID2"]
      """  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  """  
      self.ResTopicID3:str = obj["ResTopicID3"]
      """  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  """  
      self.ResTopicID4:str = obj["ResTopicID4"]
      """  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  """  
      self.ResTopicID5:str = obj["ResTopicID5"]
      """  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  """  
      self.ResTopicID6:str = obj["ResTopicID6"]
      """  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  """  
      self.ResTopicID7:str = obj["ResTopicID7"]
      """  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  """  
      self.ResTopicID8:str = obj["ResTopicID8"]
      """  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  """  
      self.ResTopicID9:str = obj["ResTopicID9"]
      """  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  """  
      self.ResTopicID10:str = obj["ResTopicID10"]
      """  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  """  
      self.ResTopics:str = obj["ResTopics"]
      """  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  """  
      self.Forward:bool = obj["Forward"]
      """  It is updated by Calculate Global Scheduling Order process, it indicates if a job has to be scheduled Backwards or Forwards by Global Scheduling Process and it can be modified by Adjust Scheduling Global Order  """  
      self.SchedSeq:int = obj["SchedSeq"]
      """  This is the sequence number used to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  """  
      self.PAAExists:bool = obj["PAAExists"]
      """  Indicates if at least one subassembly contains a part that is plan as assembly.  It does not indicate if the assembly is marked as PAA - only that the part is PAA in the BOM.  Used in MRP when determining if a job can be reused.  """  
      self.DtlsWithinLeadTime:bool = obj["DtlsWithinLeadTime"]
      """  Indicates if the job structure (BOM) was created inside or outside of the mfg lead time for the job part.  Used in MRP when determining if a job can be reused.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.RoughCut:bool = obj["RoughCut"]
      """  It indicates that the shop load for that job was not generated (shopload table). The load in shopload can be recreated by Save Resource Load process  """  
      self.PlanGUID:str = obj["PlanGUID"]
      """  PlanGUID  """  
      self.PlanUserID:str = obj["PlanUserID"]
      """  PlanUserID  """  
      self.LastChangedBy:str = obj["LastChangedBy"]
      """  LastChangedBy  """  
      self.LastChangedOn:str = obj["LastChangedOn"]
      """  LastChangedOn  """  
      self.EPMExportLevel:int = obj["EPMExportLevel"]
      """  EPMExportLevel  """  
      self.JobWorkflowState:str = obj["JobWorkflowState"]
      """  JobWorkflowState  """  
      self.JobCSR:str = obj["JobCSR"]
      """  JobCSR  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LastExternalMESDate:str = obj["LastExternalMESDate"]
      """  LastExternalMESDate  """  
      self.LastScheduleDate:str = obj["LastScheduleDate"]
      """  LastScheduleDate  """  
      self.LastScheduleProc:str = obj["LastScheduleProc"]
      """  LastScheduleProc  """  
      self.SchedPriority:int = obj["SchedPriority"]
      """  Sequence priority used internally by Calculate Global Scheduling Order process to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  """  
      self.DaysLate:int = obj["DaysLate"]
      """  It indicates the days a job is going to be late in relation to its required due date  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process  """  
      self.SyncReqBy:bool = obj["SyncReqBy"]
      """  SyncReqBy  """  
      self.CustName:str = obj["CustName"]
      """  CustName  """  
      self.CustID:str = obj["CustID"]
      """  CustID  """  
      self.IsCSRSet:bool = obj["IsCSRSet"]
      """  IsCSRSet  """  
      self.UnReadyCostProcess:bool = obj["UnReadyCostProcess"]
      """  UnReadyCostProcess  """  
      self.ProcSuspendedUpdates:str = obj["ProcSuspendedUpdates"]
      """  ProcSuspendedUpdates  """  
      self.ProjProcessedDate:str = obj["ProjProcessedDate"]
      """  DateTime field to indicate when this record has been read by project analysis process  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.UseAdvancedStaging:bool = obj["UseAdvancedStaging"]
      """  Indicates if this revision is to use Advanced Staging.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PersonIDName:str = obj["PersonIDName"]
      """  PersonIDName  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the job is ready to be fulfilled.  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.FSMServiceReportID:str = obj["FSMServiceReportID"]
      """  FSMServiceReportID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcJobMtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobMtl records are also marked.  This is used to make database access to open material records more efficient.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """  Indicates if this material requirement has been issued complete.  If "yes" then this record is NOT part of the Part.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number that this material is associated with.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number.  If the material is being purchased (JobMtl.BuyIt = yes) this does need to be a valid part in the Part file.  """  
      self.Description:str = obj["Description"]
      """  A description of the material.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Quantity per parent.  Field Service was EstQty in FSCallMt.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  Required Quantity per END ITEM.  This is a calculated field.  Calculated as (Parent Required Qty X QtyPer) + calculated Scrap.  The parent quantity is either the JobHead.ProdQty if  JobMtl.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobMtl.AssemblySeq > 0.  """  
      self.IUM:str = obj["IUM"]
      """  Internal unit of measure.  The unit used to measure the material.  """  
      self.LeadTime:int = obj["LeadTime"]
      """   Expected purchasing lead time (in days).  This field is only valid if JobMtl.BuyIt = yes.  This can be used to calculate a suggested "Order By Date" based off the Required Date field.
When scheduling the job, purchased material can push a schedule out if the material lead time prevents the material from being available when the operation could start.  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   A material record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job.  The related operation is also used to calculate the JobMtl.ReqDate based on the operations scheduled start date and materials lead time.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this Job Material.  """  
      self.EstMtlBurUnitCost:int = obj["EstMtlBurUnitCost"]
      """  Estimated Material Burden Unit Cost of the material.  Defaults from the Part table if valid PartNum.  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  Estimated Unit Cost of the material.  Defaults from the Part table if valid PartNum.  """  
      self.IssuedQty:int = obj["IssuedQty"]
      """  This quantity is a summary of all Issue Transactions.  For FS this was FSCallMt.ActQty  """  
      self.TotalCost:int = obj["TotalCost"]
      """  Total cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  FS - was UnitCost in FSCallMt  """  
      self.MtlBurCost:int = obj["MtlBurCost"]
      """  Total Material Burden cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  """  
      self.ReqDate:str = obj["ReqDate"]
      """  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse that the material is allocated against.  """  
      self.SalvagePartNum:str = obj["SalvagePartNum"]
      """  Part number for salvageable scrap from this material record.  An optional field.  This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via salvage receipt process.  """  
      self.SalvageDescription:str = obj["SalvageDescription"]
      """  Description of Salvageable material.  Use Part.Description for a default.  """  
      self.SalvageQtyPer:int = obj["SalvageQtyPer"]
      """  A factor that multiplied by the JobMtl.RequiredQty results in the expected total salvage quantity.  """  
      self.SalvageUM:str = obj["SalvageUM"]
      """  Default unit of measure for the Salvaged Part.  Default from the Part.IUM.  """  
      self.SalvageMtlBurRate:int = obj["SalvageMtlBurRate"]
      """  The salvage material burden rate for this Job Material.  """  
      self.SalvageUnitCredit:int = obj["SalvageUnitCredit"]
      """  Estimated Salvage Unit Credit.  Use the appropriate cost from the Part master as a default.  """  
      self.SalvageEstMtlBurUnitCredit:int = obj["SalvageEstMtlBurUnitCredit"]
      """  Estimated Salvage Mtl burden Unit Credit.  Use the appropriate cost from the Part master as a default.  """  
      self.SalvageQtyToDate:int = obj["SalvageQtyToDate"]
      """  This quantity is a summary of all transactions for receipt of salvage to inventory.  This is not directly maintainable.  """  
      self.SalvageCredit:int = obj["SalvageCredit"]
      """  Total salvage credit to date.  A summary of salvage receipt transactions.  """  
      self.SalvageMtlBurCredit:int = obj["SalvageMtlBurCredit"]
      """  Total salvage Mtl Burden credit to date.  A summary of salvage receipt transactions.  """  
      self.MfgComment:str = obj["MfgComment"]
      """   Comments for manufacturing about this material record.  These comments are printed on manufacturing reports, such as the router.  For valid Parts use the Part.MfgComment as a default.
View as editor widget.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Used to identify a default vendor.  Use the Part.VendorNum as a default.  This will be used as a default for purchasing and miscellaneous receipts.  This field is not directly maintainable, instead its assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by selection list processing.  An optional field, but if entered must be valid.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default purchase point defined in the Vendor file.  """  
      self.BuyIt:bool = obj["BuyIt"]
      """  Indicates if this material is to be purchased for the Job.  If this is a non inventory part then this is "Yes" and cannot be changed.  If this is a valid Part then set it to "NO" but the user can override it. Material that is marked to be purchased (BuyIt = Yes) are NOT included in the PartWhse.AllocatedQty.  """  
      self.Ordered:bool = obj["Ordered"]
      """  FUTURE IMPLEMENTATION.  This logical relates to material that is flagged to be purchased (BuyIt = Yes).  When purchase orders are created for this job material requirement this flag is set to Yes indicating that a purchase order has been placed.  The idea would be to use this within purchasing to quickly see the "direct job requirements" where no purchase orders have been placed.  """  
      self.PurComment:str = obj["PurComment"]
      """   Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.
View as editor widget.  """  
      self.BackFlush:bool = obj["BackFlush"]
      """   Indicates if this material will be backflushed.
Note: this field is defaulted from Part.BackFlush
Backflushing occurs via the write trigger on LaborDtl.  The basic idea is to issue material based on the labor quantities reported. The formula for the issue quantity is: (JobMtl.RequiredQty/JobOper.RunQty) * (LaborDtl.LaborQty + LaborDtl.SrapQty).  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the EstScrapQty entry as being a fixed quantity or a percentage of required quantity.  """  
      self.FixedQty:bool = obj["FixedQty"]
      """  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  """  
      self.FindNum:str = obj["FindNum"]
      """  Characters used on the drawing to show where material is used.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.SndAlrtCmpl:bool = obj["SndAlrtCmpl"]
      """  Controls if an alert is to be sent when this JobMtl is completed.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if inspection is required when items are received to this JobMtl.  Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Direct:bool = obj["Direct"]
      """  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified.  """  
      self.MaterialMtlCost:int = obj["MaterialMtlCost"]
      """  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  """  
      self.MaterialLabCost:int = obj["MaterialLabCost"]
      """  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.MaterialSubCost:int = obj["MaterialSubCost"]
      """  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.MaterialBurCost:int = obj["MaterialBurCost"]
      """  Total Bur cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  """  
      self.SalvageMtlCredit:int = obj["SalvageMtlCredit"]
      """  Total salvage Mtl credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.SalvageLbrCredit:int = obj["SalvageLbrCredit"]
      """  Total salvage Lbr credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.SalvageBurCredit:int = obj["SalvageBurCredit"]
      """  Total salvage Burden credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.SalvageSubCredit:int = obj["SalvageSubCredit"]
      """  Total salvage Subcontract credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  """  
      self.APSAddResType:str = obj["APSAddResType"]
      """   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this Material belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this material relates to.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  FS - Unit Price for the Material in base currency.  """  
      self.BillableUnitPrice:int = obj["BillableUnitPrice"]
      """  FS - Billable Unit Price for the Material in base currency.  """  
      self.DocBillableUnitPrice:int = obj["DocBillableUnitPrice"]
      """  FS - Billable Price per unit for the material in customers currency.  """  
      self.ResReasonCode:str = obj["ResReasonCode"]
      """  Problem reason code from the reason master table. type Service call.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  """  
      self.Billable:bool = obj["Billable"]
      """  Is this a billable material item.  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """  Holds the quantity of the item that has been shipped through misc.  shipments  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  FS - Unit Price for the Material in Customer currency.  """  
      self.QtyStagedToDate:int = obj["QtyStagedToDate"]
      """  The todate quantity that has been moved to the work centers input Warehouse/Bin.  This is NOT A balance.  It is a todate value. It is not reduced as it is consumed. Used in calculation of "Outstanding" material in the Request Material program (ame30-dg.w). Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the material in/out of the staging area(Issues,Returns).  """  
      self.AddedMtl:bool = obj["AddedMtl"]
      """  This material was added after initial setup of the job  """  
      self.MiscCharge:bool = obj["MiscCharge"]
      """  This indicates that this JobMtl record is for a Misc charge related to this job/assembly.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.   It must be a AP Misc. charge.  """  
      self.SCMiscCode:str = obj["SCMiscCode"]
      """  The Miscellaneous Charge Code for Service Call billing. This must be valid in the MiscChrg master file.   It must be a AR Misc. charge.  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this job material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this job material.  Can be zero if RFQ(s) are not required.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQ number that the item is linked to.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.RFQStat:str = obj["RFQStat"]
      """   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.GlbRFQ:bool = obj["GlbRFQ"]
      """  Global RFQ flag.  Used in Consolidated Purchasing.  """  
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      """  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  """  
      self.WIReqDate:str = obj["WIReqDate"]
      """  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  """  
      self.Rpt1BillableUnitPrice:int = obj["Rpt1BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2BillableUnitPrice:int = obj["Rpt2BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3BillableUnitPrice:int = obj["Rpt3BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.BaseRequiredQty:int = obj["BaseRequiredQty"]
      """   Required Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the JobMtl.RequiredQty which is in the UOM of the requirement to the JobMtl.BaseUOM which is the UOM of the Part and it's unit costs.
This quantity multiplied by the JobMtl.EstMtlUnitCost is used to update the total estimated costs found in JobAsmbl.TLEMaterialCost  """  
      self.BaseUOM:str = obj["BaseUOM"]
      """   Unit of Measure of the JobMtl.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as JobMtl.IUM  """  
      self.Weight:int = obj["Weight"]
      """  Material Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Material Weight UOM defaulted from Part Master.  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  Base Part Number. Used in the configurator to identify the configurator part Number.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  """  
      self.SelectForPicking:bool = obj["SelectForPicking"]
      """  Indicates if the job material is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  """  
      self.StagingWarehouseCode:str = obj["StagingWarehouseCode"]
      """  The job pick "Staging" warehouse for the job material.  Defaults from the system default warehouse (PlantConfCtrl.DefJobPickWhse).  """  
      self.StagingBinNum:str = obj["StagingBinNum"]
      """  The job pick "Staging" bin for the job material.  Defaults from the system default bin (PlantConfCtrl.DefJobPickBin).  """  
      self.PickError:str = obj["PickError"]
      """   A non blank character indicates that the release could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  """  
      self.EstMtlUnitCost:int = obj["EstMtlUnitCost"]
      """   Estimated Material Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.EstLbrUnitCost:int = obj["EstLbrUnitCost"]
      """   Estimated Labor Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.EstBurUnitCost:int = obj["EstBurUnitCost"]
      """   Estimated Burden Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.EstSubUnitCost:int = obj["EstSubUnitCost"]
      """   Estimated Subcontract Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  """  
      self.SalvageEstMtlUnitCredit:int = obj["SalvageEstMtlUnitCredit"]
      """   Estimated Salvage Material Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.SalvageEstLbrUnitCredit:int = obj["SalvageEstLbrUnitCredit"]
      """   Estimated Salvage Labor Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.SalvageEstBurUnitCredit:int = obj["SalvageEstBurUnitCredit"]
      """   Estimated Salvage Burden Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.SalvageEstSubUnitCredit:int = obj["SalvageEstSubUnitCredit"]
      """   Estimated Salvage Subcontract Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  """  
      self.LoanedQty:int = obj["LoanedQty"]
      """  The material quantity that has been loaned out to another job.  """  
      self.BorrowedQty:int = obj["BorrowedQty"]
      """  The material quantity that has been borrowed from another job.  """  
      self.ReassignSNAsm:bool = obj["ReassignSNAsm"]
      """  flag used to designate if the serial numbers from the job material/subassembly can be reassigned as the serial number of the parent assembly (top assembly or n deep subassembly) being reworked using a job.  """  
      self.GeneralPlanInfo:str = obj["GeneralPlanInfo"]
      """  GeneralPlanInfo  """  
      self.EstStdDescription:str = obj["EstStdDescription"]
      """  EstStdDescription  """  
      self.PricingUOM:str = obj["PricingUOM"]
      """  PricingUOM  """  
      self.RemovedFromPlan:bool = obj["RemovedFromPlan"]
      """  RemovedFromPlan  """  
      self.IsPOCostingMaintained:bool = obj["IsPOCostingMaintained"]
      """  IsPOCostingMaintained  """  
      self.EstStdType:int = obj["EstStdType"]
      """  EstStdType  """  
      self.POCostingFactor:int = obj["POCostingFactor"]
      """  POCostingFactor  """  
      self.PlannedQtyPerUnit:int = obj["PlannedQtyPerUnit"]
      """  PlannedQtyPerUnit  """  
      self.POCostingDirection:int = obj["POCostingDirection"]
      """  POCostingDirection  """  
      self.POCostingUnitVal:int = obj["POCostingUnitVal"]
      """  POCostingUnitVal  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OrigStructTag:str = obj["OrigStructTag"]
      """  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  """  
      self.OrigGroupSeq:int = obj["OrigGroupSeq"]
      """  By storing the original Group Sequence of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  """  
      self.ShowStatusIcon:str = obj["ShowStatusIcon"]
      """  ShowStatusIcon  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  """  
      self.StagingLotNum:str = obj["StagingLotNum"]
      """  Stores the lot number of the material in the Staging Warehouse/Bin.  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.LocationView:bool = obj["LocationView"]
      """  Controls if this material record is viewable in Location Management or the web.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.SalvageAttributeSetID:int = obj["SalvageAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SalvagePlanningNumberOfPieces:int = obj["SalvagePlanningNumberOfPieces"]
      """  Salvage planning number of pieces for this attribute set.  """  
      self.SalvagePlanningAttributeSetID:int = obj["SalvagePlanningAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.RelatedStage:str = obj["RelatedStage"]
      """  The identification of related StageNo.  """  
      self.SalvageRevisionNum:str = obj["SalvageRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.PartAllocQueueAction:str = obj["PartAllocQueueAction"]
      """  Indicates if the job material should be added or removed from the fulfillment queue.  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the job material is ready to be fulfilled.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcJobOpDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  Associates the record back to the JobHead.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  Assigned by the system.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the JobOper record within the JobAsmbl.   System assigned.  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  Uniquely identifies an OpDtl.  System assigned.  """  
      self.SetupOrProd:str = obj["SetupOrProd"]
      """  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "S", indicating the resource is RequiredFor the Setup phase of this operation, "P" for Production phase, or "B" meaning Both setup and production phase.  """  
      self.CapabilityID:str = obj["CapabilityID"]
      """  The user can select the capability the operation is to perform.  The system will select the resource.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  The user can select a Resource Group for the operation to be performed on.  The system will select the actual resource.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource for this operation to be performed on.  If a resource was not explicitly assigned this field is blank.  """  
      self.ConcurrentCapacity:int = obj["ConcurrentCapacity"]
      """  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  """  
      self.DailyProdRate:int = obj["DailyProdRate"]
      """  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  """  
      self.NumResources:int = obj["NumResources"]
      """  This is the number of resources the operation can run on.  If multiple resources can perform the required Capability, then up to this many will be employed.  This determines the number of setups the system will allow for the operation.  However, the number of setups cannot exceed the number of operations.  The idea being that once a part is on a machine you will complete the operation on that resource.  """  
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
      self.ProdLabRate:int = obj["ProdLabRate"]
      """  Labor rate used for estimated production labor costs. Default from the OpMasDtl.ProdLabRate.  """  
      self.SetupLabRate:int = obj["SetupLabRate"]
      """  Labor rate for estimated setup labor costs. Default from the OpMaster.SetupLabRate.  """  
      self.ProdBurRate:int = obj["ProdBurRate"]
      """  The burden rate to be used for the production time on this operation. (EstProdHrs X ProdBurRate). Default from the WrkCenter.ProdBurRate.  """  
      self.SetupBurRate:int = obj["SetupBurRate"]
      """  The burden rate to be used for the Setup time on this operation. (EstSetHours X ProdBurRate). Default from the WrkCenter.SetupBurRate.  """  
      self.ProdComplete:bool = obj["ProdComplete"]
      """  A flag indicating if the production is complete for this operation. It is updated via Labor Entry.  """  
      self.SetupComplete:bool = obj["SetupComplete"]
      """  Flag that indicates if Setup is complete on this operation. This flag is only used when the operation has EstSetupHours > 0.00.  """  
      self.ActProdHours:int = obj["ActProdHours"]
      """  Total Actual Production Hours. A summary of non-setup LaborDtl.BurdenHrs. This includes REWORK hours.  This is maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActReworkHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H").  """  
      self.ActProdRwkHours:int = obj["ActProdRwkHours"]
      """  Total Actual Production Rework  Hours. A summary of rework labor transactions (LaborDtl.BurdenHrs) where LaborDtl.LaborType = "P" and Rework = Yes. This number is also included as part of the JobOPer.ActProdHours.  Maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActProdHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H"). (See the lib/inopload.i code for load remaining logic)  """  
      self.ActSetupHours:int = obj["ActSetupHours"]
      """  Actual setup hours.  A summary of setup (LaborDtl.LaborType = S) labor transactions hours (LaborDtl.Burden). Actual Setup hours reduce the shop load if the system is configured to remove load based on hours (JCSyst.RemoveLoad = "H").  """  
      self.ActSetupRwkHours:int = obj["ActSetupRwkHours"]
      """  Total Actual Setup Rework  Hours. A summary of rework labor transactions (LaborDtl.BurdenHrs) where LaborDtl.LaborType = "S" and Rework = Yes. This number is also included as part of the JobOPer.ActSetupHours.  Maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActSetHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H"). (See the lib/inopload.i code for load remaining logic)  """  
      self.SetupPctComplete:int = obj["SetupPctComplete"]
      """  Setup function percent complete.  Maintained via labor entry.  """  
      self.ActBurCost:int = obj["ActBurCost"]
      """  Total Burden cost to date. This is update via the LaborDtl\Write.p trigger procedure. It includes ALL burden costs (Setup, Production and Rework)  """  
      self.ActLabCost:int = obj["ActLabCost"]
      """   Total of ALL labor costs to date. This includes Setup, Production and Rework. Updated via the LaborDtl.Write.p trigger.
The Total Cost, updated via the receipt process.  """  
      self.ReworkBurCost:int = obj["ReworkBurCost"]
      """  Total Rework Burden cost todate. This value is also included in the ActBurCost total. It includes both setup & production rework. Updated via LaborDtl\Write.P trigger.  """  
      self.ReworkLabCost:int = obj["ReworkLabCost"]
      """  Total Rework Labor cost to date. This value is also included in the ActLabCost field. This includes both Setup and Production. Updated via the LaborDtl\Write.p trigger.  """  
      self.ResourceLock:bool = obj["ResourceLock"]
      """  Resource Lock.  If the user explicitly selected a Resource for the JobOpDtl, when they accept the scheduling changes, the WISchedResource will be stored as the explicit Resource.  Else the WISchedResource will become the SchedResource and the WISchedResourceGrp will become the ResourceGroup.  """  
      self.SysCreateDate:str = obj["SysCreateDate"]
      """  System maintained.  Date the JobOpDtl record was added to the database.  """  
      self.SysCreateTime:int = obj["SysCreateTime"]
      """  Time in seconds since midnight that the system created the record.  """  
      self.OpDtlDesc:str = obj["OpDtlDesc"]
      """  Description is initially created when the JobOpDtl is created.   If the JobOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  """  
      self.EstSetHoursPerMch:int = obj["EstSetHoursPerMch"]
      """   The estimated set up hours per machine.
Default from OpStd.SetupHours.  Used to calculate JobOper.EstSetupHours.  """  
      self.OverrideRates:bool = obj["OverrideRates"]
      """  If yes then the user has overridden the rates that were on the  record when it was inititally created.  The initial rates came from the master files.  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Duplicated from JobOper.SetupCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Duplicated from JobOper.SetupCrewSize. Its the number of people it physically takes to setup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.RemovedFromPlan:bool = obj["RemovedFromPlan"]
      """  RemovedFromPlan  """  
      self.IsPrimaryProd:bool = obj["IsPrimaryProd"]
      """  IsPrimaryProd  """  
      self.IsPrimarySetup:bool = obj["IsPrimarySetup"]
      """  IsPrimarySetup  """  
      self.AutoSystemAdded:bool = obj["AutoSystemAdded"]
      """  AutoSystemAdded  """  
      self.MobileAllocatedResource:bool = obj["MobileAllocatedResource"]
      """  MobileAllocatedResource  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcJobOperRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobOper records are also marked.  This is used to make database access to open operation records more efficient.  """  
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
      self.OpCode:str = obj["OpCode"]
      """  Operation Master Code - Links the JobOper  record with a OpMaster record.  Default is given from WrkCenter.OpCode.  Must be valid in the OpMaster file.  """  
      self.OpStdID:str = obj["OpStdID"]
      """   The Operation standard ID.  This links the JobOper to the OpStd master file.  This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.
Valid for "inside operations" only.  """  
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
      self.QueStartDate:str = obj["QueStartDate"]
      """  Scheduled queue start date. Not directly maintainable, updated via the scheduling process.  """  
      self.QueStartHour:int = obj["QueStartHour"]
      """  Scheduled queue start hour offset from the beginning of the work day.  This field is established by scheduling.  """  
      self.StartDate:str = obj["StartDate"]
      """  Scheduled production start date. Not directly maintainable, updated via the scheduling process.  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  """  
      self.DueDate:str = obj["DueDate"]
      """  Scheduled production due date. Not directly maintainable, updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  """  
      self.MoveDueDate:str = obj["MoveDueDate"]
      """  Scheduled move due date. Not directly maintainable, updated via the scheduling process.  """  
      self.MoveDueHour:int = obj["MoveDueHour"]
      """  Scheduled move due hour offset from the beginning of the work day.  This field is established by scheduling.  """  
      self.ProdLabRate:int = obj["ProdLabRate"]
      """  Labor rate used for estimated production labor costs. Default from the OpMaster.ProdLabRate.  """  
      self.SetupLabRate:int = obj["SetupLabRate"]
      """  Labor rate for estimated setup labor costs. Default from the OpMaster.SetupLabRate.  """  
      self.ProdBurRate:int = obj["ProdBurRate"]
      """  The burden rate to be used for the production time on this operation. (EstProdHrs X ProdBurRate). Default from the WrkCenter.ProdBurRate.  """  
      self.SetupBurRate:int = obj["SetupBurRate"]
      """  The burden rate to be used for the Setup time on this operation. (EstSetHours X ProdBurRate). Default from the WrkCenter.SetupBurRate.  """  
      self.AddedOper:bool = obj["AddedOper"]
      """  This indicates if this is an "added operation". An added operation is one that was not planned on.  """  
      self.Machines:int = obj["Machines"]
      """  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to setup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  """  
      self.ProdComplete:bool = obj["ProdComplete"]
      """  A flag indicating if the production is complete for this operation. It is updated via Labor Entry.  """  
      self.SetupComplete:bool = obj["SetupComplete"]
      """  Flag that indicates if Setup is complete on this operation. This flag is only used when the operation has EstSetupHours > 0.00.  """  
      self.ActProdHours:int = obj["ActProdHours"]
      """  Total Actual Production Hours. A summary of non-setup LaborDtl.BurdenHrs. This includes REWORK hours.  This is maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActReworkHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H").  """  
      self.ActProdRwkHours:int = obj["ActProdRwkHours"]
      """  Total Actual Production Rework  Hours. A summary of rework labor transactions (LaborDtl.BurdenHrs) where LaborDtl.LaborType = "P" and Rework = Yes. This number is also included as part of the JobOPer.ActProdHours.  Maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActProdHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H"). (See the lib/inopload.i code for load remaining logic)  """  
      self.ActSetupHours:int = obj["ActSetupHours"]
      """  Actual setup hours.  A summary of setup (LaborDtl.LaborType = S) labor transactions hours (LaborDtl.Burden). Actual Setup hours reduce the shop load if the system is configured to remove load based on hours (JCSyst.RemoveLoad = "H").  """  
      self.ActSetupRwkHours:int = obj["ActSetupRwkHours"]
      """  Total Actual Setup Rework  Hours. A summary of rework labor transactions (LaborDtl.BurdenHrs) where LaborDtl.LaborType = "S" and Rework = Yes. This number is also included as part of the JobOPer.ActSetupHours.  Maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActSetHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H"). (See the lib/inopload.i code for load remaining logic)  """  
      self.QtyCompleted:int = obj["QtyCompleted"]
      """   For Non Subcontract operations: A summary of labor transaction detail. (LaborDtl.LaborQty). Labor entry/collection maintains this field.  Only the LaborQty for transactions that are Production labor ( LaborType = P ) and Not rework (LaborDtl.Rework = No) are included in this summary.
This quantity is used to reduce shop load when the system is configured to reduce load based on quantity completed. (JCSyst.RemoveLoad = Q)
For Subcontract Operations this field is updated by the Purchased Receipt process. The detail records are in the PartTran file.  """  
      self.SetupPctComplete:int = obj["SetupPctComplete"]
      """  Setup function percent complete.  Maintained via labor entry.  """  
      self.EstScrap:int = obj["EstScrap"]
      """  EstScrap =  a number representing either a scrap qty or a scrap percent depending on the value of EstScrapType field.  """  
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
      self.PartNum:str = obj["PartNum"]
      """  The PartNum to be shipped to the subcontract. Default the JobHead.PartNum or JobAsmbl.PartNum depending on the JobMtl.AssemblySeq.  """  
      self.Description:str = obj["Description"]
      """  Description used only for subcontract operations  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job operation comments.  """  
      self.SchedRelation:str = obj["SchedRelation"]
      """   Indicates the scheduling relationship between this and the preceding  operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  """  
      self.RunQty:int = obj["RunQty"]
      """   The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0.
This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  """  
      self.WIName:str = obj["WIName"]
      """   This field is blank or contains the UserID. When not blank it indicates that the operations schedule has been changed and is considered as being in a "What If" mode.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  """  
      self.WIMachines:int = obj["WIMachines"]
      """  This is the What-If number of machines that this operation will run on at the same time.  Setup by and for scheduling from the Machines field.  """  
      self.WIQueStartDate:str = obj["WIQueStartDate"]
      """  What-if Scheduled queue start date. Not directly maintainable, updated via the scheduling process.  """  
      self.WIQueStartHour:int = obj["WIQueStartHour"]
      """  What-if Scheduled queue start hour offset from the beginning of the work day.  This field is established by scheduling.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  What if Scheduled production start date. Not directly maintainable, updated via the scheduling process.  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling. It represents the What If "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  What If Scheduled production due date. Not directly maintainable, updated via the scheduling process.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  """  
      self.WIMoveDueDate:str = obj["WIMoveDueDate"]
      """  What-If Scheduled move due date. Not directly maintainable, updated via the scheduling process.  """  
      self.WIMoveDueHour:int = obj["WIMoveDueHour"]
      """  What-if Scheduled move due hour offset from the beginning of the work day.  This field is established by scheduling.  """  
      self.WIHoursPerMachine:int = obj["WIHoursPerMachine"]
      """  The Number of Hours per machine per day that this operations "What If" schedule is based on.  This is for "Inbetween" days, not first or last days.  It is a copy of WrkCenter.HoursPerMachine field at the time of scheduling.  Used in logic of maintaining ShopLoad records.  """  
      self.WILoadDate:str = obj["WILoadDate"]
      """  Date at which the operations current outstanding "What-If" load starts at.  Updated by the JobOper write trigger. (See LoadDate)  """  
      self.WILoadHour:int = obj["WILoadHour"]
      """  "Hour offset from the beginning of the work day" for the operations outstanding "What-If"  load. Related to WILoadDate.  """  
      self.ActBurCost:int = obj["ActBurCost"]
      """  Total Burden cost to date. This is update via the LaborDtl\Write.p trigger procedure. It includes ALL burden costs (Setup, Production and Rework)  """  
      self.ActLabCost:int = obj["ActLabCost"]
      """   FOR NON-SUBCONTRACT OPERATIONS: Total of "ALL" labor costs to date. This includes Setup, Production and Rework. Updated via the LaborDtl.Write.p trigger.
FOR SUBCONTRACT OPERATIONS: The Total Cost, updated via the receipt process.  """  
      self.ReworkBurCost:int = obj["ReworkBurCost"]
      """  Total Rework Burden cost todate. This value is also included in the ActBurCost total. It includes both setup & production rework. Updated via LaborDtl\Write.P trigger.  """  
      self.ReworkLabCost:int = obj["ReworkLabCost"]
      """  Total Rework Labor cost to date. This value is also included in the ActLabCost field. This includes both Setup & Production. Updated via the LaborDtl\Write.p trigger.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...).
Defaulted from VendPart.MiscAmt. This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  """  
      self.HoursPerMachine:int = obj["HoursPerMachine"]
      """  The Number of Hours per machine per day that this operations "actual" schedule is based on.  This is for "Inbetween" days, not first or last days.  It is a copy of WrkCenter.HoursPerMachine field at the time of scheduling.  Used in logic of maintaining the ShopLoad records.  """  
      self.LoadDate:str = obj["LoadDate"]
      """   Date at which the operations current outstanding load starts at.
Ex: Op schedule is 2/1/97 - 2/10/97, initially LoadDate = 2/1/97. As load is relieved through labor processing the LoadDate moves forward accordingly. When 1/2 completed the LoadDate would be 2/5/97. This field is primarily used by the Scheduling Board to calculate the graphical image of outstanding load.  Updated by the JobOper write trigger.  """  
      self.LoadHour:int = obj["LoadHour"]
      """  "Hour offset from the beginning of the work day" for the operations outstanding load. Related to LoadDate.  """  
      self.ReloadNum:int = obj["ReloadNum"]
      """  Internally used field to prevent redundant read of JobOper during execution of "Reloader" program. (See WrkCenter.ReloadNum)  """  
      self.SndAlrtCmpl:bool = obj["SndAlrtCmpl"]
      """  Controls if an alert is to be sent when this JobOper is completed.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required when items are received to this JobOper (subcontract only). Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  """  
      self.JobEngineered:bool = obj["JobEngineered"]
      """  Identical to JobHead.JobEngineered.  ShopLoad capacity is only allocated to Jobs where JobEngineered = YES.  """  
      self.EstSetHoursPerMch:int = obj["EstSetHoursPerMch"]
      """   The estimated set up hours per machine.
Default from OpStd.SetupHours.  Used to calculate JobOper.EstSetupHours.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """   Part Revision number.
Pertains to subcontracting operations only.   An optional field.   Related JobAsmbl.RevisionNum is used as the default.  """  
      self.AutoReceiptDate:str = obj["AutoReceiptDate"]
      """  Currently not used. Prep for future development.  """  
      self.LastLaborDate:str = obj["LastLaborDate"]
      """  The labor date of the last labor transaction that was posted to this operation.  Used by the JobOper write trigger Auto Receieve logic.  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this operation belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this operation relates to.  """  
      self.LaborRate:int = obj["LaborRate"]
      """  Labor rate used for  time on an operation.  Time per hour per technician. in base currency.  """  
      self.BillableLaborRate:int = obj["BillableLaborRate"]
      """  Billable Labor rate used for  time on a service.  Time per hour per technician. in base currency. This field considers the percentage coverage of a warranty or contract.  """  
      self.DocLaborRate:int = obj["DocLaborRate"]
      """  Labor rate used for  time on a service.  Time per hour per technician. In Customer currency. Does not consider warranty or contract  """  
      self.DocBillableLaborRate:int = obj["DocBillableLaborRate"]
      """  Billable Labor rate used for  time on a service.  Time per hour per technician. In Customer currency. considers warranty or contract  """  
      self.Billable:bool = obj["Billable"]
      """  FS - Is this a billable operation.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  FS - Unit Price for the subcontract in base currency.  """  
      self.BillableUnitPrice:int = obj["BillableUnitPrice"]
      """  FS - Billable Unit Price for the subcontract in base currency.  """  
      self.DocBillableUnitPrice:int = obj["DocBillableUnitPrice"]
      """  FS - Billable Price per unit for the subcontract in customers currency.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  FS - Unit Price for the for the Subcontract in Customer currency.  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  """  
      self.FAQty:int = obj["FAQty"]
      """  The quantity requested for first article inspection.  """  
      self.QtyStagedToDate:int = obj["QtyStagedToDate"]
      """  The "to date" quantity that has been moved to the input Warehouse/Bin of the subsequent operations ResourceGroup/Resource input Warehouse/Bin.  This is NOT A balance.  It is a "to date" value.  It is not reduced as it is consumed.  Used in calculation of "Outstanding" WIP in the Request Material/WIP program (ame30-dg.w).  Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the WIP material in/out of the staging area (Issues, Returns).  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this job operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this job subcontract operation.  Can be zero if RFQ(s) are not required.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQ number that the item is linked to.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.RFQStat:str = obj["RFQStat"]
      """   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  """  
      self.SetupGroup:str = obj["SetupGroup"]
      """  Used to group operation to save on setups.  """  
      self.RestoreFlag:str = obj["RestoreFlag"]
      """  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PrimarySetupOpDtl:int = obj["PrimarySetupOpDtl"]
      """   Identifies the primary JobOpDtl to be used for setup.  The setup time for the operation is determined on the JobOpDtl.
If <> 0, must identify a valid JobOpDtl.  The JobOpDtl needs to have a RequiredFor = S or B.  """  
      self.PrimaryProdOpDtl:int = obj["PrimaryProdOpDtl"]
      """   Identifies the primary JobOpDtl to be used for production.  The production run time for the operation is determined on the JobOpDtl.
If <> 0, must identify a valid JobOpDtl.  The JobOpDtl needs to have a RequiredFor = P or B.  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Operation Description.  """  
      self.KitDate:str = obj["KitDate"]
      """  Kit Date. Not directly maintanable. Updated via the scheduling process.  """  
      self.GlbRFQ:bool = obj["GlbRFQ"]
      """  Global RFQ flag.  Used in Consolidated Purchasing.  """  
      self.BookedUnitCost:int = obj["BookedUnitCost"]
      """  Booked Unit Cost  """  
      self.RecalcExpProdYld:bool = obj["RecalcExpProdYld"]
      """   Initially defaulted to false. This flag is set to true at the time JobOper.ProdComplete is set to true if JobHead.ProductionYield = true and OpMaster. PrdYldRecalcExpected = true and the actual completed qty for the operation vs. the expected completion qty is out of variance based on the under percentage set in OpMaster. This flag is used by the production yield recalculation logic to determine if recalculation is required for a job.
This field is maintained by the system only.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.RoughCutSched:bool = obj["RoughCutSched"]
      """  When true this would signify that this operation was rough cut scheduled - meaning the operation would have start and end dates but no supporting resourcetimeused or shopload records.  """  
      self.SchedComment:str = obj["SchedComment"]
      """  Scheduling Comments  """  
      self.Rpt1BillableLaborRate:int = obj["Rpt1BillableLaborRate"]
      """  Reporting currency value of this field  """  
      self.Rpt2BillableLaborRate:int = obj["Rpt2BillableLaborRate"]
      """  Reporting currency value of this field  """  
      self.Rpt3BillableLaborRate:int = obj["Rpt3BillableLaborRate"]
      """  Reporting currency value of this field  """  
      self.Rpt1BillableUnitPrice:int = obj["Rpt1BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2BillableUnitPrice:int = obj["Rpt2BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3BillableUnitPrice:int = obj["Rpt3BillableUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1LaborRate:int = obj["Rpt1LaborRate"]
      """  Reporting currency value of this field  """  
      self.Rpt2LaborRate:int = obj["Rpt2LaborRate"]
      """  Reporting currency value of this field  """  
      self.Rpt3LaborRate:int = obj["Rpt3LaborRate"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
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
      self.TearDwnEndDate:str = obj["TearDwnEndDate"]
      """  Scheduled tear down start date. The start date would be the production end date.  """  
      self.TearDwnEndHour:int = obj["TearDwnEndHour"]
      """  Scheduled tear down due hour offset from the end of the prodution time.  This field is established by scheduling.  """  
      self.WITearDwnEndDate:str = obj["WITearDwnEndDate"]
      """  Scheduled tear down start date. The start date would be the production end date.  """  
      self.WITearDwnEndHour:int = obj["WITearDwnEndHour"]
      """  Scheduled tear down due hour offset from the end of the prodution time.  This field is established by scheduling.  """  
      self.UseAllRoles:bool = obj["UseAllRoles"]
      self.AssetPartNum:str = obj["AssetPartNum"]
      """  The PartNum for the asset. This should be disabled for a service call job, in which case the asset information would be transferred from the service call line when an operation is created for the job.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number of the asset.  """  
      self.ActualStartDate:str = obj["ActualStartDate"]
      """  ActualStartDate  """  
      self.ActualStartHour:int = obj["ActualStartHour"]
      """  ActualStartHour  """  
      self.ActualEndDate:str = obj["ActualEndDate"]
      """  ActualEndDate  """  
      self.ActualEndHour:int = obj["ActualEndHour"]
      """  ActualEndHour  """  
      self.FSJobStatus:int = obj["FSJobStatus"]
      """  FSJobStatus  """  
      self.Instructions:str = obj["Instructions"]
      """  Instructions  """  
      self.ProdUOM:str = obj["ProdUOM"]
      """  ProdUOM  """  
      self.GeneralPlanInfo:str = obj["GeneralPlanInfo"]
      """  GeneralPlanInfo  """  
      self.EstStdDescription:str = obj["EstStdDescription"]
      """  EstStdDescription  """  
      self.JDFOpCompleted:bool = obj["JDFOpCompleted"]
      """  JDFOpCompleted  """  
      self.RemovedfromPlan:bool = obj["RemovedfromPlan"]
      """  RemovedfromPlan  """  
      self.EstStdType:int = obj["EstStdType"]
      """  EstStdType  """  
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
      self.MobileOperation:bool = obj["MobileOperation"]
      """  MobileOperation  """  
      self.ReWork:bool = obj["ReWork"]
      """  ReWork  """  
      self.RequestMove:bool = obj["RequestMove"]
      """  RequestMove  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.PrinterID:str = obj["PrinterID"]
      """  PrinterID  """  
      self.LastPrintedDate:str = obj["LastPrintedDate"]
      """  LastPrintedDate  """  
      self.LastPCIDPrinted:str = obj["LastPCIDPrinted"]
      """  LastPCIDPrinted  """  
      self.CurrentPkgCode:str = obj["CurrentPkgCode"]
      """  CurrentPkgCode  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.StageNumber:str = obj["StageNumber"]
      """  The identification of related StageNo.  """  
      self.TemplateID:str = obj["TemplateID"]
      """  TemplateID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcKitCompResultRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.HasRuleSet:bool = obj["HasRuleSet"]
      self.IsKept:bool = obj["IsKept"]
      self.ParentRuleTag:str = obj["ParentRuleTag"]
      self.PartNum:str = obj["PartNum"]
      """  Part Number  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote Line  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote Number  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number  """  
      self.RuleTag:str = obj["RuleTag"]
      self.TestType:str = obj["TestType"]
      """  Test Type  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcMtlResultRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TestType:str = obj["TestType"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.ParentAsmSeq:int = obj["ParentAsmSeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.MtlType:str = obj["MtlType"]
      self.PartNum:str = obj["PartNum"]
      self.RuleTag:str = obj["RuleTag"]
      self.Description:str = obj["Description"]
      self.ParentRuleTag:str = obj["ParentRuleTag"]
      self.AsmPartNum:str = obj["AsmPartNum"]
      self.HasRuleSet:bool = obj["HasRuleSet"]
      self.IsKept:bool = obj["IsKept"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcOpDtlResultRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TestType:str = obj["TestType"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      self.CapabilityID:str = obj["CapabilityID"]
      self.Description:str = obj["Description"]
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      self.ResourceID:str = obj["ResourceID"]
      self.RuleTag:str = obj["RuleTag"]
      self.ParentRuleTag:str = obj["ParentRuleTag"]
      self.AsmPartNum:str = obj["AsmPartNum"]
      self.HasRuleSet:bool = obj["HasRuleSet"]
      self.IsKept:bool = obj["IsKept"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcOprResultRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TestType:str = obj["TestType"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.OpCode:str = obj["OpCode"]
      self.OpDesc:str = obj["OpDesc"]
      self.RuleTag:str = obj["RuleTag"]
      self.ParentRuleTag:str = obj["ParentRuleTag"]
      self.AsmPartNum:str = obj["AsmPartNum"]
      self.HasRuleSet:bool = obj["HasRuleSet"]
      self.IsKept:bool = obj["IsKept"]
      self.SubContract:bool = obj["SubContract"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcQuoteAsmRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the last QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  An integer that uniquely identifies the Assembly record within the Quote/Line.  Assigned by the system one greater than the last QuoteAsm record on file for the given quote/line.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number for this assembly.  Cannot be blank.  It does not have to be valid in the Part master file.  """  
      self.Description:str = obj["Description"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description if valid Part record.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The revision number for the assembly. An optional field. Use the Part.RevisionNum as a default.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  The production Quantity required for this assembly per one of it's Parent Part.  """  
      self.IUM:str = obj["IUM"]
      """  The unit of measure for this assembly. Use the Part.IUM as a default.  """  
      self.Direct:bool = obj["Direct"]
      """  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse  """  
      self.Parent:int = obj["Parent"]
      """  Sequence number of the Parent Assembly.  0 means no parent assembly (i.e. this is the final assembly).  Cannot be negative like the other pointers because this one shows up in a browser.  """  
      self.PriorPeer:int = obj["PriorPeer"]
      """   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find the last assembly (i.e. where the Parent is the same and the NextPeer is -1). Then NextPeer of that assembly gets updated with this assembly's sequence number and this assembly gets its PriorPeer field updated with the sequence number from that assembly which was found.  -1 means that there is no prior assembly (i.e. it is the first assembly of its peers).  """  
      self.NextPeer:int = obj["NextPeer"]
      """   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find the first assembly (i.e. where the Parent is the same and the PriorPeer is -1).  Then the PriorPeer of that assembly is updated with this assembly's sequence number and then this assembly's NextPeer gets updated with the sequence number from the assembly that was found.   -1 means that the assembly is the last assembly of its peers.  """  
      self.Child:int = obj["Child"]
      """  Seq # of this assembly's very first subassembly. This is known as the Child assembly. Automatically maintained by the maintenance programs. The logic is to find the Parent assembly record and if its child is -1, update it with this assembly's seq #.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Optional field for Engineering Drawing Number. Defaulted from BomHead.DrawNum during methods pull functions.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job Assembly comments.  """  
      self.BomSequence:int = obj["BomSequence"]
      """  An internally system assigned integer which is used as part of an index to organize the QuoteAsm records into a Bill of Material fashion sequence.  """  
      self.BomLevel:int = obj["BomLevel"]
      """  An internally system assigned integer which represents the "Level of Indention" of the QuoteAsm in reference to the Bill of Material structure.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """   A system maintained field. This is how many of the assemblies are required to produce ONE of the END ITEM.  This is a calculated field.  Calculated as the
 ( Parents RequiredQty  X QtyPer).
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer. The refresh may also occur if the structure of the assemblies is changed.  """  
      self.Template:bool = obj["Template"]
      """  Indicates if this quote assembly is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number (Quote.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FindNum:str = obj["FindNum"]
      """  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   An assembly record can be related to a specific operation.  This field contains the QuoteOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap (fallout) that is expected to occur for this material. The scrap increase the Required quantity. Example; need 1000 pieces scrap of 10 % will show a required quantity of 1100.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.OrigMtlSeq:int = obj["OrigMtlSeq"]
      self.OrigRuleTag:str = obj["OrigRuleTag"]
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the assembly.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the material.  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OrigStructTag:str = obj["OrigStructTag"]
      """  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  LinkToContract  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcQuoteDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  """  
      self.Ordered:bool = obj["Ordered"]
      """  Indicates if this Quote item has been ordered. This is not directly set by the user. It is updated via Order Entry when the QuoteDtl is referenced.  """  
      self.PartNum:str = obj["PartNum"]
      """   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the QuoteDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the CustXPrt table.. The XPartNum can be blank, does not have to exist in the CustXPrt table.  THIS FIELD WILL BE USED TO PASS THE VALUE ALONG TO ORDER ENTRY.  """  
      self.QuoteComment:str = obj["QuoteComment"]
      """  Contains comments about the detail line item. These will be printed on the Quote form.  """  
      self.LeadTime:str = obj["LeadTime"]
      """  A field to describe lead time. For example "Allow 4-5 weeks". This is printed on the Quote form.  """  
      self.Template:bool = obj["Template"]
      """  Indicates if this quote detail is considered a "Template".  Template lines appear in the browse of quotes that can be copied.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.JobComment:str = obj["JobComment"]
      """  Production Job comments. These will be copied to the JobHead.CommentText when the quote is pulled into a job during a get detail function.  It is also copied to the OrderDtl.PickListComment which may then be copied to JobHead.CommentText when linked.  """  
      self.MfgDetail:bool = obj["MfgDetail"]
      """  An internally used flag field which indicates if Manufacturing Details exist for this quote line item. It is set to "Yes" if any QuoteOpr or QuoteMtl records exist for the quote line. This is controlled via write/delete triggers on the QuoteOpr and QuoteMtl files. Used by the "Get Detail" function in job entry so that only QuoteDtl record that MfgDetail = Yes are shown in the browser.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record. Defaults from the Part Master.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.CustNum:int = obj["CustNum"]
      """  Number that relates to the Customer master. Duplicated from QuoteHed.CustNum.  Used to allow efficient browsing of the QuoteDtl records for a specific customer.  """  
      self.Quoted:bool = obj["Quoted"]
      """  Mirror image of QuoteHed.Quoted.  Duplicated to provide efficient browsing of QuoteDtl records.  """  
      self.Expired:bool = obj["Expired"]
      """  Mirror image of QuoteHed.Expired.  Duplicated to provide efficient browsing of QuoteDtl records.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the line.  """  
      self.SellingExpectedQty:int = obj["SellingExpectedQty"]
      """  The quantity expected to be ordered. (In selling unit of measure)  """  
      self.SellingExpectedUM:str = obj["SellingExpectedUM"]
      """  Unit of measure (how it is sold/issued) for the SellingExpectedQty.  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  """  
      self.ConfidencePct:int = obj["ConfidencePct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential for the quote line  """  
      self.LastUpdate:str = obj["LastUpdate"]
      """  The date this line was last updated  """  
      self.LastDcdUserID:str = obj["LastDcdUserID"]
      """  The last User Is that updated this Quote  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the QuoteHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the QuoteDtl.DiscountPercent * (QuoteQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or QuoteQty fields are changed.  """  
      self.ExpectedRevenue:int = obj["ExpectedRevenue"]
      """  Expected revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  """  
      self.DocExpectedRevenue:int = obj["DocExpectedRevenue"]
      """  Expected revenue for this line  in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  """  
      self.ReqShipDate:str = obj["ReqShipDate"]
      """  The requested ship date for the sales order  """  
      self.OrderQty:int = obj["OrderQty"]
      """  The quantity to be used when a Sales order is created. (In selling unit of measure)  """  
      self.SellingExpFactor:int = obj["SellingExpFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.MultiRel:bool = obj["MultiRel"]
      """  Indicates that the order line made from this quote line should have multiple releases.  Informational only.  """  
      self.POLine:str = obj["POLine"]
      """  Optional field used to enter the customers Purchase Order line item reference number.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Code which uniquely identifies a SalesCat record.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Replicated from QuoteHed to easier sorting  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   Duplicated from QuoteHed for Query's.  Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  """  
      self.CreatedFrom:str = obj["CreatedFrom"]
      """  Indicates if the Quote line was created from opportunity entry "QUOTE" or from Order Entry "ORDER".  Used to determine if the Quote can be deleted when the Order gets deleted.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  The date when the configuration was completed for the assembly.  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  The system time when the configuration was completed for the assembly.  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  The User ID of the last user to complete the configuration of the assembly.  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the line.  """  
      self.PriceListCode:str = obj["PriceListCode"]
      """  This is the Price List used to determine the starting base price.  """  
      self.BreakListCode:str = obj["BreakListCode"]
      """  This is the Price List used to determine the break % or amount.  """  
      self.PricingQty:int = obj["PricingQty"]
      """  The Expected Quantity (total qty of related quote lines) used to find price when quantity based discounting is applied.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the price returned by the price list before quantity based or order value based discounts are applied.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """   Same as List price except that this field contains the list price in
QuoteHed).  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on QuoteHed).  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  This is the Price Group ID used to price the quote line with.  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the user selected a price list different from the default.  """  
      self.PricingValue:int = obj["PricingValue"]
      """  The Expected Order Value (total extended price of related quote lines) used to find order value break when value based discounting is applied.  """  
      self.ExpUnitPrice:int = obj["ExpUnitPrice"]
      """  This is the unit price based on the expected quantity.  """  
      self.DocExpUnitPrice:int = obj["DocExpUnitPrice"]
      """  This is the unit price (in customer currency) based on the expected quantity.  """  
      self.ExpPricePerCode:str = obj["ExpPricePerCode"]
      """   Indicates the pricing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the QuoteDtl.SellingExpectedQty by the appropriate "per" value and then multiply by expected unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E"  """  
      self.MiscQtyNum:int = obj["MiscQtyNum"]
      """  An internally used integer assigned by the system to provide a unique key to the QuoteQty file.  This indicate what QuoteQty break should be used to get the related miscellaneous charges.  """  
      self.Engineer:bool = obj["Engineer"]
      """  The Quote Line has been Engineered.  """  
      self.ReadyToQuote:bool = obj["ReadyToQuote"]
      """  Indicates if Engineering details are complete/valid if the EngineerReq field is marked as Yes.  """  
      self.KitAllowUpdate:bool = obj["KitAllowUpdate"]
      """  Indicates if component lines can be added, deleted and modified during quote entry.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitShipComplete:bool = obj["KitShipComplete"]
      """  Indicates if the parent kitted part must be shipped complete or if kit components can be shipped in varying degrees of completeness.  This field is only relevant for quote lines which are kit parents.  If this field is set to "No", then KitPricing must be set to "C".  """  
      self.KitBackFlush:bool = obj["KitBackFlush"]
      """  Indicates if all components are to be backflushd when a kit parent item is shipped.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitPrintCompsPS:bool = obj["KitPrintCompsPS"]
      """  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes",then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitPrintCompsInv:bool = obj["KitPrintCompsInv"]
      """  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for quote lines which are kit parents.  """  
      self.KitPricing:str = obj["KitPricing"]
      """  Indicates how kits will be priced.  Values are: P = Parent Pricing (The price is otained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for quote lines which are kit parents.  """  
      self.KitParentLine:int = obj["KitParentLine"]
      """  The quote line number of the parent kit item.  This is only relevent for quote lines which are kit parent or component lines.  If the KitParentLine equals the QuoteLine then this is a kit parent line.  """  
      self.KitQtyPer:int = obj["KitQtyPer"]
      """  Component quantity required to fulfill one kit parent.  This field is only relevant on a quote line which is a kit component.  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      """  This field controls the order in which quote lines are displayed.  DisplaySeq is a decimal number where the whole number portion is used to sequence normal quote lines and the decimal portion is ued to sequence kit components under their associated kit parent.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of linked project.  Must exist on the Project table. Can be blank.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.MakeDirect:bool = obj["MakeDirect"]
      """  To indicate whether or not the line is make direct  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Must exist on ProjPhase table if entered  """  
      self.KitFlag:str = obj["KitFlag"]
      """   A character flag field used to differentiate between regular quote line, Sales Kit parent quote line and Sales Kit component quote line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  """  
      self.KitsLoaded:bool = obj["KitsLoaded"]
      """  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new quote line.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Non-blank value prevents taxes from being calculated for this line item  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExpectedRevenue:int = obj["Rpt1ExpectedRevenue"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExpectedRevenue:int = obj["Rpt2ExpectedRevenue"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExpectedRevenue:int = obj["Rpt3ExpectedRevenue"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExpUnitPrice:int = obj["Rpt1ExpUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExpUnitPrice:int = obj["Rpt2ExpUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExpUnitPrice:int = obj["Rpt3ExpUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1ListPrice:int = obj["Rpt1ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ListPrice:int = obj["Rpt2ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ListPrice:int = obj["Rpt3ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1OrdBasedPrice:int = obj["Rpt1OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2OrdBasedPrice:int = obj["Rpt2OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3OrdBasedPrice:int = obj["Rpt3OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.ExtPriceDtl:int = obj["ExtPriceDtl"]
      """  Extended Price for the quote line, rounded according to the Base currency Round rule  """  
      self.DocExtPriceDtl:int = obj["DocExtPriceDtl"]
      """  Extended Price for the quote line in Customer currency, rounded according to the Doc currency Round rule  """  
      self.Rpt1ExtPriceDtl:int = obj["Rpt1ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPriceDtl:int = obj["Rpt2ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPriceDtl:int = obj["Rpt3ExtPriceDtl"]
      """  Reporting currency value of this field  """  
      self.InDiscount:int = obj["InDiscount"]
      """  Reserved for future use  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """  Reserved for future use  """  
      self.InExpectedRevenue:int = obj["InExpectedRevenue"]
      """  Reserved for future use  """  
      self.DocInExpectedRevenue:int = obj["DocInExpectedRevenue"]
      """  Reserved for future use  """  
      self.InListPrice:int = obj["InListPrice"]
      """  Reserved for future use  """  
      self.DocInListPrice:int = obj["DocInListPrice"]
      """  Reserved for future use  """  
      self.InOrdBasedPrice:int = obj["InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.DocInOrdBasedPrice:int = obj["DocInOrdBasedPrice"]
      """  Reserved for future use  """  
      self.InExpUnitPrice:int = obj["InExpUnitPrice"]
      """  Reserved for future use  """  
      self.DocInExpUnitPrice:int = obj["DocInExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  Reserved for future use  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  Reserved for future use  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  Reserved for future use  """  
      self.Rpt1InExpectedRevenue:int = obj["Rpt1InExpectedRevenue"]
      """  Reserved for future use  """  
      self.Rpt2InExpectedRevenue:int = obj["Rpt2InExpectedRevenue"]
      """  Reserved for future use  """  
      self.Rpt3InExpectedRevenue:int = obj["Rpt3InExpectedRevenue"]
      """  Reserved for future use  """  
      self.Rpt1InExpUnitPrice:int = obj["Rpt1InExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt2InExpUnitPrice:int = obj["Rpt2InExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt3InExpUnitPrice:int = obj["Rpt3InExpUnitPrice"]
      """  Reserved for future use  """  
      self.Rpt1InListPrice:int = obj["Rpt1InListPrice"]
      """  Reserved for future use  """  
      self.Rpt2InListPrice:int = obj["Rpt2InListPrice"]
      """  Reserved for future use  """  
      self.Rpt3InListPrice:int = obj["Rpt3InListPrice"]
      """  Reserved for future use  """  
      self.Rpt1InOrdBasedPrice:int = obj["Rpt1InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.Rpt2InOrdBasedPrice:int = obj["Rpt2InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.Rpt3InOrdBasedPrice:int = obj["Rpt3InOrdBasedPrice"]
      """  Reserved for future use  """  
      self.InExtPriceDtl:int = obj["InExtPriceDtl"]
      """  Reserved for future use  """  
      self.DocInExtPriceDtl:int = obj["DocInExtPriceDtl"]
      """  Reserved for future use  """  
      self.Rpt1InExtPriceDtl:int = obj["Rpt1InExtPriceDtl"]
      """  Reserved for future use  """  
      self.Rpt2InExtPriceDtl:int = obj["Rpt2InExtPriceDtl"]
      """  Reserved for future use  """  
      self.Rpt3InExtPriceDtl:int = obj["Rpt3InExtPriceDtl"]
      """  Reserved for future use  """  
      self.WorstCsPct:int = obj["WorstCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  """  
      self.BestCsPct:int = obj["BestCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  """  
      self.WorstCsRevenue:int = obj["WorstCsRevenue"]
      """  Worst case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  """  
      self.DocWorstCsRevenue:int = obj["DocWorstCsRevenue"]
      """  Worst case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  """  
      self.Rpt1WorstCsRevenue:int = obj["Rpt1WorstCsRevenue"]
      self.Rpt2WorstCsRevenue:int = obj["Rpt2WorstCsRevenue"]
      self.Rpt3WorstCsRevenue:int = obj["Rpt3WorstCsRevenue"]
      self.BestCsRevenue:int = obj["BestCsRevenue"]
      """  Best case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  """  
      self.DocBestCsRevenue:int = obj["DocBestCsRevenue"]
      """  Best case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  """  
      self.Rpt1BestCsRevenue:int = obj["Rpt1BestCsRevenue"]
      self.Rpt2BestCsRevenue:int = obj["Rpt2BestCsRevenue"]
      self.Rpt3BestCsRevenue:int = obj["Rpt3BestCsRevenue"]
      self.KitCompOrigSeq:int = obj["KitCompOrigSeq"]
      """  The original material sequence of this kit component under the kit parent part.  """  
      self.KitCompOrigPart:str = obj["KitCompOrigPart"]
      """  The original kit component part number prior to processing any configurator rule programs  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.DiscBreakListCode:str = obj["DiscBreakListCode"]
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.DiscListPrice:int = obj["DiscListPrice"]
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.OverrideDiscPriceList:bool = obj["OverrideDiscPriceList"]
      self.DemandContractLine:int = obj["DemandContractLine"]
      """  Demand Contract Line  """  
      self.DemandHedSeq:int = obj["DemandHedSeq"]
      """  Demand Header sequence number to which this record is related.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  Demand Detail Sequence number to which this record is related.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.ICPOLine:int = obj["ICPOLine"]
      """  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.ICPONum:int = obj["ICPONum"]
      """  Inter-Company Purchase order number  that the detail line item is linked to.  """  
      self.Linked:bool = obj["Linked"]
      """  Indicates if this quote line is linked to an inter-company PO line.  """  
      self.LockPrice:bool = obj["LockPrice"]
      """  Indicates if the price of the quote line can be changed.  """  
      self.LockQty:bool = obj["LockQty"]
      """   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  """  
      self.VoidLine:bool = obj["VoidLine"]
      """  Indicates that the line item was closed before any shipments were made against it.  """  
      self.Warranty:bool = obj["Warranty"]
      """  Indicate that the item or the product group has a warranty.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  """  
      self.WarrantyComment:str = obj["WarrantyComment"]
      """  Editor widget for Warranty comments.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.EstimateGUID:str = obj["EstimateGUID"]
      """  EstimateGUID  """  
      self.RFQCurrBaseEst:str = obj["RFQCurrBaseEst"]
      """  RFQCurrBaseEst  """  
      self.RFQTemplate:str = obj["RFQTemplate"]
      """  RFQTemplate  """  
      self.CreateEstimate:bool = obj["CreateEstimate"]
      """  CreateEstimate  """  
      self.Rating:str = obj["Rating"]
      """  Rating  """  
      self.EstimateUserID:str = obj["EstimateUserID"]
      """  EstimateUserID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  NeedByDate  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """  Indicates the way in which parts are made for Co-Part jobs.  There are two value “S” – Sequential and “C” – Concurrent.  Sequential is the default. This field is similar to the JobHead.ProcessMode field.  """  
      self.ECCQuoteNum:str = obj["ECCQuoteNum"]
      """  ECC Quote Number  """  
      self.ECCQuoteLine:int = obj["ECCQuoteLine"]
      """  ECC Quote Line  """  
      self.ECCCmmtRef:str = obj["ECCCmmtRef"]
      """  ECC Comment Ref  """  
      self.ECCComment:str = obj["ECCComment"]
      """  ECCComment  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.Tax:int = obj["Tax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.DocTax:int = obj["DocTax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.Rpt1Tax:int = obj["Rpt1Tax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.Rpt2Tax:int = obj["Rpt2Tax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.Rpt3Tax:int = obj["Rpt3Tax"]
      """  Total tax in base currency. Tax detail for the line.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, the QuoteDtlTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  Indicates if no tax recalculation by the system is supposed to be done.  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """  Total Quote Self Assessed Taxes for the Quote Line  """  
      self.EntityUseCode:str = obj["EntityUseCode"]
      """  EntityUseCode  """  
      self.ExternalCRMQuoteLineID:str = obj["ExternalCRMQuoteLineID"]
      """  This field holds the id of this quote line in the External CRM  """  
      self.ReturnLineType:str = obj["ReturnLineType"]
      """  Type for returns: Blank, (C)redit or (S)tandard  """  
      self.MSRP:int = obj["MSRP"]
      """  Base price before any price breaks and discounts  """  
      self.DocMSRP:int = obj["DocMSRP"]
      """  Same as MSRP except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt1MSRP:int = obj["Rpt1MSRP"]
      """  Same as MSRP except that this field contains the price in a report currency converted..  """  
      self.Rpt2MSRP:int = obj["Rpt2MSRP"]
      """  Same as MSRP except that this field contains the price in a report currency converted..  """  
      self.Rpt3MSRP:int = obj["Rpt3MSRP"]
      """  Same as MSRP except that this field contains the price in a report currency converted..  """  
      self.EndCustomerPrice:int = obj["EndCustomerPrice"]
      """  Distributor end customer price.  """  
      self.DocEndCustomerPrice:int = obj["DocEndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt1EndCustomerPrice:int = obj["Rpt1EndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in a report currency converted.  """  
      self.Rpt2EndCustomerPrice:int = obj["Rpt2EndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in a report currency converted.  """  
      self.Rpt3EndCustomerPrice:int = obj["Rpt3EndCustomerPrice"]
      """  Same as end customer price except that this field contains the price in a report currency converted.  """  
      self.MFCustNum:int = obj["MFCustNum"]
      """  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  """  
      self.MFShipToNum:str = obj["MFShipToNum"]
      """  Mark For ShipToNum  """  
      self.UseOTMF:bool = obj["UseOTMF"]
      """  Indicates that the One Time Mark For information defined for this record should be used.  """  
      self.OTMFName:str = obj["OTMFName"]
      """  One Time Mark For Contact Name  """  
      self.OTMFAddress1:str = obj["OTMFAddress1"]
      """  One Time Mark For first line of the ShipTo address.  """  
      self.OTMFAddress2:str = obj["OTMFAddress2"]
      """  One Time Mark For second line of the ShipTo address.  """  
      self.OTMFAddress3:str = obj["OTMFAddress3"]
      """  One Time Mark For third line of the ShipTo address.  """  
      self.OTMFCity:str = obj["OTMFCity"]
      """  City portion of the One Time Mark For address.  """  
      self.OTMFState:str = obj["OTMFState"]
      """  The state or province portion of the One Time Mark For address.  """  
      self.OTMFZIP:str = obj["OTMFZIP"]
      """  The zip or postal code portion of the One Time Mark For address.  """  
      self.OTMFContact:str = obj["OTMFContact"]
      """  One Time Mark For Contact Name  """  
      self.OTMFFaxNum:str = obj["OTMFFaxNum"]
      """  Fax number for the One Time Mark For.  """  
      self.OTMFPhoneNum:str = obj["OTMFPhoneNum"]
      """  Phone number for the One Time Mark For  """  
      self.OTMFCountryNum:int = obj["OTMFCountryNum"]
      """  Country number for the One Time Mark For  """  
      self.PromotionalPrice:int = obj["PromotionalPrice"]
      """  Promotional Price offered to Dealer and Distributors  """  
      self.DocPromotionalPrice:int = obj["DocPromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in the customer currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt1PromotionalPrice:int = obj["Rpt1PromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt2PromotionalPrice:int = obj["Rpt2PromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  """  
      self.Rpt3PromotionalPrice:int = obj["Rpt3PromotionalPrice"]
      """  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on QuoteHed.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  Used specifically for Deal Portal and Location Inventory, not for Inventory Tracked Attributes.  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.KBOriginalConfigProdID:int = obj["KBOriginalConfigProdID"]
      """  The unique identifier of the related original CPQ Configured Quote Product.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcQuoteHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number is an integer which is used to uniquely identify a quote within the system.  This is automatically assigned by the system when the user requests to create a new quote. To create a new quote the user either takes an "add" option or leaves the Quote Number fill-in zero. The system generates a number by finding the quote number of the last record on file and then a 1 to it. It then uses the greater of Last quote number + 1 or the EQSyst.StartQuoteNum.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the internal Customer number that the links the quote to the customer master. This is not directly entered by the user. Instead the CustID is entered which provides the CustNum from the customer master. The quote must reference a valid Customer master.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Date that quote was created in the system. Not user maintainable. Set equal to the system date when record was created.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.QuoteComment:str = obj["QuoteComment"]
      """  Contains comments about the overall Quote. These will be printed on the Quote form.  """  
      self.DueDate:str = obj["DueDate"]
      """  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  """  
      self.Quoted:bool = obj["Quoted"]
      """  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  """  
      self.DateQuoted:str = obj["DateQuoted"]
      """  Date that the quoter considered the quoting process for this quote complete. This field is not accessible until Quoted = Yes. At which time this gets defaulted to system date. It is overrideable. A change to this field triggers a refresh to ExpirationDate.  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """   The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.

This date is also used as part of the quote purging criteria testing.  """  
      self.FollowUpDate:str = obj["FollowUpDate"]
      """  Date that this quote should be followed up with the prospect by. This can be left blank.  When the quote is completed (i.e. Quoted = TRUE) this field is defaulted to DateQuoted + EQSyst.FollowUpDays and is user overrideable.  If EQSyst.FollowUpDays = Zero(0) then no default is generated.  """  
      self.Reference:str = obj["Reference"]
      """  A reference field that could be used to enter the customer RFQ # or any other piece of useful information.  """  
      self.CheckOff1:bool = obj["CheckOff1"]
      """   Optional Quote check off # 1. The label for this field is found in EQSyst. If the label field is blank then field should be invisible.
These "check offs" could be used for selecting quotes. An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff2:bool = obj["CheckOff2"]
      """  Optional check off # 2.  """  
      self.CheckOff3:bool = obj["CheckOff3"]
      """  Optional check off # 3.  """  
      self.CheckOff4:bool = obj["CheckOff4"]
      """  Optional check off # 4.  """  
      self.CheckOff5:bool = obj["CheckOff5"]
      """  Optional check off # 5.  """  
      self.Expired:bool = obj["Expired"]
      """  Indicates if the Quote has expired.  A quote is expired when QuoteHed.ExpirationDate < Today.  Each time a user logs on the system does a quick check for any unexpired quotes that have an expiration date < Today and sets them as expired. This field is also set during the QuoteHed write trigger.  """  
      self.FlwAlrtSnt:bool = obj["FlwAlrtSnt"]
      """  System maintained flag - set to yes when the quote follow up alert has been sent.  """  
      self.DueAlrtSnt:bool = obj["DueAlrtSnt"]
      """  System maintained flag - set to yes when the quote due date alert has been sent.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LeadRating:str = obj["LeadRating"]
      """  A = High, Z = Low  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Link to the territory Id for this LOQ  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to Task set  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity
QUOT = Quote  """  
      self.ParentQuoteNum:int = obj["ParentQuoteNum"]
      """  Link to the parent Quote.  This Quote is a for the same job as the parent but for a different customer.  This quotes revenues estimates won't be included in the sales managers figures.  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active Stage changing task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.ExpectedClose:str = obj["ExpectedClose"]
      """  The date this quote is expected to close.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  Indicates the Type of reason for closing this quote.   "W" Win CRM "L" - Loss CRM, "T" Task CRM.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Select from list of Win or loss reason codes depending on the setting if the conclusion field  """  
      self.ConfidencePct:int = obj["ConfidencePct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  Used to establish a discount percent value which will be used as a default during Quote line entry. It can be left as zero.  Use the CUSTOMER.DISCOUNTPERCENT field as a default. Refreshed whenever QUOTEHED.CUSTOMER field changes.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Order release record created from this Quote. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new Quotes or when the QuoteHED.CUSTNUM is changed.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Establishes the Shipping Contact to be used as default on the Order release record created from this Quote. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  """  
      self.QuoteClosed:bool = obj["QuoteClosed"]
      """  This quote is no longer updatable.  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  The date that the Quote was closed.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table. Use the CUSTOMER.SHIPVIA as the default when the CUSTNUM field is changed and the SHIPTO is blank. Use SHIPTO.SHIPVIA when CUSTNUM or SHIPTO fields are changed and the SHIPTO is not blank.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  Link to the Marketing Campaign related to this Quote.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  Link to the marketing event associated with this record.  """  
      self.CallTypeCode:str = obj["CallTypeCode"]
      """  CallType code from the CallType table.  Identifies what type of communication this is. For example email, phone, visit, etc.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  """  
      self.TermsCode:str = obj["TermsCode"]
      """   Contains the key value of the record in the TERMS table which indicates the sales terms established for this Opportunity/Quote. On change of QutoeHED.CUSTNUM use the CUSTOMER.TERMS
field as the default.  """  
      self.Ordered:bool = obj["Ordered"]
      """  Indicates that the one or more detail line items have been ordered on this quote. Note: This can be set via 3 methods. 1 - When the task is marked as a win and order is created, 2 - Via the Order Entry Get function, 2 - Via the Order Entry Add from Quote Line function.  """  
      self.ApplyOrderBasedDisc:bool = obj["ApplyOrderBasedDisc"]
      """  Indicates if order based discounting needs to be applied to the quote.  """  
      self.AutoOrderBasedDisc:bool = obj["AutoOrderBasedDisc"]
      """  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this quote.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.LockRate:bool = obj["LockRate"]
      """  When checked the exchange rate defaults the currency's exchanged reate, but the user can change it. When not checked the exchange rate defaults the currecy's exchange rate, and the field is disabled  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the Quote is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the quote which could affect taxes (QuoteDtl, QuoteHed, QuoteMsc, etc). It defaults from EQSyst.QuoReadyToCalcDflt field when an order is created.  """  
      self.ExportRequested:str = obj["ExportRequested"]
      """  This field is used to store a code that represents the external system that the Quote is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.QuoteAmt:int = obj["QuoteAmt"]
      """  Total quote Amount. This field is an accumulation of the extended net amounts of the detail line items.  """  
      self.DocQuoteAmt:int = obj["DocQuoteAmt"]
      """  Total quote Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  """  
      self.Rpt1QuoteAmt:int = obj["Rpt1QuoteAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2QuoteAmt:int = obj["Rpt2QuoteAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3QuoteAmt:int = obj["Rpt3QuoteAmt"]
      """  Reporting currency value of this field  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.WorstCsPct:int = obj["WorstCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (worst case) for the quote line.  """  
      self.BestCsPct:int = obj["BestCsPct"]
      """  Allows Sales Rep to enter a percentage to factor the calculated revenue potential (best case) for the quote line.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  Demand Header sequence number to which this record is related.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready.  """  
      self.EDIQuote:bool = obj["EDIQuote"]
      """  Quote created from EDI interfaced module.  """  
      self.EDIAck:bool = obj["EDIAck"]
      """  Updated from EDI module this type of document is created.  """  
      self.OutboundQuoteDocCtr:int = obj["OutboundQuoteDocCtr"]
      """  Incremented whenever an outbound quote document is generated from the quote i.e. Response to Request For Quotes, etc.  """  
      self.DemandProcessDate:str = obj["DemandProcessDate"]
      """  Date in which the related demand was last processed.  """  
      self.DemandProcessTime:int = obj["DemandProcessTime"]
      """  System Time when demand was last processed.  """  
      self.LastTCtrlNum:str = obj["LastTCtrlNum"]
      """  EDI Transaction Control Number  """  
      self.LastBatchNum:str = obj["LastBatchNum"]
      """  EDI Batch Control Number  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DocTotalWHTax:int = obj["DocTotalWHTax"]
      """   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt1TotalWHTax:int = obj["Rpt1TotalWHTax"]
      """   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """   Total Quote Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """   Total Quote Invoice TaxesQuote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt2TotalWHTax:int = obj["Rpt2TotalWHTax"]
      """   Total Order Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """   Total Quote Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.Rpt3TotalWHTax:int = obj["Rpt3TotalWHTax"]
      """   Total Quote Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.DropShip:bool = obj["DropShip"]
      """  Freight charges will not be returned if 'yes'  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """   Quote Total Self Assessed Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.TotalTax:int = obj["TotalTax"]
      """   Quote Total Invoice Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.TotalWHTax:int = obj["TotalWHTax"]
      """   Quote Total Withholding Taxes
Quote Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Quote Total - TotalComm  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.ICPONum:int = obj["ICPONum"]
      """  Inter-Company Purchase order number that uniquely identifies the purchase order.  """  
      self.Linked:bool = obj["Linked"]
      """  Indicates if this quote header is linked to an inter-company PO header.  """  
      self.LockQty:bool = obj["LockQty"]
      """   increase/decrease when releases are changed.
When locked changes to releases does not change the quote quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the items on the order to arrive. This is used only as the default value for the NeedByDate when creating quote detail line items. This can be left blank.  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.OTSCustSaved:bool = obj["OTSCustSaved"]
      """  True if Customer or ShipTo record was created using the  OTS info.  """  
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      """  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  """  
      self.OTSSaveCustID:str = obj["OTSSaveCustID"]
      """  CustID to be used if the OTS is used to create a customer record.  """  
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      """  Override Carrier Defaults.  If not checked then the Site values will be used  """  
      self.OverrideService:bool = obj["OverrideService"]
      """  Override Service Options.  If not checked then the Site values will be used  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.RequestDate:str = obj["RequestDate"]
      """  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for QuoteDtl.RequestDate.  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.VoidQuote:bool = obj["VoidQuote"]
      """  Indicates that the Quote item was closed before any shipments were made against it.  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.TotalDiscPct:int = obj["TotalDiscPct"]
      """  Total discount percent.  """  
      self.TotalExpected:int = obj["TotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.TotalGrossValue:int = obj["TotalGrossValue"]
      self.TotalMiscAmt:int = obj["TotalMiscAmt"]
      self.TotalPotential:int = obj["TotalPotential"]
      self.TotalWorstCs:int = obj["TotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.DocTotalBestCs:int = obj["DocTotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.DocTotalDiscount:int = obj["DocTotalDiscount"]
      self.DocTotalDiscPct:int = obj["DocTotalDiscPct"]
      """  Total discount percent.  """  
      self.DocTotalExpected:int = obj["DocTotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.DocTotalGrossValue:int = obj["DocTotalGrossValue"]
      self.DocTotalMiscAmt:int = obj["DocTotalMiscAmt"]
      self.DocTotalPotential:int = obj["DocTotalPotential"]
      self.DocTotalWorstCs:int = obj["DocTotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.Rpt1TotalBestCs:int = obj["Rpt1TotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.Rpt1TotalDiscount:int = obj["Rpt1TotalDiscount"]
      self.Rpt1TotalDiscPct:int = obj["Rpt1TotalDiscPct"]
      """  Total discount percent.  """  
      self.Rpt1TotalExpected:int = obj["Rpt1TotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.Rpt1TotalGrossValue:int = obj["Rpt1TotalGrossValue"]
      self.Rpt1TotalMiscAmt:int = obj["Rpt1TotalMiscAmt"]
      self.Rpt1TotalPotential:int = obj["Rpt1TotalPotential"]
      self.Rpt1TotalWorstCs:int = obj["Rpt1TotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.Rpt2TotalBestCs:int = obj["Rpt2TotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.Rpt2TotalDiscount:int = obj["Rpt2TotalDiscount"]
      self.Rpt2TotalDiscPct:int = obj["Rpt2TotalDiscPct"]
      """  Total discount percent.  """  
      self.Rpt2TotalExpected:int = obj["Rpt2TotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.Rpt2TotalGrossValue:int = obj["Rpt2TotalGrossValue"]
      self.Rpt2TotalMiscAmt:int = obj["Rpt2TotalMiscAmt"]
      self.Rpt2TotalPotential:int = obj["Rpt2TotalPotential"]
      self.Rpt2TotalWorstCs:int = obj["Rpt2TotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.Rpt3TotalBestCs:int = obj["Rpt3TotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.Rpt3TotalDiscount:int = obj["Rpt3TotalDiscount"]
      self.Rpt3TotalDiscPct:int = obj["Rpt3TotalDiscPct"]
      """  Total discount percent.  """  
      self.Rpt3TotalExpected:int = obj["Rpt3TotalExpected"]
      """  The expected revenue, calculated with the confidence factor.  """  
      self.Rpt3TotalGrossValue:int = obj["Rpt3TotalGrossValue"]
      self.Rpt3TotalMiscAmt:int = obj["Rpt3TotalMiscAmt"]
      self.Rpt3TotalPotential:int = obj["Rpt3TotalPotential"]
      self.Rpt3TotalWorstCs:int = obj["Rpt3TotalWorstCs"]
      """  Worst case revenue, calculated with the worst case confidence factor.  """  
      self.TotalBestCs:int = obj["TotalBestCs"]
      """  Total best case revenue, calculated with the best case confidence factor.  """  
      self.TotalDiscount:int = obj["TotalDiscount"]
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.LOQPrepressText:str = obj["LOQPrepressText"]
      """  LOQPrepressText  """  
      self.LOQNewPageOnQuoteLine:bool = obj["LOQNewPageOnQuoteLine"]
      """  LOQNewPageOnQuoteLine  """  
      self.LOQBookPCFinishing:bool = obj["LOQBookPCFinishing"]
      """  LOQBookPCFinishing  """  
      self.LOQBookPCPaper:bool = obj["LOQBookPCPaper"]
      """  LOQBookPCPaper  """  
      self.LOQBookPCPress:bool = obj["LOQBookPCPress"]
      """  LOQBookPCPress  """  
      self.LOQBookPCPlates:bool = obj["LOQBookPCPlates"]
      """  LOQBookPCPlates  """  
      self.LOQVariations:bool = obj["LOQVariations"]
      """  LOQVariations  """  
      self.AEPLOQType:str = obj["AEPLOQType"]
      """  AEPLOQType  """  
      self.LOQPrepressStyle:str = obj["LOQPrepressStyle"]
      """  LOQPrepressStyle  """  
      self.QuoteCSR:str = obj["QuoteCSR"]
      """  QuoteCSR  """  
      self.DueHour:str = obj["DueHour"]
      """  DueHour  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ECCConfirmed:bool = obj["ECCConfirmed"]
      """  Quote was confirmed/rejected by ECC Web  """  
      self.ECCConfirmedBy:str = obj["ECCConfirmedBy"]
      """  Quote was confirmed/rejected by this ECC user  """  
      self.ECCMsgType:str = obj["ECCMsgType"]
      """  ECC quote message: RFQ or GQR  """  
      self.ECCWebReady:bool = obj["ECCWebReady"]
      """  Quote is ready to be approved by user via ECC web site.  """  
      self.ECCQuoteNum:str = obj["ECCQuoteNum"]
      """  ECC Quote Number  """  
      self.ECCCmmtRef:str = obj["ECCCmmtRef"]
      """  ECC Comment Reference Number  """  
      self.ECCComment:str = obj["ECCComment"]
      """  ECCComment  """  
      self.ECCStatus:str = obj["ECCStatus"]
      """  ECC Quote Status  """  
      self.ECCExpirationDate:str = obj["ECCExpirationDate"]
      """  ECC Expiration Date  """  
      self.ECCCmmtRefSK:str = obj["ECCCmmtRefSK"]
      """  ECCCmmtRefSK  """  
      self.ExternalCRMQuote:bool = obj["ExternalCRMQuote"]
      """  This field defines if the Quote  is synchronized to an External CRM.  """  
      self.ExternalCRMQuoteID:str = obj["ExternalCRMQuoteID"]
      """  This field holds the  id of this quote in the External CRM  """  
      self.ExternalCRMOrderID:str = obj["ExternalCRMOrderID"]
      """  This field holds the sales order created in the External CRM. This id might not match an Epicor ERP Order id.  """  
      self.ECCSalesRepID:str = obj["ECCSalesRepID"]
      """  Web Sales Rep ID  """  
      self.Tax:int = obj["Tax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.DocTax:int = obj["DocTax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.Rpt1Tax:int = obj["Rpt1Tax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.Rpt2Tax:int = obj["Rpt2Tax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.Rpt3Tax:int = obj["Rpt3Tax"]
      """  Total tax in base currency. The sum of all the tax details for the quote.  """  
      self.HdrTaxNoUpdt:bool = obj["HdrTaxNoUpdt"]
      """  HdrTaxNoUpdt  """  
      self.ExternalCRMLastSync:str = obj["ExternalCRMLastSync"]
      """  This field defines the last time that the Quote has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  """  
      self.ExternalCRMSyncRequired:bool = obj["ExternalCRMSyncRequired"]
      """  This fields determines if the quotes needs to be synchronized to the External CRM. If there are changes in the quote or quote detail file, Epicor ERP automatically turns on this field.  """  
      self.TotalClaimsCredit:int = obj["TotalClaimsCredit"]
      """  Total of claims credit lines  """  
      self.DocTotalClaimsCredit:int = obj["DocTotalClaimsCredit"]
      """  Total of claims credit lines in customer currency  """  
      self.Rpt1TotalClaimsCredit:int = obj["Rpt1TotalClaimsCredit"]
      """  Total of claims credit lines in report currency  """  
      self.Rpt2TotalClaimsCredit:int = obj["Rpt2TotalClaimsCredit"]
      """  Total of claims credit lines in report currency  """  
      self.Rpt3TotalClaimsCredit:int = obj["Rpt3TotalClaimsCredit"]
      """  Total of claims credit lines in report currency  """  
      self.TotalClaimsTax:int = obj["TotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes.  """  
      self.DocTotalClaimsTax:int = obj["DocTotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes in customer currency.  """  
      self.Rpt1TotalClaimsTax:int = obj["Rpt1TotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes in report currency.  """  
      self.Rpt2TotalClaimsTax:int = obj["Rpt2TotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes in report currency.  """  
      self.Rpt3TotalClaimsTax:int = obj["Rpt3TotalClaimsTax"]
      """  Total Quote claims credit Invoice Taxes in report currency.  """  
      self.TotalClaimsSATax:int = obj["TotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes.  """  
      self.DocTotalClaimsSATax:int = obj["DocTotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes in customer currency.  """  
      self.Rpt1TotalClaimsSATax:int = obj["Rpt1TotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes in customer currency.  """  
      self.Rpt2TotalClaimsSATax:int = obj["Rpt2TotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes in customer currency.  """  
      self.Rpt3TotalClaimsSATax:int = obj["Rpt3TotalClaimsSATax"]
      """  Total Quote claims credit Self Assessed Taxes in customer currency.  """  
      self.TotalClaimsWHTax:int = obj["TotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes.  """  
      self.DocTotalClaimsWHTax:int = obj["DocTotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes in customer currency.  """  
      self.Rpt1TotalClaimsWHTax:int = obj["Rpt1TotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes in report currency.  """  
      self.Rpt2TotalClaimsWHTax:int = obj["Rpt2TotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes in report currency.  """  
      self.Rpt3TotalClaimsWHTax:int = obj["Rpt3TotalClaimsWHTax"]
      """  Total Quote claims credit Withholding Taxes in report currency.  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.IncotermCode:str = obj["IncotermCode"]
      """  Incoterm Code  """  
      self.IncotermLocation:str = obj["IncotermLocation"]
      """  Incoterm Location  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcQuoteMtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The AssemblySeq number of the related QuoteAsm record.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material record within a specific Quote/Line/Assembly.  System assigned using the next available number, determined by reading last QuoteMtl record on the Quote/Line/Assembly and then adding one to it.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of required material. Does not have to be valid in Part master file, but must not be blank.  """  
      self.Description:str = obj["Description"]
      """  Description of the material. Cannot be blank  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Quantity required per one of the Parent item. This is a factor used in calculating the total material requirement.  """  
      self.IUM:str = obj["IUM"]
      """  The issue/usage unit of measure for this material.  """  
      self.Direct:bool = obj["Direct"]
      """  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  """  
      self.LeadTime:int = obj["LeadTime"]
      """  Expected Purchasing lead time (in days) for the material. This is passed along to the job if the item gets manufactured.  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   A material record can be related to a specific operation. This field contains the QuoteOpr.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job.  """  
      self.SalvagePartNum:str = obj["SalvagePartNum"]
      """  Part number for Salvaged scrap from this material record.  An optional field. This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via Salvage receipt process.  """  
      self.SalvageDescription:str = obj["SalvageDescription"]
      """  Description of Salvaged material. Use Part.Description for a default.  """  
      self.SalvageQtyPer:int = obj["SalvageQtyPer"]
      """  A factor that multiplied by the RequiredQty for the material results in the expected total salvage quantity.  """  
      self.SalvageUM:str = obj["SalvageUM"]
      """  Default Unit of measure for the Salvaged Part. Default from the Part.IUM.  """  
      self.SalvageUnitCredit:int = obj["SalvageUnitCredit"]
      """  Estimated Salvage Unit Credit. Use the appropriate cost from the Part master as a default.  """  
      self.SalvageMtlBurRate:int = obj["SalvageMtlBurRate"]
      """  The salvage material burden rate for this Quote Material.  """  
      self.SalvageEstMtlBurUnitCredit:int = obj["SalvageEstMtlBurUnitCredit"]
      """  Estimated salvage Mtl Burden Unit Credit. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  """  
      self.MfgComment:str = obj["MfgComment"]
      """   Comments for manufacturing about this material record. These comments are printed on manufacturing reports,  such as the router. For valid Parts use the Part.MfgComment as a default.
View as Editor widget.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Used to identify a default vendor. Use the Part.VendorNum as a default. This will be used as a default for purchasing and miscellaneous receipts. This field is not directly maintainable; instead it's assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  An optional field, but if entered must be valid.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  """  
      self.BuyIt:bool = obj["BuyIt"]
      """  Indicates if this material is to be Purchased for the Job. If this is a non inventory part then this is "Yes" and can't be changed. If this is a valid Part then set it to "NO" but the user can override it.  """  
      self.PurComment:str = obj["PurComment"]
      """   Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.

View as Editor widget.  """  
      self.MinimumCost:int = obj["MinimumCost"]
      """  Minimum Cost that will be used for this material. That is if the system will take the greater of (required quantity * unit cost) or (MinimumCost) when calculating the material cost for the quote.  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  Estimated Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this Quote Material.  """  
      self.EstMtlBurUnitCost:int = obj["EstMtlBurUnitCost"]
      """  Estimated Mtl Burden Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  Required Qty per ONE of the  END ITEM.  This is a system calculated field.  Calculated as (Parent Required Qty X QtyPer). The parent qty is one if assemblySeq zero else  (QuoteAsmbl.RequireQty) if AssemblySeq > 0.  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap (fallout) that is expected to occur for this material. The scrap increase the Required quantity. Example; need 1000 pieces scrap of 10 % will show a required quantity of 1100.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.FixedQty:bool = obj["FixedQty"]
      """  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  """  
      self.FindNum:str = obj["FindNum"]
      """  Characters used on the drawing to show where material is used.  """  
      self.Class:str = obj["Class"]
      """   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
CLasses could be set up for different type of raw materials. It will primarily be used as a report selection parameter.  """  
      self.APSAddResType:str = obj["APSAddResType"]
      """   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this quote material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this quote material.  Can be zero if RFQ(s) are not required.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQ number that the item is linked to.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.RFQStat:str = obj["RFQStat"]
      """   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.GlbRFQ:bool = obj["GlbRFQ"]
      """  Global RFQ flag.  Used in Consolidated Purchasing.  """  
      self.PBrkCost02:int = obj["PBrkCost02"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost03:int = obj["PBrkCost03"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost04:int = obj["PBrkCost04"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost05:int = obj["PBrkCost05"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost06:int = obj["PBrkCost06"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost07:int = obj["PBrkCost07"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost08:int = obj["PBrkCost08"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost09:int = obj["PBrkCost09"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkCost10:int = obj["PBrkCost10"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.PBrkQty01:int = obj["PBrkQty01"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty02:int = obj["PBrkQty02"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty03:int = obj["PBrkQty03"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty04:int = obj["PBrkQty04"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty05:int = obj["PBrkQty05"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty06:int = obj["PBrkQty06"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty07:int = obj["PBrkQty07"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty08:int = obj["PBrkQty08"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty09:int = obj["PBrkQty09"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkQty10:int = obj["PBrkQty10"]
      """  Price break quantity, quantity at which a price break occurs. The quantity represent the minimum qty that is needed to obtain the corresponding price established in PBCost array. Not all 4 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the material unit cost to use by first calculating the material Required Qty based on the quote quantity. Then searches the PBQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost is used else EstUnitCost is used.  """  
      self.PBrkCost01:int = obj["PBrkCost01"]
      """  Unit cost for the corresponding price break quantity. (PBrkQty)  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number initially entered on the assembly.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part/revision number initially entered on the material.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OrigStructTag:str = obj["OrigStructTag"]
      """  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  """  
      self.OrigGroupSeq:int = obj["OrigGroupSeq"]
      """  By storing the original Group Sequence of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  """  
      self.EstMtlUnitCost:int = obj["EstMtlUnitCost"]
      """  Estimated Material Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  LinkToContract  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.   It must be a AP Misc. charge.  """  
      self.MiscCharge:bool = obj["MiscCharge"]
      """  This indicates that this JobMtl record is for a Misc charge related to this job/assembly.  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.PLMMtlSeq:int = obj["PLMMtlSeq"]
      """  Unique identifier per Quote Line that allows PLM Integration to find QuoteMtl record.  """  
      self.LocationView:bool = obj["LocationView"]
      """  Controls if this material record is viewable in Location Management or the web.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.SalvageAttributeSetID:int = obj["SalvageAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SalvagePlanningNumberOfPieces:int = obj["SalvagePlanningNumberOfPieces"]
      """  Salvage planning number of pieces for this attribute set.  """  
      self.SalvagePlanningAttributeSetID:int = obj["SalvagePlanningAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SalvageRevisionNum:str = obj["SalvageRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcQuoteOpDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.   System assigned.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Used to link back to the QuoteLine.   System assigned.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Used to link back to the QuoteAsmbl record.  System assigned.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Used to link back to the QuoteOpr record.  System assigned.  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  Uniquely identifies the QuoteOpDtl.  System assigned.  """  
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
      self.SetupBurRate:int = obj["SetupBurRate"]
      """  The burden rate used for setup time.  Used as a default in Job and Quote entry.  """  
      self.ProdBurRate:int = obj["ProdBurRate"]
      """  Burden rate used for production time on an operation. Job and Quoting use it as a default when entering operation details.  """  
      self.SetupLabRate:int = obj["SetupLabRate"]
      """  The labor rate used for setup time.  Used as a default in Job and Quote entry.  """  
      self.ProdLabRate:int = obj["ProdLabRate"]
      """  Labor rate used for production time on an operation. Job and Quoting use it as a default when entering operation details.  """  
      self.SetupOrProd:str = obj["SetupOrProd"]
      """  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "S", indicating the resource is RequiredFor the Setup phase of this operation, "P" for Production phase, or "B" meaning Both setup and production phase.  """  
      self.OpDtlDesc:str = obj["OpDtlDesc"]
      """  Description is initially created when the QuoteOpDtl is created.   If the QuoteOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
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
      self.OverrideRates:bool = obj["OverrideRates"]
      """  If yes then the user has overridden the rates that were on the  record when it was inititally created.  The initial rates came from the master files.  """  
      self.ConcurrentCapacity:int = obj["ConcurrentCapacity"]
      """  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  """  
      self.DailyProdRate:int = obj["DailyProdRate"]
      """  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Duplicated from QuoteOper.SetupCrewSize.   It's the number of people it physically takes to set up this operation.  It is used as a multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation.  This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Duplicated from QuoteOper.ProdCrewSize.  The number of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee.  See also SetUpCrewSize.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcQuoteOprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The QuoteLine that record is related to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The AssemblySeq number of the related QuoteAsm record.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Quote/Line/Assembly. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last QuoteOpr for the QuoteLine/Asm and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Master Code - Links the QuoteOpr  record with a OpMaster record.  Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  """  
      self.OpStdID:str = obj["OpStdID"]
      """   The Operation standard ID. This links the JobOPer to the OpStd master file. This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.

Valid for "inside operations" only.  """  
      self.EstSetHours:int = obj["EstSetHours"]
      """  The TOTAL estimated set up hours FOR ALL MACHINES. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours * Machines.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """   The production standard for the operation. It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours. A value can be defaulted from the OpStd master.

NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  """  
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field.  The valid qualifiers are:

"HP" - Hours/Piece, "MP" - Minutes/Piece, "PH" - Pieces/Hour,

"PM" - Pieces/Minute, "OH" - Operations/Hour,

"OM"  - Operations/Minute, HR - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor to the number of pieces. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.

This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  """  
      self.OpsPerPart:int = obj["OpsPerPart"]
      """  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Production Quantity per one of the Parent Item.  """  
      self.ProdLabRate:int = obj["ProdLabRate"]
      """  Labor rate used for estimated production labor costs. Default from the OpMaster.QProdLRate if not zero, else OpMaster.ProdLRate.  """  
      self.SetupLabRate:int = obj["SetupLabRate"]
      """  Labor rate for estimated setup labor costs. Default from the OpMaster.QSetupLRate if not zero, else OpMaster.SetupLabRate.  """  
      self.ProdBurRate:int = obj["ProdBurRate"]
      """  The burden rate to be used for the production time on this operation. (EstProdHrs X ProdBurRate). Default from the WrkCenter.QProdBurRate if not zero, else WrkCenter.ProdBurRate.  """  
      self.SetupBurRate:int = obj["SetupBurRate"]
      """  The burden rate to be used for the Setup time on this operation. (EstSetHours X ProdBurRate). Default from the WrkCenter.QSetUpBurRate if not zero, else WrkCenter.SetupBurRate.  """  
      self.Machines:int = obj["Machines"]
      """  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is, the more machines the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, NOT SETUP.  The stored setup hours is a total for all machines.  This stored number is divided by the number of machines when it is displayed on the screen during operation maintenance.  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Defaulted from the WrkCenter.SetUpCrewSize field.  It's the number of people it physically takes to set up this operation.  It is used as a multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation.  This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Defaults from the WrkCenter.ProdCrewSize. The number of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee.  See also SetUpCrewSize.  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap (fallout) that is expected to occur on this operation. The scrap increase the Run quantity. Example; need 1000 pieces scrap of 10 % will show a operation run quantity of 1100.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  Issue Unit of Measure. Applicable only when SubContract = Yes  """  
      self.DaysOut:int = obj["DaysOut"]
      """  Hours required is calculated as days * 8. Only Applicable when SubContract = Yes.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum to be shipped to the subcontract. Applicable only when SubContract = Yes.  Default the QuoteDtl.PartNum or QuoteAsm.PartNum depending on the QuoteOpr.AssemblySeq.  """  
      self.Description:str = obj["Description"]
      """  Description of item to be sent to subcontractor.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for quote operation comments.  """  
      self.SchedRelation:str = obj["SchedRelation"]
      """   Indicates the scheduling relationship between this and the preceding  operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  """  
      self.MinimumCost:int = obj["MinimumCost"]
      """  Minimum Cost that will be used for subcontract costs. That is if the system will take the greater of (required quantity * unit cost) or (MinimumCost) when calculating the subcontract cost for the quote.  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  Estimated Unit Cost. May be defaulted from the appropriate Part master cost fields. Quoting allows multiple unit costs to be entered for quantity price breaks via PBQty & PBCost arrays. The price break logic considers the EstUnitCost field as the lowest element in the price break structure. That is if you had price breaks for quantities of 100, 500 and 1000. Then the EstUnitCost would represent the cost if the required qty is 1 - 99.  """  
      self.AddlSetupHours:int = obj["AddlSetupHours"]
      """  Additional Setup Hours that will be required after a certain quantity has been run for this operation. The quantity at which this occurs is established in AddSetupQty field. The system determines the setup hours as SetupHrs + (Max((RunQty - AddlSetupQty,0))/AddlSetUpQty) * AddlSetupHours. Any fractional results of the AddlSetUpQty calcs are rounded up to the next whole number before multiplying by the AddlSetUpHours..  """  
      self.AddlSetUpQty:int = obj["AddlSetUpQty"]
      """  Additional Setup quantity indicates the quantity at which additional setup time will be incurred.  """  
      self.RunQty:int = obj["RunQty"]
      """  Specifies the total production quantity for this operation. This is an application calculated field used for display purposes only. If no quantity is calculated, the default quantity displays the value of one. The value that displays in this field calculates as follows: Run Quantity = Scrap Quantity + Production Quantity. Note: The Run Qty value refreshes when maintenance is performed on the operation record or the assemblies production quantity is changed.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...).
Defaulted from VendPart.MiscAmt. This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  """  
      self.WIQueStartDate:str = obj["WIQueStartDate"]
      """  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  """  
      self.WIQueStartHour:int = obj["WIQueStartHour"]
      """  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  Used for scheduling a quote.  This date is only valid for the quantity and date the user entered for Quote Scheduling.  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling, and it only valid for the Date/Quantity the user entered in quote scheduling.  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIMoveDueDate:str = obj["WIMoveDueDate"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIMoveDueHour:int = obj["WIMoveDueHour"]
      """  Used for scheduling.  Only valid for the Date and Quantity the user entered in quote scheduling.  """  
      self.WIHoursPerMachine:int = obj["WIHoursPerMachine"]
      """  The Number of Hours per machine per day that this operations "actual" schedule is based on.  Used in logic of quote scheduling.  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this quote operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this quote subcontract operation.  Can be zero if RFQ(s) are not required.  """  
      self.FAQty:int = obj["FAQty"]
      """  The quantity requested for first article inspection.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQ number that the item is linked to.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.RFQStat:str = obj["RFQStat"]
      """   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  """  
      self.SetupGroup:str = obj["SetupGroup"]
      """  Used to group operation to save on setups.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PrimarySetupOpDtl:int = obj["PrimarySetupOpDtl"]
      """   Identifies the primary QuoteOpDtl to be used for setup.  The setup time for the operation is determined on the QuoteOpDtl.
If <> 0, must identify a valid QuoteOpDtl.  The QuoteOpDtl needs to have a RequiredFor = S or B.  """  
      self.PrimaryProdOpDtl:int = obj["PrimaryProdOpDtl"]
      """   Identifies the primary QuoteOpDtl to be used for production.  The production run time for the operation is determined on the QuoteOpDtl.
If <> 0, must identify a valid QuoteOpDtl.  The QuoteOpDtl needs to have a RequiredFor = P or B.  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Operation Description.  """  
      self.GlbRFQ:bool = obj["GlbRFQ"]
      """  Global RFQ flag.  Used in Consolidated Purchasing.  """  
      self.BrkQty07:int = obj["BrkQty07"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty08:int = obj["BrkQty08"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty09:int = obj["BrkQty09"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty10:int = obj["BrkQty10"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.PBrkCost01:int = obj["PBrkCost01"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost02:int = obj["PBrkCost02"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost03:int = obj["PBrkCost03"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost04:int = obj["PBrkCost04"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost05:int = obj["PBrkCost05"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost06:int = obj["PBrkCost06"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost07:int = obj["PBrkCost07"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost08:int = obj["PBrkCost08"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost09:int = obj["PBrkCost09"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkCost10:int = obj["PBrkCost10"]
      """  If subcontract then this is unit cost for the corresponding price break quantity. (BreakQty)  """  
      self.PBrkStdRate01:int = obj["PBrkStdRate01"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate02:int = obj["PBrkStdRate02"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate03:int = obj["PBrkStdRate03"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate04:int = obj["PBrkStdRate04"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate05:int = obj["PBrkStdRate05"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate06:int = obj["PBrkStdRate06"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate07:int = obj["PBrkStdRate07"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate08:int = obj["PBrkStdRate08"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate09:int = obj["PBrkStdRate09"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.PBrkStdRate10:int = obj["PBrkStdRate10"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantity.  """  
      self.BrkQty01:int = obj["BrkQty01"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty02:int = obj["BrkQty02"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty03:int = obj["BrkQty03"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty04:int = obj["BrkQty04"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty05:int = obj["BrkQty05"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty06:int = obj["BrkQty06"]
      """  Price break/production break quantity, quantity at which a price break occurs for subcontracting or a production break occurs for internal operations. The quantity represents the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.SNRequiredOpr:bool = obj["SNRequiredOpr"]
      """  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  """  
      self.SNRequiredSubConShip:bool = obj["SNRequiredSubConShip"]
      """  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  """  
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
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.TemplateID:str = obj["TemplateID"]
      """  TemplateID  """  
      self.StageNumber:str = obj["StageNumber"]
      """  StageNumber  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcRuleSetResultRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RuleSetID:int = obj["RuleSetID"]
      self.RuleTag:str = obj["RuleTag"]
      self.BOMElementTableName:str = obj["BOMElementTableName"]
      self.BOMElementSysRowID:str = obj["BOMElementSysRowID"]
      self.TestType:str = obj["TestType"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      self.KeepIt:bool = obj["KeepIt"]
      self.KWExpression:str = obj["KWExpression"]
      self.AsmPartNum:str = obj["AsmPartNum"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.ExprToolTip:str = obj["ExprToolTip"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcRulesResultRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RuleSetID:int = obj["RuleSetID"]
      self.RuleSeq:int = obj["RuleSeq"]
      self.ProcessSeq:int = obj["ProcessSeq"]
      self.RuleType:str = obj["RuleType"]
      self.RuleTag:str = obj["RuleTag"]
      self.ExpressionText:str = obj["ExpressionText"]
      self.ExprResult:str = obj["ExprResult"]
      self.TestType:str = obj["TestType"]
      self.ExprToolTip:str = obj["ExprToolTip"]
      self.BOMElementSysRowID:str = obj["BOMElementSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcStrCompRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of the associated configurator  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the associated configurator  """  
      self.PosOrder:int = obj["PosOrder"]
      """  Position order  """  
      self.CompName:str = obj["CompName"]
      """  Name  """  
      self.CompType:str = obj["CompType"]
      """  Type  """  
      self.CompDataType:str = obj["CompDataType"]
      """  Data Type  """  
      self.DisplayFormat:str = obj["DisplayFormat"]
      """  Display Format  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.SmartStringStart:int = obj["SmartStringStart"]
      """  Defines a starting position for the value of this input in a smart string  """  
      self.SmartStringEnd:int = obj["SmartStringEnd"]
      """  Defines an ending position for the value of this input in a smart string  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then fields on the record may be updated  """  
      self.DateFormat:str = obj["DateFormat"]
      """  The coded format to use for a Date component  """  
      self.DateSeparator:str = obj["DateSeparator"]
      """  The separator to use for a date component  """  
      self.DateFourDigitYear:bool = obj["DateFourDigitYear"]
      """  If True a 4 digit year will be used for the date  """  
      self.DateThreeCharMonth:bool = obj["DateThreeCharMonth"]
      """  Use a 3 character month instead of a numeric month  """  
      self.LogicalFormat:str = obj["LogicalFormat"]
      """  A coded value indicating the format to use for a logical component  """  
      self.LogicalTrueValue:str = obj["LogicalTrueValue"]
      """  The value to use for a True logical value  """  
      self.LogicalFalseValue:str = obj["LogicalFalseValue"]
      """  The value to use for a False logical value  """  
      self.PossibleValues:str = obj["PossibleValues"]
      """  The possible values for a Radio-Set, Combo-Box, or validated Character Fill-In  """  
      self.CanFormat:bool = obj["CanFormat"]
      """  True if formatting can be applied to the component  """  
      self.SmartStringSeparator:str = obj["SmartStringSeparator"]
      self.NumberDecimals:int = obj["NumberDecimals"]
      """  Number of decimals  """  
      self.NumberDigits:int = obj["NumberDigits"]
      """  Number of digits.  """  
      self.NumberNegatives:str = obj["NumberNegatives"]
      """  Type of negatives.  """  
      self.NumberThousands:bool = obj["NumberThousands"]
      """  Thousands' separator.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcStructRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company ID  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of the parent configured part number  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the parent configured part number  """  
      self.ConfLabel:str = obj["ConfLabel"]
      """  An optional label to identify the purpose of the sub configurator rule.  """  
      self.SubPartNum:str = obj["SubPartNum"]
      """  Sub assembly configured part number that can be run from this configurator based on the condition of this rule  """  
      self.SubRevisionNum:str = obj["SubRevisionNum"]
      """  The revision number of the configurator that can be run from this configurator based on the condition of this rule  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Optional field.  The sales companies do not have the manufacturing information available but the manufacturing company must put the result of the sub configurator somewhere in the method.  The field has 3 options, E (Equal), G (Greater Than), L (Less Than).  The result of this rule will be inserted in the BOM in the location specified in this field.  If no value is entered, the result will be appended at the end of the BOM structure.  """  
      self.Comments:str = obj["Comments"]
      """  Comments describing the structure rule  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Default operation sequence  """  
      self.RuleTag:str = obj["RuleTag"]
      """  Rule Tag  """  
      self.AsmPartNum:str = obj["AsmPartNum"]
      """  Stores the assembly part number within the multi-level BOM for which the rule is related.  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Ex: Customization, Personalization  """  
      self.StructID:int = obj["StructID"]
      """  StructID  """  
      self.RelatedTo:str = obj["RelatedTo"]
      """  RelatedTo  """  
      self.RelatedToID:str = obj["RelatedToID"]
      """  RelatedToID  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      """  DisplaySeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.E9PcInValueRuleTag:str = obj["E9PcInValueRuleTag"]
      """  E9PcInValueRuleTag  """  
      self.BasePartNum:str = obj["BasePartNum"]
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      self.CanUpdate:bool = obj["CanUpdate"]
      self.ConfigSysRowID:str = obj["ConfigSysRowID"]
      self.ConfigType:str = obj["ConfigType"]
      self.ConfigVersion:int = obj["ConfigVersion"]
      self.CreatePart:bool = obj["CreatePart"]
      self.DefaultECO:str = obj["DefaultECO"]
      self.DisplayTag:str = obj["DisplayTag"]
      self.KeepIt:bool = obj["KeepIt"]
      self.NewPartNum:str = obj["NewPartNum"]
      self.OverwriteSIValues:bool = obj["OverwriteSIValues"]
      self.ParentNewAsm:str = obj["ParentNewAsm"]
      self.PromptForAutoCreate:bool = obj["PromptForAutoCreate"]
      self.PromptForCheckout:bool = obj["PromptForCheckout"]
      self.PromptForPart:bool = obj["PromptForPart"]
      self.PromptForSIValues:bool = obj["PromptForSIValues"]
      self.ResponseAutoCreatePart:bool = obj["ResponseAutoCreatePart"]
      self.RevExists:bool = obj["RevExists"]
      self.RevolvingSeq:int = obj["RevolvingSeq"]
      """  Revolving Sequence  """  
      self.SavedGroupSeq:int = obj["SavedGroupSeq"]
      self.SaveHeadNum:int = obj["SaveHeadNum"]
      self.SIGroupSeq:int = obj["SIGroupSeq"]
      self.SIHeadNum:int = obj["SIHeadNum"]
      self.SmartString:str = obj["SmartString"]
      self.SourceSysRowID:str = obj["SourceSysRowID"]
      """  Calculated source table name, if the RelatedTo is "Part" then this column will contain "PartRe the PartRev.SysRowID and SourceTableName will have "PartRev", otherwise both columns will be blank. For non PC configurators the source row is the same across parent and child configurators.  """  
      self.SourceTableName:str = obj["SourceTableName"]
      """  Calculated source table name, if the RelatedTo is "Part" then this column will contain "PartRev" and SourceSysRowID will contain the PartRev.SysRowID, otherwise both columns will be blank. For non PC configurators the source row is the same across parent and child configurators.  """  
      self.StructTag:str = obj["StructTag"]
      self.SubBasePartNum:str = obj["SubBasePartNum"]
      self.SubBaseRevisionNum:str = obj["SubBaseRevisionNum"]
      self.SubConfigID:str = obj["SubConfigID"]
      self.UseKeepWhen:bool = obj["UseKeepWhen"]
      self.ParentStructID:int = obj["ParentStructID"]
      self.GenerateMethod:bool = obj["GenerateMethod"]
      self.BitFlag:int = obj["BitFlag"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartIUM:str = obj["PartIUM"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcTestResultRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TestType:str = obj["TestType"]
      self.TestDesc:str = obj["TestDesc"]
      self.ConfigID:str = obj["ConfigID"]
      self.SourceEntity:str = obj["SourceEntity"]
      self.TargetEntity:str = obj["TargetEntity"]
      self.ShowOnTree:bool = obj["ShowOnTree"]
      """  This flag is used on the client side to filter the current test that should be displayed on the tree. Only one record should have this value set to TRUE.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcTestResultsTableset:
   def __init__(self, obj):
      self.PcTestResult:list[Erp_Tablesets_PcTestResultRow] = obj["PcTestResult"]
      self.PcAsmResult:list[Erp_Tablesets_PcAsmResultRow] = obj["PcAsmResult"]
      self.PcMtlResult:list[Erp_Tablesets_PcMtlResultRow] = obj["PcMtlResult"]
      self.PcOprResult:list[Erp_Tablesets_PcOprResultRow] = obj["PcOprResult"]
      self.PcOpDtlResult:list[Erp_Tablesets_PcOpDtlResultRow] = obj["PcOpDtlResult"]
      self.PcRuleSetResult:list[Erp_Tablesets_PcRuleSetResultRow] = obj["PcRuleSetResult"]
      self.PcRulesResult:list[Erp_Tablesets_PcRulesResultRow] = obj["PcRulesResult"]
      self.PcActionResult:list[Erp_Tablesets_PcActionResultRow] = obj["PcActionResult"]
      self.MethodsList:list[Erp_Tablesets_MethodsListRow] = obj["MethodsList"]
      self.PcJobAsmbl:list[Erp_Tablesets_PcJobAsmblRow] = obj["PcJobAsmbl"]
      self.PcJobHead:list[Erp_Tablesets_PcJobHeadRow] = obj["PcJobHead"]
      self.PcJobMtl:list[Erp_Tablesets_PcJobMtlRow] = obj["PcJobMtl"]
      self.PcJobOpDtl:list[Erp_Tablesets_PcJobOpDtlRow] = obj["PcJobOpDtl"]
      self.PcJobOper:list[Erp_Tablesets_PcJobOperRow] = obj["PcJobOper"]
      self.PcKitCompResult:list[Erp_Tablesets_PcKitCompResultRow] = obj["PcKitCompResult"]
      self.PcQuoteAsm:list[Erp_Tablesets_PcQuoteAsmRow] = obj["PcQuoteAsm"]
      self.PcQuoteDtl:list[Erp_Tablesets_PcQuoteDtlRow] = obj["PcQuoteDtl"]
      self.PcQuoteHed:list[Erp_Tablesets_PcQuoteHedRow] = obj["PcQuoteHed"]
      self.PcQuoteMtl:list[Erp_Tablesets_PcQuoteMtlRow] = obj["PcQuoteMtl"]
      self.PcQuoteOpDtl:list[Erp_Tablesets_PcQuoteOpDtlRow] = obj["PcQuoteOpDtl"]
      self.PcQuoteOpr:list[Erp_Tablesets_PcQuoteOprRow] = obj["PcQuoteOpr"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PcUserDefinedMethodParametersRow:
   def __init__(self, obj):
      self.BoolValue:bool = obj["BoolValue"]
      self.Company:str = obj["Company"]
      self.ConfigID:str = obj["ConfigID"]
      self.DateTimeValue:str = obj["DateTimeValue"]
      self.DecimalValue:int = obj["DecimalValue"]
      self.FunctionName:str = obj["FunctionName"]
      self.IntValue:int = obj["IntValue"]
      self.Modifier:str = obj["Modifier"]
      self.ParameterName:str = obj["ParameterName"]
      self.ParamSeq:int = obj["ParamSeq"]
      self.ParamType:str = obj["ParamType"]
      self.StringValue:str = obj["StringValue"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcValueGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  RelatedToTableName  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  RelatedToSysRowID  """  
      self.CreateDate:str = obj["CreateDate"]
      """  CreateDate  """  
      self.CreateUserID:str = obj["CreateUserID"]
      """  CreateUserID  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  LastUpdated  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  LastUpdatedBy  """  
      self.ConfigStatus:str = obj["ConfigStatus"]
      """  ConfigStatus  """  
      self.SIValues:bool = obj["SIValues"]
      """  SIValues  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcValueGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  RelatedToTableName  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  RelatedToSysRowID  """  
      self.CreateDate:str = obj["CreateDate"]
      """  CreateDate  """  
      self.CreateUserID:str = obj["CreateUserID"]
      """  CreateUserID  """  
      self.LastUpdated:str = obj["LastUpdated"]
      """  LastUpdated  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  LastUpdatedBy  """  
      self.ConfigStatus:str = obj["ConfigStatus"]
      """  ConfigStatus  """  
      self.SIValues:bool = obj["SIValues"]
      """  SIValues  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DisplaySummary:bool = obj["DisplaySummary"]
      self.IncomingSmartString:bool = obj["IncomingSmartString"]
      self.TestID:str = obj["TestID"]
      """  Indicates if this value group was created because of a test (test inputs or test rules).  """  
      self.TestMode:str = obj["TestMode"]
      """  Indicates the test mode of this value group, note that TestID should be populated with a non empty Guid to make sure that all programs are generated as a test. Then this column will indicate if rules or anything else should be tested too.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcValueHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum  """  
      self.StructTag:str = obj["StructTag"]
      """  StructTag  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.RevolvingSeq:int = obj["RevolvingSeq"]
      """  RevolvingSeq  """  
      self.ForeignTableName:str = obj["ForeignTableName"]
      """  ForeignTableName  """  
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      """  ForeignSysRowID  """  
      self.SourceTableName:str = obj["SourceTableName"]
      """  SourceTableName  """  
      self.SourceSysRowID:str = obj["SourceSysRowID"]
      """  SourceSysRowID  """  
      self.ConfigType:str = obj["ConfigType"]
      """  ConfigType  """  
      self.ConfigVersion:int = obj["ConfigVersion"]
      """  ConfigVersion  """  
      self.DisplayTag:str = obj["DisplayTag"]
      """  DisplayTag  """  
      self.RuleTag:str = obj["RuleTag"]
      """  RuleTag  """  
      self.ExtConfig:bool = obj["ExtConfig"]
      """  ExtConfig  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  ExtCompany  """  
      self.AllowRecordCreation:bool = obj["AllowRecordCreation"]
      """  AllowRecordCreation  """  
      self.AllowPricing:bool = obj["AllowPricing"]
      """  AllowPricing  """  
      self.PromptForConfig:bool = obj["PromptForConfig"]
      """  PromptForConfig  """  
      self.InSmartString:bool = obj["InSmartString"]
      """  InSmartString  """  
      self.DisplaySummary:bool = obj["DisplaySummary"]
      """  DisplaySummary  """  
      self.AllowReconfig:bool = obj["AllowReconfig"]
      """  AllowReconfig  """  
      self.IsMainForeign:bool = obj["IsMainForeign"]
      """  IsMainForeign  """  
      self.NewPartNum:str = obj["NewPartNum"]
      """  NewPartNum  """  
      self.NewSmartString:str = obj["NewSmartString"]
      """  NewSmartString  """  
      self.SIValues:bool = obj["SIValues"]
      """  SIValues  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SIValuesGroupSeq:int = obj["SIValuesGroupSeq"]
      self.TestID:str = obj["TestID"]
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  Copied from the parent PcValueGrp record  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  Value is brought from the parent PcValueGroup record.  """  
      self.SIValuesHeadNum:int = obj["SIValuesHeadNum"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcValueInputLayerDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.InputName:str = obj["InputName"]
      """  Input Name  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  Image Layer ID  """  
      self.LayerSeq:int = obj["LayerSeq"]
      """  Programmatically calculated value used to keep the rows unique.  """  
      self.LayerName:str = obj["LayerName"]
      """  LayerName  """  
      self.LayerDesc:str = obj["LayerDesc"]
      """  LayerDesc  """  
      self.ZIndex:int = obj["ZIndex"]
      """  ZIndex  """  
      self.ImageID:str = obj["ImageID"]
      """  Image ID  """  
      self.FileType:str = obj["FileType"]
      """  Png file types are supported  """  
      self.Width:int = obj["Width"]
      """  Width  """  
      self.Height:int = obj["Height"]
      """  Height  """  
      self.Category:str = obj["Category"]
      """  Free form text  """  
      self.xPos:int = obj["xPos"]
      """  Reserved for future development  """  
      self.yPos:int = obj["yPos"]
      """  Reserved for future development  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcValueInputLayerHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.InputName:str = obj["InputName"]
      """  Input Name  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  Image Layer ID  """  
      self.ImageID:str = obj["ImageID"]
      """  Image ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ImageURL:str = obj["ImageURL"]
      """  Location of Image  """  
      self.FileType:str = obj["FileType"]
      """  FileType  """  
      self.Width:int = obj["Width"]
      """  Width  """  
      self.Height:int = obj["Height"]
      """  Height  """  
      self.Version:int = obj["Version"]
      """  Used by Verify Configuration to identify changes in the layer definition.  """  
      self.xPos:int = obj["xPos"]
      """  Reserved for future development  """  
      self.yPos:int = obj["yPos"]
      """  Reserved for future development  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcValueTableset:
   def __init__(self, obj):
      self.PcValueHead:list[Erp_Tablesets_PcValueHeadRow] = obj["PcValueHead"]
      self.PcConfiguredDrawings:list[Erp_Tablesets_PcConfiguredDrawingsRow] = obj["PcConfiguredDrawings"]
      self.PcContextProperties:list[Erp_Tablesets_PcContextPropertiesRow] = obj["PcContextProperties"]
      self.PcFieldPropertiesTransport:list[Erp_Tablesets_PcFieldPropertiesTransportRow] = obj["PcFieldPropertiesTransport"]
      self.PcUserDefinedMethodParameters:list[Erp_Tablesets_PcUserDefinedMethodParametersRow] = obj["PcUserDefinedMethodParameters"]
      self.PcValueInputLayerDetail:list[Erp_Tablesets_PcValueInputLayerDetailRow] = obj["PcValueInputLayerDetail"]
      self.PcValueInputLayerHeader:list[Erp_Tablesets_PcValueInputLayerHeaderRow] = obj["PcValueInputLayerHeader"]
      self.PcValueTransport:list[Erp_Tablesets_PcValueTransportRow] = obj["PcValueTransport"]
      self.PcVariableTransport:list[Erp_Tablesets_PcVariableTransportRow] = obj["PcVariableTransport"]
      self.QBuildMapping:list[Erp_Tablesets_QBuildMappingRow] = obj["QBuildMapping"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PcValueTransportRow:
   def __init__(self, obj):
      self.GroupSeq:int = obj["GroupSeq"]
      self.HeadNum:int = obj["HeadNum"]
      self.InputName:str = obj["InputName"]
      self.InputType:str = obj["InputType"]
      self.InputValue:str = obj["InputValue"]
      self.PageSeq:int = obj["PageSeq"]
      self.ValueSetSeq:int = obj["ValueSetSeq"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcVariableTransportRow:
   def __init__(self, obj):
      self.GroupSeq:int = obj["GroupSeq"]
      """  PcVariable group sequence.  """  
      self.ValueSetSeq:int = obj["ValueSetSeq"]
      """  PcVariable Value set sequence  """  
      self.VarDataType:str = obj["VarDataType"]
      """  PcVariable data type.  """  
      self.VarName:str = obj["VarName"]
      """  PcVariable var name.  """  
      self.VarValue:str = obj["VarValue"]
      """  PcVariable value.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QBuildMappingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.InputName:str = obj["InputName"]
      """  Input Name  """  
      self.ObjName:str = obj["ObjName"]
      """  This is the object name.  """  
      self.ObjParameter:str = obj["ObjParameter"]
      """  This is the name of the object parameter.  """  
      self.MappedInputName:str = obj["MappedInputName"]
      """  Name of the input mapped to this object parameter.  """  
      self.ObjParameterDataType:str = obj["ObjParameterDataType"]
      """  This is the data type of the object parameter.  """  
      self.ObjParameterInitValue:str = obj["ObjParameterInitValue"]
      """  This is the initial value of the object parameter as it was defined in the designer.  This is reserved for future development.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DataType:str = obj["DataType"]
      self.PageSeq:int = obj["PageSeq"]
      self.BitFlag:int = obj["BitFlag"]
      self.QBuildObjObjType:str = obj["QBuildObjObjType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtConfigurationRuntimeTableset:
   def __init__(self, obj):
      self.PcValueGrp:list[Erp_Tablesets_PcValueGrpRow] = obj["PcValueGrp"]
      self.PcValueHead:list[Erp_Tablesets_PcValueHeadRow] = obj["PcValueHead"]
      self.PcConfigurationParams:list[Erp_Tablesets_PcConfigurationParamsRow] = obj["PcConfigurationParams"]
      self.PcConfiguredDrawings:list[Erp_Tablesets_PcConfiguredDrawingsRow] = obj["PcConfiguredDrawings"]
      self.PcContextProperties:list[Erp_Tablesets_PcContextPropertiesRow] = obj["PcContextProperties"]
      self.PcInputsLayerDetail:list[Erp_Tablesets_PcInputsLayerDetailRow] = obj["PcInputsLayerDetail"]
      self.PcInputsLayerHeader:list[Erp_Tablesets_PcInputsLayerHeaderRow] = obj["PcInputsLayerHeader"]
      self.PcInputsPublishToDocParams:list[Erp_Tablesets_PcInputsPublishToDocParamsRow] = obj["PcInputsPublishToDocParams"]
      self.PcInputVar:list[Erp_Tablesets_PcInputVarRow] = obj["PcInputVar"]
      self.PcValueInputLayerDetail:list[Erp_Tablesets_PcValueInputLayerDetailRow] = obj["PcValueInputLayerDetail"]
      self.PcValueInputLayerHeader:list[Erp_Tablesets_PcValueInputLayerHeaderRow] = obj["PcValueInputLayerHeader"]
      self.QBuildMapping:list[Erp_Tablesets_QBuildMappingRow] = obj["QBuildMapping"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExecuteDataLookup_input:
   """ Required : 
   methodName
   configId
   testId
   inParams
   """  
   def __init__(self, obj):
      self.methodName:str = obj["methodName"]
      self.configId:str = obj["configId"]
      self.testId:str = obj["testId"]
      self.inParams:str = obj["inParams"]
      pass

class ExecuteDataLookup_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ExecuteGenerateFullImageLayerScriptCode_input:
   """ Required : 
   imageLayersInfo
   """  
   def __init__(self, obj):
      self.imageLayersInfo:list[System_Collections_Generic_KeyValuePair_System_String_System_String] = obj["imageLayersInfo"]
      pass

class ExecuteGenerateFullImageLayerScriptCode_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ExecuteGenerateImageLayerScriptCode_input:
   """ Required : 
   imageLayerID
   """  
   def __init__(self, obj):
      self.imageLayerID:str = obj["imageLayerID"]
      """  The Image Layer ID to be used for script generation  """  
      pass

class ExecuteGenerateImageLayerScriptCode_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Returns the generated script code to be used by an EpiEOWebBrowser control.  """  
      pass

class ExecuteGenerateSingleImageLayerScriptCode_input:
   """ Required : 
   imageLayerID
   zIndex
   imageValue
   layerSeq
   """  
   def __init__(self, obj):
      self.imageLayerID:str = obj["imageLayerID"]
      """  The Image Layer ID to be used for script generation  """  
      self.zIndex:int = obj["zIndex"]
      """  The Zindex value to be used for script generation. ZIndex determines the order in which the layers are displayed.  """  
      self.imageValue:str = obj["imageValue"]
      """  The image to be used on script generation.  """  
      self.layerSeq:int = obj["layerSeq"]
      """  The layer index that belongs to the modified layer.  """  
      pass

class ExecuteGenerateSingleImageLayerScriptCode_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Returns the generated script code to be used by an EpiEOWebBrowser control.  """  
      pass

class ExecutePageOnLoadEvents_input:
   """ Required : 
   pageLoadEvent
   configID
   testID
   pcValueDS
   """  
   def __init__(self, obj):
      self.pageLoadEvent:str = obj["pageLoadEvent"]
      self.configID:str = obj["configID"]
      self.testID:str = obj["testID"]
      self.pcValueDS:list[Erp_Tablesets_PcValueTableset] = obj["pcValueDS"]
      pass

class ExecutePageOnLoadEvents_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcValueDS:list[Erp_Tablesets_PcValueTableset] = obj["pcValueDS"]
      pass

      """  output parameters  """  

class ExecuteUserDefinedWithArrayReturn_input:
   """ Required : 
   methodName
   configID
   testID
   pcValueDS
   """  
   def __init__(self, obj):
      self.methodName:str = obj["methodName"]
      """  The name of the server-side UDmethod to execute.  """  
      self.configID:str = obj["configID"]
      """  The ID of the configurator the UDmethod is tied to.  """  
      self.testID:str = obj["testID"]
      """  When executing under a test (Test Inputs/Rules) this parameter should contain a valid System.Guid, otherwise it can be System.Guid.Empty  """  
      self.pcValueDS:list[Erp_Tablesets_PcValueTableset] = obj["pcValueDS"]
      pass

class ExecuteUserDefinedWithArrayReturn_output:
   def __init__(self, obj):
      self.returnObj:object
      pass

   def parameters(self, obj):
      self.pcValueDS:list[Erp_Tablesets_PcValueTableset] = obj["pcValueDS"]
      pass

      """  output parameters  """  

class ExecuteUserDefined_input:
   """ Required : 
   methodName
   configID
   testID
   pcValueDS
   """  
   def __init__(self, obj):
      self.methodName:str = obj["methodName"]
      self.configID:str = obj["configID"]
      self.testID:str = obj["testID"]
      self.pcValueDS:list[Erp_Tablesets_PcValueTableset] = obj["pcValueDS"]
      pass

class ExecuteUserDefined_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

   def parameters(self, obj):
      self.pcValueDS:list[Erp_Tablesets_PcValueTableset] = obj["pcValueDS"]
      pass

      """  output parameters  """  

class GetAllImages_input:
   """ Required : 
   inputImageList
   ConfigID
   GroupSeq
   HeadNum
   """  
   def __init__(self, obj):
      self.inputImageList:list[System_Collections_Generic_KeyValuePair_System_String_System_String] = obj["inputImageList"]
      """  List of images used in the configurator  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configurator ID to retrieve the drawings and images  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  Group Sequence for the reconfigure scenarios  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Head Number that represents the configuration in the structure of a multi level configurator  """  
      pass

class GetAllImages_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PcImagesTableset] = obj["returnObj"]
      pass

class GetAllPictureBoxImages_input:
   """ Required : 
   inputImageList
   """  
   def __init__(self, obj):
      self.inputImageList:list[System_Collections_Generic_KeyValuePair_System_String_System_String] = obj["inputImageList"]
      """  list of images for the current panel in the configuration.  The key is the input name.  The value is the image name.  """  
      pass

class GetAllPictureBoxImages_output:
   def __init__(self, obj):
      self.returnObj:list[System_Collections_Generic_KeyValuePair_System_String_System_ByteArray] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   groupSeq
   """  
   def __init__(self, obj):
      self.groupSeq:int = obj["groupSeq"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["returnObj"]
      pass

class GetECCConfigurator_input:
   """ Required : 
   eccConfigSetup
   """  
   def __init__(self, obj):
      self.eccConfigSetup      #schema had no properties on an object.
      """  eccConfigSetup: json object returned from ECC  """  
      pass

class GetECCConfigurator_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  configuratorContext string  """  
      pass

class GetGeneratedClient_input:
   """ Required : 
   configID
   TestID
   IsTestPlan
   SpecID
   SpecRevNum
   clientCheckSyntaxArgs
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Target configuration to generate, note that company is taken from session.  """  
      self.TestID:str = obj["TestID"]
      """  When executing under a test (Test Inputs/Rules) this parameter should contain a valid System.Guid, otherwise it can be System.Guid.Empty  """  
      self.IsTestPlan:bool = obj["IsTestPlan"]
      """  True when configuring inspection plan configuration  """  
      self.SpecID:str = obj["SpecID"]
      """  Specification ID of inspection plan configuration  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  Specification Revision of inspection plan configuration  """  
      self.clientCheckSyntaxArgs:list[Erp_Shared_Lib_Configurator_ClientCheckSyntaxArgs] = obj["clientCheckSyntaxArgs"]
      pass

class GetGeneratedClient_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  An array of compressed source code strings.  """  
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
      self.returnObj:list[Erp_Tablesets_ConfigurationRuntimeListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPcConfigParams_input:
   """ Required : 
   RuntimeDS
   configID
   uniqueID
   """  
   def __init__(self, obj):
      self.RuntimeDS:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["RuntimeDS"]
      self.configID:str = obj["configID"]
      self.uniqueID:str = obj["uniqueID"]
      pass

class GetNewPcConfigParams_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.RuntimeDS:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["RuntimeDS"]
      pass

      """  output parameters  """  

class GetNewPcInputVar_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["ds"]
      pass

class GetNewPcInputVar_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcInputsLayerDetail_input:
   """ Required : 
   ds
   configID
   inputName
   imageLayerID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.inputName:str = obj["inputName"]
      self.imageLayerID:str = obj["imageLayerID"]
      pass

class GetNewPcInputsLayerDetail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcInputsLayerHeader_input:
   """ Required : 
   ds
   configID
   inputName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.inputName:str = obj["inputName"]
      pass

class GetNewPcInputsLayerHeader_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcInputsPublishToDoc_input:
   """ Required : 
   RuntimeDS
   key
   """  
   def __init__(self, obj):
      self.RuntimeDS:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["RuntimeDS"]
      self.key:str = obj["key"]
      pass

class GetNewPcInputsPublishToDoc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.RuntimeDS:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["RuntimeDS"]
      pass

      """  output parameters  """  

class GetNewPcValueGrp_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["ds"]
      pass

class GetNewPcValueGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcValueHead_input:
   """ Required : 
   ds
   groupSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["ds"]
      self.groupSeq:int = obj["groupSeq"]
      pass

class GetNewPcValueHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcValueInputLayerDetail_input:
   """ Required : 
   ds
   groupSeq
   headNum
   configID
   inputName
   imageLayerID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["ds"]
      self.groupSeq:int = obj["groupSeq"]
      self.headNum:int = obj["headNum"]
      self.configID:str = obj["configID"]
      self.inputName:str = obj["inputName"]
      self.imageLayerID:str = obj["imageLayerID"]
      pass

class GetNewPcValueInputLayerDetail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcValueInputLayerHeader_input:
   """ Required : 
   ds
   groupSeq
   headNum
   configID
   inputName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["ds"]
      self.groupSeq:int = obj["groupSeq"]
      self.headNum:int = obj["headNum"]
      self.configID:str = obj["configID"]
      self.inputName:str = obj["inputName"]
      pass

class GetNewPcValueInputLayerHeader_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQBuildMapping_input:
   """ Required : 
   ds
   configID
   inputName
   objName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.inputName:str = obj["inputName"]
      self.objName:str = obj["objName"]
      pass

class GetNewQBuildMapping_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPCTransportTableset_input:
   """ Required : 
   configurationRuntime
   configurationSequenceTableSet
   """  
   def __init__(self, obj):
      self.configurationRuntime:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["configurationRuntime"]
      self.configurationSequenceTableSet:list[Erp_Tablesets_ConfigurationSequenceTableset] = obj["configurationSequenceTableSet"]
      pass

class GetPCTransportTableset_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PcValueTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.configurationRuntime:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["configurationRuntime"]
      self.configurationSequenceTableSet:list[Erp_Tablesets_ConfigurationSequenceTableset] = obj["configurationSequenceTableSet"]
      pass

      """  output parameters  """  

class GetPictureBoxImage_input:
   """ Required : 
   fileName
   inputName
   """  
   def __init__(self, obj):
      self.fileName:str = obj["fileName"]
      self.inputName:str = obj["inputName"]
      pass

class GetPictureBoxImage_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClausePcValueGrp
   whereClausePcValueHead
   whereClausePcConfigurationParams
   whereClausePcConfiguredDrawings
   whereClausePcContextProperties
   whereClausePcInputsLayerDetail
   whereClausePcInputsLayerHeader
   whereClausePcInputsPublishToDocParams
   whereClausePcInputVar
   whereClausePcValueInputLayerDetail
   whereClausePcValueInputLayerHeader
   whereClauseQBuildMapping
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePcValueGrp:str = obj["whereClausePcValueGrp"]
      self.whereClausePcValueHead:str = obj["whereClausePcValueHead"]
      self.whereClausePcConfigurationParams:str = obj["whereClausePcConfigurationParams"]
      self.whereClausePcConfiguredDrawings:str = obj["whereClausePcConfiguredDrawings"]
      self.whereClausePcContextProperties:str = obj["whereClausePcContextProperties"]
      self.whereClausePcInputsLayerDetail:str = obj["whereClausePcInputsLayerDetail"]
      self.whereClausePcInputsLayerHeader:str = obj["whereClausePcInputsLayerHeader"]
      self.whereClausePcInputsPublishToDocParams:str = obj["whereClausePcInputsPublishToDocParams"]
      self.whereClausePcInputVar:str = obj["whereClausePcInputVar"]
      self.whereClausePcValueInputLayerDetail:str = obj["whereClausePcValueInputLayerDetail"]
      self.whereClausePcValueInputLayerHeader:str = obj["whereClausePcValueInputLayerHeader"]
      self.whereClauseQBuildMapping:str = obj["whereClauseQBuildMapping"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTargetEntityValues_input:
   """ Required : 
   configID
   relatedToTableName
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      self.relatedToTableName:str = obj["relatedToTableName"]
      pass

class GetTargetEntityValues_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.allowRecordCreation:bool = obj["allowRecordCreation"]
      self.useInSmartString:bool = obj["useInSmartString"]
      pass

      """  output parameters  """  

class GetTenantID_input:
   """ Required : 
   company
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  company  """  
      pass

class GetTenantID_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Tenant ID  """  
      pass

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

class PartExists_input:
   """ Required : 
   configID
   targetEntity
   groupSeq
   basePartNum
   baseRevisionNum
   newPartNum
   mtlSeq
   ruleTag
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration ID  """  
      self.targetEntity:str = obj["targetEntity"]
      """  Target Entity - table name being processed by the configurator  """  
      self.groupSeq:int = obj["groupSeq"]
      """  Configuaration PcValueGrp.GroupSeq  """  
      self.basePartNum:str = obj["basePartNum"]
      """  Base Part Number  """  
      self.baseRevisionNum:str = obj["baseRevisionNum"]
      """  Base Revision Number  """  
      self.newPartNum:str = obj["newPartNum"]
      """  The part being configured  """  
      self.mtlSeq:int = obj["mtlSeq"]
      """  Material Sequence of the revision being configured  """  
      self.ruleTag:str = obj["ruleTag"]
      """  Generated Rule Tag of the part being configured  """  
      pass

class PartExists_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partExists:bool = obj["partExists"]
      self.notUnique:bool = obj["notUnique"]
      self.sIValues:bool = obj["sIValues"]
      pass

      """  output parameters  """  

class PartRevExists_input:
   """ Required : 
   ipPartNum
   ipRevisionNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      pass

class PartRevExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class PreStartConfiguration_input:
   """ Required : 
   configurationRuntimeDS
   configurationSummaryTS
   """  
   def __init__(self, obj):
      self.configurationRuntimeDS:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["configurationRuntimeDS"]
      self.configurationSummaryTS:list[Erp_Tablesets_ConfigurationSummaryTableset] = obj["configurationSummaryTS"]
      pass

class PreStartConfiguration_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfigurationSequenceTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.configurationRuntimeDS:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["configurationRuntimeDS"]
      self.configurationSummaryTS:list[Erp_Tablesets_ConfigurationSummaryTableset] = obj["configurationSummaryTS"]
      pass

      """  output parameters  """  

class PrepareEWCRequirements_input:
   """ Required : 
   configID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration ID  """  
      pass

class PrepareEWCRequirements_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.accessToken:str = obj["parameters"]
      self.expiresIn:int = obj["parameters"]
      pass

      """  output parameters  """  

class ProcessDocumentRules_input:
   """ Required : 
   configSequenceDS
   configRuntimeDS
   pcValueDS
   """  
   def __init__(self, obj):
      self.configSequenceDS:list[Erp_Tablesets_ConfigurationSequenceTableset] = obj["configSequenceDS"]
      self.configRuntimeDS:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["configRuntimeDS"]
      self.pcValueDS:list[Erp_Tablesets_PcValueTableset] = obj["pcValueDS"]
      pass

class ProcessDocumentRules_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.configSequenceDS:list[Erp_Tablesets_ConfigurationSequenceTableset] = obj["configSequenceDS"]
      self.configRuntimeDS:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["configRuntimeDS"]
      pass

      """  output parameters  """  

class ProcessKeepWhen_input:
   """ Required : 
   configurationSequenceDS
   configRuntimeDS
   pcValueDS
   parAltMethod
   checkNextCfg
   enableNextPage
   """  
   def __init__(self, obj):
      self.configurationSequenceDS:list[Erp_Tablesets_ConfigurationSequenceTableset] = obj["configurationSequenceDS"]
      self.configRuntimeDS:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["configRuntimeDS"]
      self.pcValueDS:list[Erp_Tablesets_PcValueTableset] = obj["pcValueDS"]
      self.parAltMethod:str = obj["parAltMethod"]
      """  Parent AltMethod  """  
      self.checkNextCfg:bool = obj["checkNextCfg"]
      """  Process Keep When Run before the configuration is display to identify if configuration sequence will be changed by changing partnum rule  """  
      self.enableNextPage:bool = obj["enableNextPage"]
      pass

class ProcessKeepWhen_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.configurationSequenceDS:list[Erp_Tablesets_ConfigurationSequenceTableset] = obj["configurationSequenceDS"]
      self.configRuntimeDS:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["configRuntimeDS"]
      self.enableNextPage:bool = obj["enableNextPage"]
      pass

      """  output parameters  """  

class ProcessNICDocumentRules_input:
   """ Required : 
   configSequenceDS
   configRuntimeDS
   """  
   def __init__(self, obj):
      self.configSequenceDS:list[Erp_Tablesets_ConfigurationSequenceTableset] = obj["configSequenceDS"]
      self.configRuntimeDS:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["configRuntimeDS"]
      pass

class ProcessNICDocumentRules_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.configSequenceDS:list[Erp_Tablesets_ConfigurationSequenceTableset] = obj["configSequenceDS"]
      self.configRuntimeDS:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["configRuntimeDS"]
      pass

      """  output parameters  """  

class ProcessNoInputsConfigurator_input:
   """ Required : 
   relatedToTable
   relatedToSysRowID
   partNum
   revisionNum
   altMethod
   configID
   foreignTableName
   foreignSysRowID
   """  
   def __init__(self, obj):
      self.relatedToTable:str = obj["relatedToTable"]
      """  Target entity this call is related to  """  
      self.relatedToSysRowID:str = obj["relatedToSysRowID"]
      """  SysRowID of the target entity  """  
      self.partNum:str = obj["partNum"]
      """  Part Number to run NIC  """  
      self.revisionNum:str = obj["revisionNum"]
      """  Revision Number to run NIC  """  
      self.altMethod:str = obj["altMethod"]
      """  Alternate Method to run NIC  """  
      self.configID:str = obj["configID"]
      """  Configuration ID  """  
      self.foreignTableName:str = obj["foreignTableName"]
      """  Foreign entity this call is related to  """  
      self.foreignSysRowID:str = obj["foreignSysRowID"]
      """  SysRowID of the foreign entity  """  
      pass

class ProcessNoInputsConfigurator_output:
   def __init__(self, obj):
      pass

class SaveConfiguration_input:
   """ Required : 
   configurationSequenceDS
   configurationRuntimeDS
   pcValueDS
   testResultsDS
   """  
   def __init__(self, obj):
      self.configurationSequenceDS:list[Erp_Tablesets_ConfigurationSequenceTableset] = obj["configurationSequenceDS"]
      self.configurationRuntimeDS:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["configurationRuntimeDS"]
      self.pcValueDS:str = obj["pcValueDS"]
      self.testResultsDS:list[Erp_Tablesets_PcTestResultsTableset] = obj["testResultsDS"]
      pass

class SaveConfiguration_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.configurationRuntimeDS:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["configurationRuntimeDS"]
      self.testPassed:bool = obj["testPassed"]
      self.failText:str = obj["parameters"]
      self.testResultsDS:list[Erp_Tablesets_PcTestResultsTableset] = obj["testResultsDS"]
      pass

      """  output parameters  """  

class SaveMultiConfiguration_input:
   """ Required : 
   configSequenceDS
   configRuntimeDS
   serializedData
   testResultsDS
   """  
   def __init__(self, obj):
      self.configSequenceDS:list[Erp_Tablesets_ConfigurationSequenceTableset] = obj["configSequenceDS"]
      self.configRuntimeDS:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["configRuntimeDS"]
      self.serializedData:str = obj["serializedData"]
      """  All configuration values stored in sets of System.String and byte[] in Bas64 format serialized.  """  
      self.testResultsDS:list[Erp_Tablesets_PcTestResultsTableset] = obj["testResultsDS"]
      pass

class SaveMultiConfiguration_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.configSequenceDS:list[Erp_Tablesets_ConfigurationSequenceTableset] = obj["configSequenceDS"]
      self.configRuntimeDS:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["configRuntimeDS"]
      self.testResultsDS:list[Erp_Tablesets_PcTestResultsTableset] = obj["testResultsDS"]
      self.testPassed:bool = obj["testPassed"]
      self.failText:str = obj["parameters"]
      pass

      """  output parameters  """  

class SavePCTransportConfiguration_input:
   """ Required : 
   configurationSequenceDS
   configurationRuntimeDS
   pcValueDS
   testResultsDS
   """  
   def __init__(self, obj):
      self.configurationSequenceDS:list[Erp_Tablesets_ConfigurationSequenceTableset] = obj["configurationSequenceDS"]
      self.configurationRuntimeDS:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["configurationRuntimeDS"]
      self.pcValueDS:list[Erp_Tablesets_PcValueTableset] = obj["pcValueDS"]
      self.testResultsDS:list[Erp_Tablesets_PcTestResultsTableset] = obj["testResultsDS"]
      pass

class SavePCTransportConfiguration_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.configurationRuntimeDS:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["configurationRuntimeDS"]
      self.testResultsDS:list[Erp_Tablesets_PcTestResultsTableset] = obj["testResultsDS"]
      pass

      """  output parameters  """  

class SavePcValueConfigurationMulti_input:
   """ Required : 
   configSequenceDS
   configRuntimeDS
   pcValueDsArray
   testResultsDS
   """  
   def __init__(self, obj):
      self.configSequenceDS:list[Erp_Tablesets_ConfigurationSequenceTableset] = obj["configSequenceDS"]
      self.configRuntimeDS:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["configRuntimeDS"]
      self.pcValueDsArray      #schema had no properties on an object.
      self.testResultsDS:list[Erp_Tablesets_PcTestResultsTableset] = obj["testResultsDS"]
      pass

class SavePcValueConfigurationMulti_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.configRuntimeDS:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["configRuntimeDS"]
      self.testPassed:bool = obj["testPassed"]
      self.failText:str = obj["parameters"]
      self.testResultsDS:list[Erp_Tablesets_PcTestResultsTableset] = obj["testResultsDS"]
      pass

      """  output parameters  """  

class SavePcValueConfiguration_input:
   """ Required : 
   configurationSequenceDS
   configurationRuntimeDS
   pcValueDS
   testResultsDS
   """  
   def __init__(self, obj):
      self.configurationSequenceDS:list[Erp_Tablesets_ConfigurationSequenceTableset] = obj["configurationSequenceDS"]
      self.configurationRuntimeDS:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["configurationRuntimeDS"]
      self.pcValueDS:list[Erp_Tablesets_PcValueTableset] = obj["pcValueDS"]
      self.testResultsDS:list[Erp_Tablesets_PcTestResultsTableset] = obj["testResultsDS"]
      pass

class SavePcValueConfiguration_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.configurationRuntimeDS:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["configurationRuntimeDS"]
      self.testPassed:bool = obj["testPassed"]
      self.failText:str = obj["parameters"]
      self.testResultsDS:list[Erp_Tablesets_PcTestResultsTableset] = obj["testResultsDS"]
      pass

      """  output parameters  """  

class StartConfiguration_input:
   """ Required : 
   ds
   ds2
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["ds"]
      self.ds2:list[Erp_Tablesets_ConfigurationSequenceTableset] = obj["ds2"]
      pass

class StartConfiguration_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Serialized input values.  """  
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class StartPcValueConfiguration_input:
   """ Required : 
   ds
   ds2
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["ds"]
      self.ds2:list[Erp_Tablesets_ConfigurationSequenceTableset] = obj["ds2"]
      pass

class StartPcValueConfiguration_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PcValueTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SuggestSmartString_input:
   """ Required : 
   configID
   testMode
   ts
   ipRelatedToTable
   ipRelatedToSysRowID
   smartStringValues
   structTag
   structID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration ID  """  
      self.testMode:bool = obj["testMode"]
      """  Test Inputs true/false  """  
      self.ts:list[Erp_Tablesets_ConfigurationSequenceTableset] = obj["ts"]
      self.ipRelatedToTable:str = obj["ipRelatedToTable"]
      """  Target entity this call is related to  """  
      self.ipRelatedToSysRowID:str = obj["ipRelatedToSysRowID"]
      """  SysRowID of the target entity  """  
      self.smartStringValues:list[Erp_Shared_Lib_Configurator_PCKeyValuePair_System_String_System_String] = obj["smartStringValues"]
      """  Collection of current input answers from the configuration session.  """  
      self.structTag:str = obj["structTag"]
      """  Identifies the row in the ConfigurationSequenceTableset being processed  """  
      self.structID:int = obj["structID"]
      """  Identifies the row in the ConfigurationSequenceTableset being processed  """  
      pass

class SuggestSmartString_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ts:list[Erp_Tablesets_ConfigurationSequenceTableset] = obj["ts"]
      self.outSmartString:str = obj["parameters"]
      pass

      """  output parameters  """  

class System_Collections_Generic_KeyValuePair_System_String_System_ByteArray:
   def __init__(self, obj):
      self.Key:str = obj["Key"]
      self.Value:str = obj["Value"]
      pass

class System_Collections_Generic_KeyValuePair_System_String_System_String:
   def __init__(self, obj):
      self.Key:str = obj["Key"]
      self.Value:str = obj["Value"]
      pass

class TestNICRules_input:
   """ Required : 
   configID
   partNum
   revisionNum
   ts
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration ID to run test rules  """  
      self.partNum:str = obj["partNum"]
      """  Part Number to run test rules  """  
      self.revisionNum:str = obj["revisionNum"]
      """  Revision Number to run test rules  """  
      self.ts:list[Erp_Tablesets_PcTestResultsTableset] = obj["ts"]
      pass

class TestNICRules_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ts:list[Erp_Tablesets_PcTestResultsTableset] = obj["ts"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtConfigurationRuntimeTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtConfigurationRuntimeTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationRuntimeTableset] = obj["ds"]
      pass

      """  output parameters  """  

