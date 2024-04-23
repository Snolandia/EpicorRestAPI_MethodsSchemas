import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.LookupDataSvc
# Description: Object to manage Lookup data: LookupTable, LookupLink, SourceValueField, TargetValueField
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_LookupDatas(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LookupDatas items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LookupDatas
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LookupTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupDatas",headers=creds) as resp:
           return await resp.json()

async def post_LookupDatas(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LookupDatas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LookupTableRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LookupTableRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupDatas", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LookupDatas_Company_MapUID(Company, MapUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LookupData item
   Description: Calls GetByID to retrieve the LookupData item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LookupData
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapUID: Desc: MapUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LookupTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupDatas(" + Company + "," + MapUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LookupDatas_Company_MapUID(Company, MapUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LookupData for the service
   Description: Calls UpdateExt to update LookupData. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LookupData
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapUID: Desc: MapUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LookupTableRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupDatas(" + Company + "," + MapUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LookupDatas_Company_MapUID(Company, MapUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LookupData item
   Description: Call UpdateExt to delete LookupData item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LookupData
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapUID: Desc: MapUID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupDatas(" + Company + "," + MapUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_LookupDatas_Company_MapUID_LookupLinks(Company, MapUID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LookupLinks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LookupLinks1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapUID: Desc: MapUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LookupLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupDatas(" + Company + "," + MapUID + ")/LookupLinks",headers=creds) as resp:
           return await resp.json()

async def get_LookupDatas_Company_MapUID_LookupLinks_Company_MapUID_LinkUID(Company, MapUID, LinkUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LookupLink item
   Description: Calls GetByID to retrieve the LookupLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LookupLink1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapUID: Desc: MapUID   Required: True
      :param LinkUID: Desc: LinkUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LookupLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupDatas(" + Company + "," + MapUID + ")/LookupLinks(" + Company + "," + MapUID + "," + LinkUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_LookupDatas_Company_MapUID_SourceValueFields(Company, MapUID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SourceValueFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SourceValueFields1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapUID: Desc: MapUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SourceValueFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupDatas(" + Company + "," + MapUID + ")/SourceValueFields",headers=creds) as resp:
           return await resp.json()

async def get_LookupDatas_Company_MapUID_SourceValueFields_Company_MapUID_SequenceNumber(Company, MapUID, SequenceNumber, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SourceValueField item
   Description: Calls GetByID to retrieve the SourceValueField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SourceValueField1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapUID: Desc: MapUID   Required: True
      :param SequenceNumber: Desc: SequenceNumber   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SourceValueFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupDatas(" + Company + "," + MapUID + ")/SourceValueFields(" + Company + "," + MapUID + "," + SequenceNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_LookupDatas_Company_MapUID_TargetValueFields(Company, MapUID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TargetValueFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TargetValueFields1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapUID: Desc: MapUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TargetValueFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupDatas(" + Company + "," + MapUID + ")/TargetValueFields",headers=creds) as resp:
           return await resp.json()

async def get_LookupDatas_Company_MapUID_TargetValueFields_Company_MapUID_SequenceNumber(Company, MapUID, SequenceNumber, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TargetValueField item
   Description: Calls GetByID to retrieve the TargetValueField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TargetValueField1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapUID: Desc: MapUID   Required: True
      :param SequenceNumber: Desc: SequenceNumber   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TargetValueFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupDatas(" + Company + "," + MapUID + ")/TargetValueFields(" + Company + "," + MapUID + "," + SequenceNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_LookupLinks(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LookupLinks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LookupLinks
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LookupLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupLinks",headers=creds) as resp:
           return await resp.json()

async def post_LookupLinks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LookupLinks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LookupLinkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LookupLinkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupLinks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LookupLinks_Company_MapUID_LinkUID(Company, MapUID, LinkUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LookupLink item
   Description: Calls GetByID to retrieve the LookupLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LookupLink
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapUID: Desc: MapUID   Required: True
      :param LinkUID: Desc: LinkUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LookupLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupLinks(" + Company + "," + MapUID + "," + LinkUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LookupLinks_Company_MapUID_LinkUID(Company, MapUID, LinkUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LookupLink for the service
   Description: Calls UpdateExt to update LookupLink. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LookupLink
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapUID: Desc: MapUID   Required: True
      :param LinkUID: Desc: LinkUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LookupLinkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupLinks(" + Company + "," + MapUID + "," + LinkUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LookupLinks_Company_MapUID_LinkUID(Company, MapUID, LinkUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LookupLink item
   Description: Call UpdateExt to delete LookupLink item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LookupLink
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapUID: Desc: MapUID   Required: True
      :param LinkUID: Desc: LinkUID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/LookupLinks(" + Company + "," + MapUID + "," + LinkUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SourceValueFields(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SourceValueFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SourceValueFields
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SourceValueFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/SourceValueFields",headers=creds) as resp:
           return await resp.json()

async def post_SourceValueFields(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SourceValueFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SourceValueFieldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SourceValueFieldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/SourceValueFields", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SourceValueFields_Company_MapUID_SequenceNumber(Company, MapUID, SequenceNumber, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SourceValueField item
   Description: Calls GetByID to retrieve the SourceValueField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SourceValueField
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapUID: Desc: MapUID   Required: True
      :param SequenceNumber: Desc: SequenceNumber   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SourceValueFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/SourceValueFields(" + Company + "," + MapUID + "," + SequenceNumber + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SourceValueFields_Company_MapUID_SequenceNumber(Company, MapUID, SequenceNumber, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SourceValueField for the service
   Description: Calls UpdateExt to update SourceValueField. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SourceValueField
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapUID: Desc: MapUID   Required: True
      :param SequenceNumber: Desc: SequenceNumber   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SourceValueFieldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/SourceValueFields(" + Company + "," + MapUID + "," + SequenceNumber + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SourceValueFields_Company_MapUID_SequenceNumber(Company, MapUID, SequenceNumber, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SourceValueField item
   Description: Call UpdateExt to delete SourceValueField item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SourceValueField
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapUID: Desc: MapUID   Required: True
      :param SequenceNumber: Desc: SequenceNumber   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/SourceValueFields(" + Company + "," + MapUID + "," + SequenceNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_TargetValueFields(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TargetValueFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TargetValueFields
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TargetValueFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/TargetValueFields",headers=creds) as resp:
           return await resp.json()

async def post_TargetValueFields(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TargetValueFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TargetValueFieldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TargetValueFieldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/TargetValueFields", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TargetValueFields_Company_MapUID_SequenceNumber(Company, MapUID, SequenceNumber, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TargetValueField item
   Description: Calls GetByID to retrieve the TargetValueField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TargetValueField
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapUID: Desc: MapUID   Required: True
      :param SequenceNumber: Desc: SequenceNumber   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TargetValueFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/TargetValueFields(" + Company + "," + MapUID + "," + SequenceNumber + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TargetValueFields_Company_MapUID_SequenceNumber(Company, MapUID, SequenceNumber, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TargetValueField for the service
   Description: Calls UpdateExt to update TargetValueField. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TargetValueField
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapUID: Desc: MapUID   Required: True
      :param SequenceNumber: Desc: SequenceNumber   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TargetValueFieldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/TargetValueFields(" + Company + "," + MapUID + "," + SequenceNumber + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TargetValueFields_Company_MapUID_SequenceNumber(Company, MapUID, SequenceNumber, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TargetValueField item
   Description: Call UpdateExt to delete TargetValueField item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TargetValueField
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MapUID: Desc: MapUID   Required: True
      :param SequenceNumber: Desc: SequenceNumber   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/TargetValueFields(" + Company + "," + MapUID + "," + SequenceNumber + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LookupTableListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseLookupTable, whereClauseLookupLink, whereClauseSourceValueField, whereClauseTargetValueField, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseLookupTable=" + whereClauseLookupTable
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLookupLink=" + whereClauseLookupLink
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSourceValueField=" + whereClauseSourceValueField
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTargetValueField=" + whereClauseTargetValueField
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(mapUID, epicorHeaders = None):
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
   params += "mapUID=" + mapUID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetByDisplayName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByDisplayName
   Description: This method returns LookupData dataset if display name is known
   OperationID: GetByDisplayName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByDisplayName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByDisplayName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCOASegments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCOASegments
   Description: This method returns list of COA segments
   OperationID: GetCOASegments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCOASegments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCOASegments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCOASegmentVals(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCOASegmentVals
   Description: This method returns list of COA segments
   OperationID: GetCOASegmentVals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCOASegmentVals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCOASegmentVals_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFieldValueList2(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFieldValueList2
   OperationID: GetFieldValueList2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFieldValueList2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFieldValueList2_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDBStructure(epicorHeaders = None):
   """  
   Summary: Invoke method GetDBStructure
   Description: This method returns dataset with schemas and tables info.
   OperationID: GetDBStructure
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDBStructure_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_LoadTableFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadTableFields
   Description: This method adds rows to the table DBLoadedField. The includes fields from peer tables and user defined tables.
   OperationID: LoadTableFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadTableFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadTableFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetColumnDataType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetColumnDataType
   Description: This method returns data type of the specified field.
   OperationID: GetColumnDataType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetColumnDataType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetColumnDataType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportToFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportToFile
   Description: This method generates the file according to extension.
   OperationID: ExportToFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportToFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportToFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportFromFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportFromFile
   Description: This method generates the file according to extension.
   OperationID: ImportFromFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportFromFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportFromFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDynamicData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDynamicData
   Description: GetDynamicData - returns an untyped dynamic dataset
   OperationID: GetDynamicData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDynamicData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDynamicData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PopulateLookupLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PopulateLookupLink
   OperationID: PopulateLookupLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PopulateLookupLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PopulateLookupLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLookupTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLookupTable
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLookupTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLookupTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLookupTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLookupLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLookupLink
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLookupLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLookupLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLookupLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSourceValueField(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSourceValueField
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSourceValueField
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSourceValueField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSourceValueField_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTargetValueField(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTargetValueField
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTargetValueField
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTargetValueField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTargetValueField_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LookupDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LookupLinkRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LookupLinkRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LookupTableListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LookupTableListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LookupTableRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LookupTableRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SourceValueFieldRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SourceValueFieldRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TargetValueFieldRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TargetValueFieldRow] = obj["value"]
      pass

class Erp_Tablesets_LookupLinkRow:
   def __init__(self, obj):
      self.LinkUID:int = obj["LinkUID"]
      """  Link unique ID.  """  
      self.MapUID:int = obj["MapUID"]
      """  Map unique ID.  """  
      self.Field1:str = obj["Field1"]
      """  Field1  """  
      self.Field2:str = obj["Field2"]
      """  Field2  """  
      self.Field3:str = obj["Field3"]
      """  Field3  """  
      self.Field4:str = obj["Field4"]
      """  Field4  """  
      self.Field5:str = obj["Field5"]
      """  Field5  """  
      self.Field6:str = obj["Field6"]
      """  Field6  """  
      self.Field7:str = obj["Field7"]
      """  Field7  """  
      self.Field8:str = obj["Field8"]
      """  Field8  """  
      self.Field9:str = obj["Field9"]
      """  Field9  """  
      self.Field10:str = obj["Field10"]
      """  Field10  """  
      self.Field11:str = obj["Field11"]
      """  Field11  """  
      self.Field12:str = obj["Field12"]
      """  Field12  """  
      self.Field13:str = obj["Field13"]
      """  Field13  """  
      self.Field14:str = obj["Field14"]
      """  Field14  """  
      self.Field15:str = obj["Field15"]
      """  Field15  """  
      self.Field16:str = obj["Field16"]
      """  Field16  """  
      self.Field17:str = obj["Field17"]
      """  Field17  """  
      self.Field18:str = obj["Field18"]
      """  Field18  """  
      self.Field19:str = obj["Field19"]
      """  Field19  """  
      self.Field20:str = obj["Field20"]
      """  Field20  """  
      self.Field21:str = obj["Field21"]
      """  Field21  """  
      self.Field22:str = obj["Field22"]
      """  Field22  """  
      self.Field23:str = obj["Field23"]
      """  Field23  """  
      self.Field24:str = obj["Field24"]
      """  Field24  """  
      self.Field25:str = obj["Field25"]
      """  Field25  """  
      self.Field26:str = obj["Field26"]
      """  Field26  """  
      self.Field27:str = obj["Field27"]
      """  Field27  """  
      self.Field28:str = obj["Field28"]
      """  Field28  """  
      self.Field29:str = obj["Field29"]
      """  Field29  """  
      self.Field30:str = obj["Field30"]
      """  Field30  """  
      self.Value1:str = obj["Value1"]
      """  Value1  """  
      self.Value2:str = obj["Value2"]
      """  Value2  """  
      self.Value3:str = obj["Value3"]
      """  Value3  """  
      self.Value4:str = obj["Value4"]
      """  Value4  """  
      self.Value5:str = obj["Value5"]
      """  Value5  """  
      self.Value6:str = obj["Value6"]
      """  Value6  """  
      self.Value7:str = obj["Value7"]
      """  Value7  """  
      self.Value8:str = obj["Value8"]
      """  Value8  """  
      self.Value9:str = obj["Value9"]
      """  Value9  """  
      self.Value10:str = obj["Value10"]
      """  Value10  """  
      self.Value11:str = obj["Value11"]
      """  Value11  """  
      self.Value12:str = obj["Value12"]
      """  Value12  """  
      self.Value13:str = obj["Value13"]
      """  Value13  """  
      self.Value14:str = obj["Value14"]
      """  Value14  """  
      self.Value15:str = obj["Value15"]
      """  Value15  """  
      self.Value16:str = obj["Value16"]
      """  Value16  """  
      self.Value17:str = obj["Value17"]
      """  Value17  """  
      self.Value18:str = obj["Value18"]
      """  Value18  """  
      self.Value19:str = obj["Value19"]
      """  Value19  """  
      self.Value20:str = obj["Value20"]
      """  Value20  """  
      self.Value21:str = obj["Value21"]
      """  Value21  """  
      self.Value22:str = obj["Value22"]
      """  Value22  """  
      self.Value23:str = obj["Value23"]
      """  Value23  """  
      self.Value24:str = obj["Value24"]
      """  Value24  """  
      self.Value25:str = obj["Value25"]
      """  Value25  """  
      self.Value26:str = obj["Value26"]
      """  Value26  """  
      self.Value27:str = obj["Value27"]
      """  Value27  """  
      self.Value28:str = obj["Value28"]
      """  Value28  """  
      self.Value29:str = obj["Value29"]
      """  Value29  """  
      self.Value30:str = obj["Value30"]
      """  Value30  """  
      self.CreationDate:str = obj["CreationDate"]
      """  System date when the link was created.  """  
      self.CreationTime:int = obj["CreationTime"]
      """  System time when the link was created (seconds since midnight format).  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  """  
      self.GlobalLookupLink:bool = obj["GlobalLookupLink"]
      """  Marks this LookupLink as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspField1:str = obj["DspField1"]
      self.DspField2:str = obj["DspField2"]
      self.DspField3:str = obj["DspField3"]
      self.DspField4:str = obj["DspField4"]
      self.DspField5:str = obj["DspField5"]
      self.DspField6:str = obj["DspField6"]
      self.DspField7:str = obj["DspField7"]
      self.DspField8:str = obj["DspField8"]
      self.DspField9:str = obj["DspField9"]
      self.DspField10:str = obj["DspField10"]
      self.DspField11:str = obj["DspField11"]
      self.DspField12:str = obj["DspField12"]
      self.DspField13:str = obj["DspField13"]
      self.DspField14:str = obj["DspField14"]
      self.DspField15:str = obj["DspField15"]
      self.DspField16:str = obj["DspField16"]
      self.DspField17:str = obj["DspField17"]
      self.DspField18:str = obj["DspField18"]
      self.DspField19:str = obj["DspField19"]
      self.DspField20:str = obj["DspField20"]
      self.DspField21:str = obj["DspField21"]
      self.DspField22:str = obj["DspField22"]
      self.DspField23:str = obj["DspField23"]
      self.DspField24:str = obj["DspField24"]
      self.DspField25:str = obj["DspField25"]
      self.DspField26:str = obj["DspField26"]
      self.DspField27:str = obj["DspField27"]
      self.DspField28:str = obj["DspField28"]
      self.DspField29:str = obj["DspField29"]
      self.DspField30:str = obj["DspField30"]
      self.DspValue1:str = obj["DspValue1"]
      self.DspValue2:str = obj["DspValue2"]
      self.DspValue3:str = obj["DspValue3"]
      self.DspValue4:str = obj["DspValue4"]
      self.DspValue5:str = obj["DspValue5"]
      self.DspValue6:str = obj["DspValue6"]
      self.DspValue7:str = obj["DspValue7"]
      self.DspValue8:str = obj["DspValue8"]
      self.DspValue9:str = obj["DspValue9"]
      self.DspValue10:str = obj["DspValue10"]
      self.DspValue11:str = obj["DspValue11"]
      self.DspValue12:str = obj["DspValue12"]
      self.DspValue13:str = obj["DspValue13"]
      self.DspValue14:str = obj["DspValue14"]
      self.DspValue15:str = obj["DspValue15"]
      self.DspValue16:str = obj["DspValue16"]
      self.DspValue17:str = obj["DspValue17"]
      self.DspValue18:str = obj["DspValue18"]
      self.DspValue19:str = obj["DspValue19"]
      self.DspValue20:str = obj["DspValue20"]
      self.DspValue21:str = obj["DspValue21"]
      self.DspValue22:str = obj["DspValue22"]
      self.DspValue23:str = obj["DspValue23"]
      self.DspValue24:str = obj["DspValue24"]
      self.DspValue25:str = obj["DspValue25"]
      self.DspValue26:str = obj["DspValue26"]
      self.DspValue27:str = obj["DspValue27"]
      self.DspValue28:str = obj["DspValue28"]
      self.DspValue29:str = obj["DspValue29"]
      self.DspValue30:str = obj["DspValue30"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LookupTableListRow:
   def __init__(self, obj):
      self.MapUID:int = obj["MapUID"]
      """  Map unique ID.  """  
      self.DisplayName:str = obj["DisplayName"]
      """  Lookup table name wich should be displayed in a tree view controls.  """  
      self.LookupName:str = obj["LookupName"]
      """  Lookup table name.  """  
      self.DetailedDescription:str = obj["DetailedDescription"]
      """  Detailed description of the lookup table.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlobalLookupTable:bool = obj["GlobalLookupTable"]
      """  Marks this LookupTable as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LookupTableRow:
   def __init__(self, obj):
      self.MapUID:int = obj["MapUID"]
      """  Map unique ID.  """  
      self.DisplayName:str = obj["DisplayName"]
      """  Lookup table name wich should be displayed in a tree view controls.  """  
      self.LookupName:str = obj["LookupName"]
      """  Lookup table name.  """  
      self.DetailedDescription:str = obj["DetailedDescription"]
      """  Detailed description of the lookup table.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlobalLookupTable:bool = obj["GlobalLookupTable"]
      """  Marks this LookupTable as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SourceValueFieldRow:
   def __init__(self, obj):
      self.SourceValueFieldUID:int = obj["SourceValueFieldUID"]
      """  Source value field unique ID.  """  
      self.MapUID:int = obj["MapUID"]
      """  Map unique ID.  """  
      self.SequenceNumber:int = obj["SequenceNumber"]
      """  Field sequence number.  """  
      self.FieldName:str = obj["FieldName"]
      """  Source field name.  """  
      self.DetailedDescription:str = obj["DetailedDescription"]
      """  Detailed description.  """  
      self.DBTable:str = obj["DBTable"]
      """  Database table which field linked to the source value field.  """  
      self.DBField:str = obj["DBField"]
      """  Field which linked to the source value field.  """  
      self.Validate:bool = obj["Validate"]
      """  Turns on the validation of the field.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlobalSourceValueField:bool = obj["GlobalSourceValueField"]
      """  Marks this SourceValueField as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DBSchemaName:str = obj["DBSchemaName"]
      """  DBSchemaName  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TargetValueFieldRow:
   def __init__(self, obj):
      self.TargetValueFieldUID:int = obj["TargetValueFieldUID"]
      """  Target value field unique ID.  """  
      self.MapUID:int = obj["MapUID"]
      """  Map unique ID.  """  
      self.SequenceNumber:int = obj["SequenceNumber"]
      """  Field sequence number.  """  
      self.FieldName:str = obj["FieldName"]
      """  Target field name.  """  
      self.DetailedDescription:str = obj["DetailedDescription"]
      """  Detailed description.  """  
      self.ValueType:str = obj["ValueType"]
      """  Value Type  """  
      self.COACode:str = obj["COACode"]
      """  Chart of accounts. Like COA.COACode.  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  Accounting segment from selected chart of accounts. Like COASegment.SegmentNbr.  """  
      self.Validate:bool = obj["Validate"]
      """  Turns on the validation of the field.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlobalTargetValueField:bool = obj["GlobalTargetValueField"]
      """  Marks this TargetValueField as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SegmentName:str = obj["SegmentName"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   mapUID
   """  
   def __init__(self, obj):
      self.mapUID:int = obj["mapUID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_DBLoadedFieldRow:
   def __init__(self, obj):
      self.DBSchemaName:str = obj["DBSchemaName"]
      self.DBTableName:str = obj["DBTableName"]
      self.DisplayFieldName:str = obj["DisplayFieldName"]
      self.ExtSchemaName:str = obj["ExtSchemaName"]
      self.ExtTableName:str = obj["ExtTableName"]
      self.ExtFieldName:str = obj["ExtFieldName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DBSchemaRow:
   def __init__(self, obj):
      self.DBSchemaName:str = obj["DBSchemaName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DBStructureTableset:
   def __init__(self, obj):
      self.DBSchema:list[Erp_Tablesets_DBSchemaRow] = obj["DBSchema"]
      self.DBTable:list[Erp_Tablesets_DBTableRow] = obj["DBTable"]
      self.DBLoadedField:list[Erp_Tablesets_DBLoadedFieldRow] = obj["DBLoadedField"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DBTableRow:
   def __init__(self, obj):
      self.DBSchemaName:str = obj["DBSchemaName"]
      """  Db Schema of the Database table from Ice.Table view  """  
      self.DBTableName:str = obj["DBTableName"]
      self.DBTableType:str = obj["DBTableType"]
      """  DB = Database, TT = Temp Table from ZDataTable  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynFieldAttributesRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.DataTableID:str = obj["DataTableID"]
      self.FieldName:str = obj["FieldName"]
      self.DataType:str = obj["DataType"]
      self.Required:bool = obj["Required"]
      self.ReadOnly:bool = obj["ReadOnly"]
      self.FieldFormat:str = obj["FieldFormat"]
      self.FieldLabel:str = obj["FieldLabel"]
      self.LikeDataFieldSystemCode:str = obj["LikeDataFieldSystemCode"]
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      self.CurrencyCodeColumn:str = obj["CurrencyCodeColumn"]
      self.CurrencyType:str = obj["CurrencyType"]
      self.CurrencySource:str = obj["CurrencySource"]
      self.BizType:str = obj["BizType"]
      self.CGCCode:str = obj["CGCCode"]
      self.UomColumn:str = obj["UomColumn"]
      self.CodeDescriptionList:str = obj["CodeDescriptionList"]
      self.Seq:int = obj["Seq"]
      self.IsHidden:bool = obj["IsHidden"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynFieldHelpRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.DataTableID:str = obj["DataTableID"]
      self.FieldName:str = obj["FieldName"]
      self.Description:str = obj["Description"]
      self.DBTableName:str = obj["DBTableName"]
      self.DBFieldName:str = obj["DBFieldName"]
      self.External:bool = obj["External"]
      self.InitialValue:str = obj["InitialValue"]
      self.IsDescriptionField:bool = obj["IsDescriptionField"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynTableAttributesRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.DataTableID:str = obj["DataTableID"]
      """  The actual generic table name used by the BL  """  
      self.UniqueTableID:str = obj["UniqueTableID"]
      """  Unique identifier for the virtual schema  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynamicMetadataTableset:
   def __init__(self, obj):
      self.DynTableAttributes:list[Erp_Tablesets_DynTableAttributesRow] = obj["DynTableAttributes"]
      self.DynFieldAttributes:list[Erp_Tablesets_DynFieldAttributesRow] = obj["DynFieldAttributes"]
      self.DynFieldHelp:list[Erp_Tablesets_DynFieldHelpRow] = obj["DynFieldHelp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LookupDataTableset:
   def __init__(self, obj):
      self.LookupTable:list[Erp_Tablesets_LookupTableRow] = obj["LookupTable"]
      self.LookupLink:list[Erp_Tablesets_LookupLinkRow] = obj["LookupLink"]
      self.SourceValueField:list[Erp_Tablesets_SourceValueFieldRow] = obj["SourceValueField"]
      self.TargetValueField:list[Erp_Tablesets_TargetValueFieldRow] = obj["TargetValueField"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LookupLinkRow:
   def __init__(self, obj):
      self.LinkUID:int = obj["LinkUID"]
      """  Link unique ID.  """  
      self.MapUID:int = obj["MapUID"]
      """  Map unique ID.  """  
      self.Field1:str = obj["Field1"]
      """  Field1  """  
      self.Field2:str = obj["Field2"]
      """  Field2  """  
      self.Field3:str = obj["Field3"]
      """  Field3  """  
      self.Field4:str = obj["Field4"]
      """  Field4  """  
      self.Field5:str = obj["Field5"]
      """  Field5  """  
      self.Field6:str = obj["Field6"]
      """  Field6  """  
      self.Field7:str = obj["Field7"]
      """  Field7  """  
      self.Field8:str = obj["Field8"]
      """  Field8  """  
      self.Field9:str = obj["Field9"]
      """  Field9  """  
      self.Field10:str = obj["Field10"]
      """  Field10  """  
      self.Field11:str = obj["Field11"]
      """  Field11  """  
      self.Field12:str = obj["Field12"]
      """  Field12  """  
      self.Field13:str = obj["Field13"]
      """  Field13  """  
      self.Field14:str = obj["Field14"]
      """  Field14  """  
      self.Field15:str = obj["Field15"]
      """  Field15  """  
      self.Field16:str = obj["Field16"]
      """  Field16  """  
      self.Field17:str = obj["Field17"]
      """  Field17  """  
      self.Field18:str = obj["Field18"]
      """  Field18  """  
      self.Field19:str = obj["Field19"]
      """  Field19  """  
      self.Field20:str = obj["Field20"]
      """  Field20  """  
      self.Field21:str = obj["Field21"]
      """  Field21  """  
      self.Field22:str = obj["Field22"]
      """  Field22  """  
      self.Field23:str = obj["Field23"]
      """  Field23  """  
      self.Field24:str = obj["Field24"]
      """  Field24  """  
      self.Field25:str = obj["Field25"]
      """  Field25  """  
      self.Field26:str = obj["Field26"]
      """  Field26  """  
      self.Field27:str = obj["Field27"]
      """  Field27  """  
      self.Field28:str = obj["Field28"]
      """  Field28  """  
      self.Field29:str = obj["Field29"]
      """  Field29  """  
      self.Field30:str = obj["Field30"]
      """  Field30  """  
      self.Value1:str = obj["Value1"]
      """  Value1  """  
      self.Value2:str = obj["Value2"]
      """  Value2  """  
      self.Value3:str = obj["Value3"]
      """  Value3  """  
      self.Value4:str = obj["Value4"]
      """  Value4  """  
      self.Value5:str = obj["Value5"]
      """  Value5  """  
      self.Value6:str = obj["Value6"]
      """  Value6  """  
      self.Value7:str = obj["Value7"]
      """  Value7  """  
      self.Value8:str = obj["Value8"]
      """  Value8  """  
      self.Value9:str = obj["Value9"]
      """  Value9  """  
      self.Value10:str = obj["Value10"]
      """  Value10  """  
      self.Value11:str = obj["Value11"]
      """  Value11  """  
      self.Value12:str = obj["Value12"]
      """  Value12  """  
      self.Value13:str = obj["Value13"]
      """  Value13  """  
      self.Value14:str = obj["Value14"]
      """  Value14  """  
      self.Value15:str = obj["Value15"]
      """  Value15  """  
      self.Value16:str = obj["Value16"]
      """  Value16  """  
      self.Value17:str = obj["Value17"]
      """  Value17  """  
      self.Value18:str = obj["Value18"]
      """  Value18  """  
      self.Value19:str = obj["Value19"]
      """  Value19  """  
      self.Value20:str = obj["Value20"]
      """  Value20  """  
      self.Value21:str = obj["Value21"]
      """  Value21  """  
      self.Value22:str = obj["Value22"]
      """  Value22  """  
      self.Value23:str = obj["Value23"]
      """  Value23  """  
      self.Value24:str = obj["Value24"]
      """  Value24  """  
      self.Value25:str = obj["Value25"]
      """  Value25  """  
      self.Value26:str = obj["Value26"]
      """  Value26  """  
      self.Value27:str = obj["Value27"]
      """  Value27  """  
      self.Value28:str = obj["Value28"]
      """  Value28  """  
      self.Value29:str = obj["Value29"]
      """  Value29  """  
      self.Value30:str = obj["Value30"]
      """  Value30  """  
      self.CreationDate:str = obj["CreationDate"]
      """  System date when the link was created.  """  
      self.CreationTime:int = obj["CreationTime"]
      """  System time when the link was created (seconds since midnight format).  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  """  
      self.GlobalLookupLink:bool = obj["GlobalLookupLink"]
      """  Marks this LookupLink as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspField1:str = obj["DspField1"]
      self.DspField2:str = obj["DspField2"]
      self.DspField3:str = obj["DspField3"]
      self.DspField4:str = obj["DspField4"]
      self.DspField5:str = obj["DspField5"]
      self.DspField6:str = obj["DspField6"]
      self.DspField7:str = obj["DspField7"]
      self.DspField8:str = obj["DspField8"]
      self.DspField9:str = obj["DspField9"]
      self.DspField10:str = obj["DspField10"]
      self.DspField11:str = obj["DspField11"]
      self.DspField12:str = obj["DspField12"]
      self.DspField13:str = obj["DspField13"]
      self.DspField14:str = obj["DspField14"]
      self.DspField15:str = obj["DspField15"]
      self.DspField16:str = obj["DspField16"]
      self.DspField17:str = obj["DspField17"]
      self.DspField18:str = obj["DspField18"]
      self.DspField19:str = obj["DspField19"]
      self.DspField20:str = obj["DspField20"]
      self.DspField21:str = obj["DspField21"]
      self.DspField22:str = obj["DspField22"]
      self.DspField23:str = obj["DspField23"]
      self.DspField24:str = obj["DspField24"]
      self.DspField25:str = obj["DspField25"]
      self.DspField26:str = obj["DspField26"]
      self.DspField27:str = obj["DspField27"]
      self.DspField28:str = obj["DspField28"]
      self.DspField29:str = obj["DspField29"]
      self.DspField30:str = obj["DspField30"]
      self.DspValue1:str = obj["DspValue1"]
      self.DspValue2:str = obj["DspValue2"]
      self.DspValue3:str = obj["DspValue3"]
      self.DspValue4:str = obj["DspValue4"]
      self.DspValue5:str = obj["DspValue5"]
      self.DspValue6:str = obj["DspValue6"]
      self.DspValue7:str = obj["DspValue7"]
      self.DspValue8:str = obj["DspValue8"]
      self.DspValue9:str = obj["DspValue9"]
      self.DspValue10:str = obj["DspValue10"]
      self.DspValue11:str = obj["DspValue11"]
      self.DspValue12:str = obj["DspValue12"]
      self.DspValue13:str = obj["DspValue13"]
      self.DspValue14:str = obj["DspValue14"]
      self.DspValue15:str = obj["DspValue15"]
      self.DspValue16:str = obj["DspValue16"]
      self.DspValue17:str = obj["DspValue17"]
      self.DspValue18:str = obj["DspValue18"]
      self.DspValue19:str = obj["DspValue19"]
      self.DspValue20:str = obj["DspValue20"]
      self.DspValue21:str = obj["DspValue21"]
      self.DspValue22:str = obj["DspValue22"]
      self.DspValue23:str = obj["DspValue23"]
      self.DspValue24:str = obj["DspValue24"]
      self.DspValue25:str = obj["DspValue25"]
      self.DspValue26:str = obj["DspValue26"]
      self.DspValue27:str = obj["DspValue27"]
      self.DspValue28:str = obj["DspValue28"]
      self.DspValue29:str = obj["DspValue29"]
      self.DspValue30:str = obj["DspValue30"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LookupTableListRow:
   def __init__(self, obj):
      self.MapUID:int = obj["MapUID"]
      """  Map unique ID.  """  
      self.DisplayName:str = obj["DisplayName"]
      """  Lookup table name wich should be displayed in a tree view controls.  """  
      self.LookupName:str = obj["LookupName"]
      """  Lookup table name.  """  
      self.DetailedDescription:str = obj["DetailedDescription"]
      """  Detailed description of the lookup table.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlobalLookupTable:bool = obj["GlobalLookupTable"]
      """  Marks this LookupTable as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LookupTableListTableset:
   def __init__(self, obj):
      self.LookupTableList:list[Erp_Tablesets_LookupTableListRow] = obj["LookupTableList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LookupTableRow:
   def __init__(self, obj):
      self.MapUID:int = obj["MapUID"]
      """  Map unique ID.  """  
      self.DisplayName:str = obj["DisplayName"]
      """  Lookup table name wich should be displayed in a tree view controls.  """  
      self.LookupName:str = obj["LookupName"]
      """  Lookup table name.  """  
      self.DetailedDescription:str = obj["DetailedDescription"]
      """  Detailed description of the lookup table.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlobalLookupTable:bool = obj["GlobalLookupTable"]
      """  Marks this LookupTable as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SourceValueFieldRow:
   def __init__(self, obj):
      self.SourceValueFieldUID:int = obj["SourceValueFieldUID"]
      """  Source value field unique ID.  """  
      self.MapUID:int = obj["MapUID"]
      """  Map unique ID.  """  
      self.SequenceNumber:int = obj["SequenceNumber"]
      """  Field sequence number.  """  
      self.FieldName:str = obj["FieldName"]
      """  Source field name.  """  
      self.DetailedDescription:str = obj["DetailedDescription"]
      """  Detailed description.  """  
      self.DBTable:str = obj["DBTable"]
      """  Database table which field linked to the source value field.  """  
      self.DBField:str = obj["DBField"]
      """  Field which linked to the source value field.  """  
      self.Validate:bool = obj["Validate"]
      """  Turns on the validation of the field.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlobalSourceValueField:bool = obj["GlobalSourceValueField"]
      """  Marks this SourceValueField as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DBSchemaName:str = obj["DBSchemaName"]
      """  DBSchemaName  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TargetValueFieldRow:
   def __init__(self, obj):
      self.TargetValueFieldUID:int = obj["TargetValueFieldUID"]
      """  Target value field unique ID.  """  
      self.MapUID:int = obj["MapUID"]
      """  Map unique ID.  """  
      self.SequenceNumber:int = obj["SequenceNumber"]
      """  Field sequence number.  """  
      self.FieldName:str = obj["FieldName"]
      """  Target field name.  """  
      self.DetailedDescription:str = obj["DetailedDescription"]
      """  Detailed description.  """  
      self.ValueType:str = obj["ValueType"]
      """  Value Type  """  
      self.COACode:str = obj["COACode"]
      """  Chart of accounts. Like COA.COACode.  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  Accounting segment from selected chart of accounts. Like COASegment.SegmentNbr.  """  
      self.Validate:bool = obj["Validate"]
      """  Turns on the validation of the field.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlobalTargetValueField:bool = obj["GlobalTargetValueField"]
      """  Marks this TargetValueField as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SegmentName:str = obj["SegmentName"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtLookupDataTableset:
   def __init__(self, obj):
      self.LookupTable:list[Erp_Tablesets_LookupTableRow] = obj["LookupTable"]
      self.LookupLink:list[Erp_Tablesets_LookupLinkRow] = obj["LookupLink"]
      self.SourceValueField:list[Erp_Tablesets_SourceValueFieldRow] = obj["SourceValueField"]
      self.TargetValueField:list[Erp_Tablesets_TargetValueFieldRow] = obj["TargetValueField"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExportToFile_input:
   """ Required : 
   mapUidList
   fileName
   format
   """  
   def __init__(self, obj):
      self.mapUidList:str = obj["mapUidList"]
      self.fileName:str = obj["fileName"]
      self.format:str = obj["format"]
      pass

class ExportToFile_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.errorMessage:str = obj["parameters"]
      self.exportedItemsNumber:int = obj["parameters"]
      self.serverFileName:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByDisplayName_input:
   """ Required : 
   displayName
   """  
   def __init__(self, obj):
      self.displayName:str = obj["displayName"]
      """  Display Name  """  
      pass

class GetByDisplayName_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LookupDataTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   mapUID
   """  
   def __init__(self, obj):
      self.mapUID:int = obj["mapUID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LookupDataTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_LookupDataTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_LookupDataTableset] = obj["returnObj"]
      pass

class GetCOASegmentVals_input:
   """ Required : 
   coaCode
   segNum
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      """  COA code  """  
      self.segNum:int = obj["segNum"]
      """  Segment number  """  
      pass

class GetCOASegmentVals_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.segValList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetCOASegments_input:
   """ Required : 
   coaCode
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      """  COA code  """  
      pass

class GetCOASegments_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.segList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetColumnDataType_input:
   """ Required : 
   schema
   table
   field
   """  
   def __init__(self, obj):
      self.schema:str = obj["schema"]
      """  Schema Name  """  
      self.table:str = obj["table"]
      """  Table Name  """  
      self.field:str = obj["field"]
      """  Field Name  """  
      pass

class GetColumnDataType_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Field Data Type  """  
      pass

class GetDBStructure_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DBStructureTableset] = obj["returnObj"]
      pass

class GetDynamicData_input:
   """ Required : 
   mapUID
   """  
   def __init__(self, obj):
      self.mapUID:int = obj["mapUID"]
      pass

class GetDynamicData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynamicMetadataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetFieldValueList2_input:
   """ Required : 
   schemaName
   tableName
   fieldName
   ds
   itemsList
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      self.ds:list[Erp_Tablesets_DBStructureTableset] = obj["ds"]
      self.itemsList:str = obj["itemsList"]
      pass

class GetFieldValueList2_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DBStructureTableset] = obj["ds"]
      self.itemsList:list = obj[any]
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
      self.returnObj:list[Erp_Tablesets_LookupTableListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewLookupLink_input:
   """ Required : 
   ds
   mapUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LookupDataTableset] = obj["ds"]
      self.mapUID:int = obj["mapUID"]
      pass

class GetNewLookupLink_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LookupDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLookupTable_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LookupDataTableset] = obj["ds"]
      pass

class GetNewLookupTable_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LookupDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSourceValueField_input:
   """ Required : 
   ds
   mapUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LookupDataTableset] = obj["ds"]
      self.mapUID:int = obj["mapUID"]
      pass

class GetNewSourceValueField_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LookupDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTargetValueField_input:
   """ Required : 
   ds
   mapUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LookupDataTableset] = obj["ds"]
      self.mapUID:int = obj["mapUID"]
      pass

class GetNewTargetValueField_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LookupDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseLookupTable
   whereClauseLookupLink
   whereClauseSourceValueField
   whereClauseTargetValueField
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseLookupTable:str = obj["whereClauseLookupTable"]
      self.whereClauseLookupLink:str = obj["whereClauseLookupLink"]
      self.whereClauseSourceValueField:str = obj["whereClauseSourceValueField"]
      self.whereClauseTargetValueField:str = obj["whereClauseTargetValueField"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LookupDataTableset] = obj["returnObj"]
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

class ImportFromFile_input:
   """ Required : 
   fileName
   """  
   def __init__(self, obj):
      self.fileName:str = obj["fileName"]
      pass

class ImportFromFile_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.mapUID:int = obj["parameters"]
      self.errorMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class LoadTableFields_input:
   """ Required : 
   schema
   table
   ds
   """  
   def __init__(self, obj):
      self.schema:str = obj["schema"]
      """  DB schema name  """  
      self.table:str = obj["table"]
      """  DB table name  """  
      self.ds:list[Erp_Tablesets_DBStructureTableset] = obj["ds"]
      pass

class LoadTableFields_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DBStructureTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PopulateLookupLink_input:
   """ Required : 
   mapUID
   columnName
   """  
   def __init__(self, obj):
      self.mapUID:int = obj["mapUID"]
      self.columnName:str = obj["columnName"]
      pass

class PopulateLookupLink_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LookupDataTableset] = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtLookupDataTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtLookupDataTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LookupDataTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LookupDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

