import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CompanySvc
# Description: Company Configuration Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Companies(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Companies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Companies
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies",headers=creds) as resp:
           return await resp.json()

async def post_Companies(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Companies
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1(Company1, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Company item
   Description: Calls GetByID to retrieve the Company item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Company
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Companies_Company1(Company1, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Company for the service
   Description: Calls UpdateExt to update Company. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Company
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Companies_Company1(Company1, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Company item
   Description: Call UpdateExt to delete Company item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Company
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_AGCompanies(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AGCompanies items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AGCompanies1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AGCompanyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/AGCompanies",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_AGCompanies_Company(Company1, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AGCompany item
   Description: Calls GetByID to retrieve the AGCompany item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AGCompany1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AGCompanyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/AGCompanies(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_APSysts(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get APSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APSysts1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/APSysts",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_APSysts_Company(Company1, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APSyst item
   Description: Calls GetByID to retrieve the APSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APSyst1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/APSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_ARSysts(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ARSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ARSysts1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/ARSysts",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_ARSysts_Company(Company1, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARSyst item
   Description: Calls GetByID to retrieve the ARSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARSyst1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/ARSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_BMSysts(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BMSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BMSysts1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BMSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/BMSysts",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_BMSysts_Company(Company1, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BMSyst item
   Description: Calls GetByID to retrieve the BMSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BMSyst1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BMSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/BMSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_BorderPcts(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BorderPcts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BorderPcts1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BorderPctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/BorderPcts",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_BorderPcts_Company_DestCountryNum(Company1, Company, DestCountryNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BorderPct item
   Description: Calls GetByID to retrieve the BorderPct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BorderPct1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DestCountryNum: Desc: DestCountryNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BorderPctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/BorderPcts(" + Company + "," + DestCountryNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_CRSysts(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CRSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CRSysts1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CRSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/CRSysts",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_CRSysts_Company(Company1, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CRSyst item
   Description: Calls GetByID to retrieve the CRSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CRSyst1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CRSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/CRSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_CSFSysts(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CSFSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CSFSysts1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CSFSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/CSFSysts",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_CSFSysts_Company(Company1, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CSFSyst item
   Description: Calls GetByID to retrieve the CSFSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CSFSyst1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CSFSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/CSFSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_Currencies(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get Currencies items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_Currencies1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrencyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/Currencies",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_Currencies_Company_CurrencyCode(Company1, Company, CurrencyCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Currency item
   Description: Calls GetByID to retrieve the Currency item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Currency1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CurrencyCode: Desc: CurrencyCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CurrencyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/Currencies(" + Company + "," + CurrencyCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_CurrRateGrps(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CurrRateGrps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CurrRateGrps1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrRateGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/CurrRateGrps",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_CurrRateGrps_Company_RateGrpCode(Company1, Company, RateGrpCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CurrRateGrp item
   Description: Calls GetByID to retrieve the CurrRateGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrRateGrp1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CurrRateGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/CurrRateGrps(" + Company + "," + RateGrpCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_EQSysts(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EQSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EQSysts1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EQSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/EQSysts",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_EQSysts_Company(Company1, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EQSyst item
   Description: Calls GetByID to retrieve the EQSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EQSyst1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EQSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/EQSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_ExtPRSysts(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ExtPRSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtPRSysts1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPRSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/ExtPRSysts",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_ExtPRSysts_Company(Company1, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtPRSyst item
   Description: Calls GetByID to retrieve the ExtPRSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtPRSyst1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtPRSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/ExtPRSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_FsSysts(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FsSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FsSysts1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FsSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/FsSysts",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_FsSysts_Company(Company1, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FsSyst item
   Description: Calls GetByID to retrieve the FsSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FsSyst1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FsSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/FsSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_GLSysts(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLSysts1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/GLSysts",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_GLSysts_Company(Company1, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLSyst item
   Description: Calls GetByID to retrieve the GLSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLSyst1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/GLSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_ISSysts(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ISSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ISSysts1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ISSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/ISSysts",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_ISSysts_Company(Company1, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ISSyst item
   Description: Calls GetByID to retrieve the ISSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ISSyst1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ISSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/ISSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_JCSysts(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get JCSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_JCSysts1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JCSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/JCSysts",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_JCSysts_Company(Company1, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JCSyst item
   Description: Calls GetByID to retrieve the JCSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JCSyst1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JCSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/JCSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_MMSysts(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MMSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MMSysts1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MMSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/MMSysts",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_MMSysts_Company(Company1, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MMSyst item
   Description: Calls GetByID to retrieve the MMSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MMSyst1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MMSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/MMSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_PDMSysts(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PDMSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PDMSysts1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PDMSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/PDMSysts",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_PDMSysts_Company(Company1, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PDMSyst item
   Description: Calls GetByID to retrieve the PDMSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PDMSyst1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PDMSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/PDMSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_PECompWhldHists(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PECompWhldHists items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PECompWhldHists1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PECompWhldHistRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/PECompWhldHists",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_PECompWhldHists_Company_RecordSeq(Company1, Company, RecordSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PECompWhldHist item
   Description: Calls GetByID to retrieve the PECompWhldHist item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PECompWhldHist1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RecordSeq: Desc: RecordSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PECompWhldHistRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/PECompWhldHists(" + Company + "," + RecordSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_PRSysts(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PRSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PRSysts1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/PRSysts",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_PRSysts_Company(Company1, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRSyst item
   Description: Calls GetByID to retrieve the PRSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRSyst1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/PRSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_TaxSvcConfigs(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TaxSvcConfigs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxSvcConfigs1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcConfigRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/TaxSvcConfigs",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_TaxSvcConfigs_Company(Company1, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxSvcConfig item
   Description: Calls GetByID to retrieve the TaxSvcConfig item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxSvcConfig1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxSvcConfigRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/TaxSvcConfigs(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_XaSysts(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get XaSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_XaSysts1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.XaSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/XaSysts",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_XaSysts_Company(Company1, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the XaSyst item
   Description: Calls GetByID to retrieve the XaSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_XaSyst1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.XaSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/XaSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_XbSysts(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get XbSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_XbSysts1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.XbSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/XbSysts",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_XbSysts_Company(Company1, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the XbSyst item
   Description: Calls GetByID to retrieve the XbSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_XbSyst1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.XbSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/XbSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_EntityGLCs(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company1, Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_CompanyAttches(Company1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CompanyAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CompanyAttches1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CompanyAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/CompanyAttches",headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1_CompanyAttches_Company_DrawingSeq(Company1, Company, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CompanyAttch item
   Description: Calls GetByID to retrieve the CompanyAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CompanyAttch1
      :param Company1: Desc: Company1   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CompanyAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/CompanyAttches(" + Company + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_AGCompanies(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AGCompanies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AGCompanies
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AGCompanyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/AGCompanies",headers=creds) as resp:
           return await resp.json()

async def post_AGCompanies(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AGCompanies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AGCompanyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AGCompanyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/AGCompanies", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AGCompanies_Company(Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AGCompany item
   Description: Calls GetByID to retrieve the AGCompany item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AGCompany
      :param Company: Desc: Company   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AGCompanyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/AGCompanies(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AGCompanies_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AGCompany for the service
   Description: Calls UpdateExt to update AGCompany. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AGCompany
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AGCompanyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/AGCompanies(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AGCompanies_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AGCompany item
   Description: Call UpdateExt to delete AGCompany item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AGCompany
      :param Company: Desc: Company   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/AGCompanies(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_APSysts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APSysts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/APSysts",headers=creds) as resp:
           return await resp.json()

async def post_APSysts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APSysts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/APSysts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APSysts_Company(Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APSyst item
   Description: Calls GetByID to retrieve the APSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APSyst
      :param Company: Desc: Company   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/APSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APSysts_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APSyst for the service
   Description: Calls UpdateExt to update APSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APSyst
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/APSysts(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APSysts_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APSyst item
   Description: Call UpdateExt to delete APSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APSyst
      :param Company: Desc: Company   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/APSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_ARSysts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ARSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARSysts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ARSysts",headers=creds) as resp:
           return await resp.json()

async def post_ARSysts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARSysts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ARSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ARSysts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ARSysts_Company(Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARSyst item
   Description: Calls GetByID to retrieve the ARSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARSyst
      :param Company: Desc: Company   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ARSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ARSysts_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ARSyst for the service
   Description: Calls UpdateExt to update ARSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARSyst
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ARSysts(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ARSysts_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ARSyst item
   Description: Call UpdateExt to delete ARSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARSyst
      :param Company: Desc: Company   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ARSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_BMSysts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BMSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BMSysts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BMSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/BMSysts",headers=creds) as resp:
           return await resp.json()

async def post_BMSysts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BMSysts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BMSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BMSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/BMSysts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BMSysts_Company(Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BMSyst item
   Description: Calls GetByID to retrieve the BMSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BMSyst
      :param Company: Desc: Company   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BMSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/BMSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BMSysts_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BMSyst for the service
   Description: Calls UpdateExt to update BMSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BMSyst
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BMSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/BMSysts(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BMSysts_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BMSyst item
   Description: Call UpdateExt to delete BMSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BMSyst
      :param Company: Desc: Company   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/BMSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_BorderPcts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BorderPcts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BorderPcts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BorderPctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/BorderPcts",headers=creds) as resp:
           return await resp.json()

async def post_BorderPcts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BorderPcts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BorderPctRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BorderPctRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/BorderPcts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BorderPcts_Company_DestCountryNum(Company, DestCountryNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BorderPct item
   Description: Calls GetByID to retrieve the BorderPct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BorderPct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DestCountryNum: Desc: DestCountryNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BorderPctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/BorderPcts(" + Company + "," + DestCountryNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BorderPcts_Company_DestCountryNum(Company, DestCountryNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BorderPct for the service
   Description: Calls UpdateExt to update BorderPct. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BorderPct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DestCountryNum: Desc: DestCountryNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BorderPctRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/BorderPcts(" + Company + "," + DestCountryNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BorderPcts_Company_DestCountryNum(Company, DestCountryNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BorderPct item
   Description: Call UpdateExt to delete BorderPct item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BorderPct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DestCountryNum: Desc: DestCountryNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/BorderPcts(" + Company + "," + DestCountryNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_CRSysts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CRSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CRSysts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CRSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CRSysts",headers=creds) as resp:
           return await resp.json()

async def post_CRSysts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CRSysts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CRSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CRSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CRSysts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CRSysts_Company(Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CRSyst item
   Description: Calls GetByID to retrieve the CRSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CRSyst
      :param Company: Desc: Company   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CRSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CRSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CRSysts_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CRSyst for the service
   Description: Calls UpdateExt to update CRSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CRSyst
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CRSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CRSysts(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CRSysts_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CRSyst item
   Description: Call UpdateExt to delete CRSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CRSyst
      :param Company: Desc: Company   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CRSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_CSFSysts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CSFSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CSFSysts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CSFSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CSFSysts",headers=creds) as resp:
           return await resp.json()

async def post_CSFSysts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CSFSysts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CSFSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CSFSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CSFSysts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CSFSysts_Company(Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CSFSyst item
   Description: Calls GetByID to retrieve the CSFSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CSFSyst
      :param Company: Desc: Company   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CSFSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CSFSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CSFSysts_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CSFSyst for the service
   Description: Calls UpdateExt to update CSFSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CSFSyst
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CSFSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CSFSysts(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CSFSysts_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CSFSyst item
   Description: Call UpdateExt to delete CSFSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CSFSyst
      :param Company: Desc: Company   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CSFSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_Currencies(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Currencies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Currencies
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrencyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Currencies",headers=creds) as resp:
           return await resp.json()

async def post_Currencies(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Currencies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CurrencyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CurrencyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Currencies", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Currencies_Company_CurrencyCode(Company, CurrencyCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Currency item
   Description: Calls GetByID to retrieve the Currency item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Currency
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CurrencyCode: Desc: CurrencyCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CurrencyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Currencies(" + Company + "," + CurrencyCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Currencies_Company_CurrencyCode(Company, CurrencyCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Currency for the service
   Description: Calls UpdateExt to update Currency. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Currency
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CurrencyCode: Desc: CurrencyCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CurrencyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Currencies(" + Company + "," + CurrencyCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Currencies_Company_CurrencyCode(Company, CurrencyCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Currency item
   Description: Call UpdateExt to delete Currency item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Currency
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CurrencyCode: Desc: CurrencyCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Currencies(" + Company + "," + CurrencyCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_CurrRateGrps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CurrRateGrps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CurrRateGrps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrRateGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CurrRateGrps",headers=creds) as resp:
           return await resp.json()

async def post_CurrRateGrps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CurrRateGrps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CurrRateGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CurrRateGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CurrRateGrps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CurrRateGrps_Company_RateGrpCode(Company, RateGrpCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CurrRateGrp item
   Description: Calls GetByID to retrieve the CurrRateGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrRateGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CurrRateGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CurrRateGrps_Company_RateGrpCode(Company, RateGrpCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CurrRateGrp for the service
   Description: Calls UpdateExt to update CurrRateGrp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CurrRateGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CurrRateGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CurrRateGrps_Company_RateGrpCode(Company, RateGrpCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CurrRateGrp item
   Description: Call UpdateExt to delete CurrRateGrp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CurrRateGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RateGrpCode: Desc: RateGrpCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_EQSysts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EQSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EQSysts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EQSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/EQSysts",headers=creds) as resp:
           return await resp.json()

async def post_EQSysts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EQSysts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EQSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EQSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/EQSysts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EQSysts_Company(Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EQSyst item
   Description: Calls GetByID to retrieve the EQSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EQSyst
      :param Company: Desc: Company   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EQSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/EQSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EQSysts_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EQSyst for the service
   Description: Calls UpdateExt to update EQSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EQSyst
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EQSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/EQSysts(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EQSysts_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EQSyst item
   Description: Call UpdateExt to delete EQSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EQSyst
      :param Company: Desc: Company   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/EQSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_ExtPRSysts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtPRSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtPRSysts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPRSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ExtPRSysts",headers=creds) as resp:
           return await resp.json()

async def post_ExtPRSysts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtPRSysts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtPRSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtPRSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ExtPRSysts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtPRSysts_Company(Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtPRSyst item
   Description: Calls GetByID to retrieve the ExtPRSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtPRSyst
      :param Company: Desc: Company   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtPRSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ExtPRSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtPRSysts_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtPRSyst for the service
   Description: Calls UpdateExt to update ExtPRSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtPRSyst
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtPRSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ExtPRSysts(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtPRSysts_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtPRSyst item
   Description: Call UpdateExt to delete ExtPRSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtPRSyst
      :param Company: Desc: Company   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ExtPRSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_FsSysts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FsSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FsSysts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FsSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/FsSysts",headers=creds) as resp:
           return await resp.json()

async def post_FsSysts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FsSysts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FsSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FsSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/FsSysts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FsSysts_Company(Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FsSyst item
   Description: Calls GetByID to retrieve the FsSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FsSyst
      :param Company: Desc: Company   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FsSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/FsSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FsSysts_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FsSyst for the service
   Description: Calls UpdateExt to update FsSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FsSyst
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FsSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/FsSysts(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FsSysts_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FsSyst item
   Description: Call UpdateExt to delete FsSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FsSyst
      :param Company: Desc: Company   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/FsSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLSysts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLSysts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GLSysts",headers=creds) as resp:
           return await resp.json()

async def post_GLSysts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLSysts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GLSysts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLSysts_Company(Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLSyst item
   Description: Calls GetByID to retrieve the GLSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLSyst
      :param Company: Desc: Company   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GLSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLSysts_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLSyst for the service
   Description: Calls UpdateExt to update GLSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLSyst
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GLSysts(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLSysts_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLSyst item
   Description: Call UpdateExt to delete GLSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLSyst
      :param Company: Desc: Company   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GLSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_ISSysts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ISSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ISSysts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ISSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ISSysts",headers=creds) as resp:
           return await resp.json()

async def post_ISSysts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ISSysts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ISSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ISSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ISSysts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ISSysts_Company(Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ISSyst item
   Description: Calls GetByID to retrieve the ISSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ISSyst
      :param Company: Desc: Company   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ISSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ISSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ISSysts_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ISSyst for the service
   Description: Calls UpdateExt to update ISSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ISSyst
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ISSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ISSysts(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ISSysts_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ISSyst item
   Description: Call UpdateExt to delete ISSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ISSyst
      :param Company: Desc: Company   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ISSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_JCSysts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get JCSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JCSysts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JCSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/JCSysts",headers=creds) as resp:
           return await resp.json()

async def post_JCSysts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JCSysts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JCSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JCSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/JCSysts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_JCSysts_Company(Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JCSyst item
   Description: Calls GetByID to retrieve the JCSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JCSyst
      :param Company: Desc: Company   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JCSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/JCSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_JCSysts_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update JCSyst for the service
   Description: Calls UpdateExt to update JCSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JCSyst
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JCSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/JCSysts(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_JCSysts_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete JCSyst item
   Description: Call UpdateExt to delete JCSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JCSyst
      :param Company: Desc: Company   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/JCSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_MMSysts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MMSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MMSysts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MMSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/MMSysts",headers=creds) as resp:
           return await resp.json()

async def post_MMSysts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MMSysts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MMSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MMSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/MMSysts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MMSysts_Company(Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MMSyst item
   Description: Calls GetByID to retrieve the MMSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MMSyst
      :param Company: Desc: Company   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MMSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/MMSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MMSysts_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MMSyst for the service
   Description: Calls UpdateExt to update MMSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MMSyst
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MMSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/MMSysts(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MMSysts_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MMSyst item
   Description: Call UpdateExt to delete MMSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MMSyst
      :param Company: Desc: Company   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/MMSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_PDMSysts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PDMSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PDMSysts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PDMSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PDMSysts",headers=creds) as resp:
           return await resp.json()

async def post_PDMSysts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PDMSysts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PDMSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PDMSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PDMSysts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PDMSysts_Company(Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PDMSyst item
   Description: Calls GetByID to retrieve the PDMSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PDMSyst
      :param Company: Desc: Company   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PDMSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PDMSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PDMSysts_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PDMSyst for the service
   Description: Calls UpdateExt to update PDMSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PDMSyst
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PDMSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PDMSysts(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PDMSysts_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PDMSyst item
   Description: Call UpdateExt to delete PDMSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PDMSyst
      :param Company: Desc: Company   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PDMSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_PECompWhldHists(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PECompWhldHists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PECompWhldHists
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PECompWhldHistRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PECompWhldHists",headers=creds) as resp:
           return await resp.json()

async def post_PECompWhldHists(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PECompWhldHists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PECompWhldHistRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PECompWhldHistRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PECompWhldHists", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PECompWhldHists_Company_RecordSeq(Company, RecordSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PECompWhldHist item
   Description: Calls GetByID to retrieve the PECompWhldHist item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PECompWhldHist
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RecordSeq: Desc: RecordSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PECompWhldHistRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PECompWhldHists(" + Company + "," + RecordSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PECompWhldHists_Company_RecordSeq(Company, RecordSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PECompWhldHist for the service
   Description: Calls UpdateExt to update PECompWhldHist. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PECompWhldHist
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RecordSeq: Desc: RecordSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PECompWhldHistRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PECompWhldHists(" + Company + "," + RecordSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PECompWhldHists_Company_RecordSeq(Company, RecordSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PECompWhldHist item
   Description: Call UpdateExt to delete PECompWhldHist item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PECompWhldHist
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RecordSeq: Desc: RecordSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PECompWhldHists(" + Company + "," + RecordSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PRSysts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PRSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRSysts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PRSysts",headers=creds) as resp:
           return await resp.json()

async def post_PRSysts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRSysts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PRSysts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PRSysts_Company(Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRSyst item
   Description: Calls GetByID to retrieve the PRSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRSyst
      :param Company: Desc: Company   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PRSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PRSysts_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PRSyst for the service
   Description: Calls UpdateExt to update PRSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRSyst
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PRSysts(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PRSysts_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PRSyst item
   Description: Call UpdateExt to delete PRSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRSyst
      :param Company: Desc: Company   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PRSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxSvcConfigs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxSvcConfigs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxSvcConfigs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcConfigRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/TaxSvcConfigs",headers=creds) as resp:
           return await resp.json()

async def post_TaxSvcConfigs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxSvcConfigs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxSvcConfigRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxSvcConfigRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/TaxSvcConfigs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxSvcConfigs_Company(Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxSvcConfig item
   Description: Calls GetByID to retrieve the TaxSvcConfig item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxSvcConfig
      :param Company: Desc: Company   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxSvcConfigRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/TaxSvcConfigs(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxSvcConfigs_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxSvcConfig for the service
   Description: Calls UpdateExt to update TaxSvcConfig. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxSvcConfig
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxSvcConfigRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/TaxSvcConfigs(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxSvcConfigs_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxSvcConfig item
   Description: Call UpdateExt to delete TaxSvcConfig item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxSvcConfig
      :param Company: Desc: Company   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/TaxSvcConfigs(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_XaSysts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get XaSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_XaSysts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.XaSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/XaSysts",headers=creds) as resp:
           return await resp.json()

async def post_XaSysts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_XaSysts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.XaSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.XaSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/XaSysts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_XaSysts_Company(Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the XaSyst item
   Description: Calls GetByID to retrieve the XaSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_XaSyst
      :param Company: Desc: Company   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.XaSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/XaSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_XaSysts_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update XaSyst for the service
   Description: Calls UpdateExt to update XaSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_XaSyst
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.XaSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/XaSysts(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_XaSysts_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete XaSyst item
   Description: Call UpdateExt to delete XaSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_XaSyst
      :param Company: Desc: Company   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/XaSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_XbSysts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get XbSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_XbSysts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.XbSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/XbSysts",headers=creds) as resp:
           return await resp.json()

async def post_XbSysts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_XbSysts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.XbSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.XbSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/XbSysts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_XbSysts_Company(Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the XbSyst item
   Description: Calls GetByID to retrieve the XbSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_XbSyst
      :param Company: Desc: Company   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.XbSystRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/XbSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_XbSysts_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update XbSyst for the service
   Description: Calls UpdateExt to update XbSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_XbSyst
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.XbSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/XbSysts(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_XbSysts_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete XbSyst item
   Description: Call UpdateExt to delete XbSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_XbSyst
      :param Company: Desc: Company   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/XbSysts(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EntityGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def post_EntityGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EntityGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/EntityGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EntityGLC for the service
   Description: Calls UpdateExt to update EntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EntityGLC item
   Description: Call UpdateExt to delete EntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_CompanyAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CompanyAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CompanyAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CompanyAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CompanyAttches",headers=creds) as resp:
           return await resp.json()

async def post_CompanyAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CompanyAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CompanyAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CompanyAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CompanyAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CompanyAttches_Company_DrawingSeq(Company, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CompanyAttch item
   Description: Calls GetByID to retrieve the CompanyAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CompanyAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CompanyAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CompanyAttches(" + Company + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CompanyAttches_Company_DrawingSeq(Company, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CompanyAttch for the service
   Description: Calls UpdateExt to update CompanyAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CompanyAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CompanyAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CompanyAttches(" + Company + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CompanyAttches_Company_DrawingSeq(Company, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CompanyAttch item
   Description: Call UpdateExt to delete CompanyAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CompanyAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CompanyAttches(" + Company + "," + DrawingSeq + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCompany, whereClauseCompanyAttch, whereClauseAGCompany, whereClauseAPSyst, whereClauseARSyst, whereClauseBMSyst, whereClauseBorderPct, whereClauseCRSyst, whereClauseCSFSyst, whereClauseCurrency, whereClauseCurrRateGrp, whereClauseEQSyst, whereClauseExtPRSyst, whereClauseFsSyst, whereClauseGLSyst, whereClauseISSyst, whereClauseJCSyst, whereClauseMMSyst, whereClausePDMSyst, whereClausePECompWhldHist, whereClausePRSyst, whereClauseTaxSvcConfig, whereClauseXaSyst, whereClauseXbSyst, whereClauseEntityGLC, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCompanyAttch=" + whereClauseCompanyAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAGCompany=" + whereClauseAGCompany
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAPSyst=" + whereClauseAPSyst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseARSyst=" + whereClauseARSyst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBMSyst=" + whereClauseBMSyst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBorderPct=" + whereClauseBorderPct
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCRSyst=" + whereClauseCRSyst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCSFSyst=" + whereClauseCSFSyst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCurrency=" + whereClauseCurrency
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCurrRateGrp=" + whereClauseCurrRateGrp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEQSyst=" + whereClauseEQSyst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseExtPRSyst=" + whereClauseExtPRSyst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFsSyst=" + whereClauseFsSyst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLSyst=" + whereClauseGLSyst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseISSyst=" + whereClauseISSyst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseJCSyst=" + whereClauseJCSyst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMMSyst=" + whereClauseMMSyst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePDMSyst=" + whereClausePDMSyst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePECompWhldHist=" + whereClausePECompWhldHist
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePRSyst=" + whereClausePRSyst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaxSvcConfig=" + whereClauseTaxSvcConfig
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseXaSyst=" + whereClauseXaSyst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseXbSyst=" + whereClauseXbSyst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEntityGLC=" + whereClauseEntityGLC
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(company, epicorHeaders = None):
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
   params += "company=" + company

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeJPFiscalCalendarID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeJPFiscalCalendarID
   Description: Performs required logic when XbSyst.JPFiscalCalendarID is modified.
   OperationID: ChangeJPFiscalCalendarID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeJPFiscalCalendarID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJPFiscalCalendarID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSendToFSA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSendToFSA
   Description: Performs required logic when Company.SendToFSA is modified.
   OperationID: ChangeSendToFSA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSendToFSA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSendToFSA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckAPTaxLnLevel(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckAPTaxLnLevel
   Description: This method will determine if the APTaxLnLevel is changing and output a message to the user
   OperationID: CheckAPTaxLnLevel
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckAPTaxLnLevel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAPTaxLnLevel_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckARinvcDates(epicorHeaders = None):
   """  
   Summary: Invoke method CheckARinvcDates
   Description: This method test the link of the dates in AR Invoice
   OperationID: CheckARinvcDates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckARinvcDates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_CheckDefTaxLiability(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDefTaxLiability
   Description: This method checks whether Tax Liability exists and not flagged as used in Tax Connect
   OperationID: CheckDefTaxLiability
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDefTaxLiability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDefTaxLiability_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDefTaxType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDefTaxType
   Description: This method checks whether Tax Type exists
   OperationID: CheckDefTaxType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDefTaxType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDefTaxType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPayrollDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPayrollDate
   Description: This method is to be run before the update method (or on leave of the field).
If there is a problem with the date, a message will be returned for the user to approve
or cancel.  If the user approved the error, then the update method can be run.
   OperationID: CheckPayrollDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPayrollDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPayrollDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckRedStornoOpt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckRedStornoOpt
   Description: Prevent setting this option if tran type docs have red storno set
   OperationID: CheckRedStornoOpt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRedStornoOpt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRedStornoOpt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckUDCodeEx(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckUDCodeEx
   Description: Checks whether user-defined code exists and active.
   OperationID: CheckUDCodeEx
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckUDCodeEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckUDCodeEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckUDCodesExistence(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckUDCodesExistence
   Description: Checks whether user-defined code exists and active.
   OperationID: CheckUDCodesExistence
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckUDCodesExistence_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckUDCodesExistence_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckVATFormat(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckVATFormat
   Description: This method test the validity of the VAT format
   OperationID: CheckVATFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckVATFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckVATFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChgCompanyFisCal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChgCompanyFisCal
   Description: none
   OperationID: ChgCompanyFisCal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChgCompanyFisCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChgCompanyFisCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChgCountry(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChgCountry
   Description: This method defaults the tax region information when the Company.CountryNum
field changes
   OperationID: ChgCountry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChgCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChgCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChgingMJTemplate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChgingMJTemplate
   Description: This method defaults the Maintenance Job Description when the MMSyst.TemplateJobNum
field changes
   OperationID: ChgingMJTemplate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChgingMJTemplate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChgingMJTemplate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChgJCSystForecastPeriods(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChgJCSystForecastPeriods
   Description: none
   OperationID: ChgJCSystForecastPeriods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChgJCSystForecastPeriods_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChgJCSystForecastPeriods_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CleanHCMLink(epicorHeaders = None):
   """  
   Summary: Invoke method CleanHCMLink
   Description: This method remove all HCM Link on related Payroll tables.
   OperationID: CleanHCMLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CleanHCMLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_DisabledGLFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DisabledGLFields
   Description: This method sens back a list of fields to be disabled
   OperationID: DisabledGLFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DisabledGLFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisabledGLFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ETCAfterAddrVal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ETCAfterAddrVal
   Description: After the tax integration has been called, update the Company address if it
was changed.
   OperationID: ETCAfterAddrVal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ETCAfterAddrVal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ETCAfterAddrVal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ETCValidateAddress(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ETCValidateAddress
   Description: Call tax integration and loads temp tables from the results.
   OperationID: ETCValidateAddress
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ETCValidateAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ETCValidateAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FormatList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FormatList
   Description: This method returns the list of available G/L account format styles
   OperationID: FormatList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FormatList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FormatList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBookMethodList(epicorHeaders = None):
   """  
   Summary: Invoke method GetBookMethodList
   Description: Get list of revision statuses.
   OperationID: GetBookMethodList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBookMethodList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetCheckOffLabels(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCheckOffLabels
   Description: This method returns a delimited list of the CheckOff labels for either Job, Quote or DMR
   OperationID: GetCheckOffLabels
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCheckOffLabels_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCheckOffLabels_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCPayCompanyList(epicorHeaders = None):
   """  
   Summary: Invoke method GetCPayCompanyList
   Description: This method returns a list of valid Central Payment 'Parent Company' IDs
UI note - user should  select only ONE of the valid codes.
   OperationID: GetCPayCompanyList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCPayCompanyList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetModLicensing(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetModLicensing
   Description: This method returns the licensing flags for the company beging updates.
If updating a company different from the one logged in on, then you need
to use these variables in your licensing checks
   OperationID: GetModLicensing
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetModLicensing_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetModLicensing_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBorderPercent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBorderPercent
   Description: This method replaces the standard GetNewBorderPct() method so the Company can be
passed as a parameter
   OperationID: GetNewBorderPercent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBorderPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBorderPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSerialNumbers(epicorHeaders = None):
   """  
   Summary: Invoke method GetSerialNumbers
   Description: This method provides a list of license serial number available for use
   OperationID: GetSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBankAcctID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBankAcctID
   Description: OnChangeBankAcctID
   OperationID: OnChangeBankAcctID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeARBankAcctID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeARBankAcctID
   Description: OnChangeARankAcctID
   OperationID: OnChangeARBankAcctID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeARBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeARBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCentralCollectionParentCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCentralCollectionParentCompany
   Description: This method allow to validate if there are still customers or un-posted invoices with central collection.
   OperationID: OnChangeCentralCollectionParentCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCentralCollectionParentCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCentralCollectionParentCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeUseAltBillToAddr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeUseAltBillToAddr
   Description: OnChangeUseAltBillToAddr
   OperationID: OnChangeUseAltBillToAddr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeUseAltBillToAddr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUseAltBillToAddr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAddrValEnabled(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAddrValEnabled
   Description: OnChangeAddrValEnabled
   OperationID: OnChangeAddrValEnabled
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAddrValEnabled_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAddrValEnabled_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDefTaxLiability(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDefTaxLiability
   Description: This method should be called when Default Tax Liability is changed
   OperationID: OnChangeDefTaxLiability
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDefTaxLiability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDefTaxLiability_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFlow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFlow
   Description: This method should be called when Flow value is changed
   OperationID: OnChangeFlow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFlow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFlow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMasterChart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMasterChart
   Description: This method is called when the MasterCOA is changed.
   OperationID: OnChangeMasterChart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMasterChart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMasterChart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeGJJournalCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeGJJournalCode
   Description: This method is called when the GJJournalCode is changed.
   OperationID: OnChangeGJJournalCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeGJJournalCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeGJJournalCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingDestCountryNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingDestCountryNum
   Description: This method should be called when Destination Country is Changed
   OperationID: OnChangingDestCountryNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingDestCountryNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingDestCountryNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSiteIsLegalEntity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSiteIsLegalEntity
   Description: This method should be called when SiteIsLegalEntity is changed
   OperationID: OnChangeSiteIsLegalEntity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSiteIsLegalEntity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSiteIsLegalEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingSubRateGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingSubRateGrp
   Description: This method should be called when SubRateGrp is Changed
   OperationID: OnChangingSubRateGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingSubRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSubRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TestTaxConnection(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TestTaxConnection
   Description: This method will test the tax integration connection to Avalara
   OperationID: TestTaxConnection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestTaxConnection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestTaxConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TestExtCRMConnection(epicorHeaders = None):
   """  
   Summary: Invoke method TestExtCRMConnection
   Description: Tests the connection for Salesforce
   OperationID: TestExtCRMConnection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestExtCRMConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTranDocType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTranDocType
   Description: OnChangeTranDocType
   OperationID: OnChangeTranDocType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTranDocType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTranDocType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeELIDefReportID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeELIDefReportID
   Description: OnChangeELIDefReportID
   OperationID: OnChangeELIDefReportID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeELIDefReportID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeELIDefReportID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeELIDefEinvoicePath(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeELIDefEinvoicePath
   Description: Invoked when ELIDefEinvoicePath is changed
   OperationID: OnChangeELIDefEinvoicePath
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeELIDefEinvoicePath_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeELIDefEinvoicePath_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetOCRAlgorithmList(epicorHeaders = None):
   """  
   Summary: Invoke method GetOCRAlgorithmList
   Description: This method returns a list of valid OCR Algorithms
   OperationID: GetOCRAlgorithmList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOCRAlgorithmList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetMaxWorkQueueRecords(epicorHeaders = None):
   """  
   Summary: Invoke method GetMaxWorkQueueRecords
   Description: This method returns the value MaxWorkQueueRecords parameter in XaSyst
   OperationID: GetMaxWorkQueueRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMaxWorkQueueRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: none
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InitializeCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InitializeCompany
   Description: none
   OperationID: InitializeCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InitializeCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitializeCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSystemTimeZoneList(epicorHeaders = None):
   """  
   Summary: Invoke method GetSystemTimeZoneList
   Description: This method returns a list of Microsoft Time Zone Index Values and their corresponding display name
   OperationID: GetSystemTimeZoneList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSystemTimeZoneList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_NLCopyDigipoortSettingToAllCompanies(epicorHeaders = None):
   """  
   Summary: Invoke method NLCopyDigipoortSettingToAllCompanies
   Description: Copy Digipoort setting to all Netherlands companies
   OperationID: NLCopyDigipoortSettingToAllCompanies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/NLCopyDigipoortSettingToAllCompanies_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetInitialPath(epicorHeaders = None):
   """  
   Summary: Invoke method GetInitialPath
   Description: Get the initial default path where the  Configuration file is going to be created
   OperationID: GetInitialPath
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInitialPath_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ValidateSendToFSA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSendToFSA
   Description: Method that validates if the SendToFSA flag was changed to false.
   OperationID: ValidateSendToFSA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSendToFSA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSendToFSA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateIntrastatCodeForCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateIntrastatCodeForCompany
   Description: Method that validates if Intrastat code is configured for Company Country
   OperationID: ValidateIntrastatCodeForCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateIntrastatCodeForCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateIntrastatCodeForCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLegalNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLegalNumbers
   Description: return the tran doc types linked to legal numbers to fill the combo
   OperationID: GetLegalNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLegalNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQuickShipURL(epicorHeaders = None):
   """  
   Summary: Invoke method GetQuickShipURL
   Description: Retrieve the Quick Ship URL
   OperationID: GetQuickShipURL
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuickShipURL_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_CompanyTaxConnectEnabled(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CompanyTaxConnectEnabled
   Description: Returns if tax connect is enabled
   OperationID: CompanyTaxConnectEnabled
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CompanyTaxConnectEnabled_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CompanyTaxConnectEnabled_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CompanyTaxConnectCertCaptureEnabled(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CompanyTaxConnectCertCaptureEnabled
   Description: Returns if avalara certcapture is enabled
   OperationID: CompanyTaxConnectCertCaptureEnabled
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CompanyTaxConnectCertCaptureEnabled_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CompanyTaxConnectCertCaptureEnabled_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SiteIsLegalEntity(epicorHeaders = None):
   """  
   Summary: Invoke method SiteIsLegalEntity
   Description: Indicates site can be used as a legal entity.
   OperationID: SiteIsLegalEntity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SiteIsLegalEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ValidateMYIndustryCodeOnChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateMYIndustryCodeOnChanging
   Description: Validate and correct proposed Industry Code value
   OperationID: ValidateMYIndustryCodeOnChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateMYIndustryCodeOnChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMYIndustryCodeOnChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCompanyAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCompanyAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCompanyAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCompanyAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCompanyAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAGCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAGCompany
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAGCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAGCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAGCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPSyst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPSyst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewARSyst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewARSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARSyst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBMSyst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBMSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBMSyst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBMSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBMSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBorderPct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBorderPct
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBorderPct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBorderPct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBorderPct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCRSyst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCRSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCRSyst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCRSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCRSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCSFSyst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCSFSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCSFSyst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCSFSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCSFSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCurrency(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCurrency
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCurrency
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCurrency_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCurrency_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCurrRateGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCurrRateGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCurrRateGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCurrRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCurrRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEQSyst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEQSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEQSyst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEQSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEQSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtPRSyst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtPRSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtPRSyst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtPRSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtPRSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFsSyst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFsSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFsSyst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFsSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFsSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLSyst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLSyst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewISSyst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewISSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewISSyst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewISSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewISSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewJCSyst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewJCSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJCSyst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJCSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJCSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMMSyst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMMSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMMSyst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMMSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMMSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPDMSyst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPDMSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPDMSyst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPDMSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPDMSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPECompWhldHist(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPECompWhldHist
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPECompWhldHist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPECompWhldHist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPECompWhldHist_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPRSyst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPRSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRSyst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxSvcConfig(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxSvcConfig
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxSvcConfig
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxSvcConfig_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxSvcConfig_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewXaSyst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewXaSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewXaSyst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewXaSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewXaSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewXbSyst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewXbSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewXbSyst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewXbSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewXbSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEntityGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEntityGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AGCompanyRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AGCompanyRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APSystRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APSystRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARSystRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ARSystRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BMSystRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BMSystRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BorderPctRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BorderPctRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRSystRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CRSystRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CSFSystRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CSFSystRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CompanyAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CompanyAttchRow] = obj["value"]
      pass

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

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateGrpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CurrRateGrpRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrencyRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CurrencyRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EQSystRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EQSystRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EntityGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRSystRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtPRSystRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FsSystRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FsSystRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLSystRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLSystRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ISSystRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ISSystRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JCSystRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JCSystRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MMSystRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MMSystRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PDMSystRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PDMSystRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PECompWhldHistRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PECompWhldHistRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRSystRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PRSystRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcConfigRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxSvcConfigRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_XaSystRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_XaSystRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_XbSystRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_XbSystRow] = obj["value"]
      pass

class Erp_Tablesets_AGCompanyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GenFilesFolder:str = obj["GenFilesFolder"]
      """  Generated Files Folder  """  
      self.InvMoveMandCUIT:bool = obj["InvMoveMandCUIT"]
      """  Inventory Movement Mandatory CUIT  """  
      self.SOMandCUIT:bool = obj["SOMandCUIT"]
      """  Sales Order Mandatory CUIT  """  
      self.DefaultDestination:str = obj["DefaultDestination"]
      """  Default Import Destination  """  
      self.TransportKey:str = obj["TransportKey"]
      """  Transport Key  """  
      self.WHCertificateSigner:str = obj["WHCertificateSigner"]
      """  Withholding Certificate Signer  """  
      self.SignerPosition:str = obj["SignerPosition"]
      """  Signer Position  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.WebServiceConfigCode:str = obj["WebServiceConfigCode"]
      """  Web Service Code  """  
      self.ElectronicCreditInvMinAmt:int = obj["ElectronicCreditInvMinAmt"]
      """  ElectronicCreditInvMinAmt  """  
      self.FinOption:str = obj["FinOption"]
      """  FinOption  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SaveReceipts:bool = obj["SaveReceipts"]
      """  Indicates if Receipt transactions are to be used to create invoices. This flag is used by the Receipt entry program to set the value of the RcvHead.SaveForInvoicing.  Invoice entry pulls in receipt details  Receipt.SaveForInvoicing = Yes and Receipt.Invoiced =  No.  """  
      self.AlwaysDiscount:bool = obj["AlwaysDiscount"]
      """  Configures the A/P automatic invoice payment selection process to unconditionally take any available discount amount.  """  
      self.FmtCode:str = obj["FmtCode"]
      """  Identifies default aging format, the details of which is stored in the AgingRptFmt table.  """  
      self.DefaultFmtCode:str = obj["DefaultFmtCode"]
      """  Stores the FmtCode of the AgingRptFmt record that is to be considered the A/P default.  """  
      self.CheckPerforationLineNum:int = obj["CheckPerforationLineNum"]
      """  Used by AP Check printing.  It is the line # at which the check perforation is.  """  
      self.CPayParent:str = obj["CPayParent"]
      """  For internal use only.  Used with CPayCompany to enforce security of the Centralized Payment Parent company.  """  
      self.CPayCompany:str = obj["CPayCompany"]
      """  Company that is the Parent of Centralized Payment process.  More than one company can be attached to a serial number that has the Centralized Payment module entered.  This field designates which of those companies is the Central Payment Parent Company and can therefore create invoices flagged for centralized payment.  """  
      self.AllowReverseCharges:bool = obj["AllowReverseCharges"]
      """  Indicates if user is allowed to override the Reverse Charge Method in the AP invoice line.  """  
      self.RoundTolerance:int = obj["RoundTolerance"]
      """  It used to catch rounding differences that might occur when vendor invoices are settled in a currency different from the invoice currency  """  
      self.RoundInvoice:bool = obj["RoundInvoice"]
      """  If the value is true and in case the total balance of an invoice transaction is within the total rounding setup for the currency of the invoice the balance is automatically accepted and booked as a rounding difference.  If the value is false the user has to balance the transaction manually.  """  
      self.LogInvAccting:str = obj["LogInvAccting"]
      """   Determines how a logged invoice is processed through the accounting system.
TR = Authorization Tracking.  Logged invoices are not processed by the Posting Engine.  Logging invoices is done for tracking purposes.  Full accounting is done when the AP Invoice is created.
TA - Account for Taxes.  When logged invoices are posted, accounts payable and tax amounts are booked directly to the respective accounts, the invoice net amount is posted to a Logged Invoice Suspense Account.  The entry is removed from the suspense account when the logged invoice is converted to an AP Invoice.
S - Book All to a Suspense Account.  When the logged invoice is posted the tax invoice and net amount are posted to a Logged Invoice Suspense Account.  The entry is removed from the suspense account when the logged invoice is voided or converted to a regular AP Invoice.  """  
      self.AuthAdmins:str = obj["AuthAdmins"]
      """  List of authorized administrators who are able to mark a logged action as complete.  """  
      self.LogInvAutoAprv:bool = obj["LogInvAutoAprv"]
      """  Indicates if Logged Invoices are created in an Aprpoved state or if they must be manually approved.  If the Accounting Option is 'Authorization Tracking' logged invoices can not be auto approved.  """  
      self.GLStage:str = obj["GLStage"]
      """  First G/L Update Stage  """  
      self.NextPINum:int = obj["NextPINum"]
      """  Next available number in PI numbering sequence  """  
      self.NumDigit:int = obj["NumDigit"]
      """  Number of digits allowed for PI Numbering  """  
      self.NextExpInvSeq:int = obj["NextExpInvSeq"]
      """  Next available number sequence for ap invoices created from employee expenses.  """  
      self.InvcReadyToCalcDflt:bool = obj["InvcReadyToCalcDflt"]
      """  This flag will be used to default the InvcHead.ReadyToCalc field when an Account Payable invoice is created. Defaults to No.  """  
      self.ExchangeDateToUse:int = obj["ExchangeDateToUse"]
      """  Indicates which date to use (Apply/Invoice Date) to calculate exchange rates.  """  
      self.LNBasedOnDate:int = obj["LNBasedOnDate"]
      """  Invoice Legal Numbers based on “Apply/Invoice” Date for AP invoices and Debit Memos  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CopyExcRateDM:bool = obj["CopyExcRateDM"]
      """  Indicates that it need to copy exchange Rates during generation of AP Debit Memo.  """  
      self.CopyExcRateCorrInv:bool = obj["CopyExcRateCorrInv"]
      """  Indicates that it need to copy exchange Rates for creating AP Correction Invoice.  """  
      self.UsePODtlTaxable:bool = obj["UsePODtlTaxable"]
      """  The Taxable option from Purchase Order Entry is brought into AP Invoice Entry.  """  
      self.LNReqForInvc:bool = obj["LNReqForInvc"]
      """  Invoice Legal Number required for AP Invoices and Debit Memos.  """  
      self.ApplyAPPrePayAuto:bool = obj["ApplyAPPrePayAuto"]
      """  Apply pre-payments on accounts payable (AP) invoices automatically.  """  
      self.DatesSetUp:bool = obj["DatesSetUp"]
      """  Field to enable functionality of Dates Set Up  """  
      self.APAmdApplyDate:bool = obj["APAmdApplyDate"]
      """  Field to Allow Amend the Apply Date on AP Invoices  """  
      self.APAmdTaxPDate:bool = obj["APAmdTaxPDate"]
      """  Field to Allow Amend the Tax Point Date on AP Invoices  """  
      self.APAmdTaxRateD:bool = obj["APAmdTaxRateD"]
      """  Field to Allow Amend the Tax Rate Date on AP Invoices  """  
      self.APDefApplyDate:str = obj["APDefApplyDate"]
      """  Field to default the Apply Date on AP Invoices  """  
      self.APDefTaxPDate:str = obj["APDefTaxPDate"]
      """  Field to default the Tax Point Date on AP Invoices  """  
      self.APDefTaxRateD:str = obj["APDefTaxRateD"]
      """  Field to default the Tax Rate Date on AP Invoices  """  
      self.APLinkApplyDate:str = obj["APLinkApplyDate"]
      """  Field to link the Apply Date on AP Invoices  """  
      self.APLinkTaxPDate:str = obj["APLinkTaxPDate"]
      """  Field to link the Tax Point Date on AP Invoices  """  
      self.APLinkTaxRateD:str = obj["APLinkTaxRateD"]
      """  Field to link the Tax Rate Date on AP Invoices  """  
      self.TWAPLegNumSource:str = obj["TWAPLegNumSource"]
      """  TWAPLegNumSource  """  
      self.TWAPThresholdTax:int = obj["TWAPThresholdTax"]
      """  TWAPThresholdTax  """  
      self.TaxYear:int = obj["TaxYear"]
      """  Current Tax Year  """  
      self.PayersTIN:str = obj["PayersTIN"]
      """  Taxpayer Identification Number for Payer  """  
      self.NameControl:str = obj["NameControl"]
      """  Name Control for 1099 Payer  """  
      self.OfficeCode:str = obj["OfficeCode"]
      """  Office Code for 1099 Payer  """  
      self.Name1:str = obj["Name1"]
      """  First line of the Payer name  """  
      self.Name2:str = obj["Name2"]
      """  Second line of Payer name  """  
      self.Address1:str = obj["Address1"]
      """  First address line of the Payer address  """  
      self.Address2:str = obj["Address2"]
      """  Second address line of the Payer address  """  
      self.Address3:str = obj["Address3"]
      """  Third address line of the Payer address  """  
      self.City:str = obj["City"]
      """  City portion of the address of the Payer address  """  
      self.State:str = obj["State"]
      """  State portion of the Payer address  """  
      self.ZIP:str = obj["ZIP"]
      """  Postal code or zip code portion of the Payer address  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The phone number of the Payer  """  
      self.TransControlCode:str = obj["TransControlCode"]
      """  Transmitter Control Code  """  
      self.COExtWordAmt:str = obj["COExtWordAmt"]
      """  COExtWordAmt  """  
      self.DeferredExpCurr:int = obj["DeferredExpCurr"]
      """  DeferredExpCurr  """  
      self.AllowMultInvcReceipts:bool = obj["AllowMultInvcReceipts"]
      """  Flag that allows to create multiple invoicing of receipts  """  
      self.DaysOutstanding:int = obj["DaysOutstanding"]
      """  Days outstanding allowed. It is used to validate if the days between the invoice date and receipt date are greater or equal than this value  """  
      self.PcntTolerance:int = obj["PcntTolerance"]
      """  Percentage of tolerance that is allowed in each receipt and its invoiced and not invoiced lines  """  
      self.AmountTolerance:int = obj["AmountTolerance"]
      """  Amount of tolerance that is allowed in each receipt and its not invoiced lines  """  
      self.TaxEntityType:str = obj["TaxEntityType"]
      """  Type of the Payer  """  
      self.TaxEntitySubCat:str = obj["TaxEntitySubCat"]
      """  Subcategory of the Payer  """  
      self.ContactPerson:str = obj["ContactPerson"]
      """  Contact person name  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Role/Designation of the contact person  """  
      self.BranchName:str = obj["BranchName"]
      """  Name of the office branch  """  
      self.PayersPAN:str = obj["PayersPAN"]
      """  Permanent Account Number for Payer  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Contact person email address  """  
      self.AreaCode:str = obj["AreaCode"]
      """  Area code for the phone number of the Payer  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The fax number of the Payer  """  
      self.FutureDateAction:str = obj["FutureDateAction"]
      """  The action to take when an AP Invoice Invoice Date or Apply Date is greater than today plus the days horizon.  Options are (W)arning, (S)top, (N)one  """  
      self.FutureDateDaysHorizon:int = obj["FutureDateDaysHorizon"]
      """  The number of days beyond today's date that an AP Invoice Invoice Date or Appy Date can be.  """  
      self.US1099KFiler:str = obj["US1099KFiler"]
      """  Form 1099-K Filer  """  
      self.US1099KPSEName:str = obj["US1099KPSEName"]
      """  Form 1099-K PSE Name  """  
      self.US1099KPSEPhone:str = obj["US1099KPSEPhone"]
      """  Form 1099-K PSE Phone  """  
      self.CopyExcRateCancelInv:bool = obj["CopyExcRateCancelInv"]
      """  Indicates that the exchange rate will be copied when creating an AP Cancellation Invoice.  """  
      self.APTaxRoundOption:int = obj["APTaxRoundOption"]
      """  APTaxRoundOption  """  
      self.EInvoice:bool = obj["EInvoice"]
      """  EInvoice  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  TaxRegionCode  """  
      self.CentralizedPayment:bool = obj["CentralizedPayment"]
      """  Centralized Payment  """  
      self.US1099ReportBySite:bool = obj["US1099ReportBySite"]
      """  US1099ReportBySite  """  
      self.APTaxRptDate:int = obj["APTaxRptDate"]
      """  Indicates which date is used for TaxTran Transaction Date - AP Invoices related records  """  
      self.AuthAdminsName:str = obj["AuthAdminsName"]
      self.ExchangeDate:int = obj["ExchangeDate"]
      """  Indicates which date to use to calculate exchange rates  """  
      self.TaxRegionCodeDesc:str = obj["TaxRegionCodeDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.AgingRptFmtDescription:str = obj["AgingRptFmtDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.StartInvoiceNum:int = obj["StartInvoiceNum"]
      """  Used to establish the beginning Invoice #. When the system generates a new InvcHead it will assign the greater of (StartInvoiceNum) or (the last Invoice # on file + 1) as the invoice number.  """  
      self.SaveShipments:bool = obj["SaveShipments"]
      """  Indicates if Shipment transactions are to be used to create invoices. This flag is used by the Shipping entry program to set the value of the  "Invoiced" flag field. (see ShipHead.Invoiced).  Invoice entry generates invoices for Shipments which contain  "Invoiced" flag =  No.  """  
      self.CreditOrderAction:str = obj["CreditOrderAction"]
      """  Order Entry action to a Credit Held customer.  Valid values are "WARN" or "STOP".  WARN means that the user is given a warning, but allowed to proceed (or cancel) with the order and customer placed on credit hold.  STOP means that the order line addition/change to the order is not accepted and the order and customer are not placed on credit hold.  """  
      self.CreditShipAction:str = obj["CreditShipAction"]
      """  Shipping Entry action to a Credit Held order.  Valid values are "WARN" or "STOP".  WARN means that the user is warned that the order is on credit hold, but allowed to proceed (or cancel) with the shipment.  STOP means that the shipment for that order is not accepted.  """  
      self.SJJournalCode:str = obj["SJJournalCode"]
      """  The Journal Code of the Journal that will be used for A/R invoices. Normally this would be called Sales Journal.  """  
      self.AJJournalCode:str = obj["AJJournalCode"]
      """   The Journal Code of the Journal that will be used for A/R adjustments and application of credit memos.
Normally this would be called the Adjustments Journal.  """  
      self.UseShipDateForInvDate:bool = obj["UseShipDateForInvDate"]
      """  Use Shipment date for Invoice Date  """  
      self.DefaultFmtCode:str = obj["DefaultFmtCode"]
      """  Stores the FmtCode of the AgingRptFmt record that is to be considered the A/R default.  """  
      self.FmtCode:str = obj["FmtCode"]
      """  Identifies default aging format, the details of which is stored in the AgingRptFmt table.  """  
      self.InvcReadyToCalcDflt:bool = obj["InvcReadyToCalcDflt"]
      """  This flag will be used to default the InvcHead.ReadyToCalc field when an invoice is created. Defaults to No  """  
      self.AllowReverseCharges:bool = obj["AllowReverseCharges"]
      """  Indicates if user is allowed to override the Reverse Charge Method in the AR invoice line.  """  
      self.RoundTolerance:int = obj["RoundTolerance"]
      """  It is used to catch rounding differences that might occur when customer invoices are settled in a currency different from the invoice currency.  """  
      self.TaxARCustomRules:bool = obj["TaxARCustomRules"]
      """  if Yes it means that tax rounding and calculation level (line or total) are performed according to rules set on each customer, if NO - according to company setup  """  
      self.RlsClassCredit:str = obj["RlsClassCredit"]
      """  Credit checking relationship  """  
      self.RlsClassReport:str = obj["RlsClassReport"]
      """  Reporting relationship class  """  
      self.RlsClassPayerSold:str = obj["RlsClassPayerSold"]
      """  Payer-sold to relationship, lets payer customer pays for the sold to customer, who is billed in the invoice  """  
      self.AcrossNatAcc:bool = obj["AcrossNatAcc"]
      """  Accepts payments from any customer within the same national account, regardless of parent-child status  """  
      self.ProrateDiscToLine:bool = obj["ProrateDiscToLine"]
      """  This field is used to enable ability in Cash Receipts to prorate the discount amount back to the original sales accounts instead of the Discount Account of the module or group part.  """  
      self.LNReqForInvc:bool = obj["LNReqForInvc"]
      """  Indicates if legal numbers are required for invoices.  """  
      self.ChargeMethod:bool = obj["ChargeMethod"]
      """  Indicates how finance/late charges are calculated and charged with these two options: Percentage on Invoice Amount (Default) or Percentage on Amount Overdue.  """  
      self.OncePerInvoice:bool = obj["OncePerInvoice"]
      """  Indicates if finance charge shall only be applied once per invoice. In case it?s not checked, finance charges shall be calculated each time the process is executed.  """  
      self.CombWReminder:bool = obj["CombWReminder"]
      """  Indicates that the system will generate a combined reminder letter and finance charge invoice.  """  
      self.ARClearing:bool = obj["ARClearing"]
      """  A/R Clearing Accounting  """  
      self.AllowSettlementInDiffCurr:bool = obj["AllowSettlementInDiffCurr"]
      """  Indicates if user is allowed to set Invoice Settlement in Different Currency for Cash Receipts and Credit Memo.  """  
      self.ARDefApplyDate:str = obj["ARDefApplyDate"]
      """  Field to default the Apply Date on AR Invoices.  """  
      self.ARDefShipDate:str = obj["ARDefShipDate"]
      """  Field to default the Shipment Date on AR Invoices.  """  
      self.ARDefTaxPDate:str = obj["ARDefTaxPDate"]
      """  Field to default the Tax Point Date on AR Invoices.  """  
      self.ARDefCurrDate:str = obj["ARDefCurrDate"]
      """  Field to default the Currency Date on AR Invoices.  """  
      self.ARDefTaxRateD:str = obj["ARDefTaxRateD"]
      """  Field to default the Tax Rate Date on AR Invoices.  """  
      self.ARLinkApplyDate:str = obj["ARLinkApplyDate"]
      """  Field to link the Apply Date on AR Invoices.  """  
      self.ARLinkShipDate:str = obj["ARLinkShipDate"]
      """  Field to link the Shipment Date on AR Invoices.  """  
      self.ARLinkTaxPDate:str = obj["ARLinkTaxPDate"]
      """  Field to link the Tax Point Date on AR Invoices.  """  
      self.ARLinkCurrDate:str = obj["ARLinkCurrDate"]
      """  Field to link the Currency Date Date on AR Invoices.  """  
      self.ARLinkTaxRateD:str = obj["ARLinkTaxRateD"]
      """  Field to link the Tax Rate Date on AR Invoices.  """  
      self.ARAmdApplyDate:bool = obj["ARAmdApplyDate"]
      """  Field to Allow Amend the Apply Date on AR Invoices.  """  
      self.ARAmdShipDate:bool = obj["ARAmdShipDate"]
      """  Field to Allow Amend the Shipment Date on AR Invoices.  """  
      self.ARAmdTaxPDate:bool = obj["ARAmdTaxPDate"]
      """  Field to Allow Amend the Tax Point Date on AR Invoices.  """  
      self.ARAmdCurreDate:bool = obj["ARAmdCurreDate"]
      """  Field to Allow Amend the Currency Date on AR Invoices.  """  
      self.ARAmdTaxRateD:bool = obj["ARAmdTaxRateD"]
      """  Field to Allow Amend the Tax Rate Date on AR Invoices.  """  
      self.DatesSetUp:bool = obj["DatesSetUp"]
      """  Field to enable funcionality of Dates Set Up  """  
      self.ARDefTaxRCrD:str = obj["ARDefTaxRCrD"]
      """  Field to default the Tax Rate Date for cancellation or adjusment credit on AR Invoices.  """  
      self.ARAmdTaxRCrD:bool = obj["ARAmdTaxRCrD"]
      """  Field to Allow Amend the Tax Rate Date for cancellation or adjusment credit on AR Invoices.  """  
      self.UseAltBillToAddr:bool = obj["UseAltBillToAddr"]
      """  This field will hold the default value for InvcHead.UseAltBillTo which indicates if the Alternate Bill To address should be used for taxing instead of the ship to address.  """  
      self.CopyExchangeRate:bool = obj["CopyExchangeRate"]
      """  Flag to indicate if the Exchange Rate should be copied from the original Invoice for a Correction Invoice.  """  
      self.GLStage:str = obj["GLStage"]
      """  Indicates first PI stage that updates the G/L  """  
      self.EndorseAP:bool = obj["EndorseAP"]
      """  Endorse AP  """  
      self.GLStatus:bool = obj["GLStatus"]
      """  GL Status  """  
      self.UnapprovedStatus:str = obj["UnapprovedStatus"]
      """  Unapproved Status  """  
      self.PortfolioStatus:str = obj["PortfolioStatus"]
      """  Portfolio Status  """  
      self.BankStatus:str = obj["BankStatus"]
      """  Bank Status  """  
      self.SettledStatus:str = obj["SettledStatus"]
      """  Settled Status  """  
      self.NextPINum:int = obj["NextPINum"]
      """  Next available number in PI numbering sequence  """  
      self.NumDigit:int = obj["NumDigit"]
      """  Number of digits allowed for PI Numbering  """  
      self.PreferredBank:str = obj["PreferredBank"]
      """  Cash Receipts from sale preferred bank.  """  
      self.IsDiscountforCreditM:bool = obj["IsDiscountforCreditM"]
      """  IsDiscountforCreditM  """  
      self.MandateCounter:int = obj["MandateCounter"]
      """  MandateCounter  """  
      self.SEPADDMsgCounter:int = obj["SEPADDMsgCounter"]
      """  SEPADDMsgCounter  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllowConfirmationTax:bool = obj["AllowConfirmationTax"]
      """  Indicates that for AR Invoices the confirmation taxes can be used.  """  
      self.UseAltBillToID:bool = obj["UseAltBillToID"]
      """  UseAltBillToID  """  
      self.CopyExcRateCancelInv:bool = obj["CopyExcRateCancelInv"]
      """  CopyExcRateCancelInv  """  
      self.CopyExcRateCM:bool = obj["CopyExcRateCM"]
      """  CopyExcRateCM  """  
      self.ExchangeDate:int = obj["ExchangeDate"]
      """  ExchangeDate  """  
      self.AllowOverpaidInv:bool = obj["AllowOverpaidInv"]
      """  AllowOverpaidInv  """  
      self.AutoARBal:bool = obj["AutoARBal"]
      """  AutoARBal  """  
      self.CancelledStatus:str = obj["CancelledStatus"]
      """  CancelledStatus  """  
      self.AdjDocLevTax:bool = obj["AdjDocLevTax"]
      """  AdjDocLevTax  """  
      self.RetainCreditOverride:bool = obj["RetainCreditOverride"]
      """  RetainCreditOverride  """  
      self.LNCashRecForUnappliedRec:bool = obj["LNCashRecForUnappliedRec"]
      """  LNCashRecForUnappliedRec  """  
      self.AllowNegativeDiscount:bool = obj["AllowNegativeDiscount"]
      """  AllowNegativeDiscount  """  
      self.AllowNegativeQuantity:bool = obj["AllowNegativeQuantity"]
      """  AllowNegativeQuantity  """  
      self.UseControlledCM:bool = obj["UseControlledCM"]
      """  UseControlledCM  """  
      self.UseCopyNumInARInv:bool = obj["UseCopyNumInARInv"]
      """  Use Copy Numbers in AR Invoice  """  
      self.CreditLimitInvoiceAction:str = obj["CreditLimitInvoiceAction"]
      """  Miscellaneous AR Invoice action to a Credit Held customer.  Valid values are "WARN" or "STOPENTRY", “STOPPOST”, “IGNORE”.  WARN means that the user is given a warning, but allowed to proceed (or cancel) with the invoice.  STOPENTRY means that the user is given a message that invoice cannot be created.  STOPPOST means the user is giving a message the invoice cannot be created, but it cannot be posted until the customer is removed from credit hold.  IGNORE means no message is received but the invoice will be marked as on credit hold.  """  
      self.MaxWriteOffAmt:int = obj["MaxWriteOffAmt"]
      """  Maximum Write Off Amount  """  
      self.AllowNegativeWriteOff:bool = obj["AllowNegativeWriteOff"]
      """  Allow Negative Write Off  """  
      self.DepTaxTreatment:str = obj["DepTaxTreatment"]
      """  Invoice Deposit Tax Treatment  """  
      self.DepAllowNegativeTax:bool = obj["DepAllowNegativeTax"]
      """  Can be set = yes, if Deposit Invoice Tax treatment is Tax Shipment Net movement. Allow shipment invoice with negative net tax elements  """  
      self.DepTaxCatID:str = obj["DepTaxCatID"]
      """  Product Tax Category  """  
      self.DepInvcRequired:bool = obj["DepInvcRequired"]
      """  Require Deposit Invoice  """  
      self.DepDaysDelay:int = obj["DepDaysDelay"]
      """  Invoice Days Delay  """  
      self.DepTranDocTypeID:str = obj["DepTranDocTypeID"]
      """  Deposit transaction Document Type of type AR Invoice  """  
      self.DepShowLinkedInvc:bool = obj["DepShowLinkedInvc"]
      """  Deposit Invoices show prior linked Deposit Invoices  """  
      self.MandatoryARRemittanceSlip:bool = obj["MandatoryARRemittanceSlip"]
      """  MandatoryARRemittanceSlip  """  
      self.EndorsedToSupplierStatus:str = obj["EndorsedToSupplierStatus"]
      """  Endorsed to Supplier PI Status  """  
      self.AllowNegBal:bool = obj["AllowNegBal"]
      """  AllowNegBal  """  
      self.CColCompany:str = obj["CColCompany"]
      """  Company that is the Parent of Centralized Collection process.  This field designates which company is the Central Collection Parent Company and can therefore receive and pay the invoices flagged for centralized collection.  """  
      self.CentralCollectionForAutoInv:bool = obj["CentralCollectionForAutoInv"]
      """  Flag to indicate if Invoices created automatically will be marked for Central Collection.  """  
      self.UseBillToTaxIDInSL:bool = obj["UseBillToTaxIDInSL"]
      """  Use Bill To Tax ID in Sales List  """  
      self.SplitRevenueByTaxEffRate:bool = obj["SplitRevenueByTaxEffRate"]
      """  Split Revenue based on combination of Product Group and Tax Effective Rate GLC  """  
      self.EnableSettlementFeature:bool = obj["EnableSettlementFeature"]
      """  EnableSettlementFeature  """  
      self.ARClearingAcctDesc:str = obj["ARClearingAcctDesc"]
      self.ARClearingDept:str = obj["ARClearingDept"]
      """  XASyst.ARClearingDept  """  
      self.ARClearingDisplayAccount:str = obj["ARClearingDisplayAccount"]
      self.ARClearingDiv:str = obj["ARClearingDiv"]
      """  XASyst.ARClearingDiv  """  
      self.ARTaxRptDate:int = obj["ARTaxRptDate"]
      """  Indicates which date is used for TaxTran Transaction Date - AR Invoices related records  """  
      self.ARVoucherInvoices:bool = obj["ARVoucherInvoices"]
      """  If yes, enable IntPay acount (from GLSyst)  """  
      self.DEPTaxCatIDDescription:str = obj["DEPTaxCatIDDescription"]
      self.DepTranDocTypeLinkDescription:str = obj["DepTranDocTypeLinkDescription"]
      self.isRlsCreditEmpty:bool = obj["isRlsCreditEmpty"]
      self.isRlsPayEmpty:bool = obj["isRlsPayEmpty"]
      self.isRlsReportEmpty:bool = obj["isRlsReportEmpty"]
      self.ARClearingChart:str = obj["ARClearingChart"]
      """  XASyst.ARClearingChart  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AgingRptFmtDescription:str = obj["AgingRptFmtDescription"]
      self.AJJournalCodeJrnlDescription:str = obj["AJJournalCodeJrnlDescription"]
      self.PIStatusBStatusDesc:str = obj["PIStatusBStatusDesc"]
      self.PIStatusCStatusDesc:str = obj["PIStatusCStatusDesc"]
      self.PIStatusEToSStatusDesc:str = obj["PIStatusEToSStatusDesc"]
      self.PIStatusPStatusDesc:str = obj["PIStatusPStatusDesc"]
      self.PIStatusSStatusDesc:str = obj["PIStatusSStatusDesc"]
      self.PIStatusUStatusDesc:str = obj["PIStatusUStatusDesc"]
      self.PreferredBankDescription:str = obj["PreferredBankDescription"]
      self.PreferredBankBankName:str = obj["PreferredBankBankName"]
      self.SJJournalCodeJrnlDescription:str = obj["SJJournalCodeJrnlDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BMSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.UnapproveRevOnCheckout:bool = obj["UnapproveRevOnCheckout"]
      """  Unapprove part revisions when checked out to ECO.  """  
      self.VerifyPassword:bool = obj["VerifyPassword"]
      """  Indicates if the user's password will be verified during operations such as Rev approve/unapprove, checkout, checkin.  """  
      self.WorkflowRequired:bool = obj["WorkflowRequired"]
      """  If TRUE then a workflow group and task set is required on ECO Group records.  """  
      self.SingleUser:bool = obj["SingleUser"]
      """  If TRUE then the Engineering Workbench is limited to one user per ECO Group.  If FALSE then individual revisions within a group can be locked.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BorderPctRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DestCountryNum:int = obj["DestCountryNum"]
      """  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  """  
      self.PctAtBorder:int = obj["PctAtBorder"]
      """  This is used to calculate the percentage of the miscellaneous charge to be applied in the Intrastat.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DestCountryNumDescription:str = obj["DestCountryNumDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CRSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DefTaskSetID:str = obj["DefTaskSetID"]
      """  Company default Task set.  Used to assign to new lead/opportunity/quote when there isn't a task set for the Sales Territory for the Quote.  """  
      self.DefMktgCampaignID:str = obj["DefMktgCampaignID"]
      """  Company default Marketing Campaign.  Used to assign to a new lead/opportunity/quote.  """  
      self.DefWebMktgCampaignID:str = obj["DefWebMktgCampaignID"]
      """  Company default Web Marketing Campaign.  Used to assign to a new lead/opportunity/quote.  """  
      self.WinReasonCode:str = obj["WinReasonCode"]
      """  Default "win" reason Code.  From Reason table with Code type of "w"  """  
      self.LossReasonCode:str = obj["LossReasonCode"]
      """  Default "Loss" reason Code.  From Reason table with Code type of "L"  """  
      self.TaskReasonCode:str = obj["TaskReasonCode"]
      """  Default "Task Completion" reason Code.  From Reason table with Code type of "T"  """  
      self.CloseTasksWin:bool = obj["CloseTasksWin"]
      """  Indicates that the win Function will close all open tasks on the LOQ  """  
      self.CloseTasksLose:bool = obj["CloseTasksLose"]
      """  Indicates that the Lose Function will close all open tasks on the LOQ  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Company default Sales territory  """  
      self.DefICMktgCampaignID:str = obj["DefICMktgCampaignID"]
      """  Company default Inter-Company Marketing Campaign.  Used to assign to a new lead/opportunity/quote.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UseTerritorySecurity:bool = obj["UseTerritorySecurity"]
      """  This flag indicates if the territory security is applied to sales order. By applying territory security at SO the user only can load sales orders and customers for the territory that his workforce has access.  """  
      self.CRMCallsShown:int = obj["CRMCallsShown"]
      """  Number  of calls assigned to the owner that are loaded automatically when opening CRM Call log.  """  
      self.ExternalCRMIntegration:bool = obj["ExternalCRMIntegration"]
      """  This fields defines if the Epicor ERP CRM is integrated to an External CRM.  Only enabled if there is an active license for External CRM Integration.  """  
      self.ExternalCRMSystem:str = obj["ExternalCRMSystem"]
      """  This fields define the external software used as the Extenral CRM. The valid option are  S: Salesfore.com .  """  
      self.ExternalCRMURL:str = obj["ExternalCRMURL"]
      """  This is the URL used to integrate to the External CRM system  """  
      self.ExternalCRMMasterFile:str = obj["ExternalCRMMasterFile"]
      """  This field determines what system is used as the primary master file holder. The valid values are E : Epicor ERP  C: External CRM  """  
      self.ExternalToken:str = obj["ExternalToken"]
      """  This field defines the token used to integrate to the External CRM  """  
      self.ExternalCRMLoginID:str = obj["ExternalCRMLoginID"]
      """  This field defines the user id used to integrate to the External CRM  """  
      self.ExternalCRMPassword:str = obj["ExternalCRMPassword"]
      """  This field defines the token password to integrate to the External CRM  """  
      self.ExternalCRMTimeZoneID:str = obj["ExternalCRMTimeZoneID"]
      """  This field defines the time zone used by the External CRM. This is used in cases where the External CRM is located in a different time zone than Epicor ERP.  """  
      self.ExternalCRMDefaultICTypeID:str = obj["ExternalCRMDefaultICTypeID"]
      """  This field defines the default Industry Class Type used by the External CRM. The valid values are all the active Industry Class Type Id defined in Epicor ERP.  """  
      self.ExternalCRMLastSync:str = obj["ExternalCRMLastSync"]
      """  This field defines the last time that the External CRM has been Synchronized to Epicor ERP. This field is maintained by the External CRM Synchronization  process.  """  
      self.ExternalCRMLastSyncContact:str = obj["ExternalCRMLastSyncContact"]
      """  This field defines the last time that Customer Contacts  has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  """  
      self.ExternalCRMLastSyncCustomer:str = obj["ExternalCRMLastSyncCustomer"]
      """  This field defines the last time that the Customers  has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  """  
      self.ExternalCRMLastSyncPart:str = obj["ExternalCRMLastSyncPart"]
      """  This field defines the last time that  Part  has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  """  
      self.ExternalCRMLastSyncQuote:str = obj["ExternalCRMLastSyncQuote"]
      """  This field defines the last time that  Quotes  has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  """  
      self.ExternalCRMCreateSO:int = obj["ExternalCRMCreateSO"]
      """  This field is used by the External CRM integration only.  """  
      self.ExternalCRMPasswordMasked:str = obj["ExternalCRMPasswordMasked"]
      """  External CRM masked password.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DefICMktgCampDescription:str = obj["DefICMktgCampDescription"]
      self.DefMktgCampaignIDCampDescription:str = obj["DefMktgCampaignIDCampDescription"]
      self.DefTaskSetIDWorkflowType:str = obj["DefTaskSetIDWorkflowType"]
      self.DefTaskSetIDTaskSetDescription:str = obj["DefTaskSetIDTaskSetDescription"]
      self.DefWebMtkgCampDescription:str = obj["DefWebMtkgCampDescription"]
      self.ExternalCRMDefaultICTypeDescription:str = obj["ExternalCRMDefaultICTypeDescription"]
      self.LossReasonDescription:str = obj["LossReasonDescription"]
      self.TaskReasonDescription:str = obj["TaskReasonDescription"]
      self.TerritoryIDTerritoryDesc:str = obj["TerritoryIDTerritoryDesc"]
      self.WinReasonDescription:str = obj["WinReasonDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CSFSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxInfo1:str = obj["TaxInfo1"]
      self.TaxInfo2:str = obj["TaxInfo2"]
      self.TaxInfo3:str = obj["TaxInfo3"]
      self.TaxInfo4:str = obj["TaxInfo4"]
      self.TaxInfo5:str = obj["TaxInfo5"]
      self.TaxInfo6:str = obj["TaxInfo6"]
      self.TaxInfo7:str = obj["TaxInfo7"]
      self.TaxInfo8:str = obj["TaxInfo8"]
      self.TaxInfo9:str = obj["TaxInfo9"]
      self.TaxInfo10:str = obj["TaxInfo10"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RedStornoOpt:str = obj["RedStornoOpt"]
      """  RedStornoOpt  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CompanyAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
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
      self.Company1:str = obj["Company1"]
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

class Erp_Tablesets_CurrRateGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines if the record is inactive  """  
      self.BaseRateGrpCode:str = obj["BaseRateGrpCode"]
      """  Determins if there is a base rate group to use if no rules or rates are defined for a currency  """  
      self.CrossCurrCode:str = obj["CrossCurrCode"]
      """  Currency to use during single or double currency conversions  """  
      self.CrossRound:bool = obj["CrossRound"]
      """  Determine if rounding should be done after conversion  """  
      self.CrossRoundDec:int = obj["CrossRoundDec"]
      """  Number of decimals to use during rounding  """  
      self.AltCrossCurrCode:str = obj["AltCrossCurrCode"]
      """  Currency used for double currency conversions  """  
      self.AltCrossRound:bool = obj["AltCrossRound"]
      """  Determine if rounding should be done after conversion  """  
      self.AltCrossRoundDec:int = obj["AltCrossRoundDec"]
      """  Number of decimals to use during rounding  """  
      self.GlobalGrp:bool = obj["GlobalGrp"]
      """  Determines whether or not this rate group is shared between more than one company.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this record will receive global updates.  """  
      self.RateNumDec:int = obj["RateNumDec"]
      """  Number of decimals for the exchange rates  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableGlobalGrp:bool = obj["EnableGlobalGrp"]
      """  control when the GlobalGrp field should be enabled.  """  
      self.EnableGlobalLock:bool = obj["EnableGlobalLock"]
      """  Control when the GlobalLock field should be enabled.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency is Global (master or linked)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany and GlbRateGrpCode that is linking to this Rate Group.  """  
      self.GlbCompanyName:str = obj["GlbCompanyName"]
      """  Company Name from linked global rate group.  """  
      self.GlbRateGrpCode:str = obj["GlbRateGrpCode"]
      """  Rate group Code from linked global rate group.  """  
      self.GlbRateGrpDesc:str = obj["GlbRateGrpDesc"]
      """  Description from linked global rate group.  """  
      self.GlbCompanyID:str = obj["GlbCompanyID"]
      """  Company ID from linked global rate group.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AltCrossCurrCurrName:str = obj["AltCrossCurrCurrName"]
      self.AltCrossCurrCurrDesc:str = obj["AltCrossCurrCurrDesc"]
      self.AltCrossCurrCurrencyID:str = obj["AltCrossCurrCurrencyID"]
      self.AltCrossCurrDocumentDesc:str = obj["AltCrossCurrDocumentDesc"]
      self.AltCrossCurrCurrSymbol:str = obj["AltCrossCurrCurrSymbol"]
      self.BaseRateGrpDescDescription:str = obj["BaseRateGrpDescDescription"]
      self.CrossCurrCurrDesc:str = obj["CrossCurrCurrDesc"]
      self.CrossCurrCurrName:str = obj["CrossCurrCurrName"]
      self.CrossCurrCurrencyID:str = obj["CrossCurrCurrencyID"]
      self.CrossCurrDocumentDesc:str = obj["CrossCurrDocumentDesc"]
      self.CrossCurrCurrSymbol:str = obj["CrossCurrCurrSymbol"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CurrencyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.CurrDesc:str = obj["CurrDesc"]
      """  Description of the currency  """  
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.DocumentDesc:str = obj["DocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.Note:str = obj["Note"]
      """  Notes the about the Currency.  """  
      self.CurrName:str = obj["CurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyID:str = obj["CurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.DecimalsGeneral:int = obj["DecimalsGeneral"]
      """  Number of decimals used for any types of amounts where they entered, printed, displayed, except unit price and unit cost, according to the table zFieldDecimal where ValueType = "G"  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the currency is active  """  
      self.DecimalsPrice:int = obj["DecimalsPrice"]
      """  Number of decimals used for any unit prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "P"  """  
      self.MaintRate:bool = obj["MaintRate"]
      """  Can only maintain exchange rates for currencies with this flag checked  """  
      self.DecimalsCost:int = obj["DecimalsCost"]
      """  Number of decimals used for any cost prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "C"  """  
      self.BaseCurr:bool = obj["BaseCurr"]
      """  Indicates if this is the base currency.  Only one base currency is allowed  """  
      self.RoundMltpUnitPrice:int = obj["RoundMltpUnitPrice"]
      """  Define multiple that Unit Prices for sales related documents shall be rounded to, 0- no rounding.  """  
      self.ReportCurr:bool = obj["ReportCurr"]
      """  Indicates if this is a reporting currency  """  
      self.RoundMltpUnitTax:int = obj["RoundMltpUnitTax"]
      """  Define multiple that Unit Tax for sales related documents shall be rounded to, 0- no rounding.  """  
      self.RoundMltpExtPrice:int = obj["RoundMltpExtPrice"]
      """  Define multiple that Extended Prices (total line amount) for sales related documents shall be rounded to, 0- no rounding.  """  
      self.RoundMltpExtTax:int = obj["RoundMltpExtTax"]
      """  Define multiple that Extended Tax (total line tax) for sales related documents shall be rounded to, 0- no rounding.  """  
      self.RoundMltpTotalAmt:int = obj["RoundMltpTotalAmt"]
      """  Define multiple that Total amount for sales related documents shall be rounded to, 0- no rounding.  """  
      self.GlobalCurr:bool = obj["GlobalCurr"]
      """  Determines whether or not this currency is shared between more than one company.  """  
      self.RoundMltpTotalTax:int = obj["RoundMltpTotalTax"]
      """  Define multiple that Total Tax amount for sales related documents shall be rounded to, 0- no rounding.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this currency record will receive global updates.  """  
      self.RoundRuleUnitPrice:int = obj["RoundRuleUnitPrice"]
      """  Define the rule how Unit Price for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.ScaleFactor:int = obj["ScaleFactor"]
      """  Display factor for exchange rates  """  
      self.RoundRuleUnitTax:int = obj["RoundRuleUnitTax"]
      """  Define the rule how Unit Tax for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  """  
      self.RoundRuleExtPrice:int = obj["RoundRuleExtPrice"]
      """  Define the rule how Extended Prices (total line amount) for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.ReportCurrPos:int = obj["ReportCurrPos"]
      """  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  """  
      self.RoundRuleExtTax:int = obj["RoundRuleExtTax"]
      """  Define the rule how Extended Tax (total tax amount) for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.RoundRuleTotalAmt:int = obj["RoundRuleTotalAmt"]
      """  Define the rule how total amount for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.RoundRuleTotalTax:int = obj["RoundRuleTotalTax"]
      """  Define the rule how total tax amount for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.RoundTolerance:int = obj["RoundTolerance"]
      """  It used in AP Invoice, if the rounding amount remaining is less or equal to the tolerance, the remaining amount is automatically booked.  """  
      self.ISONumber:int = obj["ISONumber"]
      """  ISO unique identifier  """  
      self.StoreID:str = obj["StoreID"]
      """  Store ID for Credit Card Processing  """  
      self.RoundMltpAnnualCharge:int = obj["RoundMltpAnnualCharge"]
      """  Define multiple that Annual Depreciation Charge for asset related documents shall be rounded to, 0- no rounding.  """  
      self.RoundMltpPeriodCharge:int = obj["RoundMltpPeriodCharge"]
      """  Define multiple that Period Depreciation Charge for asset  related documents shall be rounded to, 0- no rounding.  """  
      self.RoundRuleAnnualCharge:int = obj["RoundRuleAnnualCharge"]
      """  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.RoundRulePeriodCharge:int = obj["RoundRulePeriodCharge"]
      """  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGAFIPCode:str = obj["AGAFIPCode"]
      """  AGAFIPCode  """  
      self.ISOCurrCode:str = obj["ISOCurrCode"]
      """  This Currency Code is used for CRE Processors.  """  
      self.ProcessorNum:int = obj["ProcessorNum"]
      """  ProcessorNum  """  
      self.BookCurr:bool = obj["BookCurr"]
      self.CompanyBase:bool = obj["CompanyBase"]
      self.CountryName:str = obj["CountryName"]
      """  Name of Country.  """  
      self.EnableBaseCurr:bool = obj["EnableBaseCurr"]
      """  Control when the Base Currency should be enable.  """  
      self.EnableDecimals:bool = obj["EnableDecimals"]
      """  If currency exist in any transaction the decimals fields should be disables.  """  
      self.EnableGlobalCurr:bool = obj["EnableGlobalCurr"]
      """  control when the Global Currency field should be enable.  """  
      self.EnableGlobalLock:bool = obj["EnableGlobalLock"]
      """  Control when the GlobalLock field should be enable.  """  
      self.EnableInactive:bool = obj["EnableInactive"]
      """  Control when the Inactive field should be enable.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  GlbCompany that is linked to this currency  """  
      self.GlbCompanyName:str = obj["GlbCompanyName"]
      """  GlbCompany Name that is linked to this currency  """  
      self.GlbCurrDesc:str = obj["GlbCurrDesc"]
      """  GlbCurrency Description that is linked to this currency  """  
      self.GlbCurrencyCode:str = obj["GlbCurrencyCode"]
      """  GlbCurrency Code that is linked to this currency  """  
      self.GlbCurrencyID:str = obj["GlbCurrencyID"]
      """  GlbCurrency ID that is linked to this currency  """  
      self.GlbCurrSymbol:str = obj["GlbCurrSymbol"]
      """  GlbCurrency Symbol that is linked to this currency  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency is Global (master or linked)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany and GlbCurrencyCode that is linking to this currency  """  
      self.HasCCInterface:bool = obj["HasCCInterface"]
      self.BaseRowRowID:str = obj["BaseRowRowID"]
      """  This field store the RowID of the record that is marked as Base Currency.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CountryDescription:str = obj["CountryDescription"]
      self.CreditCardProcessorDesc:str = obj["CreditCardProcessorDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EQSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.StartQuoteNum:int = obj["StartQuoteNum"]
      """  Used to establish the beginning Sales Order #. When the system generates a new order it will assign the greater of (StartOrderNum) or (the last orders # on file + 1) as the order number.  """  
      self.FollowUpDays:int = obj["FollowUpDays"]
      """  A integer that express the # of days from the date quoted that someone should follow up with the customer concerning the quote. This is used by quote entry to calculate a default follow up date (QuoteHed.FollowUpDate). Default follow up date is QuoteHed.DateQuoted + EQSyst.FollowUpDays  """  
      self.ExpirationDays:int = obj["ExpirationDays"]
      """  An integer that express the # of days from the quoted date when quotes will expire. This is used by quote entry to calculate the QuoteHed.ExpirationDate  """  
      self.QuoteDueDays:int = obj["QuoteDueDays"]
      """  An integer that defines the # of days in which the quoting process needs to be completed in. Quote entry uses this in calculating the QuoteHed.DueDate.  """  
      self.CheckOff1Label:str = obj["CheckOff1Label"]
      """  Label used for the QuoteHed.CheckOff1 field.  There are 5 CheckOffLabel fields. They are all optional. If entered then the corresponding QuoteHed.CheckOff fields become active.  """  
      self.CheckOff2Label:str = obj["CheckOff2Label"]
      """  Label used for the QuoteHed.CheckOff2 field.  """  
      self.CheckOff3Label:str = obj["CheckOff3Label"]
      """  Label used for the QuoteHed.CheckOff3 field.  """  
      self.CheckOff4Label:str = obj["CheckOff4Label"]
      """  Label used for theQuoteHed.CheckOff4 field.  """  
      self.CheckOff5Label:str = obj["CheckOff5Label"]
      """  Label used for the QuoteHed.CheckOff5 field.  """  
      self.MarkUpID:str = obj["MarkUpID"]
      """  The ID that establishes link to the default QMarkUp record which was indicated as the System Wide default. Provides default markup percents used by quote entry when none are associated to the specific customer. This ID is not directly entered. Instead it is updated by the user checking a toggle box during QMarkUp maintenance indicating "System Default". This may be left blank, which indicates there are no defaults.  """  
      self.Message1:str = obj["Message1"]
      """  Footer message for bottom of quote form  """  
      self.Message2:str = obj["Message2"]
      """  Footer message for bottom of quote form  """  
      self.PreventQQChange:bool = obj["PreventQQChange"]
      """  If set to Yes, the user must change the Quote "Quoted"  flag to No before they are allowed to make any changes.  """  
      self.LogChanges:bool = obj["LogChanges"]
      """  If this is Yes, then when Quotes are set to "Quoted"  or any header flag is changed on a "Planned" job the user will be prompted to enter a description of the changes.  This option is only available when "PreventQQChange" = Yes.  """  
      self.GenQuoteQtys:bool = obj["GenQuoteQtys"]
      """  System Option to generate all the quantities from the price breaks in quote detail entry.  """  
      self.QuoReadyToCalcDflt:bool = obj["QuoReadyToCalcDflt"]
      """  This flag will be used to default the QuoteHed.ReadyToCalc field when an invoice is created. Defaults to No  """  
      self.ReduceRelQty:bool = obj["ReduceRelQty"]
      """  Option to keep the Quote Detail quantity constant.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RefreshWorksheetOD:bool = obj["RefreshWorksheetOD"]
      """  Refresh Worksheet on Demand . If this flag is check the Quote Worksheet will automatically refresh and it will only refresh if the user manually select the action in Quote Entry.  """  
      self.GetCostsFromInventory:bool = obj["GetCostsFromInventory"]
      """  GetCostsFromInventory  """  
      self.DfltExpectedQtyTo:str = obj["DfltExpectedQtyTo"]
      """  DfltExpectedQtyTo  """  
      self.DfltOrderQtyToExpQty:bool = obj["DfltOrderQtyToExpQty"]
      """  DfltOrderQtyToExpQty  """  
      self.SellingExpectedQty:int = obj["SellingExpectedQty"]
      """  SellingExpectedQty  """  
      self.UseQuoteBOM:bool = obj["UseQuoteBOM"]
      """  Quotes can be used as souce BOM if true  """  
      self.DeferQtyUpd:bool = obj["DeferQtyUpd"]
      """   If true, the system will defer update of Required Qty when the QuoteAsm QtyPer field is updated 
*** FUTURE USE  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.GlobalEntityGLC:bool = obj["GlobalEntityGLC"]
      """  Marks this EntityGLC as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtPRSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company ID  """  
      self.FilePath:str = obj["FilePath"]
      """  Default File  """  
      self.ExtIntCompID:str = obj["ExtIntCompID"]
      """  3rd Party Payroll provider assigned company identifier  """  
      self.ConsHrs:bool = obj["ConsHrs"]
      """  Consolidates single entry per employee  """  
      self.TempD:bool = obj["TempD"]
      """  Indicates if an identifier is required in the export file  """  
      self.ZeroNul:bool = obj["ZeroNul"]
      """  Export Zero Hours as Blank  """  
      self.SupHead:bool = obj["SupHead"]
      """  Indicates that only child records will be sent to the export file  """  
      self.SemiMonthDay:int = obj["SemiMonthDay"]
      """  2nd Period Start Day  """  
      self.Delimiter:str = obj["Delimiter"]
      """  Indicates which normal character will separate each field  """  
      self.TotalAllHrs:bool = obj["TotalAllHrs"]
      """  Total hours for Base, OT and premium per line  """  
      self.GrpPayTypeID:bool = obj["GrpPayTypeID"]
      """  Group hours by pay type  """  
      self.PayExportLayoutID:str = obj["PayExportLayoutID"]
      """  Default Export Layout  """  
      self.DetailHours:bool = obj["DetailHours"]
      """  Detailed Labor Hours  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SplitExportLines:bool = obj["SplitExportLines"]
      """  When checked, separate lines are created for Base, Overtime and Other (Premium) hours in Export File  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FsSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.StartContractNum:int = obj["StartContractNum"]
      """  Used to establish the beginning Service Contract Number. When the system generates a new Contract it will assign the greater of (StartContractNum) or (the last Contract Num. on file + 1) as the Contract number.  """  
      self.StartServiceCallNum:int = obj["StartServiceCallNum"]
      """  Used to establish the beginning Service Call Number. When the system generates a new Service Call it will assign the greater of (StartServiceCallNum) or (the last Service Call Number on file + 1) as the Service Call number.  """  
      self.ExpireHorizon:int = obj["ExpireHorizon"]
      """  This is the window of days that is used to determine if a service contract is going to expire soon.  If the current date plus the expire horizon is greater than or equal to the entered expire date on a contract, the contract is considered to be expiring soon.  """  
      self.PrintPrice:bool = obj["PrintPrice"]
      """  This flag is used when printing service call tickets.  If "YES" then labor and material pricing will print on the ticket.  """  
      self.CallProdCode:str = obj["CallProdCode"]
      """  Product Group Code. This will be used as a default for service calls.  This can be blank or must be valid in the ProdGrup table.  """  
      self.CallJobPrefix:str = obj["CallJobPrefix"]
      """  This prefix will be used for service call job.  The service call job will be the prefix + service call number + service call Line number.  """  
      self.ContractStartup:bool = obj["ContractStartup"]
      """  This flag is to be set to 'YES' during intial startup. When this flag is set to 'YES' all Service Contracts will be created as active invoiced and shipped.  The idea is that a cusomter that purchases FS may already have active service contracts that have been invoiced.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RenewalPeriod:int = obj["RenewalPeriod"]
      """  This field stores the allowed Contract Renewal Period which is used to determine how long a contract/renewal can be renewed past its expiration date.  If the RenewalPeriod = 0 then it means that ALL expired contracts can still be renewed anytime.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CallProdDescription:str = obj["CallProdDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SalesCategory:str = obj["SalesCategory"]
      """  Maintained through Category Maintenance.  The sales category may be used in the Financial Statements to compare Income Statement accounts against.  """  
      self.ARInterfaced:bool = obj["ARInterfaced"]
      """  Indicates if the A/R module is interfaced with General Ledger.  When interfaced A/R posting routines will automatically create "posted" journal  entries in G/L.  """  
      self.APInterfaced:bool = obj["APInterfaced"]
      """  Indicates if the Accounts Payable module is interfaced with General Ledger.  When interfaced A/P posting routines will automatically create "posted" journal  entries in G/L.  """  
      self.PRInterfaced:bool = obj["PRInterfaced"]
      """  Indicates if the Payroll module is interfaced with General Ledger.  When interfaced, P/R posting routines will automatically create "posted" journal  entries in G/L.  """  
      self.PostInvtyWipCos:bool = obj["PostInvtyWipCos"]
      """  Configuration option which controls if the user has the option in the periodic Inventory/Wip/Cost of sales calculation process to post the results to general ledger.  If this is set to No then the user will not have the option to post to G/L.  """  
      self.GJJournalCode:str = obj["GJJournalCode"]
      """  The Journal Code of the Journal that will be used for Journal entry transactions. Manual Journal entries.  """  
      self.ARVoucherInvoices:bool = obj["ARVoucherInvoices"]
      """   Indicates if the user wants to use Vouchering for A/R Invoices.  Only available if the G/L module is installed.
If yes then the system will do the following
- Print a Voucher # on the invoice.
- When invoices are printed they will be automatically posted. .  The "Voucher number" is actually the Journal Number to which the invoice posted.  """  
      self.APVoucherInvoices:bool = obj["APVoucherInvoices"]
      """   Indicates if the user wants to use Vouchering for A/P Invoices.  Only available if the G/L module is installed.
If yes then the system will print a Voucher assignment log when A/P invoices are posted.  The "Voucher number" is actually the Journal Number to which the invoice posted.  """  
      self.AllowUnBalancedEntries:bool = obj["AllowUnBalancedEntries"]
      """  Allow unbalanced entries to be entered in General Journal Entry with a warning.  """  
      self.AllowManualGJEntries:bool = obj["AllowManualGJEntries"]
      """  Allow manual General Journal entries to be made for System Accounts.  """  
      self.ExtGL:bool = obj["ExtGL"]
      """  Flag to indicate that an External GL interface is being used  """  
      self.MasterCOA:str = obj["MasterCOA"]
      """  Identifies the Master COA for the company  """  
      self.BatchGLBalances:bool = obj["BatchGLBalances"]
      """   Indicates if GL balances are maintained real time or in batch. If Yes, the GLJrnDtl write trigger does NOT update the GLPeriodBal table.
If No, the GLJrnDtl write trigger updates the GLPeriod table.  The default value is no.  """  
      self.BatchGLDailyBal:bool = obj["BatchGLDailyBal"]
      """   If BatchGLBalances = yes the users have the ability to have the daily balances updated in batch mode.  This option is only available if BatchGLBalances equals Yes.
A Yes in this field indicates the GLJrnDtl write trigger does not update the GLDailyBal table.
If No, the GLJrnDtl write trigger updates the GLDailyBalTable.
The default value is No.  """  
      self.MatchUsingCurrentDate:bool = obj["MatchUsingCurrentDate"]
      """   This option determines which date gets stored in the GLJrnDtl.MatchDate field when GL transactions are matched.

If true, then the date that the transactions are matched is used.  If false, then the latest apply date of the matched transactions is used.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefaultBookMode:str = obj["DefaultBookMode"]
      """  It is used to store default Book Mode in GL Journal Entry.  """  
      self.GJJournalCodeOpen:str = obj["GJJournalCodeOpen"]
      """  The Journal Code of the Journal that will be used for Opening Journal entry transactions. Manual Journal entries.  """  
      self.GJJournalCodeClose:str = obj["GJJournalCodeClose"]
      """  The Journal Code of the Journal that will be used for Clousing Journal entry transactions. Manual Journal entries.  """  
      self.TaxEntryMode:str = obj["TaxEntryMode"]
      """  It is used to store tax entry mode for GL Journal header. Possible values: 0`No Taxes~1`Taxable Journal Lines~2`Taxable Journal Lines or Tax adjustment Journal.  """  
      self.DefaultTaxLiability:str = obj["DefaultTaxLiability"]
      """  It is used to store default value of tax liability for tax line in GL Journal entry routine.  """  
      self.DefaultTaxType:str = obj["DefaultTaxType"]
      """  It is used to store default value of tax type for tax line in GL Journal entry routine.  """  
      self.KeepRevisionHistory:bool = obj["KeepRevisionHistory"]
      """  If the flag is on then posting rules conversion program creates a copy of current active revision before merging with the revision provided in the update/upgrade.  """  
      self.FormatSelection:str = obj["FormatSelection"]
      self.DisplayGLFormat:str = obj["DisplayGLFormat"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.DefaultTaxLiabilityDescription:str = obj["DefaultTaxLiabilityDescription"]
      self.DefaultTaxTypeDescription:str = obj["DefaultTaxTypeDescription"]
      self.TaxLiabilityTaxCodes:str = obj["TaxLiabilityTaxCodes"]
      """  The list of tax codes for Default Tax Liability  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GJJournalJrnlDescription:str = obj["GJJournalJrnlDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ISSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EnableHarbour:bool = obj["EnableHarbour"]
      """  Enable Harbor Flag  """  
      self.PeriodFormat:str = obj["PeriodFormat"]
      """  Countries may differ in the way periods are reported.  """  
      self.DescType:str = obj["DescType"]
      """  Description Type  """  
      self.DefISRegion:str = obj["DefISRegion"]
      """  Intrastat Region  """  
      self.ISOrigCountryReq:bool = obj["ISOrigCountryReq"]
      """  Country of Origin required  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.APRGFlow2:str = obj["APRGFlow2"]
      """  APRGFlow2  """  
      self.APRGFlowSpec2:str = obj["APRGFlowSpec2"]
      """  APRGFlowSpec2  """  
      self.APRGTranType2:str = obj["APRGTranType2"]
      """  APRGTranType2  """  
      self.ARRGFlow2:str = obj["ARRGFlow2"]
      """  ARRGFlow2  """  
      self.ARRGFlowSpec2:str = obj["ARRGFlowSpec2"]
      """  ARRGFlowSpec2  """  
      self.ARRGTranType2:str = obj["ARRGTranType2"]
      """  ARRGTranType2  """  
      self.Generate2APRGLine:bool = obj["Generate2APRGLine"]
      """  Generate2APRGLine  """  
      self.Generate2ARRGLine:bool = obj["Generate2ARRGLine"]
      """  Generate2ARRGLine  """  
      self.Flow1Desc:str = obj["Flow1Desc"]
      """  Flow1Desc  """  
      self.Flow2Desc:str = obj["Flow2Desc"]
      """  Flow2Desc  """  
      self.StartIstatNum:int = obj["StartIstatNum"]
      """  StartIstatNum  """  
      self.APFlow:str = obj["APFlow"]
      """  APFlow  """  
      self.APFlowSpec:str = obj["APFlowSpec"]
      """  APFlowSpec  """  
      self.APTranType:str = obj["APTranType"]
      """  APTranType  """  
      self.APRGFlow:str = obj["APRGFlow"]
      """  APRGFlow  """  
      self.APRGFlowSpec:str = obj["APRGFlowSpec"]
      """  APRGFlowSpec  """  
      self.APRGTranType:str = obj["APRGTranType"]
      """  APRGTranType  """  
      self.ARFlow:str = obj["ARFlow"]
      """  ARFlow  """  
      self.ARFlowSpec:str = obj["ARFlowSpec"]
      """  ARFlowSpec  """  
      self.ARTranType:str = obj["ARTranType"]
      """  ARTranType  """  
      self.ARRGFlow:str = obj["ARRGFlow"]
      """  ARRGFlow  """  
      self.ARRGFlowSpec:str = obj["ARRGFlowSpec"]
      """  ARRGFlowSpec  """  
      self.ARRGTranType:str = obj["ARRGTranType"]
      """  ARRGTranType  """  
      self.ISCurrency:str = obj["ISCurrency"]
      """  ISCurrency  """  
      self.APExtraTradeCommodityFlow:str = obj["APExtraTradeCommodityFlow"]
      """  APExtraTradeCommodityFlow  """  
      self.APExtraTradeTranType:str = obj["APExtraTradeTranType"]
      """  APExtraTradeTranType  """  
      self.APExtraTradeCustomsProcedure:str = obj["APExtraTradeCustomsProcedure"]
      """  APExtraTradeCustomsProcedure  """  
      self.APExtraTradeISCustomsDeclCountry:str = obj["APExtraTradeISCustomsDeclCountry"]
      """  APExtraTradeISCustomsDeclCountry  """  
      self.APExtraTradeISEUBorderCrossingCountry:str = obj["APExtraTradeISEUBorderCrossingCountry"]
      """  APExtraTradeISEUBorderCrossingCountry  """  
      self.APRGExtraTradeCommodityFlow:str = obj["APRGExtraTradeCommodityFlow"]
      """  APRGExtraTradeCommodityFlow  """  
      self.APRGExtraTradeTranType:str = obj["APRGExtraTradeTranType"]
      """  APRGExtraTradeTranType  """  
      self.APRGExtraTradeCustomsProcedure:str = obj["APRGExtraTradeCustomsProcedure"]
      """  APRGExtraTradeCustomsProcedure  """  
      self.APRGExtraTradeISCustomsDeclCountry:str = obj["APRGExtraTradeISCustomsDeclCountry"]
      """  APRGExtraTradeISCustomsDeclCountry  """  
      self.APRGExtraTradeISEUBorderCrossingCountry:str = obj["APRGExtraTradeISEUBorderCrossingCountry"]
      """  APRGExtraTradeISEUBorderCrossingCountry  """  
      self.ARRGFlowSpec2Descr:str = obj["ARRGFlowSpec2Descr"]
      """  Shipping Returned 2  """  
      self.ARRGFlowSpecDescr:str = obj["ARRGFlowSpecDescr"]
      """  Shipping Returned  """  
      self.Generate2APRGExtraTradeLine:bool = obj["Generate2APRGExtraTradeLine"]
      """  Generate2APRGExtraTradeLine  """  
      self.ARRGTranType2Descr:str = obj["ARRGTranType2Descr"]
      """  Shipping Returned 2  """  
      self.APRGExtraTradeCommodityFlow2:str = obj["APRGExtraTradeCommodityFlow2"]
      """  APRGExtraTradeCommodityFlow2  """  
      self.APRGExtraTradeTranType2:str = obj["APRGExtraTradeTranType2"]
      """  APRGExtraTradeTranType2  """  
      self.ARRGTranTypeDescr:str = obj["ARRGTranTypeDescr"]
      """  Shipping Returned  """  
      self.ARTranTypeDescr:str = obj["ARTranTypeDescr"]
      """  Shipping Normal  """  
      self.APRGExtraTradeCustomsProcedure2:str = obj["APRGExtraTradeCustomsProcedure2"]
      """  APRGExtraTradeCustomsProcedure2  """  
      self.APRGExtraTradeISCustomsDeclCountry2:str = obj["APRGExtraTradeISCustomsDeclCountry2"]
      """  APRGExtraTradeISCustomsDeclCountry2  """  
      self.RegionDesc:str = obj["RegionDesc"]
      """  Intrastat Region Description  """  
      self.APRGExtraTradeISEUBorderCrossingCountry2:str = obj["APRGExtraTradeISEUBorderCrossingCountry2"]
      """  APRGExtraTradeISEUBorderCrossingCountry2  """  
      self.APFlowSpecDescr:str = obj["APFlowSpecDescr"]
      """  Receipt Normal  """  
      self.APRGFlowSpec2Descr:str = obj["APRGFlowSpec2Descr"]
      """  Receipt Returned 2  """  
      self.ARExtraTradeCommodityFlow:str = obj["ARExtraTradeCommodityFlow"]
      """  ARExtraTradeCommodityFlow  """  
      self.ARExtraTradeTranType:str = obj["ARExtraTradeTranType"]
      """  ARExtraTradeTranType  """  
      self.APRGFlowSpecDescr:str = obj["APRGFlowSpecDescr"]
      """  Receipt Returned  """  
      self.APRGTranType2Descr:str = obj["APRGTranType2Descr"]
      """  Receipt Returned 2  """  
      self.ARExtraTradeCustomsProcedure:str = obj["ARExtraTradeCustomsProcedure"]
      """  ARExtraTradeCustomsProcedure  """  
      self.ARExtraTradeISCustomsDeclCountry:str = obj["ARExtraTradeISCustomsDeclCountry"]
      """  ARExtraTradeISCustomsDeclCountry  """  
      self.APRGTranTypeDescr:str = obj["APRGTranTypeDescr"]
      """  Receipt Returned  """  
      self.ARExtraTradeISEUBorderCrossingCountry:str = obj["ARExtraTradeISEUBorderCrossingCountry"]
      """  ARExtraTradeISEUBorderCrossingCountry  """  
      self.APTranTypeDescr:str = obj["APTranTypeDescr"]
      """  Receipt Normal  """  
      self.ARFlowSpecDescr:str = obj["ARFlowSpecDescr"]
      """  Shipping Normal  """  
      self.ARRGExtraTradeCommodityFlow:str = obj["ARRGExtraTradeCommodityFlow"]
      """  ARRGExtraTradeCommodityFlow  """  
      self.ARRGExtraTradeTranType:str = obj["ARRGExtraTradeTranType"]
      """  ARRGExtraTradeTranType  """  
      self.FlowList:str = obj["FlowList"]
      """  Used to populate the Intrastat Flow combos  """  
      self.ARRGExtraTradeCustomsProcedure:str = obj["ARRGExtraTradeCustomsProcedure"]
      """  ARRGExtraTradeCustomsProcedure  """  
      self.ARRGExtraTradeISCustomsDeclCountry:str = obj["ARRGExtraTradeISCustomsDeclCountry"]
      """  ARRGExtraTradeISCustomsDeclCountry  """  
      self.ARRGExtraTradeISEUBorderCrossingCountry:str = obj["ARRGExtraTradeISEUBorderCrossingCountry"]
      """  ARRGExtraTradeISEUBorderCrossingCountry  """  
      self.Generate2ARRGExtraTradeLine:bool = obj["Generate2ARRGExtraTradeLine"]
      """  Generate2ARRGExtraTradeLine  """  
      self.ARRGExtraTradeCommodityFlow2:str = obj["ARRGExtraTradeCommodityFlow2"]
      """  ARRGExtraTradeCommodityFlow2  """  
      self.ARRGExtraTradeTranType2:str = obj["ARRGExtraTradeTranType2"]
      """  ARRGExtraTradeTranType2  """  
      self.ARRGExtraTradeCustomsProcedure2:str = obj["ARRGExtraTradeCustomsProcedure2"]
      """  ARRGExtraTradeCustomsProcedure2  """  
      self.ARRGExtraTradeISCustomsDeclCountry2:str = obj["ARRGExtraTradeISCustomsDeclCountry2"]
      """  ARRGExtraTradeISCustomsDeclCountry2  """  
      self.ARRGExtraTradeISEUBorderCrossingCountry2:str = obj["ARRGExtraTradeISEUBorderCrossingCountry2"]
      """  ARRGExtraTradeISEUBorderCrossingCountry2  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JCSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CheckOff1Label:str = obj["CheckOff1Label"]
      """  Label used for the JobHead.CheckOff1 field.  There are 5 CheckOffLabel fields.  They are all optional.  If entered then the corresponding JobHead.CheckOff fields become active.  """  
      self.CheckOff2Label:str = obj["CheckOff2Label"]
      """  Label used for the JobHead.CheckOff2 field.  """  
      self.CheckOff3Label:str = obj["CheckOff3Label"]
      """  Label used for the JobHead.CheckOff3 field.  """  
      self.CheckOff4Label:str = obj["CheckOff4Label"]
      """  Label used for the JobHead.CheckOff4 field.  """  
      self.CheckOff5Label:str = obj["CheckOff5Label"]
      """  Label used for the JobHead.CheckOff5 field.  """  
      self.ClockFormat:str = obj["ClockFormat"]
      """  Indicates the format of how labor time is entered.  It can be entered as (M) - hours/minutes or (H) - Hours/Hundredths.  """  
      self.FeedPayroll:bool = obj["FeedPayroll"]
      """  Indicates if the labor entry details will be transferred to the Payroll system.  This is used to set the value of LaborDtl.Payroll flag.  """  
      self.RemoveLoad:str = obj["RemoveLoad"]
      """  Controls how shop load is removed.  It can either be by Actual Hours  "H" or based on quantity completed "Q".  """  
      self.MachinePrompt:bool = obj["MachinePrompt"]
      """  Controls whether or not entry of a Machine ID will be prompted for in Labor Entry and Labor Collection.  """  
      self.ReworkReasons:bool = obj["ReworkReasons"]
      """  Indicates if system should prompt for entry of a Rework Reason code for rework transactions during Labor Collection or Labor Entry.  """  
      self.ScrapReasons:bool = obj["ScrapReasons"]
      """  Indicates if system should prompt user to enter a Scrap Reason code for labor transactions where the scrap quantity is not zero during Labor Entry or Labor Collection.  """  
      self.JobSeqLength:int = obj["JobSeqLength"]
      """  Indicates the maximum number of digits to be entered into the JCSyst.NextJobNum field.  This also controls the number of digits that the system will generate when the user requests a "Next Job Number" while creating a new job number.  """  
      self.NextJobNumber:int = obj["NextJobNumber"]
      """  The value in this field represents the next default job sequence number.  The number of digits that can be entered is controlled by JCSyst.JobSeqLength.  Example of how the system uses these fields to generate a number that is inserted as part of the Job number when the user requests "Next Job Number" while creating a new job number would be: JobSeqLength = 6 and NextJobNumber = 100.  Then the system would try to insert  "000100" into the job number at the current insertion point.  """  
      self.Grace:int = obj["Grace"]
      """  Grace Period, stored as Hours/Hundredths  """  
      self.StdFormat:str = obj["StdFormat"]
      """   Default qualifier for the Production Standard field.  This is used as a default to the qualifier field in operation details when there is no related  OpStd record.  The valid qualifiers are:
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour, "PM" - Pieces/Minute, "OH" - Operations/Hour, "OM"  - Operations/minute, HR - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   Default standard basis is to be used to with standards that are time per piece (HP & MP).  The basis is a Divisor.  Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours.  The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Default for the JobOper and QuoteOpr.EstScrapType fields  """  
      self.InvAdjReasons:bool = obj["InvAdjReasons"]
      """  Indicates if system should prompt user to enter an Inventory Adjustment Reason code for quantity and cost adjustments.  """  
      self.SchedCode:str = obj["SchedCode"]
      """  SchedPri.SchedCode value that is marked as the default scheduling code in the Scheduling Priority Code master file.  """  
      self.SchedStartedOps:bool = obj["SchedStartedOps"]
      """  Default for scheduling operations that have been started.  A started operation is one with labor reported to it.  Global Scheduling uses this value.  """  
      self.WksLaborHistWarn:int = obj["WksLaborHistWarn"]
      """  The number of weeks labor warning detail is stored until they are purged.  """  
      self.GenLaborWarnMsg:bool = obj["GenLaborWarnMsg"]
      """  This option controls whether or not the labor warnings messages are generated/reported.  When this option is turned on labor warning records are created and the labor edit list and/or entry/tracker programs report these warnings.  When it is turned off the labor edit list performs its own warning checking and no warnings are reported in the entry/tracker programs.  This option should only be turned on between labor periods (i.e. after all of the labor has been reported, but before the next periods information has been entered).  Only maintainable if the Data Collection module has been installed.  """  
      self.PreventPJChange:bool = obj["PreventPJChange"]
      """  If set to Yes, the user must change the Job Engineered flag to No before they are allowed to make any changes to a Job.  """  
      self.LogChanges:bool = obj["LogChanges"]
      """  If this is Yes, then when Jobs are set to "Planned"  or any header flag is changed on a "Planned" job the user will be prompted to enter a description of the changes.  This option is only available when "PreventPJChange" = Yes.  """  
      self.EarlyClockInAllowance:int = obj["EarlyClockInAllowance"]
      """  Number of minutes used by data collection to determine the time frame in which early clock in times are to be adjusted forward to the shift start time.  If clock in time falls within the  time range of (Shift Start - Allowance) to Shift Start then the clock in time will set to Shift Start time.  """  
      self.LateClockInAllowance:int = obj["LateClockInAllowance"]
      """  Number of minutes used by data collection to determine the time frame in which late clock in times are to be adjusted backwards to the shift start time.  If clock in time falls within the  time range of Shift Start to (Shift Start + Allowance)  then the clock in time will set to Shift Start time.  """  
      self.EarlyClockOutAllowance:int = obj["EarlyClockOutAllowance"]
      """  Number of minutes used by data collection to determine the time frame in which early clock out times are to be adjusted forward to the shift end time.  If clock out time falls within the  time range of (Shift End - Allowance) to Shift End  then the clock out time will set to Shift end.  """  
      self.LateClockOutAllowance:int = obj["LateClockOutAllowance"]
      """  Minutes used to determine the time frame in which late clock out times are to be adjusted backwards to the shift end time.  If clock out time falls within the  time range of Shift end to (Shift Start + Allowance) then the clock out time will set to Shift End time.  """  
      self.FloatPartRev:bool = obj["FloatPartRev"]
      """  Default for "Floating " the part revision.  To "Float" the revision of unfirm jobs to the revision in effect at the time of the requirement.  """  
      self.ForecastDaysBefore:int = obj["ForecastDaysBefore"]
      """   Number of days before the forecast date in which any sales orders that exist should reduce the forecast quantity.
Ex: Forecast date of 3/31/98, Days before of 10, then any orders that have a date of 3/21/98 to 3/31/98 would reduce the forecast.  """  
      self.ForecastDaysAfter:int = obj["ForecastDaysAfter"]
      """   Number of days after the forecast date in which any sales orders that exist should reduce the forecast quantity.
Ex: Forecast date of 3/31/98, Days after  of 10, then any orders that have a date of 4/01/98 to 4/10/98 would reduce the forecast.  """  
      self.DetailGrace:bool = obj["DetailGrace"]
      """   Indicates if the LateClockIn or EarlyClockOut grace period should be applied to the labor detail transactions.
Ex: 10 minute LateClockIn, Shift Start = 8:00am, Employee clocks in and starts an activity  at 8:05.  If DetailGrace = Yes then StartTime on the detail will be adjusted to 8:00.  If DetailGrace = No then StartTime remains as 8:05 and an the 5 minutes will be included in the  idle time.  This setting does NOT affect how Start/End times are adjusted for the timecard record.  In both cases for this example the start time for the timecard will be 8:00.  """  
      self.PreventFABypass:bool = obj["PreventFABypass"]
      """  If set to Yes, the user is unable to start production work for an operation which is waiting for First Article approval.  """  
      self.ChgImpactPriceListCode:str = obj["ChgImpactPriceListCode"]
      """  Used to get a value for jobs not referencing a sales order.  If a part in not in the price list then use Part.UnitPrice.  """  
      self.EarlyGracePeriod:int = obj["EarlyGracePeriod"]
      """   Used in conjunction with the Late Grace Period to determine if a job is early, on-time or late.  Example: Early Grace Period is 4, Late Grace Period is 1, Job Required Date is 05/20/02: If the job is
scheduled to be completed before 05/16/02 it is Early.  If the job is
scheduled to be completed anywhere from 05/16/02 through 05/21/02 it is on-time.  If the job is scheduled to be completed after 05/21/02 it is late.  """  
      self.LateGracePeriod:int = obj["LateGracePeriod"]
      """   Used in conjunction with the Early Grace Period to determine if a job is early, on-time or late.  Example: Early Grace Period is 4, Late Grace Period is 1, Job Required Date is 05/20/02: If the job is
scheduled to be completed before 05/16/02 it is Early.  If the job is
scheduled to be completed anywhere from 05/16/02 through 05/21/02 it is on-time.  If the job is scheduled to be completed after 05/21/02 it is late.  """  
      self.QuickJobID:str = obj["QuickJobID"]
      """   NJ - Next Job
OR - Order Release  """  
      self.KanBanPrefix:str = obj["KanBanPrefix"]
      """  KanBanPrefix  """  
      self.NextOrderNumber:int = obj["NextOrderNumber"]
      """  The value in this field represents the next default transfer Order sequence number.  The number of digits that can be entered is controlled by JCSyst.OrderSeqLength.  Example of how the system uses these fields to generate a number that is inserted as part of the Transfer Order number when the user requests "Next Order Number" while creating a new Transfer Order number would be: OrderSeqLength = 6 and NextOrderNumber = 100.  Then the system would try to insert  "000100" into the Order number at the current insertion point.  """  
      self.OrderSeqLength:int = obj["OrderSeqLength"]
      """  Indicates the maximum number of digits to be entered into the JCSyst.NextOrderNum field.  This also controls the number of digits that the system will generate when the user requests a "Next Order Number" while creating a new order number.  """  
      self.NextTranLineNumber:int = obj["NextTranLineNumber"]
      """  The value in this field represents the next default transfer Order Line sequence number.  The number of digits that can be entered is controlled by JCSyst.OrderSeqLength.  Example of how the system uses these fields to generate a number that is inserted as part of the Transfer Detail Line number when the user requests "Next Line Number" when converting an MRP Transfer Line number would be: OrderSeqLength = 6 and NextTranLineNumber = 100.  Then the system would try to insert  "000100" into the Line Number at the current insertion point.  """  
      self.AllowSchedulingBeforeToday:bool = obj["AllowSchedulingBeforeToday"]
      """  Determines if a scheduler is allowed to schedule/reschedule jobs/operations (from the Scheduling Boards) to do work before today.  """  
      self.DirectShipVar:str = obj["DirectShipVar"]
      """  Indicates where to post all variances on a job that shipped direct for a standard cost part.  M = to the Product Group, C = to the Cost of Sales.  """  
      self.SplitMfgCostElements:bool = obj["SplitMfgCostElements"]
      """  Flag to indicate how to split the manufacturing cost elements when a manufactured material is issued to the job.  If flag is set to true, the cost of the issued material will be split into individual manufacturing cost elements. If set to false, the cost of the issued material is added to the manufacturing material cost element only.  """  
      self.UnfirmATP:bool = obj["UnfirmATP"]
      """  This flag is used by ATP to determine if Unfirm Jobs should be considered in ATP calculations.  """  
      self.ForecastPeriods:str = obj["ForecastPeriods"]
      """   The ForecastPeriods field defines the forecast periods that are used with the import and export process.

Examples: Year, Semester, Quarter, Month, Week, Day

This field is used with the ForecastPeriodsPerYear field.  """  
      self.ForecastPeriodsPerYear:int = obj["ForecastPeriodsPerYear"]
      """   The ForecastPeriodsPerYear field defines the number of forecast periods per year.

This field is used with the ForecastPeriods field.  """  
      self.ReplaceMissingValues:bool = obj["ReplaceMissingValues"]
      """   The ReplaceMissingValues field is used to determine how periods with zero demand should be exported when exporting forecast data.

If yes, then zero demand will be replaced with the string "MISSING" as long as there is no demand in previous periods.  If previous periods have some demand, then zero demand will be left as zero.

If the value of this field is no, then zero demand will be left as zero when exporting demand.  """  
      self.ForecastImportDay:int = obj["ForecastImportDay"]
      """   The ForecastImportDay field is used by the forecast import process to determine the forecast date for each forecast period.

The valid values for this field are dependent on the value in the ForecastPeriods field.  """  
      self.ChkEmpPrjRole:bool = obj["ChkEmpPrjRole"]
      """  If false then when an employee is booking hours to a job they can enter any Project Role code that has been set up on the employee. When the field is set to true then the Project Role entered MUST be one of the Project Role codes that have been assigned to the operation.  """  
      self.DfltPrjRoleLoc:str = obj["DfltPrjRoleLoc"]
      """   Defines where the default role code will be obtained.
The options are ?
Operation: Project Role code from the operation will be used.
Employee. Project Role Code from the Employee will be used.  """  
      self.DfltRevRecMthd:str = obj["DfltRevRecMthd"]
      """  Defines the default revenue recognition method to be used in project entry.The options are Default =  (blank).Code/Desc: INV = On Invoice, LBR = Labor Booking, MAN = Manual, BDN = Actual Burden, PCC = POC-Cost-to-Cost, PCE = POC-Efforts, PCU = POC-Units-of-Delivery  """  
      self.AllowRevRecChg:bool = obj["AllowRevRecChg"]
      """  Indicates whether the revenue recognition method can be changed on the project.  """  
      self.RevRecJrnlReverse:str = obj["RevRecJrnlReverse"]
      """  When set to Reserve following month the journal created will be flagged as a reversing journal.PCL = Reverse on Project Close, MON = Reverse Following Month  """  
      self.DfltPrjRtSrc:str = obj["DfltPrjRtSrc"]
      """  Defines where the invoice process will obtain the Project Role Rates from. Hierarchical works as defined for Invoice Preparation. All of the others will ONLY obtain the rates from the area defined. HIER = Hierarchical, PROJ = Project Only, EMPL = Employee Only, ROLE = Project Role Only  """  
      self.AllowPrjRtSrcChg:bool = obj["AllowPrjRtSrcChg"]
      """  True indicates the user can change the Derive Project Rates from at the project level.  """  
      self.ExtFcstImpFormat:str = obj["ExtFcstImpFormat"]
      """  The default format to use when importing forecast data from external forecast solutions.  """  
      self.ExtFcstExpFormat:str = obj["ExtFcstExpFormat"]
      """  The default format to use when exporting sales history data to external forecast solutions.  """  
      self.ConInvMeth:str = obj["ConInvMeth"]
      """   Default of Invoicing Method of new Project. If advanced billing is not licensed the only options are CS and MB. Code/Desc:
CS = Customer Shipment, 
MB = Milestone Billing, 
FF = Fixed Fee;
CP = Cost Plus;
TM = Time and Material;
PP = Progress payment;

The default is Customer Shipment.  """  
      self.MtlTaxCatID:str = obj["MtlTaxCatID"]
      """  Tax Category to default into Project. MtlTaxCatID.  """  
      self.LbrTaxCatID:str = obj["LbrTaxCatID"]
      """  Tax Category to default into Project LbrTaxCatID.  """  
      self.FeeTaxCatID:str = obj["FeeTaxCatID"]
      """  Tax Category to default into Project. FeeTaxCatID.  """  
      self.ODCTaxCatID:str = obj["ODCTaxCatID"]
      """  Tax Category to default into Project. ODCaxCatID.  """  
      self.SubTaxCatID:str = obj["SubTaxCatID"]
      """  Tax Category to default into Project. SubTaxCatID.  """  
      self.BdnTaxCatID:str = obj["BdnTaxCatID"]
      """  Tax Category to default into Project. BdnTaxCatID.  """  
      self.TaxOnNetOfRet:bool = obj["TaxOnNetOfRet"]
      """  Tax Category to default into Project. TaxOnNetOfRet.  """  
      self.AllowChkEmpPrjRoleChg:bool = obj["AllowChkEmpPrjRoleChg"]
      """  indicates if the company setting for ChkEmpPrjRole can be overridden at the project level.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AdvancedLaborRate:bool = obj["AdvancedLaborRate"]
      """  AdvancedLaborRate  """  
      self.CapRevID:int = obj["CapRevID"]
      """  CapRevID  """  
      self.AutoReceipt:bool = obj["AutoReceipt"]
      """  AutoReceipt  """  
      self.MRPJobID:str = obj["MRPJobID"]
      """  MRPJobID  """  
      self.PbsTaxCatID:str = obj["PbsTaxCatID"]
      """  Tax Category to default into Project. PbsTaxCatID. (Billing Schedule)  """  
      self.SOAllowWBSPhase:bool = obj["SOAllowWBSPhase"]
      """  True indicates the user can link a sales order per wbs phase on project.  """  
      self.SOAutoRelWBSPhase:bool = obj["SOAutoRelWBSPhase"]
      """  SOAutoRelWBSPhase  """  
      self.SchedAnUnEngineered:bool = obj["SchedAnUnEngineered"]
      """  SchedAnUnEngineered  """  
      self.GetCostsFromTemplate:bool = obj["GetCostsFromTemplate"]
      """  GetCostsFromTemplate  """  
      self.AllowMoveJobsAcrossPlants:bool = obj["AllowMoveJobsAcrossPlants"]
      """  Allows moving Jobs across sites within the company and not only for the site where user is logged on.  """  
      self.MPSOnly:bool = obj["MPSOnly"]
      """  MPSOnly  """  
      self.EnableSchedDebugLog:bool = obj["EnableSchedDebugLog"]
      """  EnableSchedDebugLog  """  
      self.IncludeExtraDetailsLog:bool = obj["IncludeExtraDetailsLog"]
      """  IncludeExtraDetailsLog  """  
      self.MtlQtyParentDefault:int = obj["MtlQtyParentDefault"]
      """  MtlQtyParentDefault  """  
      self.AssignPrimarySupplier:bool = obj["AssignPrimarySupplier"]
      """  AssignPrimarySupplier  """  
      self.AvoidIncludeQuotePrjRevenue:bool = obj["AvoidIncludeQuotePrjRevenue"]
      """  AvoidIncludeQuotePrjRevenue  """  
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.MaxLogDay:int = obj["MaxLogDay"]
      """  MaxLogDay  """  
      self.DefaultRecognizeRevenueAtPhaseLevel:bool = obj["DefaultRecognizeRevenueAtPhaseLevel"]
      """  Default Option to activate Revenue Recognition at WBS Phase level  """  
      self.EnableShipTo:bool = obj["EnableShipTo"]
      """  EnableShipTo  """  
      self.StdFormatDesc:str = obj["StdFormatDesc"]
      self.TaxCatPbsDescription:str = obj["TaxCatPbsDescription"]
      self.IncludeQuotePrjRevenue:bool = obj["IncludeQuotePrjRevenue"]
      """  Include quotes without link to SO to Projected Revenue  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ChgImpactPriceLstListDescription:str = obj["ChgImpactPriceLstListDescription"]
      self.TaxCatBdnDescription:str = obj["TaxCatBdnDescription"]
      self.TaxCatFeeDescription:str = obj["TaxCatFeeDescription"]
      self.TaxCatLbrDescription:str = obj["TaxCatLbrDescription"]
      self.TaxCatMtlDescription:str = obj["TaxCatMtlDescription"]
      self.TaxCatODCDescription:str = obj["TaxCatODCDescription"]
      self.TaxCatSubDescription:str = obj["TaxCatSubDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MMSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DefaultStatusID:str = obj["DefaultStatusID"]
      """  Identifies the EquipStatusID that is to be used as the default for Equip.StatusID. This may be blank. Not directly maintainable. It gets set by Equipment Status maintenance when the user checks the "Default" box.  """  
      self.TemplateJobNum:str = obj["TemplateJobNum"]
      """  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  """  
      self.JobPrefix:str = obj["JobPrefix"]
      """  Prefix that will be used when generating  Maintenance Job numbers for this company. Note this may be overridden at the Site level (see SiteConfCntrl.MaintJobPrefix)  """  
      self.MaintBuffer:int = obj["MaintBuffer"]
      """  MMSyst.MaintBuffer, default for EquipPlan.MaintBuffer  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.JobHeadPartDescription:str = obj["JobHeadPartDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PDMSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PDMExportDir:str = obj["PDMExportDir"]
      """  PDM Export directory  """  
      self.PDMImportDir:str = obj["PDMImportDir"]
      """  PDM Import Directory  """  
      self.DocExportDir:str = obj["DocExportDir"]
      """  Document Export Directory  """  
      self.DocImportDir:str = obj["DocImportDir"]
      """  Document Import Directory  """  
      self.ECOGroupID:str = obj["ECOGroupID"]
      """  The default Group id for the ECO Group  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Default pdm revision number  """  
      self.SearchWord:str = obj["SearchWord"]
      """  The default pdm searchword for new parts.  """  
      self.FileNum:int = obj["FileNum"]
      """  File number used for identification of integration files.  """  
      self.PartPrefix:str = obj["PartPrefix"]
      """  File name prefix for parts.  """  
      self.BomPrefix:str = obj["BomPrefix"]
      """  File name prefix for Boms.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PLMRevision:str = obj["PLMRevision"]
      """  PLM process will consider two types of revision. Current Revision: last approved revision with effective date less or equal than today. Last approved revision: (no matter the effective date) so if the customer has multiple revisions and one is approved, even if it’s for a future date, we will send this one.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ECOGroupIDDescription:str = obj["ECOGroupIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PECompWhldHistRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RecordSeq:int = obj["RecordSeq"]
      """  Record Sequence  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Create Date  """  
      self.UserID:str = obj["UserID"]
      """  User Identifier.  """  
      self.GoodContributor:bool = obj["GoodContributor"]
      """  Good Contributor  """  
      self.WithholdingAgent:bool = obj["WithholdingAgent"]
      """  Indicates the status of Withholding Agent.  """  
      self.CollectionAgent:bool = obj["CollectionAgent"]
      """  Collection Agent withholding status.  """  
      self.NotFound:bool = obj["NotFound"]
      """  Not Found withholding status.  """  
      self.NoAddress:bool = obj["NoAddress"]
      """  No Address Provided withholding status.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Password:str = obj["Password"]
      """  During Payroll Class maintenance the user is prompted for a password.  The entered password is encoded and then compared to this string.  An encoded string that is checked before allowing access to the payroll class maintenance program.  If blank then user is prompted to enter a password before allowing access to PRClass maintenance.  It does not matter what security level the user is, they just need to know this password in order to gain access.  """  
      self.CheckSort:str = obj["CheckSort"]
      """   Controls the order in which checks are printed. Valid options are;
"SuperID", "Name", "EmpID","Dept".  """  
      self.SemiDay:int = obj["SemiDay"]
      """  Identifies the day of the month which the 2nd period starts for semimonthly payroll runs.  """  
      self.PRStartDate:str = obj["PRStartDate"]
      """  Date that the Manufacturing System payroll will become effective.  When initially starting up payroll the user enters the employee year to date information as of (PRStartDate - 1day).  If the user wants the initial quarter to date figures to be correct they should start payroll at the beginning of a quarter and enter that start date here.  """  
      self.NoPRMgr:str = obj["NoPRMgr"]
      """   Encoded field which indicates if Payroll Managers have been set up.
(Blank = Not a PR manager).  Only users that are Payroll managers are allowed access to payroll class maintenance where they can establish the list of authorized users for the class.
There must always be at least one user where DspPayrollMgr = Yes.  """  
      self.HCMEnabled:bool = obj["HCMEnabled"]
      """  Enable/Disable the HCM Integration. May be License specific (TBD)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrintRates:bool = obj["PrintRates"]
      """  PrintRates  """  
      self.AllowHighPayRate:bool = obj["AllowHighPayRate"]
      """  If enabled the user is able to enter a max pay rate of 999999.9999 in Payroll Employee, currently the system only allows a max of 9999.9999.  """  
      self.PRChecksExist:bool = obj["PRChecksExist"]
      """  Payroll checks exist for this company  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxSvcConfigRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.URL:str = obj["URL"]
      """  The location of the AvaTax service when the address will not change between the client and web service.  """  
      self.ViaURL:str = obj["ViaURL"]
      """  The intermediary server, for example a firewall, for the AvaTax service.  """  
      self.TextCase:str = obj["TextCase"]
      """  Stores the text case used for address validation. Possible values are Default, Upper, and Mixed  """  
      self.Account:str = obj["Account"]
      """  The unique account number provided by Avalara for verification against the service. May also contain a username.  """  
      self.Key:str = obj["Key"]
      """  The unique alpha-numeric key for the account provided by Avalara for verification against the service. May also contain a password if Account contains a username.  """  
      self.TaxConnectEnabled:bool = obj["TaxConnectEnabled"]
      """  Indicates whether the Epicor Tax Connect interface is active for this company. If false, no Tax Connect address validation or tax calculations will take place regardless of how the company flags are set for those functions.  """  
      self.AddrValEnabled:bool = obj["AddrValEnabled"]
      """   Indicates whether the system can perform address validation via Epicor Tax Connect. If TaxConnectEnabled flag = true this flag will be checked to see if address validations are authorized/available via the
Epicor Tax Connect. If false no address validation logic will be executed.  """  
      self.TaxCalcEnabled:bool = obj["TaxCalcEnabled"]
      """  Indicates whether the system should perform tax calculations via Epicor Tax Connect. If TaxConnectEnabled flag = true this flag will be checked to see if tax calculations are authorized/available via Epicor Tax Connect. If false the base Epicor tax calculations will take place.  """  
      self.TaxIdPrefix:str = obj["TaxIdPrefix"]
      """  The Prefix to be used in conjunction with the SalesTaxSeq database sequence for automatically created SalesTax records  """  
      self.RequestTimeOut:int = obj["RequestTimeOut"]
      """  Request timeout value for tax connect requests, in seconds.  """  
      self.DefaultTaxCatID:str = obj["DefaultTaxCatID"]
      """  The default tax category to assign to a Sales Order/Quote/Invoice  record if tax connect is enabled and no tax category is defaulted via the standard tax category default logic.  """  
      self.LastDocId:int = obj["LastDocId"]
      """  This records the last document id retrieved from a ReconcileTaxHistory call to Avalara. It will be used to default the starting document ID in the Get Tax History action in Tax Reconciliation process.  """  
      self.DebugMode:bool = obj["DebugMode"]
      """  Specifies if Tax Connect will run in Debug Mode. When TRUE the input-output XML files sent and received to Avalara will NOT be deleted so they can be reviewed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ValidateISOCode:bool = obj["ValidateISOCode"]
      """  ValidateISOCode  """  
      self.CertCaptureEnabled:bool = obj["CertCaptureEnabled"]
      """  Indicates whether the system can perform CertCapture transactions. If CertCaptureEnabled is true, CertCapture features will be available. Otherwise, they won't.  """  
      self.APTaxDisplayAccount:str = obj["APTaxDisplayAccount"]
      self.APTaxAcctDesc:str = obj["APTaxAcctDesc"]
      self.ARTaxDisplayAccount:str = obj["ARTaxDisplayAccount"]
      self.ARTaxAcctDesc:str = obj["ARTaxAcctDesc"]
      self.ETCOffline:bool = obj["ETCOffline"]
      """  External field to be used to indicate that the Tax Connect service is off line. This filed can be set by the BL when a communication failure with tax connect occurs, or can be set manually in the UI when the user indicates that tax connect is offline. If set to true then the BL will not attempt any communication with the tax service. This is used to save unnecessary processing delays trying to communicate with the tax service when it is known that the service is unavailable.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxCatDescription:str = obj["TaxCatDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_XaSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DefaultUM:str = obj["DefaultUM"]
      """  The default Unit of Measure that will be used when creating a part.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Used as the default costing method when creating new parts in Part Master Maintenance. Remember that each Part defines its own costing method. The possible values are "A" - Average, "L" - Last or  "S" - standard.  """  
      self.DefaultPlant:str = obj["DefaultPlant"]
      """  Establishes the default Site ID to be used as the default for a Part's Primary Site field during Part maintenance.  The Default Warehouse must be in the DefaultSite.  """  
      self.PrintCompanyName:bool = obj["PrintCompanyName"]
      """  Indicates if Company Name & Address should print on forms.  """  
      self.StartOrderNum:int = obj["StartOrderNum"]
      """  Used to establish the beginning Sales Order #. When the system generates a new order it will assign the greater of (StartOrderNum) or (the last orders # on file + 1) as the order number.  """  
      self.StartPONum:int = obj["StartPONum"]
      """  Used to establish the beginning Purchase Order #. When the system generates a new PO, it will assign the greater of (StartPONum) or (the last orders # on file + 1) as the PO number.  """  
      self.StartPSNum:int = obj["StartPSNum"]
      """  Used to establish the beginning Packing Slip #. When the system generates a new packing slip it will assign the greater of (StartPSNum) or (the last Packing Slips  # on file + 1) as the PS number.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Identifies the Terms master that is to be used as the default when creating customer masters. This can be left blank if there is no one best terms default. Otherwise it gets set via terms maintenance when the user checks the "Default" box.  """  
      self.ShipNoJob:bool = obj["ShipNoJob"]
      """  Controls the entry of ship from job quantity in shipping entry program. If set to "yes" then job quantity field is enabled regardless of the order being linked to a job. This is intended only to be set to "yes" during the initial system implementation period. So that users can create and ship orders for manufactured items without forcing them to have established jobs  """  
      self.BookOrders:bool = obj["BookOrders"]
      """  This field indicates if the system should generate sales order booking records. Booking tables are used to store changes in sales volume. See BookOrd & BookDtl for more info.  """  
      self.PrintBarCodes:bool = obj["PrintBarCodes"]
      """  Option that controls the sensitivity of Bar Code Printing options.  """  
      self.StartRMANum:int = obj["StartRMANum"]
      """  Used to establish the beginning RMA#. When the system generates a new RMA it will assign the greater of (StartRMANum) or (the last RMA # on file + 1) as the RMA number.  """  
      self.DefaultShipViaCode:str = obj["DefaultShipViaCode"]
      """  Identifies the ShipVia master that is to be used as the default when creating Purchase Orders. This may be blank if there is no one normal ship via. Not directly maintainable. It gets set by Ship Via maintenance when the user checks the "Default" box.  """  
      self.StartRFQNum:int = obj["StartRFQNum"]
      """  Used to establish the beginning PurchaseRFQ #. When the system generates a new RFQ it will assign the greater of (StartRFQNum) or (the last RFQ # on file + 1) as the RFQ number.  """  
      self.CheckOff1Label:str = obj["CheckOff1Label"]
      """  Label used for the DMRHead.CheckOff1 field.  There are 5 CheckOffLabel fields. They are all optional. If entered then the corresponding CheckOff fields become active.  """  
      self.CheckOff2Label:str = obj["CheckOff2Label"]
      """  Label used for the DMRHead.CheckOff2 field.  """  
      self.CheckOff3Label:str = obj["CheckOff3Label"]
      """  Label used for the DMRHead.CheckOff3 field.  """  
      self.CheckOff4Label:str = obj["CheckOff4Label"]
      """  Label used for the DMR.CheckOff4 field.  """  
      self.CheckOff5Label:str = obj["CheckOff5Label"]
      """  Label used for the DMRHead.CheckOff5 field.  """  
      self.GlobalSN:bool = obj["GlobalSN"]
      """  Global SN  """  
      self.IJJournalCode:str = obj["IJJournalCode"]
      """  The Journal Code of the Journal that will be used for Inventory/WIP transactions. The Job management Calculate WIP/COS process creates entries in this journal.  """  
      self.StartNonConfID:int = obj["StartNonConfID"]
      """  Starting ID number for non-conformance records.  """  
      self.StartCorrActID:int = obj["StartCorrActID"]
      """  Starting ID number for non-conformance records.  """  
      self.ReduceRelQty:bool = obj["ReduceRelQty"]
      """  Option to keep the Sales Order Detail quantity constant.  """  
      self.SysBuyerID:str = obj["SysBuyerID"]
      """  System default buyer id.  This identifies the buyer that will be used during the auto po generation process when no buyer is defined by the PartClass or OpCode records.  """  
      self.StartTFOrderNum:int = obj["StartTFOrderNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available number is assigned by the system. The system generates a number by finding the order number of the last record on file and then a 1 to it.  """  
      self.AutoOrderBasedDisc:bool = obj["AutoOrderBasedDisc"]
      """  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The default shipvia code for the Counter Sales order.  """  
      self.InvcGrpPfx:str = obj["InvcGrpPfx"]
      """  The invoice group prefix for counter sales orders. The invoice group id is based on this prefix plus two digits of today's month  plus two digits of the today's daynumber.  """  
      self.PlantCostID:str = obj["PlantCostID"]
      """  If a Site does not have a specified SiteCostID, use this one instead  """  
      self.HDDefaultTaskSetID:str = obj["HDDefaultTaskSetID"]
      """  The default task set for use in the Help Desk.  """  
      self.HDAutoCompleteTasks:bool = obj["HDAutoCompleteTasks"]
      """  If true, users can auto-complete Help Desk tasks by changing the current workflow stage.  """  
      self.StagingReq:bool = obj["StagingReq"]
      """  Indicates whether to use the shipping staging logic  """  
      self.EAQActive:bool = obj["EAQActive"]
      """  True value indicates that the Epicor Advanced Quality module is active.  Related to IQS integration.  """  
      self.DftInputChannel:str = obj["DftInputChannel"]
      """  This field will hold the default URL for the Service Connect input channel.  This is only used as the default as the user can specify the individual URLs for data element to be passed to amd from the IQS application.  """  
      self.DftOutputChannel:str = obj["DftOutputChannel"]
      """  This field will hold the default URL for the Service Connect output channel.  This is only used as the default as the user can specify the individual URLs for data element to be passed to amd from the IQS application.  """  
      self.DefaultMiscFreightCC:str = obj["DefaultMiscFreightCC"]
      """  Default Miscellaneous Freight Charge Customer Connect  """  
      self.SOReadyToCalcDflt:bool = obj["SOReadyToCalcDflt"]
      """  This flag will be used to default the OrderHed.ReadyToCalc field when an invoice is created. Defaults to No.  """  
      self.SODiscountUnitPrice:bool = obj["SODiscountUnitPrice"]
      """  Specifies if line discounts shall be applied to the unit price or the line value.  """  
      self.DefUOMClassID:str = obj["DefUOMClassID"]
      """   Default Unit of Measure Class. Used as the default value when creating new Part masters.
Must be  valid in the UOMClass table.
The UOMClass has a default UOMCode which replaces the 8.3 XASyst.DefaultUM.  """  
      self.AlphaNumeric:str = obj["AlphaNumeric"]
      """  The character that will represent the place holder for any alphanumeric character ((e.g. 5 / A / a). Default is "&"  """  
      self.AlphaNumExample:str = obj["AlphaNumExample"]
      """  Indicates the string to use when constructing an Example for a serial mask in Serial Mask Maintenance and the AlphaNumeric character is part of the mask. The default is "A".  """  
      self.AlphaOnly:str = obj["AlphaOnly"]
      """  This is the character used to represent alpha characters (e.g. [a to z] or [A to Z]). Default is "@"  """  
      self.AlphaOnlyExample:str = obj["AlphaOnlyExample"]
      """  Indicates the string to use when constructing an Example for a serial mask in Serial Mask Maintenance and the AlphaOnly character is part of the mask. The default will be "B".  """  
      self.NumericOnly:str = obj["NumericOnly"]
      """  This is the character used to represent a numeric character (e.g. [0 to 9]). Default is "#".  """  
      self.AnyMandatory:str = obj["AnyMandatory"]
      """  This is the character used to represent a mandatory variable that can be any alphanumeric character. Therefore if the user enters 2 followed by this character in the mask then when a serial number is created these charaters must be replaced with any single character. Default is "?"  """  
      self.OptionalAlphaNumeric:str = obj["OptionalAlphaNumeric"]
      """  This character is used to represent an optional variable that can be any alphanumeric character. NOTE this character can ONLY be added as the last characters in the mask. Default is "!"  """  
      self.StripChar:str = obj["StripChar"]
      """  This character is used to represent the characters that are to be stripped off when the internal serial number is created. This character can ONLY be at the front or back of the mask. The default is "~"  """  
      self.DayChar:str = obj["DayChar"]
      """  When this character is entered in the mask surrounded by <> characters then a day number as a 2 numeric value will be automatically inserted into the serial number at that position. This will consume 2 characters of the serial number string. (Only allowed for auto generation masks). The default is "D"  """  
      self.MonthChar:str = obj["MonthChar"]
      """  When this character  is entered in the mask surrounded by <> characters this will then automatically enter into the serial number the month number as a 2 numeric value. This will consume 2 characters of the serial number string. (Only allowed for auto generation masks). The default is "M"  """  
      self.Year2Char:str = obj["Year2Char"]
      """  When this is 2 character string is entered in the mask surrounded by <> characters this will then automatically enter into the serial number the last 2 numeric values of the current calendar year. This must be entered as 2 identical  characters and will consume 2 characters of the serial number string. (Only allowed for auto generation masks). The default is "YY"  """  
      self.Year4Char:str = obj["Year4Char"]
      """  When this 4 character string is entered in the mask surrounded by < > characters this will then automatically enter into the serial number the full value of the year. This must be entered as 4 identical  characters and will consume 4 characters of the serial number string. (Only allowed for auto generation masks) The default is "YYYY"  """  
      self.PartChar:str = obj["PartChar"]
      """  If this is entered in the mask it must be followed by a hard coded numeric value indicating the number of characters of the part number that will be included in the serial number. The PartChar and the hard coded number should be encased in <> characters when building the mask. E.g. if the part representation  character is entered as "P" and the part number is DS4000-1 and <P6> is entered in the mask then DS4000 will be included in the serial number. The default is "P". (Only allowed for auto generation masks)  """  
      self.PartCharExample:str = obj["PartCharExample"]
      """  Indicates the string to use when constructing an Example for a serial mask in Serial Mask Maintenance and the PartChar character is part of the mask. The default will be  ?EPICORSERIALNUMBERMASKFORMATEXAMPLE?.  """  
      self.SODiscountRound:str = obj["SODiscountRound"]
      """  Discount rounding option: NE - Round net price by extended amount, NP - Round net price by unit price,  EP - Round discount by extended amount; UP - Round discount by unit price.  """  
      self.SMIPackSlip:int = obj["SMIPackSlip"]
      """  Pack Slip counter used for generating new automatic SMI PO Receipts.  """  
      self.SMIYear:int = obj["SMIYear"]
      """  This field holds the current year that is used as part of the key when generating an auto generated receipt for supplier managed inventories.  This is used in the program im/GenSMIReceipt.p  """  
      self.DefaultShift:int = obj["DefaultShift"]
      """  Default is blank.  Values include active shifts.  Selected value is used as the default value for Shift in Employee Maintenance.  """  
      self.IQSActive:bool = obj["IQSActive"]
      """  Select this checkbox to enable the AQM Integration. This checkbox enables movement of data in both directions, from the Epicor application to AQM and vice versa.  """  
      self.IQSOutputDir:str = obj["IQSOutputDir"]
      """  Specifies a selected folder path where the data will be exported. For example, C:\Epicor3Data\ServiceConnect\AQM\DataExportOut. Only enable if AQM integration is active.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.StartBOLNum:int = obj["StartBOLNum"]
      """  StartBOLNum  """  
      self.PrjAllowWBSPhase:bool = obj["PrjAllowWBSPhase"]
      """  Allow Project/WBS phase to be defined  """  
      self.PrjJobType:str = obj["PrjJobType"]
      """  Default Job Type of Sales Order line.  """  
      self.RMAUseRefCosts:bool = obj["RMAUseRefCosts"]
      """  Use reference invoice costs for RMA  """  
      self.UseOMBaseCurr:bool = obj["UseOMBaseCurr"]
      """  Used for Sales Order to give the ability to find price lists using the base currency if the customer currency if foreign.  """  
      self.PassedReqMove:bool = obj["PassedReqMove"]
      """  PassedReqMove  """  
      self.FailedReqMove:bool = obj["FailedReqMove"]
      """  FailedReqMove  """  
      self.PassedRMAReqMove:bool = obj["PassedRMAReqMove"]
      """  PassedRMAReqMove  """  
      self.FailedRMAReqMove:bool = obj["FailedRMAReqMove"]
      """  FailedRMAReqMove  """  
      self.QuoteToSOReadyToCalcDflt:bool = obj["QuoteToSOReadyToCalcDflt"]
      """  QuoteToSOReadyToCalcDflt  """  
      self.SOReadyToFulfillDflt:bool = obj["SOReadyToFulfillDflt"]
      """  This flag will be used to default the OrderHed.ReadyToFulfill field when a sales order is created.  """  
      self.MaxPCIDParentChildLevels:int = obj["MaxPCIDParentChildLevels"]
      """  Indicates the maximum number of levels of parent/child nesting allowed.  """  
      self.MaxWorkQueueRecords:int = obj["MaxWorkQueueRecords"]
      """  Default Amount of Rows by Page to display in the MES Work Queue UI at Startup. Set it to ZERO to retrieve all the Work Queue records at once, into one single page.  """  
      self.RMAAllowMultipleCredInv:bool = obj["RMAAllowMultipleCredInv"]
      """  RMAAllowMultipleCredInv  """  
      self.FSATranDocTypeID:str = obj["FSATranDocTypeID"]
      """  Specifies a legal number that will default when AR invoices import from Epicor FSA.  """  
      self.FSAPromptForInstallation:bool = obj["FSAPromptForInstallation"]
      """  FSAPromptForInstallation  """  
      self.FSATranDocTypeIDCreditMemo:str = obj["FSATranDocTypeIDCreditMemo"]
      """  Specifies a legal number that will default when Credit Memos import from Epicor FSA.  """  
      self.TransactionRetrievalDays:int = obj["TransactionRetrievalDays"]
      """  TransactionRetrievalDays  """  
      self.IQSOutputFormat:str = obj["IQSOutputFormat"]
      """  This field defines the format that will be used to export the data in the AQM Synchronization Process. The valid options are Extended: Extended version and Compact: Compact version. Only enabled if AQM integration is active.  """  
      self.JobReadyToFulfillDflt:bool = obj["JobReadyToFulfillDflt"]
      """  This flag will be used to default the ReadyToFulfill field for jobs.  """  
      self.TransferReadyToFulfillDflt:bool = obj["TransferReadyToFulfillDflt"]
      """  This flag will be used to default the ReadyToFulfill field for transfer orders.  """  
      self.EnableSNMaskFields:bool = obj["EnableSNMaskFields"]
      self.FSACMemoTranDocDesc:str = obj["FSACMemoTranDocDesc"]
      self.FSAInvoiceTranDocDesc:str = obj["FSAInvoiceTranDocDesc"]
      self.InvcTranType:str = obj["InvcTranType"]
      self.TmpStartOrderNum:int = obj["TmpStartOrderNum"]
      """  A temporary field for the UI for starting order number until the db StartOrderNum field format can be changed to contain 9 digits.  """  
      self.CMTranType:str = obj["CMTranType"]
      self.FSMDocTypeID:str = obj["FSMDocTypeID"]
      """  FSMDocTypeID (Attachment Document Type).  """  
      self.FSMSyncAnalysisCd:bool = obj["FSMSyncAnalysisCd"]
      """  Company flag to enable FSM sync of Analysis Code  """  
      self.FSMSyncEmpBasic:bool = obj["FSMSyncEmpBasic"]
      """  Company flag to enable FSM sync of Employee (Service Tech)  """  
      self.FSMSyncFSAssetClass:bool = obj["FSMSyncFSAssetClass"]
      """  Company flag to enable FSM sync of Asset Class (Equipment Type)  """  
      self.FSMSyncIndirect:bool = obj["FSMSyncIndirect"]
      """  Company flag to enable FSM sync of Asset Class (Work Code)  """  
      self.FSMSyncOpMaster:bool = obj["FSMSyncOpMaster"]
      """  Company flag to enable FSM sync of Operation (Condition)  """  
      self.FSMSyncPartClass:bool = obj["FSMSyncPartClass"]
      """  Company flag to enable FSM sync of Part Class  """  
      self.FSMSyncPlant:bool = obj["FSMSyncPlant"]
      """  Company flag to enable FSM sync of Site (Dispatch Location)  """  
      self.FSMSyncSerialNo:bool = obj["FSMSyncSerialNo"]
      """  Company flag to enable FSM sync of Serial Number (Equipment)  """  
      self.FSMSyncUOM:bool = obj["FSMSyncUOM"]
      """  Company flag to enable FSM sync of UOM  """  
      self.FSMSyncWarehse:bool = obj["FSMSyncWarehse"]
      """  Company flag to enable FSM sync of Warehouse  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DefaultPlantName:str = obj["DefaultPlantName"]
      self.HDTaskTaskSetDescription:str = obj["HDTaskTaskSetDescription"]
      self.HDTaskWorkflowType:str = obj["HDTaskWorkflowType"]
      self.IJJournalJrnlDescription:str = obj["IJJournalJrnlDescription"]
      self.PlantCostDescription:str = obj["PlantCostDescription"]
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_XbSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.POUserChar1Label:str = obj["POUserChar1Label"]
      """  Contains the Label used for the user defined field in the Purchase Order Master.  """  
      self.POUserChar2Label:str = obj["POUserChar2Label"]
      """  Contains the Label used for the 2nd user defined character  field in the Purchase Order Master.  """  
      self.POUserChar3Label:str = obj["POUserChar3Label"]
      """  Contains the Label used for the 3rd user defined character field in the Purchase Order Master.  """  
      self.POUserChar4Label:str = obj["POUserChar4Label"]
      """  Contains the Label used for the 4th user defined character field in the Purchase Order Master.  """  
      self.POUserDate1Label:str = obj["POUserDate1Label"]
      """  Contains the Label used for the 1st user defined date field in the Purchase Order Master..  """  
      self.POUserDate2Label:str = obj["POUserDate2Label"]
      """  Contains the Label used for the 2nd user defined date field in the Purchase Order Master.  """  
      self.POUserDate3Label:str = obj["POUserDate3Label"]
      """  Contains the Label used for the 3rd user defined date field in the Purchase Order Master.  """  
      self.POUserDate4Label:str = obj["POUserDate4Label"]
      """  Contains the Label used for the 4th user defined date  field in the Purchase Order Master.  """  
      self.POUserDec1Label:str = obj["POUserDec1Label"]
      """  Contains the Label used for the 1st user defined decimal field in the Purchase Order Master..  """  
      self.POUserDec2Label:str = obj["POUserDec2Label"]
      """  Contains the Label used for the 2nd user defined decimal field in the Purchase Order Master.  """  
      self.POUserInt1Label:str = obj["POUserInt1Label"]
      """  Contains the Label used for the 1st user defined field in the Purchase Order Master.  """  
      self.POUserInt2Label:str = obj["POUserInt2Label"]
      """  Contains the Label used for the 2nd user defined field in the Purchase Order Master.  """  
      self.ConsolidatedPurchasingCompany:str = obj["ConsolidatedPurchasingCompany"]
      """  Company that is the Parent of Consolidated Purchasing.  More than one company can be attached to a serial number that has the Consolidated Purchasing module entered.  This field designates which of those companies is the parent of Consolidated Purchasing and can therefore create Consolidated Purchase Orders.  """  
      self.GlobalCurrencyCode:str = obj["GlobalCurrencyCode"]
      """  Holds the Currency.CurrencyCode value in which Consolidated Purchasing data will be exchanged.  """  
      self.ExpPartCKOut:bool = obj["ExpPartCKOut"]
      """  Allow Express Part Checkout.  """  
      self.ConsPurchasingParent:str = obj["ConsPurchasingParent"]
      """  For internal use only.  Used with ConsolidatedPurchasingCompany to enforce security of the Consolidated Purchasing Parent company.  """  
      self.NewPoRelAtReceipt:bool = obj["NewPoRelAtReceipt"]
      """  Determines if a new PO release is created at receipt when the quantity received is less than the quantity shipped.  The new PO Rel quantity is the difference between the ship quantity and the receipt quantity.  """  
      self.CashGrpPfx:str = obj["CashGrpPfx"]
      """  Use when creating payment records from credit card payments automatically from Sales Order or from Customer Shipment  """  
      self.CCInvPfx:str = obj["CCInvPfx"]
      """  Invoice Group Prefix used for credit card groups  """  
      self.DefBankAcctID:str = obj["DefBankAcctID"]
      """  Bank Account code to be used when creating credit card payments  """  
      self.SkipLandedCostCalc:bool = obj["SkipLandedCostCalc"]
      """  Indicates whether or not Container Tracking is to calculate landed cost.  If yes, landed costs are calculated at the time the container is received.  The cubic sq feet of a container cannot be zero.  If no, landed costs are NOT calculated.  """  
      self.WebSaleGetsCommission:bool = obj["WebSaleGetsCommission"]
      """  Does a sale that originated via Customer Connect garner a Commission?  """  
      self.DefaultLabelsPrinter:str = obj["DefaultLabelsPrinter"]
      """  Default System Printer where labels are going to be sent if there is no Device available to print labels on the Current Station.  """  
      self.DefaultFormsPrinter:str = obj["DefaultFormsPrinter"]
      """  Default System Printer where forms are going to be sent if there is no Device available to print forms on the Current Station.  """  
      self.TxtLPP:int = obj["TxtLPP"]
      """   Number of lines per page for text report. This value will be written to SysRptLst.TxtLPP. The text based reports (Progress 4gl) generate a print image .txt file. This file contains new page controls characters. The Page size needs to be configurable to handle other paper sizes (ex: A4).
At this time we will allow for a page size setting to be established at the company level.  """  
      self.DefaultMiscFreightChargeCode:str = obj["DefaultMiscFreightChargeCode"]
      """  Default Miscellaneous Charges Freight Charge Code  """  
      self.PORelShipOption:str = obj["PORelShipOption"]
      """  Valid values = "None", "Short" and "Create".   At the time a container is shipped, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the shipping quantity and a new PO release is created for the difference between the original po release quantity and the ship quantity.  If this field is not set or None is selected than PO releases are not created nor are they shipped short.  This is an optional field.  """  
      self.UseTaxBoxes:bool = obj["UseTaxBoxes"]
      """  Flag to enable VAT taxboxes  """  
      self.GenRateGrp:str = obj["GenRateGrp"]
      """  Rate Group Code for General applications  """  
      self.SalesRateGrp:str = obj["SalesRateGrp"]
      """  Rate Group Code for Sales and A/R Invoicing  """  
      self.PORateGrp:str = obj["PORateGrp"]
      """  Currency Rate Group for Purchasing and A/P Invoicing  """  
      self.InvRateGrp:str = obj["InvRateGrp"]
      """  Currency Rate Group for Inventory applications  """  
      self.FARateGrp:str = obj["FARateGrp"]
      """  Currency Rate Group for Fixed Assets  """  
      self.PRRateGrp:str = obj["PRRateGrp"]
      """  Currency Rate Group for Payroll  """  
      self.CashRateGrp:str = obj["CashRateGrp"]
      """  Currency Rate Group for Cash transactions  """  
      self.RateLockType:str = obj["RateLockType"]
      """   F = Force 1:1 rate for same currencies
C = Use Conversion through base  """  
      self.UseTranDate:bool = obj["UseTranDate"]
      """  Indicates if FIFO Cost will be recorded based on Transaction Date or System Date.  By default the UseTranDate is false which means FIFO cost queue will use system date.  """  
      self.LotBatch:bool = obj["LotBatch"]
      """  Default for Part.LotBatch  """  
      self.LotMfgBatch:bool = obj["LotMfgBatch"]
      """  Default for Part.LotMfgBatch  """  
      self.LotMfgLot:bool = obj["LotMfgLot"]
      """  Default for Part.LotMfgLot  """  
      self.LotHeat:bool = obj["LotHeat"]
      """  Default for Part.LotHeat  """  
      self.LotFirmware:bool = obj["LotFirmware"]
      """  Default for Part.LotFirmware  """  
      self.LotBeforeDt:bool = obj["LotBeforeDt"]
      """  Default for Part.LotBeforeDt  """  
      self.LotMfgDt:bool = obj["LotMfgDt"]
      """  Default for Part.LotMfgDt  """  
      self.LotCureDt:bool = obj["LotCureDt"]
      """  Default for Part.LotCureDt  """  
      self.LotExpDt:bool = obj["LotExpDt"]
      """  Default for Part.LotExpDt  """  
      self.QtyDsplyDec:int = obj["QtyDsplyDec"]
      """  Controls the number of decimal places that the UI uses to display a "quantiity" field. This only controls the display, the actual number of decimals that can be entered is based on the Unit of Measure. (UomConv.NumOfDec)  """  
      self.PORelRcptOption:str = obj["PORelRcptOption"]
      """  Valid values = "Short" and "Create".   When the container arrives, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the arrived quantity and a new PO release is created for the difference between the original po release quantity and the arrived quantity.  This is an optional field.  """  
      self.AllowShipToChange:bool = obj["AllowShipToChange"]
      """  If true, then the shipto can be changed on the packing slip to a different shipto than on the Order Release. However, it can only be changed to one of the shipto's that are referenced on the order.  """  
      self.DefDisburseMethod:str = obj["DefDisburseMethod"]
      """  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume , Weight, Value, Quantity and Manual.  """  
      self.AllowSplitContainer:bool = obj["AllowSplitContainer"]
      """  Flag to indicate if container shipment lines can be split into another container shipment.  """  
      self.AllowTransferIndCost:bool = obj["AllowTransferIndCost"]
      """  Flag to indicate if Indirect Costs from one container shipment can be transferred to another.  """  
      self.AllowReceiptLC:bool = obj["AllowReceiptLC"]
      """  Flag to indicate if Landed Cost maintenance is allowed in Receipt Entry.  """  
      self.AllowLCAfterReceipt:bool = obj["AllowLCAfterReceipt"]
      """  Allow maintenance of Landed Cost after the part is received.  """  
      self.AllowUpdTransValue:bool = obj["AllowUpdTransValue"]
      """  Allow update of PO Transaction Value during Container Landed Cost Entry.  """  
      self.DisableLCUplift:bool = obj["DisableLCUplift"]
      """  Do not allow use of Uplift Percent during Landed Cost calculation.  """  
      self.EnableRoHS:bool = obj["EnableRoHS"]
      """  Allows entry of restriction types and substances in Part Master, Operation Master, ECO and Job Entry.  """  
      self.AllowDirectRollUp:bool = obj["AllowDirectRollUp"]
      """  Default value is false. When set to true then all indirect/direct roll-up radio buttons in Part Master and Job Entry should be enabled.  """  
      self.SyncSubstWeight:bool = obj["SyncSubstWeight"]
      """  Synchronize substance weight  """  
      self.StopAtFirstFailure:bool = obj["StopAtFirstFailure"]
      """  Indicates if the RoHS Compliance Process will stop at the first failure it founds.  """  
      self.OrderHistDays:int = obj["OrderHistDays"]
      """  Number of days to look back when processing Orders for the Build From Order History  """  
      self.AllowUpdSuppPrice:bool = obj["AllowUpdSuppPrice"]
      """  Indicates if user is allowed to update the Supplier Price for Receipt created by Purchase Order.  """  
      self.SuppPerctTolerance:int = obj["SuppPerctTolerance"]
      """  It is used to catch differences between updated Supplier Price for Receipt and PO Unit Price. If no value entered then do not perform percentage check.  """  
      self.SuppMonetaryTolerance:int = obj["SuppMonetaryTolerance"]
      """  It is used to catch differences between extended values of updated Supplier Price for Receipt and PO Unit Price. If no value entered then do not perform monetary check.  """  
      self.SuppPriceLimitAction:str = obj["SuppPriceLimitAction"]
      """  Receipt action to value of Supplier Price.  Valid values are "WARN" or "STOP".  WARN means that the user is given a warning, but allowed to proceed (or cancel) the Receipt with that Supplier Price.  STOP means that the Receipt line is not correct and the user should go to PO and update PO Unit Price to make receipt with mentioned price.  """  
      self.DefaultSlowMovingFmtCode:str = obj["DefaultSlowMovingFmtCode"]
      """  The default format code to be used on the Slow Moving Stock Provision report.  """  
      self.DefaultExcessFmtCode:str = obj["DefaultExcessFmtCode"]
      """  The default format code to be used on the Excess Stock Provision report.  """  
      self.CalcPSPrice:bool = obj["CalcPSPrice"]
      """  Indicates whether or not prices for transfer orders are calculated and printed on the packslip.  """  
      self.CalcPSTax:bool = obj["CalcPSTax"]
      """  Indicates whether or not taxes are calculated for a customer shipment and printed on the packslip.  """  
      self.RaisePOforCTP:bool = obj["RaisePOforCTP"]
      """  Flag that indicates if a PO should be created when confirm in CTP.  """  
      self.DefaultSORelease:str = obj["DefaultSORelease"]
      """  Setting at company level to define if the sales order releases will be created as Make Direct or Buy To Order. Sales order lines for non part master part must be BTO or Make direct.  """  
      self.EnablePI:bool = obj["EnablePI"]
      """  This would allow the user to receive non traditional payment information (such as post dated checks and bank drafts) and use it in calculating a customer's credit limit  """  
      self.APPurchType:bool = obj["APPurchType"]
      """  If box is checked, then the AP Invoice system will enable the APInvDtl.PurchCode field for European Financial postings  """  
      self.APDiscount:bool = obj["APDiscount"]
      """  Indicates that the discount amount by line needs to be captured to be sent to an external Financials package  """  
      self.AutoMatchAll:bool = obj["AutoMatchAll"]
      """  Flag to decide if the Match By Demand logic is applied to schedules in Demand Mass Review.  """  
      self.AllowShipOrdHold:bool = obj["AllowShipOrdHold"]
      """  Allow shipping orders on hold  """  
      self.ChkUnfirmSched:bool = obj["ChkUnfirmSched"]
      """  Check Unfirm Releasses Schedule  """  
      self.ChkForecastSched:bool = obj["ChkForecastSched"]
      """  Check Forcast Schedule  """  
      self.Localization:str = obj["Localization"]
      """  Localization Country  """  
      self.UseGUI:bool = obj["UseGUI"]
      """  Use Government Uniform Invoices. Taiwan localization flag.  """  
      self.UseTaxRate:bool = obj["UseTaxRate"]
      """  Indicates if taxes are calculated in a separate exchange rate  """  
      self.TaxRateGrp:str = obj["TaxRateGrp"]
      """  Currency Rate Group for Taxes  """  
      self.OCRCalcType:bool = obj["OCRCalcType"]
      """  OCR Calculation Type. Localization for Sweden, Finland and Estonia.  """  
      self.OCRNumDrivenFrom:str = obj["OCRNumDrivenFrom"]
      """  OCR number is derived from either the invoice number or a setting at the customer. Localization for Sweden, Finland and Estonia.  """  
      self.OCRLength:int = obj["OCRLength"]
      """  OCR length is the maximum length an OCR number is allowed to be. Localization setting for Sweden, Finland and Estonia.  """  
      self.UseAcctRef:bool = obj["UseAcctRef"]
      """  The flag to indicate if Account Reference number assigned to the customer should be used as Banking Reference on AR Invoice sent to the customer.  """  
      self.CSFLMWLcnNbr:str = obj["CSFLMWLcnNbr"]
      """   Malaysia Localization
LMW License Number  """  
      self.CSFCJ5LcnNbr:str = obj["CSFCJ5LcnNbr"]
      """   Malaysia Localization
CJ5 License Number  """  
      self.CSFCJ5FileNbr:str = obj["CSFCJ5FileNbr"]
      """   Malaysia Localization
CJ5 File Number  """  
      self.CancelSchedAction:str = obj["CancelSchedAction"]
      """  Field to choose between close or delete releases on SO when the demand is process  """  
      self.THTaxRecDocType:str = obj["THTaxRecDocType"]
      """  Document Type for Tax Receipt (Thailand Localization)  """  
      self.THWHTDocType:str = obj["THWHTDocType"]
      """  Withholding Tax Document Type (Thailand Localization)  """  
      self.GUISellerCityCode:str = obj["GUISellerCityCode"]
      """   Taiwan Localization
Seller City Code  """  
      self.ExpenseAutoSupplier:bool = obj["ExpenseAutoSupplier"]
      """  This field would be true if the system should automatically create a Supplier record for each Employee for processing Expenses.  """  
      self.ExpenseAutoSupplierPrefix:str = obj["ExpenseAutoSupplierPrefix"]
      """  If the system is setup to automatically create a Supplier record for each Employee for processing Expenses, this field will be the Prefix.  This value will prefix a numeric value and be used for the Supplier ID.  """  
      self.ExpenseRateGrp:str = obj["ExpenseRateGrp"]
      """  Rate Group Code for Employee Expenses  """  
      self.ExpenseVendorSeq:int = obj["ExpenseVendorSeq"]
      """  Internal sequence for automatic creation of vendors for employees.  """  
      self.ValidateBankBranchID:bool = obj["ValidateBankBranchID"]
      """  If the flag is false then users are allowed to enter  anything in the bank branch ID field in customer bank, supplier bank and BankAcct. The code will still try to do a lookup and retrieve the description of the bank branch ID.  """  
      self.ValidateBankIBAN:bool = obj["ValidateBankIBAN"]
      """  If the flag is false then users are allowed to enter anything in the bank IBAN (International Bank Account Number) field in customer bank, supplier bank and BankAcct.  If the flag is true, the checksum validation will be performed.  """  
      self.CTPSchedulingCode:str = obj["CTPSchedulingCode"]
      """  This is the default used when calculating CTP for multiple lines on an order.  If it is non-blank, then all the CTP jobs will be scheduled to complete at the same time.  It can be overridden at the time CTP is calculated.  """  
      self.ChgLogMethod:str = obj["ChgLogMethod"]
      """   Used as the collection method for creating Change Log records.
Possible values are: "D" -  Daily (Default Value), one record is created per day and everybody's changes are stored together.  "U" - User, one  record is created per day for each user.  """  
      self.ChiefAcctName:str = obj["ChiefAcctName"]
      """  Chief Accountant Name  """  
      self.ChiefAcctCellPhone:str = obj["ChiefAcctCellPhone"]
      """  Cheif Accountant Cell Phone Number  """  
      self.ChiefAcctEmail:str = obj["ChiefAcctEmail"]
      """  Cheif Accountant Email Address  """  
      self.TRBankCode:str = obj["TRBankCode"]
      """  Tax Return Bank Code  """  
      self.TRBankBranch:str = obj["TRBankBranch"]
      """  Tax Return Bank Branch  """  
      self.TRBankAcct:str = obj["TRBankAcct"]
      """  Tax Return Bank Account  """  
      self.TotalPayID:str = obj["TotalPayID"]
      """  ID number for consolidation.  """  
      self.TaxOfficeCode:str = obj["TaxOfficeCode"]
      """  Tax Office Code  """  
      self.TaxAgentName:str = obj["TaxAgentName"]
      """  Tax Agent Name  """  
      self.TaxAgentPhone:str = obj["TaxAgentPhone"]
      """  Tax Agent Phone  """  
      self.TaxAgentTaxRegNo:str = obj["TaxAgentTaxRegNo"]
      """  Tax Agent Tax Region Number  """  
      self.EDIOutboundAs:str = obj["EDIOutboundAs"]
      """  Defines the format In which the EDI Outbound Documents will be sent to output.  """  
      self.HDDefWFGroupID:str = obj["HDDefWFGroupID"]
      """  Company default Workflow Group. Used to assign to cases.  """  
      self.StartVendAuditRefID:int = obj["StartVendAuditRefID"]
      """  Starting supplier reference ID number  """  
      self.IsDiscountforDebitM:bool = obj["IsDiscountforDebitM"]
      """  IsDiscountforDebitM  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.THBranchID:str = obj["THBranchID"]
      """  THBranchID  """  
      self.UseInvRateDefTax:bool = obj["UseInvRateDefTax"]
      """  UseInvRateDefTax  """  
      self.AllowLinkedPOChg:bool = obj["AllowLinkedPOChg"]
      """  Allow changes to be made to POs that are linked to Intercompany Sales Orders  """  
      self.ConsiderWorkingDays:bool = obj["ConsiderWorkingDays"]
      """  Consider Working Days in the Delivery Days Calculation  """  
      self.DeferTaxExchRate:int = obj["DeferTaxExchRate"]
      """  DeferTaxExchRate  """  
      self.PmtTaxUseDate:int = obj["PmtTaxUseDate"]
      """  PmtTaxUseDate  """  
      self.CNAccEntityName:str = obj["CNAccEntityName"]
      """  CNAccEntityName  """  
      self.CNAccountStructure:str = obj["CNAccountStructure"]
      """  CNAccountStructure  """  
      self.CNAttachment:str = obj["CNAttachment"]
      """  CNAttachment  """  
      self.CNBaseCurrency:str = obj["CNBaseCurrency"]
      """  CNBaseCurrency  """  
      self.CNCashier:str = obj["CNCashier"]
      """  CNCashier  """  
      self.CNCFICodeCurGainLoss:str = obj["CNCFICodeCurGainLoss"]
      """  CNCFICodeCurGainLoss  """  
      self.CNChecker:str = obj["CNChecker"]
      """  CNChecker  """  
      self.CNCompType:str = obj["CNCompType"]
      """  CNCompType  """  
      self.CNDisableEntryRules:bool = obj["CNDisableEntryRules"]
      """  CNDisableEntryRules  """  
      self.CNExportPath:str = obj["CNExportPath"]
      """  CNExportPath  """  
      self.CNGroupName:str = obj["CNGroupName"]
      """  CNGroupName  """  
      self.CNGTICollector:str = obj["CNGTICollector"]
      """  CNGTICollector  """  
      self.CNGTICommTaxCode:str = obj["CNGTICommTaxCode"]
      """  CNGTICommTaxCode  """  
      self.CNGTIDefCCFlag:bool = obj["CNGTIDefCCFlag"]
      """  CNGTIDefCCFlag  """  
      self.CNGTIDefINFlag:bool = obj["CNGTIDefINFlag"]
      """  CNGTIDefINFlag  """  
      self.CNGTIDefPath:str = obj["CNGTIDefPath"]
      """  CNGTIDefPath  """  
      self.CNGTIDefPOFlag:bool = obj["CNGTIDefPOFlag"]
      """  CNGTIDefPOFlag  """  
      self.CNGTIDefPTFlag:bool = obj["CNGTIDefPTFlag"]
      """  CNGTIDefPTFlag  """  
      self.CNGTIDefSMFlag:bool = obj["CNGTIDefSMFlag"]
      """  CNGTIDefSMFlag  """  
      self.CNGTIDefSOFlag:bool = obj["CNGTIDefSOFlag"]
      """  CNGTIDefSOFlag  """  
      self.CNGTIManager:str = obj["CNGTIManager"]
      """  CNGTIManager  """  
      self.CNGTIVATCode:str = obj["CNGTIVATCode"]
      """  CNGTIVATCode  """  
      self.CNGTIVATInvLimit:int = obj["CNGTIVATInvLimit"]
      """  CNGTIVATInvLimit  """  
      self.CNGTIVATInvLineLimit:int = obj["CNGTIVATInvLineLimit"]
      """  CNGTIVATInvLineLimit  """  
      self.CNIndustry:str = obj["CNIndustry"]
      """  CNIndustry  """  
      self.CNIndustryCode:str = obj["CNIndustryCode"]
      """  CNIndustryCode  """  
      self.CNKeeper:str = obj["CNKeeper"]
      """  CNKeeper  """  
      self.CNMaker:str = obj["CNMaker"]
      """  CNMaker  """  
      self.CNOrgCode:str = obj["CNOrgCode"]
      """  CNOrgCode  """  
      self.CNRegionCode:str = obj["CNRegionCode"]
      """  CNRegionCode  """  
      self.JPFiscalCalendarID:str = obj["JPFiscalCalendarID"]
      """  JPFiscalCalendarID  """  
      self.TWGUICalendarID:str = obj["TWGUICalendarID"]
      """  TWGUICalendarID  """  
      self.ValidateTaxID:bool = obj["ValidateTaxID"]
      """  If the flag is false then users are allowed to enter anything in the Tax ID field in customer and supplier.  If the flag is true, the validation will be performed.  """  
      self.MXDebugMode:bool = obj["MXDebugMode"]
      """  MXDebugMode  """  
      self.MXDocType:str = obj["MXDocType"]
      """  MXDocType  """  
      self.MXIEPSTaxType:str = obj["MXIEPSTaxType"]
      """  MXIEPSTaxType. Obsolete, SalesTax.MXTaxType used instead  """  
      self.MXISRTaxType:str = obj["MXISRTaxType"]
      """  MXISRTaxType. Obsolete, SalesTax.MXTaxType used instead  """  
      self.MXIVATaxType:str = obj["MXIVATaxType"]
      """  MXIVATaxType. Obsolete, SalesTax.MXTaxType used instead  """  
      self.MXPACCode:str = obj["MXPACCode"]
      """  MXPACCode  """  
      self.MXTaxRcptEFT:int = obj["MXTaxRcptEFT"]
      """  MXTaxRcptEFT  """  
      self.MXTaxRcptType:str = obj["MXTaxRcptType"]
      """  MXTaxRcptType  """  
      self.MXThumbprint:str = obj["MXThumbprint"]
      """  MXThumbprint  """  
      self.MXUseExpedidoEn:bool = obj["MXUseExpedidoEn"]
      """  MXUseExpedidoEn  """  
      self.MXValidFrom:str = obj["MXValidFrom"]
      """  MXValidFrom  """  
      self.MXValidTo:str = obj["MXValidTo"]
      """  MXValidTo  """  
      self.OCRCalcAlg:str = obj["OCRCalcAlg"]
      """  OCRCalcAlg  """  
      self.NOThresholdAmt:int = obj["NOThresholdAmt"]
      """  NOThresholdAmt  """  
      self.EAddress:str = obj["EAddress"]
      """  EAddress  """  
      self.EInvOutputDir:str = obj["EInvOutputDir"]
      """  EInvOutputDir  """  
      self.EInvImpFileLocation:str = obj["EInvImpFileLocation"]
      """  EInvImpFileLocation  """  
      self.EInvImpArchiveFileLocation:str = obj["EInvImpArchiveFileLocation"]
      """  EInvImpArchiveFileLocation  """  
      self.EInvImpSelectionMethod:str = obj["EInvImpSelectionMethod"]
      """  EInvImpSelectionMethod  """  
      self.DefaultLineTaxable:bool = obj["DefaultLineTaxable"]
      """  DefaultLineTaxable  """  
      self.PEBOEPaymentMethod:int = obj["PEBOEPaymentMethod"]
      """  Bill of Exchange Payment Method  """  
      self.PEBOEPortfolioStatus:str = obj["PEBOEPortfolioStatus"]
      """  Bill of Exchange Portfolio Status  """  
      self.AsyncShip:bool = obj["AsyncShip"]
      """  AsyncShip  """  
      self.OverridePriceListPrompt:bool = obj["OverridePriceListPrompt"]
      """  Within PO Entry when modifying unit price which was derived from a supplier price list, prompt the user to confirm.  """  
      self.DisableOverridePriceListOption:bool = obj["DisableOverridePriceListOption"]
      """  Disable Override Price List option with PO Entry  """  
      self.DEBundesbankCompanyID:str = obj["DEBundesbankCompanyID"]
      """  DEBundesbankCompanyID  """  
      self.DEZ4ExportPath:str = obj["DEZ4ExportPath"]
      """  DEZ4ExportPath  """  
      self.UseLastWhseBin:bool = obj["UseLastWhseBin"]
      """  Defaults the Warehouse and Bin in Receipt to the last used for the current Part and Pack Slip  """  
      self.POQtyOption:str = obj["POQtyOption"]
      """  Indicates what Qty Option will be defaulted for new PO lines. Options are "Our" and "Supplier".  """  
      self.ReceiptQtyOption:str = obj["ReceiptQtyOption"]
      """  Indicates what Qty Option will be defaulted for new Receipt lines. Options are "Our" and "Supplier".  """  
      self.CNGTILangID:str = obj["CNGTILangID"]
      """  CNGTILangID  """  
      self.CloseReleaseAt:str = obj["CloseReleaseAt"]
      """  Defines the point at which the PO Releases will be closed. Available options are 'Arrival', 'Receipt', or 'Invoice'.  """  
      self.SubRateGrp:str = obj["SubRateGrp"]
      """  SubRateGrp  """  
      self.StopOnUOMNoRound:bool = obj["StopOnUOMNoRound"]
      """  If true and the UOM is set to no rounding and the number of decimals is exceeded, you will get an error. Otherwise the value will be truncated (same as round down currently behaves).  """  
      self.MYIndustryCode1:str = obj["MYIndustryCode1"]
      """  MYIndustryCode1  """  
      self.MYIndustryCode2:str = obj["MYIndustryCode2"]
      """  MYIndustryCode2  """  
      self.MYIndustryCode3:str = obj["MYIndustryCode3"]
      """  MYIndustryCode3  """  
      self.MYIndustryCode4:str = obj["MYIndustryCode4"]
      """  MYIndustryCode4  """  
      self.MYIndustryCode5:str = obj["MYIndustryCode5"]
      """  MYIndustryCode5  """  
      self.PEDocumentID:str = obj["PEDocumentID"]
      """  PE Document ID  """  
      self.PEIdentityDocType:str = obj["PEIdentityDocType"]
      """  PE Identity Document Type  """  
      self.CNOurBank:str = obj["CNOurBank"]
      """  CNOurBank  """  
      self.JobLotDflt:bool = obj["JobLotDflt"]
      """  JobLotDflt  """  
      self.LACTaxCalcEnabled:bool = obj["LACTaxCalcEnabled"]
      """  LACTaxCalcEnabled  """  
      self.TWGUIRegNum:str = obj["TWGUIRegNum"]
      """  TW GUI Code  """  
      self.NLMessageRefSupplierICP:str = obj["NLMessageRefSupplierICP"]
      """  NLMessageRefSupplierICP  """  
      self.NLDigipoortDeliveryURL:str = obj["NLDigipoortDeliveryURL"]
      """  NLDigipoortDeliveryURL  """  
      self.NLDigipoortStatusURL:str = obj["NLDigipoortStatusURL"]
      """  NLDigipoortStatusURL  """  
      self.NLDigipoortServerThumbprint:str = obj["NLDigipoortServerThumbprint"]
      """  NLDigipoortServerThumbprint  """  
      self.NLDigipoortClientThumbprint:str = obj["NLDigipoortClientThumbprint"]
      """  NLDigipoortClientThumbprint  """  
      self.CNGTIEncodingFormat:int = obj["CNGTIEncodingFormat"]
      """  Encoding for GTI Export file  """  
      self.POTaxReadyToProcess:bool = obj["POTaxReadyToProcess"]
      """  Flag to determine whether PO taxes will be automatically calculated each time a PO line is updated.  """  
      self.POTaxCalculate:bool = obj["POTaxCalculate"]
      """  Flag to determine whether PO taxes will be calculated.  """  
      self.PEAddressID:str = obj["PEAddressID"]
      """  PEAddressID  """  
      self.X509Code:str = obj["X509Code"]
      """  X509Code  """  
      self.COIFRSInterestRate:int = obj["COIFRSInterestRate"]
      """  COIFRSInterestRate  """  
      self.MXCURP:str = obj["MXCURP"]
      """  MXCURP  """  
      self.APTaxLnLevel:bool = obj["APTaxLnLevel"]
      """  This flag will be used to determine if taxes are calculated for AP Invoices at Document Level (Default, False) or at Line Level (True).  """  
      self.MYLMWLcnPurchaseExpDate:str = obj["MYLMWLcnPurchaseExpDate"]
      """  MYLMWLcnPurchaseExpDate  """  
      self.MYLMWPurchaseAddr:str = obj["MYLMWPurchaseAddr"]
      """  MYLMWPurchaseAddr  """  
      self.MYLMWLcnManufacturing:str = obj["MYLMWLcnManufacturing"]
      """  MYLMWLcnManufacturing  """  
      self.MYLMWLcnManufacturingExpDate:str = obj["MYLMWLcnManufacturingExpDate"]
      """  MYLMWLcnManufacturingExpDate  """  
      self.MYLMWManufacturingAddr:str = obj["MYLMWManufacturingAddr"]
      """  MYLMWManufacturingAddr  """  
      self.ReceiptTaxCalculate:bool = obj["ReceiptTaxCalculate"]
      """  Flag to determine whether Receipt taxes will be calculated.  """  
      self.CalcQuoteTax:bool = obj["CalcQuoteTax"]
      """  Flag to determine whether Quote taxes will be calculated.  """  
      self.AttBatch:str = obj["AttBatch"]
      """  Indicates if entry of a BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttMfgBatch:str = obj["AttMfgBatch"]
      """  Indicates if entry of a MFG BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttMfgLot:str = obj["AttMfgLot"]
      """  Indicates if entry of a MFG Lot is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttHeat:str = obj["AttHeat"]
      """  Indicates if entry of a Heat Number  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttFirmware:str = obj["AttFirmware"]
      """  Indicates if entry of FIRMWARE is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttBeforeDt:str = obj["AttBeforeDt"]
      """  Indicates if entry of a Best Before Date is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttMfgDt:str = obj["AttMfgDt"]
      """  Indicates if entry of a Original Manufacture Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttCureDt:str = obj["AttCureDt"]
      """  Indicates if entry of a CURE DATE  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttExpDt:str = obj["AttExpDt"]
      """  Indicates if entry of an Expiration Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.PLTaxOfficeCode:str = obj["PLTaxOfficeCode"]
      """  PLTaxOfficeCode  """  
      self.PLRegionCode:str = obj["PLRegionCode"]
      """  PLRegionCode  """  
      self.PLProvince:str = obj["PLProvince"]
      """  PLProvince  """  
      self.PLDistrict:str = obj["PLDistrict"]
      """  PLDistrict  """  
      self.PLCommunity:str = obj["PLCommunity"]
      """  PLCommunity  """  
      self.PLBuildingNum:str = obj["PLBuildingNum"]
      """  PLBuildingNum  """  
      self.PLRoomNum:str = obj["PLRoomNum"]
      """  PLRoomNum  """  
      self.PLPostOffice:str = obj["PLPostOffice"]
      """  PLPostOffice  """  
      self.INPrevYearTurnover:int = obj["INPrevYearTurnover"]
      """  Turnover in Previous Fiscal Year  """  
      self.DeferManualEntry:bool = obj["DeferManualEntry"]
      """  DeferManualEntry  """  
      self.DeferPurchaseReceipt:bool = obj["DeferPurchaseReceipt"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Container Receipt, Receipt Entry.  """  
      self.DeferJobReceipt:bool = obj["DeferJobReceipt"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Job Receipt to Job, Job Receipt to Salvage, Job Receipt to Inventory, Kanban Receipts.  """  
      self.DeferInspection:bool = obj["DeferInspection"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Inspection Processing.  """  
      self.DeferQtyAdjustment:bool = obj["DeferQtyAdjustment"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Quantity Adjustment.  """  
      self.DeferInventoryMove:bool = obj["DeferInventoryMove"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Inventory Transfer.  """  
      self.DeferShipments:bool = obj["DeferShipments"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Customer Shipment Entry, Subcontractor Shipment Entry, Drop Shipment Entry, Order Entry.  """  
      self.DeferInventoryCounts:bool = obj["DeferInventoryCounts"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Count Tag Entry.  """  
      self.DeferAssetDisposal:bool = obj["DeferAssetDisposal"]
      """  DeferAssetDisposal  """  
      self.DeferReturnMaterials:bool = obj["DeferReturnMaterials"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: RMA Processing.  """  
      self.AllowEmpWithoutResource:bool = obj["AllowEmpWithoutResource"]
      """  Flag to indicate if it is allowed to create employees with Group resource, without a resource defined.  """  
      self.INSingleTaxCatTypeSO:bool = obj["INSingleTaxCatTypeSO"]
      """  INSingleTaxCatTypeSO  """  
      self.INSingleTaxCatTypePO:bool = obj["INSingleTaxCatTypePO"]
      """  INSingleTaxCatTypePO  """  
      self.BusinessCatID:str = obj["BusinessCatID"]
      """  BusinessCatID  """  
      self.ReceiptIncludeDutyInTax:bool = obj["ReceiptIncludeDutyInTax"]
      """  Flag to determine whether Duty will be included on Taxable amount  """  
      self.INAllowChangingPP:bool = obj["INAllowChangingPP"]
      """  INAllowChangingPP  """  
      self.NLFiscalUnityTaxID:str = obj["NLFiscalUnityTaxID"]
      """  Fiscal Unity Tax ID (CSF Netherlands)  """  
      self.FSACashGrpPfx:str = obj["FSACashGrpPfx"]
      """  Prefix for incoming FSA records. To be used to create Cash Receipt groups.  """  
      self.FSAARInvGrpPfx:str = obj["FSAARInvGrpPfx"]
      """  Prefix for incoming FSA records. To be used to create AR Invoice groups.  """  
      self.FSASendARInvToPosting:bool = obj["FSASendARInvToPosting"]
      """  Indicates if inbound AR Invoices are sent to posting when received from FSA.  """  
      self.FSAInvQtyAdjustmentReasonCode:str = obj["FSAInvQtyAdjustmentReasonCode"]
      """  Reason Code to be used for inbound inventory quantity adjustments received from Epicor FSA.  """  
      self.MXLocality:str = obj["MXLocality"]
      """  MXLocality  """  
      self.MXMunicipioCode:str = obj["MXMunicipioCode"]
      """  MXMunicipioCode  """  
      self.RevaluationAR:str = obj["RevaluationAR"]
      """  RevaluationAR  """  
      self.RevaluationAP:str = obj["RevaluationAP"]
      """  RevaluationAP  """  
      self.RevaluationBA:str = obj["RevaluationBA"]
      """  RevaluationBA  """  
      self.RevaluationPCD:str = obj["RevaluationPCD"]
      """  RevaluationPCD  """  
      self.GenerateDigitalSignature:bool = obj["GenerateDigitalSignature"]
      """  GenerateDigitalSignature  """  
      self.UseCopyNumInPackSlips:bool = obj["UseCopyNumInPackSlips"]
      """  UseCopyNumInPackSlips  """  
      self.EWConfiguratorURL:str = obj["EWConfiguratorURL"]
      """  This is the location of the the EWC generator.  """  
      self.NLDigipoortServerCertID:str = obj["NLDigipoortServerCertID"]
      """  NLDigipoortServerCertID  """  
      self.NLDigipoortClientCertID:str = obj["NLDigipoortClientCertID"]
      """  NLDigipoortClientCertID  """  
      self.UnapprovedPO:str = obj["UnapprovedPO"]
      """  UnapprovedPO  """  
      self.UnconfirmedPO:str = obj["UnconfirmedPO"]
      """  UnconfirmedPO  """  
      self.FSAShipViaCode:str = obj["FSAShipViaCode"]
      """  Default Ship Via Code for return shipments of RMAs for FSA related transactions  """  
      self.FSARMAReasonCode:str = obj["FSARMAReasonCode"]
      """  Default reason code for RMAs from FSA  """  
      self.FSAExpensePMUID:int = obj["FSAExpensePMUID"]
      """  Default payment method for expenses from FSA  """  
      self.APPrepayTaxCalc:bool = obj["APPrepayTaxCalc"]
      """  APPrepayTaxCalc  """  
      self.PLWasteRegisterNum:str = obj["PLWasteRegisterNum"]
      """  Waste Register Number (CSF Poland)  """  
      self.EWCRuntimeURL:str = obj["EWCRuntimeURL"]
      """  This is the location of the EWC Runtime.  """  
      self.AGAFIPResponsibilityCode:str = obj["AGAFIPResponsibilityCode"]
      """  AGAFIPResponsibilityCode  """  
      self.EInvCompanyIDAttr:str = obj["EInvCompanyIDAttr"]
      """  E-Invoice CompanyID Attribute  """  
      self.EInvEndpointIDAttr:str = obj["EInvEndpointIDAttr"]
      """  E-Invoice EndpointID Attribute  """  
      self.PriceToleranceOnHigherPrice:bool = obj["PriceToleranceOnHigherPrice"]
      """  PriceToleranceOnHigherPrice  """  
      self.QuickShipURL:str = obj["QuickShipURL"]
      """  URL address to the Quick Ship application  """  
      self.QSUseIntl:bool = obj["QSUseIntl"]
      """  Indicates if Quick Ship International Shipments are used.  """  
      self.QSUseBOL:bool = obj["QSUseBOL"]
      """  Indicates if Quick Ship Bill of Lading  is used.  """  
      self.QSUseCO:bool = obj["QSUseCO"]
      """  Reserved for Future Development  """  
      self.CNGTIAdminGroup:str = obj["CNGTIAdminGroup"]
      """  Stores the name of the admin group referring to the security group maintenance.  """  
      self.CNCheckerSearchSeq:int = obj["CNCheckerSearchSeq"]
      """  Define the search sequence  """  
      self.CNMakerSearchSeq:int = obj["CNMakerSearchSeq"]
      """  Define the search sequence  """  
      self.SalesTaxID:str = obj["SalesTaxID"]
      """  SalesTaxID  """  
      self.ServiceTaxID:str = obj["ServiceTaxID"]
      """  ServiceTaxID  """  
      self.ELIEinvoice:bool = obj["ELIEinvoice"]
      """  ELIEinvoice  """  
      self.ELIDefReportID:str = obj["ELIDefReportID"]
      """  ELIDefReportID  """  
      self.ELIDefStyleNum:int = obj["ELIDefStyleNum"]
      """  ELIDefStyleNum  """  
      self.ELIDefToMail:str = obj["ELIDefToMail"]
      """  ELIDefToMail  """  
      self.ELIDefCCMail:str = obj["ELIDefCCMail"]
      """  ELIDefCCMail  """  
      self.ELIDefMailTempID:str = obj["ELIDefMailTempID"]
      """  ELIDefMailTempID  """  
      self.ELIDefEinvoicePath:str = obj["ELIDefEinvoicePath"]
      """  ELIDefEinvoicePath  """  
      self.ELIDefDepTranDocTypeID:str = obj["ELIDefDepTranDocTypeID"]
      """  ELIDefDepTranDocTypeID  """  
      self.PLEnableRcvDateWarning:bool = obj["PLEnableRcvDateWarning"]
      """  Enable Received Date Warning (CSF Poland)  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """  COOneTimeID  """  
      self.COFiscalResp1:str = obj["COFiscalResp1"]
      """  COFiscalResp1  """  
      self.COFiscalResp2:str = obj["COFiscalResp2"]
      """  COFiscalResp2  """  
      self.COFiscalResp3:str = obj["COFiscalResp3"]
      """  COFiscalResp3  """  
      self.CNWeightUOMClass:str = obj["CNWeightUOMClass"]
      """  Weight UOM Class  """  
      self.EORINumber:str = obj["EORINumber"]
      """  EORI Number  """  
      self.EnableNetting:bool = obj["EnableNetting"]
      """  Enable Netting Transaction Entry  """  
      self.WithholdAcctToInterim:bool = obj["WithholdAcctToInterim"]
      """  This field indicates that posting of withholding taxes will go through interim accounts when tax timing is partially paid or fully paid.  """  
      self.ELIDefFromMail:str = obj["ELIDefFromMail"]
      """  ELIDefFromMail  """  
      self.NetTranDocTypeIDCM:str = obj["NetTranDocTypeIDCM"]
      """  This transaction document type will be the one assigned for the netting credit memo created.  """  
      self.NetTranDocTypeIDDM:str = obj["NetTranDocTypeIDDM"]
      """  Description: This transaction document type will be the one assigned for the netting debit memo created  """  
      self.TWTaxDeclarationAdminGroup:str = obj["TWTaxDeclarationAdminGroup"]
      """  Security Group to be used as Tax Declaration Admins  """  
      self.TaxValidationAllow:bool = obj["TaxValidationAllow"]
      """  Enables/disables Tax Id validation.  """  
      self.TaxValidationEFTHeadUID:int = obj["TaxValidationEFTHeadUID"]
      """  Electronic Interface of type Tax Id Validation  """  
      self.TaxValidationAutomatic:bool = obj["TaxValidationAutomatic"]
      """  Enables/disables automatic Tax Id validation when customer or supplier Tax Id is changed.  """  
      self.TaxValidationAction:int = obj["TaxValidationAction"]
      """  Action if Invalid Tax ID  """  
      self.RevaluationBAUnrealized:bool = obj["RevaluationBAUnrealized"]
      """  RevaluationBAUnrealized  """  
      self.RevaluationPCDUnrealized:bool = obj["RevaluationPCDUnrealized"]
      """  RevaluationPCDUnrealized  """  
      self.HMRCTaxValidationAllow:bool = obj["HMRCTaxValidationAllow"]
      """  HMRCTaxValidationAllow  """  
      self.HMRCTaxValidationURL:str = obj["HMRCTaxValidationURL"]
      """  HMRCTaxValidationURL  """  
      self.HMRCTaxValidationAutomatic:bool = obj["HMRCTaxValidationAutomatic"]
      """  HMRCTaxValidationAutomatic  """  
      self.HMRCTaxValidationAction:int = obj["HMRCTaxValidationAction"]
      """  HMRCTaxValidationAction  """  
      self.AttISOrigCountry:str = obj["AttISOrigCountry"]
      """  Indicates if entry of a County of Origin is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.ExternalSchemeID:str = obj["ExternalSchemeID"]
      """  Company Scheme ID  """  
      self.ExternalID:str = obj["ExternalID"]
      """  Company ID  """  
      self.SiteIsLegalEntity:bool = obj["SiteIsLegalEntity"]
      """  Indicates site can be used as a legal entity.  """  
      self.MYTaxRateByKg:str = obj["MYTaxRateByKg"]
      """  Tax Rate by Kg  """  
      self.MYTaxRateByLiter:str = obj["MYTaxRateByLiter"]
      """  Tax Rate by Liter  """  
      self.TWEncryptionKey:str = obj["TWEncryptionKey"]
      """  Encryption Key  """  
      self.ELIOperatorCode:str = obj["ELIOperatorCode"]
      """  EInvoice Operator Code  """  
      self.CurrExDiff:int = obj["CurrExDiff"]
      """  Indicates the logic used to calculate the base/rpt fields.  Currently used by Bank Funds Transfer  """  
      self.ERSDocTypeID:str = obj["ERSDocTypeID"]
      """  The document type used to generate the legal number for the invoices generated automatically at the shipment.  """  
      self.ERSInvGrpPrefix:str = obj["ERSInvGrpPrefix"]
      """  The group prefix used to generated the invoice group for the invoice generated automatically by the system when shipping an ERS PO.  """  
      self.InboundPath:str = obj["InboundPath"]
      """  Default Path where the files will be stored to be read by the Import EDI Process.  """  
      self.ELIERSDocTypeID:str = obj["ELIERSDocTypeID"]
      """  ELIERSDocTypeID  """  
      self.ELISendMail:bool = obj["ELISendMail"]
      """  ELISendMail  """  
      self.ELISendingOption:int = obj["ELISendingOption"]
      """  ELISendingOption  """  
      self.PlasticTaxUOMCode:str = obj["PlasticTaxUOMCode"]
      """  PlasticTaxUOMCode  """  
      self.PlasticTaxRate:int = obj["PlasticTaxRate"]
      """  PlasticTaxRate  """  
      self.CNQuantityControl:int = obj["CNQuantityControl"]
      """  CNQuantityControl  """  
      self.QuickShipRegCode:str = obj["QuickShipRegCode"]
      """  QuickShip Registration Code  """  
      self.QuickShipAPIURL:str = obj["QuickShipAPIURL"]
      """  URL address to the Quick Ship API  """  
      self.QuickShipUserID:str = obj["QuickShipUserID"]
      """  Quick Ship User Name  """  
      self.QuickShipPassword:str = obj["QuickShipPassword"]
      """  Quick Ship Password  """  
      self.CNBondedWhseControl:int = obj["CNBondedWhseControl"]
      """  CNBondedWhseControl  """  
      self.FreightSvcInt:str = obj["FreightSvcInt"]
      """  Freight Service Integration Selection. (AI - REST API Integration, QW - Quick Ship Web Services)  """  
      self.BaseUOMClassID:str = obj["BaseUOMClassID"]
      """  BaseUOMClassID  """  
      self.AutoLockFinGroups:bool = obj["AutoLockFinGroups"]
      """  Indicates financial groups are automatically locked on selection or creation  """  
      self.KBMaxDocTypeID:str = obj["KBMaxDocTypeID"]
      """  Controls where Attachments are place when CPQ pushes them to Kinetic.  The selected Document Type must be of Server Transfer Type.  If the selected Document Type is Reserved for Specific Tables, the Document Type Control must include the following tables: OrderDtl, QuoteAsm, QuoteDtl, JobAsmbl, JobHead.  If no Document Type is selected, the CPQ Quote Sync will be the master and pull attachments from CPQ and if there is a value CPQ Quote Sync will not run.  """  
      self.ELIRcptDefStyleNum:int = obj["ELIRcptDefStyleNum"]
      """  Default E-invoice Report Style  """  
      self.CNCFICodeDescription:str = obj["CNCFICodeDescription"]
      self.CNCOACode:str = obj["CNCOACode"]
      """  CSF China - dynamic field for calculating of the XBSyst.CNCFICodeCurGainLoss field.  """  
      self.EInvWSURL:str = obj["EInvWSURL"]
      """  Web-Service URL for E-Invoice.  """  
      self.EnableOCRCalcType:bool = obj["EnableOCRCalcType"]
      self.EnableReverse:bool = obj["EnableReverse"]
      """   If this flag is true then on Currency Revaluation screen the Reverse checkbox is enabled.
If this flag is false then on Currency Revaluaion screen Reverse checkbox is Read Only and set to true.  """  
      self.IsDiscountforCreditM:bool = obj["IsDiscountforCreditM"]
      """  Enable calculation of settlement discounts for credit memos in AR  """  
      self.JPFiscalCalDescription:str = obj["JPFiscalCalDescription"]
      self.PECollectionAgent:bool = obj["PECollectionAgent"]
      """  Peru Collection Agent withholding status  """  
      self.PEGoodsContributor:bool = obj["PEGoodsContributor"]
      """  Peru Goods Contributor withholding status  """  
      self.PENoAddress:bool = obj["PENoAddress"]
      """  Peru No Address Provided withholding status  """  
      self.PENotFound:bool = obj["PENotFound"]
      """  Peru Not Found withholding status.  """  
      self.PEWithholdAgent:bool = obj["PEWithholdAgent"]
      """  Peru Withholding Agent withholding status  """  
      self.PORelShipOptDisplay:str = obj["PORelShipOptDisplay"]
      """  Display used to for PORelShipOption  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.TWEncryptionKeyInput:str = obj["TWEncryptionKeyInput"]
      """  The field for user to input Company Encryption Key  """  
      self.CNSegmentNbr:int = obj["CNSegmentNbr"]
      """  CSF China - dynamic field for calculating of the XBSyst.CNCFICodeCurGainLoss field.  """  
      self.CurrencyExchangeDiff:str = obj["CurrencyExchangeDiff"]
      """  Currency Exchange Difference  """  
      self.OneEDIAPIUrl:str = obj["OneEDIAPIUrl"]
      """  URL of the OneEDI API Endpoint to post the demand outbound to  """  
      self.OneEDIAPIClientId:str = obj["OneEDIAPIClientId"]
      """  Client Id required to access OneEDI API  """  
      self.OneEDIAPIClientSecret:str = obj["OneEDIAPIClientSecret"]
      """  Client Secret required to access OneEDI API  """  
      self.KBMaxUrl:str = obj["KBMaxUrl"]
      """  CPQ Instance URL.  """  
      self.KBMaxUsername:str = obj["KBMaxUsername"]
      """  CPQ Username used for communication.  """  
      self.KBMaxPassword:str = obj["KBMaxPassword"]
      """  CPQ password used for communication.  """  
      self.KBMaxSqlInstance:str = obj["KBMaxSqlInstance"]
      """  CPQ SQL Instance for syncing data between Kinetic and CPQ.  """  
      self.KBMaxSqlDatabase:str = obj["KBMaxSqlDatabase"]
      self.KBMaxSqlUsername:str = obj["KBMaxSqlUsername"]
      self.KBMaxSqlPassword:str = obj["KBMaxSqlPassword"]
      self.InactivateSiteSegments:bool = obj["InactivateSiteSegments"]
      """  Indicates if site segements should be inactivated.  """  
      self.EDISupplierEnable:bool = obj["EDISupplierEnable"]
      self.BitFlag:int = obj["BitFlag"]
      self.BankBankName:str = obj["BankBankName"]
      self.BankDescription:str = obj["BankDescription"]
      self.CNOurBankBankAcctDescription:str = obj["CNOurBankBankAcctDescription"]
      self.CNOurBankBankAcctBankName:str = obj["CNOurBankBankAcctBankName"]
      self.CurrCashRateGrpDescription:str = obj["CurrCashRateGrpDescription"]
      self.CurrExpenseRateGrpDescription:str = obj["CurrExpenseRateGrpDescription"]
      self.CurrFARateGrpDescription:str = obj["CurrFARateGrpDescription"]
      self.CurrGenRateGrpDescription:str = obj["CurrGenRateGrpDescription"]
      self.CurrInvRateGrpDescription:str = obj["CurrInvRateGrpDescription"]
      self.CurrPORateGrpDescription:str = obj["CurrPORateGrpDescription"]
      self.CurrPRRateGrpDescription:str = obj["CurrPRRateGrpDescription"]
      self.CurrSalesRateGrpDescription:str = obj["CurrSalesRateGrpDescription"]
      self.CurrSubRateGrpDescription:str = obj["CurrSubRateGrpDescription"]
      self.CurrTaxRateGrpDescription:str = obj["CurrTaxRateGrpDescription"]
      self.FSAExpensePMUIDType:int = obj["FSAExpensePMUIDType"]
      self.FSAExpensePMUIDName:str = obj["FSAExpensePMUIDName"]
      self.FSAExpensePMUIDSummarizePerCustomer:bool = obj["FSAExpensePMUIDSummarizePerCustomer"]
      self.FSARMAReasonCodeDescription:str = obj["FSARMAReasonCodeDescription"]
      self.FSAShipViaCodeDescription:str = obj["FSAShipViaCodeDescription"]
      self.FSAShipViaCodeWebDesc:str = obj["FSAShipViaCodeWebDesc"]
      self.GlobalCurrencyDocumentDesc:str = obj["GlobalCurrencyDocumentDesc"]
      self.GlobalCurrencyCurrDesc:str = obj["GlobalCurrencyCurrDesc"]
      self.GlobalCurrencyCurrName:str = obj["GlobalCurrencyCurrName"]
      self.GlobalCurrencyCurrencyID:str = obj["GlobalCurrencyCurrencyID"]
      self.GlobalCurrencyCurrSymbol:str = obj["GlobalCurrencyCurrSymbol"]
      self.MXDocTypeDescription:str = obj["MXDocTypeDescription"]
      self.StockProvFmtExcessDescription:str = obj["StockProvFmtExcessDescription"]
      self.StockProvFmtSlowDescription:str = obj["StockProvFmtSlowDescription"]
      self.SysFormsPrinterDescription:str = obj["SysFormsPrinterDescription"]
      self.SysLabelsPrinterDescription:str = obj["SysLabelsPrinterDescription"]
      self.THTaxRecDocTypeDescription:str = obj["THTaxRecDocTypeDescription"]
      self.THWHTDocTypeDescription:str = obj["THWHTDocTypeDescription"]
      self.WFGroupDescription:str = obj["WFGroupDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeJPFiscalCalendarID_input:
   """ Required : 
   ipJPFiscalCalendarID
   ds
   """  
   def __init__(self, obj):
      self.ipJPFiscalCalendarID:str = obj["ipJPFiscalCalendarID"]
      """  Proposed input value of Japan Fiscal Calendar  """  
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class ChangeJPFiscalCalendarID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSendToFSA_input:
   """ Required : 
   sendToFSA
   ds
   """  
   def __init__(self, obj):
      self.sendToFSA:bool = obj["sendToFSA"]
      """  Proposed input value for checkbox Sync to FSA  """  
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class ChangeSendToFSA_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckAPTaxLnLevel_input:
   """ Required : 
   ipAPTaxLnLevel
   ds
   """  
   def __init__(self, obj):
      self.ipAPTaxLnLevel:bool = obj["ipAPTaxLnLevel"]
      """  New APTaxLnLevel value  """  
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class CheckAPTaxLnLevel_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckARinvcDates_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckDefTaxLiability_input:
   """ Required : 
   cTaxLiabilityCode
   """  
   def __init__(self, obj):
      self.cTaxLiabilityCode:str = obj["cTaxLiabilityCode"]
      """  Default Tax Liability code  """  
      pass

class CheckDefTaxLiability_output:
   def __init__(self, obj):
      pass

class CheckDefTaxType_input:
   """ Required : 
   cTaxTypeCode
   """  
   def __init__(self, obj):
      self.cTaxTypeCode:str = obj["cTaxTypeCode"]
      """  Default Tax Type code  """  
      pass

class CheckDefTaxType_output:
   def __init__(self, obj):
      pass

class CheckPayrollDate_input:
   """ Required : 
   payrollDate
   """  
   def __init__(self, obj):
      self.payrollDate:str = obj["payrollDate"]
      """  Payroll Start Date  """  
      pass

class CheckPayrollDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.payrollMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckRedStornoOpt_input:
   """ Required : 
   ipRedStornoOpt
   """  
   def __init__(self, obj):
      self.ipRedStornoOpt:str = obj["ipRedStornoOpt"]
      """  proposed red storno option. This needs to run if the option is NP (not permitted)  """  
      pass

class CheckRedStornoOpt_output:
   def __init__(self, obj):
      pass

class CheckUDCodeEx_input:
   """ Required : 
   cCodeTypeID
   cCodeID
   lPublishEx
   """  
   def __init__(self, obj):
      self.cCodeTypeID:str = obj["cCodeTypeID"]
      """  User-defined code type.  """  
      self.cCodeID:str = obj["cCodeID"]
      """  Code ID for check.  """  
      self.lPublishEx:bool = obj["lPublishEx"]
      """  If Yes - exception should be raised if UD code does not exist; If No - exception should not be raised.  """  
      pass

class CheckUDCodeEx_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cDescription:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckUDCodesExistence_input:
   """ Required : 
   cCodeID
   """  
   def __init__(self, obj):
      self.cCodeID:str = obj["cCodeID"]
      """  Code ID for check.  """  
      pass

class CheckUDCodesExistence_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.lUDCodeExists:bool = obj["lUDCodeExists"]
      pass

      """  output parameters  """  

class CheckVATFormat_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class CheckVATFormat_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChgCompanyFisCal_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class ChgCompanyFisCal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChgCountry_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class ChgCountry_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChgJCSystForecastPeriods_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class ChgJCSystForecastPeriods_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChgingMJTemplate_input:
   """ Required : 
   ds
   proposedTemplateJobNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      self.proposedTemplateJobNum:str = obj["proposedTemplateJobNum"]
      """  Proposed input value of the Template Job Num  """  
      pass

class ChgingMJTemplate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CleanHCMLink_output:
   def __init__(self, obj):
      pass

class CompanyTaxConnectCertCaptureEnabled_input:
   """ Required : 
   company
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  Company  """  
      pass

class CompanyTaxConnectCertCaptureEnabled_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class CompanyTaxConnectEnabled_input:
   """ Required : 
   company
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  Company  """  
      pass

class CompanyTaxConnectEnabled_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   company
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DisabledGLFields_input:
   """ Required : 
   vCompany
   """  
   def __init__(self, obj):
      self.vCompany:str = obj["vCompany"]
      """  Company number  """  
      pass

class DisabledGLFields_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vFieldList:str = obj["parameters"]
      pass

      """  output parameters  """  

class ETCAfterAddrVal_input:
   """ Required : 
   ds
   ds1
   companyID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_ETCAddrValidationTableset] = obj["ds1"]
      self.companyID:str = obj["companyID"]
      """  Company.CompanyID  """  
      pass

class ETCAfterAddrVal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ETCValidateAddress_input:
   """ Required : 
   companyID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  Company.Company  """  
      pass

class ETCValidateAddress_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ETCAddrValidationTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.statusFlag:bool = obj["statusFlag"]
      self.errorFlag:bool = obj["errorFlag"]
      self.errorMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_AGCompanyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GenFilesFolder:str = obj["GenFilesFolder"]
      """  Generated Files Folder  """  
      self.InvMoveMandCUIT:bool = obj["InvMoveMandCUIT"]
      """  Inventory Movement Mandatory CUIT  """  
      self.SOMandCUIT:bool = obj["SOMandCUIT"]
      """  Sales Order Mandatory CUIT  """  
      self.DefaultDestination:str = obj["DefaultDestination"]
      """  Default Import Destination  """  
      self.TransportKey:str = obj["TransportKey"]
      """  Transport Key  """  
      self.WHCertificateSigner:str = obj["WHCertificateSigner"]
      """  Withholding Certificate Signer  """  
      self.SignerPosition:str = obj["SignerPosition"]
      """  Signer Position  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.WebServiceConfigCode:str = obj["WebServiceConfigCode"]
      """  Web Service Code  """  
      self.ElectronicCreditInvMinAmt:int = obj["ElectronicCreditInvMinAmt"]
      """  ElectronicCreditInvMinAmt  """  
      self.FinOption:str = obj["FinOption"]
      """  FinOption  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SaveReceipts:bool = obj["SaveReceipts"]
      """  Indicates if Receipt transactions are to be used to create invoices. This flag is used by the Receipt entry program to set the value of the RcvHead.SaveForInvoicing.  Invoice entry pulls in receipt details  Receipt.SaveForInvoicing = Yes and Receipt.Invoiced =  No.  """  
      self.AlwaysDiscount:bool = obj["AlwaysDiscount"]
      """  Configures the A/P automatic invoice payment selection process to unconditionally take any available discount amount.  """  
      self.FmtCode:str = obj["FmtCode"]
      """  Identifies default aging format, the details of which is stored in the AgingRptFmt table.  """  
      self.DefaultFmtCode:str = obj["DefaultFmtCode"]
      """  Stores the FmtCode of the AgingRptFmt record that is to be considered the A/P default.  """  
      self.CheckPerforationLineNum:int = obj["CheckPerforationLineNum"]
      """  Used by AP Check printing.  It is the line # at which the check perforation is.  """  
      self.CPayParent:str = obj["CPayParent"]
      """  For internal use only.  Used with CPayCompany to enforce security of the Centralized Payment Parent company.  """  
      self.CPayCompany:str = obj["CPayCompany"]
      """  Company that is the Parent of Centralized Payment process.  More than one company can be attached to a serial number that has the Centralized Payment module entered.  This field designates which of those companies is the Central Payment Parent Company and can therefore create invoices flagged for centralized payment.  """  
      self.AllowReverseCharges:bool = obj["AllowReverseCharges"]
      """  Indicates if user is allowed to override the Reverse Charge Method in the AP invoice line.  """  
      self.RoundTolerance:int = obj["RoundTolerance"]
      """  It used to catch rounding differences that might occur when vendor invoices are settled in a currency different from the invoice currency  """  
      self.RoundInvoice:bool = obj["RoundInvoice"]
      """  If the value is true and in case the total balance of an invoice transaction is within the total rounding setup for the currency of the invoice the balance is automatically accepted and booked as a rounding difference.  If the value is false the user has to balance the transaction manually.  """  
      self.LogInvAccting:str = obj["LogInvAccting"]
      """   Determines how a logged invoice is processed through the accounting system.
TR = Authorization Tracking.  Logged invoices are not processed by the Posting Engine.  Logging invoices is done for tracking purposes.  Full accounting is done when the AP Invoice is created.
TA - Account for Taxes.  When logged invoices are posted, accounts payable and tax amounts are booked directly to the respective accounts, the invoice net amount is posted to a Logged Invoice Suspense Account.  The entry is removed from the suspense account when the logged invoice is converted to an AP Invoice.
S - Book All to a Suspense Account.  When the logged invoice is posted the tax invoice and net amount are posted to a Logged Invoice Suspense Account.  The entry is removed from the suspense account when the logged invoice is voided or converted to a regular AP Invoice.  """  
      self.AuthAdmins:str = obj["AuthAdmins"]
      """  List of authorized administrators who are able to mark a logged action as complete.  """  
      self.LogInvAutoAprv:bool = obj["LogInvAutoAprv"]
      """  Indicates if Logged Invoices are created in an Aprpoved state or if they must be manually approved.  If the Accounting Option is 'Authorization Tracking' logged invoices can not be auto approved.  """  
      self.GLStage:str = obj["GLStage"]
      """  First G/L Update Stage  """  
      self.NextPINum:int = obj["NextPINum"]
      """  Next available number in PI numbering sequence  """  
      self.NumDigit:int = obj["NumDigit"]
      """  Number of digits allowed for PI Numbering  """  
      self.NextExpInvSeq:int = obj["NextExpInvSeq"]
      """  Next available number sequence for ap invoices created from employee expenses.  """  
      self.InvcReadyToCalcDflt:bool = obj["InvcReadyToCalcDflt"]
      """  This flag will be used to default the InvcHead.ReadyToCalc field when an Account Payable invoice is created. Defaults to No.  """  
      self.ExchangeDateToUse:int = obj["ExchangeDateToUse"]
      """  Indicates which date to use (Apply/Invoice Date) to calculate exchange rates.  """  
      self.LNBasedOnDate:int = obj["LNBasedOnDate"]
      """  Invoice Legal Numbers based on “Apply/Invoice” Date for AP invoices and Debit Memos  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CopyExcRateDM:bool = obj["CopyExcRateDM"]
      """  Indicates that it need to copy exchange Rates during generation of AP Debit Memo.  """  
      self.CopyExcRateCorrInv:bool = obj["CopyExcRateCorrInv"]
      """  Indicates that it need to copy exchange Rates for creating AP Correction Invoice.  """  
      self.UsePODtlTaxable:bool = obj["UsePODtlTaxable"]
      """  The Taxable option from Purchase Order Entry is brought into AP Invoice Entry.  """  
      self.LNReqForInvc:bool = obj["LNReqForInvc"]
      """  Invoice Legal Number required for AP Invoices and Debit Memos.  """  
      self.ApplyAPPrePayAuto:bool = obj["ApplyAPPrePayAuto"]
      """  Apply pre-payments on accounts payable (AP) invoices automatically.  """  
      self.DatesSetUp:bool = obj["DatesSetUp"]
      """  Field to enable functionality of Dates Set Up  """  
      self.APAmdApplyDate:bool = obj["APAmdApplyDate"]
      """  Field to Allow Amend the Apply Date on AP Invoices  """  
      self.APAmdTaxPDate:bool = obj["APAmdTaxPDate"]
      """  Field to Allow Amend the Tax Point Date on AP Invoices  """  
      self.APAmdTaxRateD:bool = obj["APAmdTaxRateD"]
      """  Field to Allow Amend the Tax Rate Date on AP Invoices  """  
      self.APDefApplyDate:str = obj["APDefApplyDate"]
      """  Field to default the Apply Date on AP Invoices  """  
      self.APDefTaxPDate:str = obj["APDefTaxPDate"]
      """  Field to default the Tax Point Date on AP Invoices  """  
      self.APDefTaxRateD:str = obj["APDefTaxRateD"]
      """  Field to default the Tax Rate Date on AP Invoices  """  
      self.APLinkApplyDate:str = obj["APLinkApplyDate"]
      """  Field to link the Apply Date on AP Invoices  """  
      self.APLinkTaxPDate:str = obj["APLinkTaxPDate"]
      """  Field to link the Tax Point Date on AP Invoices  """  
      self.APLinkTaxRateD:str = obj["APLinkTaxRateD"]
      """  Field to link the Tax Rate Date on AP Invoices  """  
      self.TWAPLegNumSource:str = obj["TWAPLegNumSource"]
      """  TWAPLegNumSource  """  
      self.TWAPThresholdTax:int = obj["TWAPThresholdTax"]
      """  TWAPThresholdTax  """  
      self.TaxYear:int = obj["TaxYear"]
      """  Current Tax Year  """  
      self.PayersTIN:str = obj["PayersTIN"]
      """  Taxpayer Identification Number for Payer  """  
      self.NameControl:str = obj["NameControl"]
      """  Name Control for 1099 Payer  """  
      self.OfficeCode:str = obj["OfficeCode"]
      """  Office Code for 1099 Payer  """  
      self.Name1:str = obj["Name1"]
      """  First line of the Payer name  """  
      self.Name2:str = obj["Name2"]
      """  Second line of Payer name  """  
      self.Address1:str = obj["Address1"]
      """  First address line of the Payer address  """  
      self.Address2:str = obj["Address2"]
      """  Second address line of the Payer address  """  
      self.Address3:str = obj["Address3"]
      """  Third address line of the Payer address  """  
      self.City:str = obj["City"]
      """  City portion of the address of the Payer address  """  
      self.State:str = obj["State"]
      """  State portion of the Payer address  """  
      self.ZIP:str = obj["ZIP"]
      """  Postal code or zip code portion of the Payer address  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The phone number of the Payer  """  
      self.TransControlCode:str = obj["TransControlCode"]
      """  Transmitter Control Code  """  
      self.COExtWordAmt:str = obj["COExtWordAmt"]
      """  COExtWordAmt  """  
      self.DeferredExpCurr:int = obj["DeferredExpCurr"]
      """  DeferredExpCurr  """  
      self.AllowMultInvcReceipts:bool = obj["AllowMultInvcReceipts"]
      """  Flag that allows to create multiple invoicing of receipts  """  
      self.DaysOutstanding:int = obj["DaysOutstanding"]
      """  Days outstanding allowed. It is used to validate if the days between the invoice date and receipt date are greater or equal than this value  """  
      self.PcntTolerance:int = obj["PcntTolerance"]
      """  Percentage of tolerance that is allowed in each receipt and its invoiced and not invoiced lines  """  
      self.AmountTolerance:int = obj["AmountTolerance"]
      """  Amount of tolerance that is allowed in each receipt and its not invoiced lines  """  
      self.TaxEntityType:str = obj["TaxEntityType"]
      """  Type of the Payer  """  
      self.TaxEntitySubCat:str = obj["TaxEntitySubCat"]
      """  Subcategory of the Payer  """  
      self.ContactPerson:str = obj["ContactPerson"]
      """  Contact person name  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Role/Designation of the contact person  """  
      self.BranchName:str = obj["BranchName"]
      """  Name of the office branch  """  
      self.PayersPAN:str = obj["PayersPAN"]
      """  Permanent Account Number for Payer  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Contact person email address  """  
      self.AreaCode:str = obj["AreaCode"]
      """  Area code for the phone number of the Payer  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The fax number of the Payer  """  
      self.FutureDateAction:str = obj["FutureDateAction"]
      """  The action to take when an AP Invoice Invoice Date or Apply Date is greater than today plus the days horizon.  Options are (W)arning, (S)top, (N)one  """  
      self.FutureDateDaysHorizon:int = obj["FutureDateDaysHorizon"]
      """  The number of days beyond today's date that an AP Invoice Invoice Date or Appy Date can be.  """  
      self.US1099KFiler:str = obj["US1099KFiler"]
      """  Form 1099-K Filer  """  
      self.US1099KPSEName:str = obj["US1099KPSEName"]
      """  Form 1099-K PSE Name  """  
      self.US1099KPSEPhone:str = obj["US1099KPSEPhone"]
      """  Form 1099-K PSE Phone  """  
      self.CopyExcRateCancelInv:bool = obj["CopyExcRateCancelInv"]
      """  Indicates that the exchange rate will be copied when creating an AP Cancellation Invoice.  """  
      self.APTaxRoundOption:int = obj["APTaxRoundOption"]
      """  APTaxRoundOption  """  
      self.EInvoice:bool = obj["EInvoice"]
      """  EInvoice  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  TaxRegionCode  """  
      self.CentralizedPayment:bool = obj["CentralizedPayment"]
      """  Centralized Payment  """  
      self.US1099ReportBySite:bool = obj["US1099ReportBySite"]
      """  US1099ReportBySite  """  
      self.APTaxRptDate:int = obj["APTaxRptDate"]
      """  Indicates which date is used for TaxTran Transaction Date - AP Invoices related records  """  
      self.AuthAdminsName:str = obj["AuthAdminsName"]
      self.ExchangeDate:int = obj["ExchangeDate"]
      """  Indicates which date to use to calculate exchange rates  """  
      self.TaxRegionCodeDesc:str = obj["TaxRegionCodeDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.AgingRptFmtDescription:str = obj["AgingRptFmtDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.StartInvoiceNum:int = obj["StartInvoiceNum"]
      """  Used to establish the beginning Invoice #. When the system generates a new InvcHead it will assign the greater of (StartInvoiceNum) or (the last Invoice # on file + 1) as the invoice number.  """  
      self.SaveShipments:bool = obj["SaveShipments"]
      """  Indicates if Shipment transactions are to be used to create invoices. This flag is used by the Shipping entry program to set the value of the  "Invoiced" flag field. (see ShipHead.Invoiced).  Invoice entry generates invoices for Shipments which contain  "Invoiced" flag =  No.  """  
      self.CreditOrderAction:str = obj["CreditOrderAction"]
      """  Order Entry action to a Credit Held customer.  Valid values are "WARN" or "STOP".  WARN means that the user is given a warning, but allowed to proceed (or cancel) with the order and customer placed on credit hold.  STOP means that the order line addition/change to the order is not accepted and the order and customer are not placed on credit hold.  """  
      self.CreditShipAction:str = obj["CreditShipAction"]
      """  Shipping Entry action to a Credit Held order.  Valid values are "WARN" or "STOP".  WARN means that the user is warned that the order is on credit hold, but allowed to proceed (or cancel) with the shipment.  STOP means that the shipment for that order is not accepted.  """  
      self.SJJournalCode:str = obj["SJJournalCode"]
      """  The Journal Code of the Journal that will be used for A/R invoices. Normally this would be called Sales Journal.  """  
      self.AJJournalCode:str = obj["AJJournalCode"]
      """   The Journal Code of the Journal that will be used for A/R adjustments and application of credit memos.
Normally this would be called the Adjustments Journal.  """  
      self.UseShipDateForInvDate:bool = obj["UseShipDateForInvDate"]
      """  Use Shipment date for Invoice Date  """  
      self.DefaultFmtCode:str = obj["DefaultFmtCode"]
      """  Stores the FmtCode of the AgingRptFmt record that is to be considered the A/R default.  """  
      self.FmtCode:str = obj["FmtCode"]
      """  Identifies default aging format, the details of which is stored in the AgingRptFmt table.  """  
      self.InvcReadyToCalcDflt:bool = obj["InvcReadyToCalcDflt"]
      """  This flag will be used to default the InvcHead.ReadyToCalc field when an invoice is created. Defaults to No  """  
      self.AllowReverseCharges:bool = obj["AllowReverseCharges"]
      """  Indicates if user is allowed to override the Reverse Charge Method in the AR invoice line.  """  
      self.RoundTolerance:int = obj["RoundTolerance"]
      """  It is used to catch rounding differences that might occur when customer invoices are settled in a currency different from the invoice currency.  """  
      self.TaxARCustomRules:bool = obj["TaxARCustomRules"]
      """  if Yes it means that tax rounding and calculation level (line or total) are performed according to rules set on each customer, if NO - according to company setup  """  
      self.RlsClassCredit:str = obj["RlsClassCredit"]
      """  Credit checking relationship  """  
      self.RlsClassReport:str = obj["RlsClassReport"]
      """  Reporting relationship class  """  
      self.RlsClassPayerSold:str = obj["RlsClassPayerSold"]
      """  Payer-sold to relationship, lets payer customer pays for the sold to customer, who is billed in the invoice  """  
      self.AcrossNatAcc:bool = obj["AcrossNatAcc"]
      """  Accepts payments from any customer within the same national account, regardless of parent-child status  """  
      self.ProrateDiscToLine:bool = obj["ProrateDiscToLine"]
      """  This field is used to enable ability in Cash Receipts to prorate the discount amount back to the original sales accounts instead of the Discount Account of the module or group part.  """  
      self.LNReqForInvc:bool = obj["LNReqForInvc"]
      """  Indicates if legal numbers are required for invoices.  """  
      self.ChargeMethod:bool = obj["ChargeMethod"]
      """  Indicates how finance/late charges are calculated and charged with these two options: Percentage on Invoice Amount (Default) or Percentage on Amount Overdue.  """  
      self.OncePerInvoice:bool = obj["OncePerInvoice"]
      """  Indicates if finance charge shall only be applied once per invoice. In case it?s not checked, finance charges shall be calculated each time the process is executed.  """  
      self.CombWReminder:bool = obj["CombWReminder"]
      """  Indicates that the system will generate a combined reminder letter and finance charge invoice.  """  
      self.ARClearing:bool = obj["ARClearing"]
      """  A/R Clearing Accounting  """  
      self.AllowSettlementInDiffCurr:bool = obj["AllowSettlementInDiffCurr"]
      """  Indicates if user is allowed to set Invoice Settlement in Different Currency for Cash Receipts and Credit Memo.  """  
      self.ARDefApplyDate:str = obj["ARDefApplyDate"]
      """  Field to default the Apply Date on AR Invoices.  """  
      self.ARDefShipDate:str = obj["ARDefShipDate"]
      """  Field to default the Shipment Date on AR Invoices.  """  
      self.ARDefTaxPDate:str = obj["ARDefTaxPDate"]
      """  Field to default the Tax Point Date on AR Invoices.  """  
      self.ARDefCurrDate:str = obj["ARDefCurrDate"]
      """  Field to default the Currency Date on AR Invoices.  """  
      self.ARDefTaxRateD:str = obj["ARDefTaxRateD"]
      """  Field to default the Tax Rate Date on AR Invoices.  """  
      self.ARLinkApplyDate:str = obj["ARLinkApplyDate"]
      """  Field to link the Apply Date on AR Invoices.  """  
      self.ARLinkShipDate:str = obj["ARLinkShipDate"]
      """  Field to link the Shipment Date on AR Invoices.  """  
      self.ARLinkTaxPDate:str = obj["ARLinkTaxPDate"]
      """  Field to link the Tax Point Date on AR Invoices.  """  
      self.ARLinkCurrDate:str = obj["ARLinkCurrDate"]
      """  Field to link the Currency Date Date on AR Invoices.  """  
      self.ARLinkTaxRateD:str = obj["ARLinkTaxRateD"]
      """  Field to link the Tax Rate Date on AR Invoices.  """  
      self.ARAmdApplyDate:bool = obj["ARAmdApplyDate"]
      """  Field to Allow Amend the Apply Date on AR Invoices.  """  
      self.ARAmdShipDate:bool = obj["ARAmdShipDate"]
      """  Field to Allow Amend the Shipment Date on AR Invoices.  """  
      self.ARAmdTaxPDate:bool = obj["ARAmdTaxPDate"]
      """  Field to Allow Amend the Tax Point Date on AR Invoices.  """  
      self.ARAmdCurreDate:bool = obj["ARAmdCurreDate"]
      """  Field to Allow Amend the Currency Date on AR Invoices.  """  
      self.ARAmdTaxRateD:bool = obj["ARAmdTaxRateD"]
      """  Field to Allow Amend the Tax Rate Date on AR Invoices.  """  
      self.DatesSetUp:bool = obj["DatesSetUp"]
      """  Field to enable funcionality of Dates Set Up  """  
      self.ARDefTaxRCrD:str = obj["ARDefTaxRCrD"]
      """  Field to default the Tax Rate Date for cancellation or adjusment credit on AR Invoices.  """  
      self.ARAmdTaxRCrD:bool = obj["ARAmdTaxRCrD"]
      """  Field to Allow Amend the Tax Rate Date for cancellation or adjusment credit on AR Invoices.  """  
      self.UseAltBillToAddr:bool = obj["UseAltBillToAddr"]
      """  This field will hold the default value for InvcHead.UseAltBillTo which indicates if the Alternate Bill To address should be used for taxing instead of the ship to address.  """  
      self.CopyExchangeRate:bool = obj["CopyExchangeRate"]
      """  Flag to indicate if the Exchange Rate should be copied from the original Invoice for a Correction Invoice.  """  
      self.GLStage:str = obj["GLStage"]
      """  Indicates first PI stage that updates the G/L  """  
      self.EndorseAP:bool = obj["EndorseAP"]
      """  Endorse AP  """  
      self.GLStatus:bool = obj["GLStatus"]
      """  GL Status  """  
      self.UnapprovedStatus:str = obj["UnapprovedStatus"]
      """  Unapproved Status  """  
      self.PortfolioStatus:str = obj["PortfolioStatus"]
      """  Portfolio Status  """  
      self.BankStatus:str = obj["BankStatus"]
      """  Bank Status  """  
      self.SettledStatus:str = obj["SettledStatus"]
      """  Settled Status  """  
      self.NextPINum:int = obj["NextPINum"]
      """  Next available number in PI numbering sequence  """  
      self.NumDigit:int = obj["NumDigit"]
      """  Number of digits allowed for PI Numbering  """  
      self.PreferredBank:str = obj["PreferredBank"]
      """  Cash Receipts from sale preferred bank.  """  
      self.IsDiscountforCreditM:bool = obj["IsDiscountforCreditM"]
      """  IsDiscountforCreditM  """  
      self.MandateCounter:int = obj["MandateCounter"]
      """  MandateCounter  """  
      self.SEPADDMsgCounter:int = obj["SEPADDMsgCounter"]
      """  SEPADDMsgCounter  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllowConfirmationTax:bool = obj["AllowConfirmationTax"]
      """  Indicates that for AR Invoices the confirmation taxes can be used.  """  
      self.UseAltBillToID:bool = obj["UseAltBillToID"]
      """  UseAltBillToID  """  
      self.CopyExcRateCancelInv:bool = obj["CopyExcRateCancelInv"]
      """  CopyExcRateCancelInv  """  
      self.CopyExcRateCM:bool = obj["CopyExcRateCM"]
      """  CopyExcRateCM  """  
      self.ExchangeDate:int = obj["ExchangeDate"]
      """  ExchangeDate  """  
      self.AllowOverpaidInv:bool = obj["AllowOverpaidInv"]
      """  AllowOverpaidInv  """  
      self.AutoARBal:bool = obj["AutoARBal"]
      """  AutoARBal  """  
      self.CancelledStatus:str = obj["CancelledStatus"]
      """  CancelledStatus  """  
      self.AdjDocLevTax:bool = obj["AdjDocLevTax"]
      """  AdjDocLevTax  """  
      self.RetainCreditOverride:bool = obj["RetainCreditOverride"]
      """  RetainCreditOverride  """  
      self.LNCashRecForUnappliedRec:bool = obj["LNCashRecForUnappliedRec"]
      """  LNCashRecForUnappliedRec  """  
      self.AllowNegativeDiscount:bool = obj["AllowNegativeDiscount"]
      """  AllowNegativeDiscount  """  
      self.AllowNegativeQuantity:bool = obj["AllowNegativeQuantity"]
      """  AllowNegativeQuantity  """  
      self.UseControlledCM:bool = obj["UseControlledCM"]
      """  UseControlledCM  """  
      self.UseCopyNumInARInv:bool = obj["UseCopyNumInARInv"]
      """  Use Copy Numbers in AR Invoice  """  
      self.CreditLimitInvoiceAction:str = obj["CreditLimitInvoiceAction"]
      """  Miscellaneous AR Invoice action to a Credit Held customer.  Valid values are "WARN" or "STOPENTRY", “STOPPOST”, “IGNORE”.  WARN means that the user is given a warning, but allowed to proceed (or cancel) with the invoice.  STOPENTRY means that the user is given a message that invoice cannot be created.  STOPPOST means the user is giving a message the invoice cannot be created, but it cannot be posted until the customer is removed from credit hold.  IGNORE means no message is received but the invoice will be marked as on credit hold.  """  
      self.MaxWriteOffAmt:int = obj["MaxWriteOffAmt"]
      """  Maximum Write Off Amount  """  
      self.AllowNegativeWriteOff:bool = obj["AllowNegativeWriteOff"]
      """  Allow Negative Write Off  """  
      self.DepTaxTreatment:str = obj["DepTaxTreatment"]
      """  Invoice Deposit Tax Treatment  """  
      self.DepAllowNegativeTax:bool = obj["DepAllowNegativeTax"]
      """  Can be set = yes, if Deposit Invoice Tax treatment is Tax Shipment Net movement. Allow shipment invoice with negative net tax elements  """  
      self.DepTaxCatID:str = obj["DepTaxCatID"]
      """  Product Tax Category  """  
      self.DepInvcRequired:bool = obj["DepInvcRequired"]
      """  Require Deposit Invoice  """  
      self.DepDaysDelay:int = obj["DepDaysDelay"]
      """  Invoice Days Delay  """  
      self.DepTranDocTypeID:str = obj["DepTranDocTypeID"]
      """  Deposit transaction Document Type of type AR Invoice  """  
      self.DepShowLinkedInvc:bool = obj["DepShowLinkedInvc"]
      """  Deposit Invoices show prior linked Deposit Invoices  """  
      self.MandatoryARRemittanceSlip:bool = obj["MandatoryARRemittanceSlip"]
      """  MandatoryARRemittanceSlip  """  
      self.EndorsedToSupplierStatus:str = obj["EndorsedToSupplierStatus"]
      """  Endorsed to Supplier PI Status  """  
      self.AllowNegBal:bool = obj["AllowNegBal"]
      """  AllowNegBal  """  
      self.CColCompany:str = obj["CColCompany"]
      """  Company that is the Parent of Centralized Collection process.  This field designates which company is the Central Collection Parent Company and can therefore receive and pay the invoices flagged for centralized collection.  """  
      self.CentralCollectionForAutoInv:bool = obj["CentralCollectionForAutoInv"]
      """  Flag to indicate if Invoices created automatically will be marked for Central Collection.  """  
      self.UseBillToTaxIDInSL:bool = obj["UseBillToTaxIDInSL"]
      """  Use Bill To Tax ID in Sales List  """  
      self.SplitRevenueByTaxEffRate:bool = obj["SplitRevenueByTaxEffRate"]
      """  Split Revenue based on combination of Product Group and Tax Effective Rate GLC  """  
      self.EnableSettlementFeature:bool = obj["EnableSettlementFeature"]
      """  EnableSettlementFeature  """  
      self.ARClearingAcctDesc:str = obj["ARClearingAcctDesc"]
      self.ARClearingDept:str = obj["ARClearingDept"]
      """  XASyst.ARClearingDept  """  
      self.ARClearingDisplayAccount:str = obj["ARClearingDisplayAccount"]
      self.ARClearingDiv:str = obj["ARClearingDiv"]
      """  XASyst.ARClearingDiv  """  
      self.ARTaxRptDate:int = obj["ARTaxRptDate"]
      """  Indicates which date is used for TaxTran Transaction Date - AR Invoices related records  """  
      self.ARVoucherInvoices:bool = obj["ARVoucherInvoices"]
      """  If yes, enable IntPay acount (from GLSyst)  """  
      self.DEPTaxCatIDDescription:str = obj["DEPTaxCatIDDescription"]
      self.DepTranDocTypeLinkDescription:str = obj["DepTranDocTypeLinkDescription"]
      self.isRlsCreditEmpty:bool = obj["isRlsCreditEmpty"]
      self.isRlsPayEmpty:bool = obj["isRlsPayEmpty"]
      self.isRlsReportEmpty:bool = obj["isRlsReportEmpty"]
      self.ARClearingChart:str = obj["ARClearingChart"]
      """  XASyst.ARClearingChart  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AgingRptFmtDescription:str = obj["AgingRptFmtDescription"]
      self.AJJournalCodeJrnlDescription:str = obj["AJJournalCodeJrnlDescription"]
      self.PIStatusBStatusDesc:str = obj["PIStatusBStatusDesc"]
      self.PIStatusCStatusDesc:str = obj["PIStatusCStatusDesc"]
      self.PIStatusEToSStatusDesc:str = obj["PIStatusEToSStatusDesc"]
      self.PIStatusPStatusDesc:str = obj["PIStatusPStatusDesc"]
      self.PIStatusSStatusDesc:str = obj["PIStatusSStatusDesc"]
      self.PIStatusUStatusDesc:str = obj["PIStatusUStatusDesc"]
      self.PreferredBankDescription:str = obj["PreferredBankDescription"]
      self.PreferredBankBankName:str = obj["PreferredBankBankName"]
      self.SJJournalCodeJrnlDescription:str = obj["SJJournalCodeJrnlDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BMSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.UnapproveRevOnCheckout:bool = obj["UnapproveRevOnCheckout"]
      """  Unapprove part revisions when checked out to ECO.  """  
      self.VerifyPassword:bool = obj["VerifyPassword"]
      """  Indicates if the user's password will be verified during operations such as Rev approve/unapprove, checkout, checkin.  """  
      self.WorkflowRequired:bool = obj["WorkflowRequired"]
      """  If TRUE then a workflow group and task set is required on ECO Group records.  """  
      self.SingleUser:bool = obj["SingleUser"]
      """  If TRUE then the Engineering Workbench is limited to one user per ECO Group.  If FALSE then individual revisions within a group can be locked.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BorderPctRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DestCountryNum:int = obj["DestCountryNum"]
      """  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  """  
      self.PctAtBorder:int = obj["PctAtBorder"]
      """  This is used to calculate the percentage of the miscellaneous charge to be applied in the Intrastat.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DestCountryNumDescription:str = obj["DestCountryNumDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CRSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DefTaskSetID:str = obj["DefTaskSetID"]
      """  Company default Task set.  Used to assign to new lead/opportunity/quote when there isn't a task set for the Sales Territory for the Quote.  """  
      self.DefMktgCampaignID:str = obj["DefMktgCampaignID"]
      """  Company default Marketing Campaign.  Used to assign to a new lead/opportunity/quote.  """  
      self.DefWebMktgCampaignID:str = obj["DefWebMktgCampaignID"]
      """  Company default Web Marketing Campaign.  Used to assign to a new lead/opportunity/quote.  """  
      self.WinReasonCode:str = obj["WinReasonCode"]
      """  Default "win" reason Code.  From Reason table with Code type of "w"  """  
      self.LossReasonCode:str = obj["LossReasonCode"]
      """  Default "Loss" reason Code.  From Reason table with Code type of "L"  """  
      self.TaskReasonCode:str = obj["TaskReasonCode"]
      """  Default "Task Completion" reason Code.  From Reason table with Code type of "T"  """  
      self.CloseTasksWin:bool = obj["CloseTasksWin"]
      """  Indicates that the win Function will close all open tasks on the LOQ  """  
      self.CloseTasksLose:bool = obj["CloseTasksLose"]
      """  Indicates that the Lose Function will close all open tasks on the LOQ  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Company default Sales territory  """  
      self.DefICMktgCampaignID:str = obj["DefICMktgCampaignID"]
      """  Company default Inter-Company Marketing Campaign.  Used to assign to a new lead/opportunity/quote.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UseTerritorySecurity:bool = obj["UseTerritorySecurity"]
      """  This flag indicates if the territory security is applied to sales order. By applying territory security at SO the user only can load sales orders and customers for the territory that his workforce has access.  """  
      self.CRMCallsShown:int = obj["CRMCallsShown"]
      """  Number  of calls assigned to the owner that are loaded automatically when opening CRM Call log.  """  
      self.ExternalCRMIntegration:bool = obj["ExternalCRMIntegration"]
      """  This fields defines if the Epicor ERP CRM is integrated to an External CRM.  Only enabled if there is an active license for External CRM Integration.  """  
      self.ExternalCRMSystem:str = obj["ExternalCRMSystem"]
      """  This fields define the external software used as the Extenral CRM. The valid option are  S: Salesfore.com .  """  
      self.ExternalCRMURL:str = obj["ExternalCRMURL"]
      """  This is the URL used to integrate to the External CRM system  """  
      self.ExternalCRMMasterFile:str = obj["ExternalCRMMasterFile"]
      """  This field determines what system is used as the primary master file holder. The valid values are E : Epicor ERP  C: External CRM  """  
      self.ExternalToken:str = obj["ExternalToken"]
      """  This field defines the token used to integrate to the External CRM  """  
      self.ExternalCRMLoginID:str = obj["ExternalCRMLoginID"]
      """  This field defines the user id used to integrate to the External CRM  """  
      self.ExternalCRMPassword:str = obj["ExternalCRMPassword"]
      """  This field defines the token password to integrate to the External CRM  """  
      self.ExternalCRMTimeZoneID:str = obj["ExternalCRMTimeZoneID"]
      """  This field defines the time zone used by the External CRM. This is used in cases where the External CRM is located in a different time zone than Epicor ERP.  """  
      self.ExternalCRMDefaultICTypeID:str = obj["ExternalCRMDefaultICTypeID"]
      """  This field defines the default Industry Class Type used by the External CRM. The valid values are all the active Industry Class Type Id defined in Epicor ERP.  """  
      self.ExternalCRMLastSync:str = obj["ExternalCRMLastSync"]
      """  This field defines the last time that the External CRM has been Synchronized to Epicor ERP. This field is maintained by the External CRM Synchronization  process.  """  
      self.ExternalCRMLastSyncContact:str = obj["ExternalCRMLastSyncContact"]
      """  This field defines the last time that Customer Contacts  has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  """  
      self.ExternalCRMLastSyncCustomer:str = obj["ExternalCRMLastSyncCustomer"]
      """  This field defines the last time that the Customers  has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  """  
      self.ExternalCRMLastSyncPart:str = obj["ExternalCRMLastSyncPart"]
      """  This field defines the last time that  Part  has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  """  
      self.ExternalCRMLastSyncQuote:str = obj["ExternalCRMLastSyncQuote"]
      """  This field defines the last time that  Quotes  has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  """  
      self.ExternalCRMCreateSO:int = obj["ExternalCRMCreateSO"]
      """  This field is used by the External CRM integration only.  """  
      self.ExternalCRMPasswordMasked:str = obj["ExternalCRMPasswordMasked"]
      """  External CRM masked password.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DefICMktgCampDescription:str = obj["DefICMktgCampDescription"]
      self.DefMktgCampaignIDCampDescription:str = obj["DefMktgCampaignIDCampDescription"]
      self.DefTaskSetIDWorkflowType:str = obj["DefTaskSetIDWorkflowType"]
      self.DefTaskSetIDTaskSetDescription:str = obj["DefTaskSetIDTaskSetDescription"]
      self.DefWebMtkgCampDescription:str = obj["DefWebMtkgCampDescription"]
      self.ExternalCRMDefaultICTypeDescription:str = obj["ExternalCRMDefaultICTypeDescription"]
      self.LossReasonDescription:str = obj["LossReasonDescription"]
      self.TaskReasonDescription:str = obj["TaskReasonDescription"]
      self.TerritoryIDTerritoryDesc:str = obj["TerritoryIDTerritoryDesc"]
      self.WinReasonDescription:str = obj["WinReasonDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CSFSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxInfo1:str = obj["TaxInfo1"]
      self.TaxInfo2:str = obj["TaxInfo2"]
      self.TaxInfo3:str = obj["TaxInfo3"]
      self.TaxInfo4:str = obj["TaxInfo4"]
      self.TaxInfo5:str = obj["TaxInfo5"]
      self.TaxInfo6:str = obj["TaxInfo6"]
      self.TaxInfo7:str = obj["TaxInfo7"]
      self.TaxInfo8:str = obj["TaxInfo8"]
      self.TaxInfo9:str = obj["TaxInfo9"]
      self.TaxInfo10:str = obj["TaxInfo10"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RedStornoOpt:str = obj["RedStornoOpt"]
      """  RedStornoOpt  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CompanyAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
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

class Erp_Tablesets_CompanyListTableset:
   def __init__(self, obj):
      self.CompanyList:list[Erp_Tablesets_CompanyListRow] = obj["CompanyList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

class Erp_Tablesets_CompanyTableset:
   def __init__(self, obj):
      self.Company:list[Erp_Tablesets_CompanyRow] = obj["Company"]
      self.CompanyAttch:list[Erp_Tablesets_CompanyAttchRow] = obj["CompanyAttch"]
      self.AGCompany:list[Erp_Tablesets_AGCompanyRow] = obj["AGCompany"]
      self.APSyst:list[Erp_Tablesets_APSystRow] = obj["APSyst"]
      self.ARSyst:list[Erp_Tablesets_ARSystRow] = obj["ARSyst"]
      self.BMSyst:list[Erp_Tablesets_BMSystRow] = obj["BMSyst"]
      self.BorderPct:list[Erp_Tablesets_BorderPctRow] = obj["BorderPct"]
      self.CRSyst:list[Erp_Tablesets_CRSystRow] = obj["CRSyst"]
      self.CSFSyst:list[Erp_Tablesets_CSFSystRow] = obj["CSFSyst"]
      self.Currency:list[Erp_Tablesets_CurrencyRow] = obj["Currency"]
      self.CurrRateGrp:list[Erp_Tablesets_CurrRateGrpRow] = obj["CurrRateGrp"]
      self.EQSyst:list[Erp_Tablesets_EQSystRow] = obj["EQSyst"]
      self.ExtPRSyst:list[Erp_Tablesets_ExtPRSystRow] = obj["ExtPRSyst"]
      self.FsSyst:list[Erp_Tablesets_FsSystRow] = obj["FsSyst"]
      self.GLSyst:list[Erp_Tablesets_GLSystRow] = obj["GLSyst"]
      self.ISSyst:list[Erp_Tablesets_ISSystRow] = obj["ISSyst"]
      self.JCSyst:list[Erp_Tablesets_JCSystRow] = obj["JCSyst"]
      self.MMSyst:list[Erp_Tablesets_MMSystRow] = obj["MMSyst"]
      self.PDMSyst:list[Erp_Tablesets_PDMSystRow] = obj["PDMSyst"]
      self.PECompWhldHist:list[Erp_Tablesets_PECompWhldHistRow] = obj["PECompWhldHist"]
      self.PRSyst:list[Erp_Tablesets_PRSystRow] = obj["PRSyst"]
      self.TaxSvcConfig:list[Erp_Tablesets_TaxSvcConfigRow] = obj["TaxSvcConfig"]
      self.XaSyst:list[Erp_Tablesets_XaSystRow] = obj["XaSyst"]
      self.XbSyst:list[Erp_Tablesets_XbSystRow] = obj["XbSyst"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CurrRateGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines if the record is inactive  """  
      self.BaseRateGrpCode:str = obj["BaseRateGrpCode"]
      """  Determins if there is a base rate group to use if no rules or rates are defined for a currency  """  
      self.CrossCurrCode:str = obj["CrossCurrCode"]
      """  Currency to use during single or double currency conversions  """  
      self.CrossRound:bool = obj["CrossRound"]
      """  Determine if rounding should be done after conversion  """  
      self.CrossRoundDec:int = obj["CrossRoundDec"]
      """  Number of decimals to use during rounding  """  
      self.AltCrossCurrCode:str = obj["AltCrossCurrCode"]
      """  Currency used for double currency conversions  """  
      self.AltCrossRound:bool = obj["AltCrossRound"]
      """  Determine if rounding should be done after conversion  """  
      self.AltCrossRoundDec:int = obj["AltCrossRoundDec"]
      """  Number of decimals to use during rounding  """  
      self.GlobalGrp:bool = obj["GlobalGrp"]
      """  Determines whether or not this rate group is shared between more than one company.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this record will receive global updates.  """  
      self.RateNumDec:int = obj["RateNumDec"]
      """  Number of decimals for the exchange rates  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableGlobalGrp:bool = obj["EnableGlobalGrp"]
      """  control when the GlobalGrp field should be enabled.  """  
      self.EnableGlobalLock:bool = obj["EnableGlobalLock"]
      """  Control when the GlobalLock field should be enabled.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency is Global (master or linked)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany and GlbRateGrpCode that is linking to this Rate Group.  """  
      self.GlbCompanyName:str = obj["GlbCompanyName"]
      """  Company Name from linked global rate group.  """  
      self.GlbRateGrpCode:str = obj["GlbRateGrpCode"]
      """  Rate group Code from linked global rate group.  """  
      self.GlbRateGrpDesc:str = obj["GlbRateGrpDesc"]
      """  Description from linked global rate group.  """  
      self.GlbCompanyID:str = obj["GlbCompanyID"]
      """  Company ID from linked global rate group.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AltCrossCurrCurrName:str = obj["AltCrossCurrCurrName"]
      self.AltCrossCurrCurrDesc:str = obj["AltCrossCurrCurrDesc"]
      self.AltCrossCurrCurrencyID:str = obj["AltCrossCurrCurrencyID"]
      self.AltCrossCurrDocumentDesc:str = obj["AltCrossCurrDocumentDesc"]
      self.AltCrossCurrCurrSymbol:str = obj["AltCrossCurrCurrSymbol"]
      self.BaseRateGrpDescDescription:str = obj["BaseRateGrpDescDescription"]
      self.CrossCurrCurrDesc:str = obj["CrossCurrCurrDesc"]
      self.CrossCurrCurrName:str = obj["CrossCurrCurrName"]
      self.CrossCurrCurrencyID:str = obj["CrossCurrCurrencyID"]
      self.CrossCurrDocumentDesc:str = obj["CrossCurrDocumentDesc"]
      self.CrossCurrCurrSymbol:str = obj["CrossCurrCurrSymbol"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CurrencyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.CurrDesc:str = obj["CurrDesc"]
      """  Description of the currency  """  
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.DocumentDesc:str = obj["DocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.Note:str = obj["Note"]
      """  Notes the about the Currency.  """  
      self.CurrName:str = obj["CurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyID:str = obj["CurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.DecimalsGeneral:int = obj["DecimalsGeneral"]
      """  Number of decimals used for any types of amounts where they entered, printed, displayed, except unit price and unit cost, according to the table zFieldDecimal where ValueType = "G"  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the currency is active  """  
      self.DecimalsPrice:int = obj["DecimalsPrice"]
      """  Number of decimals used for any unit prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "P"  """  
      self.MaintRate:bool = obj["MaintRate"]
      """  Can only maintain exchange rates for currencies with this flag checked  """  
      self.DecimalsCost:int = obj["DecimalsCost"]
      """  Number of decimals used for any cost prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "C"  """  
      self.BaseCurr:bool = obj["BaseCurr"]
      """  Indicates if this is the base currency.  Only one base currency is allowed  """  
      self.RoundMltpUnitPrice:int = obj["RoundMltpUnitPrice"]
      """  Define multiple that Unit Prices for sales related documents shall be rounded to, 0- no rounding.  """  
      self.ReportCurr:bool = obj["ReportCurr"]
      """  Indicates if this is a reporting currency  """  
      self.RoundMltpUnitTax:int = obj["RoundMltpUnitTax"]
      """  Define multiple that Unit Tax for sales related documents shall be rounded to, 0- no rounding.  """  
      self.RoundMltpExtPrice:int = obj["RoundMltpExtPrice"]
      """  Define multiple that Extended Prices (total line amount) for sales related documents shall be rounded to, 0- no rounding.  """  
      self.RoundMltpExtTax:int = obj["RoundMltpExtTax"]
      """  Define multiple that Extended Tax (total line tax) for sales related documents shall be rounded to, 0- no rounding.  """  
      self.RoundMltpTotalAmt:int = obj["RoundMltpTotalAmt"]
      """  Define multiple that Total amount for sales related documents shall be rounded to, 0- no rounding.  """  
      self.GlobalCurr:bool = obj["GlobalCurr"]
      """  Determines whether or not this currency is shared between more than one company.  """  
      self.RoundMltpTotalTax:int = obj["RoundMltpTotalTax"]
      """  Define multiple that Total Tax amount for sales related documents shall be rounded to, 0- no rounding.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this currency record will receive global updates.  """  
      self.RoundRuleUnitPrice:int = obj["RoundRuleUnitPrice"]
      """  Define the rule how Unit Price for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.ScaleFactor:int = obj["ScaleFactor"]
      """  Display factor for exchange rates  """  
      self.RoundRuleUnitTax:int = obj["RoundRuleUnitTax"]
      """  Define the rule how Unit Tax for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  """  
      self.RoundRuleExtPrice:int = obj["RoundRuleExtPrice"]
      """  Define the rule how Extended Prices (total line amount) for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.ReportCurrPos:int = obj["ReportCurrPos"]
      """  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  """  
      self.RoundRuleExtTax:int = obj["RoundRuleExtTax"]
      """  Define the rule how Extended Tax (total tax amount) for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.RoundRuleTotalAmt:int = obj["RoundRuleTotalAmt"]
      """  Define the rule how total amount for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.RoundRuleTotalTax:int = obj["RoundRuleTotalTax"]
      """  Define the rule how total tax amount for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.RoundTolerance:int = obj["RoundTolerance"]
      """  It used in AP Invoice, if the rounding amount remaining is less or equal to the tolerance, the remaining amount is automatically booked.  """  
      self.ISONumber:int = obj["ISONumber"]
      """  ISO unique identifier  """  
      self.StoreID:str = obj["StoreID"]
      """  Store ID for Credit Card Processing  """  
      self.RoundMltpAnnualCharge:int = obj["RoundMltpAnnualCharge"]
      """  Define multiple that Annual Depreciation Charge for asset related documents shall be rounded to, 0- no rounding.  """  
      self.RoundMltpPeriodCharge:int = obj["RoundMltpPeriodCharge"]
      """  Define multiple that Period Depreciation Charge for asset  related documents shall be rounded to, 0- no rounding.  """  
      self.RoundRuleAnnualCharge:int = obj["RoundRuleAnnualCharge"]
      """  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.RoundRulePeriodCharge:int = obj["RoundRulePeriodCharge"]
      """  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGAFIPCode:str = obj["AGAFIPCode"]
      """  AGAFIPCode  """  
      self.ISOCurrCode:str = obj["ISOCurrCode"]
      """  This Currency Code is used for CRE Processors.  """  
      self.ProcessorNum:int = obj["ProcessorNum"]
      """  ProcessorNum  """  
      self.BookCurr:bool = obj["BookCurr"]
      self.CompanyBase:bool = obj["CompanyBase"]
      self.CountryName:str = obj["CountryName"]
      """  Name of Country.  """  
      self.EnableBaseCurr:bool = obj["EnableBaseCurr"]
      """  Control when the Base Currency should be enable.  """  
      self.EnableDecimals:bool = obj["EnableDecimals"]
      """  If currency exist in any transaction the decimals fields should be disables.  """  
      self.EnableGlobalCurr:bool = obj["EnableGlobalCurr"]
      """  control when the Global Currency field should be enable.  """  
      self.EnableGlobalLock:bool = obj["EnableGlobalLock"]
      """  Control when the GlobalLock field should be enable.  """  
      self.EnableInactive:bool = obj["EnableInactive"]
      """  Control when the Inactive field should be enable.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  GlbCompany that is linked to this currency  """  
      self.GlbCompanyName:str = obj["GlbCompanyName"]
      """  GlbCompany Name that is linked to this currency  """  
      self.GlbCurrDesc:str = obj["GlbCurrDesc"]
      """  GlbCurrency Description that is linked to this currency  """  
      self.GlbCurrencyCode:str = obj["GlbCurrencyCode"]
      """  GlbCurrency Code that is linked to this currency  """  
      self.GlbCurrencyID:str = obj["GlbCurrencyID"]
      """  GlbCurrency ID that is linked to this currency  """  
      self.GlbCurrSymbol:str = obj["GlbCurrSymbol"]
      """  GlbCurrency Symbol that is linked to this currency  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency is Global (master or linked)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany and GlbCurrencyCode that is linking to this currency  """  
      self.HasCCInterface:bool = obj["HasCCInterface"]
      self.BaseRowRowID:str = obj["BaseRowRowID"]
      """  This field store the RowID of the record that is marked as Base Currency.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CountryDescription:str = obj["CountryDescription"]
      self.CreditCardProcessorDesc:str = obj["CreditCardProcessorDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EQSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.StartQuoteNum:int = obj["StartQuoteNum"]
      """  Used to establish the beginning Sales Order #. When the system generates a new order it will assign the greater of (StartOrderNum) or (the last orders # on file + 1) as the order number.  """  
      self.FollowUpDays:int = obj["FollowUpDays"]
      """  A integer that express the # of days from the date quoted that someone should follow up with the customer concerning the quote. This is used by quote entry to calculate a default follow up date (QuoteHed.FollowUpDate). Default follow up date is QuoteHed.DateQuoted + EQSyst.FollowUpDays  """  
      self.ExpirationDays:int = obj["ExpirationDays"]
      """  An integer that express the # of days from the quoted date when quotes will expire. This is used by quote entry to calculate the QuoteHed.ExpirationDate  """  
      self.QuoteDueDays:int = obj["QuoteDueDays"]
      """  An integer that defines the # of days in which the quoting process needs to be completed in. Quote entry uses this in calculating the QuoteHed.DueDate.  """  
      self.CheckOff1Label:str = obj["CheckOff1Label"]
      """  Label used for the QuoteHed.CheckOff1 field.  There are 5 CheckOffLabel fields. They are all optional. If entered then the corresponding QuoteHed.CheckOff fields become active.  """  
      self.CheckOff2Label:str = obj["CheckOff2Label"]
      """  Label used for the QuoteHed.CheckOff2 field.  """  
      self.CheckOff3Label:str = obj["CheckOff3Label"]
      """  Label used for the QuoteHed.CheckOff3 field.  """  
      self.CheckOff4Label:str = obj["CheckOff4Label"]
      """  Label used for theQuoteHed.CheckOff4 field.  """  
      self.CheckOff5Label:str = obj["CheckOff5Label"]
      """  Label used for the QuoteHed.CheckOff5 field.  """  
      self.MarkUpID:str = obj["MarkUpID"]
      """  The ID that establishes link to the default QMarkUp record which was indicated as the System Wide default. Provides default markup percents used by quote entry when none are associated to the specific customer. This ID is not directly entered. Instead it is updated by the user checking a toggle box during QMarkUp maintenance indicating "System Default". This may be left blank, which indicates there are no defaults.  """  
      self.Message1:str = obj["Message1"]
      """  Footer message for bottom of quote form  """  
      self.Message2:str = obj["Message2"]
      """  Footer message for bottom of quote form  """  
      self.PreventQQChange:bool = obj["PreventQQChange"]
      """  If set to Yes, the user must change the Quote "Quoted"  flag to No before they are allowed to make any changes.  """  
      self.LogChanges:bool = obj["LogChanges"]
      """  If this is Yes, then when Quotes are set to "Quoted"  or any header flag is changed on a "Planned" job the user will be prompted to enter a description of the changes.  This option is only available when "PreventQQChange" = Yes.  """  
      self.GenQuoteQtys:bool = obj["GenQuoteQtys"]
      """  System Option to generate all the quantities from the price breaks in quote detail entry.  """  
      self.QuoReadyToCalcDflt:bool = obj["QuoReadyToCalcDflt"]
      """  This flag will be used to default the QuoteHed.ReadyToCalc field when an invoice is created. Defaults to No  """  
      self.ReduceRelQty:bool = obj["ReduceRelQty"]
      """  Option to keep the Quote Detail quantity constant.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RefreshWorksheetOD:bool = obj["RefreshWorksheetOD"]
      """  Refresh Worksheet on Demand . If this flag is check the Quote Worksheet will automatically refresh and it will only refresh if the user manually select the action in Quote Entry.  """  
      self.GetCostsFromInventory:bool = obj["GetCostsFromInventory"]
      """  GetCostsFromInventory  """  
      self.DfltExpectedQtyTo:str = obj["DfltExpectedQtyTo"]
      """  DfltExpectedQtyTo  """  
      self.DfltOrderQtyToExpQty:bool = obj["DfltOrderQtyToExpQty"]
      """  DfltOrderQtyToExpQty  """  
      self.SellingExpectedQty:int = obj["SellingExpectedQty"]
      """  SellingExpectedQty  """  
      self.UseQuoteBOM:bool = obj["UseQuoteBOM"]
      """  Quotes can be used as souce BOM if true  """  
      self.DeferQtyUpd:bool = obj["DeferQtyUpd"]
      """   If true, the system will defer update of Required Qty when the QuoteAsm QtyPer field is updated 
*** FUTURE USE  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ETCAddrValidationTableset:
   def __init__(self, obj):
      self.ETCAddress:list[Erp_Tablesets_ETCAddressRow] = obj["ETCAddress"]
      self.ETCMessage:list[Erp_Tablesets_ETCMessageRow] = obj["ETCMessage"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ETCAddressRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.City:str = obj["City"]
      """  City name  """  
      self.Country:str = obj["Country"]
      """  Country name  """  
      self.Line1:str = obj["Line1"]
      """  Address line 1  """  
      self.Line2:str = obj["Line2"]
      """  Address line 2  """  
      self.Line3:str = obj["Line3"]
      """  Address line 3  """  
      self.PostalCode:str = obj["PostalCode"]
      """  Postal or ZIP code  """  
      self.Region:str = obj["Region"]
      """  State or province name  """  
      self.AddrSource:str = obj["AddrSource"]
      """  This is an additional field that will be required to designate the type of address that is being validated (customer, plant, etc)  """  
      self.AddrSourceID:str = obj["AddrSourceID"]
      """  This is an additional field to contain an appropriate piece of data to be used with the AddrSource for display in the UI to clarify for the user what data the validated address relates to. Such as AddrSource = Customer and AddrSourceID = ?Addison?  """  
      self.UpdateAddr:bool = obj["UpdateAddr"]
      """  This is an additional field that will be set if the user has indicated that the Vantage address should be updated from the address validation results.  """  
      self.TransactionID:str = obj["TransactionID"]
      """  This value will come from Avalara ValidateResult TransactionID and identifies a unique specific request/response set. It will be used to tie the ETCValidAddress and ETCMessage rows to ETCAddress.  """  
      self.UpdateAllowed:bool = obj["UpdateAllowed"]
      """  This field will be set if by the process calling address validation to indicate whether the user should have the option to update the original address within the address validation UI.  """  
      self.RequestID:str = obj["RequestID"]
      """  Programmatically assign unique key to tie the ETCAddress table, the ETCValidAddress table and the ETCMessages table together.  """  
      self.AddressCode:str = obj["AddressCode"]
      """  Programmatically determined value used internally by the adapter. Defaults to the hash code of the Address object.  """  
      self.AddressType:str = obj["AddressType"]
      """  The type of address that was coded (PO Box, Rural Route, and so on), using the input address. This probably needs Code/desc data  Avalara will return F = Firm or company address; G = General Delivery address; H= High-rise or business complex; P = PO Box address; R = Rural route address; S = Street or residential address  """  
      self.CarrierRoute:str = obj["CarrierRoute"]
      """  The carrier route associated with the input address (USA). This probably needs Code/desc data  Avalara will return B = PO Box; C = City Delivery; G= General Delivery; H = Highway Contract; R = Rural route.  """  
      self.ValidCity:str = obj["ValidCity"]
      """  City name  """  
      self.ValidCountry:str = obj["ValidCountry"]
      """  Country name  """  
      self.County:str = obj["County"]
      """  County name  """  
      self.FipsCode:str = obj["FipsCode"]
      """  Federal Information Processing Standards Code (USA). This is a unique code representing each geographic combination of state, county, and city. The code is made up of the Federal Information Processing Code (FIPS) that uniquely identifies each state, county, and city in the U.S. See Federal Information Processing Standards (FIPS) Codes for more details. Digits 1-2 are the state code, digits 3-5 are the county code and digits 6-10 are the city code.  """  
      self.ValidLine1:str = obj["ValidLine1"]
      """  Line one of the valid address returned by the tax integration.  """  
      self.ValidLine2:str = obj["ValidLine2"]
      """  Line two of the valid address returned by the tax integration.  """  
      self.ValidLine3:str = obj["ValidLine3"]
      """  Line three of the valid address returned by the tax integration.  """  
      self.ValidLine4:str = obj["ValidLine4"]
      """  Line four of the valid address returned by the tax integration.  """  
      self.ValidPostalCode:str = obj["ValidPostalCode"]
      """  Postal code returned by the tax integration.  """  
      self.PostNet:str = obj["PostNet"]
      """  A 12-digit POSTNet barcode (USA). Digits 1-5 = ZIP code, digits 6-9 = Plus4 Code, digits 10-11 = delivery point, digit 12 = check digit  """  
      self.ValidRegion:str = obj["ValidRegion"]
      """  State or province name or abbreviation returned by the tax integration.  """  
      self.ResultCode:str = obj["ResultCode"]
      """  This needs Code/desc data.  Avalara will return a single code for each address validation request. We will include the result code in each ETCValidAddress row. Success = Operation Succeeded; Warning = Warnings occured, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  """  
      self.ResultSeq:int = obj["ResultSeq"]
      """  This is an additional field to set a unique sequence for each ValidMessage returned for a specific TransactionId.  """  
      self.CarrierRouteDesc:str = obj["CarrierRouteDesc"]
      """  Carrier Route description  """  
      self.AddressTypeDesc:str = obj["AddressTypeDesc"]
      """  Address type description  """  
      self.OTSCountry:str = obj["OTSCountry"]
      self.CountryNum:int = obj["CountryNum"]
      """  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.ACWPercentage:int = obj["ACWPercentage"]
      """   Auto consume window percentage: this is a percentage to calculate the auto consume window days  that scheduling engine will take in consideration to look for available quantity to consume.
The purpose of this is to look ahead for a few days that will save more time than building the goods, so unless we get the full qty “current date” we need to use the window to look for the remaining.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ETCMessageRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Details:str = obj["Details"]
      self.Helplink:str = obj["Helplink"]
      """  URL to help page for this message  """  
      self.Name:str = obj["Name"]
      """  Gets the name of the message  """  
      self.RefersTo:str = obj["RefersTo"]
      """  The item the message refers to, if applicable. Used to indicate a missing or incorrect value  """  
      self.Severity:str = obj["Severity"]
      """  This probably needs Code/desc data  Avalara will return Success = Operation Succeeded; Warning = Warnings occured, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  """  
      self.Source:str = obj["Source"]
      """  source of the message  """  
      self.Summary:str = obj["Summary"]
      """  concise summary of the message  """  
      self.TransactionID:str = obj["TransactionID"]
      """  This value will come from Avalara ValidateResult TransactionID and identifies a unique specific request/response set. It will be used to tie the ETCMessage row to ETCAddress.  """  
      self.AddrSource:str = obj["AddrSource"]
      """  This is an additional field that will be required to designate the type of address that is being validated (customer, plant, etc)  """  
      self.AddrSourceID:str = obj["AddrSourceID"]
      """  This is an additional field to contain an appropriate piece of data to be used with the AddrSource for display in the UI to clarify for the user what data the validated address relates to. Such as AddrSource = Customer and AddrSourceID = ?Addison?  """  
      self.RequestID:str = obj["RequestID"]
      """  Programitically assigned.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.GlobalEntityGLC:bool = obj["GlobalEntityGLC"]
      """  Marks this EntityGLC as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtPRSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company ID  """  
      self.FilePath:str = obj["FilePath"]
      """  Default File  """  
      self.ExtIntCompID:str = obj["ExtIntCompID"]
      """  3rd Party Payroll provider assigned company identifier  """  
      self.ConsHrs:bool = obj["ConsHrs"]
      """  Consolidates single entry per employee  """  
      self.TempD:bool = obj["TempD"]
      """  Indicates if an identifier is required in the export file  """  
      self.ZeroNul:bool = obj["ZeroNul"]
      """  Export Zero Hours as Blank  """  
      self.SupHead:bool = obj["SupHead"]
      """  Indicates that only child records will be sent to the export file  """  
      self.SemiMonthDay:int = obj["SemiMonthDay"]
      """  2nd Period Start Day  """  
      self.Delimiter:str = obj["Delimiter"]
      """  Indicates which normal character will separate each field  """  
      self.TotalAllHrs:bool = obj["TotalAllHrs"]
      """  Total hours for Base, OT and premium per line  """  
      self.GrpPayTypeID:bool = obj["GrpPayTypeID"]
      """  Group hours by pay type  """  
      self.PayExportLayoutID:str = obj["PayExportLayoutID"]
      """  Default Export Layout  """  
      self.DetailHours:bool = obj["DetailHours"]
      """  Detailed Labor Hours  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SplitExportLines:bool = obj["SplitExportLines"]
      """  When checked, separate lines are created for Base, Overtime and Other (Premium) hours in Export File  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FsSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.StartContractNum:int = obj["StartContractNum"]
      """  Used to establish the beginning Service Contract Number. When the system generates a new Contract it will assign the greater of (StartContractNum) or (the last Contract Num. on file + 1) as the Contract number.  """  
      self.StartServiceCallNum:int = obj["StartServiceCallNum"]
      """  Used to establish the beginning Service Call Number. When the system generates a new Service Call it will assign the greater of (StartServiceCallNum) or (the last Service Call Number on file + 1) as the Service Call number.  """  
      self.ExpireHorizon:int = obj["ExpireHorizon"]
      """  This is the window of days that is used to determine if a service contract is going to expire soon.  If the current date plus the expire horizon is greater than or equal to the entered expire date on a contract, the contract is considered to be expiring soon.  """  
      self.PrintPrice:bool = obj["PrintPrice"]
      """  This flag is used when printing service call tickets.  If "YES" then labor and material pricing will print on the ticket.  """  
      self.CallProdCode:str = obj["CallProdCode"]
      """  Product Group Code. This will be used as a default for service calls.  This can be blank or must be valid in the ProdGrup table.  """  
      self.CallJobPrefix:str = obj["CallJobPrefix"]
      """  This prefix will be used for service call job.  The service call job will be the prefix + service call number + service call Line number.  """  
      self.ContractStartup:bool = obj["ContractStartup"]
      """  This flag is to be set to 'YES' during intial startup. When this flag is set to 'YES' all Service Contracts will be created as active invoiced and shipped.  The idea is that a cusomter that purchases FS may already have active service contracts that have been invoiced.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RenewalPeriod:int = obj["RenewalPeriod"]
      """  This field stores the allowed Contract Renewal Period which is used to determine how long a contract/renewal can be renewed past its expiration date.  If the RenewalPeriod = 0 then it means that ALL expired contracts can still be renewed anytime.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CallProdDescription:str = obj["CallProdDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SalesCategory:str = obj["SalesCategory"]
      """  Maintained through Category Maintenance.  The sales category may be used in the Financial Statements to compare Income Statement accounts against.  """  
      self.ARInterfaced:bool = obj["ARInterfaced"]
      """  Indicates if the A/R module is interfaced with General Ledger.  When interfaced A/R posting routines will automatically create "posted" journal  entries in G/L.  """  
      self.APInterfaced:bool = obj["APInterfaced"]
      """  Indicates if the Accounts Payable module is interfaced with General Ledger.  When interfaced A/P posting routines will automatically create "posted" journal  entries in G/L.  """  
      self.PRInterfaced:bool = obj["PRInterfaced"]
      """  Indicates if the Payroll module is interfaced with General Ledger.  When interfaced, P/R posting routines will automatically create "posted" journal  entries in G/L.  """  
      self.PostInvtyWipCos:bool = obj["PostInvtyWipCos"]
      """  Configuration option which controls if the user has the option in the periodic Inventory/Wip/Cost of sales calculation process to post the results to general ledger.  If this is set to No then the user will not have the option to post to G/L.  """  
      self.GJJournalCode:str = obj["GJJournalCode"]
      """  The Journal Code of the Journal that will be used for Journal entry transactions. Manual Journal entries.  """  
      self.ARVoucherInvoices:bool = obj["ARVoucherInvoices"]
      """   Indicates if the user wants to use Vouchering for A/R Invoices.  Only available if the G/L module is installed.
If yes then the system will do the following
- Print a Voucher # on the invoice.
- When invoices are printed they will be automatically posted. .  The "Voucher number" is actually the Journal Number to which the invoice posted.  """  
      self.APVoucherInvoices:bool = obj["APVoucherInvoices"]
      """   Indicates if the user wants to use Vouchering for A/P Invoices.  Only available if the G/L module is installed.
If yes then the system will print a Voucher assignment log when A/P invoices are posted.  The "Voucher number" is actually the Journal Number to which the invoice posted.  """  
      self.AllowUnBalancedEntries:bool = obj["AllowUnBalancedEntries"]
      """  Allow unbalanced entries to be entered in General Journal Entry with a warning.  """  
      self.AllowManualGJEntries:bool = obj["AllowManualGJEntries"]
      """  Allow manual General Journal entries to be made for System Accounts.  """  
      self.ExtGL:bool = obj["ExtGL"]
      """  Flag to indicate that an External GL interface is being used  """  
      self.MasterCOA:str = obj["MasterCOA"]
      """  Identifies the Master COA for the company  """  
      self.BatchGLBalances:bool = obj["BatchGLBalances"]
      """   Indicates if GL balances are maintained real time or in batch. If Yes, the GLJrnDtl write trigger does NOT update the GLPeriodBal table.
If No, the GLJrnDtl write trigger updates the GLPeriod table.  The default value is no.  """  
      self.BatchGLDailyBal:bool = obj["BatchGLDailyBal"]
      """   If BatchGLBalances = yes the users have the ability to have the daily balances updated in batch mode.  This option is only available if BatchGLBalances equals Yes.
A Yes in this field indicates the GLJrnDtl write trigger does not update the GLDailyBal table.
If No, the GLJrnDtl write trigger updates the GLDailyBalTable.
The default value is No.  """  
      self.MatchUsingCurrentDate:bool = obj["MatchUsingCurrentDate"]
      """   This option determines which date gets stored in the GLJrnDtl.MatchDate field when GL transactions are matched.

If true, then the date that the transactions are matched is used.  If false, then the latest apply date of the matched transactions is used.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefaultBookMode:str = obj["DefaultBookMode"]
      """  It is used to store default Book Mode in GL Journal Entry.  """  
      self.GJJournalCodeOpen:str = obj["GJJournalCodeOpen"]
      """  The Journal Code of the Journal that will be used for Opening Journal entry transactions. Manual Journal entries.  """  
      self.GJJournalCodeClose:str = obj["GJJournalCodeClose"]
      """  The Journal Code of the Journal that will be used for Clousing Journal entry transactions. Manual Journal entries.  """  
      self.TaxEntryMode:str = obj["TaxEntryMode"]
      """  It is used to store tax entry mode for GL Journal header. Possible values: 0`No Taxes~1`Taxable Journal Lines~2`Taxable Journal Lines or Tax adjustment Journal.  """  
      self.DefaultTaxLiability:str = obj["DefaultTaxLiability"]
      """  It is used to store default value of tax liability for tax line in GL Journal entry routine.  """  
      self.DefaultTaxType:str = obj["DefaultTaxType"]
      """  It is used to store default value of tax type for tax line in GL Journal entry routine.  """  
      self.KeepRevisionHistory:bool = obj["KeepRevisionHistory"]
      """  If the flag is on then posting rules conversion program creates a copy of current active revision before merging with the revision provided in the update/upgrade.  """  
      self.FormatSelection:str = obj["FormatSelection"]
      self.DisplayGLFormat:str = obj["DisplayGLFormat"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.DefaultTaxLiabilityDescription:str = obj["DefaultTaxLiabilityDescription"]
      self.DefaultTaxTypeDescription:str = obj["DefaultTaxTypeDescription"]
      self.TaxLiabilityTaxCodes:str = obj["TaxLiabilityTaxCodes"]
      """  The list of tax codes for Default Tax Liability  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GJJournalJrnlDescription:str = obj["GJJournalJrnlDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ISSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EnableHarbour:bool = obj["EnableHarbour"]
      """  Enable Harbor Flag  """  
      self.PeriodFormat:str = obj["PeriodFormat"]
      """  Countries may differ in the way periods are reported.  """  
      self.DescType:str = obj["DescType"]
      """  Description Type  """  
      self.DefISRegion:str = obj["DefISRegion"]
      """  Intrastat Region  """  
      self.ISOrigCountryReq:bool = obj["ISOrigCountryReq"]
      """  Country of Origin required  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.APRGFlow2:str = obj["APRGFlow2"]
      """  APRGFlow2  """  
      self.APRGFlowSpec2:str = obj["APRGFlowSpec2"]
      """  APRGFlowSpec2  """  
      self.APRGTranType2:str = obj["APRGTranType2"]
      """  APRGTranType2  """  
      self.ARRGFlow2:str = obj["ARRGFlow2"]
      """  ARRGFlow2  """  
      self.ARRGFlowSpec2:str = obj["ARRGFlowSpec2"]
      """  ARRGFlowSpec2  """  
      self.ARRGTranType2:str = obj["ARRGTranType2"]
      """  ARRGTranType2  """  
      self.Generate2APRGLine:bool = obj["Generate2APRGLine"]
      """  Generate2APRGLine  """  
      self.Generate2ARRGLine:bool = obj["Generate2ARRGLine"]
      """  Generate2ARRGLine  """  
      self.Flow1Desc:str = obj["Flow1Desc"]
      """  Flow1Desc  """  
      self.Flow2Desc:str = obj["Flow2Desc"]
      """  Flow2Desc  """  
      self.StartIstatNum:int = obj["StartIstatNum"]
      """  StartIstatNum  """  
      self.APFlow:str = obj["APFlow"]
      """  APFlow  """  
      self.APFlowSpec:str = obj["APFlowSpec"]
      """  APFlowSpec  """  
      self.APTranType:str = obj["APTranType"]
      """  APTranType  """  
      self.APRGFlow:str = obj["APRGFlow"]
      """  APRGFlow  """  
      self.APRGFlowSpec:str = obj["APRGFlowSpec"]
      """  APRGFlowSpec  """  
      self.APRGTranType:str = obj["APRGTranType"]
      """  APRGTranType  """  
      self.ARFlow:str = obj["ARFlow"]
      """  ARFlow  """  
      self.ARFlowSpec:str = obj["ARFlowSpec"]
      """  ARFlowSpec  """  
      self.ARTranType:str = obj["ARTranType"]
      """  ARTranType  """  
      self.ARRGFlow:str = obj["ARRGFlow"]
      """  ARRGFlow  """  
      self.ARRGFlowSpec:str = obj["ARRGFlowSpec"]
      """  ARRGFlowSpec  """  
      self.ARRGTranType:str = obj["ARRGTranType"]
      """  ARRGTranType  """  
      self.ISCurrency:str = obj["ISCurrency"]
      """  ISCurrency  """  
      self.APExtraTradeCommodityFlow:str = obj["APExtraTradeCommodityFlow"]
      """  APExtraTradeCommodityFlow  """  
      self.APExtraTradeTranType:str = obj["APExtraTradeTranType"]
      """  APExtraTradeTranType  """  
      self.APExtraTradeCustomsProcedure:str = obj["APExtraTradeCustomsProcedure"]
      """  APExtraTradeCustomsProcedure  """  
      self.APExtraTradeISCustomsDeclCountry:str = obj["APExtraTradeISCustomsDeclCountry"]
      """  APExtraTradeISCustomsDeclCountry  """  
      self.APExtraTradeISEUBorderCrossingCountry:str = obj["APExtraTradeISEUBorderCrossingCountry"]
      """  APExtraTradeISEUBorderCrossingCountry  """  
      self.APRGExtraTradeCommodityFlow:str = obj["APRGExtraTradeCommodityFlow"]
      """  APRGExtraTradeCommodityFlow  """  
      self.APRGExtraTradeTranType:str = obj["APRGExtraTradeTranType"]
      """  APRGExtraTradeTranType  """  
      self.APRGExtraTradeCustomsProcedure:str = obj["APRGExtraTradeCustomsProcedure"]
      """  APRGExtraTradeCustomsProcedure  """  
      self.APRGExtraTradeISCustomsDeclCountry:str = obj["APRGExtraTradeISCustomsDeclCountry"]
      """  APRGExtraTradeISCustomsDeclCountry  """  
      self.APRGExtraTradeISEUBorderCrossingCountry:str = obj["APRGExtraTradeISEUBorderCrossingCountry"]
      """  APRGExtraTradeISEUBorderCrossingCountry  """  
      self.ARRGFlowSpec2Descr:str = obj["ARRGFlowSpec2Descr"]
      """  Shipping Returned 2  """  
      self.ARRGFlowSpecDescr:str = obj["ARRGFlowSpecDescr"]
      """  Shipping Returned  """  
      self.Generate2APRGExtraTradeLine:bool = obj["Generate2APRGExtraTradeLine"]
      """  Generate2APRGExtraTradeLine  """  
      self.ARRGTranType2Descr:str = obj["ARRGTranType2Descr"]
      """  Shipping Returned 2  """  
      self.APRGExtraTradeCommodityFlow2:str = obj["APRGExtraTradeCommodityFlow2"]
      """  APRGExtraTradeCommodityFlow2  """  
      self.APRGExtraTradeTranType2:str = obj["APRGExtraTradeTranType2"]
      """  APRGExtraTradeTranType2  """  
      self.ARRGTranTypeDescr:str = obj["ARRGTranTypeDescr"]
      """  Shipping Returned  """  
      self.ARTranTypeDescr:str = obj["ARTranTypeDescr"]
      """  Shipping Normal  """  
      self.APRGExtraTradeCustomsProcedure2:str = obj["APRGExtraTradeCustomsProcedure2"]
      """  APRGExtraTradeCustomsProcedure2  """  
      self.APRGExtraTradeISCustomsDeclCountry2:str = obj["APRGExtraTradeISCustomsDeclCountry2"]
      """  APRGExtraTradeISCustomsDeclCountry2  """  
      self.RegionDesc:str = obj["RegionDesc"]
      """  Intrastat Region Description  """  
      self.APRGExtraTradeISEUBorderCrossingCountry2:str = obj["APRGExtraTradeISEUBorderCrossingCountry2"]
      """  APRGExtraTradeISEUBorderCrossingCountry2  """  
      self.APFlowSpecDescr:str = obj["APFlowSpecDescr"]
      """  Receipt Normal  """  
      self.APRGFlowSpec2Descr:str = obj["APRGFlowSpec2Descr"]
      """  Receipt Returned 2  """  
      self.ARExtraTradeCommodityFlow:str = obj["ARExtraTradeCommodityFlow"]
      """  ARExtraTradeCommodityFlow  """  
      self.ARExtraTradeTranType:str = obj["ARExtraTradeTranType"]
      """  ARExtraTradeTranType  """  
      self.APRGFlowSpecDescr:str = obj["APRGFlowSpecDescr"]
      """  Receipt Returned  """  
      self.APRGTranType2Descr:str = obj["APRGTranType2Descr"]
      """  Receipt Returned 2  """  
      self.ARExtraTradeCustomsProcedure:str = obj["ARExtraTradeCustomsProcedure"]
      """  ARExtraTradeCustomsProcedure  """  
      self.ARExtraTradeISCustomsDeclCountry:str = obj["ARExtraTradeISCustomsDeclCountry"]
      """  ARExtraTradeISCustomsDeclCountry  """  
      self.APRGTranTypeDescr:str = obj["APRGTranTypeDescr"]
      """  Receipt Returned  """  
      self.ARExtraTradeISEUBorderCrossingCountry:str = obj["ARExtraTradeISEUBorderCrossingCountry"]
      """  ARExtraTradeISEUBorderCrossingCountry  """  
      self.APTranTypeDescr:str = obj["APTranTypeDescr"]
      """  Receipt Normal  """  
      self.ARFlowSpecDescr:str = obj["ARFlowSpecDescr"]
      """  Shipping Normal  """  
      self.ARRGExtraTradeCommodityFlow:str = obj["ARRGExtraTradeCommodityFlow"]
      """  ARRGExtraTradeCommodityFlow  """  
      self.ARRGExtraTradeTranType:str = obj["ARRGExtraTradeTranType"]
      """  ARRGExtraTradeTranType  """  
      self.FlowList:str = obj["FlowList"]
      """  Used to populate the Intrastat Flow combos  """  
      self.ARRGExtraTradeCustomsProcedure:str = obj["ARRGExtraTradeCustomsProcedure"]
      """  ARRGExtraTradeCustomsProcedure  """  
      self.ARRGExtraTradeISCustomsDeclCountry:str = obj["ARRGExtraTradeISCustomsDeclCountry"]
      """  ARRGExtraTradeISCustomsDeclCountry  """  
      self.ARRGExtraTradeISEUBorderCrossingCountry:str = obj["ARRGExtraTradeISEUBorderCrossingCountry"]
      """  ARRGExtraTradeISEUBorderCrossingCountry  """  
      self.Generate2ARRGExtraTradeLine:bool = obj["Generate2ARRGExtraTradeLine"]
      """  Generate2ARRGExtraTradeLine  """  
      self.ARRGExtraTradeCommodityFlow2:str = obj["ARRGExtraTradeCommodityFlow2"]
      """  ARRGExtraTradeCommodityFlow2  """  
      self.ARRGExtraTradeTranType2:str = obj["ARRGExtraTradeTranType2"]
      """  ARRGExtraTradeTranType2  """  
      self.ARRGExtraTradeCustomsProcedure2:str = obj["ARRGExtraTradeCustomsProcedure2"]
      """  ARRGExtraTradeCustomsProcedure2  """  
      self.ARRGExtraTradeISCustomsDeclCountry2:str = obj["ARRGExtraTradeISCustomsDeclCountry2"]
      """  ARRGExtraTradeISCustomsDeclCountry2  """  
      self.ARRGExtraTradeISEUBorderCrossingCountry2:str = obj["ARRGExtraTradeISEUBorderCrossingCountry2"]
      """  ARRGExtraTradeISEUBorderCrossingCountry2  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JCSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CheckOff1Label:str = obj["CheckOff1Label"]
      """  Label used for the JobHead.CheckOff1 field.  There are 5 CheckOffLabel fields.  They are all optional.  If entered then the corresponding JobHead.CheckOff fields become active.  """  
      self.CheckOff2Label:str = obj["CheckOff2Label"]
      """  Label used for the JobHead.CheckOff2 field.  """  
      self.CheckOff3Label:str = obj["CheckOff3Label"]
      """  Label used for the JobHead.CheckOff3 field.  """  
      self.CheckOff4Label:str = obj["CheckOff4Label"]
      """  Label used for the JobHead.CheckOff4 field.  """  
      self.CheckOff5Label:str = obj["CheckOff5Label"]
      """  Label used for the JobHead.CheckOff5 field.  """  
      self.ClockFormat:str = obj["ClockFormat"]
      """  Indicates the format of how labor time is entered.  It can be entered as (M) - hours/minutes or (H) - Hours/Hundredths.  """  
      self.FeedPayroll:bool = obj["FeedPayroll"]
      """  Indicates if the labor entry details will be transferred to the Payroll system.  This is used to set the value of LaborDtl.Payroll flag.  """  
      self.RemoveLoad:str = obj["RemoveLoad"]
      """  Controls how shop load is removed.  It can either be by Actual Hours  "H" or based on quantity completed "Q".  """  
      self.MachinePrompt:bool = obj["MachinePrompt"]
      """  Controls whether or not entry of a Machine ID will be prompted for in Labor Entry and Labor Collection.  """  
      self.ReworkReasons:bool = obj["ReworkReasons"]
      """  Indicates if system should prompt for entry of a Rework Reason code for rework transactions during Labor Collection or Labor Entry.  """  
      self.ScrapReasons:bool = obj["ScrapReasons"]
      """  Indicates if system should prompt user to enter a Scrap Reason code for labor transactions where the scrap quantity is not zero during Labor Entry or Labor Collection.  """  
      self.JobSeqLength:int = obj["JobSeqLength"]
      """  Indicates the maximum number of digits to be entered into the JCSyst.NextJobNum field.  This also controls the number of digits that the system will generate when the user requests a "Next Job Number" while creating a new job number.  """  
      self.NextJobNumber:int = obj["NextJobNumber"]
      """  The value in this field represents the next default job sequence number.  The number of digits that can be entered is controlled by JCSyst.JobSeqLength.  Example of how the system uses these fields to generate a number that is inserted as part of the Job number when the user requests "Next Job Number" while creating a new job number would be: JobSeqLength = 6 and NextJobNumber = 100.  Then the system would try to insert  "000100" into the job number at the current insertion point.  """  
      self.Grace:int = obj["Grace"]
      """  Grace Period, stored as Hours/Hundredths  """  
      self.StdFormat:str = obj["StdFormat"]
      """   Default qualifier for the Production Standard field.  This is used as a default to the qualifier field in operation details when there is no related  OpStd record.  The valid qualifiers are:
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour, "PM" - Pieces/Minute, "OH" - Operations/Hour, "OM"  - Operations/minute, HR - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   Default standard basis is to be used to with standards that are time per piece (HP & MP).  The basis is a Divisor.  Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours.  The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Default for the JobOper and QuoteOpr.EstScrapType fields  """  
      self.InvAdjReasons:bool = obj["InvAdjReasons"]
      """  Indicates if system should prompt user to enter an Inventory Adjustment Reason code for quantity and cost adjustments.  """  
      self.SchedCode:str = obj["SchedCode"]
      """  SchedPri.SchedCode value that is marked as the default scheduling code in the Scheduling Priority Code master file.  """  
      self.SchedStartedOps:bool = obj["SchedStartedOps"]
      """  Default for scheduling operations that have been started.  A started operation is one with labor reported to it.  Global Scheduling uses this value.  """  
      self.WksLaborHistWarn:int = obj["WksLaborHistWarn"]
      """  The number of weeks labor warning detail is stored until they are purged.  """  
      self.GenLaborWarnMsg:bool = obj["GenLaborWarnMsg"]
      """  This option controls whether or not the labor warnings messages are generated/reported.  When this option is turned on labor warning records are created and the labor edit list and/or entry/tracker programs report these warnings.  When it is turned off the labor edit list performs its own warning checking and no warnings are reported in the entry/tracker programs.  This option should only be turned on between labor periods (i.e. after all of the labor has been reported, but before the next periods information has been entered).  Only maintainable if the Data Collection module has been installed.  """  
      self.PreventPJChange:bool = obj["PreventPJChange"]
      """  If set to Yes, the user must change the Job Engineered flag to No before they are allowed to make any changes to a Job.  """  
      self.LogChanges:bool = obj["LogChanges"]
      """  If this is Yes, then when Jobs are set to "Planned"  or any header flag is changed on a "Planned" job the user will be prompted to enter a description of the changes.  This option is only available when "PreventPJChange" = Yes.  """  
      self.EarlyClockInAllowance:int = obj["EarlyClockInAllowance"]
      """  Number of minutes used by data collection to determine the time frame in which early clock in times are to be adjusted forward to the shift start time.  If clock in time falls within the  time range of (Shift Start - Allowance) to Shift Start then the clock in time will set to Shift Start time.  """  
      self.LateClockInAllowance:int = obj["LateClockInAllowance"]
      """  Number of minutes used by data collection to determine the time frame in which late clock in times are to be adjusted backwards to the shift start time.  If clock in time falls within the  time range of Shift Start to (Shift Start + Allowance)  then the clock in time will set to Shift Start time.  """  
      self.EarlyClockOutAllowance:int = obj["EarlyClockOutAllowance"]
      """  Number of minutes used by data collection to determine the time frame in which early clock out times are to be adjusted forward to the shift end time.  If clock out time falls within the  time range of (Shift End - Allowance) to Shift End  then the clock out time will set to Shift end.  """  
      self.LateClockOutAllowance:int = obj["LateClockOutAllowance"]
      """  Minutes used to determine the time frame in which late clock out times are to be adjusted backwards to the shift end time.  If clock out time falls within the  time range of Shift end to (Shift Start + Allowance) then the clock out time will set to Shift End time.  """  
      self.FloatPartRev:bool = obj["FloatPartRev"]
      """  Default for "Floating " the part revision.  To "Float" the revision of unfirm jobs to the revision in effect at the time of the requirement.  """  
      self.ForecastDaysBefore:int = obj["ForecastDaysBefore"]
      """   Number of days before the forecast date in which any sales orders that exist should reduce the forecast quantity.
Ex: Forecast date of 3/31/98, Days before of 10, then any orders that have a date of 3/21/98 to 3/31/98 would reduce the forecast.  """  
      self.ForecastDaysAfter:int = obj["ForecastDaysAfter"]
      """   Number of days after the forecast date in which any sales orders that exist should reduce the forecast quantity.
Ex: Forecast date of 3/31/98, Days after  of 10, then any orders that have a date of 4/01/98 to 4/10/98 would reduce the forecast.  """  
      self.DetailGrace:bool = obj["DetailGrace"]
      """   Indicates if the LateClockIn or EarlyClockOut grace period should be applied to the labor detail transactions.
Ex: 10 minute LateClockIn, Shift Start = 8:00am, Employee clocks in and starts an activity  at 8:05.  If DetailGrace = Yes then StartTime on the detail will be adjusted to 8:00.  If DetailGrace = No then StartTime remains as 8:05 and an the 5 minutes will be included in the  idle time.  This setting does NOT affect how Start/End times are adjusted for the timecard record.  In both cases for this example the start time for the timecard will be 8:00.  """  
      self.PreventFABypass:bool = obj["PreventFABypass"]
      """  If set to Yes, the user is unable to start production work for an operation which is waiting for First Article approval.  """  
      self.ChgImpactPriceListCode:str = obj["ChgImpactPriceListCode"]
      """  Used to get a value for jobs not referencing a sales order.  If a part in not in the price list then use Part.UnitPrice.  """  
      self.EarlyGracePeriod:int = obj["EarlyGracePeriod"]
      """   Used in conjunction with the Late Grace Period to determine if a job is early, on-time or late.  Example: Early Grace Period is 4, Late Grace Period is 1, Job Required Date is 05/20/02: If the job is
scheduled to be completed before 05/16/02 it is Early.  If the job is
scheduled to be completed anywhere from 05/16/02 through 05/21/02 it is on-time.  If the job is scheduled to be completed after 05/21/02 it is late.  """  
      self.LateGracePeriod:int = obj["LateGracePeriod"]
      """   Used in conjunction with the Early Grace Period to determine if a job is early, on-time or late.  Example: Early Grace Period is 4, Late Grace Period is 1, Job Required Date is 05/20/02: If the job is
scheduled to be completed before 05/16/02 it is Early.  If the job is
scheduled to be completed anywhere from 05/16/02 through 05/21/02 it is on-time.  If the job is scheduled to be completed after 05/21/02 it is late.  """  
      self.QuickJobID:str = obj["QuickJobID"]
      """   NJ - Next Job
OR - Order Release  """  
      self.KanBanPrefix:str = obj["KanBanPrefix"]
      """  KanBanPrefix  """  
      self.NextOrderNumber:int = obj["NextOrderNumber"]
      """  The value in this field represents the next default transfer Order sequence number.  The number of digits that can be entered is controlled by JCSyst.OrderSeqLength.  Example of how the system uses these fields to generate a number that is inserted as part of the Transfer Order number when the user requests "Next Order Number" while creating a new Transfer Order number would be: OrderSeqLength = 6 and NextOrderNumber = 100.  Then the system would try to insert  "000100" into the Order number at the current insertion point.  """  
      self.OrderSeqLength:int = obj["OrderSeqLength"]
      """  Indicates the maximum number of digits to be entered into the JCSyst.NextOrderNum field.  This also controls the number of digits that the system will generate when the user requests a "Next Order Number" while creating a new order number.  """  
      self.NextTranLineNumber:int = obj["NextTranLineNumber"]
      """  The value in this field represents the next default transfer Order Line sequence number.  The number of digits that can be entered is controlled by JCSyst.OrderSeqLength.  Example of how the system uses these fields to generate a number that is inserted as part of the Transfer Detail Line number when the user requests "Next Line Number" when converting an MRP Transfer Line number would be: OrderSeqLength = 6 and NextTranLineNumber = 100.  Then the system would try to insert  "000100" into the Line Number at the current insertion point.  """  
      self.AllowSchedulingBeforeToday:bool = obj["AllowSchedulingBeforeToday"]
      """  Determines if a scheduler is allowed to schedule/reschedule jobs/operations (from the Scheduling Boards) to do work before today.  """  
      self.DirectShipVar:str = obj["DirectShipVar"]
      """  Indicates where to post all variances on a job that shipped direct for a standard cost part.  M = to the Product Group, C = to the Cost of Sales.  """  
      self.SplitMfgCostElements:bool = obj["SplitMfgCostElements"]
      """  Flag to indicate how to split the manufacturing cost elements when a manufactured material is issued to the job.  If flag is set to true, the cost of the issued material will be split into individual manufacturing cost elements. If set to false, the cost of the issued material is added to the manufacturing material cost element only.  """  
      self.UnfirmATP:bool = obj["UnfirmATP"]
      """  This flag is used by ATP to determine if Unfirm Jobs should be considered in ATP calculations.  """  
      self.ForecastPeriods:str = obj["ForecastPeriods"]
      """   The ForecastPeriods field defines the forecast periods that are used with the import and export process.

Examples: Year, Semester, Quarter, Month, Week, Day

This field is used with the ForecastPeriodsPerYear field.  """  
      self.ForecastPeriodsPerYear:int = obj["ForecastPeriodsPerYear"]
      """   The ForecastPeriodsPerYear field defines the number of forecast periods per year.

This field is used with the ForecastPeriods field.  """  
      self.ReplaceMissingValues:bool = obj["ReplaceMissingValues"]
      """   The ReplaceMissingValues field is used to determine how periods with zero demand should be exported when exporting forecast data.

If yes, then zero demand will be replaced with the string "MISSING" as long as there is no demand in previous periods.  If previous periods have some demand, then zero demand will be left as zero.

If the value of this field is no, then zero demand will be left as zero when exporting demand.  """  
      self.ForecastImportDay:int = obj["ForecastImportDay"]
      """   The ForecastImportDay field is used by the forecast import process to determine the forecast date for each forecast period.

The valid values for this field are dependent on the value in the ForecastPeriods field.  """  
      self.ChkEmpPrjRole:bool = obj["ChkEmpPrjRole"]
      """  If false then when an employee is booking hours to a job they can enter any Project Role code that has been set up on the employee. When the field is set to true then the Project Role entered MUST be one of the Project Role codes that have been assigned to the operation.  """  
      self.DfltPrjRoleLoc:str = obj["DfltPrjRoleLoc"]
      """   Defines where the default role code will be obtained.
The options are ?
Operation: Project Role code from the operation will be used.
Employee. Project Role Code from the Employee will be used.  """  
      self.DfltRevRecMthd:str = obj["DfltRevRecMthd"]
      """  Defines the default revenue recognition method to be used in project entry.The options are Default =  (blank).Code/Desc: INV = On Invoice, LBR = Labor Booking, MAN = Manual, BDN = Actual Burden, PCC = POC-Cost-to-Cost, PCE = POC-Efforts, PCU = POC-Units-of-Delivery  """  
      self.AllowRevRecChg:bool = obj["AllowRevRecChg"]
      """  Indicates whether the revenue recognition method can be changed on the project.  """  
      self.RevRecJrnlReverse:str = obj["RevRecJrnlReverse"]
      """  When set to Reserve following month the journal created will be flagged as a reversing journal.PCL = Reverse on Project Close, MON = Reverse Following Month  """  
      self.DfltPrjRtSrc:str = obj["DfltPrjRtSrc"]
      """  Defines where the invoice process will obtain the Project Role Rates from. Hierarchical works as defined for Invoice Preparation. All of the others will ONLY obtain the rates from the area defined. HIER = Hierarchical, PROJ = Project Only, EMPL = Employee Only, ROLE = Project Role Only  """  
      self.AllowPrjRtSrcChg:bool = obj["AllowPrjRtSrcChg"]
      """  True indicates the user can change the Derive Project Rates from at the project level.  """  
      self.ExtFcstImpFormat:str = obj["ExtFcstImpFormat"]
      """  The default format to use when importing forecast data from external forecast solutions.  """  
      self.ExtFcstExpFormat:str = obj["ExtFcstExpFormat"]
      """  The default format to use when exporting sales history data to external forecast solutions.  """  
      self.ConInvMeth:str = obj["ConInvMeth"]
      """   Default of Invoicing Method of new Project. If advanced billing is not licensed the only options are CS and MB. Code/Desc:
CS = Customer Shipment, 
MB = Milestone Billing, 
FF = Fixed Fee;
CP = Cost Plus;
TM = Time and Material;
PP = Progress payment;

The default is Customer Shipment.  """  
      self.MtlTaxCatID:str = obj["MtlTaxCatID"]
      """  Tax Category to default into Project. MtlTaxCatID.  """  
      self.LbrTaxCatID:str = obj["LbrTaxCatID"]
      """  Tax Category to default into Project LbrTaxCatID.  """  
      self.FeeTaxCatID:str = obj["FeeTaxCatID"]
      """  Tax Category to default into Project. FeeTaxCatID.  """  
      self.ODCTaxCatID:str = obj["ODCTaxCatID"]
      """  Tax Category to default into Project. ODCaxCatID.  """  
      self.SubTaxCatID:str = obj["SubTaxCatID"]
      """  Tax Category to default into Project. SubTaxCatID.  """  
      self.BdnTaxCatID:str = obj["BdnTaxCatID"]
      """  Tax Category to default into Project. BdnTaxCatID.  """  
      self.TaxOnNetOfRet:bool = obj["TaxOnNetOfRet"]
      """  Tax Category to default into Project. TaxOnNetOfRet.  """  
      self.AllowChkEmpPrjRoleChg:bool = obj["AllowChkEmpPrjRoleChg"]
      """  indicates if the company setting for ChkEmpPrjRole can be overridden at the project level.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AdvancedLaborRate:bool = obj["AdvancedLaborRate"]
      """  AdvancedLaborRate  """  
      self.CapRevID:int = obj["CapRevID"]
      """  CapRevID  """  
      self.AutoReceipt:bool = obj["AutoReceipt"]
      """  AutoReceipt  """  
      self.MRPJobID:str = obj["MRPJobID"]
      """  MRPJobID  """  
      self.PbsTaxCatID:str = obj["PbsTaxCatID"]
      """  Tax Category to default into Project. PbsTaxCatID. (Billing Schedule)  """  
      self.SOAllowWBSPhase:bool = obj["SOAllowWBSPhase"]
      """  True indicates the user can link a sales order per wbs phase on project.  """  
      self.SOAutoRelWBSPhase:bool = obj["SOAutoRelWBSPhase"]
      """  SOAutoRelWBSPhase  """  
      self.SchedAnUnEngineered:bool = obj["SchedAnUnEngineered"]
      """  SchedAnUnEngineered  """  
      self.GetCostsFromTemplate:bool = obj["GetCostsFromTemplate"]
      """  GetCostsFromTemplate  """  
      self.AllowMoveJobsAcrossPlants:bool = obj["AllowMoveJobsAcrossPlants"]
      """  Allows moving Jobs across sites within the company and not only for the site where user is logged on.  """  
      self.MPSOnly:bool = obj["MPSOnly"]
      """  MPSOnly  """  
      self.EnableSchedDebugLog:bool = obj["EnableSchedDebugLog"]
      """  EnableSchedDebugLog  """  
      self.IncludeExtraDetailsLog:bool = obj["IncludeExtraDetailsLog"]
      """  IncludeExtraDetailsLog  """  
      self.MtlQtyParentDefault:int = obj["MtlQtyParentDefault"]
      """  MtlQtyParentDefault  """  
      self.AssignPrimarySupplier:bool = obj["AssignPrimarySupplier"]
      """  AssignPrimarySupplier  """  
      self.AvoidIncludeQuotePrjRevenue:bool = obj["AvoidIncludeQuotePrjRevenue"]
      """  AvoidIncludeQuotePrjRevenue  """  
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.MaxLogDay:int = obj["MaxLogDay"]
      """  MaxLogDay  """  
      self.DefaultRecognizeRevenueAtPhaseLevel:bool = obj["DefaultRecognizeRevenueAtPhaseLevel"]
      """  Default Option to activate Revenue Recognition at WBS Phase level  """  
      self.EnableShipTo:bool = obj["EnableShipTo"]
      """  EnableShipTo  """  
      self.StdFormatDesc:str = obj["StdFormatDesc"]
      self.TaxCatPbsDescription:str = obj["TaxCatPbsDescription"]
      self.IncludeQuotePrjRevenue:bool = obj["IncludeQuotePrjRevenue"]
      """  Include quotes without link to SO to Projected Revenue  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ChgImpactPriceLstListDescription:str = obj["ChgImpactPriceLstListDescription"]
      self.TaxCatBdnDescription:str = obj["TaxCatBdnDescription"]
      self.TaxCatFeeDescription:str = obj["TaxCatFeeDescription"]
      self.TaxCatLbrDescription:str = obj["TaxCatLbrDescription"]
      self.TaxCatMtlDescription:str = obj["TaxCatMtlDescription"]
      self.TaxCatODCDescription:str = obj["TaxCatODCDescription"]
      self.TaxCatSubDescription:str = obj["TaxCatSubDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MMSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DefaultStatusID:str = obj["DefaultStatusID"]
      """  Identifies the EquipStatusID that is to be used as the default for Equip.StatusID. This may be blank. Not directly maintainable. It gets set by Equipment Status maintenance when the user checks the "Default" box.  """  
      self.TemplateJobNum:str = obj["TemplateJobNum"]
      """  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  """  
      self.JobPrefix:str = obj["JobPrefix"]
      """  Prefix that will be used when generating  Maintenance Job numbers for this company. Note this may be overridden at the Site level (see SiteConfCntrl.MaintJobPrefix)  """  
      self.MaintBuffer:int = obj["MaintBuffer"]
      """  MMSyst.MaintBuffer, default for EquipPlan.MaintBuffer  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.JobHeadPartDescription:str = obj["JobHeadPartDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PDMSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PDMExportDir:str = obj["PDMExportDir"]
      """  PDM Export directory  """  
      self.PDMImportDir:str = obj["PDMImportDir"]
      """  PDM Import Directory  """  
      self.DocExportDir:str = obj["DocExportDir"]
      """  Document Export Directory  """  
      self.DocImportDir:str = obj["DocImportDir"]
      """  Document Import Directory  """  
      self.ECOGroupID:str = obj["ECOGroupID"]
      """  The default Group id for the ECO Group  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Default pdm revision number  """  
      self.SearchWord:str = obj["SearchWord"]
      """  The default pdm searchword for new parts.  """  
      self.FileNum:int = obj["FileNum"]
      """  File number used for identification of integration files.  """  
      self.PartPrefix:str = obj["PartPrefix"]
      """  File name prefix for parts.  """  
      self.BomPrefix:str = obj["BomPrefix"]
      """  File name prefix for Boms.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PLMRevision:str = obj["PLMRevision"]
      """  PLM process will consider two types of revision. Current Revision: last approved revision with effective date less or equal than today. Last approved revision: (no matter the effective date) so if the customer has multiple revisions and one is approved, even if it’s for a future date, we will send this one.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ECOGroupIDDescription:str = obj["ECOGroupIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PECompWhldHistRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RecordSeq:int = obj["RecordSeq"]
      """  Record Sequence  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Create Date  """  
      self.UserID:str = obj["UserID"]
      """  User Identifier.  """  
      self.GoodContributor:bool = obj["GoodContributor"]
      """  Good Contributor  """  
      self.WithholdingAgent:bool = obj["WithholdingAgent"]
      """  Indicates the status of Withholding Agent.  """  
      self.CollectionAgent:bool = obj["CollectionAgent"]
      """  Collection Agent withholding status.  """  
      self.NotFound:bool = obj["NotFound"]
      """  Not Found withholding status.  """  
      self.NoAddress:bool = obj["NoAddress"]
      """  No Address Provided withholding status.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Password:str = obj["Password"]
      """  During Payroll Class maintenance the user is prompted for a password.  The entered password is encoded and then compared to this string.  An encoded string that is checked before allowing access to the payroll class maintenance program.  If blank then user is prompted to enter a password before allowing access to PRClass maintenance.  It does not matter what security level the user is, they just need to know this password in order to gain access.  """  
      self.CheckSort:str = obj["CheckSort"]
      """   Controls the order in which checks are printed. Valid options are;
"SuperID", "Name", "EmpID","Dept".  """  
      self.SemiDay:int = obj["SemiDay"]
      """  Identifies the day of the month which the 2nd period starts for semimonthly payroll runs.  """  
      self.PRStartDate:str = obj["PRStartDate"]
      """  Date that the Manufacturing System payroll will become effective.  When initially starting up payroll the user enters the employee year to date information as of (PRStartDate - 1day).  If the user wants the initial quarter to date figures to be correct they should start payroll at the beginning of a quarter and enter that start date here.  """  
      self.NoPRMgr:str = obj["NoPRMgr"]
      """   Encoded field which indicates if Payroll Managers have been set up.
(Blank = Not a PR manager).  Only users that are Payroll managers are allowed access to payroll class maintenance where they can establish the list of authorized users for the class.
There must always be at least one user where DspPayrollMgr = Yes.  """  
      self.HCMEnabled:bool = obj["HCMEnabled"]
      """  Enable/Disable the HCM Integration. May be License specific (TBD)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrintRates:bool = obj["PrintRates"]
      """  PrintRates  """  
      self.AllowHighPayRate:bool = obj["AllowHighPayRate"]
      """  If enabled the user is able to enter a max pay rate of 999999.9999 in Payroll Employee, currently the system only allows a max of 9999.9999.  """  
      self.PRChecksExist:bool = obj["PRChecksExist"]
      """  Payroll checks exist for this company  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxSvcConfigRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.URL:str = obj["URL"]
      """  The location of the AvaTax service when the address will not change between the client and web service.  """  
      self.ViaURL:str = obj["ViaURL"]
      """  The intermediary server, for example a firewall, for the AvaTax service.  """  
      self.TextCase:str = obj["TextCase"]
      """  Stores the text case used for address validation. Possible values are Default, Upper, and Mixed  """  
      self.Account:str = obj["Account"]
      """  The unique account number provided by Avalara for verification against the service. May also contain a username.  """  
      self.Key:str = obj["Key"]
      """  The unique alpha-numeric key for the account provided by Avalara for verification against the service. May also contain a password if Account contains a username.  """  
      self.TaxConnectEnabled:bool = obj["TaxConnectEnabled"]
      """  Indicates whether the Epicor Tax Connect interface is active for this company. If false, no Tax Connect address validation or tax calculations will take place regardless of how the company flags are set for those functions.  """  
      self.AddrValEnabled:bool = obj["AddrValEnabled"]
      """   Indicates whether the system can perform address validation via Epicor Tax Connect. If TaxConnectEnabled flag = true this flag will be checked to see if address validations are authorized/available via the
Epicor Tax Connect. If false no address validation logic will be executed.  """  
      self.TaxCalcEnabled:bool = obj["TaxCalcEnabled"]
      """  Indicates whether the system should perform tax calculations via Epicor Tax Connect. If TaxConnectEnabled flag = true this flag will be checked to see if tax calculations are authorized/available via Epicor Tax Connect. If false the base Epicor tax calculations will take place.  """  
      self.TaxIdPrefix:str = obj["TaxIdPrefix"]
      """  The Prefix to be used in conjunction with the SalesTaxSeq database sequence for automatically created SalesTax records  """  
      self.RequestTimeOut:int = obj["RequestTimeOut"]
      """  Request timeout value for tax connect requests, in seconds.  """  
      self.DefaultTaxCatID:str = obj["DefaultTaxCatID"]
      """  The default tax category to assign to a Sales Order/Quote/Invoice  record if tax connect is enabled and no tax category is defaulted via the standard tax category default logic.  """  
      self.LastDocId:int = obj["LastDocId"]
      """  This records the last document id retrieved from a ReconcileTaxHistory call to Avalara. It will be used to default the starting document ID in the Get Tax History action in Tax Reconciliation process.  """  
      self.DebugMode:bool = obj["DebugMode"]
      """  Specifies if Tax Connect will run in Debug Mode. When TRUE the input-output XML files sent and received to Avalara will NOT be deleted so they can be reviewed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ValidateISOCode:bool = obj["ValidateISOCode"]
      """  ValidateISOCode  """  
      self.CertCaptureEnabled:bool = obj["CertCaptureEnabled"]
      """  Indicates whether the system can perform CertCapture transactions. If CertCaptureEnabled is true, CertCapture features will be available. Otherwise, they won't.  """  
      self.APTaxDisplayAccount:str = obj["APTaxDisplayAccount"]
      self.APTaxAcctDesc:str = obj["APTaxAcctDesc"]
      self.ARTaxDisplayAccount:str = obj["ARTaxDisplayAccount"]
      self.ARTaxAcctDesc:str = obj["ARTaxAcctDesc"]
      self.ETCOffline:bool = obj["ETCOffline"]
      """  External field to be used to indicate that the Tax Connect service is off line. This filed can be set by the BL when a communication failure with tax connect occurs, or can be set manually in the UI when the user indicates that tax connect is offline. If set to true then the BL will not attempt any communication with the tax service. This is used to save unnecessary processing delays trying to communicate with the tax service when it is known that the service is unavailable.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxCatDescription:str = obj["TaxCatDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtCompanyTableset:
   def __init__(self, obj):
      self.Company:list[Erp_Tablesets_CompanyRow] = obj["Company"]
      self.CompanyAttch:list[Erp_Tablesets_CompanyAttchRow] = obj["CompanyAttch"]
      self.AGCompany:list[Erp_Tablesets_AGCompanyRow] = obj["AGCompany"]
      self.APSyst:list[Erp_Tablesets_APSystRow] = obj["APSyst"]
      self.ARSyst:list[Erp_Tablesets_ARSystRow] = obj["ARSyst"]
      self.BMSyst:list[Erp_Tablesets_BMSystRow] = obj["BMSyst"]
      self.BorderPct:list[Erp_Tablesets_BorderPctRow] = obj["BorderPct"]
      self.CRSyst:list[Erp_Tablesets_CRSystRow] = obj["CRSyst"]
      self.CSFSyst:list[Erp_Tablesets_CSFSystRow] = obj["CSFSyst"]
      self.Currency:list[Erp_Tablesets_CurrencyRow] = obj["Currency"]
      self.CurrRateGrp:list[Erp_Tablesets_CurrRateGrpRow] = obj["CurrRateGrp"]
      self.EQSyst:list[Erp_Tablesets_EQSystRow] = obj["EQSyst"]
      self.ExtPRSyst:list[Erp_Tablesets_ExtPRSystRow] = obj["ExtPRSyst"]
      self.FsSyst:list[Erp_Tablesets_FsSystRow] = obj["FsSyst"]
      self.GLSyst:list[Erp_Tablesets_GLSystRow] = obj["GLSyst"]
      self.ISSyst:list[Erp_Tablesets_ISSystRow] = obj["ISSyst"]
      self.JCSyst:list[Erp_Tablesets_JCSystRow] = obj["JCSyst"]
      self.MMSyst:list[Erp_Tablesets_MMSystRow] = obj["MMSyst"]
      self.PDMSyst:list[Erp_Tablesets_PDMSystRow] = obj["PDMSyst"]
      self.PECompWhldHist:list[Erp_Tablesets_PECompWhldHistRow] = obj["PECompWhldHist"]
      self.PRSyst:list[Erp_Tablesets_PRSystRow] = obj["PRSyst"]
      self.TaxSvcConfig:list[Erp_Tablesets_TaxSvcConfigRow] = obj["TaxSvcConfig"]
      self.XaSyst:list[Erp_Tablesets_XaSystRow] = obj["XaSyst"]
      self.XbSyst:list[Erp_Tablesets_XbSystRow] = obj["XbSyst"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_XaSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DefaultUM:str = obj["DefaultUM"]
      """  The default Unit of Measure that will be used when creating a part.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Used as the default costing method when creating new parts in Part Master Maintenance. Remember that each Part defines its own costing method. The possible values are "A" - Average, "L" - Last or  "S" - standard.  """  
      self.DefaultPlant:str = obj["DefaultPlant"]
      """  Establishes the default Site ID to be used as the default for a Part's Primary Site field during Part maintenance.  The Default Warehouse must be in the DefaultSite.  """  
      self.PrintCompanyName:bool = obj["PrintCompanyName"]
      """  Indicates if Company Name & Address should print on forms.  """  
      self.StartOrderNum:int = obj["StartOrderNum"]
      """  Used to establish the beginning Sales Order #. When the system generates a new order it will assign the greater of (StartOrderNum) or (the last orders # on file + 1) as the order number.  """  
      self.StartPONum:int = obj["StartPONum"]
      """  Used to establish the beginning Purchase Order #. When the system generates a new PO, it will assign the greater of (StartPONum) or (the last orders # on file + 1) as the PO number.  """  
      self.StartPSNum:int = obj["StartPSNum"]
      """  Used to establish the beginning Packing Slip #. When the system generates a new packing slip it will assign the greater of (StartPSNum) or (the last Packing Slips  # on file + 1) as the PS number.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Identifies the Terms master that is to be used as the default when creating customer masters. This can be left blank if there is no one best terms default. Otherwise it gets set via terms maintenance when the user checks the "Default" box.  """  
      self.ShipNoJob:bool = obj["ShipNoJob"]
      """  Controls the entry of ship from job quantity in shipping entry program. If set to "yes" then job quantity field is enabled regardless of the order being linked to a job. This is intended only to be set to "yes" during the initial system implementation period. So that users can create and ship orders for manufactured items without forcing them to have established jobs  """  
      self.BookOrders:bool = obj["BookOrders"]
      """  This field indicates if the system should generate sales order booking records. Booking tables are used to store changes in sales volume. See BookOrd & BookDtl for more info.  """  
      self.PrintBarCodes:bool = obj["PrintBarCodes"]
      """  Option that controls the sensitivity of Bar Code Printing options.  """  
      self.StartRMANum:int = obj["StartRMANum"]
      """  Used to establish the beginning RMA#. When the system generates a new RMA it will assign the greater of (StartRMANum) or (the last RMA # on file + 1) as the RMA number.  """  
      self.DefaultShipViaCode:str = obj["DefaultShipViaCode"]
      """  Identifies the ShipVia master that is to be used as the default when creating Purchase Orders. This may be blank if there is no one normal ship via. Not directly maintainable. It gets set by Ship Via maintenance when the user checks the "Default" box.  """  
      self.StartRFQNum:int = obj["StartRFQNum"]
      """  Used to establish the beginning PurchaseRFQ #. When the system generates a new RFQ it will assign the greater of (StartRFQNum) or (the last RFQ # on file + 1) as the RFQ number.  """  
      self.CheckOff1Label:str = obj["CheckOff1Label"]
      """  Label used for the DMRHead.CheckOff1 field.  There are 5 CheckOffLabel fields. They are all optional. If entered then the corresponding CheckOff fields become active.  """  
      self.CheckOff2Label:str = obj["CheckOff2Label"]
      """  Label used for the DMRHead.CheckOff2 field.  """  
      self.CheckOff3Label:str = obj["CheckOff3Label"]
      """  Label used for the DMRHead.CheckOff3 field.  """  
      self.CheckOff4Label:str = obj["CheckOff4Label"]
      """  Label used for the DMR.CheckOff4 field.  """  
      self.CheckOff5Label:str = obj["CheckOff5Label"]
      """  Label used for the DMRHead.CheckOff5 field.  """  
      self.GlobalSN:bool = obj["GlobalSN"]
      """  Global SN  """  
      self.IJJournalCode:str = obj["IJJournalCode"]
      """  The Journal Code of the Journal that will be used for Inventory/WIP transactions. The Job management Calculate WIP/COS process creates entries in this journal.  """  
      self.StartNonConfID:int = obj["StartNonConfID"]
      """  Starting ID number for non-conformance records.  """  
      self.StartCorrActID:int = obj["StartCorrActID"]
      """  Starting ID number for non-conformance records.  """  
      self.ReduceRelQty:bool = obj["ReduceRelQty"]
      """  Option to keep the Sales Order Detail quantity constant.  """  
      self.SysBuyerID:str = obj["SysBuyerID"]
      """  System default buyer id.  This identifies the buyer that will be used during the auto po generation process when no buyer is defined by the PartClass or OpCode records.  """  
      self.StartTFOrderNum:int = obj["StartTFOrderNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available number is assigned by the system. The system generates a number by finding the order number of the last record on file and then a 1 to it.  """  
      self.AutoOrderBasedDisc:bool = obj["AutoOrderBasedDisc"]
      """  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The default shipvia code for the Counter Sales order.  """  
      self.InvcGrpPfx:str = obj["InvcGrpPfx"]
      """  The invoice group prefix for counter sales orders. The invoice group id is based on this prefix plus two digits of today's month  plus two digits of the today's daynumber.  """  
      self.PlantCostID:str = obj["PlantCostID"]
      """  If a Site does not have a specified SiteCostID, use this one instead  """  
      self.HDDefaultTaskSetID:str = obj["HDDefaultTaskSetID"]
      """  The default task set for use in the Help Desk.  """  
      self.HDAutoCompleteTasks:bool = obj["HDAutoCompleteTasks"]
      """  If true, users can auto-complete Help Desk tasks by changing the current workflow stage.  """  
      self.StagingReq:bool = obj["StagingReq"]
      """  Indicates whether to use the shipping staging logic  """  
      self.EAQActive:bool = obj["EAQActive"]
      """  True value indicates that the Epicor Advanced Quality module is active.  Related to IQS integration.  """  
      self.DftInputChannel:str = obj["DftInputChannel"]
      """  This field will hold the default URL for the Service Connect input channel.  This is only used as the default as the user can specify the individual URLs for data element to be passed to amd from the IQS application.  """  
      self.DftOutputChannel:str = obj["DftOutputChannel"]
      """  This field will hold the default URL for the Service Connect output channel.  This is only used as the default as the user can specify the individual URLs for data element to be passed to amd from the IQS application.  """  
      self.DefaultMiscFreightCC:str = obj["DefaultMiscFreightCC"]
      """  Default Miscellaneous Freight Charge Customer Connect  """  
      self.SOReadyToCalcDflt:bool = obj["SOReadyToCalcDflt"]
      """  This flag will be used to default the OrderHed.ReadyToCalc field when an invoice is created. Defaults to No.  """  
      self.SODiscountUnitPrice:bool = obj["SODiscountUnitPrice"]
      """  Specifies if line discounts shall be applied to the unit price or the line value.  """  
      self.DefUOMClassID:str = obj["DefUOMClassID"]
      """   Default Unit of Measure Class. Used as the default value when creating new Part masters.
Must be  valid in the UOMClass table.
The UOMClass has a default UOMCode which replaces the 8.3 XASyst.DefaultUM.  """  
      self.AlphaNumeric:str = obj["AlphaNumeric"]
      """  The character that will represent the place holder for any alphanumeric character ((e.g. 5 / A / a). Default is "&"  """  
      self.AlphaNumExample:str = obj["AlphaNumExample"]
      """  Indicates the string to use when constructing an Example for a serial mask in Serial Mask Maintenance and the AlphaNumeric character is part of the mask. The default is "A".  """  
      self.AlphaOnly:str = obj["AlphaOnly"]
      """  This is the character used to represent alpha characters (e.g. [a to z] or [A to Z]). Default is "@"  """  
      self.AlphaOnlyExample:str = obj["AlphaOnlyExample"]
      """  Indicates the string to use when constructing an Example for a serial mask in Serial Mask Maintenance and the AlphaOnly character is part of the mask. The default will be "B".  """  
      self.NumericOnly:str = obj["NumericOnly"]
      """  This is the character used to represent a numeric character (e.g. [0 to 9]). Default is "#".  """  
      self.AnyMandatory:str = obj["AnyMandatory"]
      """  This is the character used to represent a mandatory variable that can be any alphanumeric character. Therefore if the user enters 2 followed by this character in the mask then when a serial number is created these charaters must be replaced with any single character. Default is "?"  """  
      self.OptionalAlphaNumeric:str = obj["OptionalAlphaNumeric"]
      """  This character is used to represent an optional variable that can be any alphanumeric character. NOTE this character can ONLY be added as the last characters in the mask. Default is "!"  """  
      self.StripChar:str = obj["StripChar"]
      """  This character is used to represent the characters that are to be stripped off when the internal serial number is created. This character can ONLY be at the front or back of the mask. The default is "~"  """  
      self.DayChar:str = obj["DayChar"]
      """  When this character is entered in the mask surrounded by <> characters then a day number as a 2 numeric value will be automatically inserted into the serial number at that position. This will consume 2 characters of the serial number string. (Only allowed for auto generation masks). The default is "D"  """  
      self.MonthChar:str = obj["MonthChar"]
      """  When this character  is entered in the mask surrounded by <> characters this will then automatically enter into the serial number the month number as a 2 numeric value. This will consume 2 characters of the serial number string. (Only allowed for auto generation masks). The default is "M"  """  
      self.Year2Char:str = obj["Year2Char"]
      """  When this is 2 character string is entered in the mask surrounded by <> characters this will then automatically enter into the serial number the last 2 numeric values of the current calendar year. This must be entered as 2 identical  characters and will consume 2 characters of the serial number string. (Only allowed for auto generation masks). The default is "YY"  """  
      self.Year4Char:str = obj["Year4Char"]
      """  When this 4 character string is entered in the mask surrounded by < > characters this will then automatically enter into the serial number the full value of the year. This must be entered as 4 identical  characters and will consume 4 characters of the serial number string. (Only allowed for auto generation masks) The default is "YYYY"  """  
      self.PartChar:str = obj["PartChar"]
      """  If this is entered in the mask it must be followed by a hard coded numeric value indicating the number of characters of the part number that will be included in the serial number. The PartChar and the hard coded number should be encased in <> characters when building the mask. E.g. if the part representation  character is entered as "P" and the part number is DS4000-1 and <P6> is entered in the mask then DS4000 will be included in the serial number. The default is "P". (Only allowed for auto generation masks)  """  
      self.PartCharExample:str = obj["PartCharExample"]
      """  Indicates the string to use when constructing an Example for a serial mask in Serial Mask Maintenance and the PartChar character is part of the mask. The default will be  ?EPICORSERIALNUMBERMASKFORMATEXAMPLE?.  """  
      self.SODiscountRound:str = obj["SODiscountRound"]
      """  Discount rounding option: NE - Round net price by extended amount, NP - Round net price by unit price,  EP - Round discount by extended amount; UP - Round discount by unit price.  """  
      self.SMIPackSlip:int = obj["SMIPackSlip"]
      """  Pack Slip counter used for generating new automatic SMI PO Receipts.  """  
      self.SMIYear:int = obj["SMIYear"]
      """  This field holds the current year that is used as part of the key when generating an auto generated receipt for supplier managed inventories.  This is used in the program im/GenSMIReceipt.p  """  
      self.DefaultShift:int = obj["DefaultShift"]
      """  Default is blank.  Values include active shifts.  Selected value is used as the default value for Shift in Employee Maintenance.  """  
      self.IQSActive:bool = obj["IQSActive"]
      """  Select this checkbox to enable the AQM Integration. This checkbox enables movement of data in both directions, from the Epicor application to AQM and vice versa.  """  
      self.IQSOutputDir:str = obj["IQSOutputDir"]
      """  Specifies a selected folder path where the data will be exported. For example, C:\Epicor3Data\ServiceConnect\AQM\DataExportOut. Only enable if AQM integration is active.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.StartBOLNum:int = obj["StartBOLNum"]
      """  StartBOLNum  """  
      self.PrjAllowWBSPhase:bool = obj["PrjAllowWBSPhase"]
      """  Allow Project/WBS phase to be defined  """  
      self.PrjJobType:str = obj["PrjJobType"]
      """  Default Job Type of Sales Order line.  """  
      self.RMAUseRefCosts:bool = obj["RMAUseRefCosts"]
      """  Use reference invoice costs for RMA  """  
      self.UseOMBaseCurr:bool = obj["UseOMBaseCurr"]
      """  Used for Sales Order to give the ability to find price lists using the base currency if the customer currency if foreign.  """  
      self.PassedReqMove:bool = obj["PassedReqMove"]
      """  PassedReqMove  """  
      self.FailedReqMove:bool = obj["FailedReqMove"]
      """  FailedReqMove  """  
      self.PassedRMAReqMove:bool = obj["PassedRMAReqMove"]
      """  PassedRMAReqMove  """  
      self.FailedRMAReqMove:bool = obj["FailedRMAReqMove"]
      """  FailedRMAReqMove  """  
      self.QuoteToSOReadyToCalcDflt:bool = obj["QuoteToSOReadyToCalcDflt"]
      """  QuoteToSOReadyToCalcDflt  """  
      self.SOReadyToFulfillDflt:bool = obj["SOReadyToFulfillDflt"]
      """  This flag will be used to default the OrderHed.ReadyToFulfill field when a sales order is created.  """  
      self.MaxPCIDParentChildLevels:int = obj["MaxPCIDParentChildLevels"]
      """  Indicates the maximum number of levels of parent/child nesting allowed.  """  
      self.MaxWorkQueueRecords:int = obj["MaxWorkQueueRecords"]
      """  Default Amount of Rows by Page to display in the MES Work Queue UI at Startup. Set it to ZERO to retrieve all the Work Queue records at once, into one single page.  """  
      self.RMAAllowMultipleCredInv:bool = obj["RMAAllowMultipleCredInv"]
      """  RMAAllowMultipleCredInv  """  
      self.FSATranDocTypeID:str = obj["FSATranDocTypeID"]
      """  Specifies a legal number that will default when AR invoices import from Epicor FSA.  """  
      self.FSAPromptForInstallation:bool = obj["FSAPromptForInstallation"]
      """  FSAPromptForInstallation  """  
      self.FSATranDocTypeIDCreditMemo:str = obj["FSATranDocTypeIDCreditMemo"]
      """  Specifies a legal number that will default when Credit Memos import from Epicor FSA.  """  
      self.TransactionRetrievalDays:int = obj["TransactionRetrievalDays"]
      """  TransactionRetrievalDays  """  
      self.IQSOutputFormat:str = obj["IQSOutputFormat"]
      """  This field defines the format that will be used to export the data in the AQM Synchronization Process. The valid options are Extended: Extended version and Compact: Compact version. Only enabled if AQM integration is active.  """  
      self.JobReadyToFulfillDflt:bool = obj["JobReadyToFulfillDflt"]
      """  This flag will be used to default the ReadyToFulfill field for jobs.  """  
      self.TransferReadyToFulfillDflt:bool = obj["TransferReadyToFulfillDflt"]
      """  This flag will be used to default the ReadyToFulfill field for transfer orders.  """  
      self.EnableSNMaskFields:bool = obj["EnableSNMaskFields"]
      self.FSACMemoTranDocDesc:str = obj["FSACMemoTranDocDesc"]
      self.FSAInvoiceTranDocDesc:str = obj["FSAInvoiceTranDocDesc"]
      self.InvcTranType:str = obj["InvcTranType"]
      self.TmpStartOrderNum:int = obj["TmpStartOrderNum"]
      """  A temporary field for the UI for starting order number until the db StartOrderNum field format can be changed to contain 9 digits.  """  
      self.CMTranType:str = obj["CMTranType"]
      self.FSMDocTypeID:str = obj["FSMDocTypeID"]
      """  FSMDocTypeID (Attachment Document Type).  """  
      self.FSMSyncAnalysisCd:bool = obj["FSMSyncAnalysisCd"]
      """  Company flag to enable FSM sync of Analysis Code  """  
      self.FSMSyncEmpBasic:bool = obj["FSMSyncEmpBasic"]
      """  Company flag to enable FSM sync of Employee (Service Tech)  """  
      self.FSMSyncFSAssetClass:bool = obj["FSMSyncFSAssetClass"]
      """  Company flag to enable FSM sync of Asset Class (Equipment Type)  """  
      self.FSMSyncIndirect:bool = obj["FSMSyncIndirect"]
      """  Company flag to enable FSM sync of Asset Class (Work Code)  """  
      self.FSMSyncOpMaster:bool = obj["FSMSyncOpMaster"]
      """  Company flag to enable FSM sync of Operation (Condition)  """  
      self.FSMSyncPartClass:bool = obj["FSMSyncPartClass"]
      """  Company flag to enable FSM sync of Part Class  """  
      self.FSMSyncPlant:bool = obj["FSMSyncPlant"]
      """  Company flag to enable FSM sync of Site (Dispatch Location)  """  
      self.FSMSyncSerialNo:bool = obj["FSMSyncSerialNo"]
      """  Company flag to enable FSM sync of Serial Number (Equipment)  """  
      self.FSMSyncUOM:bool = obj["FSMSyncUOM"]
      """  Company flag to enable FSM sync of UOM  """  
      self.FSMSyncWarehse:bool = obj["FSMSyncWarehse"]
      """  Company flag to enable FSM sync of Warehouse  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DefaultPlantName:str = obj["DefaultPlantName"]
      self.HDTaskTaskSetDescription:str = obj["HDTaskTaskSetDescription"]
      self.HDTaskWorkflowType:str = obj["HDTaskWorkflowType"]
      self.IJJournalJrnlDescription:str = obj["IJJournalJrnlDescription"]
      self.PlantCostDescription:str = obj["PlantCostDescription"]
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_XbSystRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.POUserChar1Label:str = obj["POUserChar1Label"]
      """  Contains the Label used for the user defined field in the Purchase Order Master.  """  
      self.POUserChar2Label:str = obj["POUserChar2Label"]
      """  Contains the Label used for the 2nd user defined character  field in the Purchase Order Master.  """  
      self.POUserChar3Label:str = obj["POUserChar3Label"]
      """  Contains the Label used for the 3rd user defined character field in the Purchase Order Master.  """  
      self.POUserChar4Label:str = obj["POUserChar4Label"]
      """  Contains the Label used for the 4th user defined character field in the Purchase Order Master.  """  
      self.POUserDate1Label:str = obj["POUserDate1Label"]
      """  Contains the Label used for the 1st user defined date field in the Purchase Order Master..  """  
      self.POUserDate2Label:str = obj["POUserDate2Label"]
      """  Contains the Label used for the 2nd user defined date field in the Purchase Order Master.  """  
      self.POUserDate3Label:str = obj["POUserDate3Label"]
      """  Contains the Label used for the 3rd user defined date field in the Purchase Order Master.  """  
      self.POUserDate4Label:str = obj["POUserDate4Label"]
      """  Contains the Label used for the 4th user defined date  field in the Purchase Order Master.  """  
      self.POUserDec1Label:str = obj["POUserDec1Label"]
      """  Contains the Label used for the 1st user defined decimal field in the Purchase Order Master..  """  
      self.POUserDec2Label:str = obj["POUserDec2Label"]
      """  Contains the Label used for the 2nd user defined decimal field in the Purchase Order Master.  """  
      self.POUserInt1Label:str = obj["POUserInt1Label"]
      """  Contains the Label used for the 1st user defined field in the Purchase Order Master.  """  
      self.POUserInt2Label:str = obj["POUserInt2Label"]
      """  Contains the Label used for the 2nd user defined field in the Purchase Order Master.  """  
      self.ConsolidatedPurchasingCompany:str = obj["ConsolidatedPurchasingCompany"]
      """  Company that is the Parent of Consolidated Purchasing.  More than one company can be attached to a serial number that has the Consolidated Purchasing module entered.  This field designates which of those companies is the parent of Consolidated Purchasing and can therefore create Consolidated Purchase Orders.  """  
      self.GlobalCurrencyCode:str = obj["GlobalCurrencyCode"]
      """  Holds the Currency.CurrencyCode value in which Consolidated Purchasing data will be exchanged.  """  
      self.ExpPartCKOut:bool = obj["ExpPartCKOut"]
      """  Allow Express Part Checkout.  """  
      self.ConsPurchasingParent:str = obj["ConsPurchasingParent"]
      """  For internal use only.  Used with ConsolidatedPurchasingCompany to enforce security of the Consolidated Purchasing Parent company.  """  
      self.NewPoRelAtReceipt:bool = obj["NewPoRelAtReceipt"]
      """  Determines if a new PO release is created at receipt when the quantity received is less than the quantity shipped.  The new PO Rel quantity is the difference between the ship quantity and the receipt quantity.  """  
      self.CashGrpPfx:str = obj["CashGrpPfx"]
      """  Use when creating payment records from credit card payments automatically from Sales Order or from Customer Shipment  """  
      self.CCInvPfx:str = obj["CCInvPfx"]
      """  Invoice Group Prefix used for credit card groups  """  
      self.DefBankAcctID:str = obj["DefBankAcctID"]
      """  Bank Account code to be used when creating credit card payments  """  
      self.SkipLandedCostCalc:bool = obj["SkipLandedCostCalc"]
      """  Indicates whether or not Container Tracking is to calculate landed cost.  If yes, landed costs are calculated at the time the container is received.  The cubic sq feet of a container cannot be zero.  If no, landed costs are NOT calculated.  """  
      self.WebSaleGetsCommission:bool = obj["WebSaleGetsCommission"]
      """  Does a sale that originated via Customer Connect garner a Commission?  """  
      self.DefaultLabelsPrinter:str = obj["DefaultLabelsPrinter"]
      """  Default System Printer where labels are going to be sent if there is no Device available to print labels on the Current Station.  """  
      self.DefaultFormsPrinter:str = obj["DefaultFormsPrinter"]
      """  Default System Printer where forms are going to be sent if there is no Device available to print forms on the Current Station.  """  
      self.TxtLPP:int = obj["TxtLPP"]
      """   Number of lines per page for text report. This value will be written to SysRptLst.TxtLPP. The text based reports (Progress 4gl) generate a print image .txt file. This file contains new page controls characters. The Page size needs to be configurable to handle other paper sizes (ex: A4).
At this time we will allow for a page size setting to be established at the company level.  """  
      self.DefaultMiscFreightChargeCode:str = obj["DefaultMiscFreightChargeCode"]
      """  Default Miscellaneous Charges Freight Charge Code  """  
      self.PORelShipOption:str = obj["PORelShipOption"]
      """  Valid values = "None", "Short" and "Create".   At the time a container is shipped, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the shipping quantity and a new PO release is created for the difference between the original po release quantity and the ship quantity.  If this field is not set or None is selected than PO releases are not created nor are they shipped short.  This is an optional field.  """  
      self.UseTaxBoxes:bool = obj["UseTaxBoxes"]
      """  Flag to enable VAT taxboxes  """  
      self.GenRateGrp:str = obj["GenRateGrp"]
      """  Rate Group Code for General applications  """  
      self.SalesRateGrp:str = obj["SalesRateGrp"]
      """  Rate Group Code for Sales and A/R Invoicing  """  
      self.PORateGrp:str = obj["PORateGrp"]
      """  Currency Rate Group for Purchasing and A/P Invoicing  """  
      self.InvRateGrp:str = obj["InvRateGrp"]
      """  Currency Rate Group for Inventory applications  """  
      self.FARateGrp:str = obj["FARateGrp"]
      """  Currency Rate Group for Fixed Assets  """  
      self.PRRateGrp:str = obj["PRRateGrp"]
      """  Currency Rate Group for Payroll  """  
      self.CashRateGrp:str = obj["CashRateGrp"]
      """  Currency Rate Group for Cash transactions  """  
      self.RateLockType:str = obj["RateLockType"]
      """   F = Force 1:1 rate for same currencies
C = Use Conversion through base  """  
      self.UseTranDate:bool = obj["UseTranDate"]
      """  Indicates if FIFO Cost will be recorded based on Transaction Date or System Date.  By default the UseTranDate is false which means FIFO cost queue will use system date.  """  
      self.LotBatch:bool = obj["LotBatch"]
      """  Default for Part.LotBatch  """  
      self.LotMfgBatch:bool = obj["LotMfgBatch"]
      """  Default for Part.LotMfgBatch  """  
      self.LotMfgLot:bool = obj["LotMfgLot"]
      """  Default for Part.LotMfgLot  """  
      self.LotHeat:bool = obj["LotHeat"]
      """  Default for Part.LotHeat  """  
      self.LotFirmware:bool = obj["LotFirmware"]
      """  Default for Part.LotFirmware  """  
      self.LotBeforeDt:bool = obj["LotBeforeDt"]
      """  Default for Part.LotBeforeDt  """  
      self.LotMfgDt:bool = obj["LotMfgDt"]
      """  Default for Part.LotMfgDt  """  
      self.LotCureDt:bool = obj["LotCureDt"]
      """  Default for Part.LotCureDt  """  
      self.LotExpDt:bool = obj["LotExpDt"]
      """  Default for Part.LotExpDt  """  
      self.QtyDsplyDec:int = obj["QtyDsplyDec"]
      """  Controls the number of decimal places that the UI uses to display a "quantiity" field. This only controls the display, the actual number of decimals that can be entered is based on the Unit of Measure. (UomConv.NumOfDec)  """  
      self.PORelRcptOption:str = obj["PORelRcptOption"]
      """  Valid values = "Short" and "Create".   When the container arrives, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the arrived quantity and a new PO release is created for the difference between the original po release quantity and the arrived quantity.  This is an optional field.  """  
      self.AllowShipToChange:bool = obj["AllowShipToChange"]
      """  If true, then the shipto can be changed on the packing slip to a different shipto than on the Order Release. However, it can only be changed to one of the shipto's that are referenced on the order.  """  
      self.DefDisburseMethod:str = obj["DefDisburseMethod"]
      """  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume , Weight, Value, Quantity and Manual.  """  
      self.AllowSplitContainer:bool = obj["AllowSplitContainer"]
      """  Flag to indicate if container shipment lines can be split into another container shipment.  """  
      self.AllowTransferIndCost:bool = obj["AllowTransferIndCost"]
      """  Flag to indicate if Indirect Costs from one container shipment can be transferred to another.  """  
      self.AllowReceiptLC:bool = obj["AllowReceiptLC"]
      """  Flag to indicate if Landed Cost maintenance is allowed in Receipt Entry.  """  
      self.AllowLCAfterReceipt:bool = obj["AllowLCAfterReceipt"]
      """  Allow maintenance of Landed Cost after the part is received.  """  
      self.AllowUpdTransValue:bool = obj["AllowUpdTransValue"]
      """  Allow update of PO Transaction Value during Container Landed Cost Entry.  """  
      self.DisableLCUplift:bool = obj["DisableLCUplift"]
      """  Do not allow use of Uplift Percent during Landed Cost calculation.  """  
      self.EnableRoHS:bool = obj["EnableRoHS"]
      """  Allows entry of restriction types and substances in Part Master, Operation Master, ECO and Job Entry.  """  
      self.AllowDirectRollUp:bool = obj["AllowDirectRollUp"]
      """  Default value is false. When set to true then all indirect/direct roll-up radio buttons in Part Master and Job Entry should be enabled.  """  
      self.SyncSubstWeight:bool = obj["SyncSubstWeight"]
      """  Synchronize substance weight  """  
      self.StopAtFirstFailure:bool = obj["StopAtFirstFailure"]
      """  Indicates if the RoHS Compliance Process will stop at the first failure it founds.  """  
      self.OrderHistDays:int = obj["OrderHistDays"]
      """  Number of days to look back when processing Orders for the Build From Order History  """  
      self.AllowUpdSuppPrice:bool = obj["AllowUpdSuppPrice"]
      """  Indicates if user is allowed to update the Supplier Price for Receipt created by Purchase Order.  """  
      self.SuppPerctTolerance:int = obj["SuppPerctTolerance"]
      """  It is used to catch differences between updated Supplier Price for Receipt and PO Unit Price. If no value entered then do not perform percentage check.  """  
      self.SuppMonetaryTolerance:int = obj["SuppMonetaryTolerance"]
      """  It is used to catch differences between extended values of updated Supplier Price for Receipt and PO Unit Price. If no value entered then do not perform monetary check.  """  
      self.SuppPriceLimitAction:str = obj["SuppPriceLimitAction"]
      """  Receipt action to value of Supplier Price.  Valid values are "WARN" or "STOP".  WARN means that the user is given a warning, but allowed to proceed (or cancel) the Receipt with that Supplier Price.  STOP means that the Receipt line is not correct and the user should go to PO and update PO Unit Price to make receipt with mentioned price.  """  
      self.DefaultSlowMovingFmtCode:str = obj["DefaultSlowMovingFmtCode"]
      """  The default format code to be used on the Slow Moving Stock Provision report.  """  
      self.DefaultExcessFmtCode:str = obj["DefaultExcessFmtCode"]
      """  The default format code to be used on the Excess Stock Provision report.  """  
      self.CalcPSPrice:bool = obj["CalcPSPrice"]
      """  Indicates whether or not prices for transfer orders are calculated and printed on the packslip.  """  
      self.CalcPSTax:bool = obj["CalcPSTax"]
      """  Indicates whether or not taxes are calculated for a customer shipment and printed on the packslip.  """  
      self.RaisePOforCTP:bool = obj["RaisePOforCTP"]
      """  Flag that indicates if a PO should be created when confirm in CTP.  """  
      self.DefaultSORelease:str = obj["DefaultSORelease"]
      """  Setting at company level to define if the sales order releases will be created as Make Direct or Buy To Order. Sales order lines for non part master part must be BTO or Make direct.  """  
      self.EnablePI:bool = obj["EnablePI"]
      """  This would allow the user to receive non traditional payment information (such as post dated checks and bank drafts) and use it in calculating a customer's credit limit  """  
      self.APPurchType:bool = obj["APPurchType"]
      """  If box is checked, then the AP Invoice system will enable the APInvDtl.PurchCode field for European Financial postings  """  
      self.APDiscount:bool = obj["APDiscount"]
      """  Indicates that the discount amount by line needs to be captured to be sent to an external Financials package  """  
      self.AutoMatchAll:bool = obj["AutoMatchAll"]
      """  Flag to decide if the Match By Demand logic is applied to schedules in Demand Mass Review.  """  
      self.AllowShipOrdHold:bool = obj["AllowShipOrdHold"]
      """  Allow shipping orders on hold  """  
      self.ChkUnfirmSched:bool = obj["ChkUnfirmSched"]
      """  Check Unfirm Releasses Schedule  """  
      self.ChkForecastSched:bool = obj["ChkForecastSched"]
      """  Check Forcast Schedule  """  
      self.Localization:str = obj["Localization"]
      """  Localization Country  """  
      self.UseGUI:bool = obj["UseGUI"]
      """  Use Government Uniform Invoices. Taiwan localization flag.  """  
      self.UseTaxRate:bool = obj["UseTaxRate"]
      """  Indicates if taxes are calculated in a separate exchange rate  """  
      self.TaxRateGrp:str = obj["TaxRateGrp"]
      """  Currency Rate Group for Taxes  """  
      self.OCRCalcType:bool = obj["OCRCalcType"]
      """  OCR Calculation Type. Localization for Sweden, Finland and Estonia.  """  
      self.OCRNumDrivenFrom:str = obj["OCRNumDrivenFrom"]
      """  OCR number is derived from either the invoice number or a setting at the customer. Localization for Sweden, Finland and Estonia.  """  
      self.OCRLength:int = obj["OCRLength"]
      """  OCR length is the maximum length an OCR number is allowed to be. Localization setting for Sweden, Finland and Estonia.  """  
      self.UseAcctRef:bool = obj["UseAcctRef"]
      """  The flag to indicate if Account Reference number assigned to the customer should be used as Banking Reference on AR Invoice sent to the customer.  """  
      self.CSFLMWLcnNbr:str = obj["CSFLMWLcnNbr"]
      """   Malaysia Localization
LMW License Number  """  
      self.CSFCJ5LcnNbr:str = obj["CSFCJ5LcnNbr"]
      """   Malaysia Localization
CJ5 License Number  """  
      self.CSFCJ5FileNbr:str = obj["CSFCJ5FileNbr"]
      """   Malaysia Localization
CJ5 File Number  """  
      self.CancelSchedAction:str = obj["CancelSchedAction"]
      """  Field to choose between close or delete releases on SO when the demand is process  """  
      self.THTaxRecDocType:str = obj["THTaxRecDocType"]
      """  Document Type for Tax Receipt (Thailand Localization)  """  
      self.THWHTDocType:str = obj["THWHTDocType"]
      """  Withholding Tax Document Type (Thailand Localization)  """  
      self.GUISellerCityCode:str = obj["GUISellerCityCode"]
      """   Taiwan Localization
Seller City Code  """  
      self.ExpenseAutoSupplier:bool = obj["ExpenseAutoSupplier"]
      """  This field would be true if the system should automatically create a Supplier record for each Employee for processing Expenses.  """  
      self.ExpenseAutoSupplierPrefix:str = obj["ExpenseAutoSupplierPrefix"]
      """  If the system is setup to automatically create a Supplier record for each Employee for processing Expenses, this field will be the Prefix.  This value will prefix a numeric value and be used for the Supplier ID.  """  
      self.ExpenseRateGrp:str = obj["ExpenseRateGrp"]
      """  Rate Group Code for Employee Expenses  """  
      self.ExpenseVendorSeq:int = obj["ExpenseVendorSeq"]
      """  Internal sequence for automatic creation of vendors for employees.  """  
      self.ValidateBankBranchID:bool = obj["ValidateBankBranchID"]
      """  If the flag is false then users are allowed to enter  anything in the bank branch ID field in customer bank, supplier bank and BankAcct. The code will still try to do a lookup and retrieve the description of the bank branch ID.  """  
      self.ValidateBankIBAN:bool = obj["ValidateBankIBAN"]
      """  If the flag is false then users are allowed to enter anything in the bank IBAN (International Bank Account Number) field in customer bank, supplier bank and BankAcct.  If the flag is true, the checksum validation will be performed.  """  
      self.CTPSchedulingCode:str = obj["CTPSchedulingCode"]
      """  This is the default used when calculating CTP for multiple lines on an order.  If it is non-blank, then all the CTP jobs will be scheduled to complete at the same time.  It can be overridden at the time CTP is calculated.  """  
      self.ChgLogMethod:str = obj["ChgLogMethod"]
      """   Used as the collection method for creating Change Log records.
Possible values are: "D" -  Daily (Default Value), one record is created per day and everybody's changes are stored together.  "U" - User, one  record is created per day for each user.  """  
      self.ChiefAcctName:str = obj["ChiefAcctName"]
      """  Chief Accountant Name  """  
      self.ChiefAcctCellPhone:str = obj["ChiefAcctCellPhone"]
      """  Cheif Accountant Cell Phone Number  """  
      self.ChiefAcctEmail:str = obj["ChiefAcctEmail"]
      """  Cheif Accountant Email Address  """  
      self.TRBankCode:str = obj["TRBankCode"]
      """  Tax Return Bank Code  """  
      self.TRBankBranch:str = obj["TRBankBranch"]
      """  Tax Return Bank Branch  """  
      self.TRBankAcct:str = obj["TRBankAcct"]
      """  Tax Return Bank Account  """  
      self.TotalPayID:str = obj["TotalPayID"]
      """  ID number for consolidation.  """  
      self.TaxOfficeCode:str = obj["TaxOfficeCode"]
      """  Tax Office Code  """  
      self.TaxAgentName:str = obj["TaxAgentName"]
      """  Tax Agent Name  """  
      self.TaxAgentPhone:str = obj["TaxAgentPhone"]
      """  Tax Agent Phone  """  
      self.TaxAgentTaxRegNo:str = obj["TaxAgentTaxRegNo"]
      """  Tax Agent Tax Region Number  """  
      self.EDIOutboundAs:str = obj["EDIOutboundAs"]
      """  Defines the format In which the EDI Outbound Documents will be sent to output.  """  
      self.HDDefWFGroupID:str = obj["HDDefWFGroupID"]
      """  Company default Workflow Group. Used to assign to cases.  """  
      self.StartVendAuditRefID:int = obj["StartVendAuditRefID"]
      """  Starting supplier reference ID number  """  
      self.IsDiscountforDebitM:bool = obj["IsDiscountforDebitM"]
      """  IsDiscountforDebitM  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.THBranchID:str = obj["THBranchID"]
      """  THBranchID  """  
      self.UseInvRateDefTax:bool = obj["UseInvRateDefTax"]
      """  UseInvRateDefTax  """  
      self.AllowLinkedPOChg:bool = obj["AllowLinkedPOChg"]
      """  Allow changes to be made to POs that are linked to Intercompany Sales Orders  """  
      self.ConsiderWorkingDays:bool = obj["ConsiderWorkingDays"]
      """  Consider Working Days in the Delivery Days Calculation  """  
      self.DeferTaxExchRate:int = obj["DeferTaxExchRate"]
      """  DeferTaxExchRate  """  
      self.PmtTaxUseDate:int = obj["PmtTaxUseDate"]
      """  PmtTaxUseDate  """  
      self.CNAccEntityName:str = obj["CNAccEntityName"]
      """  CNAccEntityName  """  
      self.CNAccountStructure:str = obj["CNAccountStructure"]
      """  CNAccountStructure  """  
      self.CNAttachment:str = obj["CNAttachment"]
      """  CNAttachment  """  
      self.CNBaseCurrency:str = obj["CNBaseCurrency"]
      """  CNBaseCurrency  """  
      self.CNCashier:str = obj["CNCashier"]
      """  CNCashier  """  
      self.CNCFICodeCurGainLoss:str = obj["CNCFICodeCurGainLoss"]
      """  CNCFICodeCurGainLoss  """  
      self.CNChecker:str = obj["CNChecker"]
      """  CNChecker  """  
      self.CNCompType:str = obj["CNCompType"]
      """  CNCompType  """  
      self.CNDisableEntryRules:bool = obj["CNDisableEntryRules"]
      """  CNDisableEntryRules  """  
      self.CNExportPath:str = obj["CNExportPath"]
      """  CNExportPath  """  
      self.CNGroupName:str = obj["CNGroupName"]
      """  CNGroupName  """  
      self.CNGTICollector:str = obj["CNGTICollector"]
      """  CNGTICollector  """  
      self.CNGTICommTaxCode:str = obj["CNGTICommTaxCode"]
      """  CNGTICommTaxCode  """  
      self.CNGTIDefCCFlag:bool = obj["CNGTIDefCCFlag"]
      """  CNGTIDefCCFlag  """  
      self.CNGTIDefINFlag:bool = obj["CNGTIDefINFlag"]
      """  CNGTIDefINFlag  """  
      self.CNGTIDefPath:str = obj["CNGTIDefPath"]
      """  CNGTIDefPath  """  
      self.CNGTIDefPOFlag:bool = obj["CNGTIDefPOFlag"]
      """  CNGTIDefPOFlag  """  
      self.CNGTIDefPTFlag:bool = obj["CNGTIDefPTFlag"]
      """  CNGTIDefPTFlag  """  
      self.CNGTIDefSMFlag:bool = obj["CNGTIDefSMFlag"]
      """  CNGTIDefSMFlag  """  
      self.CNGTIDefSOFlag:bool = obj["CNGTIDefSOFlag"]
      """  CNGTIDefSOFlag  """  
      self.CNGTIManager:str = obj["CNGTIManager"]
      """  CNGTIManager  """  
      self.CNGTIVATCode:str = obj["CNGTIVATCode"]
      """  CNGTIVATCode  """  
      self.CNGTIVATInvLimit:int = obj["CNGTIVATInvLimit"]
      """  CNGTIVATInvLimit  """  
      self.CNGTIVATInvLineLimit:int = obj["CNGTIVATInvLineLimit"]
      """  CNGTIVATInvLineLimit  """  
      self.CNIndustry:str = obj["CNIndustry"]
      """  CNIndustry  """  
      self.CNIndustryCode:str = obj["CNIndustryCode"]
      """  CNIndustryCode  """  
      self.CNKeeper:str = obj["CNKeeper"]
      """  CNKeeper  """  
      self.CNMaker:str = obj["CNMaker"]
      """  CNMaker  """  
      self.CNOrgCode:str = obj["CNOrgCode"]
      """  CNOrgCode  """  
      self.CNRegionCode:str = obj["CNRegionCode"]
      """  CNRegionCode  """  
      self.JPFiscalCalendarID:str = obj["JPFiscalCalendarID"]
      """  JPFiscalCalendarID  """  
      self.TWGUICalendarID:str = obj["TWGUICalendarID"]
      """  TWGUICalendarID  """  
      self.ValidateTaxID:bool = obj["ValidateTaxID"]
      """  If the flag is false then users are allowed to enter anything in the Tax ID field in customer and supplier.  If the flag is true, the validation will be performed.  """  
      self.MXDebugMode:bool = obj["MXDebugMode"]
      """  MXDebugMode  """  
      self.MXDocType:str = obj["MXDocType"]
      """  MXDocType  """  
      self.MXIEPSTaxType:str = obj["MXIEPSTaxType"]
      """  MXIEPSTaxType. Obsolete, SalesTax.MXTaxType used instead  """  
      self.MXISRTaxType:str = obj["MXISRTaxType"]
      """  MXISRTaxType. Obsolete, SalesTax.MXTaxType used instead  """  
      self.MXIVATaxType:str = obj["MXIVATaxType"]
      """  MXIVATaxType. Obsolete, SalesTax.MXTaxType used instead  """  
      self.MXPACCode:str = obj["MXPACCode"]
      """  MXPACCode  """  
      self.MXTaxRcptEFT:int = obj["MXTaxRcptEFT"]
      """  MXTaxRcptEFT  """  
      self.MXTaxRcptType:str = obj["MXTaxRcptType"]
      """  MXTaxRcptType  """  
      self.MXThumbprint:str = obj["MXThumbprint"]
      """  MXThumbprint  """  
      self.MXUseExpedidoEn:bool = obj["MXUseExpedidoEn"]
      """  MXUseExpedidoEn  """  
      self.MXValidFrom:str = obj["MXValidFrom"]
      """  MXValidFrom  """  
      self.MXValidTo:str = obj["MXValidTo"]
      """  MXValidTo  """  
      self.OCRCalcAlg:str = obj["OCRCalcAlg"]
      """  OCRCalcAlg  """  
      self.NOThresholdAmt:int = obj["NOThresholdAmt"]
      """  NOThresholdAmt  """  
      self.EAddress:str = obj["EAddress"]
      """  EAddress  """  
      self.EInvOutputDir:str = obj["EInvOutputDir"]
      """  EInvOutputDir  """  
      self.EInvImpFileLocation:str = obj["EInvImpFileLocation"]
      """  EInvImpFileLocation  """  
      self.EInvImpArchiveFileLocation:str = obj["EInvImpArchiveFileLocation"]
      """  EInvImpArchiveFileLocation  """  
      self.EInvImpSelectionMethod:str = obj["EInvImpSelectionMethod"]
      """  EInvImpSelectionMethod  """  
      self.DefaultLineTaxable:bool = obj["DefaultLineTaxable"]
      """  DefaultLineTaxable  """  
      self.PEBOEPaymentMethod:int = obj["PEBOEPaymentMethod"]
      """  Bill of Exchange Payment Method  """  
      self.PEBOEPortfolioStatus:str = obj["PEBOEPortfolioStatus"]
      """  Bill of Exchange Portfolio Status  """  
      self.AsyncShip:bool = obj["AsyncShip"]
      """  AsyncShip  """  
      self.OverridePriceListPrompt:bool = obj["OverridePriceListPrompt"]
      """  Within PO Entry when modifying unit price which was derived from a supplier price list, prompt the user to confirm.  """  
      self.DisableOverridePriceListOption:bool = obj["DisableOverridePriceListOption"]
      """  Disable Override Price List option with PO Entry  """  
      self.DEBundesbankCompanyID:str = obj["DEBundesbankCompanyID"]
      """  DEBundesbankCompanyID  """  
      self.DEZ4ExportPath:str = obj["DEZ4ExportPath"]
      """  DEZ4ExportPath  """  
      self.UseLastWhseBin:bool = obj["UseLastWhseBin"]
      """  Defaults the Warehouse and Bin in Receipt to the last used for the current Part and Pack Slip  """  
      self.POQtyOption:str = obj["POQtyOption"]
      """  Indicates what Qty Option will be defaulted for new PO lines. Options are "Our" and "Supplier".  """  
      self.ReceiptQtyOption:str = obj["ReceiptQtyOption"]
      """  Indicates what Qty Option will be defaulted for new Receipt lines. Options are "Our" and "Supplier".  """  
      self.CNGTILangID:str = obj["CNGTILangID"]
      """  CNGTILangID  """  
      self.CloseReleaseAt:str = obj["CloseReleaseAt"]
      """  Defines the point at which the PO Releases will be closed. Available options are 'Arrival', 'Receipt', or 'Invoice'.  """  
      self.SubRateGrp:str = obj["SubRateGrp"]
      """  SubRateGrp  """  
      self.StopOnUOMNoRound:bool = obj["StopOnUOMNoRound"]
      """  If true and the UOM is set to no rounding and the number of decimals is exceeded, you will get an error. Otherwise the value will be truncated (same as round down currently behaves).  """  
      self.MYIndustryCode1:str = obj["MYIndustryCode1"]
      """  MYIndustryCode1  """  
      self.MYIndustryCode2:str = obj["MYIndustryCode2"]
      """  MYIndustryCode2  """  
      self.MYIndustryCode3:str = obj["MYIndustryCode3"]
      """  MYIndustryCode3  """  
      self.MYIndustryCode4:str = obj["MYIndustryCode4"]
      """  MYIndustryCode4  """  
      self.MYIndustryCode5:str = obj["MYIndustryCode5"]
      """  MYIndustryCode5  """  
      self.PEDocumentID:str = obj["PEDocumentID"]
      """  PE Document ID  """  
      self.PEIdentityDocType:str = obj["PEIdentityDocType"]
      """  PE Identity Document Type  """  
      self.CNOurBank:str = obj["CNOurBank"]
      """  CNOurBank  """  
      self.JobLotDflt:bool = obj["JobLotDflt"]
      """  JobLotDflt  """  
      self.LACTaxCalcEnabled:bool = obj["LACTaxCalcEnabled"]
      """  LACTaxCalcEnabled  """  
      self.TWGUIRegNum:str = obj["TWGUIRegNum"]
      """  TW GUI Code  """  
      self.NLMessageRefSupplierICP:str = obj["NLMessageRefSupplierICP"]
      """  NLMessageRefSupplierICP  """  
      self.NLDigipoortDeliveryURL:str = obj["NLDigipoortDeliveryURL"]
      """  NLDigipoortDeliveryURL  """  
      self.NLDigipoortStatusURL:str = obj["NLDigipoortStatusURL"]
      """  NLDigipoortStatusURL  """  
      self.NLDigipoortServerThumbprint:str = obj["NLDigipoortServerThumbprint"]
      """  NLDigipoortServerThumbprint  """  
      self.NLDigipoortClientThumbprint:str = obj["NLDigipoortClientThumbprint"]
      """  NLDigipoortClientThumbprint  """  
      self.CNGTIEncodingFormat:int = obj["CNGTIEncodingFormat"]
      """  Encoding for GTI Export file  """  
      self.POTaxReadyToProcess:bool = obj["POTaxReadyToProcess"]
      """  Flag to determine whether PO taxes will be automatically calculated each time a PO line is updated.  """  
      self.POTaxCalculate:bool = obj["POTaxCalculate"]
      """  Flag to determine whether PO taxes will be calculated.  """  
      self.PEAddressID:str = obj["PEAddressID"]
      """  PEAddressID  """  
      self.X509Code:str = obj["X509Code"]
      """  X509Code  """  
      self.COIFRSInterestRate:int = obj["COIFRSInterestRate"]
      """  COIFRSInterestRate  """  
      self.MXCURP:str = obj["MXCURP"]
      """  MXCURP  """  
      self.APTaxLnLevel:bool = obj["APTaxLnLevel"]
      """  This flag will be used to determine if taxes are calculated for AP Invoices at Document Level (Default, False) or at Line Level (True).  """  
      self.MYLMWLcnPurchaseExpDate:str = obj["MYLMWLcnPurchaseExpDate"]
      """  MYLMWLcnPurchaseExpDate  """  
      self.MYLMWPurchaseAddr:str = obj["MYLMWPurchaseAddr"]
      """  MYLMWPurchaseAddr  """  
      self.MYLMWLcnManufacturing:str = obj["MYLMWLcnManufacturing"]
      """  MYLMWLcnManufacturing  """  
      self.MYLMWLcnManufacturingExpDate:str = obj["MYLMWLcnManufacturingExpDate"]
      """  MYLMWLcnManufacturingExpDate  """  
      self.MYLMWManufacturingAddr:str = obj["MYLMWManufacturingAddr"]
      """  MYLMWManufacturingAddr  """  
      self.ReceiptTaxCalculate:bool = obj["ReceiptTaxCalculate"]
      """  Flag to determine whether Receipt taxes will be calculated.  """  
      self.CalcQuoteTax:bool = obj["CalcQuoteTax"]
      """  Flag to determine whether Quote taxes will be calculated.  """  
      self.AttBatch:str = obj["AttBatch"]
      """  Indicates if entry of a BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttMfgBatch:str = obj["AttMfgBatch"]
      """  Indicates if entry of a MFG BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttMfgLot:str = obj["AttMfgLot"]
      """  Indicates if entry of a MFG Lot is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttHeat:str = obj["AttHeat"]
      """  Indicates if entry of a Heat Number  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttFirmware:str = obj["AttFirmware"]
      """  Indicates if entry of FIRMWARE is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttBeforeDt:str = obj["AttBeforeDt"]
      """  Indicates if entry of a Best Before Date is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttMfgDt:str = obj["AttMfgDt"]
      """  Indicates if entry of a Original Manufacture Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttCureDt:str = obj["AttCureDt"]
      """  Indicates if entry of a CURE DATE  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.AttExpDt:str = obj["AttExpDt"]
      """  Indicates if entry of an Expiration Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.PLTaxOfficeCode:str = obj["PLTaxOfficeCode"]
      """  PLTaxOfficeCode  """  
      self.PLRegionCode:str = obj["PLRegionCode"]
      """  PLRegionCode  """  
      self.PLProvince:str = obj["PLProvince"]
      """  PLProvince  """  
      self.PLDistrict:str = obj["PLDistrict"]
      """  PLDistrict  """  
      self.PLCommunity:str = obj["PLCommunity"]
      """  PLCommunity  """  
      self.PLBuildingNum:str = obj["PLBuildingNum"]
      """  PLBuildingNum  """  
      self.PLRoomNum:str = obj["PLRoomNum"]
      """  PLRoomNum  """  
      self.PLPostOffice:str = obj["PLPostOffice"]
      """  PLPostOffice  """  
      self.INPrevYearTurnover:int = obj["INPrevYearTurnover"]
      """  Turnover in Previous Fiscal Year  """  
      self.DeferManualEntry:bool = obj["DeferManualEntry"]
      """  DeferManualEntry  """  
      self.DeferPurchaseReceipt:bool = obj["DeferPurchaseReceipt"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Container Receipt, Receipt Entry.  """  
      self.DeferJobReceipt:bool = obj["DeferJobReceipt"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Job Receipt to Job, Job Receipt to Salvage, Job Receipt to Inventory, Kanban Receipts.  """  
      self.DeferInspection:bool = obj["DeferInspection"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Inspection Processing.  """  
      self.DeferQtyAdjustment:bool = obj["DeferQtyAdjustment"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Quantity Adjustment.  """  
      self.DeferInventoryMove:bool = obj["DeferInventoryMove"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Inventory Transfer.  """  
      self.DeferShipments:bool = obj["DeferShipments"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Customer Shipment Entry, Subcontractor Shipment Entry, Drop Shipment Entry, Order Entry.  """  
      self.DeferInventoryCounts:bool = obj["DeferInventoryCounts"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Count Tag Entry.  """  
      self.DeferAssetDisposal:bool = obj["DeferAssetDisposal"]
      """  DeferAssetDisposal  """  
      self.DeferReturnMaterials:bool = obj["DeferReturnMaterials"]
      """  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: RMA Processing.  """  
      self.AllowEmpWithoutResource:bool = obj["AllowEmpWithoutResource"]
      """  Flag to indicate if it is allowed to create employees with Group resource, without a resource defined.  """  
      self.INSingleTaxCatTypeSO:bool = obj["INSingleTaxCatTypeSO"]
      """  INSingleTaxCatTypeSO  """  
      self.INSingleTaxCatTypePO:bool = obj["INSingleTaxCatTypePO"]
      """  INSingleTaxCatTypePO  """  
      self.BusinessCatID:str = obj["BusinessCatID"]
      """  BusinessCatID  """  
      self.ReceiptIncludeDutyInTax:bool = obj["ReceiptIncludeDutyInTax"]
      """  Flag to determine whether Duty will be included on Taxable amount  """  
      self.INAllowChangingPP:bool = obj["INAllowChangingPP"]
      """  INAllowChangingPP  """  
      self.NLFiscalUnityTaxID:str = obj["NLFiscalUnityTaxID"]
      """  Fiscal Unity Tax ID (CSF Netherlands)  """  
      self.FSACashGrpPfx:str = obj["FSACashGrpPfx"]
      """  Prefix for incoming FSA records. To be used to create Cash Receipt groups.  """  
      self.FSAARInvGrpPfx:str = obj["FSAARInvGrpPfx"]
      """  Prefix for incoming FSA records. To be used to create AR Invoice groups.  """  
      self.FSASendARInvToPosting:bool = obj["FSASendARInvToPosting"]
      """  Indicates if inbound AR Invoices are sent to posting when received from FSA.  """  
      self.FSAInvQtyAdjustmentReasonCode:str = obj["FSAInvQtyAdjustmentReasonCode"]
      """  Reason Code to be used for inbound inventory quantity adjustments received from Epicor FSA.  """  
      self.MXLocality:str = obj["MXLocality"]
      """  MXLocality  """  
      self.MXMunicipioCode:str = obj["MXMunicipioCode"]
      """  MXMunicipioCode  """  
      self.RevaluationAR:str = obj["RevaluationAR"]
      """  RevaluationAR  """  
      self.RevaluationAP:str = obj["RevaluationAP"]
      """  RevaluationAP  """  
      self.RevaluationBA:str = obj["RevaluationBA"]
      """  RevaluationBA  """  
      self.RevaluationPCD:str = obj["RevaluationPCD"]
      """  RevaluationPCD  """  
      self.GenerateDigitalSignature:bool = obj["GenerateDigitalSignature"]
      """  GenerateDigitalSignature  """  
      self.UseCopyNumInPackSlips:bool = obj["UseCopyNumInPackSlips"]
      """  UseCopyNumInPackSlips  """  
      self.EWConfiguratorURL:str = obj["EWConfiguratorURL"]
      """  This is the location of the the EWC generator.  """  
      self.NLDigipoortServerCertID:str = obj["NLDigipoortServerCertID"]
      """  NLDigipoortServerCertID  """  
      self.NLDigipoortClientCertID:str = obj["NLDigipoortClientCertID"]
      """  NLDigipoortClientCertID  """  
      self.UnapprovedPO:str = obj["UnapprovedPO"]
      """  UnapprovedPO  """  
      self.UnconfirmedPO:str = obj["UnconfirmedPO"]
      """  UnconfirmedPO  """  
      self.FSAShipViaCode:str = obj["FSAShipViaCode"]
      """  Default Ship Via Code for return shipments of RMAs for FSA related transactions  """  
      self.FSARMAReasonCode:str = obj["FSARMAReasonCode"]
      """  Default reason code for RMAs from FSA  """  
      self.FSAExpensePMUID:int = obj["FSAExpensePMUID"]
      """  Default payment method for expenses from FSA  """  
      self.APPrepayTaxCalc:bool = obj["APPrepayTaxCalc"]
      """  APPrepayTaxCalc  """  
      self.PLWasteRegisterNum:str = obj["PLWasteRegisterNum"]
      """  Waste Register Number (CSF Poland)  """  
      self.EWCRuntimeURL:str = obj["EWCRuntimeURL"]
      """  This is the location of the EWC Runtime.  """  
      self.AGAFIPResponsibilityCode:str = obj["AGAFIPResponsibilityCode"]
      """  AGAFIPResponsibilityCode  """  
      self.EInvCompanyIDAttr:str = obj["EInvCompanyIDAttr"]
      """  E-Invoice CompanyID Attribute  """  
      self.EInvEndpointIDAttr:str = obj["EInvEndpointIDAttr"]
      """  E-Invoice EndpointID Attribute  """  
      self.PriceToleranceOnHigherPrice:bool = obj["PriceToleranceOnHigherPrice"]
      """  PriceToleranceOnHigherPrice  """  
      self.QuickShipURL:str = obj["QuickShipURL"]
      """  URL address to the Quick Ship application  """  
      self.QSUseIntl:bool = obj["QSUseIntl"]
      """  Indicates if Quick Ship International Shipments are used.  """  
      self.QSUseBOL:bool = obj["QSUseBOL"]
      """  Indicates if Quick Ship Bill of Lading  is used.  """  
      self.QSUseCO:bool = obj["QSUseCO"]
      """  Reserved for Future Development  """  
      self.CNGTIAdminGroup:str = obj["CNGTIAdminGroup"]
      """  Stores the name of the admin group referring to the security group maintenance.  """  
      self.CNCheckerSearchSeq:int = obj["CNCheckerSearchSeq"]
      """  Define the search sequence  """  
      self.CNMakerSearchSeq:int = obj["CNMakerSearchSeq"]
      """  Define the search sequence  """  
      self.SalesTaxID:str = obj["SalesTaxID"]
      """  SalesTaxID  """  
      self.ServiceTaxID:str = obj["ServiceTaxID"]
      """  ServiceTaxID  """  
      self.ELIEinvoice:bool = obj["ELIEinvoice"]
      """  ELIEinvoice  """  
      self.ELIDefReportID:str = obj["ELIDefReportID"]
      """  ELIDefReportID  """  
      self.ELIDefStyleNum:int = obj["ELIDefStyleNum"]
      """  ELIDefStyleNum  """  
      self.ELIDefToMail:str = obj["ELIDefToMail"]
      """  ELIDefToMail  """  
      self.ELIDefCCMail:str = obj["ELIDefCCMail"]
      """  ELIDefCCMail  """  
      self.ELIDefMailTempID:str = obj["ELIDefMailTempID"]
      """  ELIDefMailTempID  """  
      self.ELIDefEinvoicePath:str = obj["ELIDefEinvoicePath"]
      """  ELIDefEinvoicePath  """  
      self.ELIDefDepTranDocTypeID:str = obj["ELIDefDepTranDocTypeID"]
      """  ELIDefDepTranDocTypeID  """  
      self.PLEnableRcvDateWarning:bool = obj["PLEnableRcvDateWarning"]
      """  Enable Received Date Warning (CSF Poland)  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """  COOneTimeID  """  
      self.COFiscalResp1:str = obj["COFiscalResp1"]
      """  COFiscalResp1  """  
      self.COFiscalResp2:str = obj["COFiscalResp2"]
      """  COFiscalResp2  """  
      self.COFiscalResp3:str = obj["COFiscalResp3"]
      """  COFiscalResp3  """  
      self.CNWeightUOMClass:str = obj["CNWeightUOMClass"]
      """  Weight UOM Class  """  
      self.EORINumber:str = obj["EORINumber"]
      """  EORI Number  """  
      self.EnableNetting:bool = obj["EnableNetting"]
      """  Enable Netting Transaction Entry  """  
      self.WithholdAcctToInterim:bool = obj["WithholdAcctToInterim"]
      """  This field indicates that posting of withholding taxes will go through interim accounts when tax timing is partially paid or fully paid.  """  
      self.ELIDefFromMail:str = obj["ELIDefFromMail"]
      """  ELIDefFromMail  """  
      self.NetTranDocTypeIDCM:str = obj["NetTranDocTypeIDCM"]
      """  This transaction document type will be the one assigned for the netting credit memo created.  """  
      self.NetTranDocTypeIDDM:str = obj["NetTranDocTypeIDDM"]
      """  Description: This transaction document type will be the one assigned for the netting debit memo created  """  
      self.TWTaxDeclarationAdminGroup:str = obj["TWTaxDeclarationAdminGroup"]
      """  Security Group to be used as Tax Declaration Admins  """  
      self.TaxValidationAllow:bool = obj["TaxValidationAllow"]
      """  Enables/disables Tax Id validation.  """  
      self.TaxValidationEFTHeadUID:int = obj["TaxValidationEFTHeadUID"]
      """  Electronic Interface of type Tax Id Validation  """  
      self.TaxValidationAutomatic:bool = obj["TaxValidationAutomatic"]
      """  Enables/disables automatic Tax Id validation when customer or supplier Tax Id is changed.  """  
      self.TaxValidationAction:int = obj["TaxValidationAction"]
      """  Action if Invalid Tax ID  """  
      self.RevaluationBAUnrealized:bool = obj["RevaluationBAUnrealized"]
      """  RevaluationBAUnrealized  """  
      self.RevaluationPCDUnrealized:bool = obj["RevaluationPCDUnrealized"]
      """  RevaluationPCDUnrealized  """  
      self.HMRCTaxValidationAllow:bool = obj["HMRCTaxValidationAllow"]
      """  HMRCTaxValidationAllow  """  
      self.HMRCTaxValidationURL:str = obj["HMRCTaxValidationURL"]
      """  HMRCTaxValidationURL  """  
      self.HMRCTaxValidationAutomatic:bool = obj["HMRCTaxValidationAutomatic"]
      """  HMRCTaxValidationAutomatic  """  
      self.HMRCTaxValidationAction:int = obj["HMRCTaxValidationAction"]
      """  HMRCTaxValidationAction  """  
      self.AttISOrigCountry:str = obj["AttISOrigCountry"]
      """  Indicates if entry of a County of Origin is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  """  
      self.ExternalSchemeID:str = obj["ExternalSchemeID"]
      """  Company Scheme ID  """  
      self.ExternalID:str = obj["ExternalID"]
      """  Company ID  """  
      self.SiteIsLegalEntity:bool = obj["SiteIsLegalEntity"]
      """  Indicates site can be used as a legal entity.  """  
      self.MYTaxRateByKg:str = obj["MYTaxRateByKg"]
      """  Tax Rate by Kg  """  
      self.MYTaxRateByLiter:str = obj["MYTaxRateByLiter"]
      """  Tax Rate by Liter  """  
      self.TWEncryptionKey:str = obj["TWEncryptionKey"]
      """  Encryption Key  """  
      self.ELIOperatorCode:str = obj["ELIOperatorCode"]
      """  EInvoice Operator Code  """  
      self.CurrExDiff:int = obj["CurrExDiff"]
      """  Indicates the logic used to calculate the base/rpt fields.  Currently used by Bank Funds Transfer  """  
      self.ERSDocTypeID:str = obj["ERSDocTypeID"]
      """  The document type used to generate the legal number for the invoices generated automatically at the shipment.  """  
      self.ERSInvGrpPrefix:str = obj["ERSInvGrpPrefix"]
      """  The group prefix used to generated the invoice group for the invoice generated automatically by the system when shipping an ERS PO.  """  
      self.InboundPath:str = obj["InboundPath"]
      """  Default Path where the files will be stored to be read by the Import EDI Process.  """  
      self.ELIERSDocTypeID:str = obj["ELIERSDocTypeID"]
      """  ELIERSDocTypeID  """  
      self.ELISendMail:bool = obj["ELISendMail"]
      """  ELISendMail  """  
      self.ELISendingOption:int = obj["ELISendingOption"]
      """  ELISendingOption  """  
      self.PlasticTaxUOMCode:str = obj["PlasticTaxUOMCode"]
      """  PlasticTaxUOMCode  """  
      self.PlasticTaxRate:int = obj["PlasticTaxRate"]
      """  PlasticTaxRate  """  
      self.CNQuantityControl:int = obj["CNQuantityControl"]
      """  CNQuantityControl  """  
      self.QuickShipRegCode:str = obj["QuickShipRegCode"]
      """  QuickShip Registration Code  """  
      self.QuickShipAPIURL:str = obj["QuickShipAPIURL"]
      """  URL address to the Quick Ship API  """  
      self.QuickShipUserID:str = obj["QuickShipUserID"]
      """  Quick Ship User Name  """  
      self.QuickShipPassword:str = obj["QuickShipPassword"]
      """  Quick Ship Password  """  
      self.CNBondedWhseControl:int = obj["CNBondedWhseControl"]
      """  CNBondedWhseControl  """  
      self.FreightSvcInt:str = obj["FreightSvcInt"]
      """  Freight Service Integration Selection. (AI - REST API Integration, QW - Quick Ship Web Services)  """  
      self.BaseUOMClassID:str = obj["BaseUOMClassID"]
      """  BaseUOMClassID  """  
      self.AutoLockFinGroups:bool = obj["AutoLockFinGroups"]
      """  Indicates financial groups are automatically locked on selection or creation  """  
      self.KBMaxDocTypeID:str = obj["KBMaxDocTypeID"]
      """  Controls where Attachments are place when CPQ pushes them to Kinetic.  The selected Document Type must be of Server Transfer Type.  If the selected Document Type is Reserved for Specific Tables, the Document Type Control must include the following tables: OrderDtl, QuoteAsm, QuoteDtl, JobAsmbl, JobHead.  If no Document Type is selected, the CPQ Quote Sync will be the master and pull attachments from CPQ and if there is a value CPQ Quote Sync will not run.  """  
      self.ELIRcptDefStyleNum:int = obj["ELIRcptDefStyleNum"]
      """  Default E-invoice Report Style  """  
      self.CNCFICodeDescription:str = obj["CNCFICodeDescription"]
      self.CNCOACode:str = obj["CNCOACode"]
      """  CSF China - dynamic field for calculating of the XBSyst.CNCFICodeCurGainLoss field.  """  
      self.EInvWSURL:str = obj["EInvWSURL"]
      """  Web-Service URL for E-Invoice.  """  
      self.EnableOCRCalcType:bool = obj["EnableOCRCalcType"]
      self.EnableReverse:bool = obj["EnableReverse"]
      """   If this flag is true then on Currency Revaluation screen the Reverse checkbox is enabled.
If this flag is false then on Currency Revaluaion screen Reverse checkbox is Read Only and set to true.  """  
      self.IsDiscountforCreditM:bool = obj["IsDiscountforCreditM"]
      """  Enable calculation of settlement discounts for credit memos in AR  """  
      self.JPFiscalCalDescription:str = obj["JPFiscalCalDescription"]
      self.PECollectionAgent:bool = obj["PECollectionAgent"]
      """  Peru Collection Agent withholding status  """  
      self.PEGoodsContributor:bool = obj["PEGoodsContributor"]
      """  Peru Goods Contributor withholding status  """  
      self.PENoAddress:bool = obj["PENoAddress"]
      """  Peru No Address Provided withholding status  """  
      self.PENotFound:bool = obj["PENotFound"]
      """  Peru Not Found withholding status.  """  
      self.PEWithholdAgent:bool = obj["PEWithholdAgent"]
      """  Peru Withholding Agent withholding status  """  
      self.PORelShipOptDisplay:str = obj["PORelShipOptDisplay"]
      """  Display used to for PORelShipOption  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.TWEncryptionKeyInput:str = obj["TWEncryptionKeyInput"]
      """  The field for user to input Company Encryption Key  """  
      self.CNSegmentNbr:int = obj["CNSegmentNbr"]
      """  CSF China - dynamic field for calculating of the XBSyst.CNCFICodeCurGainLoss field.  """  
      self.CurrencyExchangeDiff:str = obj["CurrencyExchangeDiff"]
      """  Currency Exchange Difference  """  
      self.OneEDIAPIUrl:str = obj["OneEDIAPIUrl"]
      """  URL of the OneEDI API Endpoint to post the demand outbound to  """  
      self.OneEDIAPIClientId:str = obj["OneEDIAPIClientId"]
      """  Client Id required to access OneEDI API  """  
      self.OneEDIAPIClientSecret:str = obj["OneEDIAPIClientSecret"]
      """  Client Secret required to access OneEDI API  """  
      self.KBMaxUrl:str = obj["KBMaxUrl"]
      """  CPQ Instance URL.  """  
      self.KBMaxUsername:str = obj["KBMaxUsername"]
      """  CPQ Username used for communication.  """  
      self.KBMaxPassword:str = obj["KBMaxPassword"]
      """  CPQ password used for communication.  """  
      self.KBMaxSqlInstance:str = obj["KBMaxSqlInstance"]
      """  CPQ SQL Instance for syncing data between Kinetic and CPQ.  """  
      self.KBMaxSqlDatabase:str = obj["KBMaxSqlDatabase"]
      self.KBMaxSqlUsername:str = obj["KBMaxSqlUsername"]
      self.KBMaxSqlPassword:str = obj["KBMaxSqlPassword"]
      self.InactivateSiteSegments:bool = obj["InactivateSiteSegments"]
      """  Indicates if site segements should be inactivated.  """  
      self.EDISupplierEnable:bool = obj["EDISupplierEnable"]
      self.BitFlag:int = obj["BitFlag"]
      self.BankBankName:str = obj["BankBankName"]
      self.BankDescription:str = obj["BankDescription"]
      self.CNOurBankBankAcctDescription:str = obj["CNOurBankBankAcctDescription"]
      self.CNOurBankBankAcctBankName:str = obj["CNOurBankBankAcctBankName"]
      self.CurrCashRateGrpDescription:str = obj["CurrCashRateGrpDescription"]
      self.CurrExpenseRateGrpDescription:str = obj["CurrExpenseRateGrpDescription"]
      self.CurrFARateGrpDescription:str = obj["CurrFARateGrpDescription"]
      self.CurrGenRateGrpDescription:str = obj["CurrGenRateGrpDescription"]
      self.CurrInvRateGrpDescription:str = obj["CurrInvRateGrpDescription"]
      self.CurrPORateGrpDescription:str = obj["CurrPORateGrpDescription"]
      self.CurrPRRateGrpDescription:str = obj["CurrPRRateGrpDescription"]
      self.CurrSalesRateGrpDescription:str = obj["CurrSalesRateGrpDescription"]
      self.CurrSubRateGrpDescription:str = obj["CurrSubRateGrpDescription"]
      self.CurrTaxRateGrpDescription:str = obj["CurrTaxRateGrpDescription"]
      self.FSAExpensePMUIDType:int = obj["FSAExpensePMUIDType"]
      self.FSAExpensePMUIDName:str = obj["FSAExpensePMUIDName"]
      self.FSAExpensePMUIDSummarizePerCustomer:bool = obj["FSAExpensePMUIDSummarizePerCustomer"]
      self.FSARMAReasonCodeDescription:str = obj["FSARMAReasonCodeDescription"]
      self.FSAShipViaCodeDescription:str = obj["FSAShipViaCodeDescription"]
      self.FSAShipViaCodeWebDesc:str = obj["FSAShipViaCodeWebDesc"]
      self.GlobalCurrencyDocumentDesc:str = obj["GlobalCurrencyDocumentDesc"]
      self.GlobalCurrencyCurrDesc:str = obj["GlobalCurrencyCurrDesc"]
      self.GlobalCurrencyCurrName:str = obj["GlobalCurrencyCurrName"]
      self.GlobalCurrencyCurrencyID:str = obj["GlobalCurrencyCurrencyID"]
      self.GlobalCurrencyCurrSymbol:str = obj["GlobalCurrencyCurrSymbol"]
      self.MXDocTypeDescription:str = obj["MXDocTypeDescription"]
      self.StockProvFmtExcessDescription:str = obj["StockProvFmtExcessDescription"]
      self.StockProvFmtSlowDescription:str = obj["StockProvFmtSlowDescription"]
      self.SysFormsPrinterDescription:str = obj["SysFormsPrinterDescription"]
      self.SysLabelsPrinterDescription:str = obj["SysLabelsPrinterDescription"]
      self.THTaxRecDocTypeDescription:str = obj["THTaxRecDocTypeDescription"]
      self.THWHTDocTypeDescription:str = obj["THWHTDocTypeDescription"]
      self.WFGroupDescription:str = obj["WFGroupDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class FormatList_input:
   """ Required : 
   vCompany
   """  
   def __init__(self, obj):
      self.vCompany:str = obj["vCompany"]
      """  Company number  """  
      pass

class FormatList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.formatList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetBookMethodList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.strList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   company
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CompanyTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CompanyTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CompanyTableset] = obj["returnObj"]
      pass

class GetCPayCompanyList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cpayCompanyList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetCheckOffLabels_input:
   """ Required : 
   appName
   """  
   def __init__(self, obj):
      self.appName:str = obj["appName"]
      """  Either Job, Quote or DMR  """  
      pass

class GetCheckOffLabels_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.labelList:str = obj["parameters"]
      pass

      """  output parameters  """  

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

class GetInitialPath_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  A string containing the default path  """  
      pass

class GetLegalNumbers_input:
   """ Required : 
   transType
   """  
   def __init__(self, obj):
      self.transType:str = obj["transType"]
      pass

class GetLegalNumbers_output:
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
      self.returnObj:list[Erp_Tablesets_CompanyListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMaxWorkQueueRecords_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class GetModLicensing_input:
   """ Required : 
   vCompany
   """  
   def __init__(self, obj):
      self.vCompany:str = obj["vCompany"]
      """  Company number  """  
      pass

class GetModLicensing_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vModules:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetNewAGCompany_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class GetNewAGCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAPSyst_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class GetNewAPSyst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewARSyst_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class GetNewARSyst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBMSyst_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class GetNewBMSyst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBorderPct_input:
   """ Required : 
   ds
   company
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      self.company:str = obj["company"]
      pass

class GetNewBorderPct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBorderPercent_input:
   """ Required : 
   ds
   company
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      self.company:str = obj["company"]
      """  The company ID  """  
      pass

class GetNewBorderPercent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCRSyst_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class GetNewCRSyst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCSFSyst_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class GetNewCSFSyst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCompanyAttch_input:
   """ Required : 
   ds
   company
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      self.company:str = obj["company"]
      pass

class GetNewCompanyAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCompany_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class GetNewCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCurrRateGrp_input:
   """ Required : 
   ds
   company
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      self.company:str = obj["company"]
      pass

class GetNewCurrRateGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCurrency_input:
   """ Required : 
   ds
   company
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      self.company:str = obj["company"]
      pass

class GetNewCurrency_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEQSyst_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class GetNewEQSyst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEntityGLC_input:
   """ Required : 
   ds
   company
   relatedToFile
   key1
   key2
   key3
   key4
   key5
   key6
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      self.company:str = obj["company"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.key6:str = obj["key6"]
      pass

class GetNewEntityGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewExtPRSyst_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class GetNewExtPRSyst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFsSyst_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class GetNewFsSyst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLSyst_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class GetNewGLSyst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewISSyst_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class GetNewISSyst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewJCSyst_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class GetNewJCSyst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMMSyst_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class GetNewMMSyst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPDMSyst_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class GetNewPDMSyst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPECompWhldHist_input:
   """ Required : 
   ds
   company
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      self.company:str = obj["company"]
      pass

class GetNewPECompWhldHist_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPRSyst_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class GetNewPRSyst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTaxSvcConfig_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class GetNewTaxSvcConfig_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewXaSyst_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class GetNewXaSyst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewXbSyst_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class GetNewXbSyst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetOCRAlgorithmList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cOCRAlgorithmList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetQuickShipURL_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The value of the QuickShipURL (string).  """  
      pass

class GetRows_input:
   """ Required : 
   whereClauseCompany
   whereClauseCompanyAttch
   whereClauseAGCompany
   whereClauseAPSyst
   whereClauseARSyst
   whereClauseBMSyst
   whereClauseBorderPct
   whereClauseCRSyst
   whereClauseCSFSyst
   whereClauseCurrency
   whereClauseCurrRateGrp
   whereClauseEQSyst
   whereClauseExtPRSyst
   whereClauseFsSyst
   whereClauseGLSyst
   whereClauseISSyst
   whereClauseJCSyst
   whereClauseMMSyst
   whereClausePDMSyst
   whereClausePECompWhldHist
   whereClausePRSyst
   whereClauseTaxSvcConfig
   whereClauseXaSyst
   whereClauseXbSyst
   whereClauseEntityGLC
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCompany:str = obj["whereClauseCompany"]
      self.whereClauseCompanyAttch:str = obj["whereClauseCompanyAttch"]
      self.whereClauseAGCompany:str = obj["whereClauseAGCompany"]
      self.whereClauseAPSyst:str = obj["whereClauseAPSyst"]
      self.whereClauseARSyst:str = obj["whereClauseARSyst"]
      self.whereClauseBMSyst:str = obj["whereClauseBMSyst"]
      self.whereClauseBorderPct:str = obj["whereClauseBorderPct"]
      self.whereClauseCRSyst:str = obj["whereClauseCRSyst"]
      self.whereClauseCSFSyst:str = obj["whereClauseCSFSyst"]
      self.whereClauseCurrency:str = obj["whereClauseCurrency"]
      self.whereClauseCurrRateGrp:str = obj["whereClauseCurrRateGrp"]
      self.whereClauseEQSyst:str = obj["whereClauseEQSyst"]
      self.whereClauseExtPRSyst:str = obj["whereClauseExtPRSyst"]
      self.whereClauseFsSyst:str = obj["whereClauseFsSyst"]
      self.whereClauseGLSyst:str = obj["whereClauseGLSyst"]
      self.whereClauseISSyst:str = obj["whereClauseISSyst"]
      self.whereClauseJCSyst:str = obj["whereClauseJCSyst"]
      self.whereClauseMMSyst:str = obj["whereClauseMMSyst"]
      self.whereClausePDMSyst:str = obj["whereClausePDMSyst"]
      self.whereClausePECompWhldHist:str = obj["whereClausePECompWhldHist"]
      self.whereClausePRSyst:str = obj["whereClausePRSyst"]
      self.whereClauseTaxSvcConfig:str = obj["whereClauseTaxSvcConfig"]
      self.whereClauseXaSyst:str = obj["whereClauseXaSyst"]
      self.whereClauseXbSyst:str = obj["whereClauseXbSyst"]
      self.whereClauseEntityGLC:str = obj["whereClauseEntityGLC"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CompanyTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSerialNumbers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.serialList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetSystemTimeZoneList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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

class InitializeCompany_input:
   """ Required : 
   companyID
   baseCurrencyCode
   decimalsCost
   decimalsPrice
   decimalsGeneral
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      self.baseCurrencyCode:str = obj["baseCurrencyCode"]
      self.decimalsCost:int = obj["decimalsCost"]
      self.decimalsPrice:int = obj["decimalsPrice"]
      self.decimalsGeneral:int = obj["decimalsGeneral"]
      pass

class InitializeCompany_output:
   def __init__(self, obj):
      pass

class NLCopyDigipoortSettingToAllCompanies_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Companies have been modified  """  
      pass

class OnChangeARBankAcctID_input:
   """ Required : 
   ipBankAcctID
   ds
   """  
   def __init__(self, obj):
      self.ipBankAcctID:str = obj["ipBankAcctID"]
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class OnChangeARBankAcctID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeAddrValEnabled_input:
   """ Required : 
   AddrValEnabled
   ds
   """  
   def __init__(self, obj):
      self.AddrValEnabled:bool = obj["AddrValEnabled"]
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class OnChangeAddrValEnabled_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBankAcctID_input:
   """ Required : 
   ipBankAcctID
   ds
   """  
   def __init__(self, obj):
      self.ipBankAcctID:str = obj["ipBankAcctID"]
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class OnChangeBankAcctID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeCentralCollectionParentCompany_input:
   """ Required : 
   ipProposedCColCompany
   ds
   """  
   def __init__(self, obj):
      self.ipProposedCColCompany:str = obj["ipProposedCColCompany"]
      """  Central Collection Parent Company value  """  
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class OnChangeCentralCollectionParentCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDefTaxLiability_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class OnChangeDefTaxLiability_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeELIDefEinvoicePath_input:
   """ Required : 
   eliDefEinvoicePath
   ds
   """  
   def __init__(self, obj):
      self.eliDefEinvoicePath:str = obj["eliDefEinvoicePath"]
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class OnChangeELIDefEinvoicePath_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeELIDefReportID_input:
   """ Required : 
   eliDefReportID
   ds
   """  
   def __init__(self, obj):
      self.eliDefReportID:str = obj["eliDefReportID"]
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class OnChangeELIDefReportID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeFlow_input:
   """ Required : 
   cFlowCode
   lIsFlowArrival
   ds
   """  
   def __init__(self, obj):
      self.cFlowCode:str = obj["cFlowCode"]
      """  Flow code.  """  
      self.lIsFlowArrival:bool = obj["lIsFlowArrival"]
      """  Flag, showed which flow code has been changing: True - Arrival; False - Despatch.  """  
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class OnChangeFlow_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeGJJournalCode_input:
   """ Required : 
   cGJJournalCode
   """  
   def __init__(self, obj):
      self.cGJJournalCode:str = obj["cGJJournalCode"]
      """  Proposed GJJournalCode  """  
      pass

class OnChangeGJJournalCode_output:
   def __init__(self, obj):
      pass

class OnChangeMasterChart_input:
   """ Required : 
   currMasterChart
   newMasterChart
   """  
   def __init__(self, obj):
      self.currMasterChart:str = obj["currMasterChart"]
      """  Current value of MasterChart  """  
      self.newMasterChart:str = obj["newMasterChart"]
      """  Proposed value of MasterChart  """  
      pass

class OnChangeMasterChart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeSiteIsLegalEntity_input:
   """ Required : 
   ipSiteIsLegalEntity
   ds
   """  
   def __init__(self, obj):
      self.ipSiteIsLegalEntity:bool = obj["ipSiteIsLegalEntity"]
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class OnChangeSiteIsLegalEntity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTranDocType_input:
   """ Required : 
   ipTranDocTypeID
   ds
   """  
   def __init__(self, obj):
      self.ipTranDocTypeID:str = obj["ipTranDocTypeID"]
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class OnChangeTranDocType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeUseAltBillToAddr_input:
   """ Required : 
   UseAltBillToAddr
   ds
   """  
   def __init__(self, obj):
      self.UseAltBillToAddr:bool = obj["UseAltBillToAddr"]
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class OnChangeUseAltBillToAddr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingDestCountryNum_input:
   """ Required : 
   pDestCountryNum
   bBorderPctSysRowID
   """  
   def __init__(self, obj):
      self.pDestCountryNum:int = obj["pDestCountryNum"]
      """  Proposed DestCountryNum  """  
      self.bBorderPctSysRowID:str = obj["bBorderPctSysRowID"]
      """  Current SysRowID  """  
      pass

class OnChangingDestCountryNum_output:
   def __init__(self, obj):
      pass

class OnChangingSubRateGrp_input:
   """ Required : 
   pSubRateGrp
   """  
   def __init__(self, obj):
      self.pSubRateGrp:str = obj["pSubRateGrp"]
      """  Proposed SubRateGrp  """  
      pass

class OnChangingSubRateGrp_output:
   def __init__(self, obj):
      pass

class SiteIsLegalEntity_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class TestExtCRMConnection_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.msgConnection:str = obj["parameters"]
      pass

      """  output parameters  """  

class TestTaxConnection_input:
   """ Required : 
   svcURL
   svcAccount
   svcLicense
   """  
   def __init__(self, obj):
      self.svcURL:str = obj["svcURL"]
      """  SvcURL  """  
      self.svcAccount:str = obj["svcAccount"]
      """  SvcAccount  """  
      self.svcLicense:str = obj["svcLicense"]
      """  SvcLicense  """  
      pass

class TestTaxConnection_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.testResult:bool = obj["testResult"]
      self.testMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCompanyTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCompanyTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateIntrastatCodeForCompany_input:
   """ Required : 
   countryNum
   """  
   def __init__(self, obj):
      self.countryNum:int = obj["countryNum"]
      """  Country for Current Company  """  
      pass

class ValidateIntrastatCodeForCompany_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ValidateMYIndustryCodeOnChanging_input:
   """ Required : 
   proposedCodeID
   proposedCodeValue
   industryCode1
   industryCode2
   industryCode3
   industryCode4
   industryCode5
   """  
   def __init__(self, obj):
      self.proposedCodeID:int = obj["proposedCodeID"]
      """  zero-based order number of industry codes  """  
      self.proposedCodeValue:str = obj["proposedCodeValue"]
      """  proposed value  """  
      self.industryCode1:str = obj["industryCode1"]
      """  industry code 1  """  
      self.industryCode2:str = obj["industryCode2"]
      """  industry code 2  """  
      self.industryCode3:str = obj["industryCode3"]
      """  industry code 3  """  
      self.industryCode4:str = obj["industryCode4"]
      """  industry code 4  """  
      self.industryCode5:str = obj["industryCode5"]
      """  industry code 5  """  
      pass

class ValidateMYIndustryCodeOnChanging_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ValidateSendToFSA_input:
   """ Required : 
   companyId
   sendToFSA
   """  
   def __init__(self, obj):
      self.companyId:str = obj["companyId"]
      """  Current Company  """  
      self.sendToFSA:bool = obj["sendToFSA"]
      """  Sync to FSA flag for Current Company  """  
      pass

class ValidateSendToFSA_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

