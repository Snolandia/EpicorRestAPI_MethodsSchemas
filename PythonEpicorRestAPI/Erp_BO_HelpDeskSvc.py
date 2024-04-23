import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.HelpDeskSvc
# Description: This is the Help Desk main business object.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_HelpDesks(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get HelpDesks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HelpDesks
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks",headers=creds) as resp:
           return await resp.json()

async def post_HelpDesks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HelpDesks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDCaseRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.HDCaseRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_HelpDesks_Company_HDCaseNum(Company, HDCaseNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HelpDesk item
   Description: Calls GetByID to retrieve the HelpDesk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HelpDesk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDCaseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_HelpDesks_Company_HDCaseNum(Company, HDCaseNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update HelpDesk for the service
   Description: Calls UpdateExt to update HelpDesk. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HelpDesk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDCaseRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_HelpDesks_Company_HDCaseNum(Company, HDCaseNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete HelpDesk item
   Description: Call UpdateExt to delete HelpDesk item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HelpDesk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_HelpDesks_Company_HDCaseNum_HDCaseFSCalls(Company, HDCaseNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get HDCaseFSCalls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_HDCaseFSCalls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseFSCallRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseFSCalls",headers=creds) as resp:
           return await resp.json()

async def get_HelpDesks_Company_HDCaseNum_HDCaseFSCalls_SysRowID(Company, HDCaseNum, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDCaseFSCall item
   Description: Calls GetByID to retrieve the HDCaseFSCall item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseFSCall1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDCaseFSCallRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseFSCalls(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_HelpDesks_Company_HDCaseNum_HDCaseJobs(Company, HDCaseNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get HDCaseJobs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_HDCaseJobs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseJobRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseJobs",headers=creds) as resp:
           return await resp.json()

async def get_HelpDesks_Company_HDCaseNum_HDCaseJobs_SysRowID(Company, HDCaseNum, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDCaseJob item
   Description: Calls GetByID to retrieve the HDCaseJob item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseJob1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDCaseJobRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseJobs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_HelpDesks_Company_HDCaseNum_HDCaseLinks(Company, HDCaseNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get HDCaseLinks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_HDCaseLinks1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseLinks",headers=creds) as resp:
           return await resp.json()

async def get_HelpDesks_Company_HDCaseNum_HDCaseLinks_Company_HDCaseNum_ExternalLink_RelatedToFile_Key1_Key2_Key3_Key4_Key5(Company, HDCaseNum, ExternalLink, RelatedToFile, Key1, Key2, Key3, Key4, Key5, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDCaseLink item
   Description: Calls GetByID to retrieve the HDCaseLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseLink1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param ExternalLink: Desc: ExternalLink   Required: True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDCaseLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseLinks(" + Company + "," + HDCaseNum + "," + ExternalLink + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")",headers=creds) as resp:
           return await resp.json()

async def get_HelpDesks_Company_HDCaseNum_HDCaseOrders(Company, HDCaseNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get HDCaseOrders items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_HDCaseOrders1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseOrderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseOrders",headers=creds) as resp:
           return await resp.json()

async def get_HelpDesks_Company_HDCaseNum_HDCaseOrders_SysRowID(Company, HDCaseNum, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDCaseOrder item
   Description: Calls GetByID to retrieve the HDCaseOrder item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseOrder1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDCaseOrderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseOrders(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_HelpDesks_Company_HDCaseNum_HDCaseQuotes(Company, HDCaseNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get HDCaseQuotes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_HDCaseQuotes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseQuoteRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseQuotes",headers=creds) as resp:
           return await resp.json()

async def get_HelpDesks_Company_HDCaseNum_HDCaseQuotes_SysRowID(Company, HDCaseNum, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDCaseQuote item
   Description: Calls GetByID to retrieve the HDCaseQuote item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseQuote1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDCaseQuoteRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseQuotes(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_HelpDesks_Company_HDCaseNum_HDCaseRMAs(Company, HDCaseNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get HDCaseRMAs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_HDCaseRMAs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseRMARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseRMAs",headers=creds) as resp:
           return await resp.json()

async def get_HelpDesks_Company_HDCaseNum_HDCaseRMAs_SysRowID(Company, HDCaseNum, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDCaseRMA item
   Description: Calls GetByID to retrieve the HDCaseRMA item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseRMA1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDCaseRMARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseRMAs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_HelpDesks_Company_HDCaseNum_HDChildCases(Company, HDCaseNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get HDChildCases items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_HDChildCases1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDChildCasesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDChildCases",headers=creds) as resp:
           return await resp.json()

async def get_HelpDesks_Company_HDCaseNum_HDChildCases_Company_HDCaseNum(Company, HDCaseNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDChildCas item
   Description: Calls GetByID to retrieve the HDChildCas item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDChildCas1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDChildCasesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDChildCases(" + Company + "," + HDCaseNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_HelpDesks_Company_HDCaseNum_HDContacts(Company, HDCaseNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get HDContacts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_HDContacts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDContactRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDContacts",headers=creds) as resp:
           return await resp.json()

async def get_HelpDesks_Company_HDCaseNum_HDContacts_Company_HDCaseNum_PerConLnkRowID(Company, HDCaseNum, PerConLnkRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDContact item
   Description: Calls GetByID to retrieve the HDContact item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDContact1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param PerConLnkRowID: Desc: PerConLnkRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDContactRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDContacts(" + Company + "," + HDCaseNum + "," + PerConLnkRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_HelpDesks_Company_HDCaseNum_HDCaseMaintReqs(Company, HDCaseNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get HDCaseMaintReqs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_HDCaseMaintReqs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseMaintReqRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseMaintReqs",headers=creds) as resp:
           return await resp.json()

async def get_HelpDesks_Company_HDCaseNum_HDCaseMaintReqs_SysRowID(Company, HDCaseNum, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDCaseMaintReq item
   Description: Calls GetByID to retrieve the HDCaseMaintReq item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseMaintReq1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDCaseMaintReqRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseMaintReqs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_HelpDesks_Company_HDCaseNum_HDCaseAttches(Company, HDCaseNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get HDCaseAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_HDCaseAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseAttches",headers=creds) as resp:
           return await resp.json()

async def get_HelpDesks_Company_HDCaseNum_HDCaseAttches_Company_HDCaseNum_DrawingSeq(Company, HDCaseNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDCaseAttch item
   Description: Calls GetByID to retrieve the HDCaseAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDCaseAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HelpDesks(" + Company + "," + HDCaseNum + ")/HDCaseAttches(" + Company + "," + HDCaseNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_HDCaseFSCalls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get HDCaseFSCalls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HDCaseFSCalls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseFSCallRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseFSCalls",headers=creds) as resp:
           return await resp.json()

async def post_HDCaseFSCalls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HDCaseFSCalls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDCaseFSCallRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.HDCaseFSCallRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseFSCalls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_HDCaseFSCalls_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDCaseFSCall item
   Description: Calls GetByID to retrieve the HDCaseFSCall item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseFSCall
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDCaseFSCallRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseFSCalls(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_HDCaseFSCalls_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update HDCaseFSCall for the service
   Description: Calls UpdateExt to update HDCaseFSCall. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HDCaseFSCall
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDCaseFSCallRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseFSCalls(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_HDCaseFSCalls_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete HDCaseFSCall item
   Description: Call UpdateExt to delete HDCaseFSCall item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HDCaseFSCall
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseFSCalls(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_HDCaseJobs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get HDCaseJobs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HDCaseJobs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseJobRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseJobs",headers=creds) as resp:
           return await resp.json()

async def post_HDCaseJobs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HDCaseJobs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDCaseJobRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.HDCaseJobRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseJobs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_HDCaseJobs_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDCaseJob item
   Description: Calls GetByID to retrieve the HDCaseJob item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseJob
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDCaseJobRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseJobs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_HDCaseJobs_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update HDCaseJob for the service
   Description: Calls UpdateExt to update HDCaseJob. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HDCaseJob
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDCaseJobRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseJobs(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_HDCaseJobs_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete HDCaseJob item
   Description: Call UpdateExt to delete HDCaseJob item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HDCaseJob
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseJobs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_HDCaseLinks(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get HDCaseLinks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HDCaseLinks
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseLinks",headers=creds) as resp:
           return await resp.json()

async def post_HDCaseLinks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HDCaseLinks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDCaseLinkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.HDCaseLinkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseLinks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_HDCaseLinks_Company_HDCaseNum_ExternalLink_RelatedToFile_Key1_Key2_Key3_Key4_Key5(Company, HDCaseNum, ExternalLink, RelatedToFile, Key1, Key2, Key3, Key4, Key5, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDCaseLink item
   Description: Calls GetByID to retrieve the HDCaseLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseLink
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param ExternalLink: Desc: ExternalLink   Required: True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDCaseLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseLinks(" + Company + "," + HDCaseNum + "," + ExternalLink + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_HDCaseLinks_Company_HDCaseNum_ExternalLink_RelatedToFile_Key1_Key2_Key3_Key4_Key5(Company, HDCaseNum, ExternalLink, RelatedToFile, Key1, Key2, Key3, Key4, Key5, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update HDCaseLink for the service
   Description: Calls UpdateExt to update HDCaseLink. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HDCaseLink
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param ExternalLink: Desc: ExternalLink   Required: True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDCaseLinkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseLinks(" + Company + "," + HDCaseNum + "," + ExternalLink + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_HDCaseLinks_Company_HDCaseNum_ExternalLink_RelatedToFile_Key1_Key2_Key3_Key4_Key5(Company, HDCaseNum, ExternalLink, RelatedToFile, Key1, Key2, Key3, Key4, Key5, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete HDCaseLink item
   Description: Call UpdateExt to delete HDCaseLink item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HDCaseLink
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param ExternalLink: Desc: ExternalLink   Required: True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseLinks(" + Company + "," + HDCaseNum + "," + ExternalLink + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")",headers=creds) as resp:
           return await resp.json()

async def get_HDCaseOrders(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get HDCaseOrders items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HDCaseOrders
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseOrderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseOrders",headers=creds) as resp:
           return await resp.json()

async def post_HDCaseOrders(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HDCaseOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDCaseOrderRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.HDCaseOrderRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseOrders", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_HDCaseOrders_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDCaseOrder item
   Description: Calls GetByID to retrieve the HDCaseOrder item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseOrder
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDCaseOrderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseOrders(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_HDCaseOrders_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update HDCaseOrder for the service
   Description: Calls UpdateExt to update HDCaseOrder. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HDCaseOrder
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDCaseOrderRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseOrders(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_HDCaseOrders_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete HDCaseOrder item
   Description: Call UpdateExt to delete HDCaseOrder item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HDCaseOrder
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseOrders(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_HDCaseQuotes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get HDCaseQuotes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HDCaseQuotes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseQuoteRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseQuotes",headers=creds) as resp:
           return await resp.json()

async def post_HDCaseQuotes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HDCaseQuotes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDCaseQuoteRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.HDCaseQuoteRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseQuotes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_HDCaseQuotes_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDCaseQuote item
   Description: Calls GetByID to retrieve the HDCaseQuote item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseQuote
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDCaseQuoteRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseQuotes(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_HDCaseQuotes_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update HDCaseQuote for the service
   Description: Calls UpdateExt to update HDCaseQuote. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HDCaseQuote
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDCaseQuoteRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseQuotes(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_HDCaseQuotes_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete HDCaseQuote item
   Description: Call UpdateExt to delete HDCaseQuote item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HDCaseQuote
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseQuotes(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_HDCaseRMAs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get HDCaseRMAs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HDCaseRMAs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseRMARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseRMAs",headers=creds) as resp:
           return await resp.json()

async def post_HDCaseRMAs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HDCaseRMAs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDCaseRMARow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.HDCaseRMARow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseRMAs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_HDCaseRMAs_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDCaseRMA item
   Description: Calls GetByID to retrieve the HDCaseRMA item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseRMA
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDCaseRMARow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseRMAs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_HDCaseRMAs_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update HDCaseRMA for the service
   Description: Calls UpdateExt to update HDCaseRMA. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HDCaseRMA
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDCaseRMARow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseRMAs(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_HDCaseRMAs_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete HDCaseRMA item
   Description: Call UpdateExt to delete HDCaseRMA item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HDCaseRMA
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseRMAs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_HDChildCases(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get HDChildCases items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HDChildCases
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDChildCasesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDChildCases",headers=creds) as resp:
           return await resp.json()

async def post_HDChildCases(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HDChildCases
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDChildCasesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.HDChildCasesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDChildCases", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_HDChildCases_Company_HDCaseNum(Company, HDCaseNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDChildCas item
   Description: Calls GetByID to retrieve the HDChildCas item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDChildCas
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDChildCasesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDChildCases(" + Company + "," + HDCaseNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_HDChildCases_Company_HDCaseNum(Company, HDCaseNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update HDChildCas for the service
   Description: Calls UpdateExt to update HDChildCas. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HDChildCas
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDChildCasesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDChildCases(" + Company + "," + HDCaseNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_HDChildCases_Company_HDCaseNum(Company, HDCaseNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete HDChildCas item
   Description: Call UpdateExt to delete HDChildCas item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HDChildCas
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDChildCases(" + Company + "," + HDCaseNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_HDContacts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get HDContacts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HDContacts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDContactRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDContacts",headers=creds) as resp:
           return await resp.json()

async def post_HDContacts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HDContacts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDContactRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.HDContactRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDContacts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_HDContacts_Company_HDCaseNum_PerConLnkRowID(Company, HDCaseNum, PerConLnkRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDContact item
   Description: Calls GetByID to retrieve the HDContact item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDContact
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param PerConLnkRowID: Desc: PerConLnkRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDContactRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDContacts(" + Company + "," + HDCaseNum + "," + PerConLnkRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_HDContacts_Company_HDCaseNum_PerConLnkRowID(Company, HDCaseNum, PerConLnkRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update HDContact for the service
   Description: Calls UpdateExt to update HDContact. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HDContact
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param PerConLnkRowID: Desc: PerConLnkRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDContactRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDContacts(" + Company + "," + HDCaseNum + "," + PerConLnkRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_HDContacts_Company_HDCaseNum_PerConLnkRowID(Company, HDCaseNum, PerConLnkRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete HDContact item
   Description: Call UpdateExt to delete HDContact item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HDContact
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param PerConLnkRowID: Desc: PerConLnkRowID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDContacts(" + Company + "," + HDCaseNum + "," + PerConLnkRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_HDCaseMaintReqs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get HDCaseMaintReqs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HDCaseMaintReqs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseMaintReqRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseMaintReqs",headers=creds) as resp:
           return await resp.json()

async def post_HDCaseMaintReqs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HDCaseMaintReqs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDCaseMaintReqRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.HDCaseMaintReqRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseMaintReqs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_HDCaseMaintReqs_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDCaseMaintReq item
   Description: Calls GetByID to retrieve the HDCaseMaintReq item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseMaintReq
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDCaseMaintReqRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseMaintReqs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_HDCaseMaintReqs_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update HDCaseMaintReq for the service
   Description: Calls UpdateExt to update HDCaseMaintReq. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HDCaseMaintReq
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDCaseMaintReqRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseMaintReqs(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_HDCaseMaintReqs_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete HDCaseMaintReq item
   Description: Call UpdateExt to delete HDCaseMaintReq item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HDCaseMaintReq
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseMaintReqs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_HDCaseAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get HDCaseAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_HDCaseAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseAttches",headers=creds) as resp:
           return await resp.json()

async def post_HDCaseAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_HDCaseAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.HDCaseAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.HDCaseAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_HDCaseAttches_Company_HDCaseNum_DrawingSeq(Company, HDCaseNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the HDCaseAttch item
   Description: Calls GetByID to retrieve the HDCaseAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_HDCaseAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.HDCaseAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseAttches(" + Company + "," + HDCaseNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_HDCaseAttches_Company_HDCaseNum_DrawingSeq(Company, HDCaseNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update HDCaseAttch for the service
   Description: Calls UpdateExt to update HDCaseAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_HDCaseAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.HDCaseAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseAttches(" + Company + "," + HDCaseNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_HDCaseAttches_Company_HDCaseNum_DrawingSeq(Company, HDCaseNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete HDCaseAttch item
   Description: Call UpdateExt to delete HDCaseAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_HDCaseAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HDCaseNum: Desc: HDCaseNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/HDCaseAttches(" + Company + "," + HDCaseNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.HDCaseListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseHDCase, whereClauseHDCaseAttch, whereClauseHDCaseFSCall, whereClauseHDCaseJob, whereClauseHDCaseLink, whereClauseHDCaseOrder, whereClauseHDCaseQuote, whereClauseHDCaseRMA, whereClauseHDChildCases, whereClauseHDContact, whereClauseHDCaseMaintReq, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseHDCase=" + whereClauseHDCase
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseHDCaseAttch=" + whereClauseHDCaseAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseHDCaseFSCall=" + whereClauseHDCaseFSCall
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseHDCaseJob=" + whereClauseHDCaseJob
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseHDCaseLink=" + whereClauseHDCaseLink
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseHDCaseOrder=" + whereClauseHDCaseOrder
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseHDCaseQuote=" + whereClauseHDCaseQuote
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseHDCaseRMA=" + whereClauseHDCaseRMA
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseHDChildCases=" + whereClauseHDChildCases
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseHDContact=" + whereClauseHDContact
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseHDCaseMaintReq=" + whereClauseHDCaseMaintReq
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(hdCaseNum, epicorHeaders = None):
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
   params += "hdCaseNum=" + hdCaseNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CheckPrePartInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPrePartInfo
   Description: This method checks to see if there are any questions or issues with the part entered
and returns a message, a part number and if any substitutes exist.  Call this method
first before calling the ChangeDtlPartNum method when the field HDCase.PartNum changes.
   OperationID: CheckPrePartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPrePartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPrePartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateFSCall(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateFSCall
   Description: Create a Field Service call from this Help Desk Case.
   OperationID: CreateFSCall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateFSCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateFSCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateFSCallLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateFSCallLine
   Description: Create a Field Service call with 1 line , for this Help Desk Case.
   OperationID: CreateFSCallLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateFSCallLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateFSCallLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateJob
   Description: Create a Job from this Help Desk Case.
PartNum must be populated before calling this method, as it is required on a Job
The HDCase in the database will be used for this call.
   OperationID: CreateJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckProjectID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckProjectID
   Description: Validate the Project ID for Quotes, Orders and Jobs.
   OperationID: CheckProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateMaintReq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateMaintReq
   Description: Create a Request from this Help Desk Case.
   OperationID: CreateMaintReq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateMaintReq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateMaintReq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateOrder
   Description: Create a quote from this Help Desk Case.
CustNum must be populated before calling this method, as it is required on a quote
The HDCase in the database will be used for this call.
   OperationID: CreateOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateQuote(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateQuote
   Description: Create a quote from this Help Desk Case.
CustNum must be populated before calling this method, as it is required on a quote
The HDCase in the database will be used for this call.
   OperationID: CreateQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateQuoteWithLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateQuoteWithLine
   Description: Create a quote with 1 line for this Help Desk Case.
CustNum and PartNum must be populated before calling this method, as it is required on a quote
The HDCase in the database will be used for this call.
   OperationID: CreateQuoteWithLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateQuoteWithLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateQuoteWithLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateOrderWithLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateOrderWithLine
   OperationID: CreateOrderWithLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateOrderWithLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateOrderWithLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateRMAUpdConNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateRMAUpdConNum
   Description: Create an RMA from this Help Desk Case.
CustNum and PrcConNum (customer contact) must be populated before calling this method, as it is required on an RMA
The HDCase in the database will be used for this call.
   OperationID: CreateRMAUpdConNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateRMAUpdConNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateRMAUpdConNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateRMALine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateRMALine
   Description: Create an RMA with 1 line for this Help Desk Case.
CustNum and PrcConNum (customer contact) must be populated before calling this method, as it is required on an RMA
The HDCase in the database will be used for this call.
   OperationID: CreateRMALine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateRMALine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateRMALine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateRMA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateRMA
   Description: Create an RMA from this Help Desk Case.
CustNum must be populated before calling this method, as it is required on an RMA
The HDCase in the database will be used for this call.
   OperationID: CreateRMA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateRMA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateRMA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangedTaskSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedTaskSet
   Description: Change a Task from this Help Desk Case when changing the Task Set.
   OperationID: ChangedTaskSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedTaskSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedTaskSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteRMAHeadLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteRMAHeadLink
   Description: Update RMAHead.HDCaseNum  = 0  to delete the link from the current HDCase.
RMAHead is populated with the record filter by the current Company, HDCaseNum and RMANum
it is modified to remove the HDCaseNum
   OperationID: DeleteRMAHeadLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteRMAHeadLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRMAHeadLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteQuoteHedLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteQuoteHedLink
   Description: Update QuoteHed.HDCaseNum  = 0  to delete the link from the current HDCase.
QuoteHead is populated with the record filter by the current Company, HDCaseNum and QuoteNum
it is modified to remove the HDCaseNum
   OperationID: DeleteQuoteHedLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteQuoteHedLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteQuoteHedLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteOrderHedLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteOrderHedLink
   Description: Update OrderHed.HDCaseNum  = 0  to delete the link from the current HDCase.
OrderHed is populated with the record filter by the current Company, HDCaseNum and OrderNum
it is modified to remove the HDCaseNum
   OperationID: DeleteOrderHedLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteOrderHedLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteOrderHedLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteJobHeadLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteJobHeadLink
   Description: Update JobHead.HDCaseNum  = 0  to delete the link from the current HDCase.
JobHead is populated with the record filter by the current Company, HDCaseNum and jobNum
it is modified to remove the HDCaseNum
   OperationID: DeleteJobHeadLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteJobHeadLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteJobHeadLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteFSCallhdLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteFSCallhdLink
   Description: Update FSCallhd.HDCaseNum  = 0  to delete the link from the current HDCase.
FSCallhd is populated with the record filter by the current Company, HDCaseNum and callNum
it is modified to remove the HDCaseNum
   OperationID: DeleteFSCallhdLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteFSCallhdLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteFSCallhdLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteMaintReqLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteMaintReqLink
   Description: Update MaintReq.HDCaseNum  = 0  to delete the link from the current HDCase.
MaintReq is populated with the record filter by the current Company, HDCaseNum and ReqID
it is modified to remove the HDCaseNum
   OperationID: DeleteMaintReqLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteMaintReqLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteMaintReqLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteHDCaseExternalLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteHDCaseExternalLink
   Description: Delete HDCaseLink records associated with the current HDCase.
   OperationID: DeleteHDCaseExternalLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteHDCaseExternalLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteHDCaseExternalLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteHDChildCaseLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteHDChildCaseLink
   Description: Delete HDChildCase records associated with the current HDCase.
   OperationID: DeleteHDChildCaseLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteHDChildCaseLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteHDChildCaseLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTaskSets(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTaskSets
   Description: Get the topics to make available as children to a given topic.
For top level topics, pass in  a blank parentTopicID
For all topics pass in "ReturnFullTopicList"
   OperationID: GetAvailTaskSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailTaskSets_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTaskSets_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetChildTopics(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetChildTopics
   Description: Get the topics to make available as children to a given topic.
           For top level topics, pass in  a blank parentTopicID
           For all topics pass in "ReturnFullTopicList"
   OperationID: GetChildTopics
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetChildTopics_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetChildTopics_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetChildTopicsDS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetChildTopicsDS
   Description: Populate HDCaseSearch ds with child topics.
   OperationID: GetChildTopicsDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetChildTopicsDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetChildTopicsDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewHDCaseSearchDS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewHDCaseSearchDS
   Description: Get new HDCaseSearch data and populate the dataset with child topics.
   OperationID: GetNewHDCaseSearchDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewHDCaseSearchDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDCaseSearchDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSearchTopicID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSearchTopicID
   Description: Validate change of search topics and populate the next available combo box.
   OperationID: OnChangeSearchTopicID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSearchTopicID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSearchTopicID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewHDCaseSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewHDCaseSearch
   Description: Get a blank set of search parameters
   OperationID: GetNewHDCaseSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewHDCaseSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDCaseSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_createAvailableMilestonesList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method createAvailableMilestonesList
   Description: Return a delimited list of the available Milestone for the selected Help Desk Case number.
   OperationID: createAvailableMilestonesList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/createAvailableMilestonesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/createAvailableMilestonesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_createAvailableTaskSetsList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method createAvailableTaskSetsList
   Description: Return a list of Available TaskSets
   OperationID: createAvailableTaskSetsList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/createAvailableTaskSetsList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/createAvailableTaskSetsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsContactTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsContactTracker
   Description: Called from Contact tracker instead of GetRows for better performance
   OperationID: GetRowsContactTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsContactTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsContactTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_HelpDeskSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HelpDeskSearch
   Description: Perform a search of the helpdesk and/or knowledgebase cases
   OperationID: HelpDeskSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HelpDeskSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HelpDeskSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAttrCodeList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAttrCodeList
   Description: Get the defaults from the AttrCodeList field on the HDCase record.
   OperationID: OnChangeAttrCodeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAttrCodeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAttrCodeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBuyerID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBuyerID
   Description: This method should be called when BuyerID change.
   OperationID: OnChangeBuyerID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBuyerID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBuyerID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCallLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCallLine
   Description: Get the defaults from the CallLine field on the HDCase
record.
   OperationID: OnChangeCallLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCallLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCallLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCallNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCallNum
   Description: Get the defaults from the CallNum field on the HDCase
record.
   OperationID: OnChangeCallNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCallNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCallNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCaseOwner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCaseOwner
   Description: Get the defaults from the CaseOwner field on the HDCase
record.
   OperationID: OnChangeCaseOwner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCaseOwner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCaseOwner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCaseTopics(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCaseTopics
   Description: Get the defaults 10 Topics fields
   OperationID: OnChangeCaseTopics
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCaseTopics_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCaseTopics_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCaseTypeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCaseTypeID
   Description: Get the defaults for the Case Type on HDCase.
   OperationID: OnChangeCaseTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCaseTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCaseTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeContractNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeContractNum
   Description: Get the defaults from the ContractNum field on the HDCase record.
   OperationID: OnChangeContractNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeContractNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeContractNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeContractLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeContractLine
   OperationID: OnChangeContractLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeContractLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeContractLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ContractHasLines(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ContractHasLines
   Description: Get the ContractLines from the ContractNum field on the HDCase record.
   OperationID: ContractHasLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ContractHasLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ContractHasLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateContractStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateContractStatus
   Description: Validate the ContractNum field on the HDCase record.
   OperationID: ValidateContractStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateContractStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateContractStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateContractPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateContractPart
   Description: Validate the ContractNum field on the HDCase record.
   OperationID: ValidateContractPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateContractPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateContractPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindPart
   Description: Find part.
   OperationID: FindPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartFromRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartFromRowID
   Description: GetPartFromRowID.
   OperationID: GetPartFromRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartFromRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCustID
   Description: Get the defaults from the CustID field on the HDCase
           record.
           This will set:
           The Customer Contact
   OperationID: OnChangeCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeEmpID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeEmpID
   Description: This method should be called when EmpID change.
   OperationID: OnChangeEmpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeEmpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeEmpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeEquipID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeEquipID
   Description: This method should be called when EquipID change.
   OperationID: OnChangeEquipID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeEquipID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeEquipID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeHDCaseSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeHDCaseSearch
   Description: Validates the search fields
   OperationID: OnChangeHDCaseSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeHDCaseSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeHDCaseSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeInvoiceLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeInvoiceLine
   Description: Get the defaults from the InvoiceLine field on the HDCase
record.
   OperationID: OnChangeInvoiceLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInvoiceLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInvoiceLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeInvoiceNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeInvoiceNum
   Description: Get the defaults from the InvoiceNum field on the HDCase
           record.
   OperationID: OnChangeInvoiceNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMktgCampaignID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMktgCampaignID
   Description: Get the defaults from the MktgCampaignID field on the HDCase
record.
   OperationID: OnChangeMktgCampaignID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMktgCampaignID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMktgCampaignID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMktgEvntSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMktgEvntSeq
   Description: Get the defaults from the MktgEvntSeq field on the HDCase
record.
   OperationID: OnChangeMktgEvntSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMktgEvntSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMktgEvntSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeName
   Description: This method should be called when Name change.
   OperationID: OnChangeName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOrderLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOrderLine
   Description: Get the defaults from the OrderLine field on the HDCase
record.
   OperationID: OnChangeOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOrderNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOrderNum
   Description: Get the defaults from the OrderNum field on the HDCase
record.
   OperationID: OnChangeOrderNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOrderNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOrderNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOrderRelNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOrderRelNum
   Description: Get the defaults from the OrderRelNum field on the HDCase
record.
   OperationID: OnChangeOrderRelNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOrderRelNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOrderRelNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartNum
   Description: Get the defaults from the PartNum field on the HDCase
record.
   OperationID: OnChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePerConLnkRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePerConLnkRowID
   Description: This method should be called when PerConLnkRowID change.
   OperationID: OnChangePerConLnkRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePerConLnkRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePerConLnkRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePrcConNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePrcConNum
   Description: Get the defaults from the PrcConNum field on the HDCase
record.
   OperationID: OnChangePrcConNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePrcConNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePrcConNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeProjectID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeProjectID
   Description: Validate the ProjectID record.
   OperationID: OnChangeProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePurPoint(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePurPoint
   Description: Get the defaults from the PurPoint field on the HDCase record.
   OperationID: OnChangePurPoint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePurPointConNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePurPointConNum
   Description: Get the defaults from the PurPointConNum field on the HDCase record.
   OperationID: OnChangePurPointConNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePurPointConNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePurPointConNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeQuantity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeQuantity
   Description: Calculate de Ext Price when Quantity Change
   OperationID: OnChangeQuantity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeQuantity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQuantity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeQuantityUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeQuantityUOM
   Description: Calculate de Unit Price when change
   OperationID: OnChangeQuantityUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeQuantityUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQuantityUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeQuoteLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeQuoteLine
   Description: Get the defaults from the QuoteLine field on the HDCase record.
   OperationID: OnChangeQuoteLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeQuoteLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQuoteLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeQuoteNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeQuoteNum
   Description: Get the defaults from the QuoteNum field on the HDCase record.
   OperationID: OnChangeQuoteNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeQuoteNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQuoteNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeReqPerConID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeReqPerConID
   Description: Get the defaults from the ReqPerConID field on the HDCase record.
   OperationID: OnChangeReqPerConID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeReqPerConID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeReqPerConID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeReqPerConLnkRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeReqPerConLnkRowID
   Description: Get the defaults from the ReqPerConLnkRowID field on the HDCase record.
   OperationID: OnChangeReqPerConLnkRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeReqPerConLnkRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeReqPerConLnkRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeRevisionNum
   Description: Get the defaults from the RevisionNum field on the HDCase record.
   OperationID: OnChangeRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeRMALine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeRMALine
   Description: Get the defaults from the RMALine field on the HDCase record.
   OperationID: OnChangeRMALine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRMALine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRMALine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeRMANum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeRMANum
   Description: Get the defaults from the RMANum field on the HDCase record.
   OperationID: OnChangeRMANum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRMANum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRMANum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSearchCaseTopics(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSearchCaseTopics
   Description: Get the defaults 10 Topics fields
   OperationID: OnChangeSearchCaseTopics
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSearchCaseTopics_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSearchCaseTopics_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSearchTopics(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSearchTopics
   Description: Get the defaults 10 Topics fields
   OperationID: OnChangeSearchTopics
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSearchTopics_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSearchTopics_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSerialNoPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSerialNoPartNum
   Description: Get the PartNum from the SerialNumber field on the HDCase record.
   OperationID: GetSerialNoPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSerialNoPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSerialNoPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSerialNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSerialNumber
   Description: Get the defaults from the SerialNumber field on the HDCase record.
   OperationID: OnChangeSerialNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSerialNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSerialNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeShipToCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeShipToCustID
   Description: Get the defaults from the ShipToCustID field on the HDCase record.
   OperationID: OnChangeShipToCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTaskSetID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTaskSetID
   Description: Check for related task with mandatory milestones related to be completed
   OperationID: OnChangeTaskSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaskSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaskSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeShipToNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeShipToNum
   Description: Get the defaults from the ShipToNum field on the HDCase record.
   OperationID: OnChangeShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeShpConNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeShpConNum
   Description: Get the defaults from the ShpConNum field on the HDCase record.
   OperationID: OnChangeShpConNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeShpConNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeShpConNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTopics(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTopics
   Description: Get the defaults 10 Topics fields
   OperationID: OnChangeTopics
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTopics_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTopics_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeUnitPrice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeUnitPrice
   Description: Calculate de Ext Price
   OperationID: OnChangeUnitPrice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeUnitPrice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUnitPrice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeVenConNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeVenConNum
   Description: Get the defaults from the PrcConNum field on the HDCase record.
   OperationID: OnChangeVenConNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeVenConNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVenConNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeVendorID
   Description: Get the defaults from the VendorID field on the HDCase record.
   OperationID: OnChangeVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeWarrantyCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeWarrantyCode
   Description: Get the defaults from the WarrantyCode field on the HDCase record.
   OperationID: OnChangeWarrantyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWarrantyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWarrantyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeWFGroupID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeWFGroupID
   Description: Get the defaults from the WFGroupID field on the HDCase record.
   OperationID: OnChangeWFGroupID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWFGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWFGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OpenCloseCase(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OpenCloseCase
   Description: This method either opens or closes a Case and returns the updated object
   OperationID: OpenCloseCase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OpenCloseCase_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OpenCloseCase_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreOpenCloseCase(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreOpenCloseCase
   Description: This method is to be run before the OpenCloseCase method so that any questions
that need to be asked before the OpenCloseCase method can run can be asked
   OperationID: PreOpenCloseCase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreOpenCloseCase_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreOpenCloseCase_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateFSCallRequirements(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateFSCallRequirements
   Description: Validates if we have all the required data to create a FSCallLine.
   OperationID: ValidateFSCallRequirements
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateFSCallRequirements_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFSCallRequirements_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewHDCase(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewHDCase
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDCase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewHDCase_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDCase_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewHDCaseAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewHDCaseAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDCaseAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewHDCaseAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDCaseAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewHDCaseFSCall(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewHDCaseFSCall
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDCaseFSCall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewHDCaseFSCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDCaseFSCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewHDCaseJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewHDCaseJob
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDCaseJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewHDCaseJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDCaseJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewHDCaseLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewHDCaseLink
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDCaseLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewHDCaseLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDCaseLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewHDCaseOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewHDCaseOrder
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDCaseOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewHDCaseOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDCaseOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewHDCaseQuote(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewHDCaseQuote
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDCaseQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewHDCaseQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDCaseQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewHDCaseRMA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewHDCaseRMA
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDCaseRMA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewHDCaseRMA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDCaseRMA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewHDChildCases(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewHDChildCases
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDChildCases
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewHDChildCases_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDChildCases_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewHDContact(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewHDContact
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDContact
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewHDContact_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDContact_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewHDCaseMaintReq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewHDCaseMaintReq
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewHDCaseMaintReq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewHDCaseMaintReq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewHDCaseMaintReq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.HelpDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_HDCaseAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseFSCallRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_HDCaseFSCallRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseJobRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_HDCaseJobRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseLinkRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_HDCaseLinkRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_HDCaseListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseMaintReqRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_HDCaseMaintReqRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseOrderRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_HDCaseOrderRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseQuoteRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_HDCaseQuoteRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseRMARow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_HDCaseRMARow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDCaseRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_HDCaseRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDChildCasesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_HDChildCasesRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_HDContactRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_HDContactRow] = obj["value"]
      pass

class Erp_Tablesets_HDCaseAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.HDCaseNum:int = obj["HDCaseNum"]
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

class Erp_Tablesets_HDCaseFSCallRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  When creating a new Service Call the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this service call.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDCaseJobRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  """  
      self.JobType:str = obj["JobType"]
      """  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this job.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDCaseLinkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  A unique help desk case number.  This number is system generated when the help desk case is created.  """  
      self.ExternalLink:bool = obj["ExternalLink"]
      """  If true this is an external link that was manually entered.  Internal links will refer to other database records.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  Identifies the master file to which the link is related.  If an external link this will be blank.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record.  """  
      self.Key2:str = obj["Key2"]
      """  2nd component of the foreign key to the related master record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  """  
      self.Key4:str = obj["Key4"]
      """  4th component of the foreign key to the related master record.  """  
      self.Key5:str = obj["Key5"]
      """  5th component of the foreign key to the related master record.  """  
      self.Description:str = obj["Description"]
      """  Description of the link contents.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDCaseListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  A unique help desk case number.  This number is system generated when the help desk case is created.  """  
      self.CustNum:int = obj["CustNum"]
      """  The customer associated with this case.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The customer ship-to associate with the Help Desk case.  This is used with the ShpConNum to reference a contact in the CustCont table.  """  
      self.ParentCase:int = obj["ParentCase"]
      """  The parent Help Desk case number of this case.  """  
      self.Description:str = obj["Description"]
      """  The description of the case issue.  """  
      self.ResolutionText:str = obj["ResolutionText"]
      """  A description if the resolution for the case.  """  
      self.PublishedText:str = obj["PublishedText"]
      """  Publishable text of the issue and resolution of the case.  """  
      self.PublishedSummary:str = obj["PublishedSummary"]
      """  A summary of the issue/resolution of the help desk case.  """  
      self.KBEntry:bool = obj["KBEntry"]
      """  If true this is a Knowledge Base entry.  """  
      self.PublishedItem:bool = obj["PublishedItem"]
      """  If true this item can be published.  If false this item is for internal use only.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part that is associated with this Help Desk case.  The part is in the Part table.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  An serial number associated with the Help Desk case.  The serial number is in the SerialNo table.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  The Quote associated with the Help Desk case.  The Quote is in the QuoteHed table.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The order associated with the Help Desk case.  The order is in the OrderHed table.  """  
      self.CaseOwner:str = obj["CaseOwner"]
      """  The SalesRepCode of the owner of the Help Desk case.  The people are stored in the SalesRep table.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date which this Help Desk case was created.  Not maintainable by the user.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  UserID who created the Help Desk case.  Not maintainable by the user.  """  
      self.CreatedTime:int = obj["CreatedTime"]
      """  The time (in milliseconds) that the Help Desk case was created.  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  UserID who last updated the Help Desk case.  Not maintainable by the user.  """  
      self.LastUpdatedDate:str = obj["LastUpdatedDate"]
      """  Date which this Help Desk case was last updated.  Not maintainable by the user.  """  
      self.LastUpdatedTime:int = obj["LastUpdatedTime"]
      """  The time (in milliseconds) that the Help Desk case was last updated.  Not maintainable by the user.  """  
      self.TopicID1:str = obj["TopicID1"]
      """  A unique identifier for the Help Desk Topic.  This is a top level topic (no parents).  """  
      self.TopicID2:str = obj["TopicID2"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID1.  """  
      self.TopicID3:str = obj["TopicID3"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID2.  """  
      self.TopicID4:str = obj["TopicID4"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID3.  """  
      self.TopicID5:str = obj["TopicID5"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID4.  """  
      self.TopicID6:str = obj["TopicID6"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID5.  """  
      self.TopicID7:str = obj["TopicID7"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID6.  """  
      self.TopicID8:str = obj["TopicID8"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID7.  """  
      self.TopicID9:str = obj["TopicID9"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID8.  """  
      self.TopicID10:str = obj["TopicID10"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID9.  """  
      self.CaseTopics:str = obj["CaseTopics"]
      """  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  """  
      self.Quantity:int = obj["Quantity"]
      """  A general quantity field.  """  
      self.QuantityUOM:str = obj["QuantityUOM"]
      """   Unit of Measure which qualifies the HDCase.Quantity.
Mandatory. Must be a valid UOM.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The quote line number  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Customer Name  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this Service call is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line that holds the warranty information for this service call  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.CompletedBy:str = obj["CompletedBy"]
      """  Case Completed By  """  
      self.CompletionDate:str = obj["CompletionDate"]
      """  Case Completion Date  """  
      self.CompletionTime:int = obj["CompletionTime"]
      """  Case Completion Time  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit price for the PartNum.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Same as UnitPrice except that this field contains the unit price in the case currency.  """  
      self.Rp1ExtPrice:int = obj["Rp1ExtPrice"]
      """  Extended Price in Report currency 1.  """  
      self.Rp2ExtPrice:int = obj["Rp2ExtPrice"]
      """  Extended Price in Report currency 2.  """  
      self.CaseTypeID:str = obj["CaseTypeID"]
      """  Unique identifier of the case type.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttrCodeList:str = obj["AttrCodeList"]
      """  Case attribute code list  """  
      self.IssueSummary:str = obj["IssueSummary"]
      """  Short summary if the issue  """  
      self.IssueText:str = obj["IssueText"]
      """  Long issue description  """  
      self.DispCreateTime:str = obj["DispCreateTime"]
      """  String version of the creation time  """  
      self.DispLastUpdateTime:str = obj["DispLastUpdateTime"]
      """  String version of the last update time  """  
      self.CaseOwnerName:str = obj["CaseOwnerName"]
      """  Name  """  
      self.CaseCode:str = obj["CaseCode"]
      self.NextReviewDate:str = obj["NextReviewDate"]
      self.EvaluationStatus:str = obj["EvaluationStatus"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDCaseMaintReqRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.ReqID:str = obj["ReqID"]
      """  System assigned number. Component of the unique index. In the format of yyyymmddnnnn. yyyymmdd is the current year, month, day. nnnn is the next sequential number within the company/Site/yyyymmdd.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  A unique help desk case number.  This number is system generated when the help desk case is created.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDCaseOrderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this order.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.Project_c:str = obj["Project_c"]
      self.OriginalOrderNo_c:int = obj["OriginalOrderNo_c"]
      self.MASFlag_c:bool = obj["MASFlag_c"]
      self.Estimate_c:bool = obj["Estimate_c"]
      self.ShipOrderComplete_c:bool = obj["ShipOrderComplete_c"]
      self.ProjectID_c:str = obj["ProjectID_c"]
      self.PhaseID_c:str = obj["PhaseID_c"]
      self.SalesCatID__c:str = obj["SalesCatID__c"]
      self.TaxCatID_c:str = obj["TaxCatID_c"]
      self.MfgOrder_c:bool = obj["MfgOrder_c"]
      pass

class Erp_Tablesets_HDCaseQuoteRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number is an integer which is used to uniquely identify a quote within the system.  This is automatically assigned by the system when the user requests to create a new quote. To create a new quote the user either takes an "add" option or leaves the Quote Number fill-in zero. The system generates a number by finding the quote number of the last record on file and then a 1 to it. It then uses the greater of Last quote number + 1 or the EQSyst.StartQuoteNum.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this quote.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDCaseRMARow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RMANum:int = obj["RMANum"]
      """  When creating a new Return Authorization the user is prompted for a Return number. If the field is zero , the next available # is assigned by the system. The system generates a number by finding the last CRAHead on file and uses its RANum + 1.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this RMA.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDCaseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  A unique help desk case number.  This number is system generated when the help desk case is created.  """  
      self.CustNum:int = obj["CustNum"]
      """  The customer associated with this case.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The customer ship-to associate with the Help Desk case.  This is used with the ShpConNum to reference a contact in the CustCont table.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Customer contact number.  This is used with the ShipToNum to reference a contact in the CustCont table.  """  
      self.ParentCase:int = obj["ParentCase"]
      """  The parent Help Desk case number of this case.  """  
      self.Description:str = obj["Description"]
      """  The description of the case issue.  """  
      self.ResolutionText:str = obj["ResolutionText"]
      """  A description if the resolution for the case.  """  
      self.PublishedText:str = obj["PublishedText"]
      """  Publishable text of the issue and resolution of the case.  """  
      self.PublishedSummary:str = obj["PublishedSummary"]
      """  A summary of the issue/resolution of the help desk case.  """  
      self.KBEntry:bool = obj["KBEntry"]
      """  If true this is a Knowledge Base entry.  """  
      self.PublishedItem:bool = obj["PublishedItem"]
      """  If true this item can be published.  If false this item is for internal use only.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part that is associated with this Help Desk case.  The part is in the Part table.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  An serial number associated with the Help Desk case.  The serial number is in the SerialNo table.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  The Quote associated with the Help Desk case.  The Quote is in the QuoteHed table.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The order associated with the Help Desk case.  The order is in the OrderHed table.  """  
      self.CallNum:int = obj["CallNum"]
      """  A Field Service call that is associated with the Help Desk case.  The field service call is in the FSCallHd table.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  A Service Contract associated with the Help Desk case.  The service contract is in the FSContHd table.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  The warranty associated with the Help Desk case.  The warranty is in the FSWarrCd table.  """  
      self.Priority:int = obj["Priority"]
      """  The priority of the Help Desk case  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set.  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  The identifier of the workflow stage.  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active milestone task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.CaseOwner:str = obj["CaseOwner"]
      """  The SalesRepCode of the owner of the Help Desk case.  The people are stored in the SalesRep table.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  This indicates if the workflow for this case is complete.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date which this Help Desk case was created.  Not maintainable by the user.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  UserID who created the Help Desk case.  Not maintainable by the user.  """  
      self.CreatedTime:int = obj["CreatedTime"]
      """  The time (in milliseconds) that the Help Desk case was created.  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  UserID who last updated the Help Desk case.  Not maintainable by the user.  """  
      self.LastUpdatedDate:str = obj["LastUpdatedDate"]
      """  Date which this Help Desk case was last updated.  Not maintainable by the user.  """  
      self.LastUpdatedTime:int = obj["LastUpdatedTime"]
      """  The time (in milliseconds) that the Help Desk case was last updated.  Not maintainable by the user.  """  
      self.TopicID1:str = obj["TopicID1"]
      """  A unique identifier for the Help Desk Topic.  This is a top level topic (no parents).  """  
      self.TopicID2:str = obj["TopicID2"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID1.  """  
      self.TopicID3:str = obj["TopicID3"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID2.  """  
      self.TopicID4:str = obj["TopicID4"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID3.  """  
      self.TopicID5:str = obj["TopicID5"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID4.  """  
      self.TopicID6:str = obj["TopicID6"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID5.  """  
      self.TopicID7:str = obj["TopicID7"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID6.  """  
      self.TopicID8:str = obj["TopicID8"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID7.  """  
      self.TopicID9:str = obj["TopicID9"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID8.  """  
      self.TopicID10:str = obj["TopicID10"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID9.  """  
      self.CaseTopics:str = obj["CaseTopics"]
      """  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  Link to the Marketing Campaign related to this Help Desk case.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  Link to the marketing event associated with this Help Desk case.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  """  
      self.Quantity:int = obj["Quantity"]
      """  A general quantity field.  """  
      self.QuantityUOM:str = obj["QuantityUOM"]
      """   Unit of Measure which qualifies the HDCase.Quantity.
Mandatory. Must be a valid UOM.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The order release number.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The quote line number  """  
      self.CallLine:int = obj["CallLine"]
      """  Field service call line number  """  
      self.RMANum:int = obj["RMANum"]
      """  The RMA Number.  """  
      self.RMALine:int = obj["RMALine"]
      """  The RMA line number.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Customer Name  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this Service call is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line that holds the warranty information for this service call  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.CompletedBy:str = obj["CompletedBy"]
      """  Case Completed By  """  
      self.CompletionDate:str = obj["CompletionDate"]
      """  Case Completion Date  """  
      self.CompletionTime:int = obj["CompletionTime"]
      """  Case Completion Time  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  The drop shipment packing slip number that this Service call is linked with  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  The drop shipment packing slip line that holds the warranty information for this service call  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier number of the drop shipment and part of the primary key of a drop shipment line.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point id of the drop shipment and part of the primary key of a drop shipment line.  """  
      self.EquipID:str = obj["EquipID"]
      """  Related Equip.EquipID.  """  
      self.EmpID:str = obj["EmpID"]
      """  Unique identifier of the primary Employee contact.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  Unique identifier of the primary Buyer contact.  """  
      self.VendorNumCon:int = obj["VendorNumCon"]
      """  Unique identifier of the Primary Vendor contact.  """  
      self.PurPointCon:str = obj["PurPointCon"]
      """  Unique identifier of the Primary Vendor PP contact.  """  
      self.VenConNum:int = obj["VenConNum"]
      """  Unique identifier of the Primary Vendor contact num.  """  
      self.PurPointConNum:int = obj["PurPointConNum"]
      """  Contact number.  Unique identifier for the Primary Purchase Point contact record.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit price for the PartNum.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Same as UnitPrice except that this field contains the unit price in the case currency.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Unit Price in Report currency 1.  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Unit Price in Report currency 2.  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Unit Price in Report currency 3.  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended price. Calculated as Quantity * (UnitPrice / PFactor).  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Same as ExtPrice except that this field contains the extended price in the case currency.  """  
      self.Rp1ExtPrice:int = obj["Rp1ExtPrice"]
      """  Extended Price in Report currency 1.  """  
      self.Rp2ExtPrice:int = obj["Rp2ExtPrice"]
      """  Extended Price in Report currency 2.  """  
      self.Rp3ExtPrice:int = obj["Rp3ExtPrice"]
      """  Extended Price in Report currency 3.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Type Code  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that will be used for this role code entry.  """  
      self.CaseTypeID:str = obj["CaseTypeID"]
      """  Unique identifier of the case type.  """  
      self.PONum:int = obj["PONum"]
      """  This field will mainly be used when a part is found to be faulty and the purchase order and receipt that were used for the part need to be recorded  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Link to the territory ID.  """  
      self.POLine:int = obj["POLine"]
      """  This field will mainly be used when a part is found to be faulty and the purchase order and receipt that were used for the part need to be recorded  """  
      self.WorkflowType:str = obj["WorkflowType"]
      """  The type of workflow.  """  
      self.POPackSlip:str = obj["POPackSlip"]
      """  This field will mainly be used when a part is found to be faulty and the purchase order and receipt that were used for the part need to be recorded  """  
      self.POPackLine:int = obj["POPackLine"]
      """  This field will mainly be used when a part is found to be faulty and the purchase order and receipt that were used for the part need to be recorded  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HDCaseStatus:str = obj["HDCaseStatus"]
      """  HDCaseStatus  """  
      self.ReqPerConID:int = obj["ReqPerConID"]
      """  ReqPerConID  """  
      self.PerConID:int = obj["PerConID"]
      """  PerConID  """  
      self.WebCase:bool = obj["WebCase"]
      """  Case was initiated from the web  """  
      self.WebComment:str = obj["WebComment"]
      """  Comment used for discussion through web  """  
      self.IDNum:str = obj["IDNum"]
      """  Identification Number of related Location Inventory record.  """  
      self.LocationNum:int = obj["LocationNum"]
      """  Unique ID Num of related Location Inventory record.  """  
      self.ContractLine:int = obj["ContractLine"]
      """  Field service contract line number. The service contract line is in the FSContDt table.  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.FSMCurrentStatus:str = obj["FSMCurrentStatus"]
      """  FSMCurrentStatus  """  
      self.FSMServiceReportID:str = obj["FSMServiceReportID"]
      """  FSMServiceReportID  """  
      self.FSMNumberOfFollowups:int = obj["FSMNumberOfFollowups"]
      """  FSMNumberOfFollowups  """  
      self.FSMReceivedBy:str = obj["FSMReceivedBy"]
      """  FSMReceivedBy  """  
      self.FSMOriginalScheduleDate:str = obj["FSMOriginalScheduleDate"]
      """  FSMOriginalScheduleDate  """  
      self.FSMCompletedDate:str = obj["FSMCompletedDate"]
      """  FSMCompletedDate  """  
      self.AllowMilestoneUpdate:bool = obj["AllowMilestoneUpdate"]
      """  If true the MilestoneSeq field can be modified  """  
      self.AttrCodeList:str = obj["AttrCodeList"]
      """  Case attribute code list  """  
      self.AvailablePrcConNum:str = obj["AvailablePrcConNum"]
      """  Available PrcConNum values  """  
      self.AvailablePurPointConNum:str = obj["AvailablePurPointConNum"]
      """  Available AvailablePurPointConNum values  """  
      self.AvailableShpConNum:str = obj["AvailableShpConNum"]
      """  Available ShpConNum values  """  
      self.AvailableTaskSets:str = obj["AvailableTaskSets"]
      """  a delimited list of Task Sets that can be selected in the TaskSetId field  """  
      self.AvailableVenConNum:str = obj["AvailableVenConNum"]
      """  Available AvailableVenConNum values  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CaseCode:str = obj["CaseCode"]
      """  Code of the event. Selected from predefined list of codes.  """  
      self.CaseStatus:str = obj["CaseStatus"]
      """  Indicates the current status of the case.  """  
      self.ChildCases:str = obj["ChildCases"]
      """  List of children linked to the case. Case numbers are separated by commas.  """  
      self.CurrentMilestone:int = obj["CurrentMilestone"]
      """  The current milestone in tasks  """  
      self.CurrentMilestoneDesc:str = obj["CurrentMilestoneDesc"]
      """  Description of current milestone.  """  
      self.CustCntCorpName:str = obj["CustCntCorpName"]
      self.CustCntEMail:str = obj["CustCntEMail"]
      self.CustCntFaxNum:str = obj["CustCntFaxNum"]
      self.CustCntFirstName:str = obj["CustCntFirstName"]
      self.CustCntLastName:str = obj["CustCntLastName"]
      self.CustCntMiddleName:str = obj["CustCntMiddleName"]
      self.CustCntName:str = obj["CustCntName"]
      self.CustCntPhoneNum:str = obj["CustCntPhoneNum"]
      self.CustomerRequiresPO:bool = obj["CustomerRequiresPO"]
      """  If true the customer requires a unique PO on Sales Orders  """  
      self.DispCreateTime:str = obj["DispCreateTime"]
      """  String version of the creation time  """  
      self.DispLastUpdateTime:str = obj["DispLastUpdateTime"]
      """  String version of the last update time  """  
      self.DropShip:bool = obj["DropShip"]
      self.EvaluationStatus:str = obj["EvaluationStatus"]
      """  Evaluation status of the event. Possible values are user defined.  """  
      self.EvaluationStatusDesc:str = obj["EvaluationStatusDesc"]
      """  Description of Evaluation Status  """  
      self.HDCaseNumString:str = obj["HDCaseNumString"]
      """  String version of HDCaseNum (used for relationships)  """  
      self.Inactive:bool = obj["Inactive"]
      self.IssueSummary:str = obj["IssueSummary"]
      """  Short summary if the issue  """  
      self.IssueText:str = obj["IssueText"]
      """  Long issue description  """  
      self.NextReviewDate:str = obj["NextReviewDate"]
      """  Date of the next review.  """  
      self.PartSalesUM:str = obj["PartSalesUM"]
      """  The SalesUM of the part  """  
      self.PPCntEmailAddress:str = obj["PPCntEmailAddress"]
      self.PPCntFaxNum:str = obj["PPCntFaxNum"]
      self.PPCntName:str = obj["PPCntName"]
      self.PPCntPhoneNum:str = obj["PPCntPhoneNum"]
      self.PricePerCode:str = obj["PricePerCode"]
      self.PurPointConName:str = obj["PurPointConName"]
      self.ReqContextLink:str = obj["ReqContextLink"]
      """  Requestor Context Link  """  
      self.ReqPerConLnkID1:str = obj["ReqPerConLnkID1"]
      """  Holds the first ID for the linked record.  """  
      self.ReqPerConLnkID2:str = obj["ReqPerConLnkID2"]
      """  Holds the second ID for the linked record. Used with compound key records like ShipTo or PurPoint.  """  
      self.ReqPerConLnkName:str = obj["ReqPerConLnkName"]
      """  The display name for the link.  """  
      self.ReqPerConLnkRowID:str = obj["ReqPerConLnkRowID"]
      """  The SysRowId of the linked PerConLnk.  """  
      self.ReqPerConName:str = obj["ReqPerConName"]
      """  Requestor PerCon Name  """  
      self.ReqPrimary:bool = obj["ReqPrimary"]
      """  Requestor is primary contact.  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Extended Price in Report currency 1.  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Extended Price in Report currency 2.  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Extended Price in Report currency 3.  """  
      self.ShipCntCorpName:str = obj["ShipCntCorpName"]
      self.ShipCntEMail:str = obj["ShipCntEMail"]
      self.ShipCntFaxNum:str = obj["ShipCntFaxNum"]
      self.ShipCntFirstName:str = obj["ShipCntFirstName"]
      self.ShipCntLastName:str = obj["ShipCntLastName"]
      self.ShipCntMiddleName:str = obj["ShipCntMiddleName"]
      self.ShipCntName:str = obj["ShipCntName"]
      self.ShipCntPhoneNum:str = obj["ShipCntPhoneNum"]
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  Customer Id of the third-party Ship To  """  
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.TargetUOM:str = obj["TargetUOM"]
      """  TargetUOM  """  
      self.TaskCompletePasswordIsValid:bool = obj["TaskCompletePasswordIsValid"]
      """  A flag to indicate the user password was validated  """  
      self.TaskCompletePasswordRequired:bool = obj["TaskCompletePasswordRequired"]
      """  Indicates if a the user password should be validated to complete a task  """  
      self.VendCntEmailAddress:str = obj["VendCntEmailAddress"]
      self.VendCntFaxNum:str = obj["VendCntFaxNum"]
      self.VendCntName:str = obj["VendCntName"]
      self.VendCntPhoneNum:str = obj["VendCntPhoneNum"]
      self.WebQuoteNum:int = obj["WebQuoteNum"]
      """  The Quote Num that created a case number from the web  """  
      self.AvailableMilestones:str = obj["AvailableMilestones"]
      """  The available next milestones for the MilestoneSeq.  """  
      self.FSMCurrentStatusDesc:str = obj["FSMCurrentStatusDesc"]
      """  Translated description of current FSM status for FSM related cases  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ActiveTaskIDTaskDescription:str = obj["ActiveTaskIDTaskDescription"]
      self.BuyerIDName:str = obj["BuyerIDName"]
      self.CaseOwnerName:str = obj["CaseOwnerName"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      self.DropShipDtlLineDesc:str = obj["DropShipDtlLineDesc"]
      self.EmpIDName:str = obj["EmpIDName"]
      self.EquipIDDescription:str = obj["EquipIDDescription"]
      self.LastTaskIDTaskDescription:str = obj["LastTaskIDTaskDescription"]
      self.LocationInventoryLotNum:str = obj["LocationInventoryLotNum"]
      self.LocationInventorySerialNumber:str = obj["LocationInventorySerialNumber"]
      self.LocationInventoryIDNum:str = obj["LocationInventoryIDNum"]
      self.MktgCampaignIDCampDescription:str = obj["MktgCampaignIDCampDescription"]
      self.MktgEventEvntDescription:str = obj["MktgEventEvntDescription"]
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.ShipToCustNumName:str = obj["ShipToCustNumName"]
      self.ShipToCustNumCustID:str = obj["ShipToCustNumCustID"]
      self.TaskSetIDWorkflowType:str = obj["TaskSetIDWorkflowType"]
      self.TaskSetIDTaskSetDescription:str = obj["TaskSetIDTaskSetDescription"]
      self.TerritoryIDTerritoryDesc:str = obj["TerritoryIDTerritoryDesc"]
      self.VendorNumConVendorID:str = obj["VendorNumConVendorID"]
      self.VendorNumConName:str = obj["VendorNumConName"]
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      self.WFGroupIDDescription:str = obj["WFGroupIDDescription"]
      self.WFStageIDDescription:str = obj["WFStageIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDChildCasesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  A unique help desk case number.  This number is system generated when the help desk case is created.  """  
      self.CustNum:int = obj["CustNum"]
      """  The customer associated with this case.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The customer ship-to associate with the Help Desk case.  This is used with the ShpConNum to reference a contact in the CustCont table.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Customer contact number.  This is used with the ShipToNum to reference a contact in the CustCont table.  """  
      self.ParentCase:int = obj["ParentCase"]
      """  The parent Help Desk case number of this case.  """  
      self.Description:str = obj["Description"]
      """  The description of the case issue.  """  
      self.ResolutionText:str = obj["ResolutionText"]
      """  A description if the resolution for the case.  """  
      self.PublishedText:str = obj["PublishedText"]
      """  Publishable text of the issue and resolution of the case.  """  
      self.PublishedSummary:str = obj["PublishedSummary"]
      """  A summary of the issue/resolution of the help desk case.  """  
      self.KBEntry:bool = obj["KBEntry"]
      """  If true this is a Knowledge Base entry.  """  
      self.PublishedItem:bool = obj["PublishedItem"]
      """  If true this item can be published.  If false this item is for internal use only.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part that is associated with this Help Desk case.  The part is in the Part table.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  An serial number associated with the Help Desk case.  The serial number is in the SerialNo table.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  The Quote associated with the Help Desk case.  The Quote is in the QuoteHed table.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The order associated with the Help Desk case.  The order is in the OrderHed table.  """  
      self.CallNum:int = obj["CallNum"]
      """  A Field Service call that is associated with the Help Desk case.  The field service call is in the FSCallHd table.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  A Service Contract associated with the Help Desk case.  The service contract is in the FSContHd table.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  The warranty associated with the Help Desk case.  The warranty is in the FSWarrCd table.  """  
      self.Priority:int = obj["Priority"]
      """  The priority of the Help Desk case  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set.  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  The identifier of the workflow stage.  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active milestone task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.CaseOwner:str = obj["CaseOwner"]
      """  The SalesRepCode of the owner of the Help Desk case.  The people are stored in the SalesRep table.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  This indicates if the workflow for this case is complete.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date which this Help Desk case was created.  Not maintainable by the user.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  UserID who created the Help Desk case.  Not maintainable by the user.  """  
      self.CreatedTime:int = obj["CreatedTime"]
      """  The time (in milliseconds) that the Help Desk case was created.  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  UserID who last updated the Help Desk case.  Not maintainable by the user.  """  
      self.LastUpdatedDate:str = obj["LastUpdatedDate"]
      """  Date which this Help Desk case was last updated.  Not maintainable by the user.  """  
      self.LastUpdatedTime:int = obj["LastUpdatedTime"]
      """  The time (in milliseconds) that the Help Desk case was last updated.  Not maintainable by the user.  """  
      self.TopicID1:str = obj["TopicID1"]
      """  A unique identifier for the Help Desk Topic.  This is a top level topic (no parents).  """  
      self.TopicID2:str = obj["TopicID2"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID1.  """  
      self.TopicID3:str = obj["TopicID3"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID2.  """  
      self.TopicID4:str = obj["TopicID4"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID3.  """  
      self.TopicID5:str = obj["TopicID5"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID4.  """  
      self.TopicID6:str = obj["TopicID6"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID5.  """  
      self.TopicID7:str = obj["TopicID7"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID6.  """  
      self.TopicID8:str = obj["TopicID8"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID7.  """  
      self.TopicID9:str = obj["TopicID9"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID8.  """  
      self.TopicID10:str = obj["TopicID10"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID9.  """  
      self.CaseTopics:str = obj["CaseTopics"]
      """  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  Link to the Marketing Campaign related to this Help Desk case.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  Link to the marketing event associated with this Help Desk case.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  """  
      self.Quantity:int = obj["Quantity"]
      """  A general quantity field.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The order release number.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The quote line number  """  
      self.CallLine:int = obj["CallLine"]
      """  Field service call line number  """  
      self.RMANum:int = obj["RMANum"]
      """  The RMA Number.  """  
      self.RMALine:int = obj["RMALine"]
      """  The RMA line number.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Customer Name  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustCntEMail:str = obj["CustCntEMail"]
      self.ShipCntEMail:str = obj["ShipCntEMail"]
      self.BitFlag:int = obj["BitFlag"]
      self.CaseOwnerName:str = obj["CaseOwnerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDContactRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  A unique help desk case number.  """  
      self.PerConLnkRowID:str = obj["PerConLnkRowID"]
      """  The SysRowId of the linked PerConLnk.  """  
      self.Primary:bool = obj["Primary"]
      """  Primary contact for each Context type. Only one allowed per context type.  The primary contact for each context type is shown on the detail sheet.  """  
      self.Comment:str = obj["Comment"]
      """  User entered comments.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Requestor:bool = obj["Requestor"]
      """  Specifies the identifier for the contact who requested the case entry.  """  
      self.Name:str = obj["Name"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      self.Zip:str = obj["Zip"]
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.ContextLink:str = obj["ContextLink"]
      self.BuyerID:str = obj["BuyerID"]
      self.BuyerName:str = obj["BuyerName"]
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.EmpID:str = obj["EmpID"]
      self.EmpName:str = obj["EmpName"]
      self.PurPoint:str = obj["PurPoint"]
      self.PurPointName:str = obj["PurPointName"]
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.VendorID:str = obj["VendorID"]
      self.VendorName:str = obj["VendorName"]
      self.Selected:bool = obj["Selected"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangedTaskSet_input:
   """ Required : 
   retainTask
   ds
   """  
   def __init__(self, obj):
      self.retainTask:bool = obj["retainTask"]
      """  Retain Task  """  
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class ChangedTaskSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.currTaskSeqNum:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPrePartInfo_input:
   """ Required : 
   vPartNum
   """  
   def __init__(self, obj):
      self.vPartNum:str = obj["vPartNum"]
      """  The input-output part number to validate and it gets returned  """  
      pass

class CheckPrePartInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vPartNum:str = obj["parameters"]
      self.vSubPartMsg:str = obj["parameters"]
      self.vSubAvail:bool = obj["vSubAvail"]
      self.vMsgType:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckProjectID_input:
   """ Required : 
   helpDeskCaseNum
   projectID
   relatedTo
   jobNum
   """  
   def __init__(self, obj):
      self.helpDeskCaseNum:int = obj["helpDeskCaseNum"]
      """  The Help Desk case number to use as a source  """  
      self.projectID:str = obj["projectID"]
      """  ProjectID to be validated  """  
      self.relatedTo:str = obj["relatedTo"]
      """  Entity that will be used to validate the ProjectID  """  
      self.jobNum:str = obj["jobNum"]
      """  Job to be updated with the new ProjectID and ContractID  """  
      pass

class CheckProjectID_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.contractID:str = obj["parameters"]
      self.errorMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ContractHasLines_input:
   """ Required : 
   ds
   proposedContractNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedContractNum:int = obj["proposedContractNum"]
      """  The proposed ContractNum  """  
      pass

class ContractHasLines_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateFSCallLine_input:
   """ Required : 
   helpDeskCaseNum
   callCode
   ds
   """  
   def __init__(self, obj):
      self.helpDeskCaseNum:int = obj["helpDeskCaseNum"]
      """  The Help Desk case number to use as a source  """  
      self.callCode:str = obj["callCode"]
      """  The call code to be used for the Field Service call  """  
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class CreateFSCallLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newCallNum:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateFSCall_input:
   """ Required : 
   helpDeskCaseNum
   callCode
   ds
   """  
   def __init__(self, obj):
      self.helpDeskCaseNum:int = obj["helpDeskCaseNum"]
      """  The Help Desk case number to use as a source  """  
      self.callCode:str = obj["callCode"]
      """  The call code to be used for the Field Service call  """  
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class CreateFSCall_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newCallNum:int = obj["parameters"]
      self.validPackingSlip:bool = obj["validPackingSlip"]
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateJob_input:
   """ Required : 
   helpDeskCaseNum
   optionTool
   ds
   """  
   def __init__(self, obj):
      self.helpDeskCaseNum:int = obj["helpDeskCaseNum"]
      """  The Help Desk case number to use as a source  """  
      self.optionTool:str = obj["optionTool"]
      """  Action Menu Option  """  
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class CreateJob_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newJobNum:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateMaintReq_input:
   """ Required : 
   helpDeskCaseNum
   ds
   """  
   def __init__(self, obj):
      self.helpDeskCaseNum:int = obj["helpDeskCaseNum"]
      """  The Help Desk case number to use as a source  """  
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class CreateMaintReq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newReqID:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateOrderWithLine_input:
   """ Required : 
   helpDeskCaseNum
   orderPONum
   contractID
   ds
   """  
   def __init__(self, obj):
      self.helpDeskCaseNum:int = obj["helpDeskCaseNum"]
      """  The Help Desk case number to use as a source  """  
      self.orderPONum:str = obj["orderPONum"]
      self.contractID:str = obj["contractID"]
      """  Fill if we want to set any Contract in the Line  """  
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class CreateOrderWithLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newOrderNum:int = obj["parameters"]
      self.errorType:int = obj["parameters"]
      self.errorMsg:str = obj["parameters"]
      self.orderDtlSysRowID:str = obj["parameters"]
      self.smartString:str = obj["parameters"]
      self.smartStringProcessed:bool = obj["smartStringProcessed"]
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateOrder_input:
   """ Required : 
   helpDeskCaseNum
   orderPONum
   ds
   """  
   def __init__(self, obj):
      self.helpDeskCaseNum:int = obj["helpDeskCaseNum"]
      """  The Help Desk case number to use as a source  """  
      self.orderPONum:str = obj["orderPONum"]
      """  The PO number to use on the order. (This may be required by the customer)  """  
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class CreateOrder_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newOrderNum:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateQuoteWithLine_input:
   """ Required : 
   helpDeskCaseNum
   contractID
   ds
   """  
   def __init__(self, obj):
      self.helpDeskCaseNum:int = obj["helpDeskCaseNum"]
      """  The Help Desk case number to use as a source  """  
      self.contractID:str = obj["contractID"]
      """  Fill if we want to set any Contract in the Line  """  
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class CreateQuoteWithLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newQuoteNum:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateQuote_input:
   """ Required : 
   helpDeskCaseNum
   ds
   """  
   def __init__(self, obj):
      self.helpDeskCaseNum:int = obj["helpDeskCaseNum"]
      """  The Help Desk case number to use as a source  """  
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class CreateQuote_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newQuoteNum:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateRMALine_input:
   """ Required : 
   helpDeskCaseNum
   reasonCode
   serialNumber
   ds
   """  
   def __init__(self, obj):
      self.helpDeskCaseNum:int = obj["helpDeskCaseNum"]
      self.reasonCode:str = obj["reasonCode"]
      self.serialNumber:str = obj["serialNumber"]
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class CreateRMALine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newRMANum:int = obj["parameters"]
      self.SNErrorMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateRMAUpdConNum_input:
   """ Required : 
   helpDeskCaseNum
   ds
   """  
   def __init__(self, obj):
      self.helpDeskCaseNum:int = obj["helpDeskCaseNum"]
      """  The Help Desk case number to use as a source  """  
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class CreateRMAUpdConNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newRMANum:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateRMA_input:
   """ Required : 
   helpDeskCaseNum
   ds
   """  
   def __init__(self, obj):
      self.helpDeskCaseNum:int = obj["helpDeskCaseNum"]
      """  The Help Desk case number to use as a source  """  
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class CreateRMA_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newRMANum:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   hdCaseNum
   """  
   def __init__(self, obj):
      self.hdCaseNum:int = obj["hdCaseNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteFSCallhdLink_input:
   """ Required : 
   helpDeskCaseNum
   callNum
   """  
   def __init__(self, obj):
      self.helpDeskCaseNum:int = obj["helpDeskCaseNum"]
      """  The Help Desk case number to use as a source  """  
      self.callNum:int = obj["callNum"]
      """  The linked fscall number  """  
      pass

class DeleteFSCallhdLink_output:
   def __init__(self, obj):
      pass

class DeleteHDCaseExternalLink_input:
   """ Required : 
   helpDeskCaseNum
   """  
   def __init__(self, obj):
      self.helpDeskCaseNum:int = obj["helpDeskCaseNum"]
      """  The Help Desk case number to use as a source  """  
      pass

class DeleteHDCaseExternalLink_output:
   def __init__(self, obj):
      pass

class DeleteHDChildCaseLink_input:
   """ Required : 
   hdChildCaseNum
   """  
   def __init__(self, obj):
      self.hdChildCaseNum:int = obj["hdChildCaseNum"]
      """  The Help Desk case number to use as a source  """  
      pass

class DeleteHDChildCaseLink_output:
   def __init__(self, obj):
      pass

class DeleteJobHeadLink_input:
   """ Required : 
   helpDeskCaseNum
   jobNum
   """  
   def __init__(self, obj):
      self.helpDeskCaseNum:int = obj["helpDeskCaseNum"]
      """  The Help Desk case number to use as a source  """  
      self.jobNum:str = obj["jobNum"]
      """  The linked job number  """  
      pass

class DeleteJobHeadLink_output:
   def __init__(self, obj):
      pass

class DeleteMaintReqLink_input:
   """ Required : 
   helpDeskCaseNum
   reqID
   """  
   def __init__(self, obj):
      self.helpDeskCaseNum:int = obj["helpDeskCaseNum"]
      """  The Help Desk case number to use as a source  """  
      self.reqID:str = obj["reqID"]
      """  The linked maint req number  """  
      pass

class DeleteMaintReqLink_output:
   def __init__(self, obj):
      pass

class DeleteOrderHedLink_input:
   """ Required : 
   helpDeskCaseNum
   orderNum
   """  
   def __init__(self, obj):
      self.helpDeskCaseNum:int = obj["helpDeskCaseNum"]
      """  The Help Desk case number to use as a source  """  
      self.orderNum:int = obj["orderNum"]
      """  The linked quote number  """  
      pass

class DeleteOrderHedLink_output:
   def __init__(self, obj):
      pass

class DeleteQuoteHedLink_input:
   """ Required : 
   helpDeskCaseNum
   quoteNum
   """  
   def __init__(self, obj):
      self.helpDeskCaseNum:int = obj["helpDeskCaseNum"]
      """  The Help Desk case number to use as a source  """  
      self.quoteNum:int = obj["quoteNum"]
      """  The linked quote number  """  
      pass

class DeleteQuoteHedLink_output:
   def __init__(self, obj):
      pass

class DeleteRMAHeadLink_input:
   """ Required : 
   helpDeskCaseNum
   rmaNum
   """  
   def __init__(self, obj):
      self.helpDeskCaseNum:int = obj["helpDeskCaseNum"]
      """  The Help Desk case number to use as a source  """  
      self.rmaNum:int = obj["rmaNum"]
      """  The linked RMA number  """  
      pass

class DeleteRMAHeadLink_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_HDCaseAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.HDCaseNum:int = obj["HDCaseNum"]
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

class Erp_Tablesets_HDCaseFSCallRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  When creating a new Service Call the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this service call.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDCaseJobRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  """  
      self.JobType:str = obj["JobType"]
      """  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this job.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDCaseLinkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  A unique help desk case number.  This number is system generated when the help desk case is created.  """  
      self.ExternalLink:bool = obj["ExternalLink"]
      """  If true this is an external link that was manually entered.  Internal links will refer to other database records.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  Identifies the master file to which the link is related.  If an external link this will be blank.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record.  """  
      self.Key2:str = obj["Key2"]
      """  2nd component of the foreign key to the related master record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  """  
      self.Key4:str = obj["Key4"]
      """  4th component of the foreign key to the related master record.  """  
      self.Key5:str = obj["Key5"]
      """  5th component of the foreign key to the related master record.  """  
      self.Description:str = obj["Description"]
      """  Description of the link contents.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDCaseListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  A unique help desk case number.  This number is system generated when the help desk case is created.  """  
      self.CustNum:int = obj["CustNum"]
      """  The customer associated with this case.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The customer ship-to associate with the Help Desk case.  This is used with the ShpConNum to reference a contact in the CustCont table.  """  
      self.ParentCase:int = obj["ParentCase"]
      """  The parent Help Desk case number of this case.  """  
      self.Description:str = obj["Description"]
      """  The description of the case issue.  """  
      self.ResolutionText:str = obj["ResolutionText"]
      """  A description if the resolution for the case.  """  
      self.PublishedText:str = obj["PublishedText"]
      """  Publishable text of the issue and resolution of the case.  """  
      self.PublishedSummary:str = obj["PublishedSummary"]
      """  A summary of the issue/resolution of the help desk case.  """  
      self.KBEntry:bool = obj["KBEntry"]
      """  If true this is a Knowledge Base entry.  """  
      self.PublishedItem:bool = obj["PublishedItem"]
      """  If true this item can be published.  If false this item is for internal use only.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part that is associated with this Help Desk case.  The part is in the Part table.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  An serial number associated with the Help Desk case.  The serial number is in the SerialNo table.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  The Quote associated with the Help Desk case.  The Quote is in the QuoteHed table.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The order associated with the Help Desk case.  The order is in the OrderHed table.  """  
      self.CaseOwner:str = obj["CaseOwner"]
      """  The SalesRepCode of the owner of the Help Desk case.  The people are stored in the SalesRep table.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date which this Help Desk case was created.  Not maintainable by the user.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  UserID who created the Help Desk case.  Not maintainable by the user.  """  
      self.CreatedTime:int = obj["CreatedTime"]
      """  The time (in milliseconds) that the Help Desk case was created.  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  UserID who last updated the Help Desk case.  Not maintainable by the user.  """  
      self.LastUpdatedDate:str = obj["LastUpdatedDate"]
      """  Date which this Help Desk case was last updated.  Not maintainable by the user.  """  
      self.LastUpdatedTime:int = obj["LastUpdatedTime"]
      """  The time (in milliseconds) that the Help Desk case was last updated.  Not maintainable by the user.  """  
      self.TopicID1:str = obj["TopicID1"]
      """  A unique identifier for the Help Desk Topic.  This is a top level topic (no parents).  """  
      self.TopicID2:str = obj["TopicID2"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID1.  """  
      self.TopicID3:str = obj["TopicID3"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID2.  """  
      self.TopicID4:str = obj["TopicID4"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID3.  """  
      self.TopicID5:str = obj["TopicID5"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID4.  """  
      self.TopicID6:str = obj["TopicID6"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID5.  """  
      self.TopicID7:str = obj["TopicID7"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID6.  """  
      self.TopicID8:str = obj["TopicID8"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID7.  """  
      self.TopicID9:str = obj["TopicID9"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID8.  """  
      self.TopicID10:str = obj["TopicID10"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID9.  """  
      self.CaseTopics:str = obj["CaseTopics"]
      """  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  """  
      self.Quantity:int = obj["Quantity"]
      """  A general quantity field.  """  
      self.QuantityUOM:str = obj["QuantityUOM"]
      """   Unit of Measure which qualifies the HDCase.Quantity.
Mandatory. Must be a valid UOM.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The quote line number  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Customer Name  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this Service call is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line that holds the warranty information for this service call  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.CompletedBy:str = obj["CompletedBy"]
      """  Case Completed By  """  
      self.CompletionDate:str = obj["CompletionDate"]
      """  Case Completion Date  """  
      self.CompletionTime:int = obj["CompletionTime"]
      """  Case Completion Time  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit price for the PartNum.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Same as UnitPrice except that this field contains the unit price in the case currency.  """  
      self.Rp1ExtPrice:int = obj["Rp1ExtPrice"]
      """  Extended Price in Report currency 1.  """  
      self.Rp2ExtPrice:int = obj["Rp2ExtPrice"]
      """  Extended Price in Report currency 2.  """  
      self.CaseTypeID:str = obj["CaseTypeID"]
      """  Unique identifier of the case type.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttrCodeList:str = obj["AttrCodeList"]
      """  Case attribute code list  """  
      self.IssueSummary:str = obj["IssueSummary"]
      """  Short summary if the issue  """  
      self.IssueText:str = obj["IssueText"]
      """  Long issue description  """  
      self.DispCreateTime:str = obj["DispCreateTime"]
      """  String version of the creation time  """  
      self.DispLastUpdateTime:str = obj["DispLastUpdateTime"]
      """  String version of the last update time  """  
      self.CaseOwnerName:str = obj["CaseOwnerName"]
      """  Name  """  
      self.CaseCode:str = obj["CaseCode"]
      self.NextReviewDate:str = obj["NextReviewDate"]
      self.EvaluationStatus:str = obj["EvaluationStatus"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDCaseListTableset:
   def __init__(self, obj):
      self.HDCaseList:list[Erp_Tablesets_HDCaseListRow] = obj["HDCaseList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_HDCaseMaintReqRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.ReqID:str = obj["ReqID"]
      """  System assigned number. Component of the unique index. In the format of yyyymmddnnnn. yyyymmdd is the current year, month, day. nnnn is the next sequential number within the company/Site/yyyymmdd.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  A unique help desk case number.  This number is system generated when the help desk case is created.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDCaseOrderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this order.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.Project_c:str = obj["Project_c"]
      self.OriginalOrderNo_c:int = obj["OriginalOrderNo_c"]
      self.MASFlag_c:bool = obj["MASFlag_c"]
      self.Estimate_c:bool = obj["Estimate_c"]
      self.ShipOrderComplete_c:bool = obj["ShipOrderComplete_c"]
      self.ProjectID_c:str = obj["ProjectID_c"]
      self.PhaseID_c:str = obj["PhaseID_c"]
      self.SalesCatID__c:str = obj["SalesCatID__c"]
      self.TaxCatID_c:str = obj["TaxCatID_c"]
      self.MfgOrder_c:bool = obj["MfgOrder_c"]
      pass

class Erp_Tablesets_HDCaseQuoteRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number is an integer which is used to uniquely identify a quote within the system.  This is automatically assigned by the system when the user requests to create a new quote. To create a new quote the user either takes an "add" option or leaves the Quote Number fill-in zero. The system generates a number by finding the quote number of the last record on file and then a 1 to it. It then uses the greater of Last quote number + 1 or the EQSyst.StartQuoteNum.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this quote.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDCaseRMARow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RMANum:int = obj["RMANum"]
      """  When creating a new Return Authorization the user is prompted for a Return number. If the field is zero , the next available # is assigned by the system. The system generates a number by finding the last CRAHead on file and uses its RANum + 1.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this RMA.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDCaseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  A unique help desk case number.  This number is system generated when the help desk case is created.  """  
      self.CustNum:int = obj["CustNum"]
      """  The customer associated with this case.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The customer ship-to associate with the Help Desk case.  This is used with the ShpConNum to reference a contact in the CustCont table.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Customer contact number.  This is used with the ShipToNum to reference a contact in the CustCont table.  """  
      self.ParentCase:int = obj["ParentCase"]
      """  The parent Help Desk case number of this case.  """  
      self.Description:str = obj["Description"]
      """  The description of the case issue.  """  
      self.ResolutionText:str = obj["ResolutionText"]
      """  A description if the resolution for the case.  """  
      self.PublishedText:str = obj["PublishedText"]
      """  Publishable text of the issue and resolution of the case.  """  
      self.PublishedSummary:str = obj["PublishedSummary"]
      """  A summary of the issue/resolution of the help desk case.  """  
      self.KBEntry:bool = obj["KBEntry"]
      """  If true this is a Knowledge Base entry.  """  
      self.PublishedItem:bool = obj["PublishedItem"]
      """  If true this item can be published.  If false this item is for internal use only.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part that is associated with this Help Desk case.  The part is in the Part table.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  An serial number associated with the Help Desk case.  The serial number is in the SerialNo table.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  The Quote associated with the Help Desk case.  The Quote is in the QuoteHed table.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The order associated with the Help Desk case.  The order is in the OrderHed table.  """  
      self.CallNum:int = obj["CallNum"]
      """  A Field Service call that is associated with the Help Desk case.  The field service call is in the FSCallHd table.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  A Service Contract associated with the Help Desk case.  The service contract is in the FSContHd table.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  The warranty associated with the Help Desk case.  The warranty is in the FSWarrCd table.  """  
      self.Priority:int = obj["Priority"]
      """  The priority of the Help Desk case  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set.  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  The identifier of the workflow stage.  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active milestone task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.CaseOwner:str = obj["CaseOwner"]
      """  The SalesRepCode of the owner of the Help Desk case.  The people are stored in the SalesRep table.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  This indicates if the workflow for this case is complete.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date which this Help Desk case was created.  Not maintainable by the user.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  UserID who created the Help Desk case.  Not maintainable by the user.  """  
      self.CreatedTime:int = obj["CreatedTime"]
      """  The time (in milliseconds) that the Help Desk case was created.  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  UserID who last updated the Help Desk case.  Not maintainable by the user.  """  
      self.LastUpdatedDate:str = obj["LastUpdatedDate"]
      """  Date which this Help Desk case was last updated.  Not maintainable by the user.  """  
      self.LastUpdatedTime:int = obj["LastUpdatedTime"]
      """  The time (in milliseconds) that the Help Desk case was last updated.  Not maintainable by the user.  """  
      self.TopicID1:str = obj["TopicID1"]
      """  A unique identifier for the Help Desk Topic.  This is a top level topic (no parents).  """  
      self.TopicID2:str = obj["TopicID2"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID1.  """  
      self.TopicID3:str = obj["TopicID3"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID2.  """  
      self.TopicID4:str = obj["TopicID4"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID3.  """  
      self.TopicID5:str = obj["TopicID5"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID4.  """  
      self.TopicID6:str = obj["TopicID6"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID5.  """  
      self.TopicID7:str = obj["TopicID7"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID6.  """  
      self.TopicID8:str = obj["TopicID8"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID7.  """  
      self.TopicID9:str = obj["TopicID9"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID8.  """  
      self.TopicID10:str = obj["TopicID10"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID9.  """  
      self.CaseTopics:str = obj["CaseTopics"]
      """  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  Link to the Marketing Campaign related to this Help Desk case.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  Link to the marketing event associated with this Help Desk case.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  """  
      self.Quantity:int = obj["Quantity"]
      """  A general quantity field.  """  
      self.QuantityUOM:str = obj["QuantityUOM"]
      """   Unit of Measure which qualifies the HDCase.Quantity.
Mandatory. Must be a valid UOM.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The order release number.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The quote line number  """  
      self.CallLine:int = obj["CallLine"]
      """  Field service call line number  """  
      self.RMANum:int = obj["RMANum"]
      """  The RMA Number.  """  
      self.RMALine:int = obj["RMALine"]
      """  The RMA line number.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Customer Name  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this Service call is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line that holds the warranty information for this service call  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.CompletedBy:str = obj["CompletedBy"]
      """  Case Completed By  """  
      self.CompletionDate:str = obj["CompletionDate"]
      """  Case Completion Date  """  
      self.CompletionTime:int = obj["CompletionTime"]
      """  Case Completion Time  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  The drop shipment packing slip number that this Service call is linked with  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  The drop shipment packing slip line that holds the warranty information for this service call  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier number of the drop shipment and part of the primary key of a drop shipment line.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point id of the drop shipment and part of the primary key of a drop shipment line.  """  
      self.EquipID:str = obj["EquipID"]
      """  Related Equip.EquipID.  """  
      self.EmpID:str = obj["EmpID"]
      """  Unique identifier of the primary Employee contact.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  Unique identifier of the primary Buyer contact.  """  
      self.VendorNumCon:int = obj["VendorNumCon"]
      """  Unique identifier of the Primary Vendor contact.  """  
      self.PurPointCon:str = obj["PurPointCon"]
      """  Unique identifier of the Primary Vendor PP contact.  """  
      self.VenConNum:int = obj["VenConNum"]
      """  Unique identifier of the Primary Vendor contact num.  """  
      self.PurPointConNum:int = obj["PurPointConNum"]
      """  Contact number.  Unique identifier for the Primary Purchase Point contact record.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit price for the PartNum.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Same as UnitPrice except that this field contains the unit price in the case currency.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Unit Price in Report currency 1.  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Unit Price in Report currency 2.  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Unit Price in Report currency 3.  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended price. Calculated as Quantity * (UnitPrice / PFactor).  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Same as ExtPrice except that this field contains the extended price in the case currency.  """  
      self.Rp1ExtPrice:int = obj["Rp1ExtPrice"]
      """  Extended Price in Report currency 1.  """  
      self.Rp2ExtPrice:int = obj["Rp2ExtPrice"]
      """  Extended Price in Report currency 2.  """  
      self.Rp3ExtPrice:int = obj["Rp3ExtPrice"]
      """  Extended Price in Report currency 3.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Type Code  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that will be used for this role code entry.  """  
      self.CaseTypeID:str = obj["CaseTypeID"]
      """  Unique identifier of the case type.  """  
      self.PONum:int = obj["PONum"]
      """  This field will mainly be used when a part is found to be faulty and the purchase order and receipt that were used for the part need to be recorded  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  Link to the territory ID.  """  
      self.POLine:int = obj["POLine"]
      """  This field will mainly be used when a part is found to be faulty and the purchase order and receipt that were used for the part need to be recorded  """  
      self.WorkflowType:str = obj["WorkflowType"]
      """  The type of workflow.  """  
      self.POPackSlip:str = obj["POPackSlip"]
      """  This field will mainly be used when a part is found to be faulty and the purchase order and receipt that were used for the part need to be recorded  """  
      self.POPackLine:int = obj["POPackLine"]
      """  This field will mainly be used when a part is found to be faulty and the purchase order and receipt that were used for the part need to be recorded  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HDCaseStatus:str = obj["HDCaseStatus"]
      """  HDCaseStatus  """  
      self.ReqPerConID:int = obj["ReqPerConID"]
      """  ReqPerConID  """  
      self.PerConID:int = obj["PerConID"]
      """  PerConID  """  
      self.WebCase:bool = obj["WebCase"]
      """  Case was initiated from the web  """  
      self.WebComment:str = obj["WebComment"]
      """  Comment used for discussion through web  """  
      self.IDNum:str = obj["IDNum"]
      """  Identification Number of related Location Inventory record.  """  
      self.LocationNum:int = obj["LocationNum"]
      """  Unique ID Num of related Location Inventory record.  """  
      self.ContractLine:int = obj["ContractLine"]
      """  Field service contract line number. The service contract line is in the FSContDt table.  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.FSMCurrentStatus:str = obj["FSMCurrentStatus"]
      """  FSMCurrentStatus  """  
      self.FSMServiceReportID:str = obj["FSMServiceReportID"]
      """  FSMServiceReportID  """  
      self.FSMNumberOfFollowups:int = obj["FSMNumberOfFollowups"]
      """  FSMNumberOfFollowups  """  
      self.FSMReceivedBy:str = obj["FSMReceivedBy"]
      """  FSMReceivedBy  """  
      self.FSMOriginalScheduleDate:str = obj["FSMOriginalScheduleDate"]
      """  FSMOriginalScheduleDate  """  
      self.FSMCompletedDate:str = obj["FSMCompletedDate"]
      """  FSMCompletedDate  """  
      self.AllowMilestoneUpdate:bool = obj["AllowMilestoneUpdate"]
      """  If true the MilestoneSeq field can be modified  """  
      self.AttrCodeList:str = obj["AttrCodeList"]
      """  Case attribute code list  """  
      self.AvailablePrcConNum:str = obj["AvailablePrcConNum"]
      """  Available PrcConNum values  """  
      self.AvailablePurPointConNum:str = obj["AvailablePurPointConNum"]
      """  Available AvailablePurPointConNum values  """  
      self.AvailableShpConNum:str = obj["AvailableShpConNum"]
      """  Available ShpConNum values  """  
      self.AvailableTaskSets:str = obj["AvailableTaskSets"]
      """  a delimited list of Task Sets that can be selected in the TaskSetId field  """  
      self.AvailableVenConNum:str = obj["AvailableVenConNum"]
      """  Available AvailableVenConNum values  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CaseCode:str = obj["CaseCode"]
      """  Code of the event. Selected from predefined list of codes.  """  
      self.CaseStatus:str = obj["CaseStatus"]
      """  Indicates the current status of the case.  """  
      self.ChildCases:str = obj["ChildCases"]
      """  List of children linked to the case. Case numbers are separated by commas.  """  
      self.CurrentMilestone:int = obj["CurrentMilestone"]
      """  The current milestone in tasks  """  
      self.CurrentMilestoneDesc:str = obj["CurrentMilestoneDesc"]
      """  Description of current milestone.  """  
      self.CustCntCorpName:str = obj["CustCntCorpName"]
      self.CustCntEMail:str = obj["CustCntEMail"]
      self.CustCntFaxNum:str = obj["CustCntFaxNum"]
      self.CustCntFirstName:str = obj["CustCntFirstName"]
      self.CustCntLastName:str = obj["CustCntLastName"]
      self.CustCntMiddleName:str = obj["CustCntMiddleName"]
      self.CustCntName:str = obj["CustCntName"]
      self.CustCntPhoneNum:str = obj["CustCntPhoneNum"]
      self.CustomerRequiresPO:bool = obj["CustomerRequiresPO"]
      """  If true the customer requires a unique PO on Sales Orders  """  
      self.DispCreateTime:str = obj["DispCreateTime"]
      """  String version of the creation time  """  
      self.DispLastUpdateTime:str = obj["DispLastUpdateTime"]
      """  String version of the last update time  """  
      self.DropShip:bool = obj["DropShip"]
      self.EvaluationStatus:str = obj["EvaluationStatus"]
      """  Evaluation status of the event. Possible values are user defined.  """  
      self.EvaluationStatusDesc:str = obj["EvaluationStatusDesc"]
      """  Description of Evaluation Status  """  
      self.HDCaseNumString:str = obj["HDCaseNumString"]
      """  String version of HDCaseNum (used for relationships)  """  
      self.Inactive:bool = obj["Inactive"]
      self.IssueSummary:str = obj["IssueSummary"]
      """  Short summary if the issue  """  
      self.IssueText:str = obj["IssueText"]
      """  Long issue description  """  
      self.NextReviewDate:str = obj["NextReviewDate"]
      """  Date of the next review.  """  
      self.PartSalesUM:str = obj["PartSalesUM"]
      """  The SalesUM of the part  """  
      self.PPCntEmailAddress:str = obj["PPCntEmailAddress"]
      self.PPCntFaxNum:str = obj["PPCntFaxNum"]
      self.PPCntName:str = obj["PPCntName"]
      self.PPCntPhoneNum:str = obj["PPCntPhoneNum"]
      self.PricePerCode:str = obj["PricePerCode"]
      self.PurPointConName:str = obj["PurPointConName"]
      self.ReqContextLink:str = obj["ReqContextLink"]
      """  Requestor Context Link  """  
      self.ReqPerConLnkID1:str = obj["ReqPerConLnkID1"]
      """  Holds the first ID for the linked record.  """  
      self.ReqPerConLnkID2:str = obj["ReqPerConLnkID2"]
      """  Holds the second ID for the linked record. Used with compound key records like ShipTo or PurPoint.  """  
      self.ReqPerConLnkName:str = obj["ReqPerConLnkName"]
      """  The display name for the link.  """  
      self.ReqPerConLnkRowID:str = obj["ReqPerConLnkRowID"]
      """  The SysRowId of the linked PerConLnk.  """  
      self.ReqPerConName:str = obj["ReqPerConName"]
      """  Requestor PerCon Name  """  
      self.ReqPrimary:bool = obj["ReqPrimary"]
      """  Requestor is primary contact.  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Extended Price in Report currency 1.  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Extended Price in Report currency 2.  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Extended Price in Report currency 3.  """  
      self.ShipCntCorpName:str = obj["ShipCntCorpName"]
      self.ShipCntEMail:str = obj["ShipCntEMail"]
      self.ShipCntFaxNum:str = obj["ShipCntFaxNum"]
      self.ShipCntFirstName:str = obj["ShipCntFirstName"]
      self.ShipCntLastName:str = obj["ShipCntLastName"]
      self.ShipCntMiddleName:str = obj["ShipCntMiddleName"]
      self.ShipCntName:str = obj["ShipCntName"]
      self.ShipCntPhoneNum:str = obj["ShipCntPhoneNum"]
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  Customer Id of the third-party Ship To  """  
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.TargetUOM:str = obj["TargetUOM"]
      """  TargetUOM  """  
      self.TaskCompletePasswordIsValid:bool = obj["TaskCompletePasswordIsValid"]
      """  A flag to indicate the user password was validated  """  
      self.TaskCompletePasswordRequired:bool = obj["TaskCompletePasswordRequired"]
      """  Indicates if a the user password should be validated to complete a task  """  
      self.VendCntEmailAddress:str = obj["VendCntEmailAddress"]
      self.VendCntFaxNum:str = obj["VendCntFaxNum"]
      self.VendCntName:str = obj["VendCntName"]
      self.VendCntPhoneNum:str = obj["VendCntPhoneNum"]
      self.WebQuoteNum:int = obj["WebQuoteNum"]
      """  The Quote Num that created a case number from the web  """  
      self.AvailableMilestones:str = obj["AvailableMilestones"]
      """  The available next milestones for the MilestoneSeq.  """  
      self.FSMCurrentStatusDesc:str = obj["FSMCurrentStatusDesc"]
      """  Translated description of current FSM status for FSM related cases  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ActiveTaskIDTaskDescription:str = obj["ActiveTaskIDTaskDescription"]
      self.BuyerIDName:str = obj["BuyerIDName"]
      self.CaseOwnerName:str = obj["CaseOwnerName"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      self.DropShipDtlLineDesc:str = obj["DropShipDtlLineDesc"]
      self.EmpIDName:str = obj["EmpIDName"]
      self.EquipIDDescription:str = obj["EquipIDDescription"]
      self.LastTaskIDTaskDescription:str = obj["LastTaskIDTaskDescription"]
      self.LocationInventoryLotNum:str = obj["LocationInventoryLotNum"]
      self.LocationInventorySerialNumber:str = obj["LocationInventorySerialNumber"]
      self.LocationInventoryIDNum:str = obj["LocationInventoryIDNum"]
      self.MktgCampaignIDCampDescription:str = obj["MktgCampaignIDCampDescription"]
      self.MktgEventEvntDescription:str = obj["MktgEventEvntDescription"]
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.ShipToCustNumName:str = obj["ShipToCustNumName"]
      self.ShipToCustNumCustID:str = obj["ShipToCustNumCustID"]
      self.TaskSetIDWorkflowType:str = obj["TaskSetIDWorkflowType"]
      self.TaskSetIDTaskSetDescription:str = obj["TaskSetIDTaskSetDescription"]
      self.TerritoryIDTerritoryDesc:str = obj["TerritoryIDTerritoryDesc"]
      self.VendorNumConVendorID:str = obj["VendorNumConVendorID"]
      self.VendorNumConName:str = obj["VendorNumConName"]
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      self.WFGroupIDDescription:str = obj["WFGroupIDDescription"]
      self.WFStageIDDescription:str = obj["WFStageIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDCaseSearchRow:
   def __init__(self, obj):
      self.SearchMode:str = obj["SearchMode"]
      """  The mode to use for searching  """  
      self.SearchPublishedItemsOnly:bool = obj["SearchPublishedItemsOnly"]
      """  Search only published items  """  
      self.WorkflowCompletionStatus:str = obj["WorkflowCompletionStatus"]
      """  The completion status of the workflow  """  
      self.CustID:str = obj["CustID"]
      """  The Customer ID  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Customer Name  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Ship to Number  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Ship To Contact Number  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Bill To Contact Number  """  
      self.TextKeywords:str = obj["TextKeywords"]
      """  Keywords to use in text searching  """  
      self.SearchIssueText:bool = obj["SearchIssueText"]
      """  Use TextKeywords to search issue text  """  
      self.SearchResolutionText:bool = obj["SearchResolutionText"]
      """  Use TextKeywords to search resolution text  """  
      self.SearchPublishedText:bool = obj["SearchPublishedText"]
      """  Use TextKeywords to search published text  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The part revision number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part description.  If blank this will be ignored.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  The serial number.   If blank this will be ignored.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  The quote number.   If 0 this will be ignored.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The quote line.   If 0 this will be ignored.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The order number.   If 0 this will be ignored.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The order line number.   If 0 this will be ignored.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The order release number.   If 0 this will be ignored.  """  
      self.CallNum:int = obj["CallNum"]
      """  Field service call number  """  
      self.CallLine:int = obj["CallLine"]
      """  Field service call line number.   If 0 this will be ignored.  """  
      self.RMANum:int = obj["RMANum"]
      """  The RMA number.   If 0 this will be ignored.  """  
      self.RMALine:int = obj["RMALine"]
      """  The RMA line number.   If 0 this will be ignored.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice number.   If 0 this will be ignored.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line number.   If 0 this will be ignored.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  The contract number.   If 0 this will be ignored.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  The warrancy code. If blank this will be ignored.  """  
      self.Priority:int = obj["Priority"]
      """  The help desk priority. If 0 this will be ignored.  """  
      self.CaseTopics:str = obj["CaseTopics"]
      """  Case topics. If blank this will be ignored.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  The marketing campaign Id. If blank this will be ignored.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  The marketing event sequence. If 0 this will be ignored.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  The project Id. If blank this will be ignored.  """  
      self.CaseOwner:str = obj["CaseOwner"]
      """  The case owner. If blank this will be ignored.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The help desk workflow group Id. If blank this will be ignored.  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  The current workflow stage. If blank this will be ignored.  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  Active task Id. If blank this will be ignored.  """  
      self.CreatedDateFrom:str = obj["CreatedDateFrom"]
      """  The starting date for a range used to search created date. If null this will be ignored.  """  
      self.CreatedDateTo:str = obj["CreatedDateTo"]
      """  The ending date for a range used to search created date. If null this will be ignored.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user that created the case. If blank this will be ignored.  """  
      self.LastUpdatedFrom:str = obj["LastUpdatedFrom"]
      """  The starting date for a range used to search last updated date. If null this will be ignored.  """  
      self.LastUpdatedTo:str = obj["LastUpdatedTo"]
      """  The ending date for a range used to search last updated date. If null this will be ignored.  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  The user that last updated the case. If blank this will be ignored.  """  
      self.Company:str = obj["Company"]
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.AvailableShpConNum:str = obj["AvailableShpConNum"]
      """  Available ShpConNum values  """  
      self.AvailablePrcConNum:str = obj["AvailablePrcConNum"]
      """  Available PrcConNum values  """  
      self.TopicID1:str = obj["TopicID1"]
      self.TopicID2:str = obj["TopicID2"]
      self.TopicID3:str = obj["TopicID3"]
      self.TopicID4:str = obj["TopicID4"]
      self.TopicID5:str = obj["TopicID5"]
      self.TopicID6:str = obj["TopicID6"]
      self.TopicID7:str = obj["TopicID7"]
      self.TopicID8:str = obj["TopicID8"]
      self.TopicID9:str = obj["TopicID9"]
      self.TopicID10:str = obj["TopicID10"]
      self.ShipToName:str = obj["ShipToName"]
      self.EquipID:str = obj["EquipID"]
      self.EquipIDDescription:str = obj["EquipIDDescription"]
      self.BuyerID:str = obj["BuyerID"]
      self.EmpID:str = obj["EmpID"]
      self.PurPointCon:str = obj["PurPointCon"]
      self.VendorNumCon:int = obj["VendorNumCon"]
      self.VenConNum:int = obj["VenConNum"]
      self.VendorName:str = obj["VendorName"]
      self.BuyerIDName:str = obj["BuyerIDName"]
      self.EmpIDName:str = obj["EmpIDName"]
      self.PurPointConNum:int = obj["PurPointConNum"]
      self.AvailableVenConNum:str = obj["AvailableVenConNum"]
      """  Available VenConNum values  """  
      self.AvailablePurPointConNum:str = obj["AvailablePurPointConNum"]
      """  Available PurPointConNum values  """  
      self.PurPointConName:str = obj["PurPointConName"]
      self.VendorNumConVendorID:str = obj["VendorNumConVendorID"]
      self.VendorNumConName:str = obj["VendorNumConName"]
      self.WorkflowType:str = obj["WorkflowType"]
      self.RelatedTo:bool = obj["RelatedTo"]
      self.LinkedTo:bool = obj["LinkedTo"]
      self.JobNum:str = obj["JobNum"]
      self.ReqID:str = obj["ReqID"]
      self.TopicID10List:str = obj["TopicID10List"]
      """  Delimited list with valid topics.  """  
      self.TopicID2List:str = obj["TopicID2List"]
      """  Delimited list with valid topics.  """  
      self.TopicID3List:str = obj["TopicID3List"]
      """  Delimited list with valid topics.  """  
      self.TopicID4List:str = obj["TopicID4List"]
      """  Delimited list with valid topics.  """  
      self.TopicID5List:str = obj["TopicID5List"]
      """  Delimited list with valid topics.  """  
      self.TopicID6List:str = obj["TopicID6List"]
      """  Delimited list with valid topics.  """  
      self.TopicID7List:str = obj["TopicID7List"]
      """  Delimited list with valid topics.  """  
      self.TopicID8List:str = obj["TopicID8List"]
      """  Delimited list with valid topics.  """  
      self.TopicID9List:str = obj["TopicID9List"]
      """  Delimited list with valid topics.  """  
      self.TopicID1List:str = obj["TopicID1List"]
      """  Delimited list with valid topics.  """  
      self.ContractLine:int = obj["ContractLine"]
      """  Field service contract line number. If 0 this will be ignored.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.ActiveTaskIDTaskDescription:str = obj["ActiveTaskIDTaskDescription"]
      self.CaseOwnerName:str = obj["CaseOwnerName"]
      self.CustIDCustID:str = obj["CustIDCustID"]
      self.CustIDBTName:str = obj["CustIDBTName"]
      self.CustIDName:str = obj["CustIDName"]
      self.MktgCampCampDescription:str = obj["MktgCampCampDescription"]
      self.MktgEvntEvntDescription:str = obj["MktgEvntEvntDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      self.WFGroupDescription:str = obj["WFGroupDescription"]
      self.WFStageDescription:str = obj["WFStageDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDCaseSearchTableset:
   def __init__(self, obj):
      self.HDCaseSearch:list[Erp_Tablesets_HDCaseSearchRow] = obj["HDCaseSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_HDChildCasesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  A unique help desk case number.  This number is system generated when the help desk case is created.  """  
      self.CustNum:int = obj["CustNum"]
      """  The customer associated with this case.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The customer ship-to associate with the Help Desk case.  This is used with the ShpConNum to reference a contact in the CustCont table.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Customer contact number.  This is used with the ShipToNum to reference a contact in the CustCont table.  """  
      self.ParentCase:int = obj["ParentCase"]
      """  The parent Help Desk case number of this case.  """  
      self.Description:str = obj["Description"]
      """  The description of the case issue.  """  
      self.ResolutionText:str = obj["ResolutionText"]
      """  A description if the resolution for the case.  """  
      self.PublishedText:str = obj["PublishedText"]
      """  Publishable text of the issue and resolution of the case.  """  
      self.PublishedSummary:str = obj["PublishedSummary"]
      """  A summary of the issue/resolution of the help desk case.  """  
      self.KBEntry:bool = obj["KBEntry"]
      """  If true this is a Knowledge Base entry.  """  
      self.PublishedItem:bool = obj["PublishedItem"]
      """  If true this item can be published.  If false this item is for internal use only.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part that is associated with this Help Desk case.  The part is in the Part table.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  An serial number associated with the Help Desk case.  The serial number is in the SerialNo table.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  The Quote associated with the Help Desk case.  The Quote is in the QuoteHed table.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The order associated with the Help Desk case.  The order is in the OrderHed table.  """  
      self.CallNum:int = obj["CallNum"]
      """  A Field Service call that is associated with the Help Desk case.  The field service call is in the FSCallHd table.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  A Service Contract associated with the Help Desk case.  The service contract is in the FSContHd table.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  The warranty associated with the Help Desk case.  The warranty is in the FSWarrCd table.  """  
      self.Priority:int = obj["Priority"]
      """  The priority of the Help Desk case  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set.  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  The identifier of the workflow stage.  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active milestone task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.CaseOwner:str = obj["CaseOwner"]
      """  The SalesRepCode of the owner of the Help Desk case.  The people are stored in the SalesRep table.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  This indicates if the workflow for this case is complete.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date which this Help Desk case was created.  Not maintainable by the user.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  UserID who created the Help Desk case.  Not maintainable by the user.  """  
      self.CreatedTime:int = obj["CreatedTime"]
      """  The time (in milliseconds) that the Help Desk case was created.  """  
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      """  UserID who last updated the Help Desk case.  Not maintainable by the user.  """  
      self.LastUpdatedDate:str = obj["LastUpdatedDate"]
      """  Date which this Help Desk case was last updated.  Not maintainable by the user.  """  
      self.LastUpdatedTime:int = obj["LastUpdatedTime"]
      """  The time (in milliseconds) that the Help Desk case was last updated.  Not maintainable by the user.  """  
      self.TopicID1:str = obj["TopicID1"]
      """  A unique identifier for the Help Desk Topic.  This is a top level topic (no parents).  """  
      self.TopicID2:str = obj["TopicID2"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID1.  """  
      self.TopicID3:str = obj["TopicID3"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID2.  """  
      self.TopicID4:str = obj["TopicID4"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID3.  """  
      self.TopicID5:str = obj["TopicID5"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID4.  """  
      self.TopicID6:str = obj["TopicID6"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID5.  """  
      self.TopicID7:str = obj["TopicID7"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID6.  """  
      self.TopicID8:str = obj["TopicID8"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID7.  """  
      self.TopicID9:str = obj["TopicID9"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID8.  """  
      self.TopicID10:str = obj["TopicID10"]
      """  A unique identifier for the Help Desk Topic.  This is a child to TopicID9.  """  
      self.CaseTopics:str = obj["CaseTopics"]
      """  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  Link to the Marketing Campaign related to this Help Desk case.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  Link to the marketing event associated with this Help Desk case.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  """  
      self.Quantity:int = obj["Quantity"]
      """  A general quantity field.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The order release number.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  The quote line number  """  
      self.CallLine:int = obj["CallLine"]
      """  Field service call line number  """  
      self.RMANum:int = obj["RMANum"]
      """  The RMA Number.  """  
      self.RMALine:int = obj["RMALine"]
      """  The RMA line number.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Customer Name  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustCntEMail:str = obj["CustCntEMail"]
      self.ShipCntEMail:str = obj["ShipCntEMail"]
      self.BitFlag:int = obj["BitFlag"]
      self.CaseOwnerName:str = obj["CaseOwnerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HDContactRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  A unique help desk case number.  """  
      self.PerConLnkRowID:str = obj["PerConLnkRowID"]
      """  The SysRowId of the linked PerConLnk.  """  
      self.Primary:bool = obj["Primary"]
      """  Primary contact for each Context type. Only one allowed per context type.  The primary contact for each context type is shown on the detail sheet.  """  
      self.Comment:str = obj["Comment"]
      """  User entered comments.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Requestor:bool = obj["Requestor"]
      """  Specifies the identifier for the contact who requested the case entry.  """  
      self.Name:str = obj["Name"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      self.Zip:str = obj["Zip"]
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.ContextLink:str = obj["ContextLink"]
      self.BuyerID:str = obj["BuyerID"]
      self.BuyerName:str = obj["BuyerName"]
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.EmpID:str = obj["EmpID"]
      self.EmpName:str = obj["EmpName"]
      self.PurPoint:str = obj["PurPoint"]
      self.PurPointName:str = obj["PurPointName"]
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.VendorID:str = obj["VendorID"]
      self.VendorName:str = obj["VendorName"]
      self.Selected:bool = obj["Selected"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HelpDeskContTrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  The name of the current company.  """  
      self.CustNum:int = obj["CustNum"]
      self.CustID:str = obj["CustID"]
      """  The customer ID.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name for customer.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      self.ShipToName:str = obj["ShipToName"]
      """  The name for the ship to location.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  Specifies the unique case number.  """  
      self.CaseOwner:str = obj["CaseOwner"]
      """  Specifies the case owner.  """  
      self.CurrentMilestone:int = obj["CurrentMilestone"]
      """  Specifies the current milestone.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.CallNum:int = obj["CallNum"]
      """  Specifies an unique number of the call.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Specifies an unique number of Contract.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Specifies the description of a Part selected.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Specifies the Part revision number.  """  
      self.IssueText:str = obj["IssueText"]
      """  Long issue description.  """  
      self.Description:str = obj["Description"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_HelpDeskContTrkTableset:
   def __init__(self, obj):
      self.HelpDeskContTrk:list[Erp_Tablesets_HelpDeskContTrkRow] = obj["HelpDeskContTrk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_HelpDeskTableset:
   def __init__(self, obj):
      self.HDCase:list[Erp_Tablesets_HDCaseRow] = obj["HDCase"]
      self.HDCaseAttch:list[Erp_Tablesets_HDCaseAttchRow] = obj["HDCaseAttch"]
      self.HDCaseFSCall:list[Erp_Tablesets_HDCaseFSCallRow] = obj["HDCaseFSCall"]
      self.HDCaseJob:list[Erp_Tablesets_HDCaseJobRow] = obj["HDCaseJob"]
      self.HDCaseLink:list[Erp_Tablesets_HDCaseLinkRow] = obj["HDCaseLink"]
      self.HDCaseOrder:list[Erp_Tablesets_HDCaseOrderRow] = obj["HDCaseOrder"]
      self.HDCaseQuote:list[Erp_Tablesets_HDCaseQuoteRow] = obj["HDCaseQuote"]
      self.HDCaseRMA:list[Erp_Tablesets_HDCaseRMARow] = obj["HDCaseRMA"]
      self.HDChildCases:list[Erp_Tablesets_HDChildCasesRow] = obj["HDChildCases"]
      self.HDContact:list[Erp_Tablesets_HDContactRow] = obj["HDContact"]
      self.HDCaseMaintReq:list[Erp_Tablesets_HDCaseMaintReqRow] = obj["HDCaseMaintReq"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtHelpDeskTableset:
   def __init__(self, obj):
      self.HDCase:list[Erp_Tablesets_HDCaseRow] = obj["HDCase"]
      self.HDCaseAttch:list[Erp_Tablesets_HDCaseAttchRow] = obj["HDCaseAttch"]
      self.HDCaseFSCall:list[Erp_Tablesets_HDCaseFSCallRow] = obj["HDCaseFSCall"]
      self.HDCaseJob:list[Erp_Tablesets_HDCaseJobRow] = obj["HDCaseJob"]
      self.HDCaseLink:list[Erp_Tablesets_HDCaseLinkRow] = obj["HDCaseLink"]
      self.HDCaseOrder:list[Erp_Tablesets_HDCaseOrderRow] = obj["HDCaseOrder"]
      self.HDCaseQuote:list[Erp_Tablesets_HDCaseQuoteRow] = obj["HDCaseQuote"]
      self.HDCaseRMA:list[Erp_Tablesets_HDCaseRMARow] = obj["HDCaseRMA"]
      self.HDChildCases:list[Erp_Tablesets_HDChildCasesRow] = obj["HDChildCases"]
      self.HDContact:list[Erp_Tablesets_HDContactRow] = obj["HDContact"]
      self.HDCaseMaintReq:list[Erp_Tablesets_HDCaseMaintReqRow] = obj["HDCaseMaintReq"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FindPart_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  PartNum  """  
      pass

class FindPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      self.opMatchType:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetAvailTaskSets_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class GetAvailTaskSets_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.whereClause:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   hdCaseNum
   """  
   def __init__(self, obj):
      self.hdCaseNum:int = obj["hdCaseNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_HelpDeskTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_HelpDeskTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_HelpDeskTableset] = obj["returnObj"]
      pass

class GetChildTopicsDS_input:
   """ Required : 
   topicID
   ds
   """  
   def __init__(self, obj):
      self.topicID:str = obj["topicID"]
      """  The Topic ID to be populated.  """  
      self.ds:list[Erp_Tablesets_HDCaseSearchTableset] = obj["ds"]
      pass

class GetChildTopicsDS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HDCaseSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetChildTopics_input:
   """ Required : 
   parentTopicID
   """  
   def __init__(self, obj):
      self.parentTopicID:str = obj["parentTopicID"]
      """  The parent topic or string.Empty for top level topics.  """  
      pass

class GetChildTopics_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.childList:str = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_HDCaseListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewHDCaseAttch_input:
   """ Required : 
   ds
   hdCaseNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.hdCaseNum:int = obj["hdCaseNum"]
      pass

class GetNewHDCaseAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewHDCaseFSCall_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class GetNewHDCaseFSCall_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewHDCaseJob_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class GetNewHDCaseJob_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewHDCaseLink_input:
   """ Required : 
   ds
   hdCaseNum
   externalLink
   relatedToFile
   key1
   key2
   key3
   key4
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.hdCaseNum:int = obj["hdCaseNum"]
      self.externalLink:bool = obj["externalLink"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      pass

class GetNewHDCaseLink_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewHDCaseMaintReq_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class GetNewHDCaseMaintReq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewHDCaseOrder_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class GetNewHDCaseOrder_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewHDCaseQuote_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class GetNewHDCaseQuote_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewHDCaseRMA_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class GetNewHDCaseRMA_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewHDCaseSearchDS_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HDCaseSearchTableset] = obj["ds"]
      pass

class GetNewHDCaseSearchDS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HDCaseSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewHDCaseSearch_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HDCaseSearchTableset] = obj["ds"]
      pass

class GetNewHDCaseSearch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HDCaseSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewHDCase_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class GetNewHDCase_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewHDChildCases_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class GetNewHDChildCases_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewHDContact_input:
   """ Required : 
   ds
   hdCaseNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.hdCaseNum:int = obj["hdCaseNum"]
      pass

class GetNewHDContact_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPartFromRowID_input:
   """ Required : 
   ipRowType
   ipRowID
   """  
   def __init__(self, obj):
      self.ipRowType:str = obj["ipRowType"]
      """  Row Type  """  
      self.ipRowID:str = obj["ipRowID"]
      """  Row ID  """  
      pass

class GetPartFromRowID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRowsContactTracker_input:
   """ Required : 
   whereClauseHDCase
   contactName
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseHDCase:str = obj["whereClauseHDCase"]
      """  Where clause for HDCase table.  """  
      self.contactName:str = obj["contactName"]
      """  The contact to return data for.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsContactTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_HelpDeskContTrkTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseHDCase
   whereClauseHDCaseAttch
   whereClauseHDCaseFSCall
   whereClauseHDCaseJob
   whereClauseHDCaseLink
   whereClauseHDCaseOrder
   whereClauseHDCaseQuote
   whereClauseHDCaseRMA
   whereClauseHDChildCases
   whereClauseHDContact
   whereClauseHDCaseMaintReq
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseHDCase:str = obj["whereClauseHDCase"]
      self.whereClauseHDCaseAttch:str = obj["whereClauseHDCaseAttch"]
      self.whereClauseHDCaseFSCall:str = obj["whereClauseHDCaseFSCall"]
      self.whereClauseHDCaseJob:str = obj["whereClauseHDCaseJob"]
      self.whereClauseHDCaseLink:str = obj["whereClauseHDCaseLink"]
      self.whereClauseHDCaseOrder:str = obj["whereClauseHDCaseOrder"]
      self.whereClauseHDCaseQuote:str = obj["whereClauseHDCaseQuote"]
      self.whereClauseHDCaseRMA:str = obj["whereClauseHDCaseRMA"]
      self.whereClauseHDChildCases:str = obj["whereClauseHDChildCases"]
      self.whereClauseHDContact:str = obj["whereClauseHDContact"]
      self.whereClauseHDCaseMaintReq:str = obj["whereClauseHDCaseMaintReq"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_HelpDeskTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSerialNoPartNum_input:
   """ Required : 
   proposedSerialNumber
   """  
   def __init__(self, obj):
      self.proposedSerialNumber:str = obj["proposedSerialNumber"]
      """  The proposed SerialNumber  """  
      pass

class GetSerialNoPartNum_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.PartNumFromSerial:str = obj["parameters"]
      pass

      """  output parameters  """  

class HelpDeskSearch_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HDCaseSearchTableset] = obj["ds"]
      pass

class HelpDeskSearch_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_HDCaseListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HDCaseSearchTableset] = obj["ds"]
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

class OnChangeAttrCodeList_input:
   """ Required : 
   ds
   proposedAttrCodeList
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedAttrCodeList:str = obj["proposedAttrCodeList"]
      """  The proposed AttrCodeList  """  
      pass

class OnChangeAttrCodeList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBuyerID_input:
   """ Required : 
   buyerID
   ds
   """  
   def __init__(self, obj):
      self.buyerID:str = obj["buyerID"]
      """  BuyerID  """  
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class OnChangeBuyerID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeCallLine_input:
   """ Required : 
   ds
   proposedCallLine
   getDefaults
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedCallLine:int = obj["proposedCallLine"]
      """  The proposed CallLine  """  
      self.getDefaults:bool = obj["getDefaults"]
      """  Assign any fields related to CallLine  """  
      pass

class OnChangeCallLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeCallNum_input:
   """ Required : 
   ds
   proposedCallNum
   getDefaults
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedCallNum:int = obj["proposedCallNum"]
      """  The proposed CallNum  """  
      self.getDefaults:bool = obj["getDefaults"]
      """  Assign any fields related to CallNum  """  
      pass

class OnChangeCallNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeCaseOwner_input:
   """ Required : 
   ds
   proposedCaseOwner
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedCaseOwner:str = obj["proposedCaseOwner"]
      """  The proposed CaseOwner  """  
      pass

class OnChangeCaseOwner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeCaseTopics_input:
   """ Required : 
   ds
   proposedCaseTopics
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedCaseTopics:str = obj["proposedCaseTopics"]
      """  The proposed case topics delimited with spaces  """  
      pass

class OnChangeCaseTopics_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeCaseTypeID_input:
   """ Required : 
   ds
   proposedCaseTypeID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedCaseTypeID:str = obj["proposedCaseTypeID"]
      """  The proposed CaseTypeID  """  
      pass

class OnChangeCaseTypeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeContractLine_input:
   """ Required : 
   ds
   proposedContractLine
   getDefaults
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedContractLine:int = obj["proposedContractLine"]
      self.getDefaults:bool = obj["getDefaults"]
      pass

class OnChangeContractLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeContractNum_input:
   """ Required : 
   ds
   proposedContractNum
   getDefaults
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedContractNum:int = obj["proposedContractNum"]
      """  The proposed ContractNum  """  
      self.getDefaults:bool = obj["getDefaults"]
      """  Assign any fields related to ContractNum  """  
      pass

class OnChangeContractNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeCustID_input:
   """ Required : 
   ds
   proposedCustID
   getDefaults
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedCustID:str = obj["proposedCustID"]
      """  The proposed Customer ID  """  
      self.getDefaults:bool = obj["getDefaults"]
      """  Assign any fields related to CustID  """  
      pass

class OnChangeCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeEmpID_input:
   """ Required : 
   empID
   ds
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      """  EmpID  """  
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class OnChangeEmpID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeEquipID_input:
   """ Required : 
   equipID
   ds
   """  
   def __init__(self, obj):
      self.equipID:str = obj["equipID"]
      """  equipID  """  
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class OnChangeEquipID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeHDCaseSearch_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HDCaseSearchTableset] = obj["ds"]
      pass

class OnChangeHDCaseSearch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HDCaseSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeInvoiceLine_input:
   """ Required : 
   ds
   proposedInvoiceLine
   getDefaults
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedInvoiceLine:int = obj["proposedInvoiceLine"]
      """  The proposed InvoiceLine  """  
      self.getDefaults:bool = obj["getDefaults"]
      """  Assign any fields related to InvoiceLine  """  
      pass

class OnChangeInvoiceLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeInvoiceNum_input:
   """ Required : 
   ds
   proposedInvoiceNum
   getDefaults
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedInvoiceNum:int = obj["proposedInvoiceNum"]
      """  The proposed InvoiceNum  """  
      self.getDefaults:bool = obj["getDefaults"]
      """  Assign any fields related to InvoiceNum  """  
      pass

class OnChangeInvoiceNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMktgCampaignID_input:
   """ Required : 
   ds
   proposedMktgCampaignID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedMktgCampaignID:str = obj["proposedMktgCampaignID"]
      """  The proposed MktgCampaignID  """  
      pass

class OnChangeMktgCampaignID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMktgEvntSeq_input:
   """ Required : 
   ds
   proposedMktgEvntSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedMktgEvntSeq:int = obj["proposedMktgEvntSeq"]
      """  The proposed MktgEvntSeq  """  
      pass

class OnChangeMktgEvntSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeName_input:
   """ Required : 
   ipName
   ds
   """  
   def __init__(self, obj):
      self.ipName:str = obj["ipName"]
      """  Name  """  
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class OnChangeName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOrderLine_input:
   """ Required : 
   ds
   proposedOrderLine
   getDefaults
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedOrderLine:int = obj["proposedOrderLine"]
      """  The proposed OrderLine  """  
      self.getDefaults:bool = obj["getDefaults"]
      """  Assign any fields related to OrderLine  """  
      pass

class OnChangeOrderLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOrderNum_input:
   """ Required : 
   ds
   proposedOrderNum
   getDefaults
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedOrderNum:int = obj["proposedOrderNum"]
      """  The proposed OrderNum  """  
      self.getDefaults:bool = obj["getDefaults"]
      """  Assign any fields related to OrderNum  """  
      pass

class OnChangeOrderNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOrderRelNum_input:
   """ Required : 
   ds
   proposedOrderRelNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedOrderRelNum:int = obj["proposedOrderRelNum"]
      """  The proposed OrderRelNum  """  
      pass

class OnChangeOrderRelNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePartNum_input:
   """ Required : 
   ds
   proposedPartNum
   getDefaults
   SysRowID
   rowType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedPartNum:str = obj["proposedPartNum"]
      """  The proposed PartNum  """  
      self.getDefaults:bool = obj["getDefaults"]
      """  Assign any fields related to PartNum  """  
      self.SysRowID:str = obj["SysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      pass

class OnChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedPartNum:str = obj["parameters"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class OnChangePerConLnkRowID_input:
   """ Required : 
   ipPerConLnkRowID
   ds
   """  
   def __init__(self, obj):
      self.ipPerConLnkRowID:str = obj["ipPerConLnkRowID"]
      """  PerConLnkRowID  """  
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class OnChangePerConLnkRowID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePrcConNum_input:
   """ Required : 
   ds
   proposedPrcConNum
   proposedPrcCustNum
   proposedPrcShipToNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedPrcConNum:int = obj["proposedPrcConNum"]
      """  The proposed PrcConNum  """  
      self.proposedPrcCustNum:int = obj["proposedPrcCustNum"]
      """  The proposed PrcCustNum  """  
      self.proposedPrcShipToNum:str = obj["proposedPrcShipToNum"]
      """  The proposed PrcShipToNum  """  
      pass

class OnChangePrcConNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeProjectID_input:
   """ Required : 
   ds
   proposedProjectID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedProjectID:str = obj["proposedProjectID"]
      """  The proposed ProjectID  """  
      pass

class OnChangeProjectID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePurPointConNum_input:
   """ Required : 
   ds
   proposedPurPointConNum
   proposedPurPoint
   proposedVendorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedPurPointConNum:int = obj["proposedPurPointConNum"]
      """  The proposed PurPointConNum  """  
      self.proposedPurPoint:str = obj["proposedPurPoint"]
      """  The proposed PurPoint  """  
      self.proposedVendorNum:int = obj["proposedVendorNum"]
      """  The proposed VendorNum  """  
      pass

class OnChangePurPointConNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePurPoint_input:
   """ Required : 
   ds
   proposedPurPoint
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedPurPoint:str = obj["proposedPurPoint"]
      """  The proposed PurPoint  """  
      pass

class OnChangePurPoint_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeQuantityUOM_input:
   """ Required : 
   proposedQuantityUOM
   ds
   """  
   def __init__(self, obj):
      self.proposedQuantityUOM:str = obj["proposedQuantityUOM"]
      """  The proposed QuantityUOM  """  
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class OnChangeQuantityUOM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeQuantity_input:
   """ Required : 
   proposedQuantity
   ds
   """  
   def __init__(self, obj):
      self.proposedQuantity:int = obj["proposedQuantity"]
      """  The proposed UnitPrice  """  
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class OnChangeQuantity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeQuoteLine_input:
   """ Required : 
   ds
   proposedQuoteLine
   getDefaults
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedQuoteLine:int = obj["proposedQuoteLine"]
      """  The proposed QuoteLine  """  
      self.getDefaults:bool = obj["getDefaults"]
      """  Assign any fields related to QuoteLine  """  
      pass

class OnChangeQuoteLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeQuoteNum_input:
   """ Required : 
   ds
   proposedQuoteNum
   getDefaults
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedQuoteNum:int = obj["proposedQuoteNum"]
      """  The proposed QuoteNum  """  
      self.getDefaults:bool = obj["getDefaults"]
      """  Assign any fields related to QuoteNum  """  
      pass

class OnChangeQuoteNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeRMALine_input:
   """ Required : 
   ds
   proposedRMALine
   getDefaults
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedRMALine:int = obj["proposedRMALine"]
      """  The proposed RMALine  """  
      self.getDefaults:bool = obj["getDefaults"]
      """  Defaults  """  
      pass

class OnChangeRMALine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeRMANum_input:
   """ Required : 
   ds
   proposedRMANum
   getDefaults
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedRMANum:int = obj["proposedRMANum"]
      """  The proposed RMANum  """  
      self.getDefaults:bool = obj["getDefaults"]
      """  Defaults  """  
      pass

class OnChangeRMANum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeReqPerConID_input:
   """ Required : 
   ds
   proposedReqPerConID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedReqPerConID:int = obj["proposedReqPerConID"]
      """  The proposed Person Contact ID  """  
      pass

class OnChangeReqPerConID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeReqPerConLnkRowID_input:
   """ Required : 
   ds
   proposedReqPerConLnkRowID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedReqPerConLnkRowID:str = obj["proposedReqPerConLnkRowID"]
      """  The proposed Person Contact Link ID  """  
      pass

class OnChangeReqPerConLnkRowID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeRevisionNum_input:
   """ Required : 
   ds
   proposedRevisionNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedRevisionNum:str = obj["proposedRevisionNum"]
      """  The proposed RevisionNum  """  
      pass

class OnChangeRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeSearchCaseTopics_input:
   """ Required : 
   ds
   proposedCaseTopics
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HDCaseSearchTableset] = obj["ds"]
      self.proposedCaseTopics:str = obj["proposedCaseTopics"]
      """  The proposed case topics delimited with spaces  """  
      pass

class OnChangeSearchCaseTopics_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HDCaseSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeSearchTopicID_input:
   """ Required : 
   changedTopicIDInt
   ds
   proposedTopicID1
   proposedTopicID2
   proposedTopicID3
   proposedTopicID4
   proposedTopicID5
   proposedTopicID6
   proposedTopicID7
   proposedTopicID8
   proposedTopicID9
   proposedTopicID10
   """  
   def __init__(self, obj):
      self.changedTopicIDInt:int = obj["changedTopicIDInt"]
      self.ds:list[Erp_Tablesets_HDCaseSearchTableset] = obj["ds"]
      self.proposedTopicID1:str = obj["proposedTopicID1"]
      self.proposedTopicID2:str = obj["proposedTopicID2"]
      self.proposedTopicID3:str = obj["proposedTopicID3"]
      self.proposedTopicID4:str = obj["proposedTopicID4"]
      self.proposedTopicID5:str = obj["proposedTopicID5"]
      self.proposedTopicID6:str = obj["proposedTopicID6"]
      self.proposedTopicID7:str = obj["proposedTopicID7"]
      self.proposedTopicID8:str = obj["proposedTopicID8"]
      self.proposedTopicID9:str = obj["proposedTopicID9"]
      self.proposedTopicID10:str = obj["proposedTopicID10"]
      pass

class OnChangeSearchTopicID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HDCaseSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeSearchTopics_input:
   """ Required : 
   ds
   proposedTopicID1
   proposedTopicID2
   proposedTopicID3
   proposedTopicID4
   proposedTopicID5
   proposedTopicID6
   proposedTopicID7
   proposedTopicID8
   proposedTopicID9
   proposedTopicID10
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HDCaseSearchTableset] = obj["ds"]
      self.proposedTopicID1:str = obj["proposedTopicID1"]
      """  The proposed TopicID1  """  
      self.proposedTopicID2:str = obj["proposedTopicID2"]
      """  The proposed TopicID2  """  
      self.proposedTopicID3:str = obj["proposedTopicID3"]
      """  The proposed TopicID3  """  
      self.proposedTopicID4:str = obj["proposedTopicID4"]
      """  The proposed TopicID4  """  
      self.proposedTopicID5:str = obj["proposedTopicID5"]
      """  The proposed TopicID5  """  
      self.proposedTopicID6:str = obj["proposedTopicID6"]
      """  The proposed TopicID6  """  
      self.proposedTopicID7:str = obj["proposedTopicID7"]
      """  The proposed TopicID7  """  
      self.proposedTopicID8:str = obj["proposedTopicID8"]
      """  The proposed TopicID8  """  
      self.proposedTopicID9:str = obj["proposedTopicID9"]
      """  The proposed TopicID9  """  
      self.proposedTopicID10:str = obj["proposedTopicID10"]
      """  The proposed TopicID10  """  
      pass

class OnChangeSearchTopics_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HDCaseSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeSerialNumber_input:
   """ Required : 
   ds
   proposedSerialNumber
   getDefaults
   proposedPartNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedSerialNumber:str = obj["proposedSerialNumber"]
      """  The proposed SerialNumber  """  
      self.getDefaults:bool = obj["getDefaults"]
      """  Assign any fields related to SerialNumber  """  
      self.proposedPartNum:str = obj["proposedPartNum"]
      """  The proposed PartNum  """  
      pass

class OnChangeSerialNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeShipToCustID_input:
   """ Required : 
   ds
   proposedShipToCustID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedShipToCustID:str = obj["proposedShipToCustID"]
      """  Proposed Third-Party Ship To  """  
      pass

class OnChangeShipToCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeShipToNum_input:
   """ Required : 
   ds
   proposedShipToNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedShipToNum:str = obj["proposedShipToNum"]
      """  The proposed ShipToNum  """  
      pass

class OnChangeShipToNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeShpConNum_input:
   """ Required : 
   ds
   proposedShpConNum
   proposedShipToNum
   proposedShpCustNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedShpConNum:int = obj["proposedShpConNum"]
      """  The proposed ShpConNum  """  
      self.proposedShipToNum:str = obj["proposedShipToNum"]
      """  The proposed ShipToNum  """  
      self.proposedShpCustNum:int = obj["proposedShpCustNum"]
      """  The proposed ShpCustNum  """  
      pass

class OnChangeShpConNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTaskSetID_input:
   """ Required : 
   ds
   proposedTaskSetID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedTaskSetID:str = obj["proposedTaskSetID"]
      """  Proposed Third-Party Ship To  """  
      pass

class OnChangeTaskSetID_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTopics_input:
   """ Required : 
   ds
   proposedTopicID1
   proposedTopicID2
   proposedTopicID3
   proposedTopicID4
   proposedTopicID5
   proposedTopicID6
   proposedTopicID7
   proposedTopicID8
   proposedTopicID9
   proposedTopicID10
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedTopicID1:str = obj["proposedTopicID1"]
      """  The proposed TopicID1  """  
      self.proposedTopicID2:str = obj["proposedTopicID2"]
      """  The proposed TopicID2  """  
      self.proposedTopicID3:str = obj["proposedTopicID3"]
      """  The proposed TopicID3  """  
      self.proposedTopicID4:str = obj["proposedTopicID4"]
      """  The proposed TopicID4  """  
      self.proposedTopicID5:str = obj["proposedTopicID5"]
      """  The proposed TopicID5  """  
      self.proposedTopicID6:str = obj["proposedTopicID6"]
      """  The proposed TopicID6  """  
      self.proposedTopicID7:str = obj["proposedTopicID7"]
      """  The proposed TopicID7  """  
      self.proposedTopicID8:str = obj["proposedTopicID8"]
      """  The proposed TopicID8  """  
      self.proposedTopicID9:str = obj["proposedTopicID9"]
      """  The proposed TopicID9  """  
      self.proposedTopicID10:str = obj["proposedTopicID10"]
      """  The proposed TopicID10  """  
      pass

class OnChangeTopics_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeUnitPrice_input:
   """ Required : 
   proposedUnitPrice
   ds
   """  
   def __init__(self, obj):
      self.proposedUnitPrice:int = obj["proposedUnitPrice"]
      """  The proposed UnitPrice  """  
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class OnChangeUnitPrice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeVenConNum_input:
   """ Required : 
   ds
   proposedVenConNum
   proposedVendorNum
   proposedPurPoint
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedVenConNum:int = obj["proposedVenConNum"]
      """  The proposed VenConNum  """  
      self.proposedVendorNum:int = obj["proposedVendorNum"]
      """  The proposed CustNum  """  
      self.proposedPurPoint:str = obj["proposedPurPoint"]
      """  The proposed PurPoint  """  
      pass

class OnChangeVenConNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeVendorID_input:
   """ Required : 
   ds
   proposedVendorID
   getDefaults
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedVendorID:str = obj["proposedVendorID"]
      """  The proposed VendorID  """  
      self.getDefaults:bool = obj["getDefaults"]
      """  Assign any fields related to VendorID  """  
      pass

class OnChangeVendorID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeWFGroupID_input:
   """ Required : 
   ds
   proposedWFGroupID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedWFGroupID:str = obj["proposedWFGroupID"]
      """  The proposed WFGroupID  """  
      pass

class OnChangeWFGroupID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeWarrantyCode_input:
   """ Required : 
   ds
   helpDeskCaseNum
   proposedPackNum
   proposedPackLine
   proposedDropShipPackSlip
   proposedDropShipPackLine
   getDefaults
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.helpDeskCaseNum:int = obj["helpDeskCaseNum"]
      """  Current Help Desk Case Number  """  
      self.proposedPackNum:int = obj["proposedPackNum"]
      """  The proposed PackNum  """  
      self.proposedPackLine:int = obj["proposedPackLine"]
      """  The proposed PackLine  """  
      self.proposedDropShipPackSlip:str = obj["proposedDropShipPackSlip"]
      """  The proposed Drop Shipment Pack Slip  """  
      self.proposedDropShipPackLine:int = obj["proposedDropShipPackLine"]
      """  The proposed Drop Shipment Pack Line  """  
      self.getDefaults:bool = obj["getDefaults"]
      """  Assign any fields related to Packing Slip  """  
      pass

class OnChangeWarrantyCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OpenCloseCase_input:
   """ Required : 
   hdCaseNum
   closeCase
   """  
   def __init__(self, obj):
      self.hdCaseNum:int = obj["hdCaseNum"]
      """  HDCaseNum to be opened or closed  """  
      self.closeCase:bool = obj["closeCase"]
      """  Yes to close Case, no to open Case  """  
      pass

class OpenCloseCase_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_HelpDeskTableset] = obj["returnObj"]
      pass

class PreOpenCloseCase_input:
   """ Required : 
   hdCaseNum
   closeCase
   """  
   def __init__(self, obj):
      self.hdCaseNum:int = obj["hdCaseNum"]
      """  The current HDCase.HDCaseNum field  """  
      self.closeCase:bool = obj["closeCase"]
      """  Yes to close Case, no to open Case  """  
      pass

class PreOpenCloseCase_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtHelpDeskTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtHelpDeskTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateContractPart_input:
   """ Required : 
   ds
   proposedContractNum
   contractLine
   partNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedContractNum:int = obj["proposedContractNum"]
      """  The proposed service contract number  """  
      self.contractLine:int = obj["contractLine"]
      """  Contract line of the contract.  """  
      self.partNum:str = obj["partNum"]
      """  partNum of the HdCase  """  
      pass

class ValidateContractPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.WarningMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateContractStatus_input:
   """ Required : 
   ds
   proposedContractNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.proposedContractNum:int = obj["proposedContractNum"]
      """  The proposed service contract number  """  
      pass

class ValidateContractStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      self.WarningMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateFSCallRequirements_input:
   """ Required : 
   helpDeskCaseNum
   ds
   """  
   def __init__(self, obj):
      self.helpDeskCaseNum:int = obj["helpDeskCaseNum"]
      """  The Help Desk case number to use as a source  """  
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

class ValidateFSCallRequirements_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.WarningMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_HelpDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class createAvailableMilestonesList_input:
   """ Required : 
   hDCaseNum
   wFComplete
   taskSetID
   """  
   def __init__(self, obj):
      self.hDCaseNum:int = obj["hDCaseNum"]
      """  Help Desk Case Number  """  
      self.wFComplete:bool = obj["wFComplete"]
      """  Current status of the Workflow for this case. HDCase.WFComplete  """  
      self.taskSetID:str = obj["taskSetID"]
      """  Task set ID, currently assigned to this Case. (HDCase.TaskSetiID)  """  
      pass

class createAvailableMilestonesList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.availableMilestonesList:str = obj["parameters"]
      pass

      """  output parameters  """  

class createAvailableTaskSetsList_input:
   """ Required : 
   taskSetID
   wFComplete
   """  
   def __init__(self, obj):
      self.taskSetID:str = obj["taskSetID"]
      """  Task set ID, currently assigned to this Case. (HDCase.TaskSetiID)  """  
      self.wFComplete:bool = obj["wFComplete"]
      """  Current status of the Workflow for this case. HDCase.WFComplete  """  
      pass

class createAvailableTaskSetsList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.availableTaskSetsList:str = obj["parameters"]
      pass

      """  output parameters  """  

