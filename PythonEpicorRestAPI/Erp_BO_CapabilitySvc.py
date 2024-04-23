import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CapabilitySvc
# Description: bo/Capbility/Capbility.p
           Capability business object
           TerryP
           01/21/04 SCR11618
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Capabilities(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Capabilities items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Capabilities
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CapabilityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/Capabilities",headers=creds) as resp:
           return await resp.json()

async def post_Capabilities(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Capabilities
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CapabilityRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CapabilityRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/Capabilities", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Capabilities_Company_CapabilityID(Company, CapabilityID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Capability item
   Description: Calls GetByID to retrieve the Capability item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Capability
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CapabilityID: Desc: CapabilityID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CapabilityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/Capabilities(" + Company + "," + CapabilityID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Capabilities_Company_CapabilityID(Company, CapabilityID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Capability for the service
   Description: Calls UpdateExt to update Capability. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Capability
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CapabilityID: Desc: CapabilityID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CapabilityRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/Capabilities(" + Company + "," + CapabilityID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Capabilities_Company_CapabilityID(Company, CapabilityID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Capability item
   Description: Call UpdateExt to delete Capability item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Capability
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CapabilityID: Desc: CapabilityID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/Capabilities(" + Company + "," + CapabilityID + ")",headers=creds) as resp:
           return await resp.json()

async def get_Capabilities_Company_CapabilityID_CapAddls(Company, CapabilityID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CapAddls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CapAddls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CapabilityID: Desc: CapabilityID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CapAddlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/Capabilities(" + Company + "," + CapabilityID + ")/CapAddls",headers=creds) as resp:
           return await resp.json()

async def get_Capabilities_Company_CapabilityID_CapAddls_Company_CapabilityID_CapAddID(Company, CapabilityID, CapAddID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CapAddl item
   Description: Calls GetByID to retrieve the CapAddl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CapAddl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CapabilityID: Desc: CapabilityID   Required: True   Allow empty value : True
      :param CapAddID: Desc: CapAddID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CapAddlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/Capabilities(" + Company + "," + CapabilityID + ")/CapAddls(" + Company + "," + CapabilityID + "," + CapAddID + ")",headers=creds) as resp:
           return await resp.json()

async def get_Capabilities_Company_CapabilityID_CapResLnks(Company, CapabilityID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CapResLnks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CapResLnks1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CapabilityID: Desc: CapabilityID   Required: True   Allow empty value : True
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/Capabilities(" + Company + "," + CapabilityID + ")/CapResLnks",headers=creds) as resp:
           return await resp.json()

async def get_Capabilities_Company_CapabilityID_CapResLnks_Company_CapabilityID_ResourceID(Company, CapabilityID, ResourceID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CapResLnk item
   Description: Calls GetByID to retrieve the CapResLnk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CapResLnk1
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/Capabilities(" + Company + "," + CapabilityID + ")/CapResLnks(" + Company + "," + CapabilityID + "," + ResourceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CapAddls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CapAddls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CapAddls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CapAddlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/CapAddls",headers=creds) as resp:
           return await resp.json()

async def post_CapAddls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CapAddls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CapAddlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CapAddlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/CapAddls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CapAddls_Company_CapabilityID_CapAddID(Company, CapabilityID, CapAddID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CapAddl item
   Description: Calls GetByID to retrieve the CapAddl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CapAddl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CapabilityID: Desc: CapabilityID   Required: True   Allow empty value : True
      :param CapAddID: Desc: CapAddID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CapAddlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/CapAddls(" + Company + "," + CapabilityID + "," + CapAddID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CapAddls_Company_CapabilityID_CapAddID(Company, CapabilityID, CapAddID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CapAddl for the service
   Description: Calls UpdateExt to update CapAddl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CapAddl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CapabilityID: Desc: CapabilityID   Required: True   Allow empty value : True
      :param CapAddID: Desc: CapAddID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CapAddlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/CapAddls(" + Company + "," + CapabilityID + "," + CapAddID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CapAddls_Company_CapabilityID_CapAddID(Company, CapabilityID, CapAddID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CapAddl item
   Description: Call UpdateExt to delete CapAddl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CapAddl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CapabilityID: Desc: CapabilityID   Required: True   Allow empty value : True
      :param CapAddID: Desc: CapAddID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/CapAddls(" + Company + "," + CapabilityID + "," + CapAddID + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/CapResLnks",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/CapResLnks", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/CapResLnks(" + Company + "," + CapabilityID + "," + ResourceID + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/CapResLnks(" + Company + "," + CapabilityID + "," + ResourceID + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/CapResLnks(" + Company + "," + CapabilityID + "," + ResourceID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CapabilityListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCapability, whereClauseCapAddl, whereClauseCapResLnk, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCapability=" + whereClauseCapability
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCapAddl=" + whereClauseCapAddl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(capabilityID, epicorHeaders = None):
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
   params += "capabilityID=" + capabilityID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_externalMESEnabled(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method externalMESEnabled
   OperationID: externalMESEnabled
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/externalMESEnabled_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/externalMESEnabled_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_getCapabilityIDDescription(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method getCapabilityIDDescription
   Description: Returns the description of the selected CapabilityID
   OperationID: getCapabilityIDDescription
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getCapabilityIDDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getCapabilityIDDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCapability(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCapability
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCapability
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCapability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCapability_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCapAddl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCapAddl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCapAddl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCapAddl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCapAddl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CapabilitySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CapAddlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CapAddlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CapResLnkRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CapResLnkRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CapabilityListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CapabilityListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CapabilityRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CapabilityRow] = obj["value"]
      pass

class Erp_Tablesets_CapAddlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CapabilityID:str = obj["CapabilityID"]
      """  A code which uniquely identifies a capability.  """  
      self.CapAddID:str = obj["CapAddID"]
      """  Additional Capability ID  """  
      self.Description:str = obj["Description"]
      """  Description of the capability.  """  
      self.ProductionCap:bool = obj["ProductionCap"]
      """  This Additional Capability is required for Production.  """  
      self.SetupCap:bool = obj["SetupCap"]
      """  This Additional Capability is required for Setup.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
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

class Erp_Tablesets_CapabilityListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CapabilityID:str = obj["CapabilityID"]
      """  A code which uniquely identifies a capability.  """  
      self.Description:str = obj["Description"]
      """  Description of the capability.  """  
      self.Inactive:bool = obj["Inactive"]
      """   Flag which indicates if the Capability is considered as "Active".
This flag will be used to exclude Capabilities from certain searches and reports.
To maintain database integrity, once a Capability has been used in cannot be deleted.  But it can be set to Inactive=yes, which will exclude the record from most searches.  """  
      self.PrimaryResourceGrpID:str = obj["PrimaryResourceGrpID"]
      """  Defines the primary Resource Group for this Capability, but it can be blank.   If not blank, it must be valid in the ResourceGroup table.  """  
      self.AdditionalResourceRequired:bool = obj["AdditionalResourceRequired"]
      """  When TRUE an error message will be generated when the routing is created an no additional resources have been defined.  """  
      self.SetupGroupRequired:bool = obj["SetupGroupRequired"]
      """  When TRUE will cause a warning message when the routing is created and no setup group is defined.  """  
      self.CapType:str = obj["CapType"]
      """  Identifies if this capability should pull costs (from either the ResourceGroup or Resource) for "L" = Labor, "R" = Burden, or "B" = both Labor and Burden.  """  
      self.OpCode:str = obj["OpCode"]
      """   Establishes the default operation used when referencing this Capability.  This is optional, but if entered it must be valid in the OpMaster.
Required if a Capability is going to be used to create a JobOper record.  """  
      self.OpStdID:str = obj["OpStdID"]
      """   Defines a default Operation standard master ID for this Capability.  If entered then this along with the ResourceGrpID, OpCode must be valid in the OpStd master file.
Required if the Capability is going to be used to create a JobOper.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates if the record is used with Machine MES  """  
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      """  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  """  
      self.OpStdDescription:str = obj["OpStdDescription"]
      """  Description of the operation standard.  Cannot be blank.  """  
      self.PrimResGrpIDDescription:str = obj["PrimResGrpIDDescription"]
      """  Long description of the Resource Group.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CapabilityRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CapabilityID:str = obj["CapabilityID"]
      """  A code which uniquely identifies a capability.  """  
      self.Description:str = obj["Description"]
      """  Description of the capability.  """  
      self.Inactive:bool = obj["Inactive"]
      """   Flag which indicates if the Capability is considered as "Active".
This flag will be used to exclude Capabilities from certain searches and reports.
To maintain database integrity, once a Capability has been used in cannot be deleted.  But it can be set to Inactive=yes, which will exclude the record from most searches.  """  
      self.PrimaryResourceGrpID:str = obj["PrimaryResourceGrpID"]
      """  Defines the primary Resource Group for this Capability, but it can be blank.   If not blank, it must be valid in the ResourceGroup table.  """  
      self.AdditionalResourceRequired:bool = obj["AdditionalResourceRequired"]
      """  When TRUE an error message will be generated when the routing is created an no additional resources have been defined.  """  
      self.SetupGroupRequired:bool = obj["SetupGroupRequired"]
      """  When TRUE will cause a warning message when the routing is created and no setup group is defined.  """  
      self.CapType:str = obj["CapType"]
      """  Identifies if this capability should pull costs (from either the ResourceGroup or Resource) for "L" = Labor, "R" = Burden, or "B" = both Labor and Burden.  """  
      self.OpCode:str = obj["OpCode"]
      """   Establishes the default operation used when referencing this Capability.  This is optional, but if entered it must be valid in the OpMaster.
Required if a Capability is going to be used to create a JobOper record.  """  
      self.OpStdID:str = obj["OpStdID"]
      """   Defines a default Operation standard master ID for this Capability.  If entered then this along with the ResourceGrpID, OpCode must be valid in the OpStd master file.
Required if the Capability is going to be used to create a JobOper.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates if the record is used with Machine MES  """  
      self.BitFlag:int = obj["BitFlag"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.OpStdDescription:str = obj["OpStdDescription"]
      self.PrimResGrpIDDescription:str = obj["PrimResGrpIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   capabilityID
   """  
   def __init__(self, obj):
      self.capabilityID:str = obj["capabilityID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CapAddlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CapabilityID:str = obj["CapabilityID"]
      """  A code which uniquely identifies a capability.  """  
      self.CapAddID:str = obj["CapAddID"]
      """  Additional Capability ID  """  
      self.Description:str = obj["Description"]
      """  Description of the capability.  """  
      self.ProductionCap:bool = obj["ProductionCap"]
      """  This Additional Capability is required for Production.  """  
      self.SetupCap:bool = obj["SetupCap"]
      """  This Additional Capability is required for Setup.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
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

class Erp_Tablesets_CapabilityListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CapabilityID:str = obj["CapabilityID"]
      """  A code which uniquely identifies a capability.  """  
      self.Description:str = obj["Description"]
      """  Description of the capability.  """  
      self.Inactive:bool = obj["Inactive"]
      """   Flag which indicates if the Capability is considered as "Active".
This flag will be used to exclude Capabilities from certain searches and reports.
To maintain database integrity, once a Capability has been used in cannot be deleted.  But it can be set to Inactive=yes, which will exclude the record from most searches.  """  
      self.PrimaryResourceGrpID:str = obj["PrimaryResourceGrpID"]
      """  Defines the primary Resource Group for this Capability, but it can be blank.   If not blank, it must be valid in the ResourceGroup table.  """  
      self.AdditionalResourceRequired:bool = obj["AdditionalResourceRequired"]
      """  When TRUE an error message will be generated when the routing is created an no additional resources have been defined.  """  
      self.SetupGroupRequired:bool = obj["SetupGroupRequired"]
      """  When TRUE will cause a warning message when the routing is created and no setup group is defined.  """  
      self.CapType:str = obj["CapType"]
      """  Identifies if this capability should pull costs (from either the ResourceGroup or Resource) for "L" = Labor, "R" = Burden, or "B" = both Labor and Burden.  """  
      self.OpCode:str = obj["OpCode"]
      """   Establishes the default operation used when referencing this Capability.  This is optional, but if entered it must be valid in the OpMaster.
Required if a Capability is going to be used to create a JobOper record.  """  
      self.OpStdID:str = obj["OpStdID"]
      """   Defines a default Operation standard master ID for this Capability.  If entered then this along with the ResourceGrpID, OpCode must be valid in the OpStd master file.
Required if the Capability is going to be used to create a JobOper.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates if the record is used with Machine MES  """  
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      """  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  """  
      self.OpStdDescription:str = obj["OpStdDescription"]
      """  Description of the operation standard.  Cannot be blank.  """  
      self.PrimResGrpIDDescription:str = obj["PrimResGrpIDDescription"]
      """  Long description of the Resource Group.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CapabilityListTableset:
   def __init__(self, obj):
      self.CapabilityList:list[Erp_Tablesets_CapabilityListRow] = obj["CapabilityList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CapabilityRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CapabilityID:str = obj["CapabilityID"]
      """  A code which uniquely identifies a capability.  """  
      self.Description:str = obj["Description"]
      """  Description of the capability.  """  
      self.Inactive:bool = obj["Inactive"]
      """   Flag which indicates if the Capability is considered as "Active".
This flag will be used to exclude Capabilities from certain searches and reports.
To maintain database integrity, once a Capability has been used in cannot be deleted.  But it can be set to Inactive=yes, which will exclude the record from most searches.  """  
      self.PrimaryResourceGrpID:str = obj["PrimaryResourceGrpID"]
      """  Defines the primary Resource Group for this Capability, but it can be blank.   If not blank, it must be valid in the ResourceGroup table.  """  
      self.AdditionalResourceRequired:bool = obj["AdditionalResourceRequired"]
      """  When TRUE an error message will be generated when the routing is created an no additional resources have been defined.  """  
      self.SetupGroupRequired:bool = obj["SetupGroupRequired"]
      """  When TRUE will cause a warning message when the routing is created and no setup group is defined.  """  
      self.CapType:str = obj["CapType"]
      """  Identifies if this capability should pull costs (from either the ResourceGroup or Resource) for "L" = Labor, "R" = Burden, or "B" = both Labor and Burden.  """  
      self.OpCode:str = obj["OpCode"]
      """   Establishes the default operation used when referencing this Capability.  This is optional, but if entered it must be valid in the OpMaster.
Required if a Capability is going to be used to create a JobOper record.  """  
      self.OpStdID:str = obj["OpStdID"]
      """   Defines a default Operation standard master ID for this Capability.  If entered then this along with the ResourceGrpID, OpCode must be valid in the OpStd master file.
Required if the Capability is going to be used to create a JobOper.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates if the record is used with Machine MES  """  
      self.BitFlag:int = obj["BitFlag"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.OpStdDescription:str = obj["OpStdDescription"]
      self.PrimResGrpIDDescription:str = obj["PrimResGrpIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CapabilityTableset:
   def __init__(self, obj):
      self.Capability:list[Erp_Tablesets_CapabilityRow] = obj["Capability"]
      self.CapAddl:list[Erp_Tablesets_CapAddlRow] = obj["CapAddl"]
      self.CapResLnk:list[Erp_Tablesets_CapResLnkRow] = obj["CapResLnk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCapabilityTableset:
   def __init__(self, obj):
      self.Capability:list[Erp_Tablesets_CapabilityRow] = obj["Capability"]
      self.CapAddl:list[Erp_Tablesets_CapAddlRow] = obj["CapAddl"]
      self.CapResLnk:list[Erp_Tablesets_CapResLnkRow] = obj["CapResLnk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   capabilityID
   """  
   def __init__(self, obj):
      self.capabilityID:str = obj["capabilityID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CapabilityTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CapabilityTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CapabilityTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CapabilityListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCapAddl_input:
   """ Required : 
   ds
   capabilityID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CapabilityTableset] = obj["ds"]
      self.capabilityID:str = obj["capabilityID"]
      pass

class GetNewCapAddl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CapabilityTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCapResLnk_input:
   """ Required : 
   ds
   capabilityID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CapabilityTableset] = obj["ds"]
      self.capabilityID:str = obj["capabilityID"]
      pass

class GetNewCapResLnk_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CapabilityTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCapability_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CapabilityTableset] = obj["ds"]
      pass

class GetNewCapability_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CapabilityTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCapability
   whereClauseCapAddl
   whereClauseCapResLnk
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCapability:str = obj["whereClauseCapability"]
      self.whereClauseCapAddl:str = obj["whereClauseCapAddl"]
      self.whereClauseCapResLnk:str = obj["whereClauseCapResLnk"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CapabilityTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtCapabilityTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCapabilityTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CapabilityTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CapabilityTableset] = obj["ds"]
      pass

      """  output parameters  """  

class externalMESEnabled_input:
   """ Required : 
   capabilityID
   """  
   def __init__(self, obj):
      self.capabilityID:str = obj["capabilityID"]
      pass

class externalMESEnabled_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class getCapabilityIDDescription_input:
   """ Required : 
   capabilityID
   """  
   def __init__(self, obj):
      self.capabilityID:str = obj["capabilityID"]
      """  CapabilityID  """  
      pass

class getCapabilityIDDescription_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Capability.Description  """  
      pass

