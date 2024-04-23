import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.VNTGLRptMasSvc
# Description: VNTGLRptMas service
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptMas(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VNTGLRptMas items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VNTGLRptMas
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptMasRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptMas",headers=creds) as resp:
           return await resp.json()

async def post_VNTGLRptMas(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VNTGLRptMas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VNTGLRptMasRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VNTGLRptMasRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptMas", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptMas_Company_LocalName_Key2(Company, LocalName, Key2, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VNTGLRptMa item
   Description: Calls GetByID to retrieve the VNTGLRptMa item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptMa
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptMasRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptMas(" + Company + "," + LocalName + "," + Key2 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VNTGLRptMas_Company_LocalName_Key2(Company, LocalName, Key2, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VNTGLRptMa for the service
   Description: Calls UpdateExt to update VNTGLRptMa. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VNTGLRptMa
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VNTGLRptMasRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptMas(" + Company + "," + LocalName + "," + Key2 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VNTGLRptMas_Company_LocalName_Key2(Company, LocalName, Key2, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VNTGLRptMa item
   Description: Call UpdateExt to delete VNTGLRptMa item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VNTGLRptMa
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptMas(" + Company + "," + LocalName + "," + Key2 + ")",headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptMas_Company_LocalName_Key2_VNTGLRptRows(Company, LocalName, Key2, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get VNTGLRptRows items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VNTGLRptRows1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptMas(" + Company + "," + LocalName + "," + Key2 + ")/VNTGLRptRows",headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptMas_Company_LocalName_Key2_VNTGLRptRows_Company_LocalName_Key2_Key3(Company, LocalName, Key2, Key3, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VNTGLRptRow item
   Description: Calls GetByID to retrieve the VNTGLRptRow item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRow1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptMas(" + Company + "," + LocalName + "," + Key2 + ")/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")",headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptRows(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VNTGLRptRows items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VNTGLRptRows
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows",headers=creds) as resp:
           return await resp.json()

async def post_VNTGLRptRows(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VNTGLRptRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptRows_Company_LocalName_Key2_Key3(Company, LocalName, Key2, Key3, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VNTGLRptRow item
   Description: Calls GetByID to retrieve the VNTGLRptRow item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRow
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VNTGLRptRows_Company_LocalName_Key2_Key3(Company, LocalName, Key2, Key3, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VNTGLRptRow for the service
   Description: Calls UpdateExt to update VNTGLRptRow. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VNTGLRptRow
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VNTGLRptRows_Company_LocalName_Key2_Key3(Company, LocalName, Key2, Key3, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VNTGLRptRow item
   Description: Call UpdateExt to delete VNTGLRptRow item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VNTGLRptRow
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")",headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptRows_Company_LocalName_Key2_Key3_VNTGLRptRowAcctCorrs(Company, LocalName, Key2, Key3, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get VNTGLRptRowAcctCorrs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VNTGLRptRowAcctCorrs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowAcctCorrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")/VNTGLRptRowAcctCorrs",headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptRows_Company_LocalName_Key2_Key3_VNTGLRptRowAcctCorrs_Company_LocalName_Key2_Key3_Key4(Company, LocalName, Key2, Key3, Key4, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VNTGLRptRowAcctCorr item
   Description: Calls GetByID to retrieve the VNTGLRptRowAcctCorr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRowAcctCorr1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctCorrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")/VNTGLRptRowAcctCorrs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")",headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptRows_Company_LocalName_Key2_Key3_VNTGLRptRowAcctObjs(Company, LocalName, Key2, Key3, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get VNTGLRptRowAcctObjs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VNTGLRptRowAcctObjs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowAcctObjRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")/VNTGLRptRowAcctObjs",headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptRows_Company_LocalName_Key2_Key3_VNTGLRptRowAcctObjs_Company_LocalName_Key2_Key3_Key4(Company, LocalName, Key2, Key3, Key4, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VNTGLRptRowAcctObj item
   Description: Calls GetByID to retrieve the VNTGLRptRowAcctObj item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRowAcctObj1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctObjRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")/VNTGLRptRowAcctObjs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")",headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptRows_Company_LocalName_Key2_Key3_VNTGLRptRowAccts(Company, LocalName, Key2, Key3, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get VNTGLRptRowAccts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VNTGLRptRowAccts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")/VNTGLRptRowAccts",headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptRows_Company_LocalName_Key2_Key3_VNTGLRptRowAccts_Company_LocalName_Key2_Key3_Key4(Company, LocalName, Key2, Key3, Key4, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VNTGLRptRowAcct item
   Description: Calls GetByID to retrieve the VNTGLRptRowAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRowAcct1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")/VNTGLRptRowAccts(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")",headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptRows_Company_LocalName_Key2_Key3_VNTGLRptRowAcctSegs(Company, LocalName, Key2, Key3, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get VNTGLRptRowAcctSegs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VNTGLRptRowAcctSegs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowAcctSegRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")/VNTGLRptRowAcctSegs",headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptRows_Company_LocalName_Key2_Key3_VNTGLRptRowAcctSegs_Company_LocalName_Key2_Key3_Key4(Company, LocalName, Key2, Key3, Key4, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VNTGLRptRowAcctSeg item
   Description: Calls GetByID to retrieve the VNTGLRptRowAcctSeg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRowAcctSeg1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctSegRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")/VNTGLRptRowAcctSegs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")",headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptRows_Company_LocalName_Key2_Key3_VNTGLRptRowAcctSums(Company, LocalName, Key2, Key3, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get VNTGLRptRowAcctSums items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VNTGLRptRowAcctSums1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowAcctSumRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")/VNTGLRptRowAcctSums",headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptRows_Company_LocalName_Key2_Key3_VNTGLRptRowAcctSums_Company_LocalName_Key2_Key3_Key4(Company, LocalName, Key2, Key3, Key4, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VNTGLRptRowAcctSum item
   Description: Calls GetByID to retrieve the VNTGLRptRowAcctSum item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRowAcctSum1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctSumRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRows(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + ")/VNTGLRptRowAcctSums(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")",headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptRowAcctCorrs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VNTGLRptRowAcctCorrs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VNTGLRptRowAcctCorrs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowAcctCorrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctCorrs",headers=creds) as resp:
           return await resp.json()

async def post_VNTGLRptRowAcctCorrs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VNTGLRptRowAcctCorrs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctCorrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctCorrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctCorrs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptRowAcctCorrs_Company_LocalName_Key2_Key3_Key4(Company, LocalName, Key2, Key3, Key4, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VNTGLRptRowAcctCorr item
   Description: Calls GetByID to retrieve the VNTGLRptRowAcctCorr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRowAcctCorr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctCorrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctCorrs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VNTGLRptRowAcctCorrs_Company_LocalName_Key2_Key3_Key4(Company, LocalName, Key2, Key3, Key4, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VNTGLRptRowAcctCorr for the service
   Description: Calls UpdateExt to update VNTGLRptRowAcctCorr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VNTGLRptRowAcctCorr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctCorrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctCorrs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VNTGLRptRowAcctCorrs_Company_LocalName_Key2_Key3_Key4(Company, LocalName, Key2, Key3, Key4, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VNTGLRptRowAcctCorr item
   Description: Call UpdateExt to delete VNTGLRptRowAcctCorr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VNTGLRptRowAcctCorr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctCorrs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")",headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptRowAcctObjs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VNTGLRptRowAcctObjs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VNTGLRptRowAcctObjs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowAcctObjRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctObjs",headers=creds) as resp:
           return await resp.json()

async def post_VNTGLRptRowAcctObjs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VNTGLRptRowAcctObjs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctObjRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctObjRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctObjs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptRowAcctObjs_Company_LocalName_Key2_Key3_Key4(Company, LocalName, Key2, Key3, Key4, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VNTGLRptRowAcctObj item
   Description: Calls GetByID to retrieve the VNTGLRptRowAcctObj item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRowAcctObj
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctObjRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctObjs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VNTGLRptRowAcctObjs_Company_LocalName_Key2_Key3_Key4(Company, LocalName, Key2, Key3, Key4, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VNTGLRptRowAcctObj for the service
   Description: Calls UpdateExt to update VNTGLRptRowAcctObj. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VNTGLRptRowAcctObj
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctObjRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctObjs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VNTGLRptRowAcctObjs_Company_LocalName_Key2_Key3_Key4(Company, LocalName, Key2, Key3, Key4, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VNTGLRptRowAcctObj item
   Description: Call UpdateExt to delete VNTGLRptRowAcctObj item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VNTGLRptRowAcctObj
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctObjs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")",headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptRowAccts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VNTGLRptRowAccts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VNTGLRptRowAccts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAccts",headers=creds) as resp:
           return await resp.json()

async def post_VNTGLRptRowAccts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VNTGLRptRowAccts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAccts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptRowAccts_Company_LocalName_Key2_Key3_Key4(Company, LocalName, Key2, Key3, Key4, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VNTGLRptRowAcct item
   Description: Calls GetByID to retrieve the VNTGLRptRowAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRowAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAccts(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VNTGLRptRowAccts_Company_LocalName_Key2_Key3_Key4(Company, LocalName, Key2, Key3, Key4, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VNTGLRptRowAcct for the service
   Description: Calls UpdateExt to update VNTGLRptRowAcct. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VNTGLRptRowAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAccts(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VNTGLRptRowAccts_Company_LocalName_Key2_Key3_Key4(Company, LocalName, Key2, Key3, Key4, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VNTGLRptRowAcct item
   Description: Call UpdateExt to delete VNTGLRptRowAcct item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VNTGLRptRowAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAccts(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")",headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptRowAcctSegs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VNTGLRptRowAcctSegs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VNTGLRptRowAcctSegs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowAcctSegRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctSegs",headers=creds) as resp:
           return await resp.json()

async def post_VNTGLRptRowAcctSegs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VNTGLRptRowAcctSegs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctSegRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctSegRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctSegs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptRowAcctSegs_Company_LocalName_Key2_Key3_Key4(Company, LocalName, Key2, Key3, Key4, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VNTGLRptRowAcctSeg item
   Description: Calls GetByID to retrieve the VNTGLRptRowAcctSeg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRowAcctSeg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctSegRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctSegs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VNTGLRptRowAcctSegs_Company_LocalName_Key2_Key3_Key4(Company, LocalName, Key2, Key3, Key4, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VNTGLRptRowAcctSeg for the service
   Description: Calls UpdateExt to update VNTGLRptRowAcctSeg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VNTGLRptRowAcctSeg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctSegRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctSegs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VNTGLRptRowAcctSegs_Company_LocalName_Key2_Key3_Key4(Company, LocalName, Key2, Key3, Key4, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VNTGLRptRowAcctSeg item
   Description: Call UpdateExt to delete VNTGLRptRowAcctSeg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VNTGLRptRowAcctSeg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctSegs(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")",headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptRowAcctSums(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VNTGLRptRowAcctSums items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VNTGLRptRowAcctSums
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptRowAcctSumRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctSums",headers=creds) as resp:
           return await resp.json()

async def post_VNTGLRptRowAcctSums(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VNTGLRptRowAcctSums
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctSumRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctSumRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctSums", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VNTGLRptRowAcctSums_Company_LocalName_Key2_Key3_Key4(Company, LocalName, Key2, Key3, Key4, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VNTGLRptRowAcctSum item
   Description: Calls GetByID to retrieve the VNTGLRptRowAcctSum item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VNTGLRptRowAcctSum
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctSumRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctSums(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VNTGLRptRowAcctSums_Company_LocalName_Key2_Key3_Key4(Company, LocalName, Key2, Key3, Key4, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VNTGLRptRowAcctSum for the service
   Description: Calls UpdateExt to update VNTGLRptRowAcctSum. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VNTGLRptRowAcctSum
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VNTGLRptRowAcctSumRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctSums(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VNTGLRptRowAcctSums_Company_LocalName_Key2_Key3_Key4(Company, LocalName, Key2, Key3, Key4, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VNTGLRptRowAcctSum item
   Description: Call UpdateExt to delete VNTGLRptRowAcctSum item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VNTGLRptRowAcctSum
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LocalName: Desc: LocalName   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/VNTGLRptRowAcctSums(" + Company + "," + LocalName + "," + Key2 + "," + Key3 + "," + Key4 + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VNTGLRptMasListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseVNTGLRptMas, whereClauseVNTGLRptRow, whereClauseVNTGLRptRowAcctCorr, whereClauseVNTGLRptRowAcctObj, whereClauseVNTGLRptRowAcct, whereClauseVNTGLRptRowAcctSeg, whereClauseVNTGLRptRowAcctSum, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseVNTGLRptMas=" + whereClauseVNTGLRptMas
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVNTGLRptRow=" + whereClauseVNTGLRptRow
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVNTGLRptRowAcctCorr=" + whereClauseVNTGLRptRowAcctCorr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVNTGLRptRowAcctObj=" + whereClauseVNTGLRptRowAcctObj
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVNTGLRptRowAcct=" + whereClauseVNTGLRptRowAcct
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVNTGLRptRowAcctSeg=" + whereClauseVNTGLRptRowAcctSeg
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVNTGLRptRowAcctSum=" + whereClauseVNTGLRptRowAcctSum
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(localName, key2, epicorHeaders = None):
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
   params += "localName=" + localName
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key2=" + key2

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetDataComboAttributeFont(epicorHeaders = None):
   """  
   Summary: Invoke method GetDataComboAttributeFont
   Description: <param name="listDataAttributeFont">The list of options for Attribute font </param>
   OperationID: GetDataComboAttributeFont
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataComboAttributeFont_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetDataComboItemValue(epicorHeaders = None):
   """  
   Summary: Invoke method GetDataComboItemValue
   Description: <param name="listDataItemValue">The list of options for Item Value </param>
   OperationID: GetDataComboItemValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataComboItemValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetDataComboReportTemplate(epicorHeaders = None):
   """  
   Summary: Invoke method GetDataComboReportTemplate
   Description: <param name="listDataReportTemplate">The list of options for RowAccountType </param>
   OperationID: GetDataComboReportTemplate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataComboReportTemplate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetDataComboRowAccountType(epicorHeaders = None):
   """  
   Summary: Invoke method GetDataComboRowAccountType
   Description: <param name="listDataRowAcctType">The list of options for RowAccountType </param>
   OperationID: GetDataComboRowAccountType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataComboRowAccountType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewVNTGLRptMas(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVNTGLRptMas
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVNTGLRptMas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVNTGLRptMas_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVNTGLRptMas_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVNTGLRptRow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVNTGLRptRow
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVNTGLRptRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVNTGLRptRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVNTGLRptRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVNTGLRptRowAcctCorr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVNTGLRptRowAcctCorr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVNTGLRptRowAcctCorr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVNTGLRptRowAcctCorr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVNTGLRptRowAcctCorr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVNTGLRptRowAcctObj(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVNTGLRptRowAcctObj
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVNTGLRptRowAcctObj
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVNTGLRptRowAcctObj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVNTGLRptRowAcctObj_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVNTGLRptRowAcct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVNTGLRptRowAcct
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVNTGLRptRowAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVNTGLRptRowAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVNTGLRptRowAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVNTGLRptRowAcctSeg(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVNTGLRptRowAcctSeg
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVNTGLRptRowAcctSeg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVNTGLRptRowAcctSeg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVNTGLRptRowAcctSeg_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVNTGLRptRowAcctSum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVNTGLRptRowAcctSum
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVNTGLRptRowAcctSum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVNTGLRptRowAcctSum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVNTGLRptRowAcctSum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VNTGLRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptMasListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VNTGLRptMasListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptMasRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VNTGLRptMasRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctCorrRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VNTGLRptRowAcctCorrRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctObjRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VNTGLRptRowAcctObjRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VNTGLRptRowAcctRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctSegRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VNTGLRptRowAcctSegRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowAcctSumRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VNTGLRptRowAcctSumRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VNTGLRptRowRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VNTGLRptRowRow] = obj["value"]
      pass

class Erp_Tablesets_VNTGLRptMasListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VNTGLRptMasRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.ShortChar11:str = obj["ShortChar11"]
      self.ShortChar12:str = obj["ShortChar12"]
      self.ShortChar13:str = obj["ShortChar13"]
      self.ShortChar14:str = obj["ShortChar14"]
      self.ShortChar15:str = obj["ShortChar15"]
      self.ShortChar16:str = obj["ShortChar16"]
      self.ShortChar17:str = obj["ShortChar17"]
      self.ShortChar18:str = obj["ShortChar18"]
      self.ShortChar19:str = obj["ShortChar19"]
      self.ShortChar20:str = obj["ShortChar20"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VNTGLRptRowAcctCorrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.ShortChar11:str = obj["ShortChar11"]
      self.ShortChar12:str = obj["ShortChar12"]
      self.ShortChar13:str = obj["ShortChar13"]
      self.ShortChar14:str = obj["ShortChar14"]
      self.ShortChar15:str = obj["ShortChar15"]
      self.ShortChar16:str = obj["ShortChar16"]
      self.ShortChar17:str = obj["ShortChar17"]
      self.ShortChar18:str = obj["ShortChar18"]
      self.ShortChar19:str = obj["ShortChar19"]
      self.ShortChar20:str = obj["ShortChar20"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VNTGLRptRowAcctObjRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.ShortChar11:str = obj["ShortChar11"]
      self.ShortChar12:str = obj["ShortChar12"]
      self.ShortChar13:str = obj["ShortChar13"]
      self.ShortChar14:str = obj["ShortChar14"]
      self.ShortChar15:str = obj["ShortChar15"]
      self.ShortChar16:str = obj["ShortChar16"]
      self.ShortChar17:str = obj["ShortChar17"]
      self.ShortChar18:str = obj["ShortChar18"]
      self.ShortChar19:str = obj["ShortChar19"]
      self.ShortChar20:str = obj["ShortChar20"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VNTGLRptRowAcctRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.ShortChar11:str = obj["ShortChar11"]
      self.ShortChar12:str = obj["ShortChar12"]
      self.ShortChar13:str = obj["ShortChar13"]
      self.ShortChar14:str = obj["ShortChar14"]
      self.ShortChar15:str = obj["ShortChar15"]
      self.ShortChar16:str = obj["ShortChar16"]
      self.ShortChar17:str = obj["ShortChar17"]
      self.ShortChar18:str = obj["ShortChar18"]
      self.ShortChar19:str = obj["ShortChar19"]
      self.ShortChar20:str = obj["ShortChar20"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VNTGLRptRowAcctSegRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.ShortChar11:str = obj["ShortChar11"]
      self.ShortChar12:str = obj["ShortChar12"]
      self.ShortChar13:str = obj["ShortChar13"]
      self.ShortChar14:str = obj["ShortChar14"]
      self.ShortChar15:str = obj["ShortChar15"]
      self.ShortChar16:str = obj["ShortChar16"]
      self.ShortChar17:str = obj["ShortChar17"]
      self.ShortChar18:str = obj["ShortChar18"]
      self.ShortChar19:str = obj["ShortChar19"]
      self.ShortChar20:str = obj["ShortChar20"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VNTGLRptRowAcctSumRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.ShortChar11:str = obj["ShortChar11"]
      self.ShortChar12:str = obj["ShortChar12"]
      self.ShortChar13:str = obj["ShortChar13"]
      self.ShortChar14:str = obj["ShortChar14"]
      self.ShortChar15:str = obj["ShortChar15"]
      self.ShortChar16:str = obj["ShortChar16"]
      self.ShortChar17:str = obj["ShortChar17"]
      self.ShortChar18:str = obj["ShortChar18"]
      self.ShortChar19:str = obj["ShortChar19"]
      self.ShortChar20:str = obj["ShortChar20"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VNTGLRptRowRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.ShortChar11:str = obj["ShortChar11"]
      self.ShortChar12:str = obj["ShortChar12"]
      self.ShortChar13:str = obj["ShortChar13"]
      self.ShortChar14:str = obj["ShortChar14"]
      self.ShortChar15:str = obj["ShortChar15"]
      self.ShortChar16:str = obj["ShortChar16"]
      self.ShortChar17:str = obj["ShortChar17"]
      self.ShortChar18:str = obj["ShortChar18"]
      self.ShortChar19:str = obj["ShortChar19"]
      self.ShortChar20:str = obj["ShortChar20"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   localName
   key2
   """  
   def __init__(self, obj):
      self.localName:str = obj["localName"]
      self.key2:str = obj["key2"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_UpdExtVNTGLRptMasTableset:
   def __init__(self, obj):
      self.VNTGLRptMas:list[Erp_Tablesets_VNTGLRptMasRow] = obj["VNTGLRptMas"]
      self.VNTGLRptRow:list[Erp_Tablesets_VNTGLRptRowRow] = obj["VNTGLRptRow"]
      self.VNTGLRptRowAcctCorr:list[Erp_Tablesets_VNTGLRptRowAcctCorrRow] = obj["VNTGLRptRowAcctCorr"]
      self.VNTGLRptRowAcctObj:list[Erp_Tablesets_VNTGLRptRowAcctObjRow] = obj["VNTGLRptRowAcctObj"]
      self.VNTGLRptRowAcct:list[Erp_Tablesets_VNTGLRptRowAcctRow] = obj["VNTGLRptRowAcct"]
      self.VNTGLRptRowAcctSeg:list[Erp_Tablesets_VNTGLRptRowAcctSegRow] = obj["VNTGLRptRowAcctSeg"]
      self.VNTGLRptRowAcctSum:list[Erp_Tablesets_VNTGLRptRowAcctSumRow] = obj["VNTGLRptRowAcctSum"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_VNTGLRptMasListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VNTGLRptMasListTableset:
   def __init__(self, obj):
      self.VNTGLRptMasList:list[Erp_Tablesets_VNTGLRptMasListRow] = obj["VNTGLRptMasList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_VNTGLRptMasRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.ShortChar11:str = obj["ShortChar11"]
      self.ShortChar12:str = obj["ShortChar12"]
      self.ShortChar13:str = obj["ShortChar13"]
      self.ShortChar14:str = obj["ShortChar14"]
      self.ShortChar15:str = obj["ShortChar15"]
      self.ShortChar16:str = obj["ShortChar16"]
      self.ShortChar17:str = obj["ShortChar17"]
      self.ShortChar18:str = obj["ShortChar18"]
      self.ShortChar19:str = obj["ShortChar19"]
      self.ShortChar20:str = obj["ShortChar20"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VNTGLRptMasTableset:
   def __init__(self, obj):
      self.VNTGLRptMas:list[Erp_Tablesets_VNTGLRptMasRow] = obj["VNTGLRptMas"]
      self.VNTGLRptRow:list[Erp_Tablesets_VNTGLRptRowRow] = obj["VNTGLRptRow"]
      self.VNTGLRptRowAcctCorr:list[Erp_Tablesets_VNTGLRptRowAcctCorrRow] = obj["VNTGLRptRowAcctCorr"]
      self.VNTGLRptRowAcctObj:list[Erp_Tablesets_VNTGLRptRowAcctObjRow] = obj["VNTGLRptRowAcctObj"]
      self.VNTGLRptRowAcct:list[Erp_Tablesets_VNTGLRptRowAcctRow] = obj["VNTGLRptRowAcct"]
      self.VNTGLRptRowAcctSeg:list[Erp_Tablesets_VNTGLRptRowAcctSegRow] = obj["VNTGLRptRowAcctSeg"]
      self.VNTGLRptRowAcctSum:list[Erp_Tablesets_VNTGLRptRowAcctSumRow] = obj["VNTGLRptRowAcctSum"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_VNTGLRptRowAcctCorrRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.ShortChar11:str = obj["ShortChar11"]
      self.ShortChar12:str = obj["ShortChar12"]
      self.ShortChar13:str = obj["ShortChar13"]
      self.ShortChar14:str = obj["ShortChar14"]
      self.ShortChar15:str = obj["ShortChar15"]
      self.ShortChar16:str = obj["ShortChar16"]
      self.ShortChar17:str = obj["ShortChar17"]
      self.ShortChar18:str = obj["ShortChar18"]
      self.ShortChar19:str = obj["ShortChar19"]
      self.ShortChar20:str = obj["ShortChar20"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VNTGLRptRowAcctObjRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.ShortChar11:str = obj["ShortChar11"]
      self.ShortChar12:str = obj["ShortChar12"]
      self.ShortChar13:str = obj["ShortChar13"]
      self.ShortChar14:str = obj["ShortChar14"]
      self.ShortChar15:str = obj["ShortChar15"]
      self.ShortChar16:str = obj["ShortChar16"]
      self.ShortChar17:str = obj["ShortChar17"]
      self.ShortChar18:str = obj["ShortChar18"]
      self.ShortChar19:str = obj["ShortChar19"]
      self.ShortChar20:str = obj["ShortChar20"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VNTGLRptRowAcctRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.ShortChar11:str = obj["ShortChar11"]
      self.ShortChar12:str = obj["ShortChar12"]
      self.ShortChar13:str = obj["ShortChar13"]
      self.ShortChar14:str = obj["ShortChar14"]
      self.ShortChar15:str = obj["ShortChar15"]
      self.ShortChar16:str = obj["ShortChar16"]
      self.ShortChar17:str = obj["ShortChar17"]
      self.ShortChar18:str = obj["ShortChar18"]
      self.ShortChar19:str = obj["ShortChar19"]
      self.ShortChar20:str = obj["ShortChar20"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VNTGLRptRowAcctSegRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.ShortChar11:str = obj["ShortChar11"]
      self.ShortChar12:str = obj["ShortChar12"]
      self.ShortChar13:str = obj["ShortChar13"]
      self.ShortChar14:str = obj["ShortChar14"]
      self.ShortChar15:str = obj["ShortChar15"]
      self.ShortChar16:str = obj["ShortChar16"]
      self.ShortChar17:str = obj["ShortChar17"]
      self.ShortChar18:str = obj["ShortChar18"]
      self.ShortChar19:str = obj["ShortChar19"]
      self.ShortChar20:str = obj["ShortChar20"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VNTGLRptRowAcctSumRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.ShortChar11:str = obj["ShortChar11"]
      self.ShortChar12:str = obj["ShortChar12"]
      self.ShortChar13:str = obj["ShortChar13"]
      self.ShortChar14:str = obj["ShortChar14"]
      self.ShortChar15:str = obj["ShortChar15"]
      self.ShortChar16:str = obj["ShortChar16"]
      self.ShortChar17:str = obj["ShortChar17"]
      self.ShortChar18:str = obj["ShortChar18"]
      self.ShortChar19:str = obj["ShortChar19"]
      self.ShortChar20:str = obj["ShortChar20"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VNTGLRptRowRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.Character07:str = obj["Character07"]
      self.Character08:str = obj["Character08"]
      self.Character09:str = obj["Character09"]
      self.Character10:str = obj["Character10"]
      self.Number01:int = obj["Number01"]
      self.Number02:int = obj["Number02"]
      self.Number03:int = obj["Number03"]
      self.Number04:int = obj["Number04"]
      self.Number05:int = obj["Number05"]
      self.Number06:int = obj["Number06"]
      self.Number07:int = obj["Number07"]
      self.Number08:int = obj["Number08"]
      self.Number09:int = obj["Number09"]
      self.Number10:int = obj["Number10"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.CheckBox02:bool = obj["CheckBox02"]
      self.CheckBox03:bool = obj["CheckBox03"]
      self.CheckBox04:bool = obj["CheckBox04"]
      self.CheckBox05:bool = obj["CheckBox05"]
      self.Number11:int = obj["Number11"]
      self.Number12:int = obj["Number12"]
      self.Number13:int = obj["Number13"]
      self.Number14:int = obj["Number14"]
      self.Number15:int = obj["Number15"]
      self.Number16:int = obj["Number16"]
      self.Number17:int = obj["Number17"]
      self.Number18:int = obj["Number18"]
      self.Number19:int = obj["Number19"]
      self.Number20:int = obj["Number20"]
      self.Date06:str = obj["Date06"]
      self.Date07:str = obj["Date07"]
      self.Date08:str = obj["Date08"]
      self.Date09:str = obj["Date09"]
      self.Date10:str = obj["Date10"]
      self.Date11:str = obj["Date11"]
      self.Date12:str = obj["Date12"]
      self.Date13:str = obj["Date13"]
      self.Date14:str = obj["Date14"]
      self.Date15:str = obj["Date15"]
      self.Date16:str = obj["Date16"]
      self.Date17:str = obj["Date17"]
      self.Date18:str = obj["Date18"]
      self.Date19:str = obj["Date19"]
      self.Date20:str = obj["Date20"]
      self.CheckBox06:bool = obj["CheckBox06"]
      self.CheckBox07:bool = obj["CheckBox07"]
      self.CheckBox08:bool = obj["CheckBox08"]
      self.CheckBox09:bool = obj["CheckBox09"]
      self.CheckBox10:bool = obj["CheckBox10"]
      self.CheckBox11:bool = obj["CheckBox11"]
      self.CheckBox12:bool = obj["CheckBox12"]
      self.CheckBox13:bool = obj["CheckBox13"]
      self.CheckBox14:bool = obj["CheckBox14"]
      self.CheckBox15:bool = obj["CheckBox15"]
      self.CheckBox16:bool = obj["CheckBox16"]
      self.CheckBox17:bool = obj["CheckBox17"]
      self.CheckBox18:bool = obj["CheckBox18"]
      self.CheckBox19:bool = obj["CheckBox19"]
      self.CheckBox20:bool = obj["CheckBox20"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.ShortChar03:str = obj["ShortChar03"]
      self.ShortChar04:str = obj["ShortChar04"]
      self.ShortChar05:str = obj["ShortChar05"]
      self.ShortChar06:str = obj["ShortChar06"]
      self.ShortChar07:str = obj["ShortChar07"]
      self.ShortChar08:str = obj["ShortChar08"]
      self.ShortChar09:str = obj["ShortChar09"]
      self.ShortChar10:str = obj["ShortChar10"]
      self.ShortChar11:str = obj["ShortChar11"]
      self.ShortChar12:str = obj["ShortChar12"]
      self.ShortChar13:str = obj["ShortChar13"]
      self.ShortChar14:str = obj["ShortChar14"]
      self.ShortChar15:str = obj["ShortChar15"]
      self.ShortChar16:str = obj["ShortChar16"]
      self.ShortChar17:str = obj["ShortChar17"]
      self.ShortChar18:str = obj["ShortChar18"]
      self.ShortChar19:str = obj["ShortChar19"]
      self.ShortChar20:str = obj["ShortChar20"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetByID_input:
   """ Required : 
   localName
   key2
   """  
   def __init__(self, obj):
      self.localName:str = obj["localName"]
      self.key2:str = obj["key2"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VNTGLRptMasTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_VNTGLRptMasTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_VNTGLRptMasTableset] = obj["returnObj"]
      pass

class GetDataComboAttributeFont_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.listDataAttributeFont:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDataComboItemValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.listDataItemValue:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDataComboReportTemplate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.listDataReportTemplate:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDataComboRowAccountType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.listDataRowAcctType:str = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_VNTGLRptMasListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewVNTGLRptMas_input:
   """ Required : 
   ds
   localName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VNTGLRptMasTableset] = obj["ds"]
      self.localName:str = obj["localName"]
      pass

class GetNewVNTGLRptMas_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VNTGLRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVNTGLRptRowAcctCorr_input:
   """ Required : 
   ds
   localName
   key2
   key3
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VNTGLRptMasTableset] = obj["ds"]
      self.localName:str = obj["localName"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      pass

class GetNewVNTGLRptRowAcctCorr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VNTGLRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVNTGLRptRowAcctObj_input:
   """ Required : 
   ds
   localName
   key2
   key3
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VNTGLRptMasTableset] = obj["ds"]
      self.localName:str = obj["localName"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      pass

class GetNewVNTGLRptRowAcctObj_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VNTGLRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVNTGLRptRowAcctSeg_input:
   """ Required : 
   ds
   localName
   key2
   key3
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VNTGLRptMasTableset] = obj["ds"]
      self.localName:str = obj["localName"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      pass

class GetNewVNTGLRptRowAcctSeg_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VNTGLRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVNTGLRptRowAcctSum_input:
   """ Required : 
   ds
   localName
   key2
   key3
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VNTGLRptMasTableset] = obj["ds"]
      self.localName:str = obj["localName"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      pass

class GetNewVNTGLRptRowAcctSum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VNTGLRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVNTGLRptRowAcct_input:
   """ Required : 
   ds
   localName
   key2
   key3
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VNTGLRptMasTableset] = obj["ds"]
      self.localName:str = obj["localName"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      pass

class GetNewVNTGLRptRowAcct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VNTGLRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVNTGLRptRow_input:
   """ Required : 
   ds
   localName
   key2
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VNTGLRptMasTableset] = obj["ds"]
      self.localName:str = obj["localName"]
      self.key2:str = obj["key2"]
      pass

class GetNewVNTGLRptRow_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VNTGLRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseVNTGLRptMas
   whereClauseVNTGLRptRow
   whereClauseVNTGLRptRowAcctCorr
   whereClauseVNTGLRptRowAcctObj
   whereClauseVNTGLRptRowAcct
   whereClauseVNTGLRptRowAcctSeg
   whereClauseVNTGLRptRowAcctSum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseVNTGLRptMas:str = obj["whereClauseVNTGLRptMas"]
      self.whereClauseVNTGLRptRow:str = obj["whereClauseVNTGLRptRow"]
      self.whereClauseVNTGLRptRowAcctCorr:str = obj["whereClauseVNTGLRptRowAcctCorr"]
      self.whereClauseVNTGLRptRowAcctObj:str = obj["whereClauseVNTGLRptRowAcctObj"]
      self.whereClauseVNTGLRptRowAcct:str = obj["whereClauseVNTGLRptRowAcct"]
      self.whereClauseVNTGLRptRowAcctSeg:str = obj["whereClauseVNTGLRptRowAcctSeg"]
      self.whereClauseVNTGLRptRowAcctSum:str = obj["whereClauseVNTGLRptRowAcctSum"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VNTGLRptMasTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtVNTGLRptMasTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtVNTGLRptMasTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VNTGLRptMasTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VNTGLRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

