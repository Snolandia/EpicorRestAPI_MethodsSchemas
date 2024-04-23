import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.LangNameSvc
# Description: LangName service.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_LangNames(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LangNames items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LangNames
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.LangNameRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/LangNames",headers=creds) as resp:
           return await resp.json()

async def post_LangNames(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LangNames
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.LangNameRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.LangNameRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/LangNames", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LangNames_Company_LangNameID(Company, LangNameID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LangName item
   Description: Calls GetByID to retrieve the LangName item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LangName
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LangNameID: Desc: LangNameID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.LangNameRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/LangNames(" + Company + "," + LangNameID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LangNames_Company_LangNameID(Company, LangNameID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LangName for the service
   Description: Calls UpdateExt to update LangName. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LangName
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LangNameID: Desc: LangNameID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.LangNameRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/LangNames(" + Company + "," + LangNameID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LangNames_Company_LangNameID(Company, LangNameID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LangName item
   Description: Call UpdateExt to delete LangName item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LangName
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LangNameID: Desc: LangNameID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/LangNames(" + Company + "," + LangNameID + ")",headers=creds) as resp:
           return await resp.json()

async def get_Cultures(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Cultures items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Cultures
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.CultureRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/Cultures",headers=creds) as resp:
           return await resp.json()

async def post_Cultures(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Cultures
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.CultureRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.CultureRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/Cultures", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Cultures_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Culture item
   Description: Calls GetByID to retrieve the Culture item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Culture
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.CultureRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/Cultures(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Cultures_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Culture for the service
   Description: Calls UpdateExt to update Culture. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Culture
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.CultureRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/Cultures(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Cultures_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Culture item
   Description: Call UpdateExt to delete Culture item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Culture
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/Cultures(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_NomenclatureModules(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get NomenclatureModules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_NomenclatureModules
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.NomenclatureModuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/NomenclatureModules",headers=creds) as resp:
           return await resp.json()

async def post_NomenclatureModules(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_NomenclatureModules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.NomenclatureModuleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.NomenclatureModuleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/NomenclatureModules", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_NomenclatureModules_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the NomenclatureModule item
   Description: Calls GetByID to retrieve the NomenclatureModule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NomenclatureModule
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.NomenclatureModuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/NomenclatureModules(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_NomenclatureModules_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update NomenclatureModule for the service
   Description: Calls UpdateExt to update NomenclatureModule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_NomenclatureModule
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.NomenclatureModuleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/NomenclatureModules(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_NomenclatureModules_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete NomenclatureModule item
   Description: Call UpdateExt to delete NomenclatureModule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_NomenclatureModule
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/NomenclatureModules(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.LangNameListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseLangName, whereClauseCulture, whereClauseNomenclatureModule, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseLangName=" + whereClauseLangName
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCulture=" + whereClauseCulture
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseNomenclatureModule=" + whereClauseNomenclatureModule
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(company, langNameID, epicorHeaders = None):
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
   params += "langNameID=" + langNameID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetListCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCustom
   Description: This overload of GetList shows all or only the languages with translations.
   OperationID: GetListCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListWithTranslations(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListWithTranslations
   Description: This overload of GetList filters out languages with no translations.
   OperationID: GetListWithTranslations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListWithTranslations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListWithTranslations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNextLanguage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNextLanguage
   Description: Returns next language that has translation record
   OperationID: GetNextLanguage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNextLanguage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNextLanguage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GeneratePseudoLanguage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GeneratePseudoLanguage
   Description: Generate a pseudo language
   OperationID: GeneratePseudoLanguage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GeneratePseudoLanguage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GeneratePseudoLanguage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCultures(epicorHeaders = None):
   """  
   Summary: Invoke method GetCultures
   Description: Gets a list of `System.Globalization.CultureInfo` names (and its English names as Description) from .NET.
Only neutral cultures are returned (not associated to a country).
   OperationID: GetCultures
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCultures_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetFormatCultures(epicorHeaders = None):
   """  
   Summary: Invoke method GetFormatCultures
   Description: Gets a list of `System.Globalization.CultureInfo` names (and its English names as Description) from .NET.
Specific cultures (i.e. associated to a country or region) are returned, including user-defined cultures.
   OperationID: GetFormatCultures
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFormatCultures_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNomenclatureModules(epicorHeaders = None):
   """  
   Summary: Invoke method GetNomenclatureModules
   Description: Gets a list of enabled nomenclature modules in NomenclatureModule table.
   OperationID: GetNomenclatureModules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNomenclatureModules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewLangName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLangName
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLangName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLangName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLangName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.LangNameSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_CultureRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_CultureRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_LangNameListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_LangNameListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_LangNameRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_LangNameRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_NomenclatureModuleRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_NomenclatureModuleRow] = obj["value"]
      pass

class Ice_Tablesets_CultureRow:
   def __init__(self, obj):
      self.Name:str = obj["Name"]
      """  Culture name.  """  
      self.Description:str = obj["Description"]
      """  English Name.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_LangNameListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Language ID  """  
      self.Description:str = obj["Description"]
      """  Language Name Description  """  
      self.ParentLangID:str = obj["ParentLangID"]
      """  Parent Language ID  """  
      self.IsCustomLang:bool = obj["IsCustomLang"]
      """  Custom Languange flag  """  
      self.HelpFileName:str = obj["HelpFileName"]
      """  Name of the help file associated with this language  """  
      self.SpellCheckingDictionary:str = obj["SpellCheckingDictionary"]
      """  Spell checking dictionary fiel  """  
      self.TransVer:int = obj["TransVer"]
      """  This field is used for Language translation version number.  """  
      self.Culture:str = obj["Culture"]
      """  Culture flag  """  
      self.FontName:str = obj["FontName"]
      """  FontName  """  
      self.CharWidthFactor:int = obj["CharWidthFactor"]
      """  CharWidthFactor  """  
      self.FontStyle:str = obj["FontStyle"]
      """  FontStyle  """  
      self.FileVersion:str = obj["FileVersion"]
      """  FileVersion  """  
      self.TranDate:str = obj["TranDate"]
      """  TranDate  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.CompanyVisibility:int = obj["CompanyVisibility"]
      """  CompanyVisibility  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HasTrans:bool = obj["HasTrans"]
      """  HasTrans  """  
      self.ParentDescDescription:str = obj["ParentDescDescription"]
      """  Language Name Description  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_LangNameRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Language ID  """  
      self.Description:str = obj["Description"]
      """  Language Name Description  """  
      self.ParentLangID:str = obj["ParentLangID"]
      """  Parent Language ID  """  
      self.IsCustomLang:bool = obj["IsCustomLang"]
      """  Custom Languange flag  """  
      self.HelpFileName:str = obj["HelpFileName"]
      """  Name of the help file associated with this language  """  
      self.SpellCheckingDictionary:str = obj["SpellCheckingDictionary"]
      """  Spell checking dictionary fiel  """  
      self.TransVer:int = obj["TransVer"]
      """  This field is used for Language translation version number.  """  
      self.Culture:str = obj["Culture"]
      """  Culture flag  """  
      self.FontName:str = obj["FontName"]
      """  FontName  """  
      self.CharWidthFactor:int = obj["CharWidthFactor"]
      """  CharWidthFactor  """  
      self.FontStyle:str = obj["FontStyle"]
      """  FontStyle  """  
      self.FileVersion:str = obj["FileVersion"]
      """  FileVersion  """  
      self.TranDate:str = obj["TranDate"]
      """  TranDate  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.CompanyVisibility:int = obj["CompanyVisibility"]
      """  CompanyVisibility  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HasTrans:bool = obj["HasTrans"]
      """  HasTrans  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.ParentDescDescription:str = obj["ParentDescDescription"]
      """  Parent Language Name Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_NomenclatureModuleRow:
   def __init__(self, obj):
      self.ModuleID:str = obj["ModuleID"]
      """  Module ID.  """  
      self.ModuleName:str = obj["ModuleName"]
      """  Module name.  """  
      self.SysRowID:str = obj["SysRowID"]
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
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.langNameID:str = obj["langNameID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GeneratePseudoLanguage_input:
   """ Required : 
   languageID
   culture
   usePseudoCode
   expansionRatio
   expansionMinChars
   expansionFillChar
   expansionEndingChar
   """  
   def __init__(self, obj):
      self.languageID:str = obj["languageID"]
      """  Which language code to use (typically pse)  """  
      self.culture:str = obj["culture"]
      """  Which culture to apply (by default )  """  
      self.usePseudoCode:bool = obj["usePseudoCode"]
      """  Should the pseudo chars be used to substitute english  """  
      self.expansionRatio:int = obj["expansionRatio"]
      """  The expansio Ration (0.3 - increase by 30%)  """  
      self.expansionMinChars:int = obj["expansionMinChars"]
      """  Expansion Minimum amount of chars (if less than this number). Typically 8  """  
      self.expansionFillChar:str = obj["expansionFillChar"]
      """  The filling char that is expanded by (*)  """  
      self.expansionEndingChar:str = obj["expansionEndingChar"]
      """  The ending char (|)  """  
      pass

class GeneratePseudoLanguage_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   company
   langNameID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.langNameID:str = obj["langNameID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_LangNameTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_LangNameTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_LangNameTableset] = obj["returnObj"]
      pass

class GetCultures_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_LangNameTableset] = obj["returnObj"]
      pass

class GetFormatCultures_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_LangNameTableset] = obj["returnObj"]
      pass

class GetListCustom_input:
   """ Required : 
   whereClause
   installed
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The criteria  """  
      self.installed:bool = obj["installed"]
      """  Show only Installed Languages  """  
      self.pageSize:int = obj["pageSize"]
      """  Size of a page  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page  """  
      pass

class GetListCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_LangNameListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListWithTranslations_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The criteria  """  
      self.pageSize:int = obj["pageSize"]
      """  Size of a page  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page  """  
      pass

class GetListWithTranslations_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_LangNameListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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
      self.returnObj:list[Ice_Tablesets_LangNameListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewLangName_input:
   """ Required : 
   ds
   company
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_LangNameTableset] = obj["ds"]
      self.company:str = obj["company"]
      pass

class GetNewLangName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_LangNameTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNextLanguage_input:
   """ Required : 
   languageID
   """  
   def __init__(self, obj):
      self.languageID:str = obj["languageID"]
      """  Language ID  """  
      pass

class GetNextLanguage_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if found a language  """  
      pass

   def parameters(self, obj):
      self.nextLanguage:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetNomenclatureModules_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_LangNameTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseLangName
   whereClauseCulture
   whereClauseNomenclatureModule
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseLangName:str = obj["whereClauseLangName"]
      self.whereClauseCulture:str = obj["whereClauseCulture"]
      self.whereClauseNomenclatureModule:str = obj["whereClauseNomenclatureModule"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_LangNameTableset] = obj["returnObj"]
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

class Ice_Tablesets_CultureRow:
   def __init__(self, obj):
      self.Name:str = obj["Name"]
      """  Culture name.  """  
      self.Description:str = obj["Description"]
      """  English Name.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_LangNameListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Language ID  """  
      self.Description:str = obj["Description"]
      """  Language Name Description  """  
      self.ParentLangID:str = obj["ParentLangID"]
      """  Parent Language ID  """  
      self.IsCustomLang:bool = obj["IsCustomLang"]
      """  Custom Languange flag  """  
      self.HelpFileName:str = obj["HelpFileName"]
      """  Name of the help file associated with this language  """  
      self.SpellCheckingDictionary:str = obj["SpellCheckingDictionary"]
      """  Spell checking dictionary fiel  """  
      self.TransVer:int = obj["TransVer"]
      """  This field is used for Language translation version number.  """  
      self.Culture:str = obj["Culture"]
      """  Culture flag  """  
      self.FontName:str = obj["FontName"]
      """  FontName  """  
      self.CharWidthFactor:int = obj["CharWidthFactor"]
      """  CharWidthFactor  """  
      self.FontStyle:str = obj["FontStyle"]
      """  FontStyle  """  
      self.FileVersion:str = obj["FileVersion"]
      """  FileVersion  """  
      self.TranDate:str = obj["TranDate"]
      """  TranDate  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.CompanyVisibility:int = obj["CompanyVisibility"]
      """  CompanyVisibility  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HasTrans:bool = obj["HasTrans"]
      """  HasTrans  """  
      self.ParentDescDescription:str = obj["ParentDescDescription"]
      """  Language Name Description  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_LangNameListTableset:
   def __init__(self, obj):
      self.LangNameList:list[Ice_Tablesets_LangNameListRow] = obj["LangNameList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_LangNameRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Language ID  """  
      self.Description:str = obj["Description"]
      """  Language Name Description  """  
      self.ParentLangID:str = obj["ParentLangID"]
      """  Parent Language ID  """  
      self.IsCustomLang:bool = obj["IsCustomLang"]
      """  Custom Languange flag  """  
      self.HelpFileName:str = obj["HelpFileName"]
      """  Name of the help file associated with this language  """  
      self.SpellCheckingDictionary:str = obj["SpellCheckingDictionary"]
      """  Spell checking dictionary fiel  """  
      self.TransVer:int = obj["TransVer"]
      """  This field is used for Language translation version number.  """  
      self.Culture:str = obj["Culture"]
      """  Culture flag  """  
      self.FontName:str = obj["FontName"]
      """  FontName  """  
      self.CharWidthFactor:int = obj["CharWidthFactor"]
      """  CharWidthFactor  """  
      self.FontStyle:str = obj["FontStyle"]
      """  FontStyle  """  
      self.FileVersion:str = obj["FileVersion"]
      """  FileVersion  """  
      self.TranDate:str = obj["TranDate"]
      """  TranDate  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.CompanyVisibility:int = obj["CompanyVisibility"]
      """  CompanyVisibility  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HasTrans:bool = obj["HasTrans"]
      """  HasTrans  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.ParentDescDescription:str = obj["ParentDescDescription"]
      """  Parent Language Name Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_LangNameTableset:
   def __init__(self, obj):
      self.LangName:list[Ice_Tablesets_LangNameRow] = obj["LangName"]
      self.Culture:list[Ice_Tablesets_CultureRow] = obj["Culture"]
      self.NomenclatureModule:list[Ice_Tablesets_NomenclatureModuleRow] = obj["NomenclatureModule"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_NomenclatureModuleRow:
   def __init__(self, obj):
      self.ModuleID:str = obj["ModuleID"]
      """  Module ID.  """  
      self.ModuleName:str = obj["ModuleName"]
      """  Module name.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UpdExtLangNameTableset:
   def __init__(self, obj):
      self.LangName:list[Ice_Tablesets_LangNameRow] = obj["LangName"]
      self.Culture:list[Ice_Tablesets_CultureRow] = obj["Culture"]
      self.NomenclatureModule:list[Ice_Tablesets_NomenclatureModuleRow] = obj["NomenclatureModule"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtLangNameTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtLangNameTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_LangNameTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_LangNameTableset] = obj["ds"]
      pass

      """  output parameters  """  

