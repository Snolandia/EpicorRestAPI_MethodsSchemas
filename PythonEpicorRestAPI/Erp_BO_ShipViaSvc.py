import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ShipViaSvc
# Description: Ship Via business object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ShipVias(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShipVias items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipVias
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipViaRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/ShipVias",headers=creds) as resp:
           return await resp.json()

async def post_ShipVias(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipVias
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipViaRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipViaRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/ShipVias", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShipVias_Company_ShipViaCode(Company, ShipViaCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipVia item
   Description: Calls GetByID to retrieve the ShipVia item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipVia
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipViaCode: Desc: ShipViaCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipViaRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/ShipVias(" + Company + "," + ShipViaCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShipVias_Company_ShipViaCode(Company, ShipViaCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShipVia for the service
   Description: Calls UpdateExt to update ShipVia. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipVia
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipViaCode: Desc: ShipViaCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipViaRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/ShipVias(" + Company + "," + ShipViaCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShipVias_Company_ShipViaCode(Company, ShipViaCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShipVia item
   Description: Call UpdateExt to delete ShipVia item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipVia
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipViaCode: Desc: ShipViaCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/ShipVias(" + Company + "," + ShipViaCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipVias_Company_ShipViaCode_LangDescs(Company, ShipViaCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LangDescs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LangDescs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipViaCode: Desc: ShipViaCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LangDescRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/ShipVias(" + Company + "," + ShipViaCode + ")/LangDescs",headers=creds) as resp:
           return await resp.json()

async def get_ShipVias_Company_ShipViaCode_LangDescs_Company_TableName_Key1_Key2_Key3_LangNameID(Company, ShipViaCode, TableName, Key1, Key2, Key3, LangNameID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LangDesc item
   Description: Calls GetByID to retrieve the LangDesc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LangDesc1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipViaCode: Desc: ShipViaCode   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param LangNameID: Desc: LangNameID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LangDescRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/ShipVias(" + Company + "," + ShipViaCode + ")/LangDescs(" + Company + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + LangNameID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipVias_Company_ShipViaCode_ShipViaTrailers(Company, ShipViaCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ShipViaTrailers items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipViaTrailers1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipViaCode: Desc: ShipViaCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipViaTrailerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/ShipVias(" + Company + "," + ShipViaCode + ")/ShipViaTrailers",headers=creds) as resp:
           return await resp.json()

async def get_ShipVias_Company_ShipViaCode_ShipViaTrailers_Company_ShipViaCode_LicensePlate(Company, ShipViaCode, LicensePlate, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipViaTrailer item
   Description: Calls GetByID to retrieve the ShipViaTrailer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipViaTrailer1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipViaCode: Desc: ShipViaCode   Required: True   Allow empty value : True
      :param LicensePlate: Desc: LicensePlate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipViaTrailerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/ShipVias(" + Company + "," + ShipViaCode + ")/ShipViaTrailers(" + Company + "," + ShipViaCode + "," + LicensePlate + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipVias_Company_ShipViaCode_ShipViaAttches(Company, ShipViaCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ShipViaAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipViaAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipViaCode: Desc: ShipViaCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipViaAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/ShipVias(" + Company + "," + ShipViaCode + ")/ShipViaAttches",headers=creds) as resp:
           return await resp.json()

async def get_ShipVias_Company_ShipViaCode_ShipViaAttches_Company_ShipViaCode_DrawingSeq(Company, ShipViaCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipViaAttch item
   Description: Calls GetByID to retrieve the ShipViaAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipViaAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipViaCode: Desc: ShipViaCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipViaAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/ShipVias(" + Company + "," + ShipViaCode + ")/ShipViaAttches(" + Company + "," + ShipViaCode + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LangDescs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LangDescs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LangDescs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LangDescRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/LangDescs",headers=creds) as resp:
           return await resp.json()

async def post_LangDescs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LangDescs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LangDescRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LangDescRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/LangDescs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LangDescs_Company_TableName_Key1_Key2_Key3_LangNameID(Company, TableName, Key1, Key2, Key3, LangNameID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LangDesc item
   Description: Calls GetByID to retrieve the LangDesc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LangDesc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param LangNameID: Desc: LangNameID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LangDescRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/LangDescs(" + Company + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + LangNameID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LangDescs_Company_TableName_Key1_Key2_Key3_LangNameID(Company, TableName, Key1, Key2, Key3, LangNameID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LangDesc for the service
   Description: Calls UpdateExt to update LangDesc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LangDesc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param LangNameID: Desc: LangNameID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LangDescRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/LangDescs(" + Company + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + LangNameID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LangDescs_Company_TableName_Key1_Key2_Key3_LangNameID(Company, TableName, Key1, Key2, Key3, LangNameID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LangDesc item
   Description: Call UpdateExt to delete LangDesc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LangDesc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/LangDescs(" + Company + "," + TableName + "," + Key1 + "," + Key2 + "," + Key3 + "," + LangNameID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipViaTrailers(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShipViaTrailers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipViaTrailers
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipViaTrailerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/ShipViaTrailers",headers=creds) as resp:
           return await resp.json()

async def post_ShipViaTrailers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipViaTrailers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipViaTrailerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipViaTrailerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/ShipViaTrailers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShipViaTrailers_Company_ShipViaCode_LicensePlate(Company, ShipViaCode, LicensePlate, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipViaTrailer item
   Description: Calls GetByID to retrieve the ShipViaTrailer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipViaTrailer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipViaCode: Desc: ShipViaCode   Required: True   Allow empty value : True
      :param LicensePlate: Desc: LicensePlate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipViaTrailerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/ShipViaTrailers(" + Company + "," + ShipViaCode + "," + LicensePlate + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShipViaTrailers_Company_ShipViaCode_LicensePlate(Company, ShipViaCode, LicensePlate, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShipViaTrailer for the service
   Description: Calls UpdateExt to update ShipViaTrailer. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipViaTrailer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipViaCode: Desc: ShipViaCode   Required: True   Allow empty value : True
      :param LicensePlate: Desc: LicensePlate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipViaTrailerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/ShipViaTrailers(" + Company + "," + ShipViaCode + "," + LicensePlate + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShipViaTrailers_Company_ShipViaCode_LicensePlate(Company, ShipViaCode, LicensePlate, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShipViaTrailer item
   Description: Call UpdateExt to delete ShipViaTrailer item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipViaTrailer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipViaCode: Desc: ShipViaCode   Required: True   Allow empty value : True
      :param LicensePlate: Desc: LicensePlate   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/ShipViaTrailers(" + Company + "," + ShipViaCode + "," + LicensePlate + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipViaAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShipViaAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipViaAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipViaAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/ShipViaAttches",headers=creds) as resp:
           return await resp.json()

async def post_ShipViaAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipViaAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipViaAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipViaAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/ShipViaAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShipViaAttches_Company_ShipViaCode_DrawingSeq(Company, ShipViaCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipViaAttch item
   Description: Calls GetByID to retrieve the ShipViaAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipViaAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipViaCode: Desc: ShipViaCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipViaAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/ShipViaAttches(" + Company + "," + ShipViaCode + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShipViaAttches_Company_ShipViaCode_DrawingSeq(Company, ShipViaCode, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShipViaAttch for the service
   Description: Calls UpdateExt to update ShipViaAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipViaAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipViaCode: Desc: ShipViaCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipViaAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/ShipViaAttches(" + Company + "," + ShipViaCode + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShipViaAttches_Company_ShipViaCode_DrawingSeq(Company, ShipViaCode, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShipViaAttch item
   Description: Call UpdateExt to delete ShipViaAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipViaAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipViaCode: Desc: ShipViaCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/ShipViaAttches(" + Company + "," + ShipViaCode + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipViaListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseShipVia, whereClauseShipViaAttch, whereClauseLangDesc, whereClauseShipViaTrailer, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseShipVia=" + whereClauseShipVia
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseShipViaAttch=" + whereClauseShipViaAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLangDesc=" + whereClauseLangDesc
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseShipViaTrailer=" + whereClauseShipViaTrailer
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(shipViaCode, epicorHeaders = None):
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
   params += "shipViaCode=" + shipViaCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCarrier(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCarrier
   OperationID: OnChangeCarrier
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCarrier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCarrier_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewShipVia(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShipVia
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipVia
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipVia_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipVia_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewShipViaAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShipViaAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipViaAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipViaAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipViaAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLangDesc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLangDesc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLangDesc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLangDesc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLangDesc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewShipViaTrailer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShipViaTrailer
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipViaTrailer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipViaTrailer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipViaTrailer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ShipViaSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LangDescRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LangDescRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipViaAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipViaAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipViaListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipViaListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipViaRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipViaRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipViaTrailerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipViaTrailerRow] = obj["value"]
      pass

class Erp_Tablesets_LangDescRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TableName:str = obj["TableName"]
      """  Name of table that this data is related  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Language ID  """  
      self.Key1:str = obj["Key1"]
      """  Contains values that represent the key1 to the foreign record that this record is related.  """  
      self.Key2:str = obj["Key2"]
      """  key2  of  the foreign record  """  
      self.Key3:str = obj["Key3"]
      """  key3 of the foreign record  """  
      self.Description:str = obj["Description"]
      """  Language Description  """  
      self.GlobalLangDesc:bool = obj["GlobalLangDesc"]
      """  Marks this LangDesc as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipViaAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ShipViaCode:str = obj["ShipViaCode"]
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

class Erp_Tablesets_ShipViaListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Descriptive code assigned by user which uniquely identifies a shipping method (carrier) master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Description:str = obj["Description"]
      """  Full description for the shipping company (carrier).  """  
      self.IStatCode:str = obj["IStatCode"]
      """  Intrastat code for this method of transportation.  """  
      self.RequiresBorder:bool = obj["RequiresBorder"]
      """  Indicates if Intrastat border crossing point is required.  """  
      self.TrackingURL:str = obj["TrackingURL"]
      """  The URL of the tracking website for this ShipVia record. This site will be used when tracking shipments from the shipment tracker.  """  
      self.TrackingNumPlaceHolder:str = obj["TrackingNumPlaceHolder"]
      """  String that is used as a place holder for the package tracking number.  This string is replaced with the actual package tracking number (Packing Slip Log number) prior to activating the link.  """  
      self.WebDesc:str = obj["WebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.Carrier:str = obj["Carrier"]
      """  The unique identifier for the carrier  """  
      self.SCAC:str = obj["SCAC"]
      """  The Standard Carrier Alpha Code used to identify the carrier.  """  
      self.GlobalShipVia:bool = obj["GlobalShipVia"]
      """  Marks this ShipVia as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SystemDefault:bool = obj["SystemDefault"]
      """  System Default Ship Via  """  
      self.HasIntl:bool = obj["HasIntl"]
      """  Indicates if the company has Internalization ... used to disable/enable BorderCorssing,  Interstat fields  """  
      self.EnableBorderCrossing:bool = obj["EnableBorderCrossing"]
      """  Indicates if the company has the EnableHarbour field (Border Crossing) set true... used to enable/disable BorderCrossing checkbox in ShipViaEntry  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipViaRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Descriptive code assigned by user which uniquely identifies a shipping method (carrier) master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Description:str = obj["Description"]
      """  Full description for the shipping company (carrier).  """  
      self.IStatCode:str = obj["IStatCode"]
      """  Intrastat code for this method of transportation.  """  
      self.RequiresBorder:bool = obj["RequiresBorder"]
      """  Indicates if Intrastat border crossing point is required.  """  
      self.TrackingURL:str = obj["TrackingURL"]
      """  The URL of the tracking website for this ShipVia record. This site will be used when tracking shipments from the shipment tracker.  """  
      self.TrackingNumPlaceHolder:str = obj["TrackingNumPlaceHolder"]
      """  String that is used as a place holder for the package tracking number.  This string is replaced with the actual package tracking number (Packing Slip Log number) prior to activating the link.  """  
      self.WebDesc:str = obj["WebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.Carrier:str = obj["Carrier"]
      """  The unique identifier for the carrier  """  
      self.SCAC:str = obj["SCAC"]
      """  The Standard Carrier Alpha Code used to identify the carrier.  """  
      self.GlobalShipVia:bool = obj["GlobalShipVia"]
      """  Marks this ShipVia as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.WIApplication:str = obj["WIApplication"]
      """  WIApplication  """  
      self.WebShipVia:str = obj["WebShipVia"]
      """  WebShipVia  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGAFIPResponsibilityCode:str = obj["AGAFIPResponsibilityCode"]
      """  AGAFIPResponsibilityCode  """  
      self.AGIDDocTypeCode:str = obj["AGIDDocTypeCode"]
      """  AGIDDocTypeCode  """  
      self.AGIDDocumentNumber:str = obj["AGIDDocumentNumber"]
      """  AGIDDocumentNumber  """  
      self.AGApartment:str = obj["AGApartment"]
      """  AGApartment  """  
      self.AGExtraStreetNumber:str = obj["AGExtraStreetNumber"]
      """  AGExtraStreetNumber  """  
      self.AGFloor:str = obj["AGFloor"]
      """  AGFloor  """  
      self.AGLocationCode:str = obj["AGLocationCode"]
      """  AGLocationCode  """  
      self.AGNeighborhood:str = obj["AGNeighborhood"]
      """  AGNeighborhood  """  
      self.AGProvinceCode:str = obj["AGProvinceCode"]
      """  AGProvinceCode  """  
      self.AGStreet:str = obj["AGStreet"]
      """  AGStreet  """  
      self.AGStreetNumber:str = obj["AGStreetNumber"]
      """  AGStreetNumber  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the record is inactive.  """  
      self.MXPermitType:str = obj["MXPermitType"]
      """  Permit Type  """  
      self.MXPermitNum:str = obj["MXPermitNum"]
      """  Permit Number  """  
      self.VehicleLicensePlate:str = obj["VehicleLicensePlate"]
      """  Vehicle License Plate  """  
      self.VehicleType:str = obj["VehicleType"]
      """  Vehicle Type  """  
      self.VehicleYear:int = obj["VehicleYear"]
      """  Vehicle Year  """  
      self.IntraEUTransportMode:str = obj["IntraEUTransportMode"]
      """  The mode of transport refers to the mode of transport within the EU.  """  
      self.ContainerShip:bool = obj["ContainerShip"]
      """  Indicates whether or not there is transport by container.  """  
      self.SystemDefault:bool = obj["SystemDefault"]
      """  System Default Ship Via  """  
      self.EnableBorderCrossing:bool = obj["EnableBorderCrossing"]
      """  Indicates if the company has the EnableHarbour field (Border Crossing) set true... used to enable/disable BorderCrossing checkbox in ShipViaEntry  """  
      self.HasIntl:bool = obj["HasIntl"]
      """  Indicates if the company has Internalization ... used to disable/enable BorderCorssing,  Interstat fields  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipViaTrailerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Ship Via  """  
      self.LicensePlate:str = obj["LicensePlate"]
      """  License Plate for Trailer  """  
      self.Type:str = obj["Type"]
      """  Type of Trailer  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   shipViaCode
   """  
   def __init__(self, obj):
      self.shipViaCode:str = obj["shipViaCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_LangDescRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TableName:str = obj["TableName"]
      """  Name of table that this data is related  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Language ID  """  
      self.Key1:str = obj["Key1"]
      """  Contains values that represent the key1 to the foreign record that this record is related.  """  
      self.Key2:str = obj["Key2"]
      """  key2  of  the foreign record  """  
      self.Key3:str = obj["Key3"]
      """  key3 of the foreign record  """  
      self.Description:str = obj["Description"]
      """  Language Description  """  
      self.GlobalLangDesc:bool = obj["GlobalLangDesc"]
      """  Marks this LangDesc as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipViaAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ShipViaCode:str = obj["ShipViaCode"]
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

class Erp_Tablesets_ShipViaListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Descriptive code assigned by user which uniquely identifies a shipping method (carrier) master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Description:str = obj["Description"]
      """  Full description for the shipping company (carrier).  """  
      self.IStatCode:str = obj["IStatCode"]
      """  Intrastat code for this method of transportation.  """  
      self.RequiresBorder:bool = obj["RequiresBorder"]
      """  Indicates if Intrastat border crossing point is required.  """  
      self.TrackingURL:str = obj["TrackingURL"]
      """  The URL of the tracking website for this ShipVia record. This site will be used when tracking shipments from the shipment tracker.  """  
      self.TrackingNumPlaceHolder:str = obj["TrackingNumPlaceHolder"]
      """  String that is used as a place holder for the package tracking number.  This string is replaced with the actual package tracking number (Packing Slip Log number) prior to activating the link.  """  
      self.WebDesc:str = obj["WebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.Carrier:str = obj["Carrier"]
      """  The unique identifier for the carrier  """  
      self.SCAC:str = obj["SCAC"]
      """  The Standard Carrier Alpha Code used to identify the carrier.  """  
      self.GlobalShipVia:bool = obj["GlobalShipVia"]
      """  Marks this ShipVia as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SystemDefault:bool = obj["SystemDefault"]
      """  System Default Ship Via  """  
      self.HasIntl:bool = obj["HasIntl"]
      """  Indicates if the company has Internalization ... used to disable/enable BorderCorssing,  Interstat fields  """  
      self.EnableBorderCrossing:bool = obj["EnableBorderCrossing"]
      """  Indicates if the company has the EnableHarbour field (Border Crossing) set true... used to enable/disable BorderCrossing checkbox in ShipViaEntry  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipViaListTableset:
   def __init__(self, obj):
      self.ShipViaList:list[Erp_Tablesets_ShipViaListRow] = obj["ShipViaList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ShipViaRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Descriptive code assigned by user which uniquely identifies a shipping method (carrier) master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Description:str = obj["Description"]
      """  Full description for the shipping company (carrier).  """  
      self.IStatCode:str = obj["IStatCode"]
      """  Intrastat code for this method of transportation.  """  
      self.RequiresBorder:bool = obj["RequiresBorder"]
      """  Indicates if Intrastat border crossing point is required.  """  
      self.TrackingURL:str = obj["TrackingURL"]
      """  The URL of the tracking website for this ShipVia record. This site will be used when tracking shipments from the shipment tracker.  """  
      self.TrackingNumPlaceHolder:str = obj["TrackingNumPlaceHolder"]
      """  String that is used as a place holder for the package tracking number.  This string is replaced with the actual package tracking number (Packing Slip Log number) prior to activating the link.  """  
      self.WebDesc:str = obj["WebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.Carrier:str = obj["Carrier"]
      """  The unique identifier for the carrier  """  
      self.SCAC:str = obj["SCAC"]
      """  The Standard Carrier Alpha Code used to identify the carrier.  """  
      self.GlobalShipVia:bool = obj["GlobalShipVia"]
      """  Marks this ShipVia as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.WIApplication:str = obj["WIApplication"]
      """  WIApplication  """  
      self.WebShipVia:str = obj["WebShipVia"]
      """  WebShipVia  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGAFIPResponsibilityCode:str = obj["AGAFIPResponsibilityCode"]
      """  AGAFIPResponsibilityCode  """  
      self.AGIDDocTypeCode:str = obj["AGIDDocTypeCode"]
      """  AGIDDocTypeCode  """  
      self.AGIDDocumentNumber:str = obj["AGIDDocumentNumber"]
      """  AGIDDocumentNumber  """  
      self.AGApartment:str = obj["AGApartment"]
      """  AGApartment  """  
      self.AGExtraStreetNumber:str = obj["AGExtraStreetNumber"]
      """  AGExtraStreetNumber  """  
      self.AGFloor:str = obj["AGFloor"]
      """  AGFloor  """  
      self.AGLocationCode:str = obj["AGLocationCode"]
      """  AGLocationCode  """  
      self.AGNeighborhood:str = obj["AGNeighborhood"]
      """  AGNeighborhood  """  
      self.AGProvinceCode:str = obj["AGProvinceCode"]
      """  AGProvinceCode  """  
      self.AGStreet:str = obj["AGStreet"]
      """  AGStreet  """  
      self.AGStreetNumber:str = obj["AGStreetNumber"]
      """  AGStreetNumber  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the record is inactive.  """  
      self.MXPermitType:str = obj["MXPermitType"]
      """  Permit Type  """  
      self.MXPermitNum:str = obj["MXPermitNum"]
      """  Permit Number  """  
      self.VehicleLicensePlate:str = obj["VehicleLicensePlate"]
      """  Vehicle License Plate  """  
      self.VehicleType:str = obj["VehicleType"]
      """  Vehicle Type  """  
      self.VehicleYear:int = obj["VehicleYear"]
      """  Vehicle Year  """  
      self.IntraEUTransportMode:str = obj["IntraEUTransportMode"]
      """  The mode of transport refers to the mode of transport within the EU.  """  
      self.ContainerShip:bool = obj["ContainerShip"]
      """  Indicates whether or not there is transport by container.  """  
      self.SystemDefault:bool = obj["SystemDefault"]
      """  System Default Ship Via  """  
      self.EnableBorderCrossing:bool = obj["EnableBorderCrossing"]
      """  Indicates if the company has the EnableHarbour field (Border Crossing) set true... used to enable/disable BorderCrossing checkbox in ShipViaEntry  """  
      self.HasIntl:bool = obj["HasIntl"]
      """  Indicates if the company has Internalization ... used to disable/enable BorderCorssing,  Interstat fields  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipViaTableset:
   def __init__(self, obj):
      self.ShipVia:list[Erp_Tablesets_ShipViaRow] = obj["ShipVia"]
      self.ShipViaAttch:list[Erp_Tablesets_ShipViaAttchRow] = obj["ShipViaAttch"]
      self.LangDesc:list[Erp_Tablesets_LangDescRow] = obj["LangDesc"]
      self.ShipViaTrailer:list[Erp_Tablesets_ShipViaTrailerRow] = obj["ShipViaTrailer"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ShipViaTrailerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Ship Via  """  
      self.LicensePlate:str = obj["LicensePlate"]
      """  License Plate for Trailer  """  
      self.Type:str = obj["Type"]
      """  Type of Trailer  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtShipViaTableset:
   def __init__(self, obj):
      self.ShipVia:list[Erp_Tablesets_ShipViaRow] = obj["ShipVia"]
      self.ShipViaAttch:list[Erp_Tablesets_ShipViaAttchRow] = obj["ShipViaAttch"]
      self.LangDesc:list[Erp_Tablesets_LangDescRow] = obj["LangDesc"]
      self.ShipViaTrailer:list[Erp_Tablesets_ShipViaTrailerRow] = obj["ShipViaTrailer"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   shipViaCode
   """  
   def __init__(self, obj):
      self.shipViaCode:str = obj["shipViaCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ShipViaTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ShipViaTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ShipViaTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ShipViaListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewLangDesc_input:
   """ Required : 
   ds
   tableName
   key1
   key2
   key3
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ShipViaTableset] = obj["ds"]
      self.tableName:str = obj["tableName"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      pass

class GetNewLangDesc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ShipViaTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewShipViaAttch_input:
   """ Required : 
   ds
   shipViaCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ShipViaTableset] = obj["ds"]
      self.shipViaCode:str = obj["shipViaCode"]
      pass

class GetNewShipViaAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ShipViaTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewShipViaTrailer_input:
   """ Required : 
   ds
   shipViaCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ShipViaTableset] = obj["ds"]
      self.shipViaCode:str = obj["shipViaCode"]
      pass

class GetNewShipViaTrailer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ShipViaTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewShipVia_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ShipViaTableset] = obj["ds"]
      pass

class GetNewShipVia_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ShipViaTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseShipVia
   whereClauseShipViaAttch
   whereClauseLangDesc
   whereClauseShipViaTrailer
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseShipVia:str = obj["whereClauseShipVia"]
      self.whereClauseShipViaAttch:str = obj["whereClauseShipViaAttch"]
      self.whereClauseLangDesc:str = obj["whereClauseLangDesc"]
      self.whereClauseShipViaTrailer:str = obj["whereClauseShipViaTrailer"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ShipViaTableset] = obj["returnObj"]
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

class OnChangeCarrier_input:
   """ Required : 
   ipCarrier
   ds
   """  
   def __init__(self, obj):
      self.ipCarrier:str = obj["ipCarrier"]
      self.ds:list[Erp_Tablesets_ShipViaTableset] = obj["ds"]
      pass

class OnChangeCarrier_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ShipViaTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtShipViaTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtShipViaTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ShipViaTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ShipViaTableset] = obj["ds"]
      pass

      """  output parameters  """  

