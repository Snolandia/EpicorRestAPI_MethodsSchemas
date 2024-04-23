import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ResourceGroupSvc
# Description: Resource Group
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ResourceGroups(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ResourceGroups items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ResourceGroups
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroups",headers=creds) as resp:
           return await resp.json()

async def post_ResourceGroups(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ResourceGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ResourceGroupRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ResourceGroupRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroups", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ResourceGroups_Company_ResourceGrpID(Company, ResourceGrpID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ResourceGroup item
   Description: Calls GetByID to retrieve the ResourceGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ResourceGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ResourceGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroups(" + Company + "," + ResourceGrpID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ResourceGroups_Company_ResourceGrpID(Company, ResourceGrpID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ResourceGroup for the service
   Description: Calls UpdateExt to update ResourceGroup. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ResourceGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ResourceGroupRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroups(" + Company + "," + ResourceGrpID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ResourceGroups_Company_ResourceGrpID(Company, ResourceGrpID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ResourceGroup item
   Description: Call UpdateExt to delete ResourceGroup item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ResourceGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroups(" + Company + "," + ResourceGrpID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ResourceGroups_Company_ResourceGrpID_Resources(Company, ResourceGrpID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get Resources items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_Resources1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroups(" + Company + "," + ResourceGrpID + ")/Resources",headers=creds) as resp:
           return await resp.json()

async def get_ResourceGroups_Company_ResourceGrpID_Resources_Company_ResourceID(Company, ResourceGrpID, ResourceID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Resource item
   Description: Calls GetByID to retrieve the Resource item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Resource1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ResourceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroups(" + Company + "," + ResourceGrpID + ")/Resources(" + Company + "," + ResourceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ResourceGroups_Company_ResourceGrpID_ResourceCals(Company, ResourceGrpID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ResourceCals items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ResourceCals1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceCalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroups(" + Company + "," + ResourceGrpID + ")/ResourceCals",headers=creds) as resp:
           return await resp.json()

async def get_ResourceGroups_Company_ResourceGrpID_ResourceCals_Company_ResourceGrpID_ResourceID_SpecialDay(Company, ResourceGrpID, ResourceID, SpecialDay, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ResourceCal item
   Description: Calls GetByID to retrieve the ResourceCal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ResourceCal1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param SpecialDay: Desc: SpecialDay   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ResourceCalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroups(" + Company + "," + ResourceGrpID + ")/ResourceCals(" + Company + "," + ResourceGrpID + "," + ResourceID + "," + SpecialDay + ")",headers=creds) as resp:
           return await resp.json()

async def get_ResourceGroups_Company_ResourceGrpID_ResourceGroupAttches(Company, ResourceGrpID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ResourceGroupAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ResourceGroupAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceGroupAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroups(" + Company + "," + ResourceGrpID + ")/ResourceGroupAttches",headers=creds) as resp:
           return await resp.json()

async def get_ResourceGroups_Company_ResourceGrpID_ResourceGroupAttches_Company_ResourceGrpID_DrawingSeq(Company, ResourceGrpID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ResourceGroupAttch item
   Description: Calls GetByID to retrieve the ResourceGroupAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ResourceGroupAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ResourceGroupAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroups(" + Company + "," + ResourceGrpID + ")/ResourceGroupAttches(" + Company + "," + ResourceGrpID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_Resources(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Resources items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Resources
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/Resources",headers=creds) as resp:
           return await resp.json()

async def post_Resources(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Resources
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ResourceRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ResourceRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/Resources", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Resources_Company_ResourceID(Company, ResourceID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Resource item
   Description: Calls GetByID to retrieve the Resource item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Resource
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ResourceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/Resources(" + Company + "," + ResourceID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Resources_Company_ResourceID(Company, ResourceID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Resource for the service
   Description: Calls UpdateExt to update Resource. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Resource
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ResourceRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/Resources(" + Company + "," + ResourceID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Resources_Company_ResourceID(Company, ResourceID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Resource item
   Description: Call UpdateExt to delete Resource item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Resource
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/Resources(" + Company + "," + ResourceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_Resources_Company_ResourceID_CapResLnks(Company, ResourceID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CapResLnks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CapResLnks1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CapResLnkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/Resources(" + Company + "," + ResourceID + ")/CapResLnks",headers=creds) as resp:
           return await resp.json()

async def get_Resources_Company_ResourceID_CapResLnks_Company_CapabilityID_ResourceID(Company, ResourceID, CapabilityID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CapResLnk item
   Description: Calls GetByID to retrieve the CapResLnk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CapResLnk1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param CapabilityID: Desc: CapabilityID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CapResLnkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/Resources(" + Company + "," + ResourceID + ")/CapResLnks(" + Company + "," + CapabilityID + "," + ResourceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CapResLnks(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CapResLnks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CapResLnks
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CapResLnkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/CapResLnks",headers=creds) as resp:
           return await resp.json()

async def post_CapResLnks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CapResLnks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CapResLnkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CapResLnkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/CapResLnks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CapResLnks_Company_CapabilityID_ResourceID(Company, CapabilityID, ResourceID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CapResLnk item
   Description: Calls GetByID to retrieve the CapResLnk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CapResLnk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CapabilityID: Desc: CapabilityID   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CapResLnkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/CapResLnks(" + Company + "," + CapabilityID + "," + ResourceID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CapResLnks_Company_CapabilityID_ResourceID(Company, CapabilityID, ResourceID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CapResLnk for the service
   Description: Calls UpdateExt to update CapResLnk. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CapResLnk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CapabilityID: Desc: CapabilityID   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CapResLnkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/CapResLnks(" + Company + "," + CapabilityID + "," + ResourceID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CapResLnks_Company_CapabilityID_ResourceID(Company, CapabilityID, ResourceID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CapResLnk item
   Description: Call UpdateExt to delete CapResLnk item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CapResLnk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CapabilityID: Desc: CapabilityID   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/CapResLnks(" + Company + "," + CapabilityID + "," + ResourceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ResourceCals(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ResourceCals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ResourceCals
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceCalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceCals",headers=creds) as resp:
           return await resp.json()

async def post_ResourceCals(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ResourceCals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ResourceCalRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ResourceCalRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceCals", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ResourceCals_Company_ResourceGrpID_ResourceID_SpecialDay(Company, ResourceGrpID, ResourceID, SpecialDay, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ResourceCal item
   Description: Calls GetByID to retrieve the ResourceCal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ResourceCal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param SpecialDay: Desc: SpecialDay   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ResourceCalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceCals(" + Company + "," + ResourceGrpID + "," + ResourceID + "," + SpecialDay + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ResourceCals_Company_ResourceGrpID_ResourceID_SpecialDay(Company, ResourceGrpID, ResourceID, SpecialDay, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ResourceCal for the service
   Description: Calls UpdateExt to update ResourceCal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ResourceCal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param SpecialDay: Desc: SpecialDay   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ResourceCalRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceCals(" + Company + "," + ResourceGrpID + "," + ResourceID + "," + SpecialDay + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ResourceCals_Company_ResourceGrpID_ResourceID_SpecialDay(Company, ResourceGrpID, ResourceID, SpecialDay, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ResourceCal item
   Description: Call UpdateExt to delete ResourceCal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ResourceCal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param SpecialDay: Desc: SpecialDay   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceCals(" + Company + "," + ResourceGrpID + "," + ResourceID + "," + SpecialDay + ")",headers=creds) as resp:
           return await resp.json()

async def get_ResourceGroupAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ResourceGroupAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ResourceGroupAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceGroupAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroupAttches",headers=creds) as resp:
           return await resp.json()

async def post_ResourceGroupAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ResourceGroupAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ResourceGroupAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ResourceGroupAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroupAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ResourceGroupAttches_Company_ResourceGrpID_DrawingSeq(Company, ResourceGrpID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ResourceGroupAttch item
   Description: Calls GetByID to retrieve the ResourceGroupAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ResourceGroupAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ResourceGroupAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroupAttches(" + Company + "," + ResourceGrpID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ResourceGroupAttches_Company_ResourceGrpID_DrawingSeq(Company, ResourceGrpID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ResourceGroupAttch for the service
   Description: Calls UpdateExt to update ResourceGroupAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ResourceGroupAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ResourceGroupAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroupAttches(" + Company + "," + ResourceGrpID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ResourceGroupAttches_Company_ResourceGrpID_DrawingSeq(Company, ResourceGrpID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ResourceGroupAttch item
   Description: Call UpdateExt to delete ResourceGroupAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ResourceGroupAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/ResourceGroupAttches(" + Company + "," + ResourceGrpID + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ResourceGroupListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseResourceGroup, whereClauseResourceGroupAttch, whereClauseResource, whereClauseCapResLnk, whereClauseResourceCal, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseResourceGroup=" + whereClauseResourceGroup
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseResourceGroupAttch=" + whereClauseResourceGroupAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseResource=" + whereClauseResource
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCapResLnk=" + whereClauseCapResLnk
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseResourceCal=" + whereClauseResourceCal
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(resourceGrpID, epicorHeaders = None):
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
   params += "resourceGrpID=" + resourceGrpID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SelectDistinctInOutWhseQuery(epicorHeaders = None):
   """  
   Summary: Invoke method SelectDistinctInOutWhseQuery
   OperationID: SelectDistinctInOutWhseQuery
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectDistinctInOutWhseQuery_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_BuildRsrcGrpResourceCalList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildRsrcGrpResourceCalList
   Description: This method will populate the ttResourceCal table using the resource group
that was passed in.
   OperationID: BuildRsrcGrpResourceCalList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildRsrcGrpResourceCalList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildRsrcGrpResourceCalList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildRsrcResourceCalList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildRsrcResourceCalList
   Description: This method will populate the ttResourceCal table using the resource group
that was passed in.
   OperationID: BuildRsrcResourceCalList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildRsrcResourceCalList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildRsrcResourceCalList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckRGPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckRGPlant
   Description: This method will verify that the Resource Group ID entered is from the Current
plant.
   OperationID: CheckRGPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRGPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRGPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CustomizeResourceCalRsrc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CustomizeResourceCalRsrc
   Description: This method will get a current ResourceCal record or create a temporary
ResourceCal record to be modified for a RESOURCE.  The ProdHours will be
defaulted from the weekday of the selected date.  If any changes are made
to the ttResourceCal record, the UpdateResourceCal method will have to be
called to write the temporary ResourceCal record to the database.
   OperationID: CustomizeResourceCalRsrc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CustomizeResourceCalRsrc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomizeResourceCalRsrc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CustomizeResourceCalRsrcGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CustomizeResourceCalRsrcGrp
   Description: This method will get a current ResourceCal record or create a temporary
ResourceCal record to be modified for a RESOURCE GROUP.  The ProdHours
will be defaulted from the weekday of the selected date.  If any changes
are made to the ttResourceCal record, the UpdateResourceCal method will have
to be called to write the temporary ResourceCal record to the database.
   OperationID: CustomizeResourceCalRsrcGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CustomizeResourceCalRsrcGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomizeResourceCalRsrcGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteResourceCal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteResourceCal
   Description: This method will delete ResourceCal record.
   OperationID: DeleteResourceCal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteResourceCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteResourceCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EnterpriseGetList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EnterpriseGetList
   Description: Will invoke GetList or perform the Enterprise Search when enterpriseSearchText / enterpriseBAQID is provided
   OperationID: EnterpriseGetList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EnterpriseGetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnterpriseGetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertNewResource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertNewResource
   Description: This method creates a new Resource after prompting for the
ResourceID and ResourceGrpID.
This is to replace the standard GetNewResource .
   OperationID: InsertNewResource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertNewResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertNewResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MoveResource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveResource
   Description: This method creates a new Resource after prompting for the
ResourceID and ResourceGrpID.
This is to replace the standard GetNewResource .
   OperationID: MoveResource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MoveResourceCal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveResourceCal
   Description: This method will change SpecialDay of ResourceCal record.
   OperationID: MoveResourceCal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveResourceCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveResourceCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetInactiveFlag(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetInactiveFlag
   Description: Call this method when the Inactive Flag on the Resource Group changes and the
user answer "Yes" to set the inactive flag on the Resources.  All of the
Resources Inactive flags will be set to equal to the new inactive setting on the
Resource Group.
   OperationID: SetInactiveFlag
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetInactiveFlag_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetInactiveFlag_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateResourceCal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateResourceCal
   Description: This method will check to see if the current ttResourceCal record was modified.
If it was modified then it compares the capacity from the ttResourceCal
the capacity of the production calendar for that day of the week.  If they
are different, or if it is a special working day or non-working day then
it save the ttResourceCal record to the database.
   OperationID: UpdateResourceCal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateResourceCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateResourceCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateInspection(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateInspection
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateResource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateResource
   Description: This method validates that the Resource exists and that it isn't assigned to
another Resource Group.
   OperationID: ValidateResource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_RequestExternalMESActiveResourceTypeValidation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RequestExternalMESActiveResourceTypeValidation
   Description: Purpose:
Parameters:  none
Notes:
   OperationID: RequestExternalMESActiveResourceTypeValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RequestExternalMESActiveResourceTypeValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RequestExternalMESActiveResourceTypeValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangedCharacteristicAttrClassID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedCharacteristicAttrClassID
   Description: Used when the Characteristic Attr Class ID is changed.
   OperationID: ChangedCharacteristicAttrClassID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedCharacteristicAttrClassID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedCharacteristicAttrClassID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeResourceGroupResourceType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeResourceGroupResourceType
   Description: This method is called when the Resource Group ResourceType field is changed.
   OperationID: ChangeResourceGroupResourceType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeResourceGroupResourceType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeResourceGroupResourceType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeResourceResourceType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeResourceResourceType
   Description: This method is called when the Resource ResourceType field is changed.
   OperationID: ChangeResourceResourceType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeResourceResourceType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeResourceResourceType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetResourceGroupsExtMES(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetResourceGroupsExtMES
   Description: Get the list of resource groups for Mattec changes
   OperationID: GetResourceGroupsExtMES
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetResourceGroupsExtMES_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetResourceGroupsExtMES_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewResourceGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewResourceGroup
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewResourceGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewResourceGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewResourceGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewResourceGroupAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewResourceGroupAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewResourceGroupAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewResourceGroupAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewResourceGroupAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewResource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewResource
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewResource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCapResLnk(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCapResLnk
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCapResLnk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCapResLnk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCapResLnk_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewResourceCal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewResourceCal
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewResourceCal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewResourceCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewResourceCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ResourceGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CapResLnkRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CapResLnkRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceCalRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ResourceCalRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceGroupAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ResourceGroupAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceGroupListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ResourceGroupListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceGroupRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ResourceGroupRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ResourceRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ResourceRow] = obj["value"]
      pass

class Erp_Tablesets_CapResLnkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CapabilityID:str = obj["CapabilityID"]
      """  A code which uniquely identifies the Capability this link applies to.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ResourceID the Capability is being linked to.  """  
      self.ResourcePriority:int = obj["ResourcePriority"]
      """  A tie breaker.  If two Resources are equal, but a user would prefer to keep one busy, then the one with the highest priority will be selected first.  """  
      self.ProductionFactor:int = obj["ProductionFactor"]
      """  A Production Factor for the link.  """  
      self.SetupFactor:int = obj["SetupFactor"]
      """  A Setup Factor for the link.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CapIDDescription:str = obj["CapIDDescription"]
      self.ResourceDescription:str = obj["ResourceDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ResourceCalRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code uniquely identifies a Resource Group.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.SpecialDay:str = obj["SpecialDay"]
      """  Exception Day  """  
      self.ProdHour01:bool = obj["ProdHour01"]
      """  ProdHour01  """  
      self.ProdHour02:bool = obj["ProdHour02"]
      """  ProdHour02  """  
      self.ProdHour03:bool = obj["ProdHour03"]
      """  ProdHour03  """  
      self.ProdHour04:bool = obj["ProdHour04"]
      """  ProdHour04  """  
      self.ProdHour05:bool = obj["ProdHour05"]
      """  ProdHour05  """  
      self.ProdHour06:bool = obj["ProdHour06"]
      """  ProdHour06  """  
      self.ProdHour07:bool = obj["ProdHour07"]
      """  ProdHour07  """  
      self.ProdHour08:bool = obj["ProdHour08"]
      """  ProdHour08  """  
      self.ProdHour09:bool = obj["ProdHour09"]
      """  ProdHour09  """  
      self.ProdHour10:bool = obj["ProdHour10"]
      """  ProdHour10  """  
      self.ProdHour11:bool = obj["ProdHour11"]
      """  ProdHour11  """  
      self.ProdHour12:bool = obj["ProdHour12"]
      """  ProdHour12  """  
      self.ProdHour13:bool = obj["ProdHour13"]
      """  ProdHour13  """  
      self.ProdHour14:bool = obj["ProdHour14"]
      """  ProdHour14  """  
      self.ProdHour15:bool = obj["ProdHour15"]
      """  ProdHour15  """  
      self.ProdHour16:bool = obj["ProdHour16"]
      """  ProdHour16  """  
      self.ProdHour17:bool = obj["ProdHour17"]
      """  ProdHour17  """  
      self.ProdHour18:bool = obj["ProdHour18"]
      """  ProdHour18  """  
      self.ProdHour19:bool = obj["ProdHour19"]
      """  ProdHour19  """  
      self.ProdHour20:bool = obj["ProdHour20"]
      """  ProdHour20  """  
      self.ProdHour21:bool = obj["ProdHour21"]
      """  ProdHour21  """  
      self.ProdHour22:bool = obj["ProdHour22"]
      """  ProdHour22  """  
      self.ProdHour23:bool = obj["ProdHour23"]
      """  ProdHour23  """  
      self.ProdHour24:bool = obj["ProdHour24"]
      """  ProdHour24  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExceptionLabel:str = obj["ExceptionLabel"]
      """  ExceptionLabel  """  
      self.DispExceptionLabel:str = obj["DispExceptionLabel"]
      """  Display Exception Label  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ResourceGroupAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ResourceGrpID:str = obj["ResourceGrpID"]
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

class Erp_Tablesets_ResourceGroupListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code uniquely identifies a Resource Group.  Cannot be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Description:str = obj["Description"]
      """  Long description of the Resource Group.  """  
      self.Inactive:bool = obj["Inactive"]
      """   Flag which indicates if the Resource Group is considered "Inactive".  For historical purposed, and data integrity, it is difficult to delete a ResourceGroup that has been used for production.  Instead, it is set to Inactive = YES.
This flag will be used to exclude Resource Groups from certain searches and reports.
Resource Groups where Inactive=yes are treated as deleted, but remain in the table to maintain database integrity.  """  
      self.JCDept:str = obj["JCDept"]
      """  The Key ID of the Home Department for this Resource Group.  This is a foreign key to the JCDept table.  """  
      self.ProdBurRate:int = obj["ProdBurRate"]
      """  The burden rate for production.  """  
      self.SetupBurRate:int = obj["SetupBurRate"]
      """  Default burden rate for Setup time.  """  
      self.QProdBurRate:int = obj["QProdBurRate"]
      """   Quoting burden rate for production in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.QSetupBurRate:int = obj["QSetupBurRate"]
      """   Quoting burden rate for setup in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.ResourceType:str = obj["ResourceType"]
      """  For scheduling purposes a Resource Group can be a Standard resource (S), Additional resource (D), or Auxiliary resource (X).  Standard resources use capacity when scheduled in a finite capacity workcenter.  An Auxiliary Resource can be used in production by  any operation concurrently with a Standard resource, but it does not use capacity.  This is significant for scheduling work to the machine.  Also, an Auxiliary resources does not have to be available for an entire operation.  Additional resources can be added to an Operation, they do use capacity and need to be available for the entire operation.  """  
      self.InputWhse:str = obj["InputWhse"]
      """  Indicates a warehouse  in which parts are staged for consumption by the Resource Group.  This must be valid in the Warehouse table.  """  
      self.OutputWhse:str = obj["OutputWhse"]
      """  Defines a warehouse for the output of a Resource Group.  This must be valid in the Warehouse table.  """  
      self.Location:bool = obj["Location"]
      """  Location  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CharacteristicAttrClassID:str = obj["CharacteristicAttrClassID"]
      """  ID of related Attribute Class, the class must be of type Characteristics.  """  
      self.CharacteristicAttributeSetID:int = obj["CharacteristicAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.JCDeptDescription:str = obj["JCDeptDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ResourceGroupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code uniquely identifies a Resource Group.  Cannot be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Description:str = obj["Description"]
      """  Long description of the Resource Group.  """  
      self.CalendarID:str = obj["CalendarID"]
      """  Identifies the production calendar for this Resource Group.   If this equals "", then the ProdCal record is the Company Level production calendar.  """  
      self.Inactive:bool = obj["Inactive"]
      """   Flag which indicates if the Resource Group is considered "Inactive".  For historical purposed, and data integrity, it is difficult to delete a ResourceGroup that has been used for production.  Instead, it is set to Inactive = YES.
This flag will be used to exclude Resource Groups from certain searches and reports.
Resource Groups where Inactive=yes are treated as deleted, but remain in the table to maintain database integrity.  """  
      self.AllowManualOverride:bool = obj["AllowManualOverride"]
      """  If it is Finite Resource Group, and this is true, then the user will be allow to overload this Resource Group from using the scheduling tools.  """  
      self.FiniteHorizon:int = obj["FiniteHorizon"]
      """  The number of days out this Resource Group will be scheduled finitely.  Production capacity requirements past this day are treated as infinite.  """  
      self.NumberOfMachines:int = obj["NumberOfMachines"]
      """   The number of Resources in this Resource Group. The number of Resources X HrsPerMachine = Capacity.
A Resource Group with zero Resources is considered infinite capacity.  """  
      self.SchMachine:int = obj["SchMachine"]
      """  Number of Resources that one operation runs on at a time within this Resource Group.  This affects how much of the total daily Resource Group capacity is used up per operation.  If Resource Group has 4  Resource, 8 hour a day, and SchMachine = 2.  An operation will schedule up to 16 hours per day.   This is used as a default to the JobOper.Machines field.  """  
      self.BurdenType:str = obj["BurdenType"]
      """  Indicates if the BurdenRate fields are either a flat hourly dollar rate or a percentage of LaborRate. Default is Hourly dollar rate.   Set to "F" (flat) or "P" (percent).  """  
      self.MoveHours:int = obj["MoveHours"]
      """  The number of hours of delay that occurs when an operation leaves this Resource Group before the next operation can begin in a different Resource Group.  """  
      self.JCDept:str = obj["JCDept"]
      """  The Key ID of the Home Department for this Resource Group.  This is a foreign key to the JCDept table.  """  
      self.QueHours:int = obj["QueHours"]
      """  Queue Time.  The number of hours of delay that occurs when an operation enters this Resource Group before it can begin. (The opposite of MoveHours)  """  
      self.OpCode:str = obj["OpCode"]
      """  Establishes the default operation used when referencing this Resource Group.  This is optional, but if entered it must be valid in the OpMaster.  """  
      self.ProdBurRate:int = obj["ProdBurRate"]
      """  The burden rate for production.  """  
      self.ProdLabRate:int = obj["ProdLabRate"]
      """  The labor rate for production.  """  
      self.SetupBurRate:int = obj["SetupBurRate"]
      """  Default burden rate for Setup time.  """  
      self.SetupLabRate:int = obj["SetupLabRate"]
      """  Default labor rate for setup time.  """  
      self.QProdBurRate:int = obj["QProdBurRate"]
      """   Quoting burden rate for production in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.QProdLabRate:int = obj["QProdLabRate"]
      """   Quoting burden rate for production on the Resource.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.QSetupBurRate:int = obj["QSetupBurRate"]
      """   Quoting burden rate for setup in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.QSetupLabRate:int = obj["QSetupLabRate"]
      """   Quoting burden rate for setup in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.SplitBurden:bool = obj["SplitBurden"]
      """  Indicates if burden hours are split out among employees when multiple employees work simultaneously on the same job operation within this Resource Group.  This feature is only applicable to Data Collection.  Manual Labor Entry does not split the burden hours. The opposite is that each employee should have their burden hours = labor hours. This situation would occur in Resource Groups that actually have "people" as machines, such as an assembly or welding center where multiple people work on the same job.  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Defines the default crew size for work done in this Resource Group.   The number of people it physically takes to run the machine. This should not be confused with scheduled number of machines, which squeezes the schedule time. The crew size is a multiplier used in calculation of Production labor hours on operations.  """  
      self.SetupCrewSize:int = obj["SetupCrewSize"]
      """  Defines the default setup crew size for work done in this Resource Group.  The number of people it physically takes to setup the Resource.  This should not be confused with scheduled number of machines, which squeezes the schedule time.  The crew size is a multiplier  used in calculation of setup labor hours for an operation.  """  
      self.OpStdID:str = obj["OpStdID"]
      """  Defines a default Operation standard master ID for this Resource Group.  If entered then this along with the ResourceGrpID, OpCode must be valid in the OpStd master file.  """  
      self.ReloadNum:int = obj["ReloadNum"]
      """  lib/Reloader.w program increments and assigns it to Joboper.ReloadNum as it processes JobOper records. It is used to prevent redundant reads during the For Each loop.  """  
      self.ReloadStatus:str = obj["ReloadStatus"]
      """  A  recovery flag which indicates the status of the Reload process for this Resource Group.  Values; Blank or "Started".  """  
      self.DailyCapacity1:int = obj["DailyCapacity1"]
      """  DailyCapacity1  """  
      self.DailyCapacity2:int = obj["DailyCapacity2"]
      """  DailyCapacity2  """  
      self.DailyCapacity3:int = obj["DailyCapacity3"]
      """  DailyCapacity3  """  
      self.DailyCapacity4:int = obj["DailyCapacity4"]
      """  DailyCapacity4  """  
      self.DailyCapacity5:int = obj["DailyCapacity5"]
      """  DailyCapacity5  """  
      self.DailyCapacity6:int = obj["DailyCapacity6"]
      """  DailyCapacity6  """  
      self.DailyCapacity7:int = obj["DailyCapacity7"]
      """  DailyCapacity7  """  
      self.QBurdenType:str = obj["QBurdenType"]
      """  Indicates if the Quote Burden Rate fields are either a flat hourly dollar rate or a percentage of Quote LaborRate.  Default is Hourly dollar rate.  Set to "F" (flat) or "P" (percent).  """  
      self.BurdenEQLabor:bool = obj["BurdenEQLabor"]
      """  Indicates if burden hours should equal Labor Hours for work reported within this Resource Group.  This feature is only applicable to Data Collection.  This is intended to be used where an employee jumps between multiple job operations without clock in/out (for efficiency purposes).  Example: Employee works on 4 operations for 8am - 1200.  They clock out of all 4 at 12.  Each transaction is given 1hr of labor.  If this is checked then each transaction will also have 1hr of burden.  Otherwise they will have 4 hrs for a total of 16 burden hrs.  """  
      self.SplitOperations:bool = obj["SplitOperations"]
      """  Used for scheduling.  If YES then a single operation in this Resoure Group can be split across multiple Resources.  """  
      self.ResourceType:str = obj["ResourceType"]
      """  For scheduling purposes a Resource Group can be a Standard resource (S), Additional resource (D), or Auxiliary resource (X).  Standard resources use capacity when scheduled in a finite capacity workcenter.  An Auxiliary Resource can be used in production by  any operation concurrently with a Standard resource, but it does not use capacity.  This is significant for scheduling work to the machine.  Also, an Auxiliary resources does not have to be available for an entire operation.  Additional resources can be added to an Operation, they do use capacity and need to be available for the entire operation.  """  
      self.InputWhse:str = obj["InputWhse"]
      """  Indicates a warehouse  in which parts are staged for consumption by the Resource Group.  This must be valid in the Warehouse table.  """  
      self.InputBinNum:str = obj["InputBinNum"]
      """  Indicates a warehouse bin  in which parts are staged for consumption by the Resource Group.  It  must be valid in the WhseBin table.  """  
      self.OutputWhse:str = obj["OutputWhse"]
      """  Defines a warehouse for the output of a Resource Group.  This must be valid in the Warehouse table.  """  
      self.OutputBinNum:str = obj["OutputBinNum"]
      """  Defines a warehouse bin for the output of a Resource Group.  It  must be valid in the WhseBin table.  """  
      self.BackflushWhse:str = obj["BackflushWhse"]
      """  Defines a warehouse for backflushing material of a Resource Group.  This must be valid in the Warehouse table.   Used with the InputWhse/InputBin.  If a JobMtl record is set to be backflushed, the the JobMtl is linked to a JobOper, and the Resource Group for the JobOper has a backflush warehouse, then the material will be backflushed from that warehouse when there is not a positive quantity available for the Resource Group InputWhse/Input Bin.  """  
      self.BackflushBinNum:str = obj["BackflushBinNum"]
      """  Defines a warehouse bin for backflushing for the Resource Group.  It  must be valid in the WhseBin table.  """  
      self.InformOverload:bool = obj["InformOverload"]
      """  Indicates that Resource Group is visible in Overload Informer.  """  
      self.MinOverloadPerc:int = obj["MinOverloadPerc"]
      """  The minimum overload threshold before a day shows up in the Overload Informer.  """  
      self.BackflushEmpID:str = obj["BackflushEmpID"]
      """  Is the Employee ID which will be defaulted into LaborDtl records which get created through backflushing.  If this field is blank, then the Employee ID on the LaborDtl record causing the backflush process to be triggered will be used.  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the Resource Group as being a "SubContract" or an "Internal".  This will determine the default when adding an operation to a BOM, Job, or Quote.  """  
      self.AutoMove:bool = obj["AutoMove"]
      """  To toggle on and off the automove flag for a Resource Group.  When false , the default is to generate a move request. When true the default is to not generate a move request. These defaults can be seen when entering a quantity and ending an activity in labor entry.  """  
      self.UseEstimates:bool = obj["UseEstimates"]
      """  Indicates if hours are split out using estimate values when working  on multiple  job operations.  """  
      self.DailyProdQty:int = obj["DailyProdQty"]
      """  Daily Production Qty: The production quantity developed to satisfy demand.  The cell is designed to produce at that quantity for a given time frame (daily).  """  
      self.BillLaborRate:int = obj["BillLaborRate"]
      """  Field Service - Labor rate used for time on an operation.  Time per hour per technician.  """  
      self.DailyProdRate:int = obj["DailyProdRate"]
      """  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity .   Once the production limit for a resource  has been reached, the Resource has been consumed for that day.  """  
      self.Location:bool = obj["Location"]
      """  Location  """  
      self.DistributeLoad:bool = obj["DistributeLoad"]
      """  Distribute Load  """  
      self.TrkProdAct:bool = obj["TrkProdAct"]
      """  Flag to indicate whether to track production activity of the resource group.  """  
      self.SetShopLoad:bool = obj["SetShopLoad"]
      """  When the capcity changes for a resourceGroup (in Resource Group Entry), this flag is set to true to indicate that Generate Shop Capacity process needs to be run to update the ShopLoad records.  This used to be performed within ResourceGroupEntry but for performance reasons it is being moved to the Generate Shop Capacity process  """  
      self.TAKTValue:int = obj["TAKTValue"]
      """  TAKT Value  """  
      self.UseCalendarForMove:bool = obj["UseCalendarForMove"]
      """  Use Calendar for Move Time  """  
      self.UseCalendarForQueue:bool = obj["UseCalendarForQueue"]
      """  Use Calendar for Queue Time  """  
      self.URL:str = obj["URL"]
      """  URL  """  
      self.JDFDevice:str = obj["JDFDevice"]
      """  JDFDevice  """  
      self.JDFOperation:str = obj["JDFOperation"]
      """  JDFOperation  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.MESQueue:bool = obj["MESQueue"]
      """  MESQueue  """  
      self.CharacteristicAttrClassID:str = obj["CharacteristicAttrClassID"]
      """  ID of related Attribute Class, the class must be of type Characteristics.  """  
      self.CharacteristicAttributeSetID:int = obj["CharacteristicAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.inputwhsedesc:str = obj["inputwhsedesc"]
      self.outputwhsedesc:str = obj["outputwhsedesc"]
      self.backflushempname:str = obj["backflushempname"]
      self.backflushwhsedesc:str = obj["backflushwhsedesc"]
      self.EnableInactive:bool = obj["EnableInactive"]
      """  Indicates if the Inactive flag should be enabled.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.JCDeptDescription:str = obj["JCDeptDescription"]
      self.OPCodeOpDesc:str = obj["OPCodeOpDesc"]
      self.OpStdDescription:str = obj["OpStdDescription"]
      self.ProdCalDescription:str = obj["ProdCalDescription"]
      self.ResourceTypeExternalMESType:str = obj["ResourceTypeExternalMESType"]
      self.ResourceTypeDescription:str = obj["ResourceTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ResourceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code that identifies the Resource Group that the resource belongs to.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.Description:str = obj["Description"]
      """  Full description of Resource.  """  
      self.Inactive:bool = obj["Inactive"]
      """   Flag which indicates if the Resource is considered "Inactive".
This flag will be used to exclude Resources from certain searches and reports.
When Inactive=yes the Resource is treated as deleted, but will remain in the table to maintain database integrity.  """  
      self.Finite:bool = obj["Finite"]
      """  If yes then this Resource is scheduled as though it has finite production capacity.  """  
      self.AllowManualOverride:bool = obj["AllowManualOverride"]
      """  If it is Finite Resource, and this is true, then the user will be allow to overload this resource from using the scheduling tools.  """  
      self.NextMaintDate:str = obj["NextMaintDate"]
      """  This Resources next scheduled maintenance date. An optional, user entered field. This can be used in report selections. It does not effect any scheduling logic.  """  
      self.OutputWhse:str = obj["OutputWhse"]
      """  Defines a warehouse for the output of a Resource Group.  This must be valid in the Warehouse table.  """  
      self.OutputBinNum:str = obj["OutputBinNum"]
      """  Defines a warehouse bin for the output of a Resource Group.  It  must be valid in the WhseBin table.  """  
      self.BackflushWhse:str = obj["BackflushWhse"]
      """  Defines a warehouse for backflushing material of a Resource Group.  This must be valid in the Warehouse table.   Used with the InputWhse/InputBin.  If a JobMtl record is set to be backflushed, the the JobMtl is linked to a JobOper, and the Resource Group for the JobOper has a backflush warehouse, then the material will be backflushed from that warehouse when there is not a positive quantity available for the Resource Group InputWhse/Input Bin.  """  
      self.BackflushBinNum:str = obj["BackflushBinNum"]
      """  Defines a warehouse bin for backflushing for the Resource Group.  It  must be valid in the WhseBin table.  """  
      self.InputWhse:str = obj["InputWhse"]
      """  Indicates a warehouse  in which parts are staged for consumption by the Resource Group.  This must be valid in the Warehouse table.  """  
      self.InputBinNum:str = obj["InputBinNum"]
      """  Indicates a warehouse bin  in which parts are staged for consumption by the Resource Group.  It  must be valid in the WhseBin table.  """  
      self.ResourceType:str = obj["ResourceType"]
      """  Allow the Resource to be linked to a ResourceType record.  This is only used for analysis purposes.  """  
      self.ConcurrentCapacity:int = obj["ConcurrentCapacity"]
      """  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  """  
      self.TrackProdQty:bool = obj["TrackProdQty"]
      """  Indicates the production quantities produced by this Resource will be tracked.  """  
      self.LinkedPart:str = obj["LinkedPart"]
      """  Links this Resource to a Part, which must be valid in the Part table.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the Resource.  Links the Resource to a Fixed Asset.  """  
      self.ProdBurRate:int = obj["ProdBurRate"]
      """  The burden rate for production.  """  
      self.ProdLabRate:int = obj["ProdLabRate"]
      """  The labor rate for production.  """  
      self.SetupBurRate:int = obj["SetupBurRate"]
      """  Default burden rate for Setup time.  """  
      self.SetupLabRate:int = obj["SetupLabRate"]
      """  Default labor rate for setup time.  """  
      self.QProdBurRate:int = obj["QProdBurRate"]
      """   Quoting burden rate for production on the Resource
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.QProdLabRate:int = obj["QProdLabRate"]
      """   Quoting burden rate for production on the Resource.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.QSetupBurRate:int = obj["QSetupBurRate"]
      """   Quoting burden rate for setup in the Resource.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.QSetupLabRate:int = obj["QSetupLabRate"]
      """   Quoting burden rate for "setup" in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.QBurdenType:str = obj["QBurdenType"]
      """  Indicates if the Quote Burden Rate fields are either a flat hourly dollar rate or a percentage of Quote LaborRate.  Default is flat hourly rate.  Valid values are "F" (flat) or "P" (percent).  """  
      self.GetDefaultBurdenFromGroup:bool = obj["GetDefaultBurdenFromGroup"]
      """  Logical to direct where the burden rate information about the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  If this field is set this is be a subcontracted resource.  """  
      self.BurdenType:str = obj["BurdenType"]
      """  Indicates if the BurdenRate fields are either a flat hourly dollar rate or a percentage of LaborRate. Default is Hourly dollar rate.   Set to "F" (flat) or "P" (percent).  """  
      self.CalendarID:str = obj["CalendarID"]
      """  Identifies the production calendar for this Resource.   If this equals "", then the ProdCal record is the Resource Group Level production calendar.  """  
      self.MoveHours:int = obj["MoveHours"]
      """  The number of hours of delay that occurs when an operation leaves this Resource before the next operation can begin in a different Resource.  """  
      self.QueHours:int = obj["QueHours"]
      """  Queue Time.  The number of hours of delay that occurs when an operation enters this Resource before it can begin. (The opposite of MoveHours)  """  
      self.GetDefaultMQFromGroup:bool = obj["GetDefaultMQFromGroup"]
      """  Logical to direct where the Move Time and Queue time for the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  This also controls whether the FiniteHorizon  and SplitOperation is from the Resource Group.  """  
      self.InformOverload:bool = obj["InformOverload"]
      """  Indicates that the Resource is visible in Overload Informer.  """  
      self.MinOverloadPerc:int = obj["MinOverloadPerc"]
      """  The minimum overload threshold before a day shows up in the Overload Informer.  """  
      self.OpCode:str = obj["OpCode"]
      """   Establishes the default operation used when referencing this Resource.  This is optional, but if entered it must be valid in the OpMaster.
Required if a Resource is going to be used to create a JobOper record.  """  
      self.OpStdID:str = obj["OpStdID"]
      """   Defines a default Operation standard master ID for this Resource.  If entered then this along with the ResourceGrpID, OpCode must be valid in the OpStd master file.
Required if the Resource is going to be used to create a JobOper.  """  
      self.GetDefaultLaborFromGroup:bool = obj["GetDefaultLaborFromGroup"]
      """  Logical to direct where the labor rate information about the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  """  
      self.FiniteHorizon:int = obj["FiniteHorizon"]
      """  The number of days out this Resource will be scheduled finitely.  Production capacity requirements past this day are treated as infinite.  """  
      self.AutoMove:bool = obj["AutoMove"]
      """  To toggle on and off the AutoMove flag for a Resource.  When false, the default is to generate a move request.  When true the default is to not generate a move request.  These defaults can be seen when entering a quantity and ending an activity in labor entry.  """  
      self.SplitOperations:bool = obj["SplitOperations"]
      """  Used for scheduling.  If YES then a single operation on this Resource can be split into multiple operations.  """  
      self.DailyProdQty:int = obj["DailyProdQty"]
      """  The production Qty developed to satisfy demand.  The cell is designed to produce at that rate for a given time frame (daily) until this production qty is met.  """  
      self.BillLaborRate:int = obj["BillLaborRate"]
      """  Field Service - Labor rate used for time on an operation.  Time per hour per technician.  """  
      self.DailyProdRate:int = obj["DailyProdRate"]
      """  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  """  
      self.GetDefaultWhseFromGroup:bool = obj["GetDefaultWhseFromGroup"]
      """  Logical to direct where the Warehouse information about the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  """  
      self.Location:bool = obj["Location"]
      """  Location  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  """  
      self.LastCalDate:str = obj["LastCalDate"]
      """  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.EquipID:str = obj["EquipID"]
      """  EquipID of Equip record that is related to the Asset.  Can be blank, be if entered must be a valid Equip reference.  Note: maintained by Equipment Entry.  Read only in Asset Entry.  """  
      self.URL:str = obj["URL"]
      """  URL  """  
      self.JDFDevice:str = obj["JDFDevice"]
      """  JDFDevice  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.NumCavs:int = obj["NumCavs"]
      """  NumCavs  """  
      self.RunnerWt:int = obj["RunnerWt"]
      """  RunnerWt  """  
      self.SetupTime:int = obj["SetupTime"]
      """  SetupTime  """  
      self.TearDownTime:int = obj["TearDownTime"]
      """  TearDownTime  """  
      self.MiscInfo1:str = obj["MiscInfo1"]
      """  MiscInfo1  """  
      self.MiscInfo2:str = obj["MiscInfo2"]
      """  MiscInfo2  """  
      self.Brand:str = obj["Brand"]
      """  Brand  """  
      self.LocID:str = obj["LocID"]
      """  LocID  """  
      self.PmMapNo:int = obj["PmMapNo"]
      """  PmMapNo  """  
      self.SetupURL:str = obj["SetupURL"]
      """  SetupURL  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MobileResource:bool = obj["MobileResource"]
      """  MobileResource  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.MESQueue:bool = obj["MESQueue"]
      """  MESQueue  """  
      self.CharacteristicAttrClassID:str = obj["CharacteristicAttrClassID"]
      """  ID of related Attribute Class, the class must be of type Characteristics.  """  
      self.CharacteristicAttributeSetID:int = obj["CharacteristicAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.ECPCEnabled:bool = obj["ECPCEnabled"]
      """  If this field is true, it marks the selected Resource as Connected Process Control (CPC) enable. If disable, connection and/or sync will not be done.  """  
      self.EquipCreate:bool = obj["EquipCreate"]
      """  A flag set by the user. When true, system willcreate Equip record from the Resource if the Equip record does not already exist. The EquipID = ResourceID.  This occurs when the record is saved.  """  
      self.Plant:str = obj["Plant"]
      """  Plant from Resource Group  """  
      self.ReadOnlyFields:str = obj["ReadOnlyFields"]
      self.BitFlag:int = obj["BitFlag"]
      self.LinkedPartTrackLots:bool = obj["LinkedPartTrackLots"]
      self.LinkedPartPartDescription:str = obj["LinkedPartPartDescription"]
      self.LinkedPartIUM:str = obj["LinkedPartIUM"]
      self.LinkedPartTrackSerialNum:bool = obj["LinkedPartTrackSerialNum"]
      self.LinkedPartTrackDimension:bool = obj["LinkedPartTrackDimension"]
      self.LinkedPartSellingFactor:int = obj["LinkedPartSellingFactor"]
      self.LinkedPartSalesUM:str = obj["LinkedPartSalesUM"]
      self.LinkedPartPricePerCode:str = obj["LinkedPartPricePerCode"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.OpStdDescription:str = obj["OpStdDescription"]
      self.ProdCalDescription:str = obj["ProdCalDescription"]
      self.ResourceTypeDescription:str = obj["ResourceTypeDescription"]
      self.ResourceTypeExternalMESType:str = obj["ResourceTypeExternalMESType"]
      self.WhseBackflushWhseDescDescription:str = obj["WhseBackflushWhseDescDescription"]
      self.WhseInputWhseDescDescription:str = obj["WhseInputWhseDescDescription"]
      self.WhseOutputWhseDescDescription:str = obj["WhseOutputWhseDescDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class BuildRsrcGrpResourceCalList_input:
   """ Required : 
   cResourceGrpID
   """  
   def __init__(self, obj):
      self.cResourceGrpID:str = obj["cResourceGrpID"]
      """  The current Resource GroupID  """  
      pass

class BuildRsrcGrpResourceCalList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ResourceGroupTableset] = obj["returnObj"]
      pass

class BuildRsrcResourceCalList_input:
   """ Required : 
   cResourceGrpID
   cResourceID
   """  
   def __init__(self, obj):
      self.cResourceGrpID:str = obj["cResourceGrpID"]
      """  The current Resource Group ID  """  
      self.cResourceID:str = obj["cResourceID"]
      """  The current Resource ID  """  
      pass

class BuildRsrcResourceCalList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ResourceGroupTableset] = obj["returnObj"]
      pass

class ChangeResourceGroupResourceType_input:
   """ Required : 
   proposedResourceType
   ds
   """  
   def __init__(self, obj):
      self.proposedResourceType:str = obj["proposedResourceType"]
      """  The proposed value for ResourceType.  """  
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

class ChangeResourceGroupResourceType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeResourceResourceType_input:
   """ Required : 
   proposedResourceType
   ds
   """  
   def __init__(self, obj):
      self.proposedResourceType:str = obj["proposedResourceType"]
      """  The proposed value for ResourceType.  """  
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

class ChangeResourceResourceType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangedCharacteristicAttrClassID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

class ChangedCharacteristicAttrClassID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckRGPlant_input:
   """ Required : 
   cResourceGrpID
   """  
   def __init__(self, obj):
      self.cResourceGrpID:str = obj["cResourceGrpID"]
      """  The current Resource GroupID  """  
      pass

class CheckRGPlant_output:
   def __init__(self, obj):
      pass

class CustomizeResourceCalRsrcGrp_input:
   """ Required : 
   cResourceGrpID
   daDate
   ds
   """  
   def __init__(self, obj):
      self.cResourceGrpID:str = obj["cResourceGrpID"]
      """  The current Resource Group ID  """  
      self.daDate:str = obj["daDate"]
      """  The selected date to be customized  """  
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

class CustomizeResourceCalRsrcGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CustomizeResourceCalRsrc_input:
   """ Required : 
   cResourceID
   cResourceGrpID
   daDate
   ds
   """  
   def __init__(self, obj):
      self.cResourceID:str = obj["cResourceID"]
      """  The current Resource ID  """  
      self.cResourceGrpID:str = obj["cResourceGrpID"]
      """  The current Resource Group ID  """  
      self.daDate:str = obj["daDate"]
      """  The selected date to be customized  """  
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

class CustomizeResourceCalRsrc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   resourceGrpID
   """  
   def __init__(self, obj):
      self.resourceGrpID:str = obj["resourceGrpID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteResourceCal_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

class DeleteResourceCal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class EnterpriseGetList_input:
   """ Required : 
   whereClause
   enterpriseBAQID
   enterpriseSearchText
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  whereClause  """  
      self.enterpriseBAQID:str = obj["enterpriseBAQID"]
      """  Enterprise BAQ ID  """  
      self.enterpriseSearchText:str = obj["enterpriseSearchText"]
      """  Enterprise Search  """  
      self.pageSize:int = obj["pageSize"]
      """  pageSize  """  
      self.absolutePage:int = obj["absolutePage"]
      """  absolutePage  """  
      pass

class EnterpriseGetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ResourceGroupListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Erp_Tablesets_CapResLnkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CapabilityID:str = obj["CapabilityID"]
      """  A code which uniquely identifies the Capability this link applies to.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ResourceID the Capability is being linked to.  """  
      self.ResourcePriority:int = obj["ResourcePriority"]
      """  A tie breaker.  If two Resources are equal, but a user would prefer to keep one busy, then the one with the highest priority will be selected first.  """  
      self.ProductionFactor:int = obj["ProductionFactor"]
      """  A Production Factor for the link.  """  
      self.SetupFactor:int = obj["SetupFactor"]
      """  A Setup Factor for the link.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CapIDDescription:str = obj["CapIDDescription"]
      self.ResourceDescription:str = obj["ResourceDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ResourceCalRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code uniquely identifies a Resource Group.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.SpecialDay:str = obj["SpecialDay"]
      """  Exception Day  """  
      self.ProdHour01:bool = obj["ProdHour01"]
      """  ProdHour01  """  
      self.ProdHour02:bool = obj["ProdHour02"]
      """  ProdHour02  """  
      self.ProdHour03:bool = obj["ProdHour03"]
      """  ProdHour03  """  
      self.ProdHour04:bool = obj["ProdHour04"]
      """  ProdHour04  """  
      self.ProdHour05:bool = obj["ProdHour05"]
      """  ProdHour05  """  
      self.ProdHour06:bool = obj["ProdHour06"]
      """  ProdHour06  """  
      self.ProdHour07:bool = obj["ProdHour07"]
      """  ProdHour07  """  
      self.ProdHour08:bool = obj["ProdHour08"]
      """  ProdHour08  """  
      self.ProdHour09:bool = obj["ProdHour09"]
      """  ProdHour09  """  
      self.ProdHour10:bool = obj["ProdHour10"]
      """  ProdHour10  """  
      self.ProdHour11:bool = obj["ProdHour11"]
      """  ProdHour11  """  
      self.ProdHour12:bool = obj["ProdHour12"]
      """  ProdHour12  """  
      self.ProdHour13:bool = obj["ProdHour13"]
      """  ProdHour13  """  
      self.ProdHour14:bool = obj["ProdHour14"]
      """  ProdHour14  """  
      self.ProdHour15:bool = obj["ProdHour15"]
      """  ProdHour15  """  
      self.ProdHour16:bool = obj["ProdHour16"]
      """  ProdHour16  """  
      self.ProdHour17:bool = obj["ProdHour17"]
      """  ProdHour17  """  
      self.ProdHour18:bool = obj["ProdHour18"]
      """  ProdHour18  """  
      self.ProdHour19:bool = obj["ProdHour19"]
      """  ProdHour19  """  
      self.ProdHour20:bool = obj["ProdHour20"]
      """  ProdHour20  """  
      self.ProdHour21:bool = obj["ProdHour21"]
      """  ProdHour21  """  
      self.ProdHour22:bool = obj["ProdHour22"]
      """  ProdHour22  """  
      self.ProdHour23:bool = obj["ProdHour23"]
      """  ProdHour23  """  
      self.ProdHour24:bool = obj["ProdHour24"]
      """  ProdHour24  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExceptionLabel:str = obj["ExceptionLabel"]
      """  ExceptionLabel  """  
      self.DispExceptionLabel:str = obj["DispExceptionLabel"]
      """  Display Exception Label  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ResourceGroupAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ResourceGrpID:str = obj["ResourceGrpID"]
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

class Erp_Tablesets_ResourceGroupListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code uniquely identifies a Resource Group.  Cannot be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Description:str = obj["Description"]
      """  Long description of the Resource Group.  """  
      self.Inactive:bool = obj["Inactive"]
      """   Flag which indicates if the Resource Group is considered "Inactive".  For historical purposed, and data integrity, it is difficult to delete a ResourceGroup that has been used for production.  Instead, it is set to Inactive = YES.
This flag will be used to exclude Resource Groups from certain searches and reports.
Resource Groups where Inactive=yes are treated as deleted, but remain in the table to maintain database integrity.  """  
      self.JCDept:str = obj["JCDept"]
      """  The Key ID of the Home Department for this Resource Group.  This is a foreign key to the JCDept table.  """  
      self.ProdBurRate:int = obj["ProdBurRate"]
      """  The burden rate for production.  """  
      self.SetupBurRate:int = obj["SetupBurRate"]
      """  Default burden rate for Setup time.  """  
      self.QProdBurRate:int = obj["QProdBurRate"]
      """   Quoting burden rate for production in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.QSetupBurRate:int = obj["QSetupBurRate"]
      """   Quoting burden rate for setup in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.ResourceType:str = obj["ResourceType"]
      """  For scheduling purposes a Resource Group can be a Standard resource (S), Additional resource (D), or Auxiliary resource (X).  Standard resources use capacity when scheduled in a finite capacity workcenter.  An Auxiliary Resource can be used in production by  any operation concurrently with a Standard resource, but it does not use capacity.  This is significant for scheduling work to the machine.  Also, an Auxiliary resources does not have to be available for an entire operation.  Additional resources can be added to an Operation, they do use capacity and need to be available for the entire operation.  """  
      self.InputWhse:str = obj["InputWhse"]
      """  Indicates a warehouse  in which parts are staged for consumption by the Resource Group.  This must be valid in the Warehouse table.  """  
      self.OutputWhse:str = obj["OutputWhse"]
      """  Defines a warehouse for the output of a Resource Group.  This must be valid in the Warehouse table.  """  
      self.Location:bool = obj["Location"]
      """  Location  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CharacteristicAttrClassID:str = obj["CharacteristicAttrClassID"]
      """  ID of related Attribute Class, the class must be of type Characteristics.  """  
      self.CharacteristicAttributeSetID:int = obj["CharacteristicAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.JCDeptDescription:str = obj["JCDeptDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ResourceGroupListTableset:
   def __init__(self, obj):
      self.ResourceGroupList:list[Erp_Tablesets_ResourceGroupListRow] = obj["ResourceGroupList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ResourceGroupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code uniquely identifies a Resource Group.  Cannot be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Description:str = obj["Description"]
      """  Long description of the Resource Group.  """  
      self.CalendarID:str = obj["CalendarID"]
      """  Identifies the production calendar for this Resource Group.   If this equals "", then the ProdCal record is the Company Level production calendar.  """  
      self.Inactive:bool = obj["Inactive"]
      """   Flag which indicates if the Resource Group is considered "Inactive".  For historical purposed, and data integrity, it is difficult to delete a ResourceGroup that has been used for production.  Instead, it is set to Inactive = YES.
This flag will be used to exclude Resource Groups from certain searches and reports.
Resource Groups where Inactive=yes are treated as deleted, but remain in the table to maintain database integrity.  """  
      self.AllowManualOverride:bool = obj["AllowManualOverride"]
      """  If it is Finite Resource Group, and this is true, then the user will be allow to overload this Resource Group from using the scheduling tools.  """  
      self.FiniteHorizon:int = obj["FiniteHorizon"]
      """  The number of days out this Resource Group will be scheduled finitely.  Production capacity requirements past this day are treated as infinite.  """  
      self.NumberOfMachines:int = obj["NumberOfMachines"]
      """   The number of Resources in this Resource Group. The number of Resources X HrsPerMachine = Capacity.
A Resource Group with zero Resources is considered infinite capacity.  """  
      self.SchMachine:int = obj["SchMachine"]
      """  Number of Resources that one operation runs on at a time within this Resource Group.  This affects how much of the total daily Resource Group capacity is used up per operation.  If Resource Group has 4  Resource, 8 hour a day, and SchMachine = 2.  An operation will schedule up to 16 hours per day.   This is used as a default to the JobOper.Machines field.  """  
      self.BurdenType:str = obj["BurdenType"]
      """  Indicates if the BurdenRate fields are either a flat hourly dollar rate or a percentage of LaborRate. Default is Hourly dollar rate.   Set to "F" (flat) or "P" (percent).  """  
      self.MoveHours:int = obj["MoveHours"]
      """  The number of hours of delay that occurs when an operation leaves this Resource Group before the next operation can begin in a different Resource Group.  """  
      self.JCDept:str = obj["JCDept"]
      """  The Key ID of the Home Department for this Resource Group.  This is a foreign key to the JCDept table.  """  
      self.QueHours:int = obj["QueHours"]
      """  Queue Time.  The number of hours of delay that occurs when an operation enters this Resource Group before it can begin. (The opposite of MoveHours)  """  
      self.OpCode:str = obj["OpCode"]
      """  Establishes the default operation used when referencing this Resource Group.  This is optional, but if entered it must be valid in the OpMaster.  """  
      self.ProdBurRate:int = obj["ProdBurRate"]
      """  The burden rate for production.  """  
      self.ProdLabRate:int = obj["ProdLabRate"]
      """  The labor rate for production.  """  
      self.SetupBurRate:int = obj["SetupBurRate"]
      """  Default burden rate for Setup time.  """  
      self.SetupLabRate:int = obj["SetupLabRate"]
      """  Default labor rate for setup time.  """  
      self.QProdBurRate:int = obj["QProdBurRate"]
      """   Quoting burden rate for production in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.QProdLabRate:int = obj["QProdLabRate"]
      """   Quoting burden rate for production on the Resource.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.QSetupBurRate:int = obj["QSetupBurRate"]
      """   Quoting burden rate for setup in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.QSetupLabRate:int = obj["QSetupLabRate"]
      """   Quoting burden rate for setup in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.SplitBurden:bool = obj["SplitBurden"]
      """  Indicates if burden hours are split out among employees when multiple employees work simultaneously on the same job operation within this Resource Group.  This feature is only applicable to Data Collection.  Manual Labor Entry does not split the burden hours. The opposite is that each employee should have their burden hours = labor hours. This situation would occur in Resource Groups that actually have "people" as machines, such as an assembly or welding center where multiple people work on the same job.  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Defines the default crew size for work done in this Resource Group.   The number of people it physically takes to run the machine. This should not be confused with scheduled number of machines, which squeezes the schedule time. The crew size is a multiplier used in calculation of Production labor hours on operations.  """  
      self.SetupCrewSize:int = obj["SetupCrewSize"]
      """  Defines the default setup crew size for work done in this Resource Group.  The number of people it physically takes to setup the Resource.  This should not be confused with scheduled number of machines, which squeezes the schedule time.  The crew size is a multiplier  used in calculation of setup labor hours for an operation.  """  
      self.OpStdID:str = obj["OpStdID"]
      """  Defines a default Operation standard master ID for this Resource Group.  If entered then this along with the ResourceGrpID, OpCode must be valid in the OpStd master file.  """  
      self.ReloadNum:int = obj["ReloadNum"]
      """  lib/Reloader.w program increments and assigns it to Joboper.ReloadNum as it processes JobOper records. It is used to prevent redundant reads during the For Each loop.  """  
      self.ReloadStatus:str = obj["ReloadStatus"]
      """  A  recovery flag which indicates the status of the Reload process for this Resource Group.  Values; Blank or "Started".  """  
      self.DailyCapacity1:int = obj["DailyCapacity1"]
      """  DailyCapacity1  """  
      self.DailyCapacity2:int = obj["DailyCapacity2"]
      """  DailyCapacity2  """  
      self.DailyCapacity3:int = obj["DailyCapacity3"]
      """  DailyCapacity3  """  
      self.DailyCapacity4:int = obj["DailyCapacity4"]
      """  DailyCapacity4  """  
      self.DailyCapacity5:int = obj["DailyCapacity5"]
      """  DailyCapacity5  """  
      self.DailyCapacity6:int = obj["DailyCapacity6"]
      """  DailyCapacity6  """  
      self.DailyCapacity7:int = obj["DailyCapacity7"]
      """  DailyCapacity7  """  
      self.QBurdenType:str = obj["QBurdenType"]
      """  Indicates if the Quote Burden Rate fields are either a flat hourly dollar rate or a percentage of Quote LaborRate.  Default is Hourly dollar rate.  Set to "F" (flat) or "P" (percent).  """  
      self.BurdenEQLabor:bool = obj["BurdenEQLabor"]
      """  Indicates if burden hours should equal Labor Hours for work reported within this Resource Group.  This feature is only applicable to Data Collection.  This is intended to be used where an employee jumps between multiple job operations without clock in/out (for efficiency purposes).  Example: Employee works on 4 operations for 8am - 1200.  They clock out of all 4 at 12.  Each transaction is given 1hr of labor.  If this is checked then each transaction will also have 1hr of burden.  Otherwise they will have 4 hrs for a total of 16 burden hrs.  """  
      self.SplitOperations:bool = obj["SplitOperations"]
      """  Used for scheduling.  If YES then a single operation in this Resoure Group can be split across multiple Resources.  """  
      self.ResourceType:str = obj["ResourceType"]
      """  For scheduling purposes a Resource Group can be a Standard resource (S), Additional resource (D), or Auxiliary resource (X).  Standard resources use capacity when scheduled in a finite capacity workcenter.  An Auxiliary Resource can be used in production by  any operation concurrently with a Standard resource, but it does not use capacity.  This is significant for scheduling work to the machine.  Also, an Auxiliary resources does not have to be available for an entire operation.  Additional resources can be added to an Operation, they do use capacity and need to be available for the entire operation.  """  
      self.InputWhse:str = obj["InputWhse"]
      """  Indicates a warehouse  in which parts are staged for consumption by the Resource Group.  This must be valid in the Warehouse table.  """  
      self.InputBinNum:str = obj["InputBinNum"]
      """  Indicates a warehouse bin  in which parts are staged for consumption by the Resource Group.  It  must be valid in the WhseBin table.  """  
      self.OutputWhse:str = obj["OutputWhse"]
      """  Defines a warehouse for the output of a Resource Group.  This must be valid in the Warehouse table.  """  
      self.OutputBinNum:str = obj["OutputBinNum"]
      """  Defines a warehouse bin for the output of a Resource Group.  It  must be valid in the WhseBin table.  """  
      self.BackflushWhse:str = obj["BackflushWhse"]
      """  Defines a warehouse for backflushing material of a Resource Group.  This must be valid in the Warehouse table.   Used with the InputWhse/InputBin.  If a JobMtl record is set to be backflushed, the the JobMtl is linked to a JobOper, and the Resource Group for the JobOper has a backflush warehouse, then the material will be backflushed from that warehouse when there is not a positive quantity available for the Resource Group InputWhse/Input Bin.  """  
      self.BackflushBinNum:str = obj["BackflushBinNum"]
      """  Defines a warehouse bin for backflushing for the Resource Group.  It  must be valid in the WhseBin table.  """  
      self.InformOverload:bool = obj["InformOverload"]
      """  Indicates that Resource Group is visible in Overload Informer.  """  
      self.MinOverloadPerc:int = obj["MinOverloadPerc"]
      """  The minimum overload threshold before a day shows up in the Overload Informer.  """  
      self.BackflushEmpID:str = obj["BackflushEmpID"]
      """  Is the Employee ID which will be defaulted into LaborDtl records which get created through backflushing.  If this field is blank, then the Employee ID on the LaborDtl record causing the backflush process to be triggered will be used.  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the Resource Group as being a "SubContract" or an "Internal".  This will determine the default when adding an operation to a BOM, Job, or Quote.  """  
      self.AutoMove:bool = obj["AutoMove"]
      """  To toggle on and off the automove flag for a Resource Group.  When false , the default is to generate a move request. When true the default is to not generate a move request. These defaults can be seen when entering a quantity and ending an activity in labor entry.  """  
      self.UseEstimates:bool = obj["UseEstimates"]
      """  Indicates if hours are split out using estimate values when working  on multiple  job operations.  """  
      self.DailyProdQty:int = obj["DailyProdQty"]
      """  Daily Production Qty: The production quantity developed to satisfy demand.  The cell is designed to produce at that quantity for a given time frame (daily).  """  
      self.BillLaborRate:int = obj["BillLaborRate"]
      """  Field Service - Labor rate used for time on an operation.  Time per hour per technician.  """  
      self.DailyProdRate:int = obj["DailyProdRate"]
      """  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity .   Once the production limit for a resource  has been reached, the Resource has been consumed for that day.  """  
      self.Location:bool = obj["Location"]
      """  Location  """  
      self.DistributeLoad:bool = obj["DistributeLoad"]
      """  Distribute Load  """  
      self.TrkProdAct:bool = obj["TrkProdAct"]
      """  Flag to indicate whether to track production activity of the resource group.  """  
      self.SetShopLoad:bool = obj["SetShopLoad"]
      """  When the capcity changes for a resourceGroup (in Resource Group Entry), this flag is set to true to indicate that Generate Shop Capacity process needs to be run to update the ShopLoad records.  This used to be performed within ResourceGroupEntry but for performance reasons it is being moved to the Generate Shop Capacity process  """  
      self.TAKTValue:int = obj["TAKTValue"]
      """  TAKT Value  """  
      self.UseCalendarForMove:bool = obj["UseCalendarForMove"]
      """  Use Calendar for Move Time  """  
      self.UseCalendarForQueue:bool = obj["UseCalendarForQueue"]
      """  Use Calendar for Queue Time  """  
      self.URL:str = obj["URL"]
      """  URL  """  
      self.JDFDevice:str = obj["JDFDevice"]
      """  JDFDevice  """  
      self.JDFOperation:str = obj["JDFOperation"]
      """  JDFOperation  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.MESQueue:bool = obj["MESQueue"]
      """  MESQueue  """  
      self.CharacteristicAttrClassID:str = obj["CharacteristicAttrClassID"]
      """  ID of related Attribute Class, the class must be of type Characteristics.  """  
      self.CharacteristicAttributeSetID:int = obj["CharacteristicAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.inputwhsedesc:str = obj["inputwhsedesc"]
      self.outputwhsedesc:str = obj["outputwhsedesc"]
      self.backflushempname:str = obj["backflushempname"]
      self.backflushwhsedesc:str = obj["backflushwhsedesc"]
      self.EnableInactive:bool = obj["EnableInactive"]
      """  Indicates if the Inactive flag should be enabled.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.JCDeptDescription:str = obj["JCDeptDescription"]
      self.OPCodeOpDesc:str = obj["OPCodeOpDesc"]
      self.OpStdDescription:str = obj["OpStdDescription"]
      self.ProdCalDescription:str = obj["ProdCalDescription"]
      self.ResourceTypeExternalMESType:str = obj["ResourceTypeExternalMESType"]
      self.ResourceTypeDescription:str = obj["ResourceTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ResourceGroupTableset:
   def __init__(self, obj):
      self.ResourceGroup:list[Erp_Tablesets_ResourceGroupRow] = obj["ResourceGroup"]
      self.ResourceGroupAttch:list[Erp_Tablesets_ResourceGroupAttchRow] = obj["ResourceGroupAttch"]
      self.Resource:list[Erp_Tablesets_ResourceRow] = obj["Resource"]
      self.CapResLnk:list[Erp_Tablesets_CapResLnkRow] = obj["CapResLnk"]
      self.ResourceCal:list[Erp_Tablesets_ResourceCalRow] = obj["ResourceCal"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ResourceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code that identifies the Resource Group that the resource belongs to.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.Description:str = obj["Description"]
      """  Full description of Resource.  """  
      self.Inactive:bool = obj["Inactive"]
      """   Flag which indicates if the Resource is considered "Inactive".
This flag will be used to exclude Resources from certain searches and reports.
When Inactive=yes the Resource is treated as deleted, but will remain in the table to maintain database integrity.  """  
      self.Finite:bool = obj["Finite"]
      """  If yes then this Resource is scheduled as though it has finite production capacity.  """  
      self.AllowManualOverride:bool = obj["AllowManualOverride"]
      """  If it is Finite Resource, and this is true, then the user will be allow to overload this resource from using the scheduling tools.  """  
      self.NextMaintDate:str = obj["NextMaintDate"]
      """  This Resources next scheduled maintenance date. An optional, user entered field. This can be used in report selections. It does not effect any scheduling logic.  """  
      self.OutputWhse:str = obj["OutputWhse"]
      """  Defines a warehouse for the output of a Resource Group.  This must be valid in the Warehouse table.  """  
      self.OutputBinNum:str = obj["OutputBinNum"]
      """  Defines a warehouse bin for the output of a Resource Group.  It  must be valid in the WhseBin table.  """  
      self.BackflushWhse:str = obj["BackflushWhse"]
      """  Defines a warehouse for backflushing material of a Resource Group.  This must be valid in the Warehouse table.   Used with the InputWhse/InputBin.  If a JobMtl record is set to be backflushed, the the JobMtl is linked to a JobOper, and the Resource Group for the JobOper has a backflush warehouse, then the material will be backflushed from that warehouse when there is not a positive quantity available for the Resource Group InputWhse/Input Bin.  """  
      self.BackflushBinNum:str = obj["BackflushBinNum"]
      """  Defines a warehouse bin for backflushing for the Resource Group.  It  must be valid in the WhseBin table.  """  
      self.InputWhse:str = obj["InputWhse"]
      """  Indicates a warehouse  in which parts are staged for consumption by the Resource Group.  This must be valid in the Warehouse table.  """  
      self.InputBinNum:str = obj["InputBinNum"]
      """  Indicates a warehouse bin  in which parts are staged for consumption by the Resource Group.  It  must be valid in the WhseBin table.  """  
      self.ResourceType:str = obj["ResourceType"]
      """  Allow the Resource to be linked to a ResourceType record.  This is only used for analysis purposes.  """  
      self.ConcurrentCapacity:int = obj["ConcurrentCapacity"]
      """  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  """  
      self.TrackProdQty:bool = obj["TrackProdQty"]
      """  Indicates the production quantities produced by this Resource will be tracked.  """  
      self.LinkedPart:str = obj["LinkedPart"]
      """  Links this Resource to a Part, which must be valid in the Part table.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the Resource.  Links the Resource to a Fixed Asset.  """  
      self.ProdBurRate:int = obj["ProdBurRate"]
      """  The burden rate for production.  """  
      self.ProdLabRate:int = obj["ProdLabRate"]
      """  The labor rate for production.  """  
      self.SetupBurRate:int = obj["SetupBurRate"]
      """  Default burden rate for Setup time.  """  
      self.SetupLabRate:int = obj["SetupLabRate"]
      """  Default labor rate for setup time.  """  
      self.QProdBurRate:int = obj["QProdBurRate"]
      """   Quoting burden rate for production on the Resource
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.QProdLabRate:int = obj["QProdLabRate"]
      """   Quoting burden rate for production on the Resource.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.QSetupBurRate:int = obj["QSetupBurRate"]
      """   Quoting burden rate for setup in the Resource.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.QSetupLabRate:int = obj["QSetupLabRate"]
      """   Quoting burden rate for "setup" in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.QBurdenType:str = obj["QBurdenType"]
      """  Indicates if the Quote Burden Rate fields are either a flat hourly dollar rate or a percentage of Quote LaborRate.  Default is flat hourly rate.  Valid values are "F" (flat) or "P" (percent).  """  
      self.GetDefaultBurdenFromGroup:bool = obj["GetDefaultBurdenFromGroup"]
      """  Logical to direct where the burden rate information about the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  If this field is set this is be a subcontracted resource.  """  
      self.BurdenType:str = obj["BurdenType"]
      """  Indicates if the BurdenRate fields are either a flat hourly dollar rate or a percentage of LaborRate. Default is Hourly dollar rate.   Set to "F" (flat) or "P" (percent).  """  
      self.CalendarID:str = obj["CalendarID"]
      """  Identifies the production calendar for this Resource.   If this equals "", then the ProdCal record is the Resource Group Level production calendar.  """  
      self.MoveHours:int = obj["MoveHours"]
      """  The number of hours of delay that occurs when an operation leaves this Resource before the next operation can begin in a different Resource.  """  
      self.QueHours:int = obj["QueHours"]
      """  Queue Time.  The number of hours of delay that occurs when an operation enters this Resource before it can begin. (The opposite of MoveHours)  """  
      self.GetDefaultMQFromGroup:bool = obj["GetDefaultMQFromGroup"]
      """  Logical to direct where the Move Time and Queue time for the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  This also controls whether the FiniteHorizon  and SplitOperation is from the Resource Group.  """  
      self.InformOverload:bool = obj["InformOverload"]
      """  Indicates that the Resource is visible in Overload Informer.  """  
      self.MinOverloadPerc:int = obj["MinOverloadPerc"]
      """  The minimum overload threshold before a day shows up in the Overload Informer.  """  
      self.OpCode:str = obj["OpCode"]
      """   Establishes the default operation used when referencing this Resource.  This is optional, but if entered it must be valid in the OpMaster.
Required if a Resource is going to be used to create a JobOper record.  """  
      self.OpStdID:str = obj["OpStdID"]
      """   Defines a default Operation standard master ID for this Resource.  If entered then this along with the ResourceGrpID, OpCode must be valid in the OpStd master file.
Required if the Resource is going to be used to create a JobOper.  """  
      self.GetDefaultLaborFromGroup:bool = obj["GetDefaultLaborFromGroup"]
      """  Logical to direct where the labor rate information about the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  """  
      self.FiniteHorizon:int = obj["FiniteHorizon"]
      """  The number of days out this Resource will be scheduled finitely.  Production capacity requirements past this day are treated as infinite.  """  
      self.AutoMove:bool = obj["AutoMove"]
      """  To toggle on and off the AutoMove flag for a Resource.  When false, the default is to generate a move request.  When true the default is to not generate a move request.  These defaults can be seen when entering a quantity and ending an activity in labor entry.  """  
      self.SplitOperations:bool = obj["SplitOperations"]
      """  Used for scheduling.  If YES then a single operation on this Resource can be split into multiple operations.  """  
      self.DailyProdQty:int = obj["DailyProdQty"]
      """  The production Qty developed to satisfy demand.  The cell is designed to produce at that rate for a given time frame (daily) until this production qty is met.  """  
      self.BillLaborRate:int = obj["BillLaborRate"]
      """  Field Service - Labor rate used for time on an operation.  Time per hour per technician.  """  
      self.DailyProdRate:int = obj["DailyProdRate"]
      """  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  """  
      self.GetDefaultWhseFromGroup:bool = obj["GetDefaultWhseFromGroup"]
      """  Logical to direct where the Warehouse information about the resource is held. Either to look at the resource itself or to look at the associated ResourceGroup record.  """  
      self.Location:bool = obj["Location"]
      """  Location  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  """  
      self.LastCalDate:str = obj["LastCalDate"]
      """  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.EquipID:str = obj["EquipID"]
      """  EquipID of Equip record that is related to the Asset.  Can be blank, be if entered must be a valid Equip reference.  Note: maintained by Equipment Entry.  Read only in Asset Entry.  """  
      self.URL:str = obj["URL"]
      """  URL  """  
      self.JDFDevice:str = obj["JDFDevice"]
      """  JDFDevice  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.NumCavs:int = obj["NumCavs"]
      """  NumCavs  """  
      self.RunnerWt:int = obj["RunnerWt"]
      """  RunnerWt  """  
      self.SetupTime:int = obj["SetupTime"]
      """  SetupTime  """  
      self.TearDownTime:int = obj["TearDownTime"]
      """  TearDownTime  """  
      self.MiscInfo1:str = obj["MiscInfo1"]
      """  MiscInfo1  """  
      self.MiscInfo2:str = obj["MiscInfo2"]
      """  MiscInfo2  """  
      self.Brand:str = obj["Brand"]
      """  Brand  """  
      self.LocID:str = obj["LocID"]
      """  LocID  """  
      self.PmMapNo:int = obj["PmMapNo"]
      """  PmMapNo  """  
      self.SetupURL:str = obj["SetupURL"]
      """  SetupURL  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MobileResource:bool = obj["MobileResource"]
      """  MobileResource  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.MESQueue:bool = obj["MESQueue"]
      """  MESQueue  """  
      self.CharacteristicAttrClassID:str = obj["CharacteristicAttrClassID"]
      """  ID of related Attribute Class, the class must be of type Characteristics.  """  
      self.CharacteristicAttributeSetID:int = obj["CharacteristicAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.ECPCEnabled:bool = obj["ECPCEnabled"]
      """  If this field is true, it marks the selected Resource as Connected Process Control (CPC) enable. If disable, connection and/or sync will not be done.  """  
      self.EquipCreate:bool = obj["EquipCreate"]
      """  A flag set by the user. When true, system willcreate Equip record from the Resource if the Equip record does not already exist. The EquipID = ResourceID.  This occurs when the record is saved.  """  
      self.Plant:str = obj["Plant"]
      """  Plant from Resource Group  """  
      self.ReadOnlyFields:str = obj["ReadOnlyFields"]
      self.BitFlag:int = obj["BitFlag"]
      self.LinkedPartTrackLots:bool = obj["LinkedPartTrackLots"]
      self.LinkedPartPartDescription:str = obj["LinkedPartPartDescription"]
      self.LinkedPartIUM:str = obj["LinkedPartIUM"]
      self.LinkedPartTrackSerialNum:bool = obj["LinkedPartTrackSerialNum"]
      self.LinkedPartTrackDimension:bool = obj["LinkedPartTrackDimension"]
      self.LinkedPartSellingFactor:int = obj["LinkedPartSellingFactor"]
      self.LinkedPartSalesUM:str = obj["LinkedPartSalesUM"]
      self.LinkedPartPricePerCode:str = obj["LinkedPartPricePerCode"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.OpStdDescription:str = obj["OpStdDescription"]
      self.ProdCalDescription:str = obj["ProdCalDescription"]
      self.ResourceTypeDescription:str = obj["ResourceTypeDescription"]
      self.ResourceTypeExternalMESType:str = obj["ResourceTypeExternalMESType"]
      self.WhseBackflushWhseDescDescription:str = obj["WhseBackflushWhseDescDescription"]
      self.WhseInputWhseDescDescription:str = obj["WhseInputWhseDescDescription"]
      self.WhseOutputWhseDescDescription:str = obj["WhseOutputWhseDescDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtResourceGroupTableset:
   def __init__(self, obj):
      self.ResourceGroup:list[Erp_Tablesets_ResourceGroupRow] = obj["ResourceGroup"]
      self.ResourceGroupAttch:list[Erp_Tablesets_ResourceGroupAttchRow] = obj["ResourceGroupAttch"]
      self.Resource:list[Erp_Tablesets_ResourceRow] = obj["Resource"]
      self.CapResLnk:list[Erp_Tablesets_CapResLnkRow] = obj["CapResLnk"]
      self.ResourceCal:list[Erp_Tablesets_ResourceCalRow] = obj["ResourceCal"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   resourceGrpID
   """  
   def __init__(self, obj):
      self.resourceGrpID:str = obj["resourceGrpID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ResourceGroupTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ResourceGroupTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ResourceGroupTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ResourceGroupListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCapResLnk_input:
   """ Required : 
   ds
   capabilityID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      self.capabilityID:str = obj["capabilityID"]
      pass

class GetNewCapResLnk_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewResourceCal_input:
   """ Required : 
   ds
   resourceGrpID
   resourceID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      self.resourceGrpID:str = obj["resourceGrpID"]
      self.resourceID:str = obj["resourceID"]
      pass

class GetNewResourceCal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewResourceGroupAttch_input:
   """ Required : 
   ds
   resourceGrpID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      self.resourceGrpID:str = obj["resourceGrpID"]
      pass

class GetNewResourceGroupAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewResourceGroup_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

class GetNewResourceGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewResource_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

class GetNewResource_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetResourceGroupsExtMES_input:
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

class GetResourceGroupsExtMES_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ResourceGroupListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseResourceGroup
   whereClauseResourceGroupAttch
   whereClauseResource
   whereClauseCapResLnk
   whereClauseResourceCal
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseResourceGroup:str = obj["whereClauseResourceGroup"]
      self.whereClauseResourceGroupAttch:str = obj["whereClauseResourceGroupAttch"]
      self.whereClauseResource:str = obj["whereClauseResource"]
      self.whereClauseCapResLnk:str = obj["whereClauseCapResLnk"]
      self.whereClauseResourceCal:str = obj["whereClauseResourceCal"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ResourceGroupTableset] = obj["returnObj"]
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

class InsertNewResource_input:
   """ Required : 
   ipResourceID
   ipResourceGrpID
   ds
   """  
   def __init__(self, obj):
      self.ipResourceID:str = obj["ipResourceID"]
      """  The new resource id value.  """  
      self.ipResourceGrpID:str = obj["ipResourceGrpID"]
      """  The resourcegrp id value that you are adding this resource to  """  
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

class InsertNewResource_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MoveResourceCal_input:
   """ Required : 
   ds
   pOriginalDay
   pNewDay
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      self.pOriginalDay:str = obj["pOriginalDay"]
      """  The original day of the excpetion  """  
      self.pNewDay:str = obj["pNewDay"]
      """  The new day the excpetion was moved to  """  
      pass

class MoveResourceCal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MoveResource_input:
   """ Required : 
   ds
   ipResourceID
   ipFromResourceGrpID
   ipToResourceGrpID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      self.ipResourceID:str = obj["ipResourceID"]
      """  The moving resource id value.  """  
      self.ipFromResourceGrpID:str = obj["ipFromResourceGrpID"]
      """  The resourcegrp id value that you are moving the resource from.  """  
      self.ipToResourceGrpID:str = obj["ipToResourceGrpID"]
      """  The resourcegrp id value that you are moving the resource to.  """  
      pass

class MoveResource_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      self.showWarningMessage:bool = obj["showWarningMessage"]
      pass

      """  output parameters  """  

class RequestExternalMESActiveResourceTypeValidation_input:
   """ Required : 
   company
   resourceType
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.resourceType:str = obj["resourceType"]
      pass

class RequestExternalMESActiveResourceTypeValidation_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class SelectDistinctInOutWhseQuery_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class SetInactiveFlag_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

class SetInactiveFlag_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtResourceGroupTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtResourceGroupTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateResourceCal_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

class UpdateResourceCal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ResourceGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateInspection_input:
   """ Required : 
   ipProposedInspPlan
   ipProposedSpecId
   """  
   def __init__(self, obj):
      self.ipProposedInspPlan:str = obj["ipProposedInspPlan"]
      """  The new proposed InspPlanPartNum value  """  
      self.ipProposedSpecId:str = obj["ipProposedSpecId"]
      """  The new proposed SpecID value  """  
      pass

class ValidateInspection_output:
   def __init__(self, obj):
      pass

class ValidateResource_input:
   """ Required : 
   ipResourceID
   ipResourceGrpID
   """  
   def __init__(self, obj):
      self.ipResourceID:str = obj["ipResourceID"]
      """  The resource id value to validate.  """  
      self.ipResourceGrpID:str = obj["ipResourceGrpID"]
      """  The resourcegrp id value to validate.  """  
      pass

class ValidateResource_output:
   def __init__(self, obj):
      pass

