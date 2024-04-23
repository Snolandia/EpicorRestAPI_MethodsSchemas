import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CurrencySvc
# Description: Currency Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Currencies(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Currencies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Currencies
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrencyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/Currencies",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/Currencies", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Currencies_Company_CurrencyCode(Company, CurrencyCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Currency item
   Description: Calls GetByID to retrieve the Currency item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Currency
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CurrencyCode: Desc: CurrencyCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/Currencies(" + Company + "," + CurrencyCode + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/Currencies(" + Company + "," + CurrencyCode + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/Currencies(" + Company + "," + CurrencyCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_Currencies_Company_CurrencyCode_EntityGLCs(Company, CurrencyCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CurrencyCode: Desc: CurrencyCode   Required: True   Allow empty value : True
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/Currencies(" + Company + "," + CurrencyCode + ")/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def get_Currencies_Company_CurrencyCode_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, CurrencyCode, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CurrencyCode: Desc: CurrencyCode   Required: True   Allow empty value : True
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/Currencies(" + Company + "," + CurrencyCode + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_Currencies_Company_CurrencyCode_CurrencyAttches(Company, CurrencyCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CurrencyAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CurrencyAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CurrencyCode: Desc: CurrencyCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrencyAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/Currencies(" + Company + "," + CurrencyCode + ")/CurrencyAttches",headers=creds) as resp:
           return await resp.json()

async def get_Currencies_Company_CurrencyCode_CurrencyAttches_Company_CurrencyCode_DrawingSeq(Company, CurrencyCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CurrencyAttch item
   Description: Calls GetByID to retrieve the CurrencyAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrencyAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CurrencyCode: Desc: CurrencyCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CurrencyAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/Currencies(" + Company + "," + CurrencyCode + ")/CurrencyAttches(" + Company + "," + CurrencyCode + "," + DrawingSeq + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/EntityGLCs",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/EntityGLCs", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_CurrencyAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CurrencyAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CurrencyAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrencyAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/CurrencyAttches",headers=creds) as resp:
           return await resp.json()

async def post_CurrencyAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CurrencyAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CurrencyAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CurrencyAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/CurrencyAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CurrencyAttches_Company_CurrencyCode_DrawingSeq(Company, CurrencyCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CurrencyAttch item
   Description: Calls GetByID to retrieve the CurrencyAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrencyAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CurrencyCode: Desc: CurrencyCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CurrencyAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/CurrencyAttches(" + Company + "," + CurrencyCode + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CurrencyAttches_Company_CurrencyCode_DrawingSeq(Company, CurrencyCode, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CurrencyAttch for the service
   Description: Calls UpdateExt to update CurrencyAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CurrencyAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CurrencyCode: Desc: CurrencyCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CurrencyAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/CurrencyAttches(" + Company + "," + CurrencyCode + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CurrencyAttches_Company_CurrencyCode_DrawingSeq(Company, CurrencyCode, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CurrencyAttch item
   Description: Call UpdateExt to delete CurrencyAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CurrencyAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CurrencyCode: Desc: CurrencyCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/CurrencyAttches(" + Company + "," + CurrencyCode + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrencyListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCurrency, whereClauseCurrencyAttch, whereClauseEntityGLC, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCurrency=" + whereClauseCurrency
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCurrencyAttch=" + whereClauseCurrencyAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(currencyCode, epicorHeaders = None):
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
   params += "currencyCode=" + currencyCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ConvertCurrAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConvertCurrAmt
   Description: This method will take the source currency, date, rate group and return the
amount in the target currency
   OperationID: ConvertCurrAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvertCurrAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertCurrAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrencyBase(epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrencyBase
   Description: This method returns the Base CurrencyCode
   OperationID: GetCurrencyBase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyBase_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetCurrencyForLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrencyForLink
   Description: This returns the Currency dataset for linking.
   OperationID: GetCurrencyForLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrencyForLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyForLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InvokeLinkSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InvokeLinkSearch
   Description: This method returns the delimited list of glbCurrCode values
   OperationID: InvokeLinkSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InvokeLinkSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InvokeLinkSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGlbCurrencyList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGlbCurrencyList
   Description: This method returns the GlbCurrency dataset based on a delimited list of
GlbCurrCode values passed in.
   OperationID: GetGlbCurrencyList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGlbCurrencyList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGlbCurrencyList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReportCurrList(epicorHeaders = None):
   """  
   Summary: Invoke method GetReportCurrList
   Description: This method returns a list of reporting currency positions and the the currencies
that are currently populating each slot
   OperationID: GetReportCurrList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportCurrList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GlbCurrenciesExist(epicorHeaders = None):
   """  
   Summary: Invoke method GlbCurrenciesExist
   Description: This method checks if GlbCurrency records exist or not.  Can be used
to determine if the option to link/unlink customers is available.
   OperationID: GlbCurrenciesExist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GlbCurrenciesExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_LinkGlbCurrency(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LinkGlbCurrency
   Description: This method performs the actual logic behind linking a currency.  It is run after
the PreLinkGlbCurrency method which determines the Currency Code to link to.
If the Currency Code is for a Currency that already exists, the GlbCurrency information is
translated and then copied to the CurrencyDataSet as an update.
If the Currency Code is for a new Currency, the GlbCurrency information is translated and then
copied to the CurrencyDataSet as an Add.  Until the update method is run on Currency record
the Link process is not completed.
   OperationID: LinkGlbCurrency
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LinkGlbCurrency_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LinkGlbCurrency_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LinkGlbCurrency2(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LinkGlbCurrency2
   Description: This method performs the actual logic behind linking a currency.  It is run after
the PreLinkGlbCurrency method which determines the Currency Code to link to.
If the Currency Code is for a Currency that already exists, the GlbCurrency information is
translated and then copied to the CurrencyDataSet as an update.
If the Currency Code is for a new Currency, the GlbCurrency information is translated and then
copied to the CurrencyDataSet as an Add.  Until the update method is run on Currency record
the Link process is not completed.
   OperationID: LinkGlbCurrency2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LinkGlbCurrency2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LinkGlbCurrency2_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreLinkGlbCurrency(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreLinkGlbCurrency
   Description: Linking a GlbCurrency record ties a global record to a new or existing Currency record so
that any changes made to the GlbCurrency record in another company are automatically copied
to any linked Currencies.
This method performs the pre link logic to check of okay to link or get the new currencyid
to create/link to.  Will be run before LinkGlbCurrency which actually creates/updates a
Currency record and will send the modified record back for update.  When the Link "button" is
originally selected, the LinkCurrencyID will be defaulted to the GlbCurrencyId field.  It will then
check to see if this ID is available for Use.  If available for use the system will return a
question asking the user if they want to use this number.  If the answer is no, then the user
either needs to select an existing currency's ID to link to or enter a brand new ID.  You will
run this method until the user answer is yes.  Then the LinkGlbCurrency method is called.
   OperationID: PreLinkGlbCurrency
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreLinkGlbCurrency_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreLinkGlbCurrency_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreLinkGlbCurrencyAuto(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreLinkGlbCurrencyAuto
   Description: This method performs the pre-link validation and logic to link local currency ID automatically when Rate type is linked.
   OperationID: PreLinkGlbCurrencyAuto
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreLinkGlbCurrencyAuto_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreLinkGlbCurrencyAuto_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SkipGlbCurrency(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SkipGlbCurrency
   Description: This method performs the logic behind the skip option for GlbCurrency
Skip - sets the Skipped flag to true.
If the CurrencyCode field is not blank will error out
   OperationID: SkipGlbCurrency
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SkipGlbCurrency_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SkipGlbCurrency_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnlinkGlbCurrency(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnlinkGlbCurrency
   Description: This method performs the logic behind the unlink option for GlbCurrency
Unlink - clears the CurrencyCode and CustId field in GlbCurrency.  Returns the Currency DataSet
   OperationID: UnlinkGlbCurrency
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlinkGlbCurrency_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlinkGlbCurrency_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateMaster(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateMaster
   Description: This method is called instead of the standard Update
   OperationID: UpdateMaster
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_onChangeDecimals(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method onChangeDecimals
   Description: This method is called when General Decimals number is changed.
   OperationID: onChangeDecimals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/onChangeDecimals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/onChangeDecimals_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeProcessorNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeProcessorNum
   Description: This method is called when Credit Card Processor is changed.
   OperationID: OnChangeProcessorNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeProcessorNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeProcessorNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetActiveSessionsList(epicorHeaders = None):
   """  
   Summary: Invoke method GetActiveSessionsList
   Description: Look for currently Actctive Sessions.
   OperationID: GetActiveSessionsList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetActiveSessionsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetRoundRuleList(epicorHeaders = None):
   """  
   Summary: Invoke method GetRoundRuleList
   Description: This method is called for Round Rules list's building.
   OperationID: GetRoundRuleList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRoundRuleList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetLinkOptsList(epicorHeaders = None):
   """  
   Summary: Invoke method GetLinkOptsList
   Description: This method is called for LinkOpts list's building.
   OperationID: GetLinkOptsList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLinkOptsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCurrencyAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCurrencyAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCurrencyAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCurrencyAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCurrencyAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CurrencySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrencyAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CurrencyAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrencyListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CurrencyListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrencyRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CurrencyRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EntityGLCRow] = obj["value"]
      pass

class Erp_Tablesets_CurrencyAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CurrencyCode:str = obj["CurrencyCode"]
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

class Erp_Tablesets_CurrencyListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.CurrDesc:str = obj["CurrDesc"]
      """  Description of the currency  """  
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyID:str = obj["CurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.DecimalsGeneral:int = obj["DecimalsGeneral"]
      """  Number of decimals used for any types of amounts where they entered, printed, displayed, except unit price and unit cost, according to the table zFieldDecimal where ValueType = "G"  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the currency is active  """  
      self.DecimalsPrice:int = obj["DecimalsPrice"]
      """  Number of decimals used for any unit prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "P"  """  
      self.DecimalsCost:int = obj["DecimalsCost"]
      """  Number of decimals used for any cost prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "C"  """  
      self.BaseCurr:bool = obj["BaseCurr"]
      """  Indicates if this is the base currency.  Only one base currency is allowed  """  
      self.ReportCurr:bool = obj["ReportCurr"]
      """  Indicates if this is a reporting currency  """  
      self.ReportCurrPos:int = obj["ReportCurrPos"]
      """  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
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




#########################################################################
# Custom Schemas:
#########################################################################
class ConvertCurrAmt_input:
   """ Required : 
   ipSourceCurrCode
   ipSourceAmt
   ipTargetCurrCode
   ipRateGrpCode
   ipDate
   ipTableName
   ipFieldName
   ipKeyTable
   ipKey1
   ipKey2
   ipKey3
   ipKey4
   ipKey5
   """  
   def __init__(self, obj):
      self.ipSourceCurrCode:str = obj["ipSourceCurrCode"]
      """  Source Currency Code  """  
      self.ipSourceAmt:str = obj["ipSourceAmt"]
      """  Delimited List of Amounts to convert  """  
      self.ipTargetCurrCode:str = obj["ipTargetCurrCode"]
      """  Target Currency Code  """  
      self.ipRateGrpCode:str = obj["ipRateGrpCode"]
      """  Rate Type to get the exchange rate from  """  
      self.ipDate:str = obj["ipDate"]
      """  Date to use to find the exchange rate  """  
      self.ipTableName:str = obj["ipTableName"]
      """  Used to find any rounding rules, no rounding applied if left blank, if not blank must contain the same amount of entries as the ipSourceAmt  """  
      self.ipFieldName:str = obj["ipFieldName"]
      """  Used to find any rounding rules, no rounding applied if left blank, if not blank must contain the same amount of entries as the ipSourceAmt  """  
      self.ipKeyTable:str = obj["ipKeyTable"]
      """  Used to find the exchange rate tied to a specific record  """  
      self.ipKey1:str = obj["ipKey1"]
      """  Used to find a specific record's Exchange Rate along with ipKeyTable  """  
      self.ipKey2:str = obj["ipKey2"]
      """  Used to find a specific record's Exchange Rate along with ipKeyTable  """  
      self.ipKey3:str = obj["ipKey3"]
      """  Used to find a specific record's Exchange Rate along with ipKeyTable  """  
      self.ipKey4:str = obj["ipKey4"]
      """  Used to find a specific record's Exchange Rate along with ipKeyTable  """  
      self.ipKey5:str = obj["ipKey5"]
      """  Used to find a specific record's Exchange Rate along with ipKeyTable  """  
      pass

class ConvertCurrAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opTargetAmt:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   currencyCode
   """  
   def __init__(self, obj):
      self.currencyCode:str = obj["currencyCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CurrencyAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CurrencyCode:str = obj["CurrencyCode"]
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

class Erp_Tablesets_CurrencyListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.CurrDesc:str = obj["CurrDesc"]
      """  Description of the currency  """  
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyID:str = obj["CurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.DecimalsGeneral:int = obj["DecimalsGeneral"]
      """  Number of decimals used for any types of amounts where they entered, printed, displayed, except unit price and unit cost, according to the table zFieldDecimal where ValueType = "G"  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the currency is active  """  
      self.DecimalsPrice:int = obj["DecimalsPrice"]
      """  Number of decimals used for any unit prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "P"  """  
      self.DecimalsCost:int = obj["DecimalsCost"]
      """  Number of decimals used for any cost prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "C"  """  
      self.BaseCurr:bool = obj["BaseCurr"]
      """  Indicates if this is the base currency.  Only one base currency is allowed  """  
      self.ReportCurr:bool = obj["ReportCurr"]
      """  Indicates if this is a reporting currency  """  
      self.ReportCurrPos:int = obj["ReportCurrPos"]
      """  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CurrencyListTableset:
   def __init__(self, obj):
      self.CurrencyList:list[Erp_Tablesets_CurrencyListRow] = obj["CurrencyList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

class Erp_Tablesets_CurrencyTableset:
   def __init__(self, obj):
      self.Currency:list[Erp_Tablesets_CurrencyRow] = obj["Currency"]
      self.CurrencyAttch:list[Erp_Tablesets_CurrencyAttchRow] = obj["CurrencyAttch"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

class Erp_Tablesets_GlbCurrencyRow:
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
      self.UnRealLossDiv:str = obj["UnRealLossDiv"]
      """   The Division component of default Unrealized Loss G/L account for a Currency.  The full G/L account number is made up of UnRealLossDiv, UnRealLossChart and UnRealLossDept.  These individual fields are never directly entered, rather it is entered as part of a field that represents the full G/L account number.  If any one of these three components are entered then it must be valid in the GLAcct.
See the GLSyst record layout for more detail on structure and usage of G/L account numbers.  """  
      self.UnRealLossDept:str = obj["UnRealLossDept"]
      """   Department component of the default Unrealized Loss G/L account for a Currency.
See UnRealLossDiv field description for related info.  """  
      self.UnRealLossChart:str = obj["UnRealLossChart"]
      """   Chart of Account  component for the default Unrealized Loss G/L account for a Currency.
See UnRealLossDiv field description for related info.  """  
      self.CurrName:str = obj["CurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyID:str = obj["CurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the currency is active  """  
      self.MaintRate:bool = obj["MaintRate"]
      """  Can only maintain exchange rates for currencies with this flag checked  """  
      self.BaseCurr:bool = obj["BaseCurr"]
      """  Indicates if this is the base currency.  Only one base currency is allowed  """  
      self.ReportCurr:bool = obj["ReportCurr"]
      """  Indicates if this is a reporting currency  """  
      self.GlobalCurr:bool = obj["GlobalCurr"]
      """  Determines whether or not this currency is shared between more than one company.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this currency record will receive global updates.  """  
      self.ScaleFactor:int = obj["ScaleFactor"]
      """  Display factor for exchange rates  """  
      self.CountryNum:int = obj["CountryNum"]
      """  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  """  
      self.GlbCurrencyCode:str = obj["GlbCurrencyCode"]
      """  Currency Code from Source Company  """  
      self.GlbCurrencyID:str = obj["GlbCurrencyID"]
      """  Currency ID from Source Company  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Source Company  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates that the user has reviewed the record but its not going to be linked currently  """  
      self.ReportCurrPos:int = obj["ReportCurrPos"]
      """  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  """  
      self.DecimalsCost:int = obj["DecimalsCost"]
      self.DecimalsGeneral:int = obj["DecimalsGeneral"]
      self.DecimalsPrice:int = obj["DecimalsPrice"]
      self.RoundMltpExtPrice:int = obj["RoundMltpExtPrice"]
      self.RoundMltpExtTax:int = obj["RoundMltpExtTax"]
      self.RoundMltpTotalAmt:int = obj["RoundMltpTotalAmt"]
      self.RoundMltpTotalTax:int = obj["RoundMltpTotalTax"]
      self.RoundMltpUnitPrice:int = obj["RoundMltpUnitPrice"]
      self.RoundMltpUnitTax:int = obj["RoundMltpUnitTax"]
      self.RoundRuleExtPrice:int = obj["RoundRuleExtPrice"]
      self.RoundRuleExtTax:int = obj["RoundRuleExtTax"]
      self.RoundRuleTotalAmt:int = obj["RoundRuleTotalAmt"]
      self.RoundRuleTotalTax:int = obj["RoundRuleTotalTax"]
      self.RoundRuleUnitPrice:int = obj["RoundRuleUnitPrice"]
      self.RoundRuleUnitTax:int = obj["RoundRuleUnitTax"]
      self.RoundTolerance:int = obj["RoundTolerance"]
      self.ISONumber:int = obj["ISONumber"]
      self.StoreID:str = obj["StoreID"]
      self.RoundMltpAnnualCharge:int = obj["RoundMltpAnnualCharge"]
      self.RoundMltpPeriodCharge:int = obj["RoundMltpPeriodCharge"]
      self.RoundRuleAnnualCharge:int = obj["RoundRuleAnnualCharge"]
      self.RoundRulePeriodCharge:int = obj["RoundRulePeriodCharge"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGAFIPCode:str = obj["AGAFIPCode"]
      """  AGAFIPCode  """  
      self.ISOCurrCode:str = obj["ISOCurrCode"]
      """  ISOCurrCode  """  
      self.ProcessorNum:int = obj["ProcessorNum"]
      """  ProcessorNum  """  
      self.LinkCurrencyCode:str = obj["LinkCurrencyCode"]
      """  Currency.CurrencyCode to link to (new or existing)  """  
      self.LinkCurrencyID:str = obj["LinkCurrencyID"]
      """  Currency.CurrencyID to link to (new or existing)  """  
      self.LocalDesc:str = obj["LocalDesc"]
      """  Description of the local Currency  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbCurrencyTableset:
   def __init__(self, obj):
      self.GlbCurrency:list[Erp_Tablesets_GlbCurrencyRow] = obj["GlbCurrency"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ReportCurrListRow:
   def __init__(self, obj):
      self.CurrencyID:str = obj["CurrencyID"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrDesc:str = obj["CurrDesc"]
      self.ReportCurrPos:int = obj["ReportCurrPos"]
      self.ReportSlot:str = obj["ReportSlot"]
      self.Company:str = obj["Company"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.Include:bool = obj["Include"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReportCurrListTableset:
   def __init__(self, obj):
      self.ReportCurrList:list[Erp_Tablesets_ReportCurrListRow] = obj["ReportCurrList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCurrencyTableset:
   def __init__(self, obj):
      self.Currency:list[Erp_Tablesets_CurrencyRow] = obj["Currency"]
      self.CurrencyAttch:list[Erp_Tablesets_CurrencyAttchRow] = obj["CurrencyAttch"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetActiveSessionsList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.SessionList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   currencyCode
   """  
   def __init__(self, obj):
      self.currencyCode:str = obj["currencyCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CurrencyTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CurrencyTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CurrencyTableset] = obj["returnObj"]
      pass

class GetCurrencyBase_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCurrencyBase:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetCurrencyForLink_input:
   """ Required : 
   currencyCode
   """  
   def __init__(self, obj):
      self.currencyCode:str = obj["currencyCode"]
      """  Global currency code field on the Glbcurrency record to link  """  
      pass

class GetCurrencyForLink_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CurrencyTableset] = obj["returnObj"]
      pass

class GetGlbCurrencyList_input:
   """ Required : 
   glbCurrCodeList
   """  
   def __init__(self, obj):
      self.glbCurrCodeList:str = obj["glbCurrCodeList"]
      """  Delimited list of glbCurrCode values  """  
      pass

class GetGlbCurrencyList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GlbCurrencyTableset] = obj["returnObj"]
      pass

class GetLinkOptsList_output:
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
      self.returnObj:list[Erp_Tablesets_CurrencyListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCurrencyAttch_input:
   """ Required : 
   ds
   currencyCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyTableset] = obj["ds"]
      self.currencyCode:str = obj["currencyCode"]
      pass

class GetNewCurrencyAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCurrency_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyTableset] = obj["ds"]
      pass

class GetNewCurrency_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEntityGLC_input:
   """ Required : 
   ds
   relatedToFile
   key1
   key2
   key3
   key4
   key5
   key6
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_CurrencyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetReportCurrList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReportCurrListTableset] = obj["returnObj"]
      pass

class GetRoundRuleList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseCurrency
   whereClauseCurrencyAttch
   whereClauseEntityGLC
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCurrency:str = obj["whereClauseCurrency"]
      self.whereClauseCurrencyAttch:str = obj["whereClauseCurrencyAttch"]
      self.whereClauseEntityGLC:str = obj["whereClauseEntityGLC"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CurrencyTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GlbCurrenciesExist_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.GlbCurrenciesExist:bool = obj["GlbCurrenciesExist"]
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

class InvokeLinkSearch_input:
   """ Required : 
   linkOpts
   externalCompany
   """  
   def __init__(self, obj):
      self.linkOpts:str = obj["linkOpts"]
      """  Link Options  """  
      self.externalCompany:str = obj["externalCompany"]
      """  External Company  """  
      pass

class InvokeLinkSearch_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Delimited list of glbCurrCode values  """  
      pass

class LinkGlbCurrency2_input:
   """ Required : 
   glbCompany
   glbCurrencyCode
   ds
   ds1
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company field on the GlbCurrency record to link  """  
      self.glbCurrencyCode:str = obj["glbCurrencyCode"]
      """  Global Currency Code field on the GlbCurrency record to link  """  
      self.ds:list[Erp_Tablesets_CurrencyTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_GlbCurrencyTableset] = obj["ds1"]
      pass

class LinkGlbCurrency2_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_GlbCurrencyTableset] = obj["ds1"]
      pass

      """  output parameters  """  

class LinkGlbCurrency_input:
   """ Required : 
   glbCompany
   glbCurrencyCode
   ds
   ds1
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company field on the GlbCurrency record to link  """  
      self.glbCurrencyCode:str = obj["glbCurrencyCode"]
      """  Global Currency Code field on the GlbCurrency record to link  """  
      self.ds:list[Erp_Tablesets_GlbCurrencyTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_CurrencyTableset] = obj["ds1"]
      pass

class LinkGlbCurrency_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrencyTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_CurrencyTableset] = obj["ds1"]
      pass

      """  output parameters  """  

class OnChangeProcessorNum_input:
   """ Required : 
   ds
   newProcessorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyTableset] = obj["ds"]
      self.newProcessorNum:int = obj["newProcessorNum"]
      """  Proposed value for ProcessorNum  """  
      pass

class OnChangeProcessorNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyTableset] = obj["ds"]
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreLinkGlbCurrencyAuto_input:
   """ Required : 
   glbCompany
   glbCurrencyCode
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company field on the GlbCurrency record to link  """  
      self.glbCurrencyCode:str = obj["glbCurrencyCode"]
      """  Global Currency Code field on the GlbCurrency record to link  """  
      pass

class PreLinkGlbCurrencyAuto_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreLinkGlbCurrency_input:
   """ Required : 
   glbCompany
   glbCurrencyCode
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company field on the GlbCurrency record to link  """  
      self.glbCurrencyCode:str = obj["glbCurrencyCode"]
      """  Global Currency Code field on the GlbCurrency record to link  """  
      self.ds:list[Erp_Tablesets_GlbCurrencyTableset] = obj["ds"]
      pass

class PreLinkGlbCurrency_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrencyTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class SkipGlbCurrency_input:
   """ Required : 
   glbCompany
   glbCurrencyCode
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company field on the GlbCurrency record to skip  """  
      self.glbCurrencyCode:str = obj["glbCurrencyCode"]
      """  Global CurrencyCode field on the GlbCurrency record to skip  """  
      self.ds:list[Erp_Tablesets_GlbCurrencyTableset] = obj["ds"]
      pass

class SkipGlbCurrency_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrencyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UnlinkGlbCurrency_input:
   """ Required : 
   glbCompany
   glbCurrencyCode
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company field on the GlbCurrency record to unlink  """  
      self.glbCurrencyCode:str = obj["glbCurrencyCode"]
      """  Global CurrencyCode field on the GlbCurrency record to unlink  """  
      self.ds:list[Erp_Tablesets_GlbCurrencyTableset] = obj["ds"]
      pass

class UnlinkGlbCurrency_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CurrencyTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrencyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCurrencyTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCurrencyTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateMaster_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyTableset] = obj["ds"]
      pass

class UpdateMaster_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyTableset] = obj["ds"]
      self.UpdateMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class onChangeDecimals_input:
   """ Required : 
   ds
   fromUpd
   generalDecimals
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyTableset] = obj["ds"]
      self.fromUpd:bool = obj["fromUpd"]
      """  If is coming from Update  """  
      self.generalDecimals:int = obj["generalDecimals"]
      """  Decimals to be changed  """  
      pass

class onChangeDecimals_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyTableset] = obj["ds"]
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

