import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.FiscalCalSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_FiscalCals(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FiscalCals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FiscalCals
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FiscalCalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalCals",headers=creds) as resp:
           return await resp.json()

async def post_FiscalCals(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FiscalCals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FiscalCalRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FiscalCalRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalCals", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FiscalCals_Company_FiscalCalendarID(Company, FiscalCalendarID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FiscalCal item
   Description: Calls GetByID to retrieve the FiscalCal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FiscalCal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FiscalCalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalCals(" + Company + "," + FiscalCalendarID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FiscalCals_Company_FiscalCalendarID(Company, FiscalCalendarID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FiscalCal for the service
   Description: Calls UpdateExt to update FiscalCal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FiscalCal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FiscalCalRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalCals(" + Company + "," + FiscalCalendarID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FiscalCals_Company_FiscalCalendarID(Company, FiscalCalendarID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FiscalCal item
   Description: Call UpdateExt to delete FiscalCal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FiscalCal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalCals(" + Company + "," + FiscalCalendarID + ")",headers=creds) as resp:
           return await resp.json()

async def get_FiscalCals_Company_FiscalCalendarID_FiscalYrs(Company, FiscalCalendarID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FiscalYrs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FiscalYrs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FiscalYrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalCals(" + Company + "," + FiscalCalendarID + ")/FiscalYrs",headers=creds) as resp:
           return await resp.json()

async def get_FiscalCals_Company_FiscalCalendarID_FiscalYrs_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix(Company, FiscalCalendarID, FiscalYear, FiscalYearSuffix, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FiscalYr item
   Description: Calls GetByID to retrieve the FiscalYr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FiscalYr1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FiscalYrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalCals(" + Company + "," + FiscalCalendarID + ")/FiscalYrs(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + ")",headers=creds) as resp:
           return await resp.json()

async def get_FiscalYrs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FiscalYrs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FiscalYrs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FiscalYrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalYrs",headers=creds) as resp:
           return await resp.json()

async def post_FiscalYrs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FiscalYrs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FiscalYrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FiscalYrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalYrs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FiscalYrs_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix(Company, FiscalCalendarID, FiscalYear, FiscalYearSuffix, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FiscalYr item
   Description: Calls GetByID to retrieve the FiscalYr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FiscalYr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FiscalYrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalYrs(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FiscalYrs_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix(Company, FiscalCalendarID, FiscalYear, FiscalYearSuffix, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FiscalYr for the service
   Description: Calls UpdateExt to update FiscalYr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FiscalYr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FiscalYrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalYrs(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FiscalYrs_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix(Company, FiscalCalendarID, FiscalYear, FiscalYearSuffix, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FiscalYr item
   Description: Call UpdateExt to delete FiscalYr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FiscalYr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalYrs(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + ")",headers=creds) as resp:
           return await resp.json()

async def get_FiscalYrs_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPers(Company, FiscalCalendarID, FiscalYear, FiscalYearSuffix, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FiscalPers items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FiscalPers1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FiscalPerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalYrs(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + ")/FiscalPers",headers=creds) as resp:
           return await resp.json()

async def get_FiscalYrs_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPers_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company, FiscalCalendarID, FiscalYear, FiscalYearSuffix, FiscalPeriod, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FiscalPer item
   Description: Calls GetByID to retrieve the FiscalPer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FiscalPer1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FiscalPerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalYrs(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + ")/FiscalPers(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")",headers=creds) as resp:
           return await resp.json()

async def get_FiscalPers(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FiscalPers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FiscalPers
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FiscalPerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalPers",headers=creds) as resp:
           return await resp.json()

async def post_FiscalPers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FiscalPers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FiscalPerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FiscalPerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalPers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FiscalPers_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company, FiscalCalendarID, FiscalYear, FiscalYearSuffix, FiscalPeriod, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FiscalPer item
   Description: Calls GetByID to retrieve the FiscalPer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FiscalPer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FiscalPerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalPers(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FiscalPers_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company, FiscalCalendarID, FiscalYear, FiscalYearSuffix, FiscalPeriod, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FiscalPer for the service
   Description: Calls UpdateExt to update FiscalPer. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FiscalPer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FiscalPerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalPers(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FiscalPers_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company, FiscalCalendarID, FiscalYear, FiscalYearSuffix, FiscalPeriod, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FiscalPer item
   Description: Call UpdateExt to delete FiscalPer item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FiscalPer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/FiscalPers(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FiscalCalListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseFiscalCal, whereClauseFiscalYr, whereClauseFiscalPer, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseFiscalCal=" + whereClauseFiscalCal
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFiscalYr=" + whereClauseFiscalYr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFiscalPer=" + whereClauseFiscalPer
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(fiscalCalendarID, epicorHeaders = None):
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
   params += "fiscalCalendarID=" + fiscalCalendarID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetLinkedBooks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLinkedBooks
   Description: Get list of GL Books which are referenced by this calendar.
   OperationID: GetLinkedBooks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLinkedBooks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLinkedBooks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateLinkedBooksWithBalFmtChg(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateLinkedBooksWithBalFmtChg
   Description: Update each referenced GL book with COABalFmtChg = true
   OperationID: UpdateLinkedBooksWithBalFmtChg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateLinkedBooksWithBalFmtChg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateLinkedBooksWithBalFmtChg_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalculateITPeriodDflts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalculateITPeriodDflts
   Description: Uses Income Tax Fiscal Year values to populate all its related fiscal Periods. Method only used for MX Localization.
   OperationID: CalculateITPeriodDflts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateITPeriodDflts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateITPeriodDflts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_deletebulk(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method deletebulk
   OperationID: deletebulk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/deletebulk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/deletebulk_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GeneratePeriods(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GeneratePeriods
   Description: Get dataset record for Generate Fiscal Periods functionality.
   OperationID: GeneratePeriods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GeneratePeriods_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GeneratePeriods_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFiscalPerGenerate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFiscalPerGenerate
   Description: Get dataset record for Generate Fiscal Periods functionality.
   OperationID: GetFiscalPerGenerate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFiscalPerGenerate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFiscalPerGenerate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGLJrnDtlInYear(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGLJrnDtlInYear
   OperationID: GetGLJrnDtlInYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGLJrnDtlInYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLJrnDtlInYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGLJrnDtlByPeriods(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGLJrnDtlByPeriods
   OperationID: GetGLJrnDtlByPeriods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGLJrnDtlByPeriods_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLJrnDtlByPeriods_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFiscalCal(epicorHeaders = None):
   """  
   Summary: Invoke method GetFiscalCal
   Description: Returns Calendar defined in company
   OperationID: GetFiscalCal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFiscalCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_CheckDataInGLJrnDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDataInGLJrnDtl
   OperationID: CheckDataInGLJrnDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDataInGLJrnDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDataInGLJrnDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetFiscalYrDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetFiscalYrDefaults
   Description: Sets default references on Previous and Next Fiscal Years, Start and End Dates depending on Fiscal Year and Fiscal Year Suffix entered
   OperationID: SetFiscalYrDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetFiscalYrDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetFiscalYrDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckIncompleteFiscalYear(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckIncompleteFiscalYear
   Description: Throws exception if EndDate of at least one Fiscal Year in the Calendar is not covered by corresponding Fiscal Period
   OperationID: CheckIncompleteFiscalYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckIncompleteFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIncompleteFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFiscalCal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFiscalCal
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFiscalCal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFiscalCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFiscalCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFiscalYr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFiscalYr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFiscalYr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFiscalYr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFiscalYr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFiscalPer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFiscalPer
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFiscalPer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFiscalPer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFiscalPer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FiscalCalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalCalListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FiscalCalListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalCalRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FiscalCalRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalPerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FiscalPerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalYrRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FiscalYrRow] = obj["value"]
      pass

class Erp_Tablesets_FiscalCalListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.Description:str = obj["Description"]
      """  Calendar description.  """  
      self.StartDate:str = obj["StartDate"]
      """  The start date of the fiscal calendar.  """  
      self.EndDate:str = obj["EndDate"]
      """  The end date of the fiscal calendar.  """  
      self.GlobalCal:bool = obj["GlobalCal"]
      """  Determines whether or not this calendar is shared between more than one company.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FiscalCalRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.Description:str = obj["Description"]
      """  Calendar description.  """  
      self.StartDate:str = obj["StartDate"]
      """  The start date of the fiscal calendar.  """  
      self.EndDate:str = obj["EndDate"]
      """  The end date of the fiscal calendar.  """  
      self.GlobalCal:bool = obj["GlobalCal"]
      """  Determines whether or not this calendar is shared between more than one company.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FiscalPerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.StartDate:str = obj["StartDate"]
      """  The start date of the fiscal period.  """  
      self.EndDate:str = obj["EndDate"]
      """  End date of the fiscal period  """  
      self.FAClosedPeriod:bool = obj["FAClosedPeriod"]
      """  Indicates if the Fixed Asset period is open or closed.  """  
      self.AdditionalDeductions:int = obj["AdditionalDeductions"]
      """  Additional Deductions to be claimed. User should calculate this value manually  """  
      self.LossesCredit:int = obj["LossesCredit"]
      """  Income Tax losses to be claimed. User should calculate this value manually  """  
      self.InvestmentCredit:int = obj["InvestmentCredit"]
      """  Investments Credit to be claimed. User should calculate this value manually  """  
      self.InventoriesCredit:int = obj["InventoriesCredit"]
      """  Inventories Credit to be claimed. User should calculate this value manually.  """  
      self.UpdateRate:int = obj["UpdateRate"]
      """  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  """  
      self.DepHoliday:bool = obj["DepHoliday"]
      """  Flag to indicate if the fiscal period is a holiday period.  This flag will be used in the asset depreciation calculation process to skip calculation of preiod depreciation charge if it's a holiday.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JPYear:int = obj["JPYear"]
      """  JPYear  """  
      self.EnableStartDate:bool = obj["EnableStartDate"]
      """  Indicates if StartDate can be changed by the user.  """  
      self.EnableEndDate:bool = obj["EnableEndDate"]
      """  Indicates if EndDate can be modified by the user.  """  
      self.NoOfDays:str = obj["NoOfDays"]
      """  Number of days (EndDate - StartDate)  """  
      self.ITUpdateRate:int = obj["ITUpdateRate"]
      """  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  """  
      self.AssetRegCurrYear:int = obj["AssetRegCurrYear"]
      """  Used in Close Asset Period / Year process  """  
      self.AssetRegCurrYearSuffix:str = obj["AssetRegCurrYearSuffix"]
      """  Used in Close Asset Period / Year process  """  
      self.AssetRegCurrPeriod:int = obj["AssetRegCurrPeriod"]
      """  Used in Close Asset Period / Year process  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FiscalYrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.StartDate:str = obj["StartDate"]
      """  The fiscal year start date.  """  
      self.EndDate:str = obj["EndDate"]
      """  The fiscal year end date.  """  
      self.NumPeriods:int = obj["NumPeriods"]
      """  The number of ordinary fiscal periods in the year.  """  
      self.NumClosingPeriods:int = obj["NumClosingPeriods"]
      """  The number of closing periods for the fiscal year.  Can be zero.  """  
      self.NextFiscalYear:int = obj["NextFiscalYear"]
      """  The next fiscal year (next FiscalYr record).  """  
      self.NextFiscalYearSuffix:str = obj["NextFiscalYearSuffix"]
      """  The next fiscal year suffix.  """  
      self.PrevFiscalYear:int = obj["PrevFiscalYear"]
      """  The previous fiscal year (previous FiscalYr record).  """  
      self.PrevFiscalYearSuffix:str = obj["PrevFiscalYearSuffix"]
      """  The previous fiscal year suffix.  """  
      self.Description:str = obj["Description"]
      """  Fiscal year description.  """  
      self.AdditionalDeductions:int = obj["AdditionalDeductions"]
      """  Additional Deductions to be claimed. User should calculate this value manually  """  
      self.LossesCredit:int = obj["LossesCredit"]
      """  Income Tax losses to be claimed. User should calculate this value manually  """  
      self.InvestmentCredit:int = obj["InvestmentCredit"]
      """  Investments Credit to be claimed. User should calculate this value manually  """  
      self.InventoriesCredit:int = obj["InventoriesCredit"]
      """  Inventories Credit to be claimed. User should calculate this value manually.  """  
      self.UpdateRate:int = obj["UpdateRate"]
      """  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.YearSuffix:str = obj["YearSuffix"]
      """  Concatenation of Year and Suffix for tree view.  """  
      self.EnableStartDate:bool = obj["EnableStartDate"]
      """  Indicates if StartDate is available for input.  """  
      self.ITUpdateRate:int = obj["ITUpdateRate"]
      """  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CalculateITPeriodDflts_input:
   """ Required : 
   ipFiscalCalendarID
   ipFiscalYear
   ipFiscalYearSuffix
   ds
   """  
   def __init__(self, obj):
      self.ipFiscalCalendarID:str = obj["ipFiscalCalendarID"]
      """  current Fiscal Calendar ID  """  
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      """  current Fiscal Year  """  
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      """  current Fiscal Year Suffix.  """  
      self.ds:list[Erp_Tablesets_FiscalCalTableset] = obj["ds"]
      pass

class CalculateITPeriodDflts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FiscalCalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckDataInGLJrnDtl_input:
   """ Required : 
   cFiscalCalendarID
   iFiscalYear
   cFiscalYearSuffix
   iFiscalPeriod
   dStartDate
   dEndDate
   iWorkMode
   """  
   def __init__(self, obj):
      self.cFiscalCalendarID:str = obj["cFiscalCalendarID"]
      self.iFiscalYear:int = obj["iFiscalYear"]
      self.cFiscalYearSuffix:str = obj["cFiscalYearSuffix"]
      self.iFiscalPeriod:int = obj["iFiscalPeriod"]
      self.dStartDate:str = obj["dStartDate"]
      self.dEndDate:str = obj["dEndDate"]
      self.iWorkMode:int = obj["iWorkMode"]
      pass

class CheckDataInGLJrnDtl_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.cBookID:str = obj["parameters"]
      self.cJournalCode:str = obj["parameters"]
      self.iJournalNum:int = obj["parameters"]
      self.iJournalLine:int = obj["parameters"]
      pass

      """  output parameters  """  

class CheckIncompleteFiscalYear_input:
   """ Required : 
   fiscalCalendarID
   """  
   def __init__(self, obj):
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      """  Fiscal Calendar ID  """  
      pass

class CheckIncompleteFiscalYear_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   fiscalCalendarID
   """  
   def __init__(self, obj):
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_FiscalCalListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.Description:str = obj["Description"]
      """  Calendar description.  """  
      self.StartDate:str = obj["StartDate"]
      """  The start date of the fiscal calendar.  """  
      self.EndDate:str = obj["EndDate"]
      """  The end date of the fiscal calendar.  """  
      self.GlobalCal:bool = obj["GlobalCal"]
      """  Determines whether or not this calendar is shared between more than one company.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FiscalCalListTableset:
   def __init__(self, obj):
      self.FiscalCalList:list[Erp_Tablesets_FiscalCalListRow] = obj["FiscalCalList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FiscalCalRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.Description:str = obj["Description"]
      """  Calendar description.  """  
      self.StartDate:str = obj["StartDate"]
      """  The start date of the fiscal calendar.  """  
      self.EndDate:str = obj["EndDate"]
      """  The end date of the fiscal calendar.  """  
      self.GlobalCal:bool = obj["GlobalCal"]
      """  Determines whether or not this calendar is shared between more than one company.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FiscalCalTableset:
   def __init__(self, obj):
      self.FiscalCal:list[Erp_Tablesets_FiscalCalRow] = obj["FiscalCal"]
      self.FiscalYr:list[Erp_Tablesets_FiscalYrRow] = obj["FiscalYr"]
      self.FiscalPer:list[Erp_Tablesets_FiscalPerRow] = obj["FiscalPer"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FiscalPerGenerateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.StartDate:str = obj["StartDate"]
      self.EndDate:str = obj["EndDate"]
      self.PeriodDuration:int = obj["PeriodDuration"]
      self.DurationType:str = obj["DurationType"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FiscalPerGenerateTableset:
   def __init__(self, obj):
      self.FiscalPerGenerate:list[Erp_Tablesets_FiscalPerGenerateRow] = obj["FiscalPerGenerate"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FiscalPerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.StartDate:str = obj["StartDate"]
      """  The start date of the fiscal period.  """  
      self.EndDate:str = obj["EndDate"]
      """  End date of the fiscal period  """  
      self.FAClosedPeriod:bool = obj["FAClosedPeriod"]
      """  Indicates if the Fixed Asset period is open or closed.  """  
      self.AdditionalDeductions:int = obj["AdditionalDeductions"]
      """  Additional Deductions to be claimed. User should calculate this value manually  """  
      self.LossesCredit:int = obj["LossesCredit"]
      """  Income Tax losses to be claimed. User should calculate this value manually  """  
      self.InvestmentCredit:int = obj["InvestmentCredit"]
      """  Investments Credit to be claimed. User should calculate this value manually  """  
      self.InventoriesCredit:int = obj["InventoriesCredit"]
      """  Inventories Credit to be claimed. User should calculate this value manually.  """  
      self.UpdateRate:int = obj["UpdateRate"]
      """  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  """  
      self.DepHoliday:bool = obj["DepHoliday"]
      """  Flag to indicate if the fiscal period is a holiday period.  This flag will be used in the asset depreciation calculation process to skip calculation of preiod depreciation charge if it's a holiday.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JPYear:int = obj["JPYear"]
      """  JPYear  """  
      self.EnableStartDate:bool = obj["EnableStartDate"]
      """  Indicates if StartDate can be changed by the user.  """  
      self.EnableEndDate:bool = obj["EnableEndDate"]
      """  Indicates if EndDate can be modified by the user.  """  
      self.NoOfDays:str = obj["NoOfDays"]
      """  Number of days (EndDate - StartDate)  """  
      self.ITUpdateRate:int = obj["ITUpdateRate"]
      """  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  """  
      self.AssetRegCurrYear:int = obj["AssetRegCurrYear"]
      """  Used in Close Asset Period / Year process  """  
      self.AssetRegCurrYearSuffix:str = obj["AssetRegCurrYearSuffix"]
      """  Used in Close Asset Period / Year process  """  
      self.AssetRegCurrPeriod:int = obj["AssetRegCurrPeriod"]
      """  Used in Close Asset Period / Year process  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FiscalYrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.StartDate:str = obj["StartDate"]
      """  The fiscal year start date.  """  
      self.EndDate:str = obj["EndDate"]
      """  The fiscal year end date.  """  
      self.NumPeriods:int = obj["NumPeriods"]
      """  The number of ordinary fiscal periods in the year.  """  
      self.NumClosingPeriods:int = obj["NumClosingPeriods"]
      """  The number of closing periods for the fiscal year.  Can be zero.  """  
      self.NextFiscalYear:int = obj["NextFiscalYear"]
      """  The next fiscal year (next FiscalYr record).  """  
      self.NextFiscalYearSuffix:str = obj["NextFiscalYearSuffix"]
      """  The next fiscal year suffix.  """  
      self.PrevFiscalYear:int = obj["PrevFiscalYear"]
      """  The previous fiscal year (previous FiscalYr record).  """  
      self.PrevFiscalYearSuffix:str = obj["PrevFiscalYearSuffix"]
      """  The previous fiscal year suffix.  """  
      self.Description:str = obj["Description"]
      """  Fiscal year description.  """  
      self.AdditionalDeductions:int = obj["AdditionalDeductions"]
      """  Additional Deductions to be claimed. User should calculate this value manually  """  
      self.LossesCredit:int = obj["LossesCredit"]
      """  Income Tax losses to be claimed. User should calculate this value manually  """  
      self.InvestmentCredit:int = obj["InvestmentCredit"]
      """  Investments Credit to be claimed. User should calculate this value manually  """  
      self.InventoriesCredit:int = obj["InventoriesCredit"]
      """  Inventories Credit to be claimed. User should calculate this value manually.  """  
      self.UpdateRate:int = obj["UpdateRate"]
      """  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.YearSuffix:str = obj["YearSuffix"]
      """  Concatenation of Year and Suffix for tree view.  """  
      self.EnableStartDate:bool = obj["EnableStartDate"]
      """  Indicates if StartDate is available for input.  """  
      self.ITUpdateRate:int = obj["ITUpdateRate"]
      """  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtFiscalCalTableset:
   def __init__(self, obj):
      self.FiscalCal:list[Erp_Tablesets_FiscalCalRow] = obj["FiscalCal"]
      self.FiscalYr:list[Erp_Tablesets_FiscalYrRow] = obj["FiscalYr"]
      self.FiscalPer:list[Erp_Tablesets_FiscalPerRow] = obj["FiscalPer"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GeneratePeriods_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FiscalPerGenerateTableset] = obj["ds"]
      pass

class GeneratePeriods_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FiscalCalTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.cOutMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   fiscalCalendarID
   """  
   def __init__(self, obj):
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FiscalCalTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FiscalCalTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FiscalCalTableset] = obj["returnObj"]
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

class GetFiscalCal_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetFiscalPerGenerate_input:
   """ Required : 
   cFiscalCalendarID
   iFiscalYear
   cFiscalYearSuffix
   """  
   def __init__(self, obj):
      self.cFiscalCalendarID:str = obj["cFiscalCalendarID"]
      """  The Fiscal Calendar ID  """  
      self.iFiscalYear:int = obj["iFiscalYear"]
      """  The Fiscal Year  """  
      self.cFiscalYearSuffix:str = obj["cFiscalYearSuffix"]
      """  The Fiscal Year Suffix  """  
      pass

class GetFiscalPerGenerate_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FiscalPerGenerateTableset] = obj["returnObj"]
      pass

class GetGLJrnDtlByPeriods_input:
   """ Required : 
   cFiscalCalendarID
   iFiscalYear
   cFiscalYearSuffix
   iFiscalPeriodFrom
   iWorkMode
   """  
   def __init__(self, obj):
      self.cFiscalCalendarID:str = obj["cFiscalCalendarID"]
      self.iFiscalYear:int = obj["iFiscalYear"]
      self.cFiscalYearSuffix:str = obj["cFiscalYearSuffix"]
      self.iFiscalPeriodFrom:int = obj["iFiscalPeriodFrom"]
      self.iWorkMode:int = obj["iWorkMode"]
      pass

class GetGLJrnDtlByPeriods_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.lIsGetIt:int = obj["parameters"]
      self.cBookID:str = obj["parameters"]
      self.cJournalCode:str = obj["parameters"]
      self.iJournalNum:int = obj["parameters"]
      self.iJournalLine:int = obj["parameters"]
      self.iFiscalYearOut:int = obj["parameters"]
      self.cFiscalYearSuffixOut:str = obj["parameters"]
      self.iFiscalPeriodOut:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetGLJrnDtlInYear_input:
   """ Required : 
   cFiscalCalendarID
   iFiscalYear
   cFiscalYearSuffix
   iFiscalPeriodFrom
   iWorkMode
   """  
   def __init__(self, obj):
      self.cFiscalCalendarID:str = obj["cFiscalCalendarID"]
      self.iFiscalYear:int = obj["iFiscalYear"]
      self.cFiscalYearSuffix:str = obj["cFiscalYearSuffix"]
      self.iFiscalPeriodFrom:int = obj["iFiscalPeriodFrom"]
      self.iWorkMode:int = obj["iWorkMode"]
      pass

class GetGLJrnDtlInYear_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.lIsGetIt:int = obj["parameters"]
      self.cBookID:str = obj["parameters"]
      self.cJournalCode:str = obj["parameters"]
      self.iJournalNum:int = obj["parameters"]
      self.iJournalLine:int = obj["parameters"]
      self.iFiscalYearOut:int = obj["parameters"]
      self.cFiscalYearSuffixOut:str = obj["parameters"]
      self.iFiscalPeriodOut:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetLinkedBooks_input:
   """ Required : 
   fiscalCalendarID
   """  
   def __init__(self, obj):
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      """  Fiscal Calendar ID  """  
      pass

class GetLinkedBooks_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FiscalCalListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewFiscalCal_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FiscalCalTableset] = obj["ds"]
      pass

class GetNewFiscalCal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FiscalCalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFiscalPer_input:
   """ Required : 
   ds
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FiscalCalTableset] = obj["ds"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      pass

class GetNewFiscalPer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FiscalCalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFiscalYr_input:
   """ Required : 
   ds
   fiscalCalendarID
   fiscalYear
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FiscalCalTableset] = obj["ds"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      pass

class GetNewFiscalYr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FiscalCalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseFiscalCal
   whereClauseFiscalYr
   whereClauseFiscalPer
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFiscalCal:str = obj["whereClauseFiscalCal"]
      self.whereClauseFiscalYr:str = obj["whereClauseFiscalYr"]
      self.whereClauseFiscalPer:str = obj["whereClauseFiscalPer"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FiscalCalTableset] = obj["returnObj"]
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

class SetFiscalYrDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FiscalCalTableset] = obj["ds"]
      pass

class SetFiscalYrDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FiscalCalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtFiscalCalTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtFiscalCalTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateLinkedBooksWithBalFmtChg_input:
   """ Required : 
   fiscalCalendarID
   """  
   def __init__(self, obj):
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      pass

class UpdateLinkedBooksWithBalFmtChg_output:
   def __init__(self, obj):
      pass

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FiscalCalTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FiscalCalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class deletebulk_input:
   """ Required : 
   ipFiscalCalendarID
   ipFiscalYear
   ipFiscalYearSuffix
   ds
   """  
   def __init__(self, obj):
      self.ipFiscalCalendarID:str = obj["ipFiscalCalendarID"]
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      self.ds:list[Erp_Tablesets_FiscalCalTableset] = obj["ds"]
      pass

class deletebulk_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FiscalCalTableset] = obj["ds"]
      pass

      """  output parameters  """  

