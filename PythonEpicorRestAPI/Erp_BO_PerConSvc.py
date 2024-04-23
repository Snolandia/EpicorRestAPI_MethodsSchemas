import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PerConSvc
# Description: Handles the Person Contact business object.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PerCons(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PerCons items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PerCons
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerConRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerCons",headers=creds) as resp:
           return await resp.json()

async def post_PerCons(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PerCons
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PerConRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PerConRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerCons", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PerCons_Company_PerConID(Company, PerConID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PerCon item
   Description: Calls GetByID to retrieve the PerCon item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PerCon
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerConID: Desc: PerConID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PerConRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerCons(" + Company + "," + PerConID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PerCons_Company_PerConID(Company, PerConID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PerCon for the service
   Description: Calls UpdateExt to update PerCon. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PerCon
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerConID: Desc: PerConID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PerConRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerCons(" + Company + "," + PerConID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PerCons_Company_PerConID(Company, PerConID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PerCon item
   Description: Call UpdateExt to delete PerCon item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PerCon
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerConID: Desc: PerConID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerCons(" + Company + "," + PerConID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PerCons_Company_PerConID_PerConLnks(Company, PerConID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PerConLnks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PerConLnks1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerConID: Desc: PerConID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerConLnkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerCons(" + Company + "," + PerConID + ")/PerConLnks",headers=creds) as resp:
           return await resp.json()

async def get_PerCons_Company_PerConID_PerConLnks_Company_PerConID_ContextLink_LinkSysRowID(Company, PerConID, ContextLink, LinkSysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PerConLnk item
   Description: Calls GetByID to retrieve the PerConLnk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PerConLnk1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerConID: Desc: PerConID   Required: True
      :param ContextLink: Desc: ContextLink   Required: True   Allow empty value : True
      :param LinkSysRowID: Desc: LinkSysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PerConLnkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerCons(" + Company + "," + PerConID + ")/PerConLnks(" + Company + "," + PerConID + "," + ContextLink + "," + LinkSysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PerCons_Company_PerConID_PerConAttches(Company, PerConID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PerConAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PerConAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerConID: Desc: PerConID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerConAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerCons(" + Company + "," + PerConID + ")/PerConAttches",headers=creds) as resp:
           return await resp.json()

async def get_PerCons_Company_PerConID_PerConAttches_Company_PerConID_DrawingSeq(Company, PerConID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PerConAttch item
   Description: Calls GetByID to retrieve the PerConAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PerConAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerConID: Desc: PerConID   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PerConAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerCons(" + Company + "," + PerConID + ")/PerConAttches(" + Company + "," + PerConID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PerConLnks(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PerConLnks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PerConLnks
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerConLnkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerConLnks",headers=creds) as resp:
           return await resp.json()

async def post_PerConLnks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PerConLnks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PerConLnkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PerConLnkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerConLnks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PerConLnks_Company_PerConID_ContextLink_LinkSysRowID(Company, PerConID, ContextLink, LinkSysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PerConLnk item
   Description: Calls GetByID to retrieve the PerConLnk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PerConLnk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerConID: Desc: PerConID   Required: True
      :param ContextLink: Desc: ContextLink   Required: True   Allow empty value : True
      :param LinkSysRowID: Desc: LinkSysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PerConLnkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerConLnks(" + Company + "," + PerConID + "," + ContextLink + "," + LinkSysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PerConLnks_Company_PerConID_ContextLink_LinkSysRowID(Company, PerConID, ContextLink, LinkSysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PerConLnk for the service
   Description: Calls UpdateExt to update PerConLnk. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PerConLnk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerConID: Desc: PerConID   Required: True
      :param ContextLink: Desc: ContextLink   Required: True   Allow empty value : True
      :param LinkSysRowID: Desc: LinkSysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PerConLnkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerConLnks(" + Company + "," + PerConID + "," + ContextLink + "," + LinkSysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PerConLnks_Company_PerConID_ContextLink_LinkSysRowID(Company, PerConID, ContextLink, LinkSysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PerConLnk item
   Description: Call UpdateExt to delete PerConLnk item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PerConLnk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerConID: Desc: PerConID   Required: True
      :param ContextLink: Desc: ContextLink   Required: True   Allow empty value : True
      :param LinkSysRowID: Desc: LinkSysRowID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerConLnks(" + Company + "," + PerConID + "," + ContextLink + "," + LinkSysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PerConAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PerConAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PerConAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerConAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerConAttches",headers=creds) as resp:
           return await resp.json()

async def post_PerConAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PerConAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PerConAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PerConAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerConAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PerConAttches_Company_PerConID_DrawingSeq(Company, PerConID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PerConAttch item
   Description: Calls GetByID to retrieve the PerConAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PerConAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerConID: Desc: PerConID   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PerConAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerConAttches(" + Company + "," + PerConID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PerConAttches_Company_PerConID_DrawingSeq(Company, PerConID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PerConAttch for the service
   Description: Calls UpdateExt to update PerConAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PerConAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerConID: Desc: PerConID   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PerConAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerConAttches(" + Company + "," + PerConID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PerConAttches_Company_PerConID_DrawingSeq(Company, PerConID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PerConAttch item
   Description: Call UpdateExt to delete PerConAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PerConAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PerConID: Desc: PerConID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerConAttches(" + Company + "," + PerConID + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerConListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePerCon, whereClausePerConAttch, whereClausePerConLnk, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePerCon=" + whereClausePerCon
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePerConAttch=" + whereClausePerConAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePerConLnk=" + whereClausePerConLnk
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(perConID, epicorHeaders = None):
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
   params += "perConID=" + perConID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetClientFileName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetClientFileName
   OperationID: GetClientFileName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetClientFileName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetClientFileName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPerConGlobalFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPerConGlobalFields
   OperationID: GetPerConGlobalFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPerConGlobalFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPerConGlobalFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeGlobalPerCon(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeGlobalPerCon
   Description: Method to call when changing the GlobalPerCon on a PerCon.
   OperationID: ChangeGlobalPerCon
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeGlobalPerCon_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGlobalPerCon_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePerConLnk(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePerConLnk
   OperationID: ChangePerConLnk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePerConLnk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePerConLnk_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDupPerCon(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDupPerCon
   Description: This method checks the Name, FirstName and LastName fields to see if there
are any duplicate contacts. A ListDataSet will be returned to the user
of any duplicates asking if the user wants to continue. Needs to be run
before Update on a NEW record only.
   OperationID: CheckDupPerCon
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDupPerCon_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDupPerCon_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultName
   Description: This method populates the detail fields from PerCon.Name when targetName = "Detail".
When targetField = "Name", then the PerCon.Name is built from the detail fields.
   OperationID: DefaultName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGlbPerConList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGlbPerConList
   Description: This method returns the GlbPerCon dataset based on a delimited list of GlbPerConID values passed in.
   OperationID: GetGlbPerConList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGlbPerConList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGlbPerConList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPerConForLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPerConForLink
   Description: This returns the PerCon dataset for linking.
   OperationID: GetPerConForLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPerConForLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPerConForLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LinkGlbPerCon(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LinkGlbPerCon
   Description: This method performs the actual logic behind linking a PerCon. It is run after
the PreLinkGlbPerCon method which determines the PerConID to link to.
If the PerConID is for a PerCon that already exists, the GlbPerCon information is
translated and then copied to the PerConDataSet as an update.
If the PerConID is for a new PerCon, the GlbPerCon information is translated and then
copied to the PerConDataSet as an Add. Until the update method is run on PerCon record
the Link process is not completed.
   OperationID: LinkGlbPerCon
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LinkGlbPerCon_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LinkGlbPerCon_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreLinkGlbPerCon(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreLinkGlbPerCon
   Description: Linking a GlbPerCon record ties a global record to a new or existing PerCon record so
that any changes made to the GlbPerCon record in another company are automatically copied
to any linked PerCon's.
This method performs the pre link logic to check of okay to link or get the new PerConID
to create/link to. Will be run before LinkGlbPerCon which actually creates/updates a
PerCon record and will send the modified record back for update.  When the Link "button" is
originally selected, the LinkPerConID will be defaulted to the GlbPerConID field.  It will then
check to see if this PerConID is available for use. If available for use the system will return a
question asking the user if they want to use this number.  If the answer is no, then the user
either needs to select an existing PerConID to link to or enter a brand new number.  You will
run this method until the user answer is yes. Then the LinkGlbPerCon method is called.
   OperationID: PreLinkGlbPerCon
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreLinkGlbPerCon_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreLinkGlbPerCon_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SkipGlbPerCon(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SkipGlbPerCon
   Description: This method performs the logic behind the skip option for GlbPerCon
Skip - sets the Skipped flag to true.
If the PerConID field is not 0 will error out
   OperationID: SkipGlbPerCon
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SkipGlbPerCon_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SkipGlbPerCon_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnlinkGlbPerCon(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnlinkGlbPerCon
   Description: This method performs the logic behind the unlink option for GlbPerCon
Unlink - clears the PerConID field in GlbPerCon.  Returns the PerCon DataSet
   OperationID: UnlinkGlbPerCon
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlinkGlbPerCon_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlinkGlbPerCon_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsPayrollManager(epicorHeaders = None):
   """  
   Summary: Invoke method IsPayrollManager
   OperationID: IsPayrollManager
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsPayrollManager_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewPerCon(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPerCon
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPerCon
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPerCon_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPerCon_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPerConAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPerConAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPerConAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPerConAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPerConAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPerConLnk(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPerConLnk
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPerConLnk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPerConLnk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPerConLnk_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PerConAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PerConListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConLnkRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PerConLnkRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PerConRow] = obj["value"]
      pass

class Erp_Tablesets_PerConAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PerConID:int = obj["PerConID"]
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

class Erp_Tablesets_PerConListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.Name:str = obj["Name"]
      """  Full name of the contact.  """  
      self.FirstName:str = obj["FirstName"]
      """  Contact's first name.  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Contact's middle name.  """  
      self.LastName:str = obj["LastName"]
      """  Contact's last name.  """  
      self.PRName:str = obj["PRName"]
      """  Name used by Payroll - defaults to FullName - link this field to the name field in Empbasic and in the future to PREmpMas.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The contact's email address.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contact's cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contact's pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contact's home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contact's alternate phone number.  """  
      self.Prefix:str = obj["Prefix"]
      """  Contact's prefix.  """  
      self.Suffix:str = obj["Suffix"]
      """  Contact's suffix.  """  
      self.Initials:str = obj["Initials"]
      """  Contact's initials.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.Address1:str = obj["Address1"]
      """  Address line 1  """  
      self.Address2:str = obj["Address2"]
      """  Address line 2  """  
      self.Address3:str = obj["Address3"]
      """  Address line 3  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value related to the SalesRep.Country value.  """  
      self.CorpName:str = obj["CorpName"]
      """  The company name of the contact's mailing address. (See Address1 for additional information).  """  
      self.RoleCode:str = obj["RoleCode"]
      """  RoleCD.RoleCode value of the role assigned to the contact.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  Contact's title.  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name of the person this contact reports to.  """  
      self.PRLastName:str = obj["PRLastName"]
      """  Contact's payroll last name.  """  
      self.PRFirstName:str = obj["PRFirstName"]
      """  Contact's payroll first name.  """  
      self.PRMiddleName:str = obj["PRMiddleName"]
      """  Contact's payroll middle name.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  The System User ID.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  """  
      self.GlobalPerCon:bool = obj["GlobalPerCon"]
      """  Marks the PerCon as a global PerCon, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CrtPREmpLnk:bool = obj["CrtPREmpLnk"]
      """  Logical column used for Create Selected Links action menu. Indicates that a PR Employee link should be created if it doesn't exist already.  """  
      self.CrtEmpLnk:bool = obj["CrtEmpLnk"]
      """  Logical column used for Create Selected Links action menu. Indicates that an Employee link should be created if it doesn't exist already.  """  
      self.CrtBuyerLnk:bool = obj["CrtBuyerLnk"]
      """  Logical column used for Create Selected Links action menu. Indicates that a Buyer link should be created if it doesn't exist already.  """  
      self.CrtWFLnk:bool = obj["CrtWFLnk"]
      """  Logical column used for Create Selected Links action menu. Indicates that a Work Force link should be created if it doesn't exist already.  """  
      self.PhotoFilePath:str = obj["PhotoFilePath"]
      """  Path to the photo file if it exists.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the PerCon is Global (master or linked)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany and GlbPerConID that is linking to this PerCon.  """  
      self.EnableGlbLock:bool = obj["EnableGlbLock"]
      self.EnableGlbPerCon:bool = obj["EnableGlbPerCon"]
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      """  A description of the role.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PerConLnkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.ContextLink:str = obj["ContextLink"]
      """   The table name and context that this PerConLnk is related to:
Customer(If related to CustCnt and CustCnt.ShipTonum = "")
Ship to(If related to CustCnt and CustCnt.ShipTonum <> "")
Supplier((If related to VendCnt and VendCnt.PurPoint = "")
Supplier PP((If related to VendCnt and VendCnt.PurPoint <> "")
Employee(If related to EmpBasic)
Work force (If related to SalesRep)
Buyer(If related to PurAgent)  """  
      self.LinkSysRowID:str = obj["LinkSysRowID"]
      """  The SysRowId of the linked table.  """  
      self.PrimaryContext:bool = obj["PrimaryContext"]
      """  Flag that indicates the primary link of the Person/Contact.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The contact's email address.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contact's cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contact's pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contact's home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contact's alternate phone number.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.Address1:str = obj["Address1"]
      """  Address line 1  """  
      self.Address2:str = obj["Address2"]
      """  Address line 2  """  
      self.Address3:str = obj["Address3"]
      """  Address line 3  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value related to the SalesRep.Country value.  """  
      self.CorpName:str = obj["CorpName"]
      """  The company name of the contact's mailing address. (See Address1 for additional information).  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID from Customer table.  """  
      self.CustName:str = obj["CustName"]
      """  Full name of the customer.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Number of the Ship To for the Customer Contact.  """  
      self.ShipToName:str = obj["ShipToName"]
      """  Name of the customer contact's Ship To.  """  
      self.CustContactName:str = obj["CustContactName"]
      """  Name of the Customer Contact.  """  
      self.VendorID:str = obj["VendorID"]
      """  Vendor ID from the Vendor table.  """  
      self.VendorName:str = obj["VendorName"]
      """  Name of the vendor.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point from the Vendor.  """  
      self.PurPointName:str = obj["PurPointName"]
      """  Name of the vendor's purchase point.  """  
      self.VendorContactName:str = obj["VendorContactName"]
      """  Name of the vendor's contact.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The code of the sales representative, from the SalesRep table.  """  
      self.SalesRepName:str = obj["SalesRepName"]
      """  Name of the sales representative.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  Buyer ID from the PurAgent table.  """  
      self.BuyerName:str = obj["BuyerName"]
      """  Name of the buyer.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID from the EmpBasic table.  """  
      self.EmpName:str = obj["EmpName"]
      """  Name of the employee.  """  
      self.PREmpID:str = obj["PREmpID"]
      self.PREmpName:str = obj["PREmpName"]
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Shows the value of the Sync. Name flag in the linked record.  """  
      self.SyncAddressToPerCon:bool = obj["SyncAddressToPerCon"]
      """  Shows the value of the Sync. Address flag in the linked record.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Shows the value of the Sync. Phone flag in the linked record.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Shows the value of the Sync. Email flag in the linked record.  """  
      self.SyncLinksToPerCon:bool = obj["SyncLinksToPerCon"]
      """  Shows the value of the Sync. Links flag in the linked record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PerConRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.Name:str = obj["Name"]
      """  Full name of the contact.  """  
      self.FirstName:str = obj["FirstName"]
      """  Contact's first name.  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Contact's middle name.  """  
      self.LastName:str = obj["LastName"]
      """  Contact's last name.  """  
      self.PRName:str = obj["PRName"]
      """  Name used by Payroll - defaults to FullName - link this field to the name field in Empbasic and in the future to PREmpMas.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The contact's email address.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contact's cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contact's pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contact's home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contact's alternate phone number.  """  
      self.Prefix:str = obj["Prefix"]
      """  Contact's prefix.  """  
      self.Suffix:str = obj["Suffix"]
      """  Contact's suffix.  """  
      self.Initials:str = obj["Initials"]
      """  Contact's initials.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.Address1:str = obj["Address1"]
      """  Address line 1  """  
      self.Address2:str = obj["Address2"]
      """  Address line 2  """  
      self.Address3:str = obj["Address3"]
      """  Address line 3  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value related to the SalesRep.Country value.  """  
      self.CorpName:str = obj["CorpName"]
      """  The company name of the contact's mailing address. (See Address1 for additional information).  """  
      self.RoleCode:str = obj["RoleCode"]
      """  RoleCD.RoleCode value of the role assigned to the contact.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  Contact's title.  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name of the person this contact reports to.  """  
      self.PRLastName:str = obj["PRLastName"]
      """  Contact's payroll last name.  """  
      self.PRFirstName:str = obj["PRFirstName"]
      """  Contact's payroll first name.  """  
      self.PRMiddleName:str = obj["PRMiddleName"]
      """  Contact's payroll middle name.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  The System User ID.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  """  
      self.GlobalPerCon:bool = obj["GlobalPerCon"]
      """  Marks the PerCon as a global PerCon, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.HCMLinked:bool = obj["HCMLinked"]
      """  Indicates if the record is linked from HCM  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IssuerPrsnIDCode:str = obj["IssuerPrsnIDCode"]
      """  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  """  
      self.IssuerIDType:str = obj["IssuerIDType"]
      """  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  """  
      self.IssuerName:str = obj["IssuerName"]
      """  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  """  
      self.IssuerSurname:str = obj["IssuerSurname"]
      """  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  """  
      self.IssuerSerialNum:str = obj["IssuerSerialNum"]
      """  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  """  
      self.IssuerIDIssDate:str = obj["IssuerIDIssDate"]
      """  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.CrtBuyerLnk:bool = obj["CrtBuyerLnk"]
      """  Logical column used for Create Selected Links action menu. Indicates that a Buyer link should be created if it doesn't exist already.  """  
      self.CrtEmpLnk:bool = obj["CrtEmpLnk"]
      """  Logical column used for Create Selected Links action menu. Indicates that an Employee link should be created if it doesn't exist already.  """  
      self.CrtPREmpLnk:bool = obj["CrtPREmpLnk"]
      """  Logical column used for Create Selected Links action menu. Indicates that a PR Employee link should be created if it doesn't exist already.  """  
      self.CrtWFLnk:bool = obj["CrtWFLnk"]
      """  Logical column used for Create Selected Links action menu. Indicates that a Work Force link should be created if it doesn't exist already.  """  
      self.EnableGlbLock:bool = obj["EnableGlbLock"]
      self.EnableGlbPerCon:bool = obj["EnableGlbPerCon"]
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the PerCon is Global (master or linked)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany and GlbPerConID that is linking to this PerCon.  """  
      self.PhotoFilePath:str = obj["PhotoFilePath"]
      """  Path to the photo file if it exists.  """  
      self.EnableCreateBuyer:bool = obj["EnableCreateBuyer"]
      self.EnableCreateEmployee:bool = obj["EnableCreateEmployee"]
      self.EnableCreatePREmployee:bool = obj["EnableCreatePREmployee"]
      self.EnableCreateWorkForce:bool = obj["EnableCreateWorkForce"]
      self.BitFlag:int = obj["BitFlag"]
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeGlobalPerCon_input:
   """ Required : 
   ipGlobalPerCon
   ds
   """  
   def __init__(self, obj):
      self.ipGlobalPerCon:bool = obj["ipGlobalPerCon"]
      """  The proposed GlobalPerCon value.  """  
      self.ds:list[Erp_Tablesets_PerConTableset] = obj["ds"]
      pass

class ChangeGlobalPerCon_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PerConTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePerConLnk_input:
   """ Required : 
   ipNewPerConID
   ipPerConID
   ipContextLink
   ipLinkSysRowID
   ds
   """  
   def __init__(self, obj):
      self.ipNewPerConID:int = obj["ipNewPerConID"]
      """  New PerConID.  """  
      self.ipPerConID:int = obj["ipPerConID"]
      """  Current PerConID.  """  
      self.ipContextLink:str = obj["ipContextLink"]
      """  ContextLink.  """  
      self.ipLinkSysRowID:str = obj["ipLinkSysRowID"]
      """  LinkSysRowID.  """  
      self.ds:list[Erp_Tablesets_PerConTableset] = obj["ds"]
      pass

class ChangePerConLnk_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PerConTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckDupPerCon_input:
   """ Required : 
   vName
   vEmail
   vPhone
   vSysRowID
   """  
   def __init__(self, obj):
      self.vName:str = obj["vName"]
      """  The name of the contact.  """  
      self.vEmail:str = obj["vEmail"]
      self.vPhone:str = obj["vPhone"]
      self.vSysRowID:str = obj["vSysRowID"]
      """  SysRowID field of the PerCon record.  """  
      pass

class CheckDupPerCon_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PerConListTableset] = obj["returnObj"]
      pass

class DefaultName_input:
   """ Required : 
   targetField
   perConID
   ds
   """  
   def __init__(self, obj):
      self.targetField:str = obj["targetField"]
      """  Indicates which fields to populate either "Detail" or "Name"  """  
      self.perConID:int = obj["perConID"]
      """  PerCon.PerConID  """  
      self.ds:list[Erp_Tablesets_PerConTableset] = obj["ds"]
      pass

class DefaultName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PerConTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   perConID
   """  
   def __init__(self, obj):
      self.perConID:int = obj["perConID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GlbPerConRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.Name:str = obj["Name"]
      """  Full name of the contact.  """  
      self.FirstName:str = obj["FirstName"]
      """  Contact's first name.  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Contact's middle name.  """  
      self.LastName:str = obj["LastName"]
      """  Contact's last name.  """  
      self.PRName:str = obj["PRName"]
      """  Name used by Payroll - defaults to FullName - link this field to the name field in Empbasic and in the future to PREmpMas.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The contact's email address.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contact's cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contact's pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contact's home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contact's alternate phone number.  """  
      self.Prefix:str = obj["Prefix"]
      """  Contact's prefix.  """  
      self.Suffix:str = obj["Suffix"]
      """  Contact's suffix.  """  
      self.Initials:str = obj["Initials"]
      """  Contact's initials.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.Address1:str = obj["Address1"]
      """  Address line 1  """  
      self.Address2:str = obj["Address2"]
      """  Address line 2  """  
      self.Address3:str = obj["Address3"]
      """  Address line 3  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value related to the SalesRep.Country value.  """  
      self.CorpName:str = obj["CorpName"]
      """  The company name of the contact's mailing address. (See Address1 for additional information).  """  
      self.RoleCode:str = obj["RoleCode"]
      """  RoleCD.RoleCode value of the role assigned to the contact.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  Contact's title.  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name of the person this contact reports to.  """  
      self.PRLastName:str = obj["PRLastName"]
      """  Contact's payroll last name.  """  
      self.PRFirstName:str = obj["PRFirstName"]
      """  Contact's payroll first name.  """  
      self.PRMiddleName:str = obj["PRMiddleName"]
      """  Contact's payroll middle name.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  The System User ID.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Owner Company Identifier.  """  
      self.GlbPerConID:int = obj["GlbPerConID"]
      """  The Owner's PerConID field identifies the PerCon and is used as the primary key.  """  
      self.OldCompany:str = obj["OldCompany"]
      """  Original Owner Company Identifier. - NOT CURRENTLY IN USE  """  
      self.OldPerConID:int = obj["OldPerConID"]
      """  The Original Owner's PerConID field identifies the PerCon and is used as the primary key.   NOT CURRENTLY IN USE  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates if the user chose to skip this record when linking global PerCon's.  The user can come back at a later time and choose to link a skipped PerCon if they need to.  """  
      self.GlobalPerCon:bool = obj["GlobalPerCon"]
      """  Marks the PerCon as a global PerCon, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.GlbName:str = obj["GlbName"]
      """  Full name of the contact. A descriptive Name assigned by the parent company user to uniquely identify the PerCon record.  """  
      self.HCMLinked:bool = obj["HCMLinked"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the PerCon is Global (master or linked)  """  
      self.LinkName:str = obj["LinkName"]
      self.LinkPerConID:int = obj["LinkPerConID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbPerConTableset:
   def __init__(self, obj):
      self.GlbPerCon:list[Erp_Tablesets_GlbPerConRow] = obj["GlbPerCon"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PerConAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PerConID:int = obj["PerConID"]
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

class Erp_Tablesets_PerConListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.Name:str = obj["Name"]
      """  Full name of the contact.  """  
      self.FirstName:str = obj["FirstName"]
      """  Contact's first name.  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Contact's middle name.  """  
      self.LastName:str = obj["LastName"]
      """  Contact's last name.  """  
      self.PRName:str = obj["PRName"]
      """  Name used by Payroll - defaults to FullName - link this field to the name field in Empbasic and in the future to PREmpMas.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The contact's email address.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contact's cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contact's pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contact's home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contact's alternate phone number.  """  
      self.Prefix:str = obj["Prefix"]
      """  Contact's prefix.  """  
      self.Suffix:str = obj["Suffix"]
      """  Contact's suffix.  """  
      self.Initials:str = obj["Initials"]
      """  Contact's initials.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.Address1:str = obj["Address1"]
      """  Address line 1  """  
      self.Address2:str = obj["Address2"]
      """  Address line 2  """  
      self.Address3:str = obj["Address3"]
      """  Address line 3  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value related to the SalesRep.Country value.  """  
      self.CorpName:str = obj["CorpName"]
      """  The company name of the contact's mailing address. (See Address1 for additional information).  """  
      self.RoleCode:str = obj["RoleCode"]
      """  RoleCD.RoleCode value of the role assigned to the contact.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  Contact's title.  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name of the person this contact reports to.  """  
      self.PRLastName:str = obj["PRLastName"]
      """  Contact's payroll last name.  """  
      self.PRFirstName:str = obj["PRFirstName"]
      """  Contact's payroll first name.  """  
      self.PRMiddleName:str = obj["PRMiddleName"]
      """  Contact's payroll middle name.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  The System User ID.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  """  
      self.GlobalPerCon:bool = obj["GlobalPerCon"]
      """  Marks the PerCon as a global PerCon, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CrtPREmpLnk:bool = obj["CrtPREmpLnk"]
      """  Logical column used for Create Selected Links action menu. Indicates that a PR Employee link should be created if it doesn't exist already.  """  
      self.CrtEmpLnk:bool = obj["CrtEmpLnk"]
      """  Logical column used for Create Selected Links action menu. Indicates that an Employee link should be created if it doesn't exist already.  """  
      self.CrtBuyerLnk:bool = obj["CrtBuyerLnk"]
      """  Logical column used for Create Selected Links action menu. Indicates that a Buyer link should be created if it doesn't exist already.  """  
      self.CrtWFLnk:bool = obj["CrtWFLnk"]
      """  Logical column used for Create Selected Links action menu. Indicates that a Work Force link should be created if it doesn't exist already.  """  
      self.PhotoFilePath:str = obj["PhotoFilePath"]
      """  Path to the photo file if it exists.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the PerCon is Global (master or linked)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany and GlbPerConID that is linking to this PerCon.  """  
      self.EnableGlbLock:bool = obj["EnableGlbLock"]
      self.EnableGlbPerCon:bool = obj["EnableGlbPerCon"]
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      """  A description of the role.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PerConListTableset:
   def __init__(self, obj):
      self.PerConList:list[Erp_Tablesets_PerConListRow] = obj["PerConList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PerConLnkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.ContextLink:str = obj["ContextLink"]
      """   The table name and context that this PerConLnk is related to:
Customer(If related to CustCnt and CustCnt.ShipTonum = "")
Ship to(If related to CustCnt and CustCnt.ShipTonum <> "")
Supplier((If related to VendCnt and VendCnt.PurPoint = "")
Supplier PP((If related to VendCnt and VendCnt.PurPoint <> "")
Employee(If related to EmpBasic)
Work force (If related to SalesRep)
Buyer(If related to PurAgent)  """  
      self.LinkSysRowID:str = obj["LinkSysRowID"]
      """  The SysRowId of the linked table.  """  
      self.PrimaryContext:bool = obj["PrimaryContext"]
      """  Flag that indicates the primary link of the Person/Contact.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The contact's email address.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contact's cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contact's pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contact's home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contact's alternate phone number.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.Address1:str = obj["Address1"]
      """  Address line 1  """  
      self.Address2:str = obj["Address2"]
      """  Address line 2  """  
      self.Address3:str = obj["Address3"]
      """  Address line 3  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value related to the SalesRep.Country value.  """  
      self.CorpName:str = obj["CorpName"]
      """  The company name of the contact's mailing address. (See Address1 for additional information).  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID from Customer table.  """  
      self.CustName:str = obj["CustName"]
      """  Full name of the customer.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Number of the Ship To for the Customer Contact.  """  
      self.ShipToName:str = obj["ShipToName"]
      """  Name of the customer contact's Ship To.  """  
      self.CustContactName:str = obj["CustContactName"]
      """  Name of the Customer Contact.  """  
      self.VendorID:str = obj["VendorID"]
      """  Vendor ID from the Vendor table.  """  
      self.VendorName:str = obj["VendorName"]
      """  Name of the vendor.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point from the Vendor.  """  
      self.PurPointName:str = obj["PurPointName"]
      """  Name of the vendor's purchase point.  """  
      self.VendorContactName:str = obj["VendorContactName"]
      """  Name of the vendor's contact.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The code of the sales representative, from the SalesRep table.  """  
      self.SalesRepName:str = obj["SalesRepName"]
      """  Name of the sales representative.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  Buyer ID from the PurAgent table.  """  
      self.BuyerName:str = obj["BuyerName"]
      """  Name of the buyer.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID from the EmpBasic table.  """  
      self.EmpName:str = obj["EmpName"]
      """  Name of the employee.  """  
      self.PREmpID:str = obj["PREmpID"]
      self.PREmpName:str = obj["PREmpName"]
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Shows the value of the Sync. Name flag in the linked record.  """  
      self.SyncAddressToPerCon:bool = obj["SyncAddressToPerCon"]
      """  Shows the value of the Sync. Address flag in the linked record.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Shows the value of the Sync. Phone flag in the linked record.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Shows the value of the Sync. Email flag in the linked record.  """  
      self.SyncLinksToPerCon:bool = obj["SyncLinksToPerCon"]
      """  Shows the value of the Sync. Links flag in the linked record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PerConRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.Name:str = obj["Name"]
      """  Full name of the contact.  """  
      self.FirstName:str = obj["FirstName"]
      """  Contact's first name.  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Contact's middle name.  """  
      self.LastName:str = obj["LastName"]
      """  Contact's last name.  """  
      self.PRName:str = obj["PRName"]
      """  Name used by Payroll - defaults to FullName - link this field to the name field in Empbasic and in the future to PREmpMas.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The contact's email address.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contact's cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contact's pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contact's home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contact's alternate phone number.  """  
      self.Prefix:str = obj["Prefix"]
      """  Contact's prefix.  """  
      self.Suffix:str = obj["Suffix"]
      """  Contact's suffix.  """  
      self.Initials:str = obj["Initials"]
      """  Contact's initials.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.Address1:str = obj["Address1"]
      """  Address line 1  """  
      self.Address2:str = obj["Address2"]
      """  Address line 2  """  
      self.Address3:str = obj["Address3"]
      """  Address line 3  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value related to the SalesRep.Country value.  """  
      self.CorpName:str = obj["CorpName"]
      """  The company name of the contact's mailing address. (See Address1 for additional information).  """  
      self.RoleCode:str = obj["RoleCode"]
      """  RoleCD.RoleCode value of the role assigned to the contact.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  Contact's title.  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name of the person this contact reports to.  """  
      self.PRLastName:str = obj["PRLastName"]
      """  Contact's payroll last name.  """  
      self.PRFirstName:str = obj["PRFirstName"]
      """  Contact's payroll first name.  """  
      self.PRMiddleName:str = obj["PRMiddleName"]
      """  Contact's payroll middle name.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  The System User ID.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  """  
      self.GlobalPerCon:bool = obj["GlobalPerCon"]
      """  Marks the PerCon as a global PerCon, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.HCMLinked:bool = obj["HCMLinked"]
      """  Indicates if the record is linked from HCM  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IssuerPrsnIDCode:str = obj["IssuerPrsnIDCode"]
      """  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  """  
      self.IssuerIDType:str = obj["IssuerIDType"]
      """  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  """  
      self.IssuerName:str = obj["IssuerName"]
      """  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  """  
      self.IssuerSurname:str = obj["IssuerSurname"]
      """  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  """  
      self.IssuerSerialNum:str = obj["IssuerSerialNum"]
      """  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  """  
      self.IssuerIDIssDate:str = obj["IssuerIDIssDate"]
      """  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.CrtBuyerLnk:bool = obj["CrtBuyerLnk"]
      """  Logical column used for Create Selected Links action menu. Indicates that a Buyer link should be created if it doesn't exist already.  """  
      self.CrtEmpLnk:bool = obj["CrtEmpLnk"]
      """  Logical column used for Create Selected Links action menu. Indicates that an Employee link should be created if it doesn't exist already.  """  
      self.CrtPREmpLnk:bool = obj["CrtPREmpLnk"]
      """  Logical column used for Create Selected Links action menu. Indicates that a PR Employee link should be created if it doesn't exist already.  """  
      self.CrtWFLnk:bool = obj["CrtWFLnk"]
      """  Logical column used for Create Selected Links action menu. Indicates that a Work Force link should be created if it doesn't exist already.  """  
      self.EnableGlbLock:bool = obj["EnableGlbLock"]
      self.EnableGlbPerCon:bool = obj["EnableGlbPerCon"]
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the PerCon is Global (master or linked)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany and GlbPerConID that is linking to this PerCon.  """  
      self.PhotoFilePath:str = obj["PhotoFilePath"]
      """  Path to the photo file if it exists.  """  
      self.EnableCreateBuyer:bool = obj["EnableCreateBuyer"]
      self.EnableCreateEmployee:bool = obj["EnableCreateEmployee"]
      self.EnableCreatePREmployee:bool = obj["EnableCreatePREmployee"]
      self.EnableCreateWorkForce:bool = obj["EnableCreateWorkForce"]
      self.BitFlag:int = obj["BitFlag"]
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PerConTableset:
   def __init__(self, obj):
      self.PerCon:list[Erp_Tablesets_PerConRow] = obj["PerCon"]
      self.PerConAttch:list[Erp_Tablesets_PerConAttchRow] = obj["PerConAttch"]
      self.PerConLnk:list[Erp_Tablesets_PerConLnkRow] = obj["PerConLnk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPerConTableset:
   def __init__(self, obj):
      self.PerCon:list[Erp_Tablesets_PerConRow] = obj["PerCon"]
      self.PerConAttch:list[Erp_Tablesets_PerConAttchRow] = obj["PerConAttch"]
      self.PerConLnk:list[Erp_Tablesets_PerConLnkRow] = obj["PerConLnk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   perConID
   """  
   def __init__(self, obj):
      self.perConID:int = obj["perConID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PerConTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PerConTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PerConTableset] = obj["returnObj"]
      pass

class GetClientFileName_input:
   """ Required : 
   IP_ServerFileName
   """  
   def __init__(self, obj):
      self.IP_ServerFileName:str = obj["IP_ServerFileName"]
      pass

class GetClientFileName_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetGlbPerConList_input:
   """ Required : 
   glbPerConIDList
   """  
   def __init__(self, obj):
      self.glbPerConIDList:str = obj["glbPerConIDList"]
      """  Delimited list of GlbPerConID values  """  
      pass

class GetGlbPerConList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GlbPerConTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PerConListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPerConAttch_input:
   """ Required : 
   ds
   perConID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PerConTableset] = obj["ds"]
      self.perConID:int = obj["perConID"]
      pass

class GetNewPerConAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PerConTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPerConLnk_input:
   """ Required : 
   ds
   perConID
   contextLink
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PerConTableset] = obj["ds"]
      self.perConID:int = obj["perConID"]
      self.contextLink:str = obj["contextLink"]
      pass

class GetNewPerConLnk_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PerConTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPerCon_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PerConTableset] = obj["ds"]
      pass

class GetNewPerCon_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PerConTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPerConForLink_input:
   """ Required : 
   ipPerConID
   """  
   def __init__(self, obj):
      self.ipPerConID:int = obj["ipPerConID"]
      """  Global PerConID field on the GlbPerCon record to link  """  
      pass

class GetPerConForLink_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PerConTableset] = obj["returnObj"]
      pass

class GetPerConGlobalFields_input:
   """ Required : 
   PerConID
   GlobalLock
   """  
   def __init__(self, obj):
      self.PerConID:int = obj["PerConID"]
      self.GlobalLock:bool = obj["GlobalLock"]
      pass

class GetPerConGlobalFields_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClausePerCon
   whereClausePerConAttch
   whereClausePerConLnk
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePerCon:str = obj["whereClausePerCon"]
      self.whereClausePerConAttch:str = obj["whereClausePerConAttch"]
      self.whereClausePerConLnk:str = obj["whereClausePerConLnk"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PerConTableset] = obj["returnObj"]
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

class IsPayrollManager_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class LinkGlbPerCon_input:
   """ Required : 
   glbCompany
   glbPerConID
   GlbPerConDS
   ds1
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company field on the GlbPerCon record to link  """  
      self.glbPerConID:int = obj["glbPerConID"]
      """  Global PerConID field on the GlbPerCon record to link  """  
      self.GlbPerConDS:list[Erp_Tablesets_GlbPerConTableset] = obj["GlbPerConDS"]
      self.ds1:list[Erp_Tablesets_PerConTableset] = obj["ds1"]
      pass

class LinkGlbPerCon_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds1:list[Erp_Tablesets_PerConTableset] = obj["ds1"]
      pass

      """  output parameters  """  

class PreLinkGlbPerCon_input:
   """ Required : 
   glbCompany
   glbPerConID
   checkDuplicate
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company field on the GlbPerCon record to link  """  
      self.glbPerConID:int = obj["glbPerConID"]
      """  Global PerConID field on the GlbPerCon record to link  """  
      self.checkDuplicate:bool = obj["checkDuplicate"]
      """  checkDuplicate  """  
      self.ds:list[Erp_Tablesets_GlbPerConTableset] = obj["ds"]
      pass

class PreLinkGlbPerCon_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PerConListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbPerConTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class SkipGlbPerCon_input:
   """ Required : 
   glbCompany
   glbPerConID
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company field on the GlbPerCon record to skip  """  
      self.glbPerConID:int = obj["glbPerConID"]
      """  Global PerConID field on the GlbPerCon record to skip  """  
      self.ds:list[Erp_Tablesets_GlbPerConTableset] = obj["ds"]
      pass

class SkipGlbPerCon_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbPerConTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UnlinkGlbPerCon_input:
   """ Required : 
   glbCompany
   glbPerConID
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company field on the GlbPerCon record to unlink  """  
      self.glbPerConID:int = obj["glbPerConID"]
      """  Global PerConID field on the GlbPerCon record to unlink  """  
      self.ds:list[Erp_Tablesets_GlbPerConTableset] = obj["ds"]
      pass

class UnlinkGlbPerCon_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PerConTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbPerConTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPerConTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPerConTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PerConTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PerConTableset] = obj["ds"]
      pass

      """  output parameters  """  

