import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ProdCalSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ProdCals(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ProdCals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ProdCals
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProdCalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals",headers=creds) as resp:
           return await resp.json()

async def post_ProdCals(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ProdCals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ProdCalRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ProdCalRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ProdCals_Company_CalendarID(Company, CalendarID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ProdCal item
   Description: Calls GetByID to retrieve the ProdCal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProdCal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ProdCalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals(" + Company + "," + CalendarID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ProdCals_Company_CalendarID(Company, CalendarID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ProdCal for the service
   Description: Calls UpdateExt to update ProdCal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ProdCal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ProdCalRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals(" + Company + "," + CalendarID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ProdCals_Company_CalendarID(Company, CalendarID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ProdCal item
   Description: Call UpdateExt to delete ProdCal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ProdCal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals(" + Company + "," + CalendarID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ProdCals_Company_CalendarID_ProdCalDays(Company, CalendarID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ProdCalDays items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ProdCalDays1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProdCalDayRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals(" + Company + "," + CalendarID + ")/ProdCalDays",headers=creds) as resp:
           return await resp.json()

async def get_ProdCals_Company_CalendarID_ProdCalDays_Company_CalendarID_ModifiedDay(Company, CalendarID, ModifiedDay, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ProdCalDay item
   Description: Calls GetByID to retrieve the ProdCalDay item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProdCalDay1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param ModifiedDay: Desc: ModifiedDay   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ProdCalDayRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals(" + Company + "," + CalendarID + ")/ProdCalDays(" + Company + "," + CalendarID + "," + ModifiedDay + ")",headers=creds) as resp:
           return await resp.json()

async def get_ProdCals_Company_CalendarID_ProdCalPlantLists(Company, CalendarID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ProdCalPlantLists items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ProdCalPlantLists1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProdCalPlantListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals(" + Company + "," + CalendarID + ")/ProdCalPlantLists",headers=creds) as resp:
           return await resp.json()

async def get_ProdCals_Company_CalendarID_ProdCalPlantLists_Company_CalendarID_Plant(Company, CalendarID, Plant, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ProdCalPlantList item
   Description: Calls GetByID to retrieve the ProdCalPlantList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProdCalPlantList1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ProdCalPlantListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals(" + Company + "," + CalendarID + ")/ProdCalPlantLists(" + Company + "," + CalendarID + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def get_ProdCals_Company_CalendarID_ProdCalRsrcLists(Company, CalendarID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ProdCalRsrcLists items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ProdCalRsrcLists1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProdCalRsrcListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals(" + Company + "," + CalendarID + ")/ProdCalRsrcLists",headers=creds) as resp:
           return await resp.json()

async def get_ProdCals_Company_CalendarID_ProdCalRsrcLists_Company_CalendarID_ResourceGrpID_ResourceID(Company, CalendarID, ResourceGrpID, ResourceID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ProdCalRsrcList item
   Description: Calls GetByID to retrieve the ProdCalRsrcList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProdCalRsrcList1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ProdCalRsrcListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals(" + Company + "," + CalendarID + ")/ProdCalRsrcLists(" + Company + "," + CalendarID + "," + ResourceGrpID + "," + ResourceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ProdCals_Company_CalendarID_ProdCalVendLists(Company, CalendarID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ProdCalVendLists items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ProdCalVendLists1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProdCalVendListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals(" + Company + "," + CalendarID + ")/ProdCalVendLists",headers=creds) as resp:
           return await resp.json()

async def get_ProdCals_Company_CalendarID_ProdCalVendLists_Company_CalendarID_VendorID(Company, CalendarID, VendorID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ProdCalVendList item
   Description: Calls GetByID to retrieve the ProdCalVendList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProdCalVendList1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param VendorID: Desc: VendorID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ProdCalVendListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals(" + Company + "," + CalendarID + ")/ProdCalVendLists(" + Company + "," + CalendarID + "," + VendorID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ProdCalDays(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ProdCalDays items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ProdCalDays
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProdCalDayRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalDays",headers=creds) as resp:
           return await resp.json()

async def post_ProdCalDays(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ProdCalDays
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ProdCalDayRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ProdCalDayRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalDays", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ProdCalDays_Company_CalendarID_ModifiedDay(Company, CalendarID, ModifiedDay, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ProdCalDay item
   Description: Calls GetByID to retrieve the ProdCalDay item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProdCalDay
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param ModifiedDay: Desc: ModifiedDay   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ProdCalDayRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalDays(" + Company + "," + CalendarID + "," + ModifiedDay + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ProdCalDays_Company_CalendarID_ModifiedDay(Company, CalendarID, ModifiedDay, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ProdCalDay for the service
   Description: Calls UpdateExt to update ProdCalDay. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ProdCalDay
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param ModifiedDay: Desc: ModifiedDay   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ProdCalDayRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalDays(" + Company + "," + CalendarID + "," + ModifiedDay + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ProdCalDays_Company_CalendarID_ModifiedDay(Company, CalendarID, ModifiedDay, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ProdCalDay item
   Description: Call UpdateExt to delete ProdCalDay item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ProdCalDay
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param ModifiedDay: Desc: ModifiedDay   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalDays(" + Company + "," + CalendarID + "," + ModifiedDay + ")",headers=creds) as resp:
           return await resp.json()

async def get_ProdCalPlantLists(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ProdCalPlantLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ProdCalPlantLists
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProdCalPlantListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalPlantLists",headers=creds) as resp:
           return await resp.json()

async def post_ProdCalPlantLists(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ProdCalPlantLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ProdCalPlantListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ProdCalPlantListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalPlantLists", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ProdCalPlantLists_Company_CalendarID_Plant(Company, CalendarID, Plant, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ProdCalPlantList item
   Description: Calls GetByID to retrieve the ProdCalPlantList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProdCalPlantList
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ProdCalPlantListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalPlantLists(" + Company + "," + CalendarID + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ProdCalPlantLists_Company_CalendarID_Plant(Company, CalendarID, Plant, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ProdCalPlantList for the service
   Description: Calls UpdateExt to update ProdCalPlantList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ProdCalPlantList
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ProdCalPlantListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalPlantLists(" + Company + "," + CalendarID + "," + Plant + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ProdCalPlantLists_Company_CalendarID_Plant(Company, CalendarID, Plant, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ProdCalPlantList item
   Description: Call UpdateExt to delete ProdCalPlantList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ProdCalPlantList
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalPlantLists(" + Company + "," + CalendarID + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def get_ProdCalRsrcLists(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ProdCalRsrcLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ProdCalRsrcLists
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProdCalRsrcListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalRsrcLists",headers=creds) as resp:
           return await resp.json()

async def post_ProdCalRsrcLists(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ProdCalRsrcLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ProdCalRsrcListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ProdCalRsrcListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalRsrcLists", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ProdCalRsrcLists_Company_CalendarID_ResourceGrpID_ResourceID(Company, CalendarID, ResourceGrpID, ResourceID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ProdCalRsrcList item
   Description: Calls GetByID to retrieve the ProdCalRsrcList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProdCalRsrcList
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ProdCalRsrcListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalRsrcLists(" + Company + "," + CalendarID + "," + ResourceGrpID + "," + ResourceID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ProdCalRsrcLists_Company_CalendarID_ResourceGrpID_ResourceID(Company, CalendarID, ResourceGrpID, ResourceID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ProdCalRsrcList for the service
   Description: Calls UpdateExt to update ProdCalRsrcList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ProdCalRsrcList
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
      :param ResourceID: Desc: ResourceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ProdCalRsrcListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalRsrcLists(" + Company + "," + CalendarID + "," + ResourceGrpID + "," + ResourceID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ProdCalRsrcLists_Company_CalendarID_ResourceGrpID_ResourceID(Company, CalendarID, ResourceGrpID, ResourceID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ProdCalRsrcList item
   Description: Call UpdateExt to delete ProdCalRsrcList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ProdCalRsrcList
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param ResourceGrpID: Desc: ResourceGrpID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalRsrcLists(" + Company + "," + CalendarID + "," + ResourceGrpID + "," + ResourceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ProdCalVendLists(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ProdCalVendLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ProdCalVendLists
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProdCalVendListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalVendLists",headers=creds) as resp:
           return await resp.json()

async def post_ProdCalVendLists(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ProdCalVendLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ProdCalVendListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ProdCalVendListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalVendLists", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ProdCalVendLists_Company_CalendarID_VendorID(Company, CalendarID, VendorID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ProdCalVendList item
   Description: Calls GetByID to retrieve the ProdCalVendList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProdCalVendList
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param VendorID: Desc: VendorID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ProdCalVendListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalVendLists(" + Company + "," + CalendarID + "," + VendorID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ProdCalVendLists_Company_CalendarID_VendorID(Company, CalendarID, VendorID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ProdCalVendList for the service
   Description: Calls UpdateExt to update ProdCalVendList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ProdCalVendList
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param VendorID: Desc: VendorID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ProdCalVendListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalVendLists(" + Company + "," + CalendarID + "," + VendorID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ProdCalVendLists_Company_CalendarID_VendorID(Company, CalendarID, VendorID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ProdCalVendList item
   Description: Call UpdateExt to delete ProdCalVendList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ProdCalVendList
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CalendarID: Desc: CalendarID   Required: True   Allow empty value : True
      :param VendorID: Desc: VendorID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalVendLists(" + Company + "," + CalendarID + "," + VendorID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProdCalListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseProdCal, whereClauseProdCalDay, whereClauseProdCalPlantList, whereClauseProdCalRsrcList, whereClauseProdCalVendList, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseProdCal=" + whereClauseProdCal
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseProdCalDay=" + whereClauseProdCalDay
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseProdCalPlantList=" + whereClauseProdCalPlantList
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseProdCalRsrcList=" + whereClauseProdCalRsrcList
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseProdCalVendList=" + whereClauseProdCalVendList
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(calendarID, epicorHeaders = None):
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
   params += "calendarID=" + calendarID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CustomizeDay(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CustomizeDay
   Description: Call this method to specify a special working day or non working day.
When this method is called, if a ProdCalDay record exists it will be deleted
(undo the special working or non working day).  If a ProdCalDay record doesn't
exist, it will create a ProdCalDay record.  If the date specified is a normal
working day, then the WorkingDay field will be set to false and the capacity
is set to 0.  If the date specified is not a normal working day, then the
WorkingDay field will be set to true and the ProdHour fields will be set to
true depending on the number of ProdCal.HoursPerDay (example: If the ProdCal.HoursPerDay
is 8 then ProdHour 1 through 8 would be set to true) and the capacity for the
working day is set equal to the ProdCal.HoursPerDay.
   OperationID: CustomizeDay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CustomizeDay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomizeDay_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DecideReadOnlyFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DecideReadOnlyFields
   Description: Decides if start processReadOnlyFieldsor not
   OperationID: DecideReadOnlyFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DecideReadOnlyFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DecideReadOnlyFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DuplicateCalendar(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DuplicateCalendar
   Description: This duplicates the production calendar for calendar ID.
   OperationID: DuplicateCalendar
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateCalendar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateCalendar_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPlantCalendar(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPlantCalendar
   Description: This method gets the plant calendar.
   OperationID: GetPlantCalendar
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPlantCalendar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPlantCalendar_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetResourceList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetResourceList
   Description: Used for the Resources/Where Used button.
This method will get list of all resources, resource groups,
vendors, and plants associated with the specified production calendar and
creates tables ttProdCalRsrcList, ttProdCalVendList, and ttProdCalPlantList.
   OperationID: GetResourceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetResourceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetResourceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsWorkDay(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsWorkDay
   Description: Returns if a selected date is a work day
   OperationID: IsWorkDay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsWorkDay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsWorkDay_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateHoursSelected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateHoursSelected
   Description: Updates hours selected per day when the calendar hours per day is changed
   OperationID: UpdateHoursSelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateHoursSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateHoursSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeProdCalHoursPerDayHour(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeProdCalHoursPerDayHour
   Description: Calculates DayHours when an hour is toggled on or off
   OperationID: ChangeProdCalHoursPerDayHour
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeProdCalHoursPerDayHour_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeProdCalHoursPerDayHour_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeProdCalHoursPerDaySelectRow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeProdCalHoursPerDaySelectRow
   Description: Updates hours on a row when SelectRow is checked or unchecked
   OperationID: ChangeProdCalHoursPerDaySelectRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeProdCalHoursPerDaySelectRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeProdCalHoursPerDaySelectRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateProdCalHours(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateProdCalHours
   Description: Updates ProdCal Hour fields with selections from ProdCalHoursPerDay
   OperationID: UpdateProdCalHours
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateProdCalHours_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateProdCalHours_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetProdCalHoursPerDay(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetProdCalHoursPerDay
   Description: Returns the ProdCalHoursPerDay dataset
   OperationID: GetProdCalHoursPerDay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetProdCalHoursPerDay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetProdCalHoursPerDay_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateWeekRangeStartingDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateWeekRangeStartingDate
   Description: Validate starting date for adding a week range
   OperationID: ValidateWeekRangeStartingDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateWeekRangeStartingDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateWeekRangeStartingDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateWeekRangeStartingWeek(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateWeekRangeStartingWeek
   Description: Validate starting week number when adding a week range
   OperationID: ValidateWeekRangeStartingWeek
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateWeekRangeStartingWeek_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateWeekRangeStartingWeek_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateWeekRangeNumberOfWeeks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateWeekRangeNumberOfWeeks
   Description: Validate number of weeks when adding a week range
   OperationID: ValidateWeekRangeNumberOfWeeks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateWeekRangeNumberOfWeeks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateWeekRangeNumberOfWeeks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewProdCal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewProdCal
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewProdCal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewProdCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewProdCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewProdCalDay(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewProdCalDay
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewProdCalDay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewProdCalDay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewProdCalDay_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalDayRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ProdCalDayRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ProdCalListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalPlantListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ProdCalPlantListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ProdCalRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalRsrcListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ProdCalRsrcListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalVendListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ProdCalVendListRow] = obj["value"]
      pass

class Erp_Tablesets_ProdCalDayRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CalendarID:str = obj["CalendarID"]
      """   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  """  
      self.ModifiedDay:str = obj["ModifiedDay"]
      """  The date that will have hours that do not conform with the hours for the associated ProdCal.  """  
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
      self.WorkingDay:bool = obj["WorkingDay"]
      """  If this is set to NO, then record is being used to identify a non-working day.  The ProdHour field is not used for non-working days.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExceptionLabel:str = obj["ExceptionLabel"]
      """  ExceptionLabel  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CalendarIDDescription:str = obj["CalendarIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProdCalListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CalendarID:str = obj["CalendarID"]
      """   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  """  
      self.Description:str = obj["Description"]
      """  Calendar description.  """  
      self.WorkWeek1:bool = obj["WorkWeek1"]
      """  WorkWeek1  """  
      self.WorkWeek2:bool = obj["WorkWeek2"]
      """  WorkWeek2  """  
      self.WorkWeek3:bool = obj["WorkWeek3"]
      """  WorkWeek3  """  
      self.WorkWeek4:bool = obj["WorkWeek4"]
      """  WorkWeek4  """  
      self.WorkWeek5:bool = obj["WorkWeek5"]
      """  WorkWeek5  """  
      self.WorkWeek6:bool = obj["WorkWeek6"]
      """  WorkWeek6  """  
      self.WorkWeek7:bool = obj["WorkWeek7"]
      """  WorkWeek7  """  
      self.ReloadStatus:str = obj["ReloadStatus"]
      """  A  recovery flag which indicates the status of the "Reload" process when the calendar is changed.  Values; Blank or "Started". (See WrkCenter.ReloadStatus, WrkCenter.ReloadNum)  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProdCalPlantListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Plant:str = obj["Plant"]
      self.PlantName:str = obj["PlantName"]
      self.CalendarID:str = obj["CalendarID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProdCalRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CalendarID:str = obj["CalendarID"]
      """   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  """  
      self.Description:str = obj["Description"]
      """  Calendar description.  """  
      self.WorkWeek1:bool = obj["WorkWeek1"]
      """  WorkWeek1  """  
      self.WorkWeek2:bool = obj["WorkWeek2"]
      """  WorkWeek2  """  
      self.WorkWeek3:bool = obj["WorkWeek3"]
      """  WorkWeek3  """  
      self.WorkWeek4:bool = obj["WorkWeek4"]
      """  WorkWeek4  """  
      self.WorkWeek5:bool = obj["WorkWeek5"]
      """  WorkWeek5  """  
      self.WorkWeek6:bool = obj["WorkWeek6"]
      """  WorkWeek6  """  
      self.WorkWeek7:bool = obj["WorkWeek7"]
      """  WorkWeek7  """  
      self.ReloadStatus:str = obj["ReloadStatus"]
      """  A  recovery flag which indicates the status of the "Reload" process when the calendar is changed.  Values; Blank or "Started". (See WrkCenter.ReloadStatus, WrkCenter.ReloadNum)  """  
      self.Hour001:bool = obj["Hour001"]
      """  Hour001  """  
      self.Hour002:bool = obj["Hour002"]
      """  Hour002  """  
      self.Hour003:bool = obj["Hour003"]
      """  Hour003  """  
      self.Hour004:bool = obj["Hour004"]
      """  Hour004  """  
      self.Hour005:bool = obj["Hour005"]
      """  Hour005  """  
      self.Hour006:bool = obj["Hour006"]
      """  Hour006  """  
      self.Hour007:bool = obj["Hour007"]
      """  Hour007  """  
      self.Hour008:bool = obj["Hour008"]
      """  Hour008  """  
      self.Hour009:bool = obj["Hour009"]
      """  Hour009  """  
      self.Hour010:bool = obj["Hour010"]
      """  Hour010  """  
      self.Hour011:bool = obj["Hour011"]
      """  Hour011  """  
      self.Hour012:bool = obj["Hour012"]
      """  Hour012  """  
      self.Hour013:bool = obj["Hour013"]
      """  Hour013  """  
      self.Hour014:bool = obj["Hour014"]
      """  Hour014  """  
      self.Hour015:bool = obj["Hour015"]
      """  Hour015  """  
      self.Hour016:bool = obj["Hour016"]
      """  Hour016  """  
      self.Hour017:bool = obj["Hour017"]
      """  Hour017  """  
      self.Hour018:bool = obj["Hour018"]
      """  Hour018  """  
      self.Hour019:bool = obj["Hour019"]
      """  Hour019  """  
      self.Hour020:bool = obj["Hour020"]
      """  Hour020  """  
      self.Hour021:bool = obj["Hour021"]
      """  Hour021  """  
      self.Hour022:bool = obj["Hour022"]
      """  Hour022  """  
      self.Hour023:bool = obj["Hour023"]
      """  Hour023  """  
      self.Hour024:bool = obj["Hour024"]
      """  Hour024  """  
      self.Hour025:bool = obj["Hour025"]
      """  Hour025  """  
      self.Hour026:bool = obj["Hour026"]
      """  Hour026  """  
      self.Hour027:bool = obj["Hour027"]
      """  Hour027  """  
      self.Hour028:bool = obj["Hour028"]
      """  Hour028  """  
      self.Hour029:bool = obj["Hour029"]
      """  Hour029  """  
      self.Hour030:bool = obj["Hour030"]
      """  Hour030  """  
      self.Hour031:bool = obj["Hour031"]
      """  Hour031  """  
      self.Hour032:bool = obj["Hour032"]
      """  Hour032  """  
      self.Hour033:bool = obj["Hour033"]
      """  Hour033  """  
      self.Hour034:bool = obj["Hour034"]
      """  Hour034  """  
      self.Hour035:bool = obj["Hour035"]
      """  Hour035  """  
      self.Hour036:bool = obj["Hour036"]
      """  Hour036  """  
      self.Hour037:bool = obj["Hour037"]
      """  Hour037  """  
      self.Hour038:bool = obj["Hour038"]
      """  Hour038  """  
      self.Hour039:bool = obj["Hour039"]
      """  Hour039  """  
      self.Hour040:bool = obj["Hour040"]
      """  Hour040  """  
      self.Hour041:bool = obj["Hour041"]
      """  Hour041  """  
      self.Hour042:bool = obj["Hour042"]
      """  Hour042  """  
      self.Hour043:bool = obj["Hour043"]
      """  Hour043  """  
      self.Hour044:bool = obj["Hour044"]
      """  Hour044  """  
      self.Hour045:bool = obj["Hour045"]
      """  Hour045  """  
      self.Hour046:bool = obj["Hour046"]
      """  Hour046  """  
      self.Hour047:bool = obj["Hour047"]
      """  Hour047  """  
      self.Hour048:bool = obj["Hour048"]
      """  Hour048  """  
      self.Hour049:bool = obj["Hour049"]
      """  Hour049  """  
      self.Hour050:bool = obj["Hour050"]
      """  Hour050  """  
      self.Hour051:bool = obj["Hour051"]
      """  Hour051  """  
      self.Hour052:bool = obj["Hour052"]
      """  Hour052  """  
      self.Hour053:bool = obj["Hour053"]
      """  Hour053  """  
      self.Hour054:bool = obj["Hour054"]
      """  Hour054  """  
      self.Hour055:bool = obj["Hour055"]
      """  Hour055  """  
      self.Hour056:bool = obj["Hour056"]
      """  Hour056  """  
      self.Hour057:bool = obj["Hour057"]
      """  Hour057  """  
      self.Hour058:bool = obj["Hour058"]
      """  Hour058  """  
      self.Hour059:bool = obj["Hour059"]
      """  Hour059  """  
      self.Hour060:bool = obj["Hour060"]
      """  Hour060  """  
      self.Hour061:bool = obj["Hour061"]
      """  Hour061  """  
      self.Hour062:bool = obj["Hour062"]
      """  Hour062  """  
      self.Hour063:bool = obj["Hour063"]
      """  Hour063  """  
      self.Hour064:bool = obj["Hour064"]
      """  Hour064  """  
      self.Hour065:bool = obj["Hour065"]
      """  Hour065  """  
      self.Hour066:bool = obj["Hour066"]
      """  Hour066  """  
      self.Hour067:bool = obj["Hour067"]
      """  Hour067  """  
      self.Hour068:bool = obj["Hour068"]
      """  Hour068  """  
      self.Hour069:bool = obj["Hour069"]
      """  Hour069  """  
      self.Hour070:bool = obj["Hour070"]
      """  Hour070  """  
      self.Hour071:bool = obj["Hour071"]
      """  Hour071  """  
      self.Hour072:bool = obj["Hour072"]
      """  Hour072  """  
      self.Hour073:bool = obj["Hour073"]
      """  Hour073  """  
      self.Hour074:bool = obj["Hour074"]
      """  Hour074  """  
      self.Hour075:bool = obj["Hour075"]
      """  Hour075  """  
      self.Hour076:bool = obj["Hour076"]
      """  Hour076  """  
      self.Hour077:bool = obj["Hour077"]
      """  Hour077  """  
      self.Hour078:bool = obj["Hour078"]
      """  Hour078  """  
      self.Hour079:bool = obj["Hour079"]
      """  Hour079  """  
      self.Hour080:bool = obj["Hour080"]
      """  Hour080  """  
      self.Hour081:bool = obj["Hour081"]
      """  Hour081  """  
      self.Hour082:bool = obj["Hour082"]
      """  Hour082  """  
      self.Hour083:bool = obj["Hour083"]
      """  Hour083  """  
      self.Hour084:bool = obj["Hour084"]
      """  Hour084  """  
      self.Hour085:bool = obj["Hour085"]
      """  Hour085  """  
      self.Hour086:bool = obj["Hour086"]
      """  Hour086  """  
      self.Hour087:bool = obj["Hour087"]
      """  Hour087  """  
      self.Hour088:bool = obj["Hour088"]
      """  Hour088  """  
      self.Hour089:bool = obj["Hour089"]
      """  Hour089  """  
      self.Hour090:bool = obj["Hour090"]
      """  Hour090  """  
      self.Hour091:bool = obj["Hour091"]
      """  Hour091  """  
      self.Hour092:bool = obj["Hour092"]
      """  Hour092  """  
      self.Hour093:bool = obj["Hour093"]
      """  Hour093  """  
      self.Hour094:bool = obj["Hour094"]
      """  Hour094  """  
      self.Hour095:bool = obj["Hour095"]
      """  Hour095  """  
      self.Hour096:bool = obj["Hour096"]
      """  Hour096  """  
      self.Hour097:bool = obj["Hour097"]
      """  Hour097  """  
      self.Hour098:bool = obj["Hour098"]
      """  Hour098  """  
      self.Hour099:bool = obj["Hour099"]
      """  Hour099  """  
      self.Hour100:bool = obj["Hour100"]
      """  Hour100  """  
      self.Hour101:bool = obj["Hour101"]
      """  Hour101  """  
      self.Hour102:bool = obj["Hour102"]
      """  Hour102  """  
      self.Hour103:bool = obj["Hour103"]
      """  Hour103  """  
      self.Hour104:bool = obj["Hour104"]
      """  Hour104  """  
      self.Hour105:bool = obj["Hour105"]
      """  Hour105  """  
      self.Hour106:bool = obj["Hour106"]
      """  Hour106  """  
      self.Hour107:bool = obj["Hour107"]
      """  Hour107  """  
      self.Hour108:bool = obj["Hour108"]
      """  Hour108  """  
      self.Hour109:bool = obj["Hour109"]
      """  Hour109  """  
      self.Hour110:bool = obj["Hour110"]
      """  Hour110  """  
      self.Hour111:bool = obj["Hour111"]
      """  Hour111  """  
      self.Hour112:bool = obj["Hour112"]
      """  Hour112  """  
      self.Hour113:bool = obj["Hour113"]
      """  Hour113  """  
      self.Hour114:bool = obj["Hour114"]
      """  Hour114  """  
      self.Hour115:bool = obj["Hour115"]
      """  Hour115  """  
      self.Hour116:bool = obj["Hour116"]
      """  Hour116  """  
      self.Hour117:bool = obj["Hour117"]
      """  Hour117  """  
      self.Hour118:bool = obj["Hour118"]
      """  Hour118  """  
      self.Hour119:bool = obj["Hour119"]
      """  Hour119  """  
      self.Hour120:bool = obj["Hour120"]
      """  Hour120  """  
      self.Hour121:bool = obj["Hour121"]
      """  Hour121  """  
      self.Hour122:bool = obj["Hour122"]
      """  Hour122  """  
      self.Hour123:bool = obj["Hour123"]
      """  Hour123  """  
      self.Hour124:bool = obj["Hour124"]
      """  Hour124  """  
      self.Hour125:bool = obj["Hour125"]
      """  Hour125  """  
      self.Hour126:bool = obj["Hour126"]
      """  Hour126  """  
      self.Hour127:bool = obj["Hour127"]
      """  Hour127  """  
      self.Hour128:bool = obj["Hour128"]
      """  Hour128  """  
      self.Hour129:bool = obj["Hour129"]
      """  Hour129  """  
      self.Hour130:bool = obj["Hour130"]
      """  Hour130  """  
      self.Hour131:bool = obj["Hour131"]
      """  Hour131  """  
      self.Hour132:bool = obj["Hour132"]
      """  Hour132  """  
      self.Hour133:bool = obj["Hour133"]
      """  Hour133  """  
      self.Hour134:bool = obj["Hour134"]
      """  Hour134  """  
      self.Hour135:bool = obj["Hour135"]
      """  Hour135  """  
      self.Hour136:bool = obj["Hour136"]
      """  Hour136  """  
      self.Hour137:bool = obj["Hour137"]
      """  Hour137  """  
      self.Hour138:bool = obj["Hour138"]
      """  Hour138  """  
      self.Hour139:bool = obj["Hour139"]
      """  Hour139  """  
      self.Hour140:bool = obj["Hour140"]
      """  Hour140  """  
      self.Hour141:bool = obj["Hour141"]
      """  Hour141  """  
      self.Hour142:bool = obj["Hour142"]
      """  Hour142  """  
      self.Hour143:bool = obj["Hour143"]
      """  Hour143  """  
      self.Hour144:bool = obj["Hour144"]
      """  Hour144  """  
      self.Hour145:bool = obj["Hour145"]
      """  Hour145  """  
      self.Hour146:bool = obj["Hour146"]
      """  Hour146  """  
      self.Hour147:bool = obj["Hour147"]
      """  Hour147  """  
      self.Hour148:bool = obj["Hour148"]
      """  Hour148  """  
      self.Hour149:bool = obj["Hour149"]
      """  Hour149  """  
      self.Hour150:bool = obj["Hour150"]
      """  Hour150  """  
      self.Hour151:bool = obj["Hour151"]
      """  Hour151  """  
      self.Hour152:bool = obj["Hour152"]
      """  Hour152  """  
      self.Hour153:bool = obj["Hour153"]
      """  Hour153  """  
      self.Hour154:bool = obj["Hour154"]
      """  Hour154  """  
      self.Hour155:bool = obj["Hour155"]
      """  Hour155  """  
      self.Hour156:bool = obj["Hour156"]
      """  Hour156  """  
      self.Hour157:bool = obj["Hour157"]
      """  Hour157  """  
      self.Hour158:bool = obj["Hour158"]
      """  Hour158  """  
      self.Hour159:bool = obj["Hour159"]
      """  Hour159  """  
      self.Hour160:bool = obj["Hour160"]
      """  Hour160  """  
      self.Hour161:bool = obj["Hour161"]
      """  Hour161  """  
      self.Hour162:bool = obj["Hour162"]
      """  Hour162  """  
      self.Hour163:bool = obj["Hour163"]
      """  Hour163  """  
      self.Hour164:bool = obj["Hour164"]
      """  Hour164  """  
      self.Hour165:bool = obj["Hour165"]
      """  Hour165  """  
      self.Hour166:bool = obj["Hour166"]
      """  Hour166  """  
      self.Hour167:bool = obj["Hour167"]
      """  Hour167  """  
      self.Hour168:bool = obj["Hour168"]
      """  Hour168  """  
      self.HoursPerDay:int = obj["HoursPerDay"]
      """  The Number of Hours that a single Resouce is available per day.  """  
      self.BeginWeekday:int = obj["BeginWeekday"]
      """  Day of the week on which the Production Calendar begins.  Values mirror the values returned by the Progress "weekday" function.  Valid values:  1 = Sunday, 2 = Monday, 3 = Tuesday, 4 = Wednesday, 5 = Thursday, 6 = Friday, 7 = Sunday.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NumberOfMachines:int = obj["NumberOfMachines"]
      """  Num of machines assigned to the workcenter  """  
      self.PlantCalendar:bool = obj["PlantCalendar"]
      self.ProposedCalendarID:str = obj["ProposedCalendarID"]
      self.ReadOnlyFields:str = obj["ReadOnlyFields"]
      """  Delimited list of read-only fields  """  
      self.StartTime1:int = obj["StartTime1"]
      self.StartTime2:int = obj["StartTime2"]
      self.StartTime3:int = obj["StartTime3"]
      self.StartTime4:int = obj["StartTime4"]
      self.StartTime5:int = obj["StartTime5"]
      self.StartTime6:int = obj["StartTime6"]
      self.StartTime7:int = obj["StartTime7"]
      self.EndTime1:int = obj["EndTime1"]
      self.EndTime2:int = obj["EndTime2"]
      self.EndTime3:int = obj["EndTime3"]
      self.EndTime4:int = obj["EndTime4"]
      self.EndTime5:int = obj["EndTime5"]
      self.EndTime6:int = obj["EndTime6"]
      self.EndTime7:int = obj["EndTime7"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProdCalRsrcListRow:
   def __init__(self, obj):
      self.ResourceID:str = obj["ResourceID"]
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      self.ResourceDescription:str = obj["ResourceDescription"]
      self.Company:str = obj["Company"]
      self.CalendarID:str = obj["CalendarID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProdCalVendListRow:
   def __init__(self, obj):
      self.VendorID:str = obj["VendorID"]
      """  Vendor ID  """  
      self.Company:str = obj["Company"]
      self.VendorName:str = obj["VendorName"]
      self.CalendarID:str = obj["CalendarID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeProdCalHoursPerDayHour_input:
   """ Required : 
   rowSeq
   columnChanged
   ds
   """  
   def __init__(self, obj):
      self.rowSeq:int = obj["rowSeq"]
      """  RowSeq value of the row that was modified  """  
      self.columnChanged:str = obj["columnChanged"]
      """  Name of the column that was changed  """  
      self.ds:list[Erp_Tablesets_ProdCalHoursPerDayTableset] = obj["ds"]
      pass

class ChangeProdCalHoursPerDayHour_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProdCalHoursPerDayTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeProdCalHoursPerDaySelectRow_input:
   """ Required : 
   rowSeq
   defaultHoursPerDay
   ds
   """  
   def __init__(self, obj):
      self.rowSeq:int = obj["rowSeq"]
      """  RowSeq value of the row that was modified  """  
      self.defaultHoursPerDay:int = obj["defaultHoursPerDay"]
      """  Default Hours Per Day for the calendar  """  
      self.ds:list[Erp_Tablesets_ProdCalHoursPerDayTableset] = obj["ds"]
      pass

class ChangeProdCalHoursPerDaySelectRow_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProdCalHoursPerDayTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CustomizeDay_input:
   """ Required : 
   cCalendarID
   daDate
   exceptionLabel
   ds
   """  
   def __init__(self, obj):
      self.cCalendarID:str = obj["cCalendarID"]
      """  cCalendar Descriptive Code  """  
      self.daDate:str = obj["daDate"]
      """  Modified date  """  
      self.exceptionLabel:str = obj["exceptionLabel"]
      """  Exception Label  """  
      self.ds:list[Erp_Tablesets_ProdCalTableset] = obj["ds"]
      pass

class CustomizeDay_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProdCalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DecideReadOnlyFields_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProdCalTableset] = obj["ds"]
      pass

class DecideReadOnlyFields_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProdCalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   calendarID
   """  
   def __init__(self, obj):
      self.calendarID:str = obj["calendarID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DuplicateCalendar_input:
   """ Required : 
   cOldCalendarID
   cNewCalendarID
   ds
   """  
   def __init__(self, obj):
      self.cOldCalendarID:str = obj["cOldCalendarID"]
      """  The Current Calendar ID.  """  
      self.cNewCalendarID:str = obj["cNewCalendarID"]
      """  Calendar ID of the new Calendar  """  
      self.ds:list[Erp_Tablesets_ProdCalTableset] = obj["ds"]
      pass

class DuplicateCalendar_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProdCalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_ProdCalDayRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CalendarID:str = obj["CalendarID"]
      """   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  """  
      self.ModifiedDay:str = obj["ModifiedDay"]
      """  The date that will have hours that do not conform with the hours for the associated ProdCal.  """  
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
      self.WorkingDay:bool = obj["WorkingDay"]
      """  If this is set to NO, then record is being used to identify a non-working day.  The ProdHour field is not used for non-working days.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExceptionLabel:str = obj["ExceptionLabel"]
      """  ExceptionLabel  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CalendarIDDescription:str = obj["CalendarIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProdCalHoursPerDayRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CalendarID:str = obj["CalendarID"]
      self.DayHours:int = obj["DayHours"]
      """  Number of hours selected for the week day  """  
      self.Hour01:bool = obj["Hour01"]
      """  Hour 1  """  
      self.Hour02:bool = obj["Hour02"]
      """  Hour 2  """  
      self.Hour03:bool = obj["Hour03"]
      self.Hour04:bool = obj["Hour04"]
      self.Hour05:bool = obj["Hour05"]
      self.Hour06:bool = obj["Hour06"]
      self.Hour07:bool = obj["Hour07"]
      """  Hour 7  """  
      self.Hour08:bool = obj["Hour08"]
      """  Hour 8  """  
      self.Hour09:bool = obj["Hour09"]
      self.Hour10:bool = obj["Hour10"]
      """  Hour 10  """  
      self.Hour11:bool = obj["Hour11"]
      """  Hour 11  """  
      self.Hour12:bool = obj["Hour12"]
      """  Hour 12  """  
      self.Hour13:bool = obj["Hour13"]
      """  Hour 13  """  
      self.Hour14:bool = obj["Hour14"]
      self.Hour15:bool = obj["Hour15"]
      """  Hour 15  """  
      self.Hour16:bool = obj["Hour16"]
      """  Hour 16  """  
      self.Hour17:bool = obj["Hour17"]
      """  Hour 17  """  
      self.Hour18:bool = obj["Hour18"]
      """  Hour 18  """  
      self.Hour19:bool = obj["Hour19"]
      """  Hour 19  """  
      self.Hour20:bool = obj["Hour20"]
      """  Hour 20  """  
      self.Hour21:bool = obj["Hour21"]
      """  Hour 21  """  
      self.Hour22:bool = obj["Hour22"]
      """  Hour 22  """  
      self.Hour23:bool = obj["Hour23"]
      """  Hour 23  """  
      self.Hour24:bool = obj["Hour24"]
      """  Hour 24  """  
      self.DayOfWeek:str = obj["DayOfWeek"]
      """  Day of the week the row represents, i.e. Monday, Tuesday, etc  """  
      self.RowSeq:int = obj["RowSeq"]
      """  Row Sequence  """  
      self.SelectRow:bool = obj["SelectRow"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProdCalHoursPerDayTableset:
   def __init__(self, obj):
      self.ProdCalHoursPerDay:list[Erp_Tablesets_ProdCalHoursPerDayRow] = obj["ProdCalHoursPerDay"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ProdCalListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CalendarID:str = obj["CalendarID"]
      """   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  """  
      self.Description:str = obj["Description"]
      """  Calendar description.  """  
      self.WorkWeek1:bool = obj["WorkWeek1"]
      """  WorkWeek1  """  
      self.WorkWeek2:bool = obj["WorkWeek2"]
      """  WorkWeek2  """  
      self.WorkWeek3:bool = obj["WorkWeek3"]
      """  WorkWeek3  """  
      self.WorkWeek4:bool = obj["WorkWeek4"]
      """  WorkWeek4  """  
      self.WorkWeek5:bool = obj["WorkWeek5"]
      """  WorkWeek5  """  
      self.WorkWeek6:bool = obj["WorkWeek6"]
      """  WorkWeek6  """  
      self.WorkWeek7:bool = obj["WorkWeek7"]
      """  WorkWeek7  """  
      self.ReloadStatus:str = obj["ReloadStatus"]
      """  A  recovery flag which indicates the status of the "Reload" process when the calendar is changed.  Values; Blank or "Started". (See WrkCenter.ReloadStatus, WrkCenter.ReloadNum)  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProdCalListTableset:
   def __init__(self, obj):
      self.ProdCalList:list[Erp_Tablesets_ProdCalListRow] = obj["ProdCalList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ProdCalPlantListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Plant:str = obj["Plant"]
      self.PlantName:str = obj["PlantName"]
      self.CalendarID:str = obj["CalendarID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProdCalRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CalendarID:str = obj["CalendarID"]
      """   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  """  
      self.Description:str = obj["Description"]
      """  Calendar description.  """  
      self.WorkWeek1:bool = obj["WorkWeek1"]
      """  WorkWeek1  """  
      self.WorkWeek2:bool = obj["WorkWeek2"]
      """  WorkWeek2  """  
      self.WorkWeek3:bool = obj["WorkWeek3"]
      """  WorkWeek3  """  
      self.WorkWeek4:bool = obj["WorkWeek4"]
      """  WorkWeek4  """  
      self.WorkWeek5:bool = obj["WorkWeek5"]
      """  WorkWeek5  """  
      self.WorkWeek6:bool = obj["WorkWeek6"]
      """  WorkWeek6  """  
      self.WorkWeek7:bool = obj["WorkWeek7"]
      """  WorkWeek7  """  
      self.ReloadStatus:str = obj["ReloadStatus"]
      """  A  recovery flag which indicates the status of the "Reload" process when the calendar is changed.  Values; Blank or "Started". (See WrkCenter.ReloadStatus, WrkCenter.ReloadNum)  """  
      self.Hour001:bool = obj["Hour001"]
      """  Hour001  """  
      self.Hour002:bool = obj["Hour002"]
      """  Hour002  """  
      self.Hour003:bool = obj["Hour003"]
      """  Hour003  """  
      self.Hour004:bool = obj["Hour004"]
      """  Hour004  """  
      self.Hour005:bool = obj["Hour005"]
      """  Hour005  """  
      self.Hour006:bool = obj["Hour006"]
      """  Hour006  """  
      self.Hour007:bool = obj["Hour007"]
      """  Hour007  """  
      self.Hour008:bool = obj["Hour008"]
      """  Hour008  """  
      self.Hour009:bool = obj["Hour009"]
      """  Hour009  """  
      self.Hour010:bool = obj["Hour010"]
      """  Hour010  """  
      self.Hour011:bool = obj["Hour011"]
      """  Hour011  """  
      self.Hour012:bool = obj["Hour012"]
      """  Hour012  """  
      self.Hour013:bool = obj["Hour013"]
      """  Hour013  """  
      self.Hour014:bool = obj["Hour014"]
      """  Hour014  """  
      self.Hour015:bool = obj["Hour015"]
      """  Hour015  """  
      self.Hour016:bool = obj["Hour016"]
      """  Hour016  """  
      self.Hour017:bool = obj["Hour017"]
      """  Hour017  """  
      self.Hour018:bool = obj["Hour018"]
      """  Hour018  """  
      self.Hour019:bool = obj["Hour019"]
      """  Hour019  """  
      self.Hour020:bool = obj["Hour020"]
      """  Hour020  """  
      self.Hour021:bool = obj["Hour021"]
      """  Hour021  """  
      self.Hour022:bool = obj["Hour022"]
      """  Hour022  """  
      self.Hour023:bool = obj["Hour023"]
      """  Hour023  """  
      self.Hour024:bool = obj["Hour024"]
      """  Hour024  """  
      self.Hour025:bool = obj["Hour025"]
      """  Hour025  """  
      self.Hour026:bool = obj["Hour026"]
      """  Hour026  """  
      self.Hour027:bool = obj["Hour027"]
      """  Hour027  """  
      self.Hour028:bool = obj["Hour028"]
      """  Hour028  """  
      self.Hour029:bool = obj["Hour029"]
      """  Hour029  """  
      self.Hour030:bool = obj["Hour030"]
      """  Hour030  """  
      self.Hour031:bool = obj["Hour031"]
      """  Hour031  """  
      self.Hour032:bool = obj["Hour032"]
      """  Hour032  """  
      self.Hour033:bool = obj["Hour033"]
      """  Hour033  """  
      self.Hour034:bool = obj["Hour034"]
      """  Hour034  """  
      self.Hour035:bool = obj["Hour035"]
      """  Hour035  """  
      self.Hour036:bool = obj["Hour036"]
      """  Hour036  """  
      self.Hour037:bool = obj["Hour037"]
      """  Hour037  """  
      self.Hour038:bool = obj["Hour038"]
      """  Hour038  """  
      self.Hour039:bool = obj["Hour039"]
      """  Hour039  """  
      self.Hour040:bool = obj["Hour040"]
      """  Hour040  """  
      self.Hour041:bool = obj["Hour041"]
      """  Hour041  """  
      self.Hour042:bool = obj["Hour042"]
      """  Hour042  """  
      self.Hour043:bool = obj["Hour043"]
      """  Hour043  """  
      self.Hour044:bool = obj["Hour044"]
      """  Hour044  """  
      self.Hour045:bool = obj["Hour045"]
      """  Hour045  """  
      self.Hour046:bool = obj["Hour046"]
      """  Hour046  """  
      self.Hour047:bool = obj["Hour047"]
      """  Hour047  """  
      self.Hour048:bool = obj["Hour048"]
      """  Hour048  """  
      self.Hour049:bool = obj["Hour049"]
      """  Hour049  """  
      self.Hour050:bool = obj["Hour050"]
      """  Hour050  """  
      self.Hour051:bool = obj["Hour051"]
      """  Hour051  """  
      self.Hour052:bool = obj["Hour052"]
      """  Hour052  """  
      self.Hour053:bool = obj["Hour053"]
      """  Hour053  """  
      self.Hour054:bool = obj["Hour054"]
      """  Hour054  """  
      self.Hour055:bool = obj["Hour055"]
      """  Hour055  """  
      self.Hour056:bool = obj["Hour056"]
      """  Hour056  """  
      self.Hour057:bool = obj["Hour057"]
      """  Hour057  """  
      self.Hour058:bool = obj["Hour058"]
      """  Hour058  """  
      self.Hour059:bool = obj["Hour059"]
      """  Hour059  """  
      self.Hour060:bool = obj["Hour060"]
      """  Hour060  """  
      self.Hour061:bool = obj["Hour061"]
      """  Hour061  """  
      self.Hour062:bool = obj["Hour062"]
      """  Hour062  """  
      self.Hour063:bool = obj["Hour063"]
      """  Hour063  """  
      self.Hour064:bool = obj["Hour064"]
      """  Hour064  """  
      self.Hour065:bool = obj["Hour065"]
      """  Hour065  """  
      self.Hour066:bool = obj["Hour066"]
      """  Hour066  """  
      self.Hour067:bool = obj["Hour067"]
      """  Hour067  """  
      self.Hour068:bool = obj["Hour068"]
      """  Hour068  """  
      self.Hour069:bool = obj["Hour069"]
      """  Hour069  """  
      self.Hour070:bool = obj["Hour070"]
      """  Hour070  """  
      self.Hour071:bool = obj["Hour071"]
      """  Hour071  """  
      self.Hour072:bool = obj["Hour072"]
      """  Hour072  """  
      self.Hour073:bool = obj["Hour073"]
      """  Hour073  """  
      self.Hour074:bool = obj["Hour074"]
      """  Hour074  """  
      self.Hour075:bool = obj["Hour075"]
      """  Hour075  """  
      self.Hour076:bool = obj["Hour076"]
      """  Hour076  """  
      self.Hour077:bool = obj["Hour077"]
      """  Hour077  """  
      self.Hour078:bool = obj["Hour078"]
      """  Hour078  """  
      self.Hour079:bool = obj["Hour079"]
      """  Hour079  """  
      self.Hour080:bool = obj["Hour080"]
      """  Hour080  """  
      self.Hour081:bool = obj["Hour081"]
      """  Hour081  """  
      self.Hour082:bool = obj["Hour082"]
      """  Hour082  """  
      self.Hour083:bool = obj["Hour083"]
      """  Hour083  """  
      self.Hour084:bool = obj["Hour084"]
      """  Hour084  """  
      self.Hour085:bool = obj["Hour085"]
      """  Hour085  """  
      self.Hour086:bool = obj["Hour086"]
      """  Hour086  """  
      self.Hour087:bool = obj["Hour087"]
      """  Hour087  """  
      self.Hour088:bool = obj["Hour088"]
      """  Hour088  """  
      self.Hour089:bool = obj["Hour089"]
      """  Hour089  """  
      self.Hour090:bool = obj["Hour090"]
      """  Hour090  """  
      self.Hour091:bool = obj["Hour091"]
      """  Hour091  """  
      self.Hour092:bool = obj["Hour092"]
      """  Hour092  """  
      self.Hour093:bool = obj["Hour093"]
      """  Hour093  """  
      self.Hour094:bool = obj["Hour094"]
      """  Hour094  """  
      self.Hour095:bool = obj["Hour095"]
      """  Hour095  """  
      self.Hour096:bool = obj["Hour096"]
      """  Hour096  """  
      self.Hour097:bool = obj["Hour097"]
      """  Hour097  """  
      self.Hour098:bool = obj["Hour098"]
      """  Hour098  """  
      self.Hour099:bool = obj["Hour099"]
      """  Hour099  """  
      self.Hour100:bool = obj["Hour100"]
      """  Hour100  """  
      self.Hour101:bool = obj["Hour101"]
      """  Hour101  """  
      self.Hour102:bool = obj["Hour102"]
      """  Hour102  """  
      self.Hour103:bool = obj["Hour103"]
      """  Hour103  """  
      self.Hour104:bool = obj["Hour104"]
      """  Hour104  """  
      self.Hour105:bool = obj["Hour105"]
      """  Hour105  """  
      self.Hour106:bool = obj["Hour106"]
      """  Hour106  """  
      self.Hour107:bool = obj["Hour107"]
      """  Hour107  """  
      self.Hour108:bool = obj["Hour108"]
      """  Hour108  """  
      self.Hour109:bool = obj["Hour109"]
      """  Hour109  """  
      self.Hour110:bool = obj["Hour110"]
      """  Hour110  """  
      self.Hour111:bool = obj["Hour111"]
      """  Hour111  """  
      self.Hour112:bool = obj["Hour112"]
      """  Hour112  """  
      self.Hour113:bool = obj["Hour113"]
      """  Hour113  """  
      self.Hour114:bool = obj["Hour114"]
      """  Hour114  """  
      self.Hour115:bool = obj["Hour115"]
      """  Hour115  """  
      self.Hour116:bool = obj["Hour116"]
      """  Hour116  """  
      self.Hour117:bool = obj["Hour117"]
      """  Hour117  """  
      self.Hour118:bool = obj["Hour118"]
      """  Hour118  """  
      self.Hour119:bool = obj["Hour119"]
      """  Hour119  """  
      self.Hour120:bool = obj["Hour120"]
      """  Hour120  """  
      self.Hour121:bool = obj["Hour121"]
      """  Hour121  """  
      self.Hour122:bool = obj["Hour122"]
      """  Hour122  """  
      self.Hour123:bool = obj["Hour123"]
      """  Hour123  """  
      self.Hour124:bool = obj["Hour124"]
      """  Hour124  """  
      self.Hour125:bool = obj["Hour125"]
      """  Hour125  """  
      self.Hour126:bool = obj["Hour126"]
      """  Hour126  """  
      self.Hour127:bool = obj["Hour127"]
      """  Hour127  """  
      self.Hour128:bool = obj["Hour128"]
      """  Hour128  """  
      self.Hour129:bool = obj["Hour129"]
      """  Hour129  """  
      self.Hour130:bool = obj["Hour130"]
      """  Hour130  """  
      self.Hour131:bool = obj["Hour131"]
      """  Hour131  """  
      self.Hour132:bool = obj["Hour132"]
      """  Hour132  """  
      self.Hour133:bool = obj["Hour133"]
      """  Hour133  """  
      self.Hour134:bool = obj["Hour134"]
      """  Hour134  """  
      self.Hour135:bool = obj["Hour135"]
      """  Hour135  """  
      self.Hour136:bool = obj["Hour136"]
      """  Hour136  """  
      self.Hour137:bool = obj["Hour137"]
      """  Hour137  """  
      self.Hour138:bool = obj["Hour138"]
      """  Hour138  """  
      self.Hour139:bool = obj["Hour139"]
      """  Hour139  """  
      self.Hour140:bool = obj["Hour140"]
      """  Hour140  """  
      self.Hour141:bool = obj["Hour141"]
      """  Hour141  """  
      self.Hour142:bool = obj["Hour142"]
      """  Hour142  """  
      self.Hour143:bool = obj["Hour143"]
      """  Hour143  """  
      self.Hour144:bool = obj["Hour144"]
      """  Hour144  """  
      self.Hour145:bool = obj["Hour145"]
      """  Hour145  """  
      self.Hour146:bool = obj["Hour146"]
      """  Hour146  """  
      self.Hour147:bool = obj["Hour147"]
      """  Hour147  """  
      self.Hour148:bool = obj["Hour148"]
      """  Hour148  """  
      self.Hour149:bool = obj["Hour149"]
      """  Hour149  """  
      self.Hour150:bool = obj["Hour150"]
      """  Hour150  """  
      self.Hour151:bool = obj["Hour151"]
      """  Hour151  """  
      self.Hour152:bool = obj["Hour152"]
      """  Hour152  """  
      self.Hour153:bool = obj["Hour153"]
      """  Hour153  """  
      self.Hour154:bool = obj["Hour154"]
      """  Hour154  """  
      self.Hour155:bool = obj["Hour155"]
      """  Hour155  """  
      self.Hour156:bool = obj["Hour156"]
      """  Hour156  """  
      self.Hour157:bool = obj["Hour157"]
      """  Hour157  """  
      self.Hour158:bool = obj["Hour158"]
      """  Hour158  """  
      self.Hour159:bool = obj["Hour159"]
      """  Hour159  """  
      self.Hour160:bool = obj["Hour160"]
      """  Hour160  """  
      self.Hour161:bool = obj["Hour161"]
      """  Hour161  """  
      self.Hour162:bool = obj["Hour162"]
      """  Hour162  """  
      self.Hour163:bool = obj["Hour163"]
      """  Hour163  """  
      self.Hour164:bool = obj["Hour164"]
      """  Hour164  """  
      self.Hour165:bool = obj["Hour165"]
      """  Hour165  """  
      self.Hour166:bool = obj["Hour166"]
      """  Hour166  """  
      self.Hour167:bool = obj["Hour167"]
      """  Hour167  """  
      self.Hour168:bool = obj["Hour168"]
      """  Hour168  """  
      self.HoursPerDay:int = obj["HoursPerDay"]
      """  The Number of Hours that a single Resouce is available per day.  """  
      self.BeginWeekday:int = obj["BeginWeekday"]
      """  Day of the week on which the Production Calendar begins.  Values mirror the values returned by the Progress "weekday" function.  Valid values:  1 = Sunday, 2 = Monday, 3 = Tuesday, 4 = Wednesday, 5 = Thursday, 6 = Friday, 7 = Sunday.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NumberOfMachines:int = obj["NumberOfMachines"]
      """  Num of machines assigned to the workcenter  """  
      self.PlantCalendar:bool = obj["PlantCalendar"]
      self.ProposedCalendarID:str = obj["ProposedCalendarID"]
      self.ReadOnlyFields:str = obj["ReadOnlyFields"]
      """  Delimited list of read-only fields  """  
      self.StartTime1:int = obj["StartTime1"]
      self.StartTime2:int = obj["StartTime2"]
      self.StartTime3:int = obj["StartTime3"]
      self.StartTime4:int = obj["StartTime4"]
      self.StartTime5:int = obj["StartTime5"]
      self.StartTime6:int = obj["StartTime6"]
      self.StartTime7:int = obj["StartTime7"]
      self.EndTime1:int = obj["EndTime1"]
      self.EndTime2:int = obj["EndTime2"]
      self.EndTime3:int = obj["EndTime3"]
      self.EndTime4:int = obj["EndTime4"]
      self.EndTime5:int = obj["EndTime5"]
      self.EndTime6:int = obj["EndTime6"]
      self.EndTime7:int = obj["EndTime7"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProdCalRsrcListRow:
   def __init__(self, obj):
      self.ResourceID:str = obj["ResourceID"]
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      self.ResourceDescription:str = obj["ResourceDescription"]
      self.Company:str = obj["Company"]
      self.CalendarID:str = obj["CalendarID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProdCalTableset:
   def __init__(self, obj):
      self.ProdCal:list[Erp_Tablesets_ProdCalRow] = obj["ProdCal"]
      self.ProdCalDay:list[Erp_Tablesets_ProdCalDayRow] = obj["ProdCalDay"]
      self.ProdCalPlantList:list[Erp_Tablesets_ProdCalPlantListRow] = obj["ProdCalPlantList"]
      self.ProdCalRsrcList:list[Erp_Tablesets_ProdCalRsrcListRow] = obj["ProdCalRsrcList"]
      self.ProdCalVendList:list[Erp_Tablesets_ProdCalVendListRow] = obj["ProdCalVendList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ProdCalVendListRow:
   def __init__(self, obj):
      self.VendorID:str = obj["VendorID"]
      """  Vendor ID  """  
      self.Company:str = obj["Company"]
      self.VendorName:str = obj["VendorName"]
      self.CalendarID:str = obj["CalendarID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtProdCalTableset:
   def __init__(self, obj):
      self.ProdCal:list[Erp_Tablesets_ProdCalRow] = obj["ProdCal"]
      self.ProdCalDay:list[Erp_Tablesets_ProdCalDayRow] = obj["ProdCalDay"]
      self.ProdCalPlantList:list[Erp_Tablesets_ProdCalPlantListRow] = obj["ProdCalPlantList"]
      self.ProdCalRsrcList:list[Erp_Tablesets_ProdCalRsrcListRow] = obj["ProdCalRsrcList"]
      self.ProdCalVendList:list[Erp_Tablesets_ProdCalVendListRow] = obj["ProdCalVendList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   calendarID
   """  
   def __init__(self, obj):
      self.calendarID:str = obj["calendarID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ProdCalTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ProdCalTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ProdCalTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ProdCalListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewProdCalDay_input:
   """ Required : 
   ds
   calendarID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProdCalTableset] = obj["ds"]
      self.calendarID:str = obj["calendarID"]
      pass

class GetNewProdCalDay_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProdCalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewProdCal_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProdCalTableset] = obj["ds"]
      pass

class GetNewProdCal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProdCalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPlantCalendar_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProdCalTableset] = obj["ds"]
      pass

class GetPlantCalendar_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProdCalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetProdCalHoursPerDay_input:
   """ Required : 
   calendarID
   """  
   def __init__(self, obj):
      self.calendarID:str = obj["calendarID"]
      """  Calendar  """  
      pass

class GetProdCalHoursPerDay_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ProdCalHoursPerDayTableset] = obj["returnObj"]
      pass

class GetResourceList_input:
   """ Required : 
   ds
   calendarID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProdCalTableset] = obj["ds"]
      self.calendarID:str = obj["calendarID"]
      """  Calendar ID  """  
      pass

class GetResourceList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProdCalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseProdCal
   whereClauseProdCalDay
   whereClauseProdCalPlantList
   whereClauseProdCalRsrcList
   whereClauseProdCalVendList
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseProdCal:str = obj["whereClauseProdCal"]
      self.whereClauseProdCalDay:str = obj["whereClauseProdCalDay"]
      self.whereClauseProdCalPlantList:str = obj["whereClauseProdCalPlantList"]
      self.whereClauseProdCalRsrcList:str = obj["whereClauseProdCalRsrcList"]
      self.whereClauseProdCalVendList:str = obj["whereClauseProdCalVendList"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ProdCalTableset] = obj["returnObj"]
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

class IsWorkDay_input:
   """ Required : 
   calendarID
   selectedDate
   """  
   def __init__(self, obj):
      self.calendarID:str = obj["calendarID"]
      """  Calendar ID to check  """  
      self.selectedDate:str = obj["selectedDate"]
      """  Date to check  """  
      pass

class IsWorkDay_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isWorkingDay:bool = obj["isWorkingDay"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtProdCalTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtProdCalTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateHoursSelected_input:
   """ Required : 
   hoursPerDay
   ds
   """  
   def __init__(self, obj):
      self.hoursPerDay:int = obj["hoursPerDay"]
      """  Hours per day  """  
      self.ds:list[Erp_Tablesets_ProdCalHoursPerDayTableset] = obj["ds"]
      pass

class UpdateHoursSelected_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProdCalHoursPerDayTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateProdCalHours_input:
   """ Required : 
   ds
   ds1
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProdCalTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_ProdCalHoursPerDayTableset] = obj["ds1"]
      pass

class UpdateProdCalHours_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProdCalTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_ProdCalHoursPerDayTableset] = obj["ds1"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProdCalTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProdCalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateWeekRangeNumberOfWeeks_input:
   """ Required : 
   numberOfWeeks
   startingDate
   """  
   def __init__(self, obj):
      self.numberOfWeeks:int = obj["numberOfWeeks"]
      """  The number of weeks to validate  """  
      self.startingDate:str = obj["startingDate"]
      """  The week range start date  """  
      pass

class ValidateWeekRangeNumberOfWeeks_output:
   def __init__(self, obj):
      pass

class ValidateWeekRangeStartingDate_input:
   """ Required : 
   startDate
   """  
   def __init__(self, obj):
      self.startDate:str = obj["startDate"]
      """  The date to validate  """  
      pass

class ValidateWeekRangeStartingDate_output:
   def __init__(self, obj):
      pass

class ValidateWeekRangeStartingWeek_input:
   """ Required : 
   startingWeekNumber
   """  
   def __init__(self, obj):
      self.startingWeekNumber:int = obj["startingWeekNumber"]
      """  Starting week number to validate  """  
      pass

class ValidateWeekRangeStartingWeek_output:
   def __init__(self, obj):
      pass

