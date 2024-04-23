import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MXGLJournalFolioImportSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_MXGLJournalFolioImports(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MXGLJournalFolioImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MXGLJournalFolioImports
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXGLJournalFolioImportParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/MXGLJournalFolioImports",headers=creds) as resp:
           return await resp.json()

async def post_MXGLJournalFolioImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MXGLJournalFolioImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MXGLJournalFolioImportParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MXGLJournalFolioImportParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/MXGLJournalFolioImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MXGLJournalFolioImports_Company_UserID(Company, UserID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MXGLJournalFolioImport item
   Description: Calls GetByID to retrieve the MXGLJournalFolioImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MXGLJournalFolioImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MXGLJournalFolioImportParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/MXGLJournalFolioImports(" + Company + "," + UserID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MXGLJournalFolioImports_Company_UserID(Company, UserID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MXGLJournalFolioImport for the service
   Description: Calls UpdateExt to update MXGLJournalFolioImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MXGLJournalFolioImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MXGLJournalFolioImportParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/MXGLJournalFolioImports(" + Company + "," + UserID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MXGLJournalFolioImports_Company_UserID(Company, UserID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MXGLJournalFolioImport item
   Description: Call UpdateExt to delete MXGLJournalFolioImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MXGLJournalFolioImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/MXGLJournalFolioImports(" + Company + "," + UserID + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLXmlFiles(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLXmlFiles items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLXmlFiles
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLXmlFileRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/GLXmlFiles",headers=creds) as resp:
           return await resp.json()

async def post_GLXmlFiles(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLXmlFiles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLXmlFileRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLXmlFileRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/GLXmlFiles", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLXmlFiles_FileName(FileName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLXmlFile item
   Description: Calls GetByID to retrieve the GLXmlFile item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLXmlFile
      :param FileName: Desc: FileName   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLXmlFileRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/GLXmlFiles(" + FileName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLXmlFiles_FileName(FileName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLXmlFile for the service
   Description: Calls UpdateExt to update GLXmlFile. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLXmlFile
      :param FileName: Desc: FileName   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLXmlFileRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/GLXmlFiles(" + FileName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLXmlFiles_FileName(FileName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLXmlFile item
   Description: Call UpdateExt to delete GLXmlFile item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLXmlFile
      :param FileName: Desc: FileName   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/GLXmlFiles(" + FileName + ")",headers=creds) as resp:
           return await resp.json()

async def get_Journals(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Journals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Journals
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JournalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/Journals",headers=creds) as resp:
           return await resp.json()

async def post_Journals(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Journals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JournalRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.JournalRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/Journals", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Journals_FileName_FiscalYear_FiscalYearSuffix_JournalCode_BookId_JournalNum_LegalNumber(FileName, FiscalYear, FiscalYearSuffix, JournalCode, BookId, JournalNum, LegalNumber, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Journal item
   Description: Calls GetByID to retrieve the Journal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Journal
      :param FileName: Desc: FileName   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param BookId: Desc: BookId   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param LegalNumber: Desc: LegalNumber   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.JournalRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/Journals(" + FileName + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + BookId + "," + JournalNum + "," + LegalNumber + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Journals_FileName_FiscalYear_FiscalYearSuffix_JournalCode_BookId_JournalNum_LegalNumber(FileName, FiscalYear, FiscalYearSuffix, JournalCode, BookId, JournalNum, LegalNumber, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Journal for the service
   Description: Calls UpdateExt to update Journal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Journal
      :param FileName: Desc: FileName   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param BookId: Desc: BookId   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param LegalNumber: Desc: LegalNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.JournalRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/Journals(" + FileName + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + BookId + "," + JournalNum + "," + LegalNumber + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Journals_FileName_FiscalYear_FiscalYearSuffix_JournalCode_BookId_JournalNum_LegalNumber(FileName, FiscalYear, FiscalYearSuffix, JournalCode, BookId, JournalNum, LegalNumber, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Journal item
   Description: Call UpdateExt to delete Journal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Journal
      :param FileName: Desc: FileName   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param BookId: Desc: BookId   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param LegalNumber: Desc: LegalNumber   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/Journals(" + FileName + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + BookId + "," + JournalNum + "," + LegalNumber + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXGLJournalFolioImportListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseMXGLJournalFolioImportParam, whereClauseGLXmlFile, whereClauseJournal, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseMXGLJournalFolioImportParam=" + whereClauseMXGLJournalFolioImportParam
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLXmlFile=" + whereClauseGLXmlFile
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseJournal=" + whereClauseJournal
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(company, userID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "userID=" + userID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewParameters(epicorHeaders = None):
   """  
   Summary: Invoke method GetNewParameters
   Description: Get default parameters for current user.
   OperationID: GetNewParameters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewParameters_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaults
   Description: Get default parameters for current user.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SaveDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SaveDefaults
   Description: Save default parameters for current user.
   OperationID: SaveDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemoveDefaults(epicorHeaders = None):
   """  
   Summary: Invoke method RemoveDefaults
   Description: Remove default parameters for current user.
   OperationID: RemoveDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ParseXmls(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ParseXmls
   Description: Parses XMLs in order to retrieve Fiscal Folio and auto map them to GLJournals
   OperationID: ParseXmls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ParseXmls_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ParseXmls_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ParseXmlsInStr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ParseXmlsInStr
   Description: Parses XMLs in order to retrieve Fiscal Folio and auto map them to GLJournals
   OperationID: ParseXmlsInStr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ParseXmlsInStr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ParseXmlsInStr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnMatchedChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnMatchedChanged
   Description: Match or unmatch xml and journal
   OperationID: OnMatchedChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnMatchedChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnMatchedChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnMatchedChanged_Ref(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnMatchedChanged_Ref
   Description: Match or unmatch xml and payment
   OperationID: OnMatchedChanged_Ref
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnMatchedChanged_Ref_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnMatchedChanged_Ref_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateFiscalFolio(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateFiscalFolio
   Description: Finally updates Fiscal Folio on all matched AP journals
   OperationID: UpdateFiscalFolio
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateFiscalFolio_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateFiscalFolio_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXGLJournalFolioImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLXmlFileRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLXmlFileRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JournalRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_JournalRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXGLJournalFolioImportListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MXGLJournalFolioImportListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXGLJournalFolioImportParamRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MXGLJournalFolioImportParamRow] = obj["value"]
      pass

class Erp_Tablesets_GLXmlFileRow:
   def __init__(self, obj):
      self.FileName:str = obj["FileName"]
      """  File Name  """  
      self.ErrorMessage:str = obj["ErrorMessage"]
      """  Error Message  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code  """  
      self.TaxId:str = obj["TaxId"]
      """  Tax ID  """  
      self.Serie:str = obj["Serie"]
      """  Serie  """  
      self.Folio:str = obj["Folio"]
      """  Folio  """  
      self.JournalDate:str = obj["JournalDate"]
      """  Journal Date  """  
      self.JournalAmt:int = obj["JournalAmt"]
      """  Journal Amount  """  
      self.IsMatched:bool = obj["IsMatched"]
      """  Is file matched with invoice  """  
      self.FiscalFolio:str = obj["FiscalFolio"]
      """  Fiscal Folio  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number  """  
      self.JournalNum:int = obj["JournalNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JournalRow:
   def __init__(self, obj):
      self.FileName:str = obj["FileName"]
      """  Xml File Name  """  
      self.FiscalFolio:str = obj["FiscalFolio"]
      """  Fiscal Folio  """  
      self.JournalAmt:int = obj["JournalAmt"]
      """  Journal Amount  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code  """  
      self.JournalDate:str = obj["JournalDate"]
      """  Journal Date  """  
      self.LegalNumber:str = obj["LegalNumber"]
      self.TaxId:str = obj["TaxId"]
      """  Tax ID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.BookId:str = obj["BookId"]
      """  Book ID  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal Num  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MXGLJournalFolioImportListRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MXGLJournalFolioImportParamRow:
   def __init__(self, obj):
      self.BookId:str = obj["BookId"]
      """  Book ID  """  
      self.FiscalFolioXPath:str = obj["FiscalFolioXPath"]
      """  XPath to Fiscal Folio field  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.JournalAmtXPath:str = obj["JournalAmtXPath"]
      """  XPath to Journal Amount field  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code  """  
      self.JournalDateXPath:str = obj["JournalDateXPath"]
      """  XPath to Journal Date field  """  
      self.JournalFolioXPath:str = obj["JournalFolioXPath"]
      """  XPath to Journal Folio field  """  
      self.JournalSerieXPath:str = obj["JournalSerieXPath"]
      """  XPath to Journal Serie field  """  
      self.TaxIdXPath:str = obj["TaxIdXPath"]
      """  XPath to Tax ID field  """  
      self.JournalDateIsUsed:bool = obj["JournalDateIsUsed"]
      """  Enable/disable Journal Date field value for additional search with manual matching  """  
      self.JournalAmtIsUsed:bool = obj["JournalAmtIsUsed"]
      """  Enable/disable Journal Amount field value for additional search with manual matching  """  
      self.Company:str = obj["Company"]
      self.UserID:str = obj["UserID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_GLXmlFileRow:
   def __init__(self, obj):
      self.FileName:str = obj["FileName"]
      """  File Name  """  
      self.ErrorMessage:str = obj["ErrorMessage"]
      """  Error Message  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code  """  
      self.TaxId:str = obj["TaxId"]
      """  Tax ID  """  
      self.Serie:str = obj["Serie"]
      """  Serie  """  
      self.Folio:str = obj["Folio"]
      """  Folio  """  
      self.JournalDate:str = obj["JournalDate"]
      """  Journal Date  """  
      self.JournalAmt:int = obj["JournalAmt"]
      """  Journal Amount  """  
      self.IsMatched:bool = obj["IsMatched"]
      """  Is file matched with invoice  """  
      self.FiscalFolio:str = obj["FiscalFolio"]
      """  Fiscal Folio  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number  """  
      self.JournalNum:int = obj["JournalNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JournalRow:
   def __init__(self, obj):
      self.FileName:str = obj["FileName"]
      """  Xml File Name  """  
      self.FiscalFolio:str = obj["FiscalFolio"]
      """  Fiscal Folio  """  
      self.JournalAmt:int = obj["JournalAmt"]
      """  Journal Amount  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code  """  
      self.JournalDate:str = obj["JournalDate"]
      """  Journal Date  """  
      self.LegalNumber:str = obj["LegalNumber"]
      self.TaxId:str = obj["TaxId"]
      """  Tax ID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.BookId:str = obj["BookId"]
      """  Book ID  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal Num  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MXGLJournalFolioImportListRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MXGLJournalFolioImportListTableset:
   def __init__(self, obj):
      self.MXGLJournalFolioImportList:list[Erp_Tablesets_MXGLJournalFolioImportListRow] = obj["MXGLJournalFolioImportList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MXGLJournalFolioImportParamRow:
   def __init__(self, obj):
      self.BookId:str = obj["BookId"]
      """  Book ID  """  
      self.FiscalFolioXPath:str = obj["FiscalFolioXPath"]
      """  XPath to Fiscal Folio field  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.JournalAmtXPath:str = obj["JournalAmtXPath"]
      """  XPath to Journal Amount field  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code  """  
      self.JournalDateXPath:str = obj["JournalDateXPath"]
      """  XPath to Journal Date field  """  
      self.JournalFolioXPath:str = obj["JournalFolioXPath"]
      """  XPath to Journal Folio field  """  
      self.JournalSerieXPath:str = obj["JournalSerieXPath"]
      """  XPath to Journal Serie field  """  
      self.TaxIdXPath:str = obj["TaxIdXPath"]
      """  XPath to Tax ID field  """  
      self.JournalDateIsUsed:bool = obj["JournalDateIsUsed"]
      """  Enable/disable Journal Date field value for additional search with manual matching  """  
      self.JournalAmtIsUsed:bool = obj["JournalAmtIsUsed"]
      """  Enable/disable Journal Amount field value for additional search with manual matching  """  
      self.Company:str = obj["Company"]
      self.UserID:str = obj["UserID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MXGLJournalFolioImportTableset:
   def __init__(self, obj):
      self.MXGLJournalFolioImportParam:list[Erp_Tablesets_MXGLJournalFolioImportParamRow] = obj["MXGLJournalFolioImportParam"]
      self.GLXmlFile:list[Erp_Tablesets_GLXmlFileRow] = obj["GLXmlFile"]
      self.Journal:list[Erp_Tablesets_JournalRow] = obj["Journal"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtMXGLJournalFolioImportTableset:
   def __init__(self, obj):
      self.MXGLJournalFolioImportParam:list[Erp_Tablesets_MXGLJournalFolioImportParamRow] = obj["MXGLJournalFolioImportParam"]
      self.GLXmlFile:list[Erp_Tablesets_GLXmlFileRow] = obj["GLXmlFile"]
      self.Journal:list[Erp_Tablesets_JournalRow] = obj["Journal"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   company
   userID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.userID:str = obj["userID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MXGLJournalFolioImportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MXGLJournalFolioImportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MXGLJournalFolioImportTableset] = obj["returnObj"]
      pass

class GetDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MXGLJournalFolioImportTableset] = obj["ds"]
      pass

class GetDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MXGLJournalFolioImportTableset] = obj["ds"]
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
      self.returnObj:list[Erp_Tablesets_MXGLJournalFolioImportListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewParameters_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MXGLJournalFolioImportTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseMXGLJournalFolioImportParam
   whereClauseGLXmlFile
   whereClauseJournal
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMXGLJournalFolioImportParam:str = obj["whereClauseMXGLJournalFolioImportParam"]
      self.whereClauseGLXmlFile:str = obj["whereClauseGLXmlFile"]
      self.whereClauseJournal:str = obj["whereClauseJournal"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MXGLJournalFolioImportTableset] = obj["returnObj"]
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

class OnMatchedChanged_Ref_input:
   """ Required : 
   ds
   newIsMatched
   filename
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MXGLJournalFolioImportTableset] = obj["ds"]
      self.newIsMatched:bool = obj["newIsMatched"]
      self.filename:str = obj["filename"]
      pass

class OnMatchedChanged_Ref_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MXGLJournalFolioImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnMatchedChanged_input:
   """ Required : 
   ds
   newIsMatched
   filename
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MXGLJournalFolioImportTableset] = obj["ds"]
      self.newIsMatched:bool = obj["newIsMatched"]
      self.filename:str = obj["filename"]
      pass

class OnMatchedChanged_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MXGLJournalFolioImportTableset] = obj["returnObj"]
      pass

class ParseXmlsInStr_input:
   """ Required : 
   ds
   filenames
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MXGLJournalFolioImportTableset] = obj["ds"]
      self.filenames:str = obj["filenames"]
      """  list of filename, delimited by '|'  """  
      pass

class ParseXmlsInStr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MXGLJournalFolioImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ParseXmls_input:
   """ Required : 
   ds
   filenames
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MXGLJournalFolioImportTableset] = obj["ds"]
      self.filenames:str = obj["filenames"]
      pass

class ParseXmls_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MXGLJournalFolioImportTableset] = obj["returnObj"]
      pass

class RemoveDefaults_output:
   def __init__(self, obj):
      pass

class SaveDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MXGLJournalFolioImportTableset] = obj["ds"]
      pass

class SaveDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MXGLJournalFolioImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMXGLJournalFolioImportTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMXGLJournalFolioImportTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateFiscalFolio_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MXGLJournalFolioImportTableset] = obj["ds"]
      pass

class UpdateFiscalFolio_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MXGLJournalFolioImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MXGLJournalFolioImportTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MXGLJournalFolioImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

