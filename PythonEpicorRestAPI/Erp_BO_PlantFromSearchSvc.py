import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PlantFromSearchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PlantFromSearches(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlantFromSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantFromSearches
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantFromSearches",headers=creds) as resp:
           return await resp.json()

async def post_PlantFromSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantFromSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlantRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantFromSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlantFromSearches_Company_Plant(Company, Plant, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlantFromSearch item
   Description: Calls GetByID to retrieve the PlantFromSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantFromSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantFromSearches(" + Company + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlantFromSearches_Company_Plant(Company, Plant, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlantFromSearch for the service
   Description: Calls UpdateExt to update PlantFromSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantFromSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantFromSearches(" + Company + "," + Plant + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlantFromSearches_Company_Plant(Company, Plant, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlantFromSearch item
   Description: Call UpdateExt to delete PlantFromSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantFromSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantFromSearches(" + Company + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlantFromSearches_Company_Plant_PlantEGLCs(Company, Plant, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PlantEGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlantEGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantEGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantFromSearches(" + Company + "," + Plant + ")/PlantEGLCs",headers=creds) as resp:
           return await resp.json()

async def get_PlantFromSearches_Company_Plant_PlantEGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, Plant, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlantEGLC item
   Description: Calls GetByID to retrieve the PlantEGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantEGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantEGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantFromSearches(" + Company + "," + Plant + ")/PlantEGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlantFromSearches_Company_Plant_PlantAttches(Company, Plant, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PlantAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlantAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantFromSearches(" + Company + "," + Plant + ")/PlantAttches",headers=creds) as resp:
           return await resp.json()

async def get_PlantFromSearches_Company_Plant_PlantAttches_Company_Plant_DrawingSeq(Company, Plant, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlantAttch item
   Description: Calls GetByID to retrieve the PlantAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantFromSearches(" + Company + "," + Plant + ")/PlantAttches(" + Company + "," + Plant + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlantEGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlantEGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantEGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantEGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantEGLCs",headers=creds) as resp:
           return await resp.json()

async def post_PlantEGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantEGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantEGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlantEGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantEGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlantEGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlantEGLC item
   Description: Calls GetByID to retrieve the PlantEGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantEGLC
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
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantEGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantEGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlantEGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlantEGLC for the service
   Description: Calls UpdateExt to update PlantEGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantEGLC
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
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantEGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantEGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlantEGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlantEGLC item
   Description: Call UpdateExt to delete PlantEGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantEGLC
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantEGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlantAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlantAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantAttches",headers=creds) as resp:
           return await resp.json()

async def post_PlantAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlantAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlantAttches_Company_Plant_DrawingSeq(Company, Plant, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlantAttch item
   Description: Calls GetByID to retrieve the PlantAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantAttches(" + Company + "," + Plant + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlantAttches_Company_Plant_DrawingSeq(Company, Plant, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlantAttch for the service
   Description: Calls UpdateExt to update PlantAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantAttches(" + Company + "," + Plant + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlantAttches_Company_Plant_DrawingSeq(Company, Plant, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlantAttch item
   Description: Call UpdateExt to delete PlantAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/PlantAttches(" + Company + "," + Plant + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePlant, whereClausePlantAttch, whereClausePlantEGLC, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePlant=" + whereClausePlant
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePlantAttch=" + whereClausePlantAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePlantEGLC=" + whereClausePlantEGLC
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(plant, epicorHeaders = None):
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
   params += "plant=" + plant

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPlantAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPlantAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlantAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlantAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlantAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPlantEGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPlantEGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlantEGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlantEGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlantEGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantFromSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlantAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantEGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlantEGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlantListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlantRow] = obj["value"]
      pass

class Erp_Tablesets_PlantAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Plant:str = obj["Plant"]
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

class Erp_Tablesets_PlantEGLCRow:
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
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlantListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.Name:str = obj["Name"]
      """  The Site name. Used on shipping reports.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlantRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.Name:str = obj["Name"]
      """  The Site name. Used on shipping reports.  """  
      self.Address1:str = obj["Address1"]
      """  Site address line 1.  """  
      self.Address2:str = obj["Address2"]
      """  Site address line 2.  """  
      self.Address3:str = obj["Address3"]
      """  Site address line 3.  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of the address. This field is in sync with the Country.Country field. Must be a valid entry in the Country table.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Main phone number of the Site.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Main fax number of the Site.  """  
      self.CommentText:str = obj["CommentText"]
      """  Comments are intended to be internal comments about a specific Site. These may get pulled into other programs. They are mainly intended as an online storage facility.  """  
      self.PlanningExceptionDays:int = obj["PlanningExceptionDays"]
      """  Number of days early that a supply source (Job or PO) can be without MRP suggesting to postpone the supply.  """  
      self.ISRegion:str = obj["ISRegion"]
      """  Intrastat Region  """  
      self.PlantCostID:str = obj["PlantCostID"]
      """  Id to the Cost Set Group that is used as the default CostGrp.  """  
      self.PrepTime:int = obj["PrepTime"]
      """  Lead Time added to the mfg item to determine the start date.  """  
      self.KitTime:int = obj["KitTime"]
      """  For Manufactured Parts to determine the Due date of the material  """  
      self.ReqTransferHeader:bool = obj["ReqTransferHeader"]
      """  If checked, then Transfer Orders will be created when the requirement is marked as "firm".  """  
      self.CalendarID:str = obj["CalendarID"]
      """  Identifies the default Production Calendar for this Site.   If this equals "", then the ProdCal record is the Company level production calendar.  """  
      self.AllowShipAction:str = obj["AllowShipAction"]
      """  Transfer Shipment entry action to a Transfer Order.  Valid values are "WARN", "STOP" or "NONE" .  WARN means that the user is given a warning, but allowed to proceed (or cancel) with the shipment and transfer request does not have a header.  STOP means that the request cannot be added to the shipment.  NONE allows the request to be added to the shipment with no warnings.  """  
      self.AutoConfirmWindow:int = obj["AutoConfirmWindow"]
      """  Number of days before a sugestion is automatically converted to a firmed requirement.  """  
      self.SingleLineOrder:bool = obj["SingleLineOrder"]
      """  When this field is checked then if transfer orders are being created automatically then each suggestion will create a separate transfer order  """  
      self.MaxOpStartDelay:int = obj["MaxOpStartDelay"]
      """  Maximum Operation Start Delay  """  
      self.MaxOpLength:int = obj["MaxOpLength"]
      """  Maximum Operation Length  """  
      self.DefStationID:str = obj["DefStationID"]
      """  Default Station ID for the Site  """  
      self.FiniteHorz:int = obj["FiniteHorz"]
      """  Number of days to the end of the finite horizon window  """  
      self.NextUnfirmJob:str = obj["NextUnfirmJob"]
      """  Used by MRP.  """  
      self.NextUnfirmTFLine:str = obj["NextUnfirmTFLine"]
      """  Used by MRP.  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag  """  
      self.RCutHorz:int = obj["RCutHorz"]
      """  Number of days to the beginning of the rough cut scheduling horizon window  """  
      self.IncLeadTime:bool = obj["IncLeadTime"]
      """  Include lead time in manufacturing lead time calculation  """  
      self.IncTransLeadTime:bool = obj["IncTransLeadTime"]
      """  Include transfer lead time in manufacturing lead time calculation  """  
      self.IncReceiveTime:bool = obj["IncReceiveTime"]
      """  Include receive time in manufacturing lead time calculation  """  
      self.IncKitTime:bool = obj["IncKitTime"]
      """  Include kit time in manufacturing lead time calculation  """  
      self.IncRCParams:bool = obj["IncRCParams"]
      """  Include rough cut parameters in manufacturing lead time calculation  """  
      self.OverloadHorz:int = obj["OverloadHorz"]
      """  Defines the number of days from the current date the scheduling uses to create job records within the Shop Load table.  """  
      self.SchedulingSendAhead:str = obj["SchedulingSendAhead"]
      """   Determines if the start-to-start job operation offset will be used for production or setup time.  If setup

is chosen, a secondary operation with a start to start relationship will schedule setup to begin xxx 

minutes (defined in the operation) after the production starts on the primary operation.  If production is 

chosen then the production time of the secondary operation will be scheduled to start xxx minutes after the 

production starts on the primary operation.  """  
      self.UnfirmSeriesHorizon:int = obj["UnfirmSeriesHorizon"]
      """  Unfirm Series Horizon  """  
      self.AutoFirmHorizon:int = obj["AutoFirmHorizon"]
      """  AutoFirmHorizon  """  
      self.ManagerName:str = obj["ManagerName"]
      """  Name of the person responsible for delivery  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID (Used Primary for Thailand Localization)  """  
      self.MaintPlant:str = obj["MaintPlant"]
      """  Pertains to Maintenance Management. Site which performs Equipment Maintenance for the this Site.  Note; Maintenance will be allowed in Equipments Site or MaintSite of it's Site.  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.SiteDesc1:str = obj["SiteDesc1"]
      """  Site Description 1  """  
      self.SiteDesc2:str = obj["SiteDesc2"]
      """  Site Description 2  """  
      self.SiteType:str = obj["SiteType"]
      """  Site Type: 0-Normal, 2-Main Site, 3-Sub Site, 5-Consolidated  """  
      self.BusinessTypeCode:str = obj["BusinessTypeCode"]
      """  Business Type Code  """  
      self.BusTypeDesc1:str = obj["BusTypeDesc1"]
      """  Business Type Description 1  """  
      self.BusTypeDesc2:str = obj["BusTypeDesc2"]
      """  Business Type Description 2  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGDefaultInvoicingPoint:str = obj["AGDefaultInvoicingPoint"]
      """  AGDefaultInvoicingPoint  """  
      self.ForceSSTime:bool = obj["ForceSSTime"]
      """  It will force the times to be Start to Start when scheduling this kind of operations.  """  
      self.ForceFFTime:bool = obj["ForceFFTime"]
      """  It will force the times to be Finish to Finish when scheduling this kind of operations  """  
      self.UseLeadTimeDOS:bool = obj["UseLeadTimeDOS"]
      """  Within the leadtime window (MRP Start Date + Lead Time) use Lead Time Days of supply logic in place of standard days of supply  """  
      self.AllowMinQty:bool = obj["AllowMinQty"]
      """  Within the lead time window, allow consumption of minimum qty until below safety  """  
      self.IgnoreMtlConstraints:bool = obj["IgnoreMtlConstraints"]
      """  It will allow the user to move the job in regardless of material constraints and Subcontract PO?s  """  
      self.AGProvinceCode:str = obj["AGProvinceCode"]
      """  AGProvinceCode  """  
      self.AGLocationCode:str = obj["AGLocationCode"]
      """  AGLocationCode  """  
      self.AGNeighborhood:str = obj["AGNeighborhood"]
      """  AGNeighborhood  """  
      self.AGStreet:str = obj["AGStreet"]
      """  AGStreet  """  
      self.AGStreetNumber:str = obj["AGStreetNumber"]
      """  AGStreetNumber  """  
      self.AGExtraStreetNumber:str = obj["AGExtraStreetNumber"]
      """  AGExtraStreetNumber  """  
      self.AGFloor:str = obj["AGFloor"]
      """  AGFloor  """  
      self.AGApartment:str = obj["AGApartment"]
      """  AGApartment  """  
      self.MXMunicipio:str = obj["MXMunicipio"]
      """  MXMunicipio  """  
      self.MaxLateDaysPORel:int = obj["MaxLateDaysPORel"]
      """  Defines the Number of Days from the PO release date the schedule engine considers a late PO Release or discard it. If the PO release date plus the supplier due date horizon is before today then the PO Release is discarded. If the PO release date plus the supplier due date horizon is today or later then the PO Release is considered late.  """  
      self.INECCNumber:str = obj["INECCNumber"]
      """  Obsolete  """  
      self.INExciseRange:str = obj["INExciseRange"]
      """  Obsolete  """  
      self.INExciseDivision:str = obj["INExciseDivision"]
      """  Obsolete  """  
      self.INExCommissionRate:str = obj["INExCommissionRate"]
      """  Obsolete  """  
      self.INTINNumber:str = obj["INTINNumber"]
      """  INTINNumber  """  
      self.INCSTNumber:str = obj["INCSTNumber"]
      """  Obsolete  """  
      self.INSTRegistration:str = obj["INSTRegistration"]
      """  Obsolete  """  
      self.UseSchedulingMultiJob:bool = obj["UseSchedulingMultiJob"]
      """  Default value for the this flag at every place where the scheduling UI is called to instruct to the scheduling engine looks for any assembly or material that has a direct job link and those linked jobs get rescheduled as well to be just in time to supply the main job.  """  
      self.AutoLoadChildJobs:bool = obj["AutoLoadChildJobs"]
      """  Will allow to auto load all child jobs related to the selected job at the Job Scheduling Board.  """  
      self.AutoLoadParentJobs:bool = obj["AutoLoadParentJobs"]
      """  Will allow to auto load all parent jobs related to the selected job at the Job Scheduling Board.  """  
      self.MinimizeWIP:bool = obj["MinimizeWIP"]
      """  Indicate to schedule engine to get the final date of the parent job and do backwards all the group of jobs to minimize gaps.  """  
      self.TimeZoneID:str = obj["TimeZoneID"]
      """  Time Zone of the site.  """  
      self.TimeZoneAdjustForDST:bool = obj["TimeZoneAdjustForDST"]
      """  Not used.  """  
      self.SyncReqBy:bool = obj["SyncReqBy"]
      """  SyncReqBy  """  
      self.ACWPercentage:int = obj["ACWPercentage"]
      """  Auto consume window percentage, this is a percentage to calculate the auto consume window days  that scheduling engine will take in consideration to look for available quantity to consume.  """  
      self.BWSchedStartTime:int = obj["BWSchedStartTime"]
      """  It is the time used for schedule engine when scheduling backwards automatically. In some screens it is just a default and can be modified before scheduling.  """  
      self.INTaxRegistrationID:str = obj["INTaxRegistrationID"]
      """  INTaxRegistrationID  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the Plant has to be synchronized with Epicor FSA application.  """  
      self.SchedulingDirection:str = obj["SchedulingDirection"]
      """  Determines the schedule direction that will default when manually scheduling a job. The following screens will be impacted by this setting: Job Entry, Service Job Entry, Maintenance Job Entry, Job Scheduling Board, Multi Resource Scheduling Board, Resource Scheduling Board, Job Manager, Project Entry.  """  
      self.US1099PayersTIN:str = obj["US1099PayersTIN"]
      """  US1099PayersTIN  """  
      self.US1099NameControl:str = obj["US1099NameControl"]
      """  US1099NameControl  """  
      self.US1099OfficeCode:str = obj["US1099OfficeCode"]
      """  US1099OfficeCode  """  
      self.US1099ContactPerson:str = obj["US1099ContactPerson"]
      """  US1099ContactPerson  """  
      self.US1099EMailAddress:str = obj["US1099EMailAddress"]
      """  US1099EmailAddress  """  
      self.US1099FaxNum:str = obj["US1099FaxNum"]
      """  US1099FaxNum  """  
      self.US1099PhoneNum:str = obj["US1099PhoneNum"]
      """  US1099PhoneNum  """  
      self.US1099TransControlCode:str = obj["US1099TransControlCode"]
      """  US1099TransControlCode  """  
      self.US1099Name1:str = obj["US1099Name1"]
      """  US1099Name1  """  
      self.US1099Name2:str = obj["US1099Name2"]
      """  US1099Name2  """  
      self.US1099Address1:str = obj["US1099Address1"]
      """  US1099Address1  """  
      self.US1099Address2:str = obj["US1099Address2"]
      """  US1099Address2  """  
      self.US1099Address3:str = obj["US1099Address3"]
      """  US1099Address3  """  
      self.US1099City:str = obj["US1099City"]
      """  US1099City  """  
      self.US1099State:str = obj["US1099State"]
      """  US1099State  """  
      self.US1099ZIP:str = obj["US1099ZIP"]
      """  US1099ZIP  """  
      self.TaxID:str = obj["TaxID"]
      """  TaxID  """  
      self.COASegReferences:str = obj["COASegReferences"]
      """  List of fields which are referenced by COA segments.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Reason code for cost code change.  """  
      self.ReasonReq:bool = obj["ReasonReq"]
      """  Reason code required flag.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  Reason type  """  
      self.Use3rdPartySched:bool = obj["Use3rdPartySched"]
      """  Indicates if the scheduling logic in the system is not used because a third party scheduling.  """  
      self.ReasonCodeDescription:str = obj["ReasonCodeDescription"]
      """  Reason Code Description  """  
      self.KineticColor:str = obj["KineticColor"]
      """  Background color for site (Kinetic UI).  """  
      self.LogoFileName:str = obj["LogoFileName"]
      self.LogoImageContent:str = obj["LogoImageContent"]
      self.BitFlag:int = obj["BitFlag"]
      self.AGLocationDescription:str = obj["AGLocationDescription"]
      self.AGProvinceCodeDescription:str = obj["AGProvinceCodeDescription"]
      self.CalendarIDDescription:str = obj["CalendarIDDescription"]
      self.CompanySendToFSA:bool = obj["CompanySendToFSA"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.MaintPlantName:str = obj["MaintPlantName"]
      self.PlantCostDescription:str = obj["PlantCostDescription"]
      self.XbSystSiteIsLegalEntity:bool = obj["XbSystSiteIsLegalEntity"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_PlantAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Plant:str = obj["Plant"]
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

class Erp_Tablesets_PlantEGLCRow:
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
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlantListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.Name:str = obj["Name"]
      """  The Site name. Used on shipping reports.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlantListTableset:
   def __init__(self, obj):
      self.PlantList:list[Erp_Tablesets_PlantListRow] = obj["PlantList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PlantRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.Name:str = obj["Name"]
      """  The Site name. Used on shipping reports.  """  
      self.Address1:str = obj["Address1"]
      """  Site address line 1.  """  
      self.Address2:str = obj["Address2"]
      """  Site address line 2.  """  
      self.Address3:str = obj["Address3"]
      """  Site address line 3.  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of the address. This field is in sync with the Country.Country field. Must be a valid entry in the Country table.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Main phone number of the Site.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Main fax number of the Site.  """  
      self.CommentText:str = obj["CommentText"]
      """  Comments are intended to be internal comments about a specific Site. These may get pulled into other programs. They are mainly intended as an online storage facility.  """  
      self.PlanningExceptionDays:int = obj["PlanningExceptionDays"]
      """  Number of days early that a supply source (Job or PO) can be without MRP suggesting to postpone the supply.  """  
      self.ISRegion:str = obj["ISRegion"]
      """  Intrastat Region  """  
      self.PlantCostID:str = obj["PlantCostID"]
      """  Id to the Cost Set Group that is used as the default CostGrp.  """  
      self.PrepTime:int = obj["PrepTime"]
      """  Lead Time added to the mfg item to determine the start date.  """  
      self.KitTime:int = obj["KitTime"]
      """  For Manufactured Parts to determine the Due date of the material  """  
      self.ReqTransferHeader:bool = obj["ReqTransferHeader"]
      """  If checked, then Transfer Orders will be created when the requirement is marked as "firm".  """  
      self.CalendarID:str = obj["CalendarID"]
      """  Identifies the default Production Calendar for this Site.   If this equals "", then the ProdCal record is the Company level production calendar.  """  
      self.AllowShipAction:str = obj["AllowShipAction"]
      """  Transfer Shipment entry action to a Transfer Order.  Valid values are "WARN", "STOP" or "NONE" .  WARN means that the user is given a warning, but allowed to proceed (or cancel) with the shipment and transfer request does not have a header.  STOP means that the request cannot be added to the shipment.  NONE allows the request to be added to the shipment with no warnings.  """  
      self.AutoConfirmWindow:int = obj["AutoConfirmWindow"]
      """  Number of days before a sugestion is automatically converted to a firmed requirement.  """  
      self.SingleLineOrder:bool = obj["SingleLineOrder"]
      """  When this field is checked then if transfer orders are being created automatically then each suggestion will create a separate transfer order  """  
      self.MaxOpStartDelay:int = obj["MaxOpStartDelay"]
      """  Maximum Operation Start Delay  """  
      self.MaxOpLength:int = obj["MaxOpLength"]
      """  Maximum Operation Length  """  
      self.DefStationID:str = obj["DefStationID"]
      """  Default Station ID for the Site  """  
      self.FiniteHorz:int = obj["FiniteHorz"]
      """  Number of days to the end of the finite horizon window  """  
      self.NextUnfirmJob:str = obj["NextUnfirmJob"]
      """  Used by MRP.  """  
      self.NextUnfirmTFLine:str = obj["NextUnfirmTFLine"]
      """  Used by MRP.  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag  """  
      self.RCutHorz:int = obj["RCutHorz"]
      """  Number of days to the beginning of the rough cut scheduling horizon window  """  
      self.IncLeadTime:bool = obj["IncLeadTime"]
      """  Include lead time in manufacturing lead time calculation  """  
      self.IncTransLeadTime:bool = obj["IncTransLeadTime"]
      """  Include transfer lead time in manufacturing lead time calculation  """  
      self.IncReceiveTime:bool = obj["IncReceiveTime"]
      """  Include receive time in manufacturing lead time calculation  """  
      self.IncKitTime:bool = obj["IncKitTime"]
      """  Include kit time in manufacturing lead time calculation  """  
      self.IncRCParams:bool = obj["IncRCParams"]
      """  Include rough cut parameters in manufacturing lead time calculation  """  
      self.OverloadHorz:int = obj["OverloadHorz"]
      """  Defines the number of days from the current date the scheduling uses to create job records within the Shop Load table.  """  
      self.SchedulingSendAhead:str = obj["SchedulingSendAhead"]
      """   Determines if the start-to-start job operation offset will be used for production or setup time.  If setup

is chosen, a secondary operation with a start to start relationship will schedule setup to begin xxx 

minutes (defined in the operation) after the production starts on the primary operation.  If production is 

chosen then the production time of the secondary operation will be scheduled to start xxx minutes after the 

production starts on the primary operation.  """  
      self.UnfirmSeriesHorizon:int = obj["UnfirmSeriesHorizon"]
      """  Unfirm Series Horizon  """  
      self.AutoFirmHorizon:int = obj["AutoFirmHorizon"]
      """  AutoFirmHorizon  """  
      self.ManagerName:str = obj["ManagerName"]
      """  Name of the person responsible for delivery  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID (Used Primary for Thailand Localization)  """  
      self.MaintPlant:str = obj["MaintPlant"]
      """  Pertains to Maintenance Management. Site which performs Equipment Maintenance for the this Site.  Note; Maintenance will be allowed in Equipments Site or MaintSite of it's Site.  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.SiteDesc1:str = obj["SiteDesc1"]
      """  Site Description 1  """  
      self.SiteDesc2:str = obj["SiteDesc2"]
      """  Site Description 2  """  
      self.SiteType:str = obj["SiteType"]
      """  Site Type: 0-Normal, 2-Main Site, 3-Sub Site, 5-Consolidated  """  
      self.BusinessTypeCode:str = obj["BusinessTypeCode"]
      """  Business Type Code  """  
      self.BusTypeDesc1:str = obj["BusTypeDesc1"]
      """  Business Type Description 1  """  
      self.BusTypeDesc2:str = obj["BusTypeDesc2"]
      """  Business Type Description 2  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGDefaultInvoicingPoint:str = obj["AGDefaultInvoicingPoint"]
      """  AGDefaultInvoicingPoint  """  
      self.ForceSSTime:bool = obj["ForceSSTime"]
      """  It will force the times to be Start to Start when scheduling this kind of operations.  """  
      self.ForceFFTime:bool = obj["ForceFFTime"]
      """  It will force the times to be Finish to Finish when scheduling this kind of operations  """  
      self.UseLeadTimeDOS:bool = obj["UseLeadTimeDOS"]
      """  Within the leadtime window (MRP Start Date + Lead Time) use Lead Time Days of supply logic in place of standard days of supply  """  
      self.AllowMinQty:bool = obj["AllowMinQty"]
      """  Within the lead time window, allow consumption of minimum qty until below safety  """  
      self.IgnoreMtlConstraints:bool = obj["IgnoreMtlConstraints"]
      """  It will allow the user to move the job in regardless of material constraints and Subcontract PO?s  """  
      self.AGProvinceCode:str = obj["AGProvinceCode"]
      """  AGProvinceCode  """  
      self.AGLocationCode:str = obj["AGLocationCode"]
      """  AGLocationCode  """  
      self.AGNeighborhood:str = obj["AGNeighborhood"]
      """  AGNeighborhood  """  
      self.AGStreet:str = obj["AGStreet"]
      """  AGStreet  """  
      self.AGStreetNumber:str = obj["AGStreetNumber"]
      """  AGStreetNumber  """  
      self.AGExtraStreetNumber:str = obj["AGExtraStreetNumber"]
      """  AGExtraStreetNumber  """  
      self.AGFloor:str = obj["AGFloor"]
      """  AGFloor  """  
      self.AGApartment:str = obj["AGApartment"]
      """  AGApartment  """  
      self.MXMunicipio:str = obj["MXMunicipio"]
      """  MXMunicipio  """  
      self.MaxLateDaysPORel:int = obj["MaxLateDaysPORel"]
      """  Defines the Number of Days from the PO release date the schedule engine considers a late PO Release or discard it. If the PO release date plus the supplier due date horizon is before today then the PO Release is discarded. If the PO release date plus the supplier due date horizon is today or later then the PO Release is considered late.  """  
      self.INECCNumber:str = obj["INECCNumber"]
      """  Obsolete  """  
      self.INExciseRange:str = obj["INExciseRange"]
      """  Obsolete  """  
      self.INExciseDivision:str = obj["INExciseDivision"]
      """  Obsolete  """  
      self.INExCommissionRate:str = obj["INExCommissionRate"]
      """  Obsolete  """  
      self.INTINNumber:str = obj["INTINNumber"]
      """  INTINNumber  """  
      self.INCSTNumber:str = obj["INCSTNumber"]
      """  Obsolete  """  
      self.INSTRegistration:str = obj["INSTRegistration"]
      """  Obsolete  """  
      self.UseSchedulingMultiJob:bool = obj["UseSchedulingMultiJob"]
      """  Default value for the this flag at every place where the scheduling UI is called to instruct to the scheduling engine looks for any assembly or material that has a direct job link and those linked jobs get rescheduled as well to be just in time to supply the main job.  """  
      self.AutoLoadChildJobs:bool = obj["AutoLoadChildJobs"]
      """  Will allow to auto load all child jobs related to the selected job at the Job Scheduling Board.  """  
      self.AutoLoadParentJobs:bool = obj["AutoLoadParentJobs"]
      """  Will allow to auto load all parent jobs related to the selected job at the Job Scheduling Board.  """  
      self.MinimizeWIP:bool = obj["MinimizeWIP"]
      """  Indicate to schedule engine to get the final date of the parent job and do backwards all the group of jobs to minimize gaps.  """  
      self.TimeZoneID:str = obj["TimeZoneID"]
      """  Time Zone of the site.  """  
      self.TimeZoneAdjustForDST:bool = obj["TimeZoneAdjustForDST"]
      """  Not used.  """  
      self.SyncReqBy:bool = obj["SyncReqBy"]
      """  SyncReqBy  """  
      self.ACWPercentage:int = obj["ACWPercentage"]
      """  Auto consume window percentage, this is a percentage to calculate the auto consume window days  that scheduling engine will take in consideration to look for available quantity to consume.  """  
      self.BWSchedStartTime:int = obj["BWSchedStartTime"]
      """  It is the time used for schedule engine when scheduling backwards automatically. In some screens it is just a default and can be modified before scheduling.  """  
      self.INTaxRegistrationID:str = obj["INTaxRegistrationID"]
      """  INTaxRegistrationID  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the Plant has to be synchronized with Epicor FSA application.  """  
      self.SchedulingDirection:str = obj["SchedulingDirection"]
      """  Determines the schedule direction that will default when manually scheduling a job. The following screens will be impacted by this setting: Job Entry, Service Job Entry, Maintenance Job Entry, Job Scheduling Board, Multi Resource Scheduling Board, Resource Scheduling Board, Job Manager, Project Entry.  """  
      self.US1099PayersTIN:str = obj["US1099PayersTIN"]
      """  US1099PayersTIN  """  
      self.US1099NameControl:str = obj["US1099NameControl"]
      """  US1099NameControl  """  
      self.US1099OfficeCode:str = obj["US1099OfficeCode"]
      """  US1099OfficeCode  """  
      self.US1099ContactPerson:str = obj["US1099ContactPerson"]
      """  US1099ContactPerson  """  
      self.US1099EMailAddress:str = obj["US1099EMailAddress"]
      """  US1099EmailAddress  """  
      self.US1099FaxNum:str = obj["US1099FaxNum"]
      """  US1099FaxNum  """  
      self.US1099PhoneNum:str = obj["US1099PhoneNum"]
      """  US1099PhoneNum  """  
      self.US1099TransControlCode:str = obj["US1099TransControlCode"]
      """  US1099TransControlCode  """  
      self.US1099Name1:str = obj["US1099Name1"]
      """  US1099Name1  """  
      self.US1099Name2:str = obj["US1099Name2"]
      """  US1099Name2  """  
      self.US1099Address1:str = obj["US1099Address1"]
      """  US1099Address1  """  
      self.US1099Address2:str = obj["US1099Address2"]
      """  US1099Address2  """  
      self.US1099Address3:str = obj["US1099Address3"]
      """  US1099Address3  """  
      self.US1099City:str = obj["US1099City"]
      """  US1099City  """  
      self.US1099State:str = obj["US1099State"]
      """  US1099State  """  
      self.US1099ZIP:str = obj["US1099ZIP"]
      """  US1099ZIP  """  
      self.TaxID:str = obj["TaxID"]
      """  TaxID  """  
      self.COASegReferences:str = obj["COASegReferences"]
      """  List of fields which are referenced by COA segments.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Reason code for cost code change.  """  
      self.ReasonReq:bool = obj["ReasonReq"]
      """  Reason code required flag.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  Reason type  """  
      self.Use3rdPartySched:bool = obj["Use3rdPartySched"]
      """  Indicates if the scheduling logic in the system is not used because a third party scheduling.  """  
      self.ReasonCodeDescription:str = obj["ReasonCodeDescription"]
      """  Reason Code Description  """  
      self.KineticColor:str = obj["KineticColor"]
      """  Background color for site (Kinetic UI).  """  
      self.LogoFileName:str = obj["LogoFileName"]
      self.LogoImageContent:str = obj["LogoImageContent"]
      self.BitFlag:int = obj["BitFlag"]
      self.AGLocationDescription:str = obj["AGLocationDescription"]
      self.AGProvinceCodeDescription:str = obj["AGProvinceCodeDescription"]
      self.CalendarIDDescription:str = obj["CalendarIDDescription"]
      self.CompanySendToFSA:bool = obj["CompanySendToFSA"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.MaintPlantName:str = obj["MaintPlantName"]
      self.PlantCostDescription:str = obj["PlantCostDescription"]
      self.XbSystSiteIsLegalEntity:bool = obj["XbSystSiteIsLegalEntity"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlantTableset:
   def __init__(self, obj):
      self.Plant:list[Erp_Tablesets_PlantRow] = obj["Plant"]
      self.PlantAttch:list[Erp_Tablesets_PlantAttchRow] = obj["PlantAttch"]
      self.PlantEGLC:list[Erp_Tablesets_PlantEGLCRow] = obj["PlantEGLC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPlantTableset:
   def __init__(self, obj):
      self.Plant:list[Erp_Tablesets_PlantRow] = obj["Plant"]
      self.PlantAttch:list[Erp_Tablesets_PlantAttchRow] = obj["PlantAttch"]
      self.PlantEGLC:list[Erp_Tablesets_PlantEGLCRow] = obj["PlantEGLC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   plant
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PlantTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PlantTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PlantTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PlantListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPlantAttch_input:
   """ Required : 
   ds
   plant
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlantTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      pass

class GetNewPlantAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPlantEGLC_input:
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
      self.ds:list[Erp_Tablesets_PlantTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.key6:str = obj["key6"]
      pass

class GetNewPlantEGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePlant
   whereClausePlantAttch
   whereClausePlantEGLC
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePlant:str = obj["whereClausePlant"]
      self.whereClausePlantAttch:str = obj["whereClausePlantAttch"]
      self.whereClausePlantEGLC:str = obj["whereClausePlantEGLC"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PlantTableset] = obj["returnObj"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPlantTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPlantTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlantTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantTableset] = obj["ds"]
      pass

      """  output parameters  """  

