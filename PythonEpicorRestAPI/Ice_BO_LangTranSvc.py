import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.LangTranSvc
# Description: LangTran service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_LangTrans(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LangTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LangTrans
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.LangTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/LangTrans",headers=creds) as resp:
           return await resp.json()

async def post_LangTrans(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LangTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.LangTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.LangTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/LangTrans", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LangTrans_Company_LangNameID_OrgTextID_ProgramID(Company, LangNameID, OrgTextID, ProgramID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LangTran item
   Description: Calls GetByID to retrieve the LangTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LangTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LangNameID: Desc: LangNameID   Required: True   Allow empty value : True
      :param OrgTextID: Desc: OrgTextID   Required: True
      :param ProgramID: Desc: ProgramID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.LangTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/LangTrans(" + Company + "," + LangNameID + "," + OrgTextID + "," + ProgramID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LangTrans_Company_LangNameID_OrgTextID_ProgramID(Company, LangNameID, OrgTextID, ProgramID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LangTran for the service
   Description: Calls UpdateExt to update LangTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LangTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LangNameID: Desc: LangNameID   Required: True   Allow empty value : True
      :param OrgTextID: Desc: OrgTextID   Required: True
      :param ProgramID: Desc: ProgramID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.LangTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/LangTrans(" + Company + "," + LangNameID + "," + OrgTextID + "," + ProgramID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LangTrans_Company_LangNameID_OrgTextID_ProgramID(Company, LangNameID, OrgTextID, ProgramID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LangTran item
   Description: Call UpdateExt to delete LangTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LangTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LangNameID: Desc: LangNameID   Required: True   Allow empty value : True
      :param OrgTextID: Desc: OrgTextID   Required: True
      :param ProgramID: Desc: ProgramID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/LangTrans(" + Company + "," + LangNameID + "," + OrgTextID + "," + ProgramID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.LangTranListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseLangTran, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseLangTran=" + whereClauseLangTran
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(company, langNameID, orgTextID, programID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
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
   params += "langNameID=" + langNameID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "orgTextID=" + orgTextID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "programID=" + programID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetProgTrans(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetProgTrans
   Description: This method returns a list of program specific translations for a original text and language.
   OperationID: GetProgTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetProgTrans_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetProgTrans_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTransByProgramID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTransByProgramID
   Description: This method returns a list of translations from a start at program id
   OperationID: GetTransByProgramID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTransByProgramID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransByProgramID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTransByText(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTransByText
   Description: This method returns a list of translations from a start at text.
   OperationID: GetTransByText
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTransByText_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransByText_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTransByTextID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTransByTextID
   Description: This method returns a list of translations from a start at text id
   OperationID: GetTransByTextID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTransByTextID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransByTextID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTransByTranslation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTransByTranslation
   Description: This method returns a list of translations from a start at translated text
   OperationID: GetTransByTranslation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTransByTranslation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransByTranslation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateAll
   Description: This method update LangTran table
Not used - obsoleted in 11.1.200.
   OperationID: UpdateAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteTranRecords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteTranRecords
   Description: Deletes Translation
   OperationID: DeleteTranRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteTranRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteTranRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportXml(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportXml
   Description: Import translations passed from XML via TranTextTableset.
   OperationID: ImportXml
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportXml_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportXml_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Translate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Translate
   Description: Translate procedure
   OperationID: Translate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Translate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Translate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTranslationForTool(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTranslationForTool
   Description: Get Translations to show in Translation Tool
Works similar to Translate method, but divides Program specific and indenendent translations into 2 columns,
as expected by Translation Tool
   OperationID: GetTranslationForTool
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTranslationForTool_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTranslationForTool_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetAppTranslations(programID, languageID, request, epicorHeaders = None):
   """  
   Summary: Invoke method GetAppTranslations
   Description: This methods gets the MetaUI application translations.
   OperationID: Get_GetAppTranslations
      :param programID: Desc: The program ID.   Required: True   Allow empty value : True
      :param languageID: Desc: language ID.   Required: True   Allow empty value : True
      :param request: Desc: MetaFX request (JSON serialized) to get the application strings   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAppTranslations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "programID=" + programID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "languageID=" + languageID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "request=" + request

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_UpdateTranslations(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateTranslations
   Description: This method update translations and also LangOrg, LangXref if necessary
   OperationID: UpdateTranslations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateTranslations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateTranslations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteTranslation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteTranslation
   Description: Deletes Translation
   OperationID: DeleteTranslation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteTranslation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteTranslation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateSingleTranslation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateSingleTranslation
   Description: Updates single translation.
   OperationID: UpdateSingleTranslation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateSingleTranslation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSingleTranslation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteTranslations(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteTranslations
   Description: Delete all translations for specified language.
   OperationID: DeleteTranslations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteTranslations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteTranslations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteCustomizedTranslations(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteCustomizedTranslations
   Description: Delete all custom translations (ID less than 0) for a specified language.
   OperationID: DeleteCustomizedTranslations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteCustomizedTranslations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteCustomizedTranslations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemoveOrphans(epicorHeaders = None):
   """  
   Summary: Invoke method RemoveOrphans
   Description: Remove Orphan records
   OperationID: RemoveOrphans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveOrphans_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_DeleteRecordsNotInList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteRecordsNotInList
   Description: Delete Language records whose ID is not in the list passed.
   OperationID: DeleteRecordsNotInList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteRecordsNotInList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRecordsNotInList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportTranslationData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportTranslationData
   Description: Import translation data
   OperationID: ImportTranslationData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportTranslationData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportTranslationData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportTranslationData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportTranslationData
   Description: Export translation data
   OperationID: ExportTranslationData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportTranslationData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportTranslationData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportToFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportToFile
   Description: Export translation data to file
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLicensedModules(epicorHeaders = None):
   """  
   Summary: Invoke method GetLicensedModules
   Description: Gets the list of licensed (installed and enabled) modules.
   OperationID: GetLicensedModules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLicensedModules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewLangTran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLangTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLangTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLangTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLangTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_LangTranListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_LangTranListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_LangTranRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_LangTranRow] = obj["value"]
      pass

class Ice_Tablesets_LangTranListRow:
   def __init__(self, obj):
      self.LangNameID:str = obj["LangNameID"]
      """  Language ID  """  
      self.OrgTextID:int = obj["OrgTextID"]
      """  Original Text ID  """  
      self.ProgramID:str = obj["ProgramID"]
      """  Program ID  """  
      self.TransText:str = obj["TransText"]
      """  Translated text.  """  
      self.CustomTrans:bool = obj["CustomTrans"]
      """  Custom Translation  """  
      self.SortTransText:str = obj["SortTransText"]
      """  The first 50 characters from TransText  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HasError:bool = obj["HasError"]
      """  Indicating if an error occured during update  """  
      self.ErrMessage:str = obj["ErrMessage"]
      """  Error returned by update  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      """  Language Name Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_LangTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Language ID  """  
      self.OrgTextID:int = obj["OrgTextID"]
      """  Original Text ID  """  
      self.ProgramID:str = obj["ProgramID"]
      """  Program ID  """  
      self.TransText:str = obj["TransText"]
      """  Translated text.  """  
      self.CustomTrans:bool = obj["CustomTrans"]
      """  Custom Translation  """  
      self.SortTransText:str = obj["SortTransText"]
      """  The first 50 characters from TransText  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.OrigOrgTextID:int = obj["OrigOrgTextID"]
      """  OrigOrgTextID  """  
      self.NomenclatureID:str = obj["NomenclatureID"]
      """  NomenclatureID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ErrMessage:str = obj["ErrMessage"]
      """  Error returned by update  """  
      self.HasError:bool = obj["HasError"]
      """  Indicating if an error occured during update  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   company
   langNameID
   orgTextID
   programID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.langNameID:str = obj["langNameID"]
      self.orgTextID:int = obj["orgTextID"]
      self.programID:str = obj["programID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteCustomizedTranslations_input:
   """ Required : 
   companyID
   languageID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  Company ID  """  
      self.languageID:str = obj["languageID"]
      """  Language ID  """  
      pass

class DeleteCustomizedTranslations_output:
   def __init__(self, obj):
      pass

class DeleteRecordsNotInList_input:
   """ Required : 
   companyID
   listOrgTextID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  Company ID.  """  
      self.listOrgTextID:int = obj["listOrgTextID"]
      """  List Of IDs.  """  
      pass

class DeleteRecordsNotInList_output:
   def __init__(self, obj):
      pass

class DeleteTranRecords_input:
   """ Required : 
   companyID
   pcLanguageID
   pcProgramID
   pcOrgTextID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  The company ID  """  
      self.pcLanguageID:str = obj["pcLanguageID"]
      """  The language ID  """  
      self.pcProgramID:str = obj["pcProgramID"]
      """  The program ID  """  
      self.pcOrgTextID:int = obj["pcOrgTextID"]
      """  ID  """  
      pass

class DeleteTranRecords_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.bSucceed:bool = obj["bSucceed"]
      pass

      """  output parameters  """  

class DeleteTranslation_input:
   """ Required : 
   company
   pcLanguageID
   pcProgramID
   pcText
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  The company ID.  """  
      self.pcLanguageID:str = obj["pcLanguageID"]
      """  The language ID  """  
      self.pcProgramID:str = obj["pcProgramID"]
      """  The program ID  """  
      self.pcText:str = obj["pcText"]
      """  Text  """  
      pass

class DeleteTranslation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.bSucceed:bool = obj["bSucceed"]
      pass

      """  output parameters  """  

class DeleteTranslations_input:
   """ Required : 
   companyID
   languageID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  Company ID  """  
      self.languageID:str = obj["languageID"]
      """  Language ID  """  
      pass

class DeleteTranslations_output:
   def __init__(self, obj):
      pass

class ExportToFile_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_TranslationDataTableset] = obj["ds"]
      pass

class ExportToFile_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_TranslationDataTableset] = obj["returnObj"]
      pass

class ExportTranslationData_input:
   """ Required : 
   companyID
   languageID
   withReferences
   onlyCustomization
   onlyTranslated
   onlyUntranslated
   fromOrgTextID
   toOrgTextID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  Company ID  """  
      self.languageID:str = obj["languageID"]
      """  Language ID  """  
      self.withReferences:bool = obj["withReferences"]
      """  Export ProgramID references  """  
      self.onlyCustomization:bool = obj["onlyCustomization"]
      """  Only customized  """  
      self.onlyTranslated:bool = obj["onlyTranslated"]
      """  Only translated  """  
      self.onlyUntranslated:bool = obj["onlyUntranslated"]
      """  Only untranslated  """  
      self.fromOrgTextID:int = obj["fromOrgTextID"]
      """  From ID  """  
      self.toOrgTextID:int = obj["toOrgTextID"]
      """  To ID  """  
      pass

class ExportTranslationData_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_TranslationDataTableset] = obj["returnObj"]
      pass

class GetAppTranslations_input:
   """ Required : 
   programID
   languageID
   request
   """  
   def __init__(self, obj):
      self.programID:str = obj["programID"]
      """  The program ID.  """  
      self.languageID:str = obj["languageID"]
      """  language ID.  """  
      self.request:str = obj["request"]
      """  MetaFX request (JSON serialized) to get the application strings  """  
      pass

class GetAppTranslations_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_TranTextTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   company
   langNameID
   orgTextID
   programID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.langNameID:str = obj["langNameID"]
      self.orgTextID:int = obj["orgTextID"]
      self.programID:str = obj["programID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_LangTranTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_LangTranTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_LangTranTableset] = obj["returnObj"]
      pass

class GetLicensedModules_output:
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
      self.returnObj:list[Ice_Tablesets_LangTranListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewLangTran_input:
   """ Required : 
   ds
   company
   langNameID
   orgTextID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_LangTranTableset] = obj["ds"]
      self.company:str = obj["company"]
      self.langNameID:str = obj["langNameID"]
      self.orgTextID:int = obj["orgTextID"]
      pass

class GetNewLangTran_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_LangTranTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetProgTrans_input:
   """ Required : 
   companyID
   pcLanguageID
   piOrigTextID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  The company ID.  """  
      self.pcLanguageID:str = obj["pcLanguageID"]
      """  The language ID.  """  
      self.piOrigTextID:int = obj["piOrigTextID"]
      """  The original text ID.  """  
      pass

class GetProgTrans_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_TranTextTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseLangTran
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseLangTran:str = obj["whereClauseLangTran"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_LangTranTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTransByProgramID_input:
   """ Required : 
   pcLangID
   pcProgID
   """  
   def __init__(self, obj):
      self.pcLangID:str = obj["pcLangID"]
      """  The language ID  """  
      self.pcProgID:str = obj["pcProgID"]
      """  The start at program ID  """  
      pass

class GetTransByProgramID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_TranTextTableset] = obj["returnObj"]
      pass

class GetTransByTextID_input:
   """ Required : 
   pcLangID
   piTextID
   """  
   def __init__(self, obj):
      self.pcLangID:str = obj["pcLangID"]
      """  The language ID  """  
      self.piTextID:int = obj["piTextID"]
      """  The start at text ID  """  
      pass

class GetTransByTextID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_TranTextTableset] = obj["returnObj"]
      pass

class GetTransByText_input:
   """ Required : 
   companyID
   pcLangID
   pcText
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  The company ID.  """  
      self.pcLangID:str = obj["pcLangID"]
      """  The language ID.  """  
      self.pcText:str = obj["pcText"]
      """  The start at text.  """  
      pass

class GetTransByText_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_TranTextTableset] = obj["returnObj"]
      pass

class GetTransByTranslation_input:
   """ Required : 
   pcLangID
   pcTranslation
   """  
   def __init__(self, obj):
      self.pcLangID:str = obj["pcLangID"]
      """  The language ID  """  
      self.pcTranslation:str = obj["pcTranslation"]
      """  The start at translated text  """  
      pass

class GetTransByTranslation_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_TranTextTableset] = obj["returnObj"]
      pass

class GetTranslationForTool_input:
   """ Required : 
   ds
   bAddIfMissing
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_TranTextTableset] = obj["ds"]
      self.bAddIfMissing:bool = obj["bAddIfMissing"]
      """  If True and record is missing in LangOrg, it will be added  """  
      pass

class GetTranslationForTool_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_TranTextTableset] = obj["returnObj"]
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

class Ice_Tablesets_LangTranExportOptionsRow:
   def __init__(self, obj):
      self.Start:int = obj["Start"]
      """  Range start.  """  
      self.End:int = obj["End"]
      """  Range end.  """  
      self.IncludeReferences:bool = obj["IncludeReferences"]
      """  If export should include ProgramID references.  """  
      self.OnlyTranslated:bool = obj["OnlyTranslated"]
      """  If the export should only included translated text entries.  """  
      self.OnlyUntranslated:bool = obj["OnlyUntranslated"]
      """  If the export should include only untranslated text entries.  """  
      self.OnlyCustomization:bool = obj["OnlyCustomization"]
      """  If the export should only contain user-defined translation text entries.  """  
      self.Company:str = obj["Company"]
      """  Company.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Language Name ID.  """  
      self.ServerFileName:str = obj["ServerFileName"]
      """  Export server filename.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_LangTranListRow:
   def __init__(self, obj):
      self.LangNameID:str = obj["LangNameID"]
      """  Language ID  """  
      self.OrgTextID:int = obj["OrgTextID"]
      """  Original Text ID  """  
      self.ProgramID:str = obj["ProgramID"]
      """  Program ID  """  
      self.TransText:str = obj["TransText"]
      """  Translated text.  """  
      self.CustomTrans:bool = obj["CustomTrans"]
      """  Custom Translation  """  
      self.SortTransText:str = obj["SortTransText"]
      """  The first 50 characters from TransText  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HasError:bool = obj["HasError"]
      """  Indicating if an error occured during update  """  
      self.ErrMessage:str = obj["ErrMessage"]
      """  Error returned by update  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      """  Language Name Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_LangTranListTableset:
   def __init__(self, obj):
      self.LangTranList:list[Ice_Tablesets_LangTranListRow] = obj["LangTranList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_LangTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Language ID  """  
      self.OrgTextID:int = obj["OrgTextID"]
      """  Original Text ID  """  
      self.ProgramID:str = obj["ProgramID"]
      """  Program ID  """  
      self.TransText:str = obj["TransText"]
      """  Translated text.  """  
      self.CustomTrans:bool = obj["CustomTrans"]
      """  Custom Translation  """  
      self.SortTransText:str = obj["SortTransText"]
      """  The first 50 characters from TransText  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.OrigOrgTextID:int = obj["OrigOrgTextID"]
      """  OrigOrgTextID  """  
      self.NomenclatureID:str = obj["NomenclatureID"]
      """  NomenclatureID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ErrMessage:str = obj["ErrMessage"]
      """  Error returned by update  """  
      self.HasError:bool = obj["HasError"]
      """  Indicating if an error occured during update  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_LangTranTableset:
   def __init__(self, obj):
      self.LangTran:list[Ice_Tablesets_LangTranRow] = obj["LangTran"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_TranDataHeaderRow:
   def __init__(self, obj):
      self.LanguageID:str = obj["LanguageID"]
      self.Description:str = obj["Description"]
      self.FileVersion:str = obj["FileVersion"]
      self.TranDate:str = obj["TranDate"]
      self.Company:str = obj["Company"]
      self.CompanyVisibility:int = obj["CompanyVisibility"]
      """  Company visibility. Either 0 if the record is database-wide or 10 if it is company-specific.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  If the translation texts are system (Epicor) data.  """  
      self.NomenclatureID:str = obj["NomenclatureID"]
      """  UID of the license module that the translation data uses,  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_TranDataRow:
   def __init__(self, obj):
      self.OrgTextID:int = obj["OrgTextID"]
      self.OriginalText:str = obj["OriginalText"]
      self.TranslatedText:str = obj["TranslatedText"]
      self.ProgramID:str = obj["ProgramID"]
      self.ErrorCode:int = obj["ErrorCode"]
      self.ProgramSpecific:bool = obj["ProgramSpecific"]
      self.Company:str = obj["Company"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.OrigOrgTextID:int = obj["OrigOrgTextID"]
      """  Original OrgTextID.  """  
      self.NomenclatureID:str = obj["NomenclatureID"]
      """  Nomenclature ID.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_TranTextLayerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ErrorCode:int = obj["ErrorCode"]
      self.LanguageID:str = obj["LanguageID"]
      self.NomenclatureID:str = obj["NomenclatureID"]
      """  Nomenclature ID, i.e. the UID of the module used for this translation text.  """  
      self.OrgTextID:int = obj["OrgTextID"]
      self.OriginalText:str = obj["OriginalText"]
      self.OrigOrgTextID:int = obj["OrigOrgTextID"]
      """  If a customization is applied to the texts, this contains the OrgTextID of the original translation.  """  
      self.ProgramID:str = obj["ProgramID"]
      self.ProgTranText:str = obj["ProgTranText"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.TranslatedText:str = obj["TranslatedText"]
      self.Layer:str = obj["Layer"]
      """  Layer, either Base or Customization.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_TranTextRow:
   def __init__(self, obj):
      self.LanguageID:str = obj["LanguageID"]
      self.ProgramID:str = obj["ProgramID"]
      self.OriginalText:str = obj["OriginalText"]
      self.TranslatedText:str = obj["TranslatedText"]
      self.ProgTranText:str = obj["ProgTranText"]
      self.OrgTextID:int = obj["OrgTextID"]
      self.ErrorCode:int = obj["ErrorCode"]
      self.Company:str = obj["Company"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.NomenclatureID:str = obj["NomenclatureID"]
      """  Nomenclature ID, i.e. the UID of the module used for this translation text.  """  
      self.OrigOrgTextID:int = obj["OrigOrgTextID"]
      """  If a customization is applied to the texts, this contains the OrgTextID of the original translation.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_TranTextTableset:
   def __init__(self, obj):
      self.TranText:list[Ice_Tablesets_TranTextRow] = obj["TranText"]
      self.TranTextLayer:list[Ice_Tablesets_TranTextLayerRow] = obj["TranTextLayer"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_TranslationDataTableset:
   def __init__(self, obj):
      self.TranData:list[Ice_Tablesets_TranDataRow] = obj["TranData"]
      self.LangTranExportOptions:list[Ice_Tablesets_LangTranExportOptionsRow] = obj["LangTranExportOptions"]
      self.TranDataHeader:list[Ice_Tablesets_TranDataHeaderRow] = obj["TranDataHeader"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtLangTranTableset:
   def __init__(self, obj):
      self.LangTran:list[Ice_Tablesets_LangTranRow] = obj["LangTran"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ImportTranslationData_input:
   """ Required : 
   ds
   overwriteTranslations
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_TranslationDataTableset] = obj["ds"]
      self.overwriteTranslations:bool = obj["overwriteTranslations"]
      """  Overwrite Translation  """  
      pass

class ImportTranslationData_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_TranslationDataTableset] = obj["returnObj"]
      pass

class ImportXml_input:
   """ Required : 
   ds
   bCustomization
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_TranTextTableset] = obj["ds"]
      self.bCustomization:bool = obj["bCustomization"]
      """  If true and record is missing in LangOrg, it will be added.  """  
      pass

class ImportXml_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_TranTextTableset] = obj["returnObj"]
      pass

class RemoveOrphans_output:
   def __init__(self, obj):
      pass

class Translate_input:
   """ Required : 
   ds
   bAddIfMissing
   bFindSimilar
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_TranTextTableset] = obj["ds"]
      self.bAddIfMissing:bool = obj["bAddIfMissing"]
      """  If True and record is missing in LangOrg, it will be added  """  
      self.bFindSimilar:bool = obj["bFindSimilar"]
      """  If True search for similar record when exact unmatched  """  
      pass

class Translate_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_TranTextTableset] = obj["returnObj"]
      pass

class UpdateAll_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_LangTranTableset] = obj["ds"]
      pass

class UpdateAll_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_LangTranTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtLangTranTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtLangTranTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateSingleTranslation_input:
   """ Required : 
   company
   pcLanguage
   pcProgram
   pcText
   pcTranslation
   pcProgTranslation
   nomenclatureId
   system
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  Company  """  
      self.pcLanguage:str = obj["pcLanguage"]
      """  Language  """  
      self.pcProgram:str = obj["pcProgram"]
      """  Program  """  
      self.pcText:str = obj["pcText"]
      """  Text  """  
      self.pcTranslation:str = obj["pcTranslation"]
      """  Translation  """  
      self.pcProgTranslation:str = obj["pcProgTranslation"]
      """  Program-specific translation  """  
      self.nomenclatureId:str = obj["nomenclatureId"]
      """  Nomenclature ID (null if not set).  """  
      self.system:bool = obj["system"]
      """  If system (if there is no Productization enabled, it will be set to false)  """  
      pass

class UpdateSingleTranslation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.success:bool = obj["success"]
      pass

      """  output parameters  """  

class UpdateTranslations_input:
   """ Required : 
   ds
   pbUpdateLangOrg
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_TranTextTableset] = obj["ds"]
      self.pbUpdateLangOrg:bool = obj["pbUpdateLangOrg"]
      """  Flag indicating if a LangOrg should be created if not exists  """  
      pass

class UpdateTranslations_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_TranTextTableset] = obj["ds"]
      self.bReturn:bool = obj["bReturn"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_LangTranTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_LangTranTableset] = obj["ds"]
      pass

      """  output parameters  """  

