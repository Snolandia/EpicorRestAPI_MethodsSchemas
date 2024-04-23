import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ConsMonitorSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ConsMonitors(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ConsMonitors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConsMonitors
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CompanyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsMonitors",headers=creds) as resp:
           return await resp.json()

async def post_ConsMonitors(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConsMonitors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CompanyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CompanyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsMonitors", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ConsMonitors_Company(Company, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConsMonitor item
   Description: Calls GetByID to retrieve the ConsMonitor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsMonitor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CompanyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsMonitors(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ConsMonitors_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ConsMonitor for the service
   Description: Calls UpdateExt to update ConsMonitor. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConsMonitor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CompanyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsMonitors(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ConsMonitors_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ConsMonitor item
   Description: Call UpdateExt to delete ConsMonitor item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConsMonitor
      :param Company: Desc: Company   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsMonitors(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_ConsMonitors_Company_ConsTgtDefs(Company, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ConsTgtDefs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ConsTgtDefs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsMonitors(" + Company + ")/ConsTgtDefs",headers=creds) as resp:
           return await resp.json()

async def get_ConsMonitors_Company_ConsTgtDefs_Company_ConsDefID(Company, ConsDefID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConsTgtDef item
   Description: Calls GetByID to retrieve the ConsTgtDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsTgtDef1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsTgtDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsMonitors(" + Company + ")/ConsTgtDefs(" + Company + "," + ConsDefID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ConsTgtDefs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ConsTgtDefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConsTgtDefs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtDefs",headers=creds) as resp:
           return await resp.json()

async def post_ConsTgtDefs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConsTgtDefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ConsTgtDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ConsTgtDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtDefs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ConsTgtDefs_Company_ConsDefID(Company, ConsDefID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConsTgtDef item
   Description: Calls GetByID to retrieve the ConsTgtDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsTgtDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsTgtDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ConsTgtDefs_Company_ConsDefID(Company, ConsDefID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ConsTgtDef for the service
   Description: Calls UpdateExt to update ConsTgtDef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConsTgtDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ConsTgtDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ConsTgtDefs_Company_ConsDefID(Company, ConsDefID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ConsTgtDef item
   Description: Call UpdateExt to delete ConsTgtDef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConsTgtDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ConsTgtDefs_Company_ConsDefID_ConsTgtGens(Company, ConsDefID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ConsTgtGens items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ConsTgtGens1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtGenRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")/ConsTgtGens",headers=creds) as resp:
           return await resp.json()

async def get_ConsTgtDefs_Company_ConsDefID_ConsTgtGens_Company_GenID(Company, ConsDefID, GenID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConsTgtGen item
   Description: Calls GetByID to retrieve the ConsTgtGen item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsTgtGen1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
      :param GenID: Desc: GenID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsTgtGenRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")/ConsTgtGens(" + Company + "," + GenID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ConsTgtDefs_Company_ConsDefID_ConsTgtSrcs(Company, ConsDefID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ConsTgtSrcs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ConsTgtSrcs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtSrcRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")/ConsTgtSrcs",headers=creds) as resp:
           return await resp.json()

async def get_ConsTgtDefs_Company_ConsDefID_ConsTgtSrcs_Company_ConsDefID_SourceBook(Company, ConsDefID, SourceBook, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConsTgtSrc item
   Description: Calls GetByID to retrieve the ConsTgtSrc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsTgtSrc1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
      :param SourceBook: Desc: SourceBook   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsTgtSrcRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtDefs(" + Company + "," + ConsDefID + ")/ConsTgtSrcs(" + Company + "," + ConsDefID + "," + SourceBook + ")",headers=creds) as resp:
           return await resp.json()

async def get_ConsTgtGens(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ConsTgtGens items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConsTgtGens
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtGenRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGens",headers=creds) as resp:
           return await resp.json()

async def post_ConsTgtGens(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConsTgtGens
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ConsTgtGenRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ConsTgtGenRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGens", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ConsTgtGens_Company_GenID(Company, GenID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConsTgtGen item
   Description: Calls GetByID to retrieve the ConsTgtGen item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsTgtGen
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GenID: Desc: GenID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsTgtGenRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGens(" + Company + "," + GenID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ConsTgtGens_Company_GenID(Company, GenID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ConsTgtGen for the service
   Description: Calls UpdateExt to update ConsTgtGen. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConsTgtGen
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GenID: Desc: GenID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ConsTgtGenRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGens(" + Company + "," + GenID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ConsTgtGens_Company_GenID(Company, GenID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ConsTgtGen item
   Description: Call UpdateExt to delete ConsTgtGen item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConsTgtGen
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GenID: Desc: GenID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGens(" + Company + "," + GenID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ConsTgtGens_Company_GenID_ConsSrcCtrls(Company, GenID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ConsSrcCtrls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ConsSrcCtrls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GenID: Desc: GenID   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsSrcCtrlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGens(" + Company + "," + GenID + ")/ConsSrcCtrls",headers=creds) as resp:
           return await resp.json()

async def get_ConsTgtGens_Company_GenID_ConsSrcCtrls_Company_GenID_SourceBook(Company, GenID, SourceBook, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConsSrcCtrl item
   Description: Calls GetByID to retrieve the ConsSrcCtrl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsSrcCtrl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GenID: Desc: GenID   Required: True
      :param SourceBook: Desc: SourceBook   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsSrcCtrlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGens(" + Company + "," + GenID + ")/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")",headers=creds) as resp:
           return await resp.json()

async def get_ConsSrcCtrls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ConsSrcCtrls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConsSrcCtrls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsSrcCtrlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcCtrls",headers=creds) as resp:
           return await resp.json()

async def post_ConsSrcCtrls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConsSrcCtrls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ConsSrcCtrlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ConsSrcCtrlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcCtrls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ConsSrcCtrls_Company_GenID_SourceBook(Company, GenID, SourceBook, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConsSrcCtrl item
   Description: Calls GetByID to retrieve the ConsSrcCtrl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsSrcCtrl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GenID: Desc: GenID   Required: True
      :param SourceBook: Desc: SourceBook   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsSrcCtrlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ConsSrcCtrls_Company_GenID_SourceBook(Company, GenID, SourceBook, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ConsSrcCtrl for the service
   Description: Calls UpdateExt to update ConsSrcCtrl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConsSrcCtrl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GenID: Desc: GenID   Required: True
      :param SourceBook: Desc: SourceBook   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ConsSrcCtrlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ConsSrcCtrls_Company_GenID_SourceBook(Company, GenID, SourceBook, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ConsSrcCtrl item
   Description: Call UpdateExt to delete ConsSrcCtrl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConsSrcCtrl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GenID: Desc: GenID   Required: True
      :param SourceBook: Desc: SourceBook   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")",headers=creds) as resp:
           return await resp.json()

async def get_ConsSrcCtrls_Company_GenID_SourceBook_ConsSrcRates(Company, GenID, SourceBook, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ConsSrcRates items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ConsSrcRates1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GenID: Desc: GenID   Required: True
      :param SourceBook: Desc: SourceBook   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsSrcRatesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")/ConsSrcRates",headers=creds) as resp:
           return await resp.json()

async def get_ConsSrcCtrls_Company_GenID_SourceBook_ConsSrcRates_Company_GenID_SourceBook_FiscalYear_FiscalYearSuffix_FiscalPeriod_RateTypeID(Company, GenID, SourceBook, FiscalYear, FiscalYearSuffix, FiscalPeriod, RateTypeID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConsSrcRate item
   Description: Calls GetByID to retrieve the ConsSrcRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsSrcRate1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GenID: Desc: GenID   Required: True
      :param SourceBook: Desc: SourceBook   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param RateTypeID: Desc: RateTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsSrcRatesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")/ConsSrcRates(" + Company + "," + GenID + "," + SourceBook + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + RateTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ConsSrcRates(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ConsSrcRates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConsSrcRates
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsSrcRatesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcRates",headers=creds) as resp:
           return await resp.json()

async def post_ConsSrcRates(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConsSrcRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ConsSrcRatesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ConsSrcRatesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcRates", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ConsSrcRates_Company_GenID_SourceBook_FiscalYear_FiscalYearSuffix_FiscalPeriod_RateTypeID(Company, GenID, SourceBook, FiscalYear, FiscalYearSuffix, FiscalPeriod, RateTypeID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConsSrcRate item
   Description: Calls GetByID to retrieve the ConsSrcRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsSrcRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GenID: Desc: GenID   Required: True
      :param SourceBook: Desc: SourceBook   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param RateTypeID: Desc: RateTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsSrcRatesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcRates(" + Company + "," + GenID + "," + SourceBook + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + RateTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ConsSrcRates_Company_GenID_SourceBook_FiscalYear_FiscalYearSuffix_FiscalPeriod_RateTypeID(Company, GenID, SourceBook, FiscalYear, FiscalYearSuffix, FiscalPeriod, RateTypeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ConsSrcRate for the service
   Description: Calls UpdateExt to update ConsSrcRate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConsSrcRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GenID: Desc: GenID   Required: True
      :param SourceBook: Desc: SourceBook   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param RateTypeID: Desc: RateTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ConsSrcRatesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcRates(" + Company + "," + GenID + "," + SourceBook + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + RateTypeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ConsSrcRates_Company_GenID_SourceBook_FiscalYear_FiscalYearSuffix_FiscalPeriod_RateTypeID(Company, GenID, SourceBook, FiscalYear, FiscalYearSuffix, FiscalPeriod, RateTypeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ConsSrcRate item
   Description: Call UpdateExt to delete ConsSrcRate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConsSrcRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GenID: Desc: GenID   Required: True
      :param SourceBook: Desc: SourceBook   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param RateTypeID: Desc: RateTypeID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsSrcRates(" + Company + "," + GenID + "," + SourceBook + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + RateTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ConsTgtSrcs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ConsTgtSrcs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConsTgtSrcs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtSrcRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtSrcs",headers=creds) as resp:
           return await resp.json()

async def post_ConsTgtSrcs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConsTgtSrcs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ConsTgtSrcRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ConsTgtSrcRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtSrcs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ConsTgtSrcs_Company_ConsDefID_SourceBook(Company, ConsDefID, SourceBook, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConsTgtSrc item
   Description: Calls GetByID to retrieve the ConsTgtSrc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsTgtSrc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
      :param SourceBook: Desc: SourceBook   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsTgtSrcRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtSrcs(" + Company + "," + ConsDefID + "," + SourceBook + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ConsTgtSrcs_Company_ConsDefID_SourceBook(Company, ConsDefID, SourceBook, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ConsTgtSrc for the service
   Description: Calls UpdateExt to update ConsTgtSrc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConsTgtSrc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
      :param SourceBook: Desc: SourceBook   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ConsTgtSrcRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtSrcs(" + Company + "," + ConsDefID + "," + SourceBook + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ConsTgtSrcs_Company_ConsDefID_SourceBook(Company, ConsDefID, SourceBook, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ConsTgtSrc item
   Description: Call UpdateExt to delete ConsTgtSrc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConsTgtSrc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
      :param SourceBook: Desc: SourceBook   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtSrcs(" + Company + "," + ConsDefID + "," + SourceBook + ")",headers=creds) as resp:
           return await resp.json()

async def get_ConsTgtSrcs_Company_ConsDefID_SourceBook_ConsTgtGenTemps(Company, ConsDefID, SourceBook, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ConsTgtGenTemps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ConsTgtGenTemps1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
      :param SourceBook: Desc: SourceBook   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtGenTempRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtSrcs(" + Company + "," + ConsDefID + "," + SourceBook + ")/ConsTgtGenTemps",headers=creds) as resp:
           return await resp.json()

async def get_ConsTgtSrcs_Company_ConsDefID_SourceBook_ConsTgtGenTemps_Company_ConsDefID_GenID_SourceBook(Company, ConsDefID, SourceBook, GenID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConsTgtGenTemp item
   Description: Calls GetByID to retrieve the ConsTgtGenTemp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsTgtGenTemp1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
      :param SourceBook: Desc: SourceBook   Required: True   Allow empty value : True
      :param GenID: Desc: GenID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsTgtGenTempRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtSrcs(" + Company + "," + ConsDefID + "," + SourceBook + ")/ConsTgtGenTemps(" + Company + "," + ConsDefID + "," + GenID + "," + SourceBook + ")",headers=creds) as resp:
           return await resp.json()

async def get_ConsTgtGenTemps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ConsTgtGenTemps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConsTgtGenTemps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtGenTempRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGenTemps",headers=creds) as resp:
           return await resp.json()

async def post_ConsTgtGenTemps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConsTgtGenTemps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ConsTgtGenTempRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ConsTgtGenTempRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGenTemps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ConsTgtGenTemps_Company_ConsDefID_GenID_SourceBook(Company, ConsDefID, GenID, SourceBook, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConsTgtGenTemp item
   Description: Calls GetByID to retrieve the ConsTgtGenTemp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsTgtGenTemp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
      :param GenID: Desc: GenID   Required: True
      :param SourceBook: Desc: SourceBook   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ConsTgtGenTempRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGenTemps(" + Company + "," + ConsDefID + "," + GenID + "," + SourceBook + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ConsTgtGenTemps_Company_ConsDefID_GenID_SourceBook(Company, ConsDefID, GenID, SourceBook, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ConsTgtGenTemp for the service
   Description: Calls UpdateExt to update ConsTgtGenTemp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConsTgtGenTemp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
      :param GenID: Desc: GenID   Required: True
      :param SourceBook: Desc: SourceBook   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ConsTgtGenTempRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGenTemps(" + Company + "," + ConsDefID + "," + GenID + "," + SourceBook + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ConsTgtGenTemps_Company_ConsDefID_GenID_SourceBook(Company, ConsDefID, GenID, SourceBook, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ConsTgtGenTemp item
   Description: Call UpdateExt to delete ConsTgtGenTemp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConsTgtGenTemp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConsDefID: Desc: ConsDefID   Required: True   Allow empty value : True
      :param GenID: Desc: GenID   Required: True
      :param SourceBook: Desc: SourceBook   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/ConsTgtGenTemps(" + Company + "," + ConsDefID + "," + GenID + "," + SourceBook + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CompanyListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCompany, whereClauseConsTgtDef, whereClauseConsTgtGen, whereClauseConsSrcCtrl, whereClauseConsSrcRates, whereClauseConsTgtSrc, whereClauseConsTgtGenTemp, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCompany=" + whereClauseCompany
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseConsTgtDef=" + whereClauseConsTgtDef
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseConsTgtGen=" + whereClauseConsTgtGen
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseConsSrcCtrl=" + whereClauseConsSrcCtrl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseConsSrcRates=" + whereClauseConsSrcRates
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseConsTgtSrc=" + whereClauseConsTgtSrc
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseConsTgtGenTemp=" + whereClauseConsTgtGenTemp
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectDefaults
   Description: Get the select default values
   OperationID: GetSelectDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectDefaultsWithCalendarID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectDefaultsWithCalendarID
   Description: Get the select default values for Book
   OperationID: GetSelectDefaultsWithCalendarID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectDefaultsWithCalendarID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectDefaultsWithCalendarID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectYearDefaultsWithCalendarID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectYearDefaultsWithCalendarID
   Description: Get the select default values for Book and Year
   OperationID: GetSelectYearDefaultsWithCalendarID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectYearDefaultsWithCalendarID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectYearDefaultsWithCalendarID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectYearSuffixDefaultsWithCalendarID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectYearSuffixDefaultsWithCalendarID
   Description: Get the select default values for Book, Year and YearSuffix
   OperationID: GetSelectYearSuffixDefaultsWithCalendarID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectYearSuffixDefaultsWithCalendarID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectYearSuffixDefaultsWithCalendarID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSelectFiscalInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSelectFiscalInfo
   Description: On change fiscal information from selection section.
   OperationID: OnChangeSelectFiscalInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSelectFiscalInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSelectFiscalInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateTargetBook(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateTargetBook
   Description: Validate book when is selected.
   OperationID: ValidateTargetBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateTargetBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateTargetBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSelectFiscalInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSelectFiscalInfo
   Description: Validate when fiscal info changed.
   OperationID: ValidateSelectFiscalInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSelectFiscalInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSelectFiscalInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSelectFiscalYearSuffixInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSelectFiscalYearSuffixInfo
   Description: Validate when fiscal info changed.
   OperationID: ValidateSelectFiscalYearSuffixInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSelectFiscalYearSuffixInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSelectFiscalYearSuffixInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSelectFiscalYearInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSelectFiscalYearInfo
   Description: Validate when fiscal info changed.
   OperationID: ValidateSelectFiscalYearInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSelectFiscalYearInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSelectFiscalYearInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsMonitor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsMonitor
   Description: Retrieve all records for Monitor
   OperationID: GetRowsMonitor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsMonitor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsMonitor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefinitionMonitor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefinitionMonitor
   OperationID: GetDefinitionMonitor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefinitionMonitor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefinitionMonitor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCompany
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewConsTgtDef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewConsTgtDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewConsTgtDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewConsTgtDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsTgtDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewConsTgtGen(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewConsTgtGen
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewConsTgtGen
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewConsTgtGen_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsTgtGen_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewConsSrcCtrl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewConsSrcCtrl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewConsSrcCtrl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewConsSrcCtrl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsSrcCtrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewConsSrcRates(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewConsSrcRates
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewConsSrcRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewConsSrcRates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsSrcRates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewConsTgtSrc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewConsTgtSrc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewConsTgtSrc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewConsTgtSrc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsTgtSrc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CompanyListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CompanyListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CompanyRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CompanyRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsSrcCtrlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ConsSrcCtrlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsSrcRatesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ConsSrcRatesRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtDefRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ConsTgtDefRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtGenRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ConsTgtGenRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtGenTempRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ConsTgtGenTempRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtSrcRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ConsTgtSrcRow] = obj["value"]
      pass

class Erp_Tablesets_CompanyListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Name:str = obj["Name"]
      """  Company Name  """  
      self.Address1:str = obj["Address1"]
      """  First company address line.  """  
      self.City:str = obj["City"]
      """  City portion of company address.  """  
      self.State:str = obj["State"]
      """  State portion of company address.  """  
      self.Zip:str = obj["Zip"]
      """  Postal code or zip code portion of company address.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Company phone number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CompanyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Name:str = obj["Name"]
      """  Company Name  """  
      self.Address1:str = obj["Address1"]
      """  First company address line.  """  
      self.Address2:str = obj["Address2"]
      """  Second company address line.  """  
      self.Address3:str = obj["Address3"]
      """  Third company address line.  """  
      self.City:str = obj["City"]
      """  City portion of company address.  """  
      self.State:str = obj["State"]
      """  State portion of company address.  """  
      self.Zip:str = obj["Zip"]
      """  Postal code or zip code portion of company address.  """  
      self.Country:str = obj["Country"]
      """  Country portion of company address.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Company phone number  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Company fax number  """  
      self.FEIN:str = obj["FEIN"]
      """  Federal Income Tax Number  """  
      self.StateTaxID:str = obj["StateTaxID"]
      """  State Tax ID  """  
      self.CurrentFiscalYear:int = obj["CurrentFiscalYear"]
      """  Current fiscal year  """  
      self.EDICode:str = obj["EDICode"]
      """  This is the Trading Partner ID that is used for incoming and outgoing EDI.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region Code for this company. This tax region is used to define the 'interior'. It is used as a default tax region in Vendor Maintenance.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.Number:int = obj["Number"]
      """  Added for FRx Integration which requires that the company is identified by a unique positive integer, as opposed to a character string.  FRx calls this the entity number.  It is maintained on the General Ledger configuration screen.  """  
      self.FRxDSN:str = obj["FRxDSN"]
      """  Data Source Name for the FRx database for this company.  Must be linked to a SQL Server 7.0 database to allow exporting of data for financial reporting using FRx.  This field is maintained on the General Ledger configuration screen for each company.  """  
      self.EschedFileSet:str = obj["EschedFileSet"]
      """  The file set where the eScheduling XML messages will be sent.  It must be a valid DOS file name.  If eScheduling is being used with the Manufacturing System this field is required.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  Unique identifier from and external G/L interface  """  
      self.LogoFile:str = obj["LogoFile"]
      """  Name of file that contains the company's logo image.  This can be blank (no logo available).  This is used for Customer/Sales/Supplier Connect.  """  
      self.EmpPhotoPath:str = obj["EmpPhotoPath"]
      """  Path the Employee Photos are stored in.  """  
      self.CalendarID:str = obj["CalendarID"]
      """   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  """  
      self.FrxUserid:str = obj["FrxUserid"]
      """  The User ID for FRx.  """  
      self.FRxPassWord:str = obj["FRxPassWord"]
      """  FRxUserID password  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar id for the company.  """  
      self.LegalName:str = obj["LegalName"]
      """  Company legal name  """  
      self.TaxRegReason:str = obj["TaxRegReason"]
      """  Tax Payer Registration Reason Code  """  
      self.ActTypeCode:str = obj["ActTypeCode"]
      """  Economic Activity Type  """  
      self.OrgRegCode:str = obj["OrgRegCode"]
      """  Organization Registration Code  """  
      self.ManagerName:str = obj["ManagerName"]
      """  Chief Executive Officerr name  """  
      self.ChiefAcctName:str = obj["ChiefAcctName"]
      """  Chief Financial Officer Name  """  
      self.ReportTypePref:str = obj["ReportTypePref"]
      """  Type of report  """  
      self.WIApplication:str = obj["WIApplication"]
      """  WIApplication  """  
      self.WIAutoCreateJob:bool = obj["WIAutoCreateJob"]
      """  WIAutoCreateJob  """  
      self.WIGetDetails:bool = obj["WIGetDetails"]
      """  WIGetDetails  """  
      self.WISchedule:bool = obj["WISchedule"]
      """  WISchedule  """  
      self.WIRelease:bool = obj["WIRelease"]
      """  WIRelease  """  
      self.WIShippingCosts:bool = obj["WIShippingCosts"]
      """  WIShippingCosts  """  
      self.DeepCopy:bool = obj["DeepCopy"]
      """  DeepCopy  """  
      self.DeepCopyDupOrRevEst:bool = obj["DeepCopyDupOrRevEst"]
      """  DeepCopyDupOrRevEst  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MapURL:str = obj["MapURL"]
      """  MapURL  """  
      self.MXMunicipio:str = obj["MXMunicipio"]
      """  MXMunicipio  """  
      self.APBOECheck:int = obj["APBOECheck"]
      """  APBOE Check  """  
      self.COSequenceCert:int = obj["COSequenceCert"]
      """  COSequenceCert  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the Company has to be synchronized with Epicor FSA application.  """  
      self.EpicorAccountNum:int = obj["EpicorAccountNum"]
      """  Epicor client number for CRE  """  
      self.StartDate:str = obj["StartDate"]
      """  StartDate  """  
      self.KindOfEmp:str = obj["KindOfEmp"]
      """  Kind of Employer F - Federal Government, S - State and Local Governmental Employer, T - Tax Exempt Employer, Y - State and Local Tax Exempt Employer, N - None Apply  """  
      self.EmploymentCode:str = obj["EmploymentCode"]
      """  Use the Employment Code field to select either the 941 (Option R) tax form or the 944 (Option F) tax form, depending upon the tax form the employer files. This selection is used in the W2 Processing program during W2 form export.  """  
      self.PurchaseScheduleMode:str = obj["PurchaseScheduleMode"]
      """  Purchase Schedule Mode specifies how the related demand requirements should be handled for this company.  """  
      self.BaseCurrCode:str = obj["BaseCurrCode"]
      """  Currency.BaseCurrCode field  """  
      self.ExtPRConfig:bool = obj["ExtPRConfig"]
      self.HasCurrTrans:bool = obj["HasCurrTrans"]
      """  Has Currency Transactions  """  
      self.Intrastat:bool = obj["Intrastat"]
      self.ProductName:str = obj["ProductName"]
      """  Name of product (MFGSYS Name)  """  
      self.AllowSchedulingBeforeToday:bool = obj["AllowSchedulingBeforeToday"]
      self.BitFlag:int = obj["BitFlag"]
      self.CalendarDescription:str = obj["CalendarDescription"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConsSrcCtrlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calcualted sequence number not inteneded for external use.  """  
      self.SourceBook:str = obj["SourceBook"]
      """  Unique Book Identifier  This is the book that is being consolidated into a target book.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.ConsDefID:str = obj["ConsDefID"]
      """  Unique identifer for the consolidation definition  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Posted Date  """  
      self.PostedTime:int = obj["PostedTime"]
      """  (secounds since midnight)  """  
      self.PostedBy:str = obj["PostedBy"]
      """  User ID of person that posted this period.  """  
      self.DiffOnExchangeAcct:str = obj["DiffOnExchangeAcct"]
      """  Account Number where rounding differences will be posted  """  
      self.GenStatus:str = obj["GenStatus"]
      """  Indicates the current status of the generation.  G =  Generated.  PI = Posted to the Intermediate book.  P = consolidated and Posted to the target.  """  
      self.Bypassed:bool = obj["Bypassed"]
      """  Indicates if consolidation was bypassed  """  
      self.DiffExSegValue1:str = obj["DiffExSegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.DiffExSegValue2:str = obj["DiffExSegValue2"]
      """  SegmentValue 2.  See COASegment segment number 1 for a description of this field.  """  
      self.DiffExSegValue3:str = obj["DiffExSegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.DiffExSegValue4:str = obj["DiffExSegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.DiffExSegValue5:str = obj["DiffExSegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.DiffExSegValue6:str = obj["DiffExSegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.DiffExSegValue7:str = obj["DiffExSegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.DiffExSegValue8:str = obj["DiffExSegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.DiffExSegValue9:str = obj["DiffExSegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.DiffExSegValue10:str = obj["DiffExSegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.DiffExSegValue11:str = obj["DiffExSegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.DiffExSegValue12:str = obj["DiffExSegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.DiffExSegValue13:str = obj["DiffExSegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.DiffExSegValue14:str = obj["DiffExSegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.DiffExSegValue15:str = obj["DiffExSegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.DiffExSegValue16:str = obj["DiffExSegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.DiffExSegValue17:str = obj["DiffExSegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.DiffExSegValue18:str = obj["DiffExSegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.DiffExSegValue19:str = obj["DiffExSegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.DiffExSegValue20:str = obj["DiffExSegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.RemoteAcct:str = obj["RemoteAcct"]
      """  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  """  
      self.BalanceSheetDefType:str = obj["BalanceSheetDefType"]
      """  The related ConsType ID  """  
      self.IncomeStmtDefType:str = obj["IncomeStmtDefType"]
      """  The related ConsType ID  """  
      self.ClosingPeriods:int = obj["ClosingPeriods"]
      """  The number of closing periods to be processed during consolidation.  The default value is zero which indicates that closing periods are not consolidated.  """  
      self.ExcludeOpenPrds:bool = obj["ExcludeOpenPrds"]
      """  Applies to Periodic Consolidation only.  Logical indicating if open periods are excluded from consolidation.  If yes, any balance records written against a source book in a period that is still open is not sent to the target company.  If no, all balance records are sent.  Note: The fiscal calendar is defined on the GLBook table for the source company and book.  """  
      self.TgtJrnlCode:str = obj["TgtJrnlCode"]
      """  The journal code to use when posting the consolidation records in the target company book.  """  
      self.ReverseDBCR:bool = obj["ReverseDBCR"]
      """  This option is only avaialble when 'Use Intermediate Book' equals yes.  Indicates if debit and credit amounts are swapped before the data is transferred.  """  
      self.COAMapUID:int = obj["COAMapUID"]
      """  Accounting segments mapping ID to use when calling the mapping engine.  Must be a valid entry in the COAMap table.  This is NOT available when remote parent is set to true.  The source COA on the mapping record must be the same as the COA assigned to the source book.  If the source company equals the target company then the target COA on this mapping record must be the COA assigned to the target book.  """  
      self.IntermediateJrnlCode:str = obj["IntermediateJrnlCode"]
      """  Only available when 'Use Intermediate Book' equals yes.  This is the the journal code to use when posting consolidated entries to the intermediate book.  """  
      self.Retransfer:bool = obj["Retransfer"]
      """  Retransfer  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AdjustFromFiscalPeriod:int = obj["AdjustFromFiscalPeriod"]
      """  The fiscal period to start adjusting from  """  
      self.PeriodEndDate:str = obj["PeriodEndDate"]
      """  PeriodEndDate  """  
      self.AdjPeriodEndDate:str = obj["AdjPeriodEndDate"]
      """  AdjPeriodEndDate  """  
      self.ProcessedFiscalPeriod:int = obj["ProcessedFiscalPeriod"]
      """  When posting, the last fiscal period that was processed without error, particulary for consolidations that span multiple periods.  """  
      self.ConsolidationStatus:str = obj["ConsolidationStatus"]
      """   Indicates the status of the consolidation for display purposes.  Is set programatically.

F - First consolidation
R - Retrospective
L - Last Period Delta
O - Overriding Period  """  
      self.PeriodsMissed:bool = obj["PeriodsMissed"]
      """  Indicates if previous periods have not been consolidated  """  
      self.SourceCOA:str = obj["SourceCOA"]
      """  Source COA code  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  TargetCOA for DiffExtAccount  """  
      self.NextPeriodConsolidation:bool = obj["NextPeriodConsolidation"]
      """  Flag indicating that next period consolidation has been performed  """  
      self.BitFlag:int = obj["BitFlag"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.SourceBookDescription:str = obj["SourceBookDescription"]
      self.SourceBookCurrencyCode:str = obj["SourceBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConsSrcRatesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calcualted sequence number not inteneded for external use.  """  
      self.SourceBook:str = obj["SourceBook"]
      """  Unique Book Identifier  This is the book that is being consolidated into a target book.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.RateTypeID:str = obj["RateTypeID"]
      """  Rate Type id of related RateType.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate that will be used for this Rate Type.  """  
      self.UserModified:bool = obj["UserModified"]
      """  Internal field used to indicate whether or not the user modified the rates.  """  
      self.RateError:bool = obj["RateError"]
      """  Internal field used to indicate if the system was unable to calcuate the rates.  If yes, the rates are in error.  If no, the rates are okay.  """  
      self.CalcDate:str = obj["CalcDate"]
      """  Calculation Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefaultMethod:str = obj["DefaultMethod"]
      """  Daily Average, Period End or None  """  
      self.Selected:bool = obj["Selected"]
      """  Indicates if the record is selected for retrieval of default values  """  
      self.Description:str = obj["Description"]
      self.BitFlag:int = obj["BitFlag"]
      self.RateTypeIDDescription:str = obj["RateTypeIDDescription"]
      self.SourceBookCurrencyCode:str = obj["SourceBookCurrencyCode"]
      self.SourceBookDescription:str = obj["SourceBookDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConsTgtDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ConsDefID:str = obj["ConsDefID"]
      """  Unique identifer for the consolidation definition  """  
      self.Description:str = obj["Description"]
      """  Free form text that describes the target that sources are consolidated into.  """  
      self.RemoteParent:bool = obj["RemoteParent"]
      """  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  """  
      self.VantageDB:bool = obj["VantageDB"]
      """  Used to notify the consolidation routine whether or not the Parent company is running an Epicor database.  """  
      self.TgtCompany:str = obj["TgtCompany"]
      """  Target Company Identifier.  """  
      self.TgtBook:str = obj["TgtBook"]
      """  Unique Book Identifier  This is the book the source book is consolidated to.  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  """  
      self.ConsolidationType:str = obj["ConsolidationType"]
      """   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  """  
      self.OutputFile:str = obj["OutputFile"]
      """  Import/Export file name.  """  
      self.IntermediateBookID:str = obj["IntermediateBookID"]
      """  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  """  
      self.ImmediateTrans:bool = obj["ImmediateTrans"]
      """  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RemoteAcct:str = obj["RemoteAcct"]
      """  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  """  
      self.AdjustMode:str = obj["AdjustMode"]
      """  D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

O = Override.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TgtBookCal:str = obj["TgtBookCal"]
      """  Target Book Fiscal Calendar  """  
      self.IterBookFiscalCal:str = obj["IterBookFiscalCal"]
      """  Intermediate book fiscal calendar  """  
      self.TgtBookFiscalCal:str = obj["TgtBookFiscalCal"]
      """  Target Book fiscal Calendar  """  
      self.TgtBookDesc:str = obj["TgtBookDesc"]
      """  Target Book Description  """  
      self.IntermediateCOA:str = obj["IntermediateCOA"]
      """  Intermediate COA Code  """  
      self.AdjustModeInput:bool = obj["AdjustModeInput"]
      """  Field used for UI.  The option is stored in db filed AdjustMode, which is a string.  On the UI, the field should appear as a checkbox.  """  
      self.SrcCompany:str = obj["SrcCompany"]
      """  Source Company  """  
      self.SrcCompanyName:str = obj["SrcCompanyName"]
      """  Source Company Name  """  
      self.HasConsolitation:bool = obj["HasConsolitation"]
      """  This column is used to accomplish the following UI behavior, in order to enable and disable some UI controls according to if a consolidation was already created using the definition.  """  
      self.LastGenStatus:str = obj["LastGenStatus"]
      """  The field is used in the Consolidation Monitor Entry for tracking the state of the last consolidation  """  
      self.IterBookFiscalCalID:str = obj["IterBookFiscalCalID"]
      """  Intermediate book fiscal calendar ID.  """  
      self.TgtBookFiscalCalID:str = obj["TgtBookFiscalCalID"]
      """  Target Book fiscal Calendar ID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.InterBookCurrencyCode:str = obj["InterBookCurrencyCode"]
      self.InterBookDescription:str = obj["InterBookDescription"]
      self.TargetCOName:str = obj["TargetCOName"]
      self.TgtCOADescription:str = obj["TgtCOADescription"]
      self.TgtCurrencyCurrName:str = obj["TgtCurrencyCurrName"]
      self.TgtCurrencyCurrSymbol:str = obj["TgtCurrencyCurrSymbol"]
      self.TgtCurrencyCurrencyID:str = obj["TgtCurrencyCurrencyID"]
      self.TgtCurrencyDocumentDesc:str = obj["TgtCurrencyDocumentDesc"]
      self.TgtCurrencyCurrDesc:str = obj["TgtCurrencyCurrDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConsTgtGenRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calculated sequence number not inteneded for external use.  """  
      self.ConsDefID:str = obj["ConsDefID"]
      """  Unique identifer for the consolidation definition  """  
      self.Description:str = obj["Description"]
      """  Generation Description  """  
      self.GenStatus:str = obj["GenStatus"]
      """  Indicates the current status of the generation.  O = Open generation and consolidation have not occurred.  G =  Generated.  PI = Posted to the Intermediate book.  P = consolidated and Posted to the target.  """  
      self.TgtCompany:str = obj["TgtCompany"]
      """  Target Company Identifier.  """  
      self.TgtBook:str = obj["TgtBook"]
      """  Unique Book Identifier  This is the book the source book is consolidated to.  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  """  
      self.IntermediateBookID:str = obj["IntermediateBookID"]
      """  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  """  
      self.ImmediateTrans:bool = obj["ImmediateTrans"]
      """  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RemoteParent:bool = obj["RemoteParent"]
      """  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  """  
      self.VantageDB:bool = obj["VantageDB"]
      """  Used to notify the consolidation routine whether or not the Parent company is running an Epicor database.  """  
      self.OutputFile:str = obj["OutputFile"]
      """  Import/Export file name.  """  
      self.RemoteAcct:str = obj["RemoteAcct"]
      """  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  """  
      self.ConsolidationType:str = obj["ConsolidationType"]
      """   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  """  
      self.AdjustMode:str = obj["AdjustMode"]
      """   THIS IS RESERVED FOR FUTURE USE.

D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

F = Full Replacement.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EntryMode:str = obj["EntryMode"]
      """  Identifies the mode the record was added in.  C = Consolidation, R = Retrospective Adjustment  """  
      self.MasterCOA:bool = obj["MasterCOA"]
      """  Logical indicating if this COA is the Master COA.  """  
      self.LatestConsolidation:bool = obj["LatestConsolidation"]
      """  LatestConsolidation  """  
      self.ClosingPeriods:int = obj["ClosingPeriods"]
      """  Closing periods parameter defined in Consolidation definition.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ConsDefIDDescription:str = obj["ConsDefIDDescription"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.IntermediateBookIDDescription:str = obj["IntermediateBookIDDescription"]
      self.IntermediateBookIDCurrencyCode:str = obj["IntermediateBookIDCurrencyCode"]
      self.TargetCOADescription:str = obj["TargetCOADescription"]
      self.TgtBookCurrencyCode:str = obj["TgtBookCurrencyCode"]
      self.TgtBookDescription:str = obj["TgtBookDescription"]
      self.TgtCompanyName:str = obj["TgtCompanyName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConsTgtGenTempRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calculated sequence number not inteneded for external use.  """  
      self.ConsDefID:str = obj["ConsDefID"]
      """  Unique identifer for the consolidation definition  """  
      self.Description:str = obj["Description"]
      """  Generation Description  """  
      self.GenStatus:str = obj["GenStatus"]
      """  Indicates the current status of the generation.  O = Open generation and consolidation have not occurred.  G =  Generated.  PI = Posted to the Intermediate book.  P = consolidated and Posted to the target.  """  
      self.TgtCompany:str = obj["TgtCompany"]
      """  Target Company Identifier.  """  
      self.TgtBook:str = obj["TgtBook"]
      """  Unique Book Identifier  This is the book the source book is consolidated to.  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  """  
      self.IntermediateBookID:str = obj["IntermediateBookID"]
      """  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  """  
      self.ImmediateTrans:bool = obj["ImmediateTrans"]
      """  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RemoteParent:bool = obj["RemoteParent"]
      """  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  """  
      self.VantageDB:bool = obj["VantageDB"]
      """  Used to notify the consolidation routine whether or not the Parent company is running a Vantage database.  """  
      self.OutputFile:str = obj["OutputFile"]
      """  Import/Export file name.  """  
      self.RemoteAcct:str = obj["RemoteAcct"]
      """  The free form Diff on Exchange Acct for a Remote Parent that is not a Vantage Database  """  
      self.ConsolidationType:str = obj["ConsolidationType"]
      """   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  """  
      self.AdjustMode:str = obj["AdjustMode"]
      """   THIS IS RESERVED FOR FUTURE USE.

D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

F = Full Replacement.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EntryMode:str = obj["EntryMode"]
      """  Identifies the mode the record was added in.  C = Consolidation, R = Retrospective Adjustment  """  
      self.MasterCOA:bool = obj["MasterCOA"]
      """  Logical indicating if this COA is the Master COA.  """  
      self.SourceBook:str = obj["SourceBook"]
      self.ScrBookDesc:str = obj["ScrBookDesc"]
      self.ConsNodeCaption:str = obj["ConsNodeCaption"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConsTgtSrcRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ConsDefID:str = obj["ConsDefID"]
      """  Unique identifer for the consolidation definition  """  
      self.SourceBook:str = obj["SourceBook"]
      """  Unique Book Identifier  This is the book that is being consolidated into a target book.  """  
      self.BalanceSheetDefType:str = obj["BalanceSheetDefType"]
      """  The related ConsType ID  """  
      self.IncomeStmtDefType:str = obj["IncomeStmtDefType"]
      """  The related ConsType ID  """  
      self.ClosingPeriods:int = obj["ClosingPeriods"]
      """  The number of closing periods to be processed during consolidation.  The default value is zero which indicates that closing periods are not consolidated.  """  
      self.ExcludeOpenPrds:bool = obj["ExcludeOpenPrds"]
      """  Applies to Periodic Consolidation only.  Logical indicating if open periods are excluded from consolidation.  If yes, any balance records written against a source book in a period that is still open is not sent to the target company.  If no, all balance records are sent.  Note: The fiscal calendar is defined on the GLBook table for the source company and book.  """  
      self.TgtJrnlCode:str = obj["TgtJrnlCode"]
      """  The journal code to use when posting the consolidation records in the target company book.  """  
      self.ReverseDBCR:bool = obj["ReverseDBCR"]
      """  This option is only avaialble when 'Use Intermediate Book' equals yes.  Indicates if debit and credit amounts are swapped before the data is transferred.  """  
      self.COAMapUID:int = obj["COAMapUID"]
      """  Accounting segments mapping ID to use when calling the mapping engine.  Must be a valid entry in the COAMap table.  This is NOT available when remote parent is set to true.  The source COA on the mapping record must be the same as the COA assigned to the source book.  If the source company equals the target company then the target COA on this mapping record must be the COA assigned to the target book.  """  
      self.IntermediateJrnlCode:str = obj["IntermediateJrnlCode"]
      """  Only available when 'Use Intermediate Book' equals yes.  This is the the journal code to use when posting consolidated entries to the intermediate book.  """  
      self.DiffOnExchangeAcct:str = obj["DiffOnExchangeAcct"]
      """  Account Number where rounding differences will be posted  """  
      self.DiffExSegValue1:str = obj["DiffExSegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.DiffExSegValue2:str = obj["DiffExSegValue2"]
      """  SegmentValue 2.  See COASegment segment number 1 for a description of this field.  """  
      self.DiffExSegValue3:str = obj["DiffExSegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.DiffExSegValue4:str = obj["DiffExSegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.DiffExSegValue5:str = obj["DiffExSegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.DiffExSegValue6:str = obj["DiffExSegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.DiffExSegValue7:str = obj["DiffExSegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.DiffExSegValue8:str = obj["DiffExSegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.DiffExSegValue9:str = obj["DiffExSegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.DiffExSegValue10:str = obj["DiffExSegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.DiffExSegValue11:str = obj["DiffExSegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.DiffExSegValue12:str = obj["DiffExSegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.DiffExSegValue13:str = obj["DiffExSegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.DiffExSegValue14:str = obj["DiffExSegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.DiffExSegValue15:str = obj["DiffExSegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.DiffExSegValue16:str = obj["DiffExSegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.DiffExSegValue17:str = obj["DiffExSegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.DiffExSegValue18:str = obj["DiffExSegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.DiffExSegValue19:str = obj["DiffExSegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.DiffExSegValue20:str = obj["DiffExSegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  Target COA - this field is intended for internal use  """  
      self.TargetCompany:str = obj["TargetCompany"]
      """  Target Company ID - intended for internal use  """  
      self.SourceCOA:str = obj["SourceCOA"]
      """  Source COA code  """  
      self.InterJrnlDesc:str = obj["InterJrnlDesc"]
      """  Intermediate Journal Code description.  This is either from the JrnlCode or GLBJrnCode table.  """  
      self.TgtJrnlCodeDesc:str = obj["TgtJrnlCodeDesc"]
      """  Target Journal Code description.  This is either from the JrnlCode or GLBJrnCode table.  """  
      self.CurrencyDesc:str = obj["CurrencyDesc"]
      """  Currency code description from either the Currency or GLBCurrency table.  """  
      self.SrcFiscalCalendar:str = obj["SrcFiscalCalendar"]
      """  Source book fiscal calendar.  """  
      self.DiffOnExchangeDesc:str = obj["DiffOnExchangeDesc"]
      """  Holds GLAccount description temporarily to provide extra information to the user.  """  
      self.IntermediateCOA:str = obj["IntermediateCOA"]
      """  Intermediate COA Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BalanceConsTypeDescription:str = obj["BalanceConsTypeDescription"]
      self.BalanceRateDescription:str = obj["BalanceRateDescription"]
      self.COAMapDisplayName:str = obj["COAMapDisplayName"]
      self.IncomeConsTypeDescription:str = obj["IncomeConsTypeDescription"]
      self.IncomeRateDescription:str = obj["IncomeRateDescription"]
      self.SrcBookDescription:str = obj["SrcBookDescription"]
      self.SrcBookCurrencyCode:str = obj["SrcBookCurrencyCode"]
      self.SrcCompanyName:str = obj["SrcCompanyName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CompanyListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Name:str = obj["Name"]
      """  Company Name  """  
      self.Address1:str = obj["Address1"]
      """  First company address line.  """  
      self.City:str = obj["City"]
      """  City portion of company address.  """  
      self.State:str = obj["State"]
      """  State portion of company address.  """  
      self.Zip:str = obj["Zip"]
      """  Postal code or zip code portion of company address.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Company phone number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CompanyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Name:str = obj["Name"]
      """  Company Name  """  
      self.Address1:str = obj["Address1"]
      """  First company address line.  """  
      self.Address2:str = obj["Address2"]
      """  Second company address line.  """  
      self.Address3:str = obj["Address3"]
      """  Third company address line.  """  
      self.City:str = obj["City"]
      """  City portion of company address.  """  
      self.State:str = obj["State"]
      """  State portion of company address.  """  
      self.Zip:str = obj["Zip"]
      """  Postal code or zip code portion of company address.  """  
      self.Country:str = obj["Country"]
      """  Country portion of company address.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Company phone number  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Company fax number  """  
      self.FEIN:str = obj["FEIN"]
      """  Federal Income Tax Number  """  
      self.StateTaxID:str = obj["StateTaxID"]
      """  State Tax ID  """  
      self.CurrentFiscalYear:int = obj["CurrentFiscalYear"]
      """  Current fiscal year  """  
      self.EDICode:str = obj["EDICode"]
      """  This is the Trading Partner ID that is used for incoming and outgoing EDI.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region Code for this company. This tax region is used to define the 'interior'. It is used as a default tax region in Vendor Maintenance.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.Number:int = obj["Number"]
      """  Added for FRx Integration which requires that the company is identified by a unique positive integer, as opposed to a character string.  FRx calls this the entity number.  It is maintained on the General Ledger configuration screen.  """  
      self.FRxDSN:str = obj["FRxDSN"]
      """  Data Source Name for the FRx database for this company.  Must be linked to a SQL Server 7.0 database to allow exporting of data for financial reporting using FRx.  This field is maintained on the General Ledger configuration screen for each company.  """  
      self.EschedFileSet:str = obj["EschedFileSet"]
      """  The file set where the eScheduling XML messages will be sent.  It must be a valid DOS file name.  If eScheduling is being used with the Manufacturing System this field is required.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  Unique identifier from and external G/L interface  """  
      self.LogoFile:str = obj["LogoFile"]
      """  Name of file that contains the company's logo image.  This can be blank (no logo available).  This is used for Customer/Sales/Supplier Connect.  """  
      self.EmpPhotoPath:str = obj["EmpPhotoPath"]
      """  Path the Employee Photos are stored in.  """  
      self.CalendarID:str = obj["CalendarID"]
      """   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  """  
      self.FrxUserid:str = obj["FrxUserid"]
      """  The User ID for FRx.  """  
      self.FRxPassWord:str = obj["FRxPassWord"]
      """  FRxUserID password  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar id for the company.  """  
      self.LegalName:str = obj["LegalName"]
      """  Company legal name  """  
      self.TaxRegReason:str = obj["TaxRegReason"]
      """  Tax Payer Registration Reason Code  """  
      self.ActTypeCode:str = obj["ActTypeCode"]
      """  Economic Activity Type  """  
      self.OrgRegCode:str = obj["OrgRegCode"]
      """  Organization Registration Code  """  
      self.ManagerName:str = obj["ManagerName"]
      """  Chief Executive Officerr name  """  
      self.ChiefAcctName:str = obj["ChiefAcctName"]
      """  Chief Financial Officer Name  """  
      self.ReportTypePref:str = obj["ReportTypePref"]
      """  Type of report  """  
      self.WIApplication:str = obj["WIApplication"]
      """  WIApplication  """  
      self.WIAutoCreateJob:bool = obj["WIAutoCreateJob"]
      """  WIAutoCreateJob  """  
      self.WIGetDetails:bool = obj["WIGetDetails"]
      """  WIGetDetails  """  
      self.WISchedule:bool = obj["WISchedule"]
      """  WISchedule  """  
      self.WIRelease:bool = obj["WIRelease"]
      """  WIRelease  """  
      self.WIShippingCosts:bool = obj["WIShippingCosts"]
      """  WIShippingCosts  """  
      self.DeepCopy:bool = obj["DeepCopy"]
      """  DeepCopy  """  
      self.DeepCopyDupOrRevEst:bool = obj["DeepCopyDupOrRevEst"]
      """  DeepCopyDupOrRevEst  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MapURL:str = obj["MapURL"]
      """  MapURL  """  
      self.MXMunicipio:str = obj["MXMunicipio"]
      """  MXMunicipio  """  
      self.APBOECheck:int = obj["APBOECheck"]
      """  APBOE Check  """  
      self.COSequenceCert:int = obj["COSequenceCert"]
      """  COSequenceCert  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the Company has to be synchronized with Epicor FSA application.  """  
      self.EpicorAccountNum:int = obj["EpicorAccountNum"]
      """  Epicor client number for CRE  """  
      self.StartDate:str = obj["StartDate"]
      """  StartDate  """  
      self.KindOfEmp:str = obj["KindOfEmp"]
      """  Kind of Employer F - Federal Government, S - State and Local Governmental Employer, T - Tax Exempt Employer, Y - State and Local Tax Exempt Employer, N - None Apply  """  
      self.EmploymentCode:str = obj["EmploymentCode"]
      """  Use the Employment Code field to select either the 941 (Option R) tax form or the 944 (Option F) tax form, depending upon the tax form the employer files. This selection is used in the W2 Processing program during W2 form export.  """  
      self.PurchaseScheduleMode:str = obj["PurchaseScheduleMode"]
      """  Purchase Schedule Mode specifies how the related demand requirements should be handled for this company.  """  
      self.BaseCurrCode:str = obj["BaseCurrCode"]
      """  Currency.BaseCurrCode field  """  
      self.ExtPRConfig:bool = obj["ExtPRConfig"]
      self.HasCurrTrans:bool = obj["HasCurrTrans"]
      """  Has Currency Transactions  """  
      self.Intrastat:bool = obj["Intrastat"]
      self.ProductName:str = obj["ProductName"]
      """  Name of product (MFGSYS Name)  """  
      self.AllowSchedulingBeforeToday:bool = obj["AllowSchedulingBeforeToday"]
      self.BitFlag:int = obj["BitFlag"]
      self.CalendarDescription:str = obj["CalendarDescription"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConsMonitorListTableset:
   def __init__(self, obj):
      self.CompanyList:list[Erp_Tablesets_CompanyListRow] = obj["CompanyList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ConsMonitorTableset:
   def __init__(self, obj):
      self.Company:list[Erp_Tablesets_CompanyRow] = obj["Company"]
      self.ConsTgtDef:list[Erp_Tablesets_ConsTgtDefRow] = obj["ConsTgtDef"]
      self.ConsTgtGen:list[Erp_Tablesets_ConsTgtGenRow] = obj["ConsTgtGen"]
      self.ConsSrcCtrl:list[Erp_Tablesets_ConsSrcCtrlRow] = obj["ConsSrcCtrl"]
      self.ConsSrcRates:list[Erp_Tablesets_ConsSrcRatesRow] = obj["ConsSrcRates"]
      self.ConsTgtSrc:list[Erp_Tablesets_ConsTgtSrcRow] = obj["ConsTgtSrc"]
      self.ConsTgtGenTemp:list[Erp_Tablesets_ConsTgtGenTempRow] = obj["ConsTgtGenTemp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ConsSrcCtrlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calcualted sequence number not inteneded for external use.  """  
      self.SourceBook:str = obj["SourceBook"]
      """  Unique Book Identifier  This is the book that is being consolidated into a target book.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.ConsDefID:str = obj["ConsDefID"]
      """  Unique identifer for the consolidation definition  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Posted Date  """  
      self.PostedTime:int = obj["PostedTime"]
      """  (secounds since midnight)  """  
      self.PostedBy:str = obj["PostedBy"]
      """  User ID of person that posted this period.  """  
      self.DiffOnExchangeAcct:str = obj["DiffOnExchangeAcct"]
      """  Account Number where rounding differences will be posted  """  
      self.GenStatus:str = obj["GenStatus"]
      """  Indicates the current status of the generation.  G =  Generated.  PI = Posted to the Intermediate book.  P = consolidated and Posted to the target.  """  
      self.Bypassed:bool = obj["Bypassed"]
      """  Indicates if consolidation was bypassed  """  
      self.DiffExSegValue1:str = obj["DiffExSegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.DiffExSegValue2:str = obj["DiffExSegValue2"]
      """  SegmentValue 2.  See COASegment segment number 1 for a description of this field.  """  
      self.DiffExSegValue3:str = obj["DiffExSegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.DiffExSegValue4:str = obj["DiffExSegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.DiffExSegValue5:str = obj["DiffExSegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.DiffExSegValue6:str = obj["DiffExSegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.DiffExSegValue7:str = obj["DiffExSegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.DiffExSegValue8:str = obj["DiffExSegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.DiffExSegValue9:str = obj["DiffExSegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.DiffExSegValue10:str = obj["DiffExSegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.DiffExSegValue11:str = obj["DiffExSegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.DiffExSegValue12:str = obj["DiffExSegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.DiffExSegValue13:str = obj["DiffExSegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.DiffExSegValue14:str = obj["DiffExSegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.DiffExSegValue15:str = obj["DiffExSegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.DiffExSegValue16:str = obj["DiffExSegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.DiffExSegValue17:str = obj["DiffExSegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.DiffExSegValue18:str = obj["DiffExSegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.DiffExSegValue19:str = obj["DiffExSegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.DiffExSegValue20:str = obj["DiffExSegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.RemoteAcct:str = obj["RemoteAcct"]
      """  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  """  
      self.BalanceSheetDefType:str = obj["BalanceSheetDefType"]
      """  The related ConsType ID  """  
      self.IncomeStmtDefType:str = obj["IncomeStmtDefType"]
      """  The related ConsType ID  """  
      self.ClosingPeriods:int = obj["ClosingPeriods"]
      """  The number of closing periods to be processed during consolidation.  The default value is zero which indicates that closing periods are not consolidated.  """  
      self.ExcludeOpenPrds:bool = obj["ExcludeOpenPrds"]
      """  Applies to Periodic Consolidation only.  Logical indicating if open periods are excluded from consolidation.  If yes, any balance records written against a source book in a period that is still open is not sent to the target company.  If no, all balance records are sent.  Note: The fiscal calendar is defined on the GLBook table for the source company and book.  """  
      self.TgtJrnlCode:str = obj["TgtJrnlCode"]
      """  The journal code to use when posting the consolidation records in the target company book.  """  
      self.ReverseDBCR:bool = obj["ReverseDBCR"]
      """  This option is only avaialble when 'Use Intermediate Book' equals yes.  Indicates if debit and credit amounts are swapped before the data is transferred.  """  
      self.COAMapUID:int = obj["COAMapUID"]
      """  Accounting segments mapping ID to use when calling the mapping engine.  Must be a valid entry in the COAMap table.  This is NOT available when remote parent is set to true.  The source COA on the mapping record must be the same as the COA assigned to the source book.  If the source company equals the target company then the target COA on this mapping record must be the COA assigned to the target book.  """  
      self.IntermediateJrnlCode:str = obj["IntermediateJrnlCode"]
      """  Only available when 'Use Intermediate Book' equals yes.  This is the the journal code to use when posting consolidated entries to the intermediate book.  """  
      self.Retransfer:bool = obj["Retransfer"]
      """  Retransfer  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AdjustFromFiscalPeriod:int = obj["AdjustFromFiscalPeriod"]
      """  The fiscal period to start adjusting from  """  
      self.PeriodEndDate:str = obj["PeriodEndDate"]
      """  PeriodEndDate  """  
      self.AdjPeriodEndDate:str = obj["AdjPeriodEndDate"]
      """  AdjPeriodEndDate  """  
      self.ProcessedFiscalPeriod:int = obj["ProcessedFiscalPeriod"]
      """  When posting, the last fiscal period that was processed without error, particulary for consolidations that span multiple periods.  """  
      self.ConsolidationStatus:str = obj["ConsolidationStatus"]
      """   Indicates the status of the consolidation for display purposes.  Is set programatically.

F - First consolidation
R - Retrospective
L - Last Period Delta
O - Overriding Period  """  
      self.PeriodsMissed:bool = obj["PeriodsMissed"]
      """  Indicates if previous periods have not been consolidated  """  
      self.SourceCOA:str = obj["SourceCOA"]
      """  Source COA code  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  TargetCOA for DiffExtAccount  """  
      self.NextPeriodConsolidation:bool = obj["NextPeriodConsolidation"]
      """  Flag indicating that next period consolidation has been performed  """  
      self.BitFlag:int = obj["BitFlag"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.SourceBookDescription:str = obj["SourceBookDescription"]
      self.SourceBookCurrencyCode:str = obj["SourceBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConsSrcRatesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calcualted sequence number not inteneded for external use.  """  
      self.SourceBook:str = obj["SourceBook"]
      """  Unique Book Identifier  This is the book that is being consolidated into a target book.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.RateTypeID:str = obj["RateTypeID"]
      """  Rate Type id of related RateType.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate that will be used for this Rate Type.  """  
      self.UserModified:bool = obj["UserModified"]
      """  Internal field used to indicate whether or not the user modified the rates.  """  
      self.RateError:bool = obj["RateError"]
      """  Internal field used to indicate if the system was unable to calcuate the rates.  If yes, the rates are in error.  If no, the rates are okay.  """  
      self.CalcDate:str = obj["CalcDate"]
      """  Calculation Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefaultMethod:str = obj["DefaultMethod"]
      """  Daily Average, Period End or None  """  
      self.Selected:bool = obj["Selected"]
      """  Indicates if the record is selected for retrieval of default values  """  
      self.Description:str = obj["Description"]
      self.BitFlag:int = obj["BitFlag"]
      self.RateTypeIDDescription:str = obj["RateTypeIDDescription"]
      self.SourceBookCurrencyCode:str = obj["SourceBookCurrencyCode"]
      self.SourceBookDescription:str = obj["SourceBookDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConsTgtDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ConsDefID:str = obj["ConsDefID"]
      """  Unique identifer for the consolidation definition  """  
      self.Description:str = obj["Description"]
      """  Free form text that describes the target that sources are consolidated into.  """  
      self.RemoteParent:bool = obj["RemoteParent"]
      """  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  """  
      self.VantageDB:bool = obj["VantageDB"]
      """  Used to notify the consolidation routine whether or not the Parent company is running an Epicor database.  """  
      self.TgtCompany:str = obj["TgtCompany"]
      """  Target Company Identifier.  """  
      self.TgtBook:str = obj["TgtBook"]
      """  Unique Book Identifier  This is the book the source book is consolidated to.  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  """  
      self.ConsolidationType:str = obj["ConsolidationType"]
      """   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  """  
      self.OutputFile:str = obj["OutputFile"]
      """  Import/Export file name.  """  
      self.IntermediateBookID:str = obj["IntermediateBookID"]
      """  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  """  
      self.ImmediateTrans:bool = obj["ImmediateTrans"]
      """  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RemoteAcct:str = obj["RemoteAcct"]
      """  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  """  
      self.AdjustMode:str = obj["AdjustMode"]
      """  D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

O = Override.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TgtBookCal:str = obj["TgtBookCal"]
      """  Target Book Fiscal Calendar  """  
      self.IterBookFiscalCal:str = obj["IterBookFiscalCal"]
      """  Intermediate book fiscal calendar  """  
      self.TgtBookFiscalCal:str = obj["TgtBookFiscalCal"]
      """  Target Book fiscal Calendar  """  
      self.TgtBookDesc:str = obj["TgtBookDesc"]
      """  Target Book Description  """  
      self.IntermediateCOA:str = obj["IntermediateCOA"]
      """  Intermediate COA Code  """  
      self.AdjustModeInput:bool = obj["AdjustModeInput"]
      """  Field used for UI.  The option is stored in db filed AdjustMode, which is a string.  On the UI, the field should appear as a checkbox.  """  
      self.SrcCompany:str = obj["SrcCompany"]
      """  Source Company  """  
      self.SrcCompanyName:str = obj["SrcCompanyName"]
      """  Source Company Name  """  
      self.HasConsolitation:bool = obj["HasConsolitation"]
      """  This column is used to accomplish the following UI behavior, in order to enable and disable some UI controls according to if a consolidation was already created using the definition.  """  
      self.LastGenStatus:str = obj["LastGenStatus"]
      """  The field is used in the Consolidation Monitor Entry for tracking the state of the last consolidation  """  
      self.IterBookFiscalCalID:str = obj["IterBookFiscalCalID"]
      """  Intermediate book fiscal calendar ID.  """  
      self.TgtBookFiscalCalID:str = obj["TgtBookFiscalCalID"]
      """  Target Book fiscal Calendar ID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.InterBookCurrencyCode:str = obj["InterBookCurrencyCode"]
      self.InterBookDescription:str = obj["InterBookDescription"]
      self.TargetCOName:str = obj["TargetCOName"]
      self.TgtCOADescription:str = obj["TgtCOADescription"]
      self.TgtCurrencyCurrName:str = obj["TgtCurrencyCurrName"]
      self.TgtCurrencyCurrSymbol:str = obj["TgtCurrencyCurrSymbol"]
      self.TgtCurrencyCurrencyID:str = obj["TgtCurrencyCurrencyID"]
      self.TgtCurrencyDocumentDesc:str = obj["TgtCurrencyDocumentDesc"]
      self.TgtCurrencyCurrDesc:str = obj["TgtCurrencyCurrDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConsTgtGenRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calculated sequence number not inteneded for external use.  """  
      self.ConsDefID:str = obj["ConsDefID"]
      """  Unique identifer for the consolidation definition  """  
      self.Description:str = obj["Description"]
      """  Generation Description  """  
      self.GenStatus:str = obj["GenStatus"]
      """  Indicates the current status of the generation.  O = Open generation and consolidation have not occurred.  G =  Generated.  PI = Posted to the Intermediate book.  P = consolidated and Posted to the target.  """  
      self.TgtCompany:str = obj["TgtCompany"]
      """  Target Company Identifier.  """  
      self.TgtBook:str = obj["TgtBook"]
      """  Unique Book Identifier  This is the book the source book is consolidated to.  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  """  
      self.IntermediateBookID:str = obj["IntermediateBookID"]
      """  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  """  
      self.ImmediateTrans:bool = obj["ImmediateTrans"]
      """  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RemoteParent:bool = obj["RemoteParent"]
      """  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  """  
      self.VantageDB:bool = obj["VantageDB"]
      """  Used to notify the consolidation routine whether or not the Parent company is running an Epicor database.  """  
      self.OutputFile:str = obj["OutputFile"]
      """  Import/Export file name.  """  
      self.RemoteAcct:str = obj["RemoteAcct"]
      """  The free form Diff on Exchange Acct for a Remote Parent that is not an Epicor Database  """  
      self.ConsolidationType:str = obj["ConsolidationType"]
      """   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  """  
      self.AdjustMode:str = obj["AdjustMode"]
      """   THIS IS RESERVED FOR FUTURE USE.

D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

F = Full Replacement.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EntryMode:str = obj["EntryMode"]
      """  Identifies the mode the record was added in.  C = Consolidation, R = Retrospective Adjustment  """  
      self.MasterCOA:bool = obj["MasterCOA"]
      """  Logical indicating if this COA is the Master COA.  """  
      self.LatestConsolidation:bool = obj["LatestConsolidation"]
      """  LatestConsolidation  """  
      self.ClosingPeriods:int = obj["ClosingPeriods"]
      """  Closing periods parameter defined in Consolidation definition.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ConsDefIDDescription:str = obj["ConsDefIDDescription"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.IntermediateBookIDDescription:str = obj["IntermediateBookIDDescription"]
      self.IntermediateBookIDCurrencyCode:str = obj["IntermediateBookIDCurrencyCode"]
      self.TargetCOADescription:str = obj["TargetCOADescription"]
      self.TgtBookCurrencyCode:str = obj["TgtBookCurrencyCode"]
      self.TgtBookDescription:str = obj["TgtBookDescription"]
      self.TgtCompanyName:str = obj["TgtCompanyName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConsTgtGenTempRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calculated sequence number not inteneded for external use.  """  
      self.ConsDefID:str = obj["ConsDefID"]
      """  Unique identifer for the consolidation definition  """  
      self.Description:str = obj["Description"]
      """  Generation Description  """  
      self.GenStatus:str = obj["GenStatus"]
      """  Indicates the current status of the generation.  O = Open generation and consolidation have not occurred.  G =  Generated.  PI = Posted to the Intermediate book.  P = consolidated and Posted to the target.  """  
      self.TgtCompany:str = obj["TgtCompany"]
      """  Target Company Identifier.  """  
      self.TgtBook:str = obj["TgtBook"]
      """  Unique Book Identifier  This is the book the source book is consolidated to.  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  Target Chart of Accounts.  Can only be entered when remote parent is set to true or when the source and target companies are not the same and the target book is null.  This must be a vlaid entry in the GLBCOA table.  """  
      self.IntermediateBookID:str = obj["IntermediateBookID"]
      """  Only available when 'Use Intermediate Book' equals true.  Must be a valid GLBook in the source company whose BookType = 2 (Consolidation).  The intermediate book must have the same COA and currency as the target book.  """  
      self.ImmediateTrans:bool = obj["ImmediateTrans"]
      """  Logical indicating if the data written to the intermediate book is automatically transferred to the target company.  If yes, the data is automatically transferred.  If not, the user has the opportunity to review the intermediate books and is responsible for submitting the process that transfers the data.  This option is only available when 'Use Intermediate Book' equals yes.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RemoteParent:bool = obj["RemoteParent"]
      """  Used to notify the consolidation routine whether or not the Parent company is in the same database as the subsidiary's data.  """  
      self.VantageDB:bool = obj["VantageDB"]
      """  Used to notify the consolidation routine whether or not the Parent company is running a Vantage database.  """  
      self.OutputFile:str = obj["OutputFile"]
      """  Import/Export file name.  """  
      self.RemoteAcct:str = obj["RemoteAcct"]
      """  The free form Diff on Exchange Acct for a Remote Parent that is not a Vantage Database  """  
      self.ConsolidationType:str = obj["ConsolidationType"]
      """   Identifies how data is consolidated.  P = Periodic.  C = Continuous.

Under Periodic Consolidation the GLPeriodBal records are consolidated and transmitted to the target company and book.  Under Continuous Consolidation the GLJrnDtl records are transmitted.  """  
      self.AdjustMode:str = obj["AdjustMode"]
      """   THIS IS RESERVED FOR FUTURE USE.

D = Delta Generation.  The difference between the existing ConsBookTrack amount and the newly calcualted amount is consolidated into the parent company.

F = Full Replacement.  The existing GLJrnDtl records are deleted and new ones are created for the current balance.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EntryMode:str = obj["EntryMode"]
      """  Identifies the mode the record was added in.  C = Consolidation, R = Retrospective Adjustment  """  
      self.MasterCOA:bool = obj["MasterCOA"]
      """  Logical indicating if this COA is the Master COA.  """  
      self.SourceBook:str = obj["SourceBook"]
      self.ScrBookDesc:str = obj["ScrBookDesc"]
      self.ConsNodeCaption:str = obj["ConsNodeCaption"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConsTgtSrcRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ConsDefID:str = obj["ConsDefID"]
      """  Unique identifer for the consolidation definition  """  
      self.SourceBook:str = obj["SourceBook"]
      """  Unique Book Identifier  This is the book that is being consolidated into a target book.  """  
      self.BalanceSheetDefType:str = obj["BalanceSheetDefType"]
      """  The related ConsType ID  """  
      self.IncomeStmtDefType:str = obj["IncomeStmtDefType"]
      """  The related ConsType ID  """  
      self.ClosingPeriods:int = obj["ClosingPeriods"]
      """  The number of closing periods to be processed during consolidation.  The default value is zero which indicates that closing periods are not consolidated.  """  
      self.ExcludeOpenPrds:bool = obj["ExcludeOpenPrds"]
      """  Applies to Periodic Consolidation only.  Logical indicating if open periods are excluded from consolidation.  If yes, any balance records written against a source book in a period that is still open is not sent to the target company.  If no, all balance records are sent.  Note: The fiscal calendar is defined on the GLBook table for the source company and book.  """  
      self.TgtJrnlCode:str = obj["TgtJrnlCode"]
      """  The journal code to use when posting the consolidation records in the target company book.  """  
      self.ReverseDBCR:bool = obj["ReverseDBCR"]
      """  This option is only avaialble when 'Use Intermediate Book' equals yes.  Indicates if debit and credit amounts are swapped before the data is transferred.  """  
      self.COAMapUID:int = obj["COAMapUID"]
      """  Accounting segments mapping ID to use when calling the mapping engine.  Must be a valid entry in the COAMap table.  This is NOT available when remote parent is set to true.  The source COA on the mapping record must be the same as the COA assigned to the source book.  If the source company equals the target company then the target COA on this mapping record must be the COA assigned to the target book.  """  
      self.IntermediateJrnlCode:str = obj["IntermediateJrnlCode"]
      """  Only available when 'Use Intermediate Book' equals yes.  This is the the journal code to use when posting consolidated entries to the intermediate book.  """  
      self.DiffOnExchangeAcct:str = obj["DiffOnExchangeAcct"]
      """  Account Number where rounding differences will be posted  """  
      self.DiffExSegValue1:str = obj["DiffExSegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.DiffExSegValue2:str = obj["DiffExSegValue2"]
      """  SegmentValue 2.  See COASegment segment number 1 for a description of this field.  """  
      self.DiffExSegValue3:str = obj["DiffExSegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.DiffExSegValue4:str = obj["DiffExSegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.DiffExSegValue5:str = obj["DiffExSegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.DiffExSegValue6:str = obj["DiffExSegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.DiffExSegValue7:str = obj["DiffExSegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.DiffExSegValue8:str = obj["DiffExSegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.DiffExSegValue9:str = obj["DiffExSegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.DiffExSegValue10:str = obj["DiffExSegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.DiffExSegValue11:str = obj["DiffExSegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.DiffExSegValue12:str = obj["DiffExSegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.DiffExSegValue13:str = obj["DiffExSegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.DiffExSegValue14:str = obj["DiffExSegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.DiffExSegValue15:str = obj["DiffExSegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.DiffExSegValue16:str = obj["DiffExSegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.DiffExSegValue17:str = obj["DiffExSegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.DiffExSegValue18:str = obj["DiffExSegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.DiffExSegValue19:str = obj["DiffExSegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.DiffExSegValue20:str = obj["DiffExSegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  Target COA - this field is intended for internal use  """  
      self.TargetCompany:str = obj["TargetCompany"]
      """  Target Company ID - intended for internal use  """  
      self.SourceCOA:str = obj["SourceCOA"]
      """  Source COA code  """  
      self.InterJrnlDesc:str = obj["InterJrnlDesc"]
      """  Intermediate Journal Code description.  This is either from the JrnlCode or GLBJrnCode table.  """  
      self.TgtJrnlCodeDesc:str = obj["TgtJrnlCodeDesc"]
      """  Target Journal Code description.  This is either from the JrnlCode or GLBJrnCode table.  """  
      self.CurrencyDesc:str = obj["CurrencyDesc"]
      """  Currency code description from either the Currency or GLBCurrency table.  """  
      self.SrcFiscalCalendar:str = obj["SrcFiscalCalendar"]
      """  Source book fiscal calendar.  """  
      self.DiffOnExchangeDesc:str = obj["DiffOnExchangeDesc"]
      """  Holds GLAccount description temporarily to provide extra information to the user.  """  
      self.IntermediateCOA:str = obj["IntermediateCOA"]
      """  Intermediate COA Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BalanceConsTypeDescription:str = obj["BalanceConsTypeDescription"]
      self.BalanceRateDescription:str = obj["BalanceRateDescription"]
      self.COAMapDisplayName:str = obj["COAMapDisplayName"]
      self.IncomeConsTypeDescription:str = obj["IncomeConsTypeDescription"]
      self.IncomeRateDescription:str = obj["IncomeRateDescription"]
      self.SrcBookDescription:str = obj["SrcBookDescription"]
      self.SrcBookCurrencyCode:str = obj["SrcBookCurrencyCode"]
      self.SrcCompanyName:str = obj["SrcCompanyName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtConsMonitorTableset:
   def __init__(self, obj):
      self.Company:list[Erp_Tablesets_CompanyRow] = obj["Company"]
      self.ConsTgtDef:list[Erp_Tablesets_ConsTgtDefRow] = obj["ConsTgtDef"]
      self.ConsTgtGen:list[Erp_Tablesets_ConsTgtGenRow] = obj["ConsTgtGen"]
      self.ConsSrcCtrl:list[Erp_Tablesets_ConsSrcCtrlRow] = obj["ConsSrcCtrl"]
      self.ConsSrcRates:list[Erp_Tablesets_ConsSrcRatesRow] = obj["ConsSrcRates"]
      self.ConsTgtSrc:list[Erp_Tablesets_ConsTgtSrcRow] = obj["ConsTgtSrc"]
      self.ConsTgtGenTemp:list[Erp_Tablesets_ConsTgtGenTempRow] = obj["ConsTgtGenTemp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConsMonitorTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ConsMonitorTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ConsMonitorTableset] = obj["returnObj"]
      pass

class GetDefinitionMonitor_input:
   """ Required : 
   ipConsDefID
   ipTgtBook
   ipTgtBookStartDate
   ipTgtBookEndDate
   """  
   def __init__(self, obj):
      self.ipConsDefID:str = obj["ipConsDefID"]
      self.ipTgtBook:str = obj["ipTgtBook"]
      self.ipTgtBookStartDate:str = obj["ipTgtBookStartDate"]
      self.ipTgtBookEndDate:str = obj["ipTgtBookEndDate"]
      pass

class GetDefinitionMonitor_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConsMonitorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_ConsMonitorListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCompany_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConsMonitorTableset] = obj["ds"]
      pass

class GetNewCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsMonitorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewConsSrcCtrl_input:
   """ Required : 
   ds
   genID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConsMonitorTableset] = obj["ds"]
      self.genID:int = obj["genID"]
      pass

class GetNewConsSrcCtrl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsMonitorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewConsSrcRates_input:
   """ Required : 
   ds
   genID
   sourceBook
   fiscalYear
   fiscalYearSuffix
   fiscalPeriod
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConsMonitorTableset] = obj["ds"]
      self.genID:int = obj["genID"]
      self.sourceBook:str = obj["sourceBook"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.fiscalPeriod:int = obj["fiscalPeriod"]
      pass

class GetNewConsSrcRates_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsMonitorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewConsTgtDef_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConsMonitorTableset] = obj["ds"]
      pass

class GetNewConsTgtDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsMonitorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewConsTgtGen_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConsMonitorTableset] = obj["ds"]
      pass

class GetNewConsTgtGen_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsMonitorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewConsTgtSrc_input:
   """ Required : 
   ds
   consDefID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConsMonitorTableset] = obj["ds"]
      self.consDefID:str = obj["consDefID"]
      pass

class GetNewConsTgtSrc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsMonitorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsMonitor_input:
   """ Required : 
   ipTgtBook
   ipTgtBookStartDate
   ipTgtBookEndDate
   """  
   def __init__(self, obj):
      self.ipTgtBook:str = obj["ipTgtBook"]
      self.ipTgtBookStartDate:str = obj["ipTgtBookStartDate"]
      self.ipTgtBookEndDate:str = obj["ipTgtBookEndDate"]
      pass

class GetRowsMonitor_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConsMonitorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCompany
   whereClauseConsTgtDef
   whereClauseConsTgtGen
   whereClauseConsSrcCtrl
   whereClauseConsSrcRates
   whereClauseConsTgtSrc
   whereClauseConsTgtGenTemp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCompany:str = obj["whereClauseCompany"]
      self.whereClauseConsTgtDef:str = obj["whereClauseConsTgtDef"]
      self.whereClauseConsTgtGen:str = obj["whereClauseConsTgtGen"]
      self.whereClauseConsSrcCtrl:str = obj["whereClauseConsSrcCtrl"]
      self.whereClauseConsSrcRates:str = obj["whereClauseConsSrcRates"]
      self.whereClauseConsTgtSrc:str = obj["whereClauseConsTgtSrc"]
      self.whereClauseConsTgtGenTemp:str = obj["whereClauseConsTgtGenTemp"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConsMonitorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSelectDefaultsWithCalendarID_input:
   """ Required : 
   opBookID
   """  
   def __init__(self, obj):
      self.opBookID:str = obj["opBookID"]
      pass

class GetSelectDefaultsWithCalendarID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ouFiscalYear:int = obj["parameters"]
      self.ouFiscalPeriod:int = obj["parameters"]
      self.ouFiscalYearSuffix:str = obj["parameters"]
      self.ouPeriodStart:str = obj["parameters"]
      self.ouPeriodEnd:str = obj["parameters"]
      self.fiscalCalendarID:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetSelectDefaults_input:
   """ Required : 
   opBookID
   """  
   def __init__(self, obj):
      self.opBookID:str = obj["opBookID"]
      pass

class GetSelectDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ouFiscalYear:int = obj["parameters"]
      self.ouFiscalPeriod:int = obj["parameters"]
      self.ouFiscalYearSuffix:str = obj["parameters"]
      self.ouPeriodStart:str = obj["parameters"]
      self.ouPeriodEnd:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetSelectYearDefaultsWithCalendarID_input:
   """ Required : 
   opBookID
   ouFiscalYear
   """  
   def __init__(self, obj):
      self.opBookID:str = obj["opBookID"]
      self.ouFiscalYear:int = obj["ouFiscalYear"]
      pass

class GetSelectYearDefaultsWithCalendarID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ouFiscalPeriod:int = obj["parameters"]
      self.ouFiscalYearSuffix:str = obj["parameters"]
      self.ouPeriodStart:str = obj["parameters"]
      self.ouPeriodEnd:str = obj["parameters"]
      self.fiscalCalendarID:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetSelectYearSuffixDefaultsWithCalendarID_input:
   """ Required : 
   opBookID
   ouFiscalYear
   ouFiscalYearSuffix
   """  
   def __init__(self, obj):
      self.opBookID:str = obj["opBookID"]
      self.ouFiscalYear:int = obj["ouFiscalYear"]
      self.ouFiscalYearSuffix:str = obj["ouFiscalYearSuffix"]
      pass

class GetSelectYearSuffixDefaultsWithCalendarID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ouFiscalPeriod:int = obj["parameters"]
      self.ouPeriodStart:str = obj["parameters"]
      self.ouPeriodEnd:str = obj["parameters"]
      self.fiscalCalendarID:str = obj["parameters"]
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

class OnChangeSelectFiscalInfo_input:
   """ Required : 
   ipBookID
   ipFiscalYear
   ipFiscalYearSuffix
   ipFiscalPeriod
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      self.ipFiscalPeriod:int = obj["ipFiscalPeriod"]
      pass

class OnChangeSelectFiscalInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPeriodStartDate:str = obj["parameters"]
      self.opPeriodEndDate:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtConsMonitorTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtConsMonitorTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConsMonitorTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsMonitorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateSelectFiscalInfo_input:
   """ Required : 
   ipBookID
   ipFiscalYear
   ipFiscalYearSuffix
   ipFiscalPeriod
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      self.ipFiscalPeriod:int = obj["ipFiscalPeriod"]
      pass

class ValidateSelectFiscalInfo_output:
   def __init__(self, obj):
      pass

class ValidateSelectFiscalYearInfo_input:
   """ Required : 
   ipBookID
   ipFiscalYear
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      pass

class ValidateSelectFiscalYearInfo_output:
   def __init__(self, obj):
      pass

class ValidateSelectFiscalYearSuffixInfo_input:
   """ Required : 
   ipBookID
   ipFiscalYear
   ipFiscalYearSuffix
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      pass

class ValidateSelectFiscalYearSuffixInfo_output:
   def __init__(self, obj):
      pass

class ValidateTargetBook_input:
   """ Required : 
   ipBookID
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      pass

class ValidateTargetBook_output:
   def __init__(self, obj):
      pass

