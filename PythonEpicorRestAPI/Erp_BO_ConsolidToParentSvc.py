import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ConsolidToParentSvc
# Description: bo/ConsolidToParent/ConsolidToParent
Consolidate to Parent Business Object
SCR 40420 (Opr. 320)
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ConsolidToParents(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ConsolidToParents items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConsolidToParents
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsolidToParents",headers=creds) as resp:
           return await resp.json()

async def post_ConsolidToParents(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConsolidToParents
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsolidToParents", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ConsolidToParents_Company_GenID(Company, GenID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConsolidToParent item
   Description: Calls GetByID to retrieve the ConsolidToParent item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConsolidToParent
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsolidToParents(" + Company + "," + GenID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ConsolidToParents_Company_GenID(Company, GenID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ConsolidToParent for the service
   Description: Calls UpdateExt to update ConsolidToParent. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConsolidToParent
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsolidToParents(" + Company + "," + GenID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ConsolidToParents_Company_GenID(Company, GenID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ConsolidToParent item
   Description: Call UpdateExt to delete ConsolidToParent item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConsolidToParent
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsolidToParents(" + Company + "," + GenID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ConsolidToParents_Company_GenID_ConsSrcCtrls(Company, GenID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsolidToParents(" + Company + "," + GenID + ")/ConsSrcCtrls",headers=creds) as resp:
           return await resp.json()

async def get_ConsolidToParents_Company_GenID_ConsSrcCtrls_Company_GenID_SourceBook(Company, GenID, SourceBook, select = None, expand = None, filter = None, epicorHeaders = None):
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsolidToParents(" + Company + "," + GenID + ")/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcCtrls",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcCtrls", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")/ConsSrcRates",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcCtrls(" + Company + "," + GenID + "," + SourceBook + ")/ConsSrcRates(" + Company + "," + GenID + "," + SourceBook + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + RateTypeID + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcRates",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcRates", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcRates(" + Company + "," + GenID + "," + SourceBook + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + RateTypeID + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcRates(" + Company + "," + GenID + "," + SourceBook + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + RateTypeID + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/ConsSrcRates(" + Company + "," + GenID + "," + SourceBook + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + RateTypeID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ConsTgtGenListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseConsTgtGen, whereClauseConsSrcCtrl, whereClauseConsSrcRates, pageSize, absolutePage, epicorHeaders = None):
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(genID, epicorHeaders = None):
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
   params += "genID=" + genID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetConsDefIDData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetConsDefIDData
   Description: Gets information from the Consolidation Definition
   OperationID: GetConsDefIDData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetConsDefIDData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetConsDefIDData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaults
   Description: Method to call to get the default consolidation types and currency exchange rates.
   OperationID: GetDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RecalculateRates(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RecalculateRates
   Description: This method checks if the consolidation rates may need recalculation, and warn user about it.
   OperationID: RecalculateRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecalculateRates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecalculateRates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewConsTgtGenEntryMode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewConsTgtGenEntryMode
   Description: Gets a new Consolidation to Parent record for the specified Entry Type
   OperationID: GetNewConsTgtGenEntryMode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewConsTgtGenEntryMode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConsTgtGenEntryMode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateExchangeRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateExchangeRate
   Description: Checks if the user modified the exchange rate
   OperationID: ValidateExchangeRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSrcAdjustFromFiscalPeriod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSrcAdjustFromFiscalPeriod
   Description: Called when Adjust From Fiscal Period is changed
   OperationID: ValidateSrcAdjustFromFiscalPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSrcAdjustFromFiscalPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSrcAdjustFromFiscalPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSrcFiscalPeriod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSrcFiscalPeriod
   Description: Validates the source control fiscal period
   OperationID: ValidateSrcFiscalPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSrcFiscalPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSrcFiscalPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePrevRecords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePrevRecords
   Description: Validates if previous consolidations have been processed
   OperationID: ValidatePrevRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePrevRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePrevRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckConsReadyToPost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckConsReadyToPost
   Description: Checks if the consoliation is ready to post
   OperationID: CheckConsReadyToPost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckConsReadyToPost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckConsReadyToPost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SendErrorMsg(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SendErrorMsg
   Description: Sends the error message
   OperationID: SendErrorMsg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SendErrorMsg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SendErrorMsg_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateClosingPeriods(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateClosingPeriods
   Description: Validates closing periods
   OperationID: ValidateClosingPeriods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateClosingPeriods_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateClosingPeriods_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateFiscalPeriod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateFiscalPeriod
   Description: Validates the fiscal period
   OperationID: ValidateFiscalPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateFiscalPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFiscalPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateFiscalYearandGetPeriods(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateFiscalYearandGetPeriods
   Description: Validates the fiscal year and selects the fiscal periods
   OperationID: ValidateFiscalYearandGetPeriods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateFiscalYearandGetPeriods_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFiscalYearandGetPeriods_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateFiscalYear(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateFiscalYear
   Description: Validates the fiscal year
   OperationID: ValidateFiscalYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateGenID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateGenID
   Description: Validate the Consolidation ID
   OperationID: ValidateGenID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateGenID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateGenID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateRateGroupStatus(epicorHeaders = None):
   """  
   Summary: Invoke method ValidateRateGroupStatus
   Description: Validate the Rate Group Status
   OperationID: ValidateRateGroupStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRateGroupStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ValidateLastConsol(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateLastConsol
   Description: Checks if it is the Last Consolidation depending on SourceBook and Consolidation Definition
   OperationID: ValidateLastConsol
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateLastConsol_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateLastConsol_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConsolidToParentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
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

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtGenListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ConsTgtGenListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ConsTgtGenRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ConsTgtGenRow] = obj["value"]
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

class Erp_Tablesets_ConsTgtGenListRow:
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
      self.MasterCOA:bool = obj["MasterCOA"]
      """  Logical indicating if this COA is the Master COA.  """  
      self.ConsDefIDDescription:str = obj["ConsDefIDDescription"]
      """  Free form text that describes the target that sources are consolidated into.  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.IntermediateBookIDCurrencyCode:str = obj["IntermediateBookIDCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.IntermediateBookIDDescription:str = obj["IntermediateBookIDDescription"]
      """  Descripiton of Book  """  
      self.TargetCOADescription:str = obj["TargetCOADescription"]
      """  The description or Name of this Chart of Accounts.  """  
      self.TgtBookCurrencyCode:str = obj["TgtBookCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.TgtBookDescription:str = obj["TgtBookDescription"]
      """  Descripiton of Book  """  
      self.TgtCompanyName:str = obj["TgtCompanyName"]
      """  Company Name  """  
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




#########################################################################
# Custom Schemas:
#########################################################################
class CheckConsReadyToPost_input:
   """ Required : 
   intGenID
   txtSourceBook
   txtFiscalCalendarID
   intFiscalYear
   txtFiscalYearSuffix
   intFiscalPeriod
   """  
   def __init__(self, obj):
      self.intGenID:int = obj["intGenID"]
      """  The Consolidation ID  """  
      self.txtSourceBook:str = obj["txtSourceBook"]
      """  The Source Book  """  
      self.txtFiscalCalendarID:str = obj["txtFiscalCalendarID"]
      """  The Fiscal Calendar ID  """  
      self.intFiscalYear:int = obj["intFiscalYear"]
      """  The Fiscal Year  """  
      self.txtFiscalYearSuffix:str = obj["txtFiscalYearSuffix"]
      """  The Fiscal Year Suffix  """  
      self.intFiscalPeriod:int = obj["intFiscalPeriod"]
      """  The Fiscal Period  """  
      pass

class CheckConsReadyToPost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.txtpriorPeriodNotPostedMsg:str = obj["parameters"]
      self.txtperiodAlreadyPostedMsg:str = obj["parameters"]
      self.txtperiodAlreadyGeneratedMsg:str = obj["parameters"]
      self.txtfileAlreadyExistsMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   genID
   """  
   def __init__(self, obj):
      self.genID:int = obj["genID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
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

class Erp_Tablesets_ConsTgtGenListRow:
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
      self.MasterCOA:bool = obj["MasterCOA"]
      """  Logical indicating if this COA is the Master COA.  """  
      self.ConsDefIDDescription:str = obj["ConsDefIDDescription"]
      """  Free form text that describes the target that sources are consolidated into.  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.IntermediateBookIDCurrencyCode:str = obj["IntermediateBookIDCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.IntermediateBookIDDescription:str = obj["IntermediateBookIDDescription"]
      """  Descripiton of Book  """  
      self.TargetCOADescription:str = obj["TargetCOADescription"]
      """  The description or Name of this Chart of Accounts.  """  
      self.TgtBookCurrencyCode:str = obj["TgtBookCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.TgtBookDescription:str = obj["TgtBookDescription"]
      """  Descripiton of Book  """  
      self.TgtCompanyName:str = obj["TgtCompanyName"]
      """  Company Name  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConsTgtGenListTableset:
   def __init__(self, obj):
      self.ConsTgtGenList:list[Erp_Tablesets_ConsTgtGenListRow] = obj["ConsTgtGenList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

class Erp_Tablesets_ConsolidToParentTableset:
   def __init__(self, obj):
      self.ConsTgtGen:list[Erp_Tablesets_ConsTgtGenRow] = obj["ConsTgtGen"]
      self.ConsSrcCtrl:list[Erp_Tablesets_ConsSrcCtrlRow] = obj["ConsSrcCtrl"]
      self.ConsSrcRates:list[Erp_Tablesets_ConsSrcRatesRow] = obj["ConsSrcRates"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtConsolidToParentTableset:
   def __init__(self, obj):
      self.ConsTgtGen:list[Erp_Tablesets_ConsTgtGenRow] = obj["ConsTgtGen"]
      self.ConsSrcCtrl:list[Erp_Tablesets_ConsSrcCtrlRow] = obj["ConsSrcCtrl"]
      self.ConsSrcRates:list[Erp_Tablesets_ConsSrcRatesRow] = obj["ConsSrcRates"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   genID
   """  
   def __init__(self, obj):
      self.genID:int = obj["genID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConsolidToParentTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ConsolidToParentTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ConsolidToParentTableset] = obj["returnObj"]
      pass

class GetConsDefIDData_input:
   """ Required : 
   proposedConsDefID
   ds
   """  
   def __init__(self, obj):
      self.proposedConsDefID:str = obj["proposedConsDefID"]
      """  The proposed Consolidation Definition ID  """  
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      pass

class GetConsDefIDData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDefaults_input:
   """ Required : 
   ipGenID
   ipSourceBook
   ipGetDefaultType
   ds
   """  
   def __init__(self, obj):
      self.ipGenID:int = obj["ipGenID"]
      """  The Generation ID  """  
      self.ipSourceBook:str = obj["ipSourceBook"]
      """  The Source Book  """  
      self.ipGetDefaultType:int = obj["ipGetDefaultType"]
      """  GetDefault Type. 1 - All, 2 - Just record in screen.  """  
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      pass

class GetDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
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
      self.returnObj:list[Erp_Tablesets_ConsTgtGenListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewConsSrcCtrl_input:
   """ Required : 
   ds
   genID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      self.genID:int = obj["genID"]
      pass

class GetNewConsSrcCtrl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewConsTgtGenEntryMode_input:
   """ Required : 
   EntryMode
   ds
   """  
   def __init__(self, obj):
      self.EntryMode:str = obj["EntryMode"]
      """  The Entry Mode  """  
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      pass

class GetNewConsTgtGenEntryMode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewConsTgtGen_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      pass

class GetNewConsTgtGen_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseConsTgtGen
   whereClauseConsSrcCtrl
   whereClauseConsSrcRates
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseConsTgtGen:str = obj["whereClauseConsTgtGen"]
      self.whereClauseConsSrcCtrl:str = obj["whereClauseConsSrcCtrl"]
      self.whereClauseConsSrcRates:str = obj["whereClauseConsSrcRates"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConsolidToParentTableset] = obj["returnObj"]
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

class RecalculateRates_input:
   """ Required : 
   GenID
   SourceBook
   Option
   ds
   """  
   def __init__(self, obj):
      self.GenID:int = obj["GenID"]
      self.SourceBook:str = obj["SourceBook"]
      self.Option:int = obj["Option"]
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      pass

class RecalculateRates_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SendErrorMsg_input:
   """ Required : 
   ipcMethod
   ipcGenId
   ipcSourceBook
   ipcMsg
   """  
   def __init__(self, obj):
      self.ipcMethod:str = obj["ipcMethod"]
      """  The Generation Method  """  
      self.ipcGenId:str = obj["ipcGenId"]
      """  The Consolidation ID  """  
      self.ipcSourceBook:str = obj["ipcSourceBook"]
      """  The Source Book  """  
      self.ipcMsg:str = obj["ipcMsg"]
      """  The message to send  """  
      pass

class SendErrorMsg_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtConsolidToParentTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtConsolidToParentTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateClosingPeriods_input:
   """ Required : 
   ipFiscalCalendarID
   ipFiscalYear
   ipFiscalYearSuffix
   proposedClosingPeriods
   ipCalledFromUI
   """  
   def __init__(self, obj):
      self.ipFiscalCalendarID:str = obj["ipFiscalCalendarID"]
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      self.proposedClosingPeriods:int = obj["proposedClosingPeriods"]
      self.ipCalledFromUI:bool = obj["ipCalledFromUI"]
      pass

class ValidateClosingPeriods_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opcMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateExchangeRate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      pass

class ValidateExchangeRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateFiscalPeriod_input:
   """ Required : 
   ipcompany
   ipFiscalCalendarID
   ipFiscalYear
   ipFiscalYearSuffix
   proposedFiscalPeriod
   ipCalledFromUI
   """  
   def __init__(self, obj):
      self.ipcompany:str = obj["ipcompany"]
      """  The Company ID  """  
      self.ipFiscalCalendarID:str = obj["ipFiscalCalendarID"]
      """  The Fiscal Calendar ID  """  
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      """  The Fiscal Year  """  
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      """  The Fiscal Year Suffix  """  
      self.proposedFiscalPeriod:int = obj["proposedFiscalPeriod"]
      """  The FIscal Period  """  
      self.ipCalledFromUI:bool = obj["ipCalledFromUI"]
      """  Indicates if this method was called from the UI  """  
      pass

class ValidateFiscalPeriod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opcMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateFiscalYear_input:
   """ Required : 
   ipFiscalCalendarID
   proposedFiscalYear
   ipCalledFromUI
   """  
   def __init__(self, obj):
      self.ipFiscalCalendarID:str = obj["ipFiscalCalendarID"]
      """  The Fiscal Calendar ID  """  
      self.proposedFiscalYear:int = obj["proposedFiscalYear"]
      """  The Fiscal Year  """  
      self.ipCalledFromUI:bool = obj["ipCalledFromUI"]
      """  Indicates if this method was called from the UI  """  
      pass

class ValidateFiscalYear_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opFiscalYearSuffix:str = obj["parameters"]
      self.opcMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateFiscalYearandGetPeriods_input:
   """ Required : 
   proposedFiscalYear
   ds
   ipCalledFromUI
   entryMode
   """  
   def __init__(self, obj):
      self.proposedFiscalYear:int = obj["proposedFiscalYear"]
      """  The Fiscal Year  """  
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      self.ipCalledFromUI:bool = obj["ipCalledFromUI"]
      """  Indicates if this method was called from the UI  """  
      self.entryMode:str = obj["entryMode"]
      """  Consolidation Entry Mode  """  
      pass

class ValidateFiscalYearandGetPeriods_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      self.opcMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateGenID_input:
   """ Required : 
   intGenID
   """  
   def __init__(self, obj):
      self.intGenID:int = obj["intGenID"]
      pass

class ValidateGenID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.Recalculate:bool = obj["Recalculate"]
      pass

      """  output parameters  """  

class ValidateLastConsol_input:
   """ Required : 
   genID
   sourceBook
   consDefID
   """  
   def __init__(self, obj):
      self.genID:int = obj["genID"]
      """  Consolidation ID  """  
      self.sourceBook:str = obj["sourceBook"]
      """  Source Book  """  
      self.consDefID:str = obj["consDefID"]
      """  Consolidation Definition ID  """  
      pass

class ValidateLastConsol_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ValidatePrevRecords_input:
   """ Required : 
   intYear
   txtFiscalYearSuffix
   intPeriod
   ds
   """  
   def __init__(self, obj):
      self.intYear:int = obj["intYear"]
      """  Fiscal Year  """  
      self.txtFiscalYearSuffix:str = obj["txtFiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.intPeriod:int = obj["intPeriod"]
      """  Fiscal Period  """  
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      pass

class ValidatePrevRecords_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.txtPriorPeriodNotPostedMsg:str = obj["parameters"]
      self.txtPeriodAlreadyPostedMsg:str = obj["parameters"]
      self.txtPeriodAlreadyGeneratedMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateRateGroupStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.strInactiveRateType:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateSrcAdjustFromFiscalPeriod_input:
   """ Required : 
   proposedAdjustFromFiscalPeriod
   ds
   """  
   def __init__(self, obj):
      self.proposedAdjustFromFiscalPeriod:int = obj["proposedAdjustFromFiscalPeriod"]
      """  The proposed Adjust From Fiscal Year  """  
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      pass

class ValidateSrcAdjustFromFiscalPeriod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateSrcFiscalPeriod_input:
   """ Required : 
   proposedFiscalPeriod
   ds
   """  
   def __init__(self, obj):
      self.proposedFiscalPeriod:int = obj["proposedFiscalPeriod"]
      """  The proposed fiscal period  """  
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      pass

class ValidateSrcFiscalPeriod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConsolidToParentTableset] = obj["ds"]
      self.opcMsg:str = obj["parameters"]
      self.opClosingPeriod:int = obj["parameters"]
      pass

      """  output parameters  """  

