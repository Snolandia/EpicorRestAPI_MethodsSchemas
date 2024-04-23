import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.FAssetSvc
# Description: Fixed Asset module
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_FAssets(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FAssets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FAssets
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAssetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssets",headers=creds) as resp:
           return await resp.json()

async def post_FAssets(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FAssets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAssetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FAssetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssets", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FAssets_Company_AssetNum(Company, AssetNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FAsset item
   Description: Calls GetByID to retrieve the FAsset item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAsset
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAssetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssets(" + Company + "," + AssetNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FAssets_Company_AssetNum(Company, AssetNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FAsset for the service
   Description: Calls UpdateExt to update FAsset. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FAsset
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAssetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssets(" + Company + "," + AssetNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FAssets_Company_AssetNum(Company, AssetNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FAsset item
   Description: Call UpdateExt to delete FAsset item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FAsset
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssets(" + Company + "," + AssetNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_FAssets_Company_AssetNum_ChildAssets(Company, AssetNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ChildAssets items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ChildAssets1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ChildAssetsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssets(" + Company + "," + AssetNum + ")/ChildAssets",headers=creds) as resp:
           return await resp.json()

async def get_FAssets_Company_AssetNum_ChildAssets_Company_AssetNum(Company, AssetNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ChildAsset item
   Description: Calls GetByID to retrieve the ChildAsset item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ChildAsset1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ChildAssetsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssets(" + Company + "," + AssetNum + ")/ChildAssets(" + Company + "," + AssetNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_FAssets_Company_AssetNum_FAssetDtls(Company, AssetNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FAssetDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FAssetDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAssetDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssets(" + Company + "," + AssetNum + ")/FAssetDtls",headers=creds) as resp:
           return await resp.json()

async def get_FAssets_Company_AssetNum_FAssetDtls_Company_AssetNum_AssetRegID(Company, AssetNum, AssetRegID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FAssetDtl item
   Description: Calls GetByID to retrieve the FAssetDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAssetDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAssetDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssets(" + Company + "," + AssetNum + ")/FAssetDtls(" + Company + "," + AssetNum + "," + AssetRegID + ")",headers=creds) as resp:
           return await resp.json()

async def get_FAssets_Company_AssetNum_FAssetAttches(Company, AssetNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FAssetAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FAssetAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAssetAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssets(" + Company + "," + AssetNum + ")/FAssetAttches",headers=creds) as resp:
           return await resp.json()

async def get_FAssets_Company_AssetNum_FAssetAttches_Company_AssetNum_DrawingSeq(Company, AssetNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FAssetAttch item
   Description: Calls GetByID to retrieve the FAssetAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAssetAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAssetAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssets(" + Company + "," + AssetNum + ")/FAssetAttches(" + Company + "," + AssetNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ChildAssets(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ChildAssets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ChildAssets
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ChildAssetsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/ChildAssets",headers=creds) as resp:
           return await resp.json()

async def post_ChildAssets(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ChildAssets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ChildAssetsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ChildAssetsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/ChildAssets", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ChildAssets_Company_AssetNum(Company, AssetNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ChildAsset item
   Description: Calls GetByID to retrieve the ChildAsset item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ChildAsset
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ChildAssetsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/ChildAssets(" + Company + "," + AssetNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ChildAssets_Company_AssetNum(Company, AssetNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ChildAsset for the service
   Description: Calls UpdateExt to update ChildAsset. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ChildAsset
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ChildAssetsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/ChildAssets(" + Company + "," + AssetNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ChildAssets_Company_AssetNum(Company, AssetNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ChildAsset item
   Description: Call UpdateExt to delete ChildAsset item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ChildAsset
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/ChildAssets(" + Company + "," + AssetNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_FAssetDtls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FAssetDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FAssetDtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAssetDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtls",headers=creds) as resp:
           return await resp.json()

async def post_FAssetDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FAssetDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAssetDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FAssetDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FAssetDtls_Company_AssetNum_AssetRegID(Company, AssetNum, AssetRegID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FAssetDtl item
   Description: Calls GetByID to retrieve the FAssetDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAssetDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAssetDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtls(" + Company + "," + AssetNum + "," + AssetRegID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FAssetDtls_Company_AssetNum_AssetRegID(Company, AssetNum, AssetRegID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FAssetDtl for the service
   Description: Calls UpdateExt to update FAssetDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FAssetDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAssetDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtls(" + Company + "," + AssetNum + "," + AssetRegID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FAssetDtls_Company_AssetNum_AssetRegID(Company, AssetNum, AssetRegID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FAssetDtl item
   Description: Call UpdateExt to delete FAssetDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FAssetDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtls(" + Company + "," + AssetNum + "," + AssetRegID + ")",headers=creds) as resp:
           return await resp.json()

async def get_FAssetDtls_Company_AssetNum_AssetRegID_FAssetDtlAttches(Company, AssetNum, AssetRegID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FAssetDtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FAssetDtlAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAssetDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtls(" + Company + "," + AssetNum + "," + AssetRegID + ")/FAssetDtlAttches",headers=creds) as resp:
           return await resp.json()

async def get_FAssetDtls_Company_AssetNum_AssetRegID_FAssetDtlAttches_Company_AssetNum_AssetRegID_DrawingSeq(Company, AssetNum, AssetRegID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FAssetDtlAttch item
   Description: Calls GetByID to retrieve the FAssetDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAssetDtlAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAssetDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtls(" + Company + "," + AssetNum + "," + AssetRegID + ")/FAssetDtlAttches(" + Company + "," + AssetNum + "," + AssetRegID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_FAssetDtlAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FAssetDtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FAssetDtlAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAssetDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtlAttches",headers=creds) as resp:
           return await resp.json()

async def post_FAssetDtlAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FAssetDtlAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAssetDtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FAssetDtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtlAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FAssetDtlAttches_Company_AssetNum_AssetRegID_DrawingSeq(Company, AssetNum, AssetRegID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FAssetDtlAttch item
   Description: Calls GetByID to retrieve the FAssetDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAssetDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAssetDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtlAttches(" + Company + "," + AssetNum + "," + AssetRegID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FAssetDtlAttches_Company_AssetNum_AssetRegID_DrawingSeq(Company, AssetNum, AssetRegID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FAssetDtlAttch for the service
   Description: Calls UpdateExt to update FAssetDtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FAssetDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAssetDtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtlAttches(" + Company + "," + AssetNum + "," + AssetRegID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FAssetDtlAttches_Company_AssetNum_AssetRegID_DrawingSeq(Company, AssetNum, AssetRegID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FAssetDtlAttch item
   Description: Call UpdateExt to delete FAssetDtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FAssetDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetDtlAttches(" + Company + "," + AssetNum + "," + AssetRegID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_FAssetAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FAssetAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FAssetAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAssetAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetAttches",headers=creds) as resp:
           return await resp.json()

async def post_FAssetAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FAssetAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAssetAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FAssetAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FAssetAttches_Company_AssetNum_DrawingSeq(Company, AssetNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FAssetAttch item
   Description: Calls GetByID to retrieve the FAssetAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAssetAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAssetAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetAttches(" + Company + "," + AssetNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FAssetAttches_Company_AssetNum_DrawingSeq(Company, AssetNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FAssetAttch for the service
   Description: Calls UpdateExt to update FAssetAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FAssetAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAssetAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetAttches(" + Company + "," + AssetNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FAssetAttches_Company_AssetNum_DrawingSeq(Company, AssetNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FAssetAttch item
   Description: Call UpdateExt to delete FAssetAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FAssetAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/FAssetAttches(" + Company + "," + AssetNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAssetListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseFAsset, whereClauseFAssetAttch, whereClauseChildAssets, whereClauseFAssetDtl, whereClauseFAssetDtlAttch, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseFAsset=" + whereClauseFAsset
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFAssetAttch=" + whereClauseFAssetAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseChildAssets=" + whereClauseChildAssets
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFAssetDtl=" + whereClauseFAssetDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFAssetDtlAttch=" + whereClauseFAssetDtlAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(assetNum, epicorHeaders = None):
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
   params += "assetNum=" + assetNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetClientFileName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetClientFileName
   OperationID: GetClientFileName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetClientFileName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetClientFileName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalcTaxAmtLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalcTaxAmtLine
   Description: Called to calculate the Tax for the AP Invoice Line
   OperationID: CalcTaxAmtLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcTaxAmtLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcTaxAmtLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeAssetMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeAssetMethod
   Description: Update AssetMethod when a different AssetMethod is selected.
   OperationID: ChangeAssetMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAssetMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAssetMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeAssetRegister(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeAssetRegister
   Description: Update AssetRegister when a different AssetRegister is selected.
   OperationID: ChangeAssetRegister
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAssetRegister_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAssetRegister_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreDuplicate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreDuplicate
   Description: Performs validations before Asset duplication
   OperationID: PreDuplicate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreDuplicate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreDuplicate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Duplicate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Duplicate
   Description: Duplicate fixed asset.
   OperationID: Duplicate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Duplicate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Duplicate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportData(epicorHeaders = None):
   """  
   Summary: Invoke method ExportData
   Description: ExportData
   OperationID: ExportData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetChildAssets(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetChildAssets
   Description: Get the ChildAsset records for a parent asset.
   OperationID: GetChildAssets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetChildAssets_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetChildAssets_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFAssetByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFAssetByID
   Description: Get Fixed Asset by ID
   OperationID: GetFAssetByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFAssetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFAssetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewChildAsset(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewChildAsset
   Description: To be called when a new ChildAssets row is needed.
   OperationID: GetNewChildAsset
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewChildAsset_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewChildAsset_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportData
   OperationID: ImportData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveAcquiredDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveAcquiredDate
   Description: The purpose of this code is to assign the commissioned date to the
acquired date for a new fixed asset. (Only run this code on a new fixed asset)
Called on leave of Acquired Date field.
   OperationID: LeaveAcquiredDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveAcquiredDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveAcquiredDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveChildAssetNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveChildAssetNum
   Description: To be called on leave of (Child) AssetNum field.
   OperationID: LeaveChildAssetNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveChildAssetNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveChildAssetNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveInsPremium(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveInsPremium
   Description: To be called on leave of FAsset.InsurancePremium field
   OperationID: LeaveInsPremium
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveInsPremium_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveInsPremium_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveInsValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveInsValue
   Description: To be called on leave of FAsset.InsuranceValue field
   OperationID: LeaveInsValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveInsValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveInsValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveInvoiceLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveInvoiceLine
   Description: Called on the leave of Invoice Line
   OperationID: LeaveInvoiceLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveInvoiceLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveInvoiceLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveInvoiceNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveInvoiceNum
   Description: Called on the leave of Invoice Number
   OperationID: LeaveInvoiceNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveJobNum
   Description: To be called on leave of Job Number field
   OperationID: LeaveJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveLeaseValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveLeaseValue
   Description: To be called on leave of FAsset.LeaseValue field
   OperationID: LeaveLeaseValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveLeaseValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveLeaseValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeavePONum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeavePONum
   Description: To be called on leave of VendorID field
   OperationID: LeavePONum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeavePONum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeavePONum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveReplaceValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveReplaceValue
   Description: To be called on leave of ReplaceValue field
   OperationID: LeaveReplaceValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveReplaceValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveReplaceValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveResidualValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveResidualValue
   Description: To be called on leave of ResidualValue field
   OperationID: LeaveResidualValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveResidualValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveResidualValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveVendorID
   Description: To be called on leave of VendorID field
   OperationID: LeaveVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PostedDepExist(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PostedDepExist
   Description: Returns true if the asset registry has posted depreciation transactions.
   OperationID: PostedDepExist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostedDepExist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostedDepExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TestAllowDelete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TestAllowDelete
   Description: This procedure is to provide a check before deleting the records
You can use this method to provide a message to the user of this fact and provide a confirmation dialog. This is
intended to be called before the delete procedure.
If there are existing records SureMsg will contain a translated text message
which can be used to display in your message dialog.  Otherwise it returns blanks and there is no need to provide a
dialog.
   OperationID: TestAllowDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestAllowDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestAllowDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TestParentChildIntegrity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TestParentChildIntegrity
   Description: This procedure should be called to check for parent\child integrity.
The procedure throws an exception if the relation is invalid.
   OperationID: TestParentChildIntegrity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestParentChildIntegrity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestParentChildIntegrity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCommodityCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCommodityCode
   Description: Validate entered Commodity Code
   OperationID: OnChangeCommodityCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCommodityCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCommodityCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportToDS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportToDS
   Description: Import Logic
   OperationID: ImportToDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportToDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportToDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportProcess(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportProcess
   Description: Export Process
   OperationID: ExportProcess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportProcess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportProcess_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFAsset(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFAsset
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFAsset
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFAsset_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFAsset_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFAssetAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFAssetAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFAssetAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFAssetAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFAssetAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFAssetDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFAssetDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFAssetDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFAssetDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFAssetDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFAssetDtlAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFAssetDtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFAssetDtlAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFAssetDtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFAssetDtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FAssetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ChildAssetsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ChildAssetsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FAssetAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetDtlAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FAssetDtlAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FAssetDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FAssetListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAssetRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FAssetRow] = obj["value"]
      pass

class Erp_Tablesets_ChildAssetsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset Number  """  
      self.AssetDescription:str = obj["AssetDescription"]
      """  Asset Description  """  
      self.ParentAsset:str = obj["ParentAsset"]
      """  Parent Asset Number  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.AssetSeq:int = obj["AssetSeq"]
      """  Asset Sequence  """  
      self.ParentAssetSeq:int = obj["ParentAssetSeq"]
      """  Parent Asset Sequence  """  
      self.AssetStatus:str = obj["AssetStatus"]
      self.TagNum:str = obj["TagNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAssetAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.AssetNum:str = obj["AssetNum"]
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

class Erp_Tablesets_FAssetDtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.AssetNum:str = obj["AssetNum"]
      self.AssetRegID:str = obj["AssetRegID"]
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

class Erp_Tablesets_FAssetDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the asset.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Identifier of the asset  """  
      self.AssetRegID:str = obj["AssetRegID"]
      """  Identifier of the Asset Register.  """  
      self.AdditionSpread:bool = obj["AdditionSpread"]
      """  Flag to indicate that calculated depreciation between the fiscal period of asset commission date and the first open fiscal period should be distributed over all open remaining periods of the first depreciation year or when false then the calculated depreciation will be applied to the first open fiscal period.  """  
      self.SpreadCode:str = obj["SpreadCode"]
      """  Identifier of the spread code table that will be used for the Addition Spread option.  """  
      self.LifeModifier:str = obj["LifeModifier"]
      """  In case of life depreciation method the life modifier expresses the unit of measure of life. Values are: Periods and Years.  """  
      self.AnnualDepRate:int = obj["AnnualDepRate"]
      """  The Depreciation Rate that will be used to calculate the Annual Charge.  """  
      self.AssetLife:int = obj["AssetLife"]
      """  Number of periods or years - unit defined in the Life Modifier.  """  
      self.CYOpenDepn:int = obj["CYOpenDepn"]
      """  Current year opening depreciation  """  
      self.CYOpenBookValue:int = obj["CYOpenBookValue"]
      """  Current year opening bookvalue  """  
      self.CYOpenGrantDepn:int = obj["CYOpenGrantDepn"]
      """  Current year opening grant depreciation  """  
      self.CYOpenGrantBookValue:int = obj["CYOpenGrantBookValue"]
      """  Current year opening grant bookvalue  """  
      self.CYAddPrevDepn:int = obj["CYAddPrevDepn"]
      """  Depreciation applied in previous years through addition this year.  """  
      self.CYAddCurrDepn:int = obj["CYAddCurrDepn"]
      """  Current year depreciation  """  
      self.CYAddBookvalue:int = obj["CYAddBookvalue"]
      """  Current year Addition Bookvalue is the addition bookvalue added to the asset  this year.  """  
      self.CYDispPrevDepn:int = obj["CYDispPrevDepn"]
      """  Depreciation applied in previous years through disposal this year.  """  
      self.CYDispCurrDepn:int = obj["CYDispCurrDepn"]
      """  Depreciation applied this year through addition this year.  """  
      self.CYDispBookValue:int = obj["CYDispBookValue"]
      """  Current year disposal bookvalue is the disposal bookvalue disposed from the asset this year.  """  
      self.CurrentPrevYearDepn:int = obj["CurrentPrevYearDepn"]
      """  Depreciated in previous years  """  
      self.CurrentPostedDepn:int = obj["CurrentPostedDepn"]
      """  Depreciated (and posted) in the current year.  """  
      self.CurrentBookvalue:int = obj["CurrentBookvalue"]
      """  The current bookvalue.  """  
      self.CurrentUnpostedDepn:int = obj["CurrentUnpostedDepn"]
      """  Depreciations open for this year.  """  
      self.CurrentYEBookvalue:int = obj["CurrentYEBookvalue"]
      """  The projected bookvalue at the end of this year.  """  
      self.AssetMethod:str = obj["AssetMethod"]
      """  Identifier of the depreciation method table.  """  
      self.BookID:str = obj["BookID"]
      """  The G/L Book that will be used when posting asset depreciations against this register.  """  
      self.CalendarID:str = obj["CalendarID"]
      """  Identifies the Asset Calendar used when posting asset activities.  This calendar could be different from the G/L Book Fiscal Calendar.  """  
      self.DepConvention:str = obj["DepConvention"]
      """  Convention used for the depreciation calculation of the asset.  This will determine how depreciation is prorated for the year in which the asset is placed in service.  Valid values are: "HY" (Half Year); "MM" (Mid Month); "QR" (Quarter); "MQ" (Mid Quarter); "FM" (Full Month); "EM" (Entire Month); "SD" (Service Date), "NM" (Next Month), and "AD" (Acquisition Date).  This field can be blank.  """  
      self.RetroAdjust:bool = obj["RetroAdjust"]
      """  Flag to indicate if the changes in asset depreciation costs, due to an adjustment of asset cost or depreciation parameters, will affect the current year depreciation calculation.  """  
      self.ProdUnitSpread:str = obj["ProdUnitSpread"]
      """  Production Unit Spread Code.  """  
      self.TotalProdUnit:int = obj["TotalProdUnit"]
      """  Total Production Units.  This could be the total production units per Year or per Period depending on the depreciation charge basis of the asset depreciation method.  """  
      self.AnnualFixedValue:int = obj["AnnualFixedValue"]
      """  The Fixed Value that will be used as the Annual Charge amount during the asset depreciation calculation.  This field is only used if the depreciation method is set up to 'Use Fixed Value' for the annual charge calculation.  """  
      self.AnnualSpread:str = obj["AnnualSpread"]
      """  Annual Charge Spread Code  """  
      self.PeriodFixedValue:int = obj["PeriodFixedValue"]
      """  The Fixed Value that will be used as the Period Charge amount during the asset period depreciation calculation.  This field is only used if the depreciation method is set up to 'Use Fixed Value' for the period charge calculation.  """  
      self.PeriodSpread:str = obj["PeriodSpread"]
      """  Period Charge Spread  """  
      self.PeriodRateSpread:str = obj["PeriodRateSpread"]
      """  Spread Code used to determine the spread values used when prorating Annual Charge.  """  
      self.FinalSpread:str = obj["FinalSpread"]
      """  Final Spread Code  """  
      self.MethodSwitched:bool = obj["MethodSwitched"]
      """  Indicates if this asset register detail has already switched or used the alternate depreciation method. An asset register is only allowed to switch to an alternate depreciation method once and cannot switch back to original method.  """  
      self.AltAssetMethod:str = obj["AltAssetMethod"]
      """  Alternate Depreciation Method  """  
      self.DocCurrentPrevYearDepn:int = obj["DocCurrentPrevYearDepn"]
      """  Depreciated in previous years  """  
      self.DocCurrentPostedDepn:int = obj["DocCurrentPostedDepn"]
      """  Depreciated (and posted) in the current year.  """  
      self.DocCurrentBookvalue:int = obj["DocCurrentBookvalue"]
      """  The current bookvalue.  """  
      self.DocCurrentUnpostedDepn:int = obj["DocCurrentUnpostedDepn"]
      """  Depreciations open for this year.  """  
      self.DocCurrentYEBookvalue:int = obj["DocCurrentYEBookvalue"]
      """  The projected bookvalue at the end of this year.  """  
      self.Rpt1CurrentPrevYearDepn:int = obj["Rpt1CurrentPrevYearDepn"]
      """  Depreciated in previous years  """  
      self.Rpt1CurrentPostedDepn:int = obj["Rpt1CurrentPostedDepn"]
      """  Depreciated (and posted) in the current year.  """  
      self.Rpt1CurrentBookvalue:int = obj["Rpt1CurrentBookvalue"]
      """  The current bookvalue.  """  
      self.Rpt1CurrentUnpostedDepn:int = obj["Rpt1CurrentUnpostedDepn"]
      """  Depreciations open for this year.  """  
      self.Rpt1CurrentYEBookvalue:int = obj["Rpt1CurrentYEBookvalue"]
      """  The projected bookvalue at the end of this year.  """  
      self.Rpt2CurrentPrevYearDepn:int = obj["Rpt2CurrentPrevYearDepn"]
      """  Depreciated in previous years  """  
      self.Rpt2CurrentPostedDepn:int = obj["Rpt2CurrentPostedDepn"]
      """  Depreciated (and posted) in the current year.  """  
      self.Rpt2CurrentBookvalue:int = obj["Rpt2CurrentBookvalue"]
      """  The current bookvalue.  """  
      self.Rpt2CurrentUnpostedDepn:int = obj["Rpt2CurrentUnpostedDepn"]
      """  Depreciations open for this year.  """  
      self.Rpt2CurrentYEBookvalue:int = obj["Rpt2CurrentYEBookvalue"]
      """  The projected bookvalue at the end of this year.  """  
      self.Rpt3CurrentPrevYearDepn:int = obj["Rpt3CurrentPrevYearDepn"]
      """  Depreciated in previous years  """  
      self.Rpt3CurrentPostedDepn:int = obj["Rpt3CurrentPostedDepn"]
      """  Depreciated (and posted) in the current year.  """  
      self.Rpt3CurrentBookvalue:int = obj["Rpt3CurrentBookvalue"]
      """  The current bookvalue.  """  
      self.Rpt3CurrentUnpostedDepn:int = obj["Rpt3CurrentUnpostedDepn"]
      """  Depreciations open for this year.  """  
      self.Rpt3CurrentYEBookvalue:int = obj["Rpt3CurrentYEBookvalue"]
      """  The projected bookvalue at the end of this year.  """  
      self.UseFinalSpread:bool = obj["UseFinalSpread"]
      """  Flag to indicate that the total of depreciations in the last year of depreciation should be distributed over all fiscal periods of the last year.  """  
      self.DepRecalcNeeded:bool = obj["DepRecalcNeeded"]
      """  System maintained field.  Indicates that asset depreciation needs to be recalculated for this depreciation method.  """  
      self.CurrentGrantPYDepn:int = obj["CurrentGrantPYDepn"]
      """  Grant Depreciation in previous years  """  
      self.CurrentGrantPostedDepn:int = obj["CurrentGrantPostedDepn"]
      """  Grant Depreciation (and posted) in the current year.  """  
      self.CurrentGrantBookValue:int = obj["CurrentGrantBookValue"]
      """  The current grant book value.  """  
      self.CurrentGrantUnpostedDepn:int = obj["CurrentGrantUnpostedDepn"]
      """  Grant Depreciations open for this year.  """  
      self.CurrentGrantYEBookValue:int = obj["CurrentGrantYEBookValue"]
      """  The projected grant bookvalue at the end of this year.  """  
      self.DocCurrentGrantPYDepn:int = obj["DocCurrentGrantPYDepn"]
      """  Grant Depreciation in previous years  """  
      self.DocCurrentGrantPostedDepn:int = obj["DocCurrentGrantPostedDepn"]
      """  Grant Depreciation (and posted) in the current year.  """  
      self.DocCurrentGrantBookValue:int = obj["DocCurrentGrantBookValue"]
      """  The current grant book value.  """  
      self.DocCurrentGrantUnpostedDepn:int = obj["DocCurrentGrantUnpostedDepn"]
      """  Grant Depreciations open for this year.  """  
      self.DocCurrentGrantYEBookValue:int = obj["DocCurrentGrantYEBookValue"]
      """  The projected grant bookvalue at the end of this year.  """  
      self.Rpt1CurrentGrantPYDepn:int = obj["Rpt1CurrentGrantPYDepn"]
      """  Grant Depreciation in previous years  """  
      self.Rpt1CurrentGrantPostedDepn:int = obj["Rpt1CurrentGrantPostedDepn"]
      """  Grant Depreciation (and posted) in the current year.  """  
      self.Rpt1CurrentGrantBookValue:int = obj["Rpt1CurrentGrantBookValue"]
      """  The current grant book value.  """  
      self.Rpt1CurrentGrantUnpostedDepn:int = obj["Rpt1CurrentGrantUnpostedDepn"]
      """  Grant Depreciations open for this year.  """  
      self.Rpt1CurrentGrantYEBookValue:int = obj["Rpt1CurrentGrantYEBookValue"]
      """  The projected grant bookvalue at the end of this year.  """  
      self.Rpt2CurrentGrantPYDepn:int = obj["Rpt2CurrentGrantPYDepn"]
      """  Grant Depreciation in previous years  """  
      self.Rpt2CurrentGrantPostedDepn:int = obj["Rpt2CurrentGrantPostedDepn"]
      """  Grant Depreciation (and posted) in the current year.  """  
      self.Rpt2CurrentGrantBookValue:int = obj["Rpt2CurrentGrantBookValue"]
      """  The current grant book value.  """  
      self.Rpt2CurrentGrantUnpostedDepn:int = obj["Rpt2CurrentGrantUnpostedDepn"]
      """  Grant Depreciations open for this year.  """  
      self.Rpt2CurrentGrantYEBookValue:int = obj["Rpt2CurrentGrantYEBookValue"]
      """  The projected grant bookvalue at the end of this year.  """  
      self.Rpt3CurrentGrantPYDepn:int = obj["Rpt3CurrentGrantPYDepn"]
      """  Grant Depreciation in previous years  """  
      self.Rpt3CurrentGrantPostedDepn:int = obj["Rpt3CurrentGrantPostedDepn"]
      """  Grant Depreciation (and posted) in the current year.  """  
      self.Rpt3CurrentGrantBookValue:int = obj["Rpt3CurrentGrantBookValue"]
      """  The current grant book value.  """  
      self.Rpt3CurrentGrantUnpostedDepn:int = obj["Rpt3CurrentGrantUnpostedDepn"]
      """  Grant Depreciations open for this year.  """  
      self.Rpt3CurrentGrantYEBookValue:int = obj["Rpt3CurrentGrantYEBookValue"]
      """  The projected grant bookvalue at the end of this year.  """  
      self.DocCYOpenBookValue:int = obj["DocCYOpenBookValue"]
      """  Current year opening bookvalue  """  
      self.DocCYAddPrevDepn:int = obj["DocCYAddPrevDepn"]
      """  Previous years addition depreciation  """  
      self.DocCYAddCurrDepn:int = obj["DocCYAddCurrDepn"]
      """  Current year addition depreciation  """  
      self.DocCYAddBookValue:int = obj["DocCYAddBookValue"]
      """  Current year Addition Bookvalue is the addition bookvalue added to the asset  this year.  """  
      self.DocCYDispPrevDepn:int = obj["DocCYDispPrevDepn"]
      """  Previous years Disposal depreciation  """  
      self.DocCYDispCurrDepn:int = obj["DocCYDispCurrDepn"]
      """  Current year Disposal depreciation  """  
      self.DocCYDispBookValue:int = obj["DocCYDispBookValue"]
      """  Current year disposal bookvalue is the disposal bookvalue disposed from the asset this year.  """  
      self.Rpt1CYOpenBookValue:int = obj["Rpt1CYOpenBookValue"]
      """  Current year opening bookvalue  """  
      self.Rpt1CYAddPrevDepn:int = obj["Rpt1CYAddPrevDepn"]
      """  Previous years Addition depreciation  """  
      self.Rpt1CYAddCurrDepn:int = obj["Rpt1CYAddCurrDepn"]
      """  Current year Addition depreciation  """  
      self.Rpt1CYAddBookValue:int = obj["Rpt1CYAddBookValue"]
      """  Current year Addition Bookvalue is the addition bookvalue added to the asset  this year.  """  
      self.Rpt1CYDispPrevDepn:int = obj["Rpt1CYDispPrevDepn"]
      """  Previous years Disposal depreciation  """  
      self.Rpt1CYDispCurrDepn:int = obj["Rpt1CYDispCurrDepn"]
      """  Current year Disposal depreciation  """  
      self.Rpt1CYDispBookValue:int = obj["Rpt1CYDispBookValue"]
      """  Current year disposal bookvalue is the disposal bookvalue disposed from the asset this year.  """  
      self.Rpt2CYOpenBookValue:int = obj["Rpt2CYOpenBookValue"]
      """  Current year opening bookvalue  """  
      self.Rpt2CYAddPrevDepn:int = obj["Rpt2CYAddPrevDepn"]
      """  Previous years Addition depreciation  """  
      self.Rpt2CYAddCurrDepn:int = obj["Rpt2CYAddCurrDepn"]
      """  Current year Addition depreciation  """  
      self.Rpt2CYAddBookValue:int = obj["Rpt2CYAddBookValue"]
      """  Current year Addition Bookvalue is the addition bookvalue added to the asset  this year.  """  
      self.Rpt2CYDispPrevDepn:int = obj["Rpt2CYDispPrevDepn"]
      """  Previous years Disposal depreciation  """  
      self.Rpt2CYDispCurrDepn:int = obj["Rpt2CYDispCurrDepn"]
      """  Current year Disposal depreciation  """  
      self.Rpt2CYDispBookValue:int = obj["Rpt2CYDispBookValue"]
      """  Current year disposal bookvalue is the disposal bookvalue disposed from the asset this year.  """  
      self.Rpt3CYOpenBookValue:int = obj["Rpt3CYOpenBookValue"]
      """  Current year opening bookvalue  """  
      self.Rpt3CYAddPrevDepn:int = obj["Rpt3CYAddPrevDepn"]
      """  Previous years Addition depreciation  """  
      self.Rpt3CYAddCurrDepn:int = obj["Rpt3CYAddCurrDepn"]
      """  Current year Addition depreciation  """  
      self.Rpt3CYAddBookValue:int = obj["Rpt3CYAddBookValue"]
      """  Current year Addition Bookvalue is the addition bookvalue added to the asset  this year.  """  
      self.Rpt3CYDispPrevDepn:int = obj["Rpt3CYDispPrevDepn"]
      """  Previous years Disposal depreciation  """  
      self.Rpt3CYDispCurrDepn:int = obj["Rpt3CYDispCurrDepn"]
      """  Current year Disposal depreciation  """  
      self.Rpt3CYDispBookValue:int = obj["Rpt3CYDispBookValue"]
      """  Current year disposal bookvalue is the disposal bookvalue disposed from the asset this year.  """  
      self.DocCYOpenGrantDepn:int = obj["DocCYOpenGrantDepn"]
      """  Current year opening grant depreciation  """  
      self.Rpt1CYOpenGrantDepn:int = obj["Rpt1CYOpenGrantDepn"]
      """  Current year opening grant depreciation  """  
      self.Rpt2CYOpenGrantDepn:int = obj["Rpt2CYOpenGrantDepn"]
      """  Current year opening grant depreciation  """  
      self.Rpt3CYOpenGrantDepn:int = obj["Rpt3CYOpenGrantDepn"]
      """  Current year opening grant depreciation  """  
      self.DepRecalcDate:str = obj["DepRecalcDate"]
      """  The last depreciation recalculation apply date.  This is the date used to get the exchange rate for the depreciation calculation process.  """  
      self.InitBookValue:int = obj["InitBookValue"]
      """  This is the initial book value of the entire asset depreciation schedule.  """  
      self.DocInitBookValue:int = obj["DocInitBookValue"]
      """  This is the Initial book value of the entire asset depreciation schedule.  """  
      self.Rpt1InitBookValue:int = obj["Rpt1InitBookValue"]
      """  This is the Initial book value of the entire asset depreciation schedule.  """  
      self.Rpt2InitBookValue:int = obj["Rpt2InitBookValue"]
      """  This is the Initial book value of the entire asset depreciation schedule.  """  
      self.Rpt3InitBookValue:int = obj["Rpt3InitBookValue"]
      """  This is the Initial book value of the entire asset depreciation schedule.  """  
      self.InitGrantBookValue:int = obj["InitGrantBookValue"]
      """  This is the Initial grant book value of the entire asset depreciation schedule.  """  
      self.DocInitGrantBookValue:int = obj["DocInitGrantBookValue"]
      """  This is the Initial grant book value of the entire asset depreciation schedule.  """  
      self.Rpt1InitGrantBookValue:int = obj["Rpt1InitGrantBookValue"]
      """  This is the Initial grant book value of the entire asset depreciation schedule.  """  
      self.Rpt2InitGrantBookValue:int = obj["Rpt2InitGrantBookValue"]
      """  This is the Initial grant book value of the entire asset depreciation schedule.  """  
      self.Rpt3InitGrantBookValue:int = obj["Rpt3InitGrantBookValue"]
      """  This is the Initial grant book value of the entire asset depreciation schedule.  """  
      self.CYImpBookValue:int = obj["CYImpBookValue"]
      """  Current year Impairment Bookvalue is the impairment bookvalue subtracted from the asset this year.  """  
      self.CYDispGrantPrevDepn:int = obj["CYDispGrantPrevDepn"]
      """  Previous years Disposal Grant depreciation  """  
      self.CYDispGrantCurrDepn:int = obj["CYDispGrantCurrDepn"]
      """  Current year Disposal Grant depreciation  """  
      self.CYDispGrantBookValue:int = obj["CYDispGrantBookValue"]
      """  Current year disposal grant bookvalue is the disposal grant bookvalue disposed from the asset this year.  """  
      self.DocCYOpenGrantBookValue:int = obj["DocCYOpenGrantBookValue"]
      """  Current year opening grant bookvalue  """  
      self.DocCYImpBookValue:int = obj["DocCYImpBookValue"]
      """  Current year Impairment Bookvalue is the impairment bookvalue subtracted from the asset this year.  """  
      self.DocCYDispGrantPrevDepn:int = obj["DocCYDispGrantPrevDepn"]
      """  Previous years Disposal Grant depreciation  """  
      self.DocCYDispGrantCurrDepn:int = obj["DocCYDispGrantCurrDepn"]
      """  Current year Disposal Grant depreciation  """  
      self.DocCYDispGrantBookValue:int = obj["DocCYDispGrantBookValue"]
      """  Current year disposal grant bookvalue is the disposal grant bookvalue disposed from the asset this year.  """  
      self.Rpt1CYOpenGrantBookValue:int = obj["Rpt1CYOpenGrantBookValue"]
      """  Current year opening grant bookvalue  """  
      self.Rpt1CYImpBookValue:int = obj["Rpt1CYImpBookValue"]
      """  Current year Impairment Bookvalue is the impairment bookvalue subtracted from the asset this year.  """  
      self.Rpt1CYDispGrantPrevDepn:int = obj["Rpt1CYDispGrantPrevDepn"]
      """  Previous years Disposal Grant depreciation  """  
      self.Rpt1CYDispGrantCurrDepn:int = obj["Rpt1CYDispGrantCurrDepn"]
      """  Current year Disposal Grant depreciation  """  
      self.Rpt1CYDispGrantBookValue:int = obj["Rpt1CYDispGrantBookValue"]
      """  Current year disposal grant bookvalue is the disposal grant bookvalue disposed from the asset this year.  """  
      self.Rpt2CYOpenGrantBookValue:int = obj["Rpt2CYOpenGrantBookValue"]
      """  Current year opening grant bookvalue  """  
      self.Rpt2CYImpBookValue:int = obj["Rpt2CYImpBookValue"]
      """  Current year Impairment Bookvalue is the impairment bookvalue subtracted from the asset this year.  """  
      self.Rpt2CYDispGrantPrevDepn:int = obj["Rpt2CYDispGrantPrevDepn"]
      """  Previous years Disposal Grant depreciation  """  
      self.Rpt2CYDispGrantCurrDepn:int = obj["Rpt2CYDispGrantCurrDepn"]
      """  Current year Disposal Grant depreciation  """  
      self.Rpt2CYDispGrantBookValue:int = obj["Rpt2CYDispGrantBookValue"]
      """  Current year disposal grant bookvalue is the disposal grant bookvalue disposed from the asset this year.  """  
      self.Rpt3CYOpenGrantBookValue:int = obj["Rpt3CYOpenGrantBookValue"]
      """  Current year opening grant bookvalue  """  
      self.Rpt3CYImpBookValue:int = obj["Rpt3CYImpBookValue"]
      """  Current year Impairment Bookvalue is the impairment bookvalue subtracted from the asset this year.  """  
      self.Rpt3CYDispGrantPrevDepn:int = obj["Rpt3CYDispGrantPrevDepn"]
      """  Previous years Disposal Grant depreciation  """  
      self.Rpt3CYDispGrantCurrDepn:int = obj["Rpt3CYDispGrantCurrDepn"]
      """  Current year Disposal Grant depreciation  """  
      self.Rpt3CYDispGrantBookValue:int = obj["Rpt3CYDispGrantBookValue"]
      """  Current year disposal grant bookvalue is the disposal grant bookvalue disposed from the asset this year.  """  
      self.DocCYOpenDepn:int = obj["DocCYOpenDepn"]
      """  Current year opening depreciation  """  
      self.Rpt1CYOpenDepn:int = obj["Rpt1CYOpenDepn"]
      """  Current year opening depreciation  """  
      self.Rpt2CYOpenDepn:int = obj["Rpt2CYOpenDepn"]
      """  Current year opening depreciation  """  
      self.Rpt3CYOpenDepn:int = obj["Rpt3CYOpenDepn"]
      """  Current year opening depreciation  """  
      self.CurrentActPrevDepn:int = obj["CurrentActPrevDepn"]
      """  Actual posted depreciation recorded for the previous years.  This depreciation amount is not affected by the disposal depreciation.  """  
      self.CurrentActPostedDepn:int = obj["CurrentActPostedDepn"]
      """  Actual posted depreciation recorded for the current year.  This depreciation amount is not affected by the disposal depreciation.  """  
      self.DocCurrentActPrevDepn:int = obj["DocCurrentActPrevDepn"]
      """  Actual posted depreciation recorded for the previous years.  This depreciation amount is not affected by the disposal depreciation.  """  
      self.DocCurrentActPostedDepn:int = obj["DocCurrentActPostedDepn"]
      """  Actual posted depreciation recorded for the current year.  This depreciation amount is not affected by the disposal depreciation.  """  
      self.Rpt1CurrentActPrevDepn:int = obj["Rpt1CurrentActPrevDepn"]
      """  Actual posted depreciation recorded for the previous years.  This depreciation amount is not affected by the disposal depreciation.  """  
      self.Rpt1CurrentActPostedDepn:int = obj["Rpt1CurrentActPostedDepn"]
      """  Actual posted depreciation recorded for the current year.  This depreciation amount is not affected by the disposal depreciation.  """  
      self.Rpt2CurrentActPrevDepn:int = obj["Rpt2CurrentActPrevDepn"]
      """  Actual posted depreciation recorded for the previous years.  This depreciation amount is not affected by the disposal depreciation.  """  
      self.Rpt2CurrentActPostedDepn:int = obj["Rpt2CurrentActPostedDepn"]
      """  Actual posted depreciation recorded for the current year.  This depreciation amount is not affected by the disposal depreciation.  """  
      self.Rpt3CurrentActPrevDepn:int = obj["Rpt3CurrentActPrevDepn"]
      """  Actual posted depreciation recorded for the previous years.  This depreciation amount is not affected by the disposal depreciation.  """  
      self.Rpt3CurrentActPostedDepn:int = obj["Rpt3CurrentActPostedDepn"]
      """  Actual posted depreciation recorded for the current year.  This depreciation amount is not affected by the disposal depreciation.  """  
      self.CYAddGrantPrevDepn:int = obj["CYAddGrantPrevDepn"]
      """  Previous years Addition Grant depreciation  """  
      self.CYAddGrantCurrDepn:int = obj["CYAddGrantCurrDepn"]
      """  Previous years Addition Grant depreciation  """  
      self.CYAddGrantBookValue:int = obj["CYAddGrantBookValue"]
      """  Current year addition grant bookvalue is the addition grant bookvalue added to the asset this year.  """  
      self.DocCYAddGrantPrevDepn:int = obj["DocCYAddGrantPrevDepn"]
      """  Previous years Addition Grant depreciation  """  
      self.DocCYAddGrantCurrDepn:int = obj["DocCYAddGrantCurrDepn"]
      """  Current year Addition Grant depreciation  """  
      self.DocCYAddGrantBookValue:int = obj["DocCYAddGrantBookValue"]
      """  Current year addition grant bookvalue is the addition grant bookvalue added to the asset this year.  """  
      self.Rpt1CYAddGrantPrevDepn:int = obj["Rpt1CYAddGrantPrevDepn"]
      """  Previous years Addition Grant depreciation  """  
      self.Rpt1CYAddGrantCurrDepn:int = obj["Rpt1CYAddGrantCurrDepn"]
      """  Current year Addition Grant depreciation  """  
      self.Rpt1CYAddGrantBookValue:int = obj["Rpt1CYAddGrantBookValue"]
      """  Current year addition grant bookvalue is the addition grant bookvalue added to the asset this year.  """  
      self.Rpt2CYAddGrantPrevDepn:int = obj["Rpt2CYAddGrantPrevDepn"]
      """  Previous years Addition Grant depreciation  """  
      self.Rpt2CYAddGrantCurrDepn:int = obj["Rpt2CYAddGrantCurrDepn"]
      """  Current year Addition Grant depreciation  """  
      self.Rpt2CYAddGrantBookValue:int = obj["Rpt2CYAddGrantBookValue"]
      """  Current year addition grant bookvalue is the addition grant bookvalue added to the asset this year.  """  
      self.Rpt3CYAddGrantPrevDepn:int = obj["Rpt3CYAddGrantPrevDepn"]
      """  Previous years Addition Grant depreciation  """  
      self.Rpt3CYAddGrantCurrDepn:int = obj["Rpt3CYAddGrantCurrDepn"]
      """  Current year Addition Grant depreciation  """  
      self.Rpt3CYAddGrantBookValue:int = obj["Rpt3CYAddGrantBookValue"]
      """  Current year addition grant bookvalue is the addition grant bookvalue added to the asset this year.  """  
      self.Depreciate:bool = obj["Depreciate"]
      """  Depreciation Flag. When true then the asset register will be processed in the depreciation recalculation process and the depreciation posting process.  If set to false then all depreciation parameters are blank and not updatable.  """  
      self.CYOpenCost:int = obj["CYOpenCost"]
      """  Current year opening cost  """  
      self.DocCYOpenCost:int = obj["DocCYOpenCost"]
      """  Current year opening cost  """  
      self.Rpt1CYOpenCost:int = obj["Rpt1CYOpenCost"]
      """  Current year opening cost  """  
      self.Rpt2CYOpenCost:int = obj["Rpt2CYOpenCost"]
      """  Current year opening cost  """  
      self.Rpt3CYOpenCost:int = obj["Rpt3CYOpenCost"]
      """  Current year opening cost  """  
      self.CYOpenGrant:int = obj["CYOpenGrant"]
      """  Current year opening grant amount  """  
      self.DocCYOpenGrant:int = obj["DocCYOpenGrant"]
      """  Current year opening cost  """  
      self.Rpt1CYOpenGrant:int = obj["Rpt1CYOpenGrant"]
      """  Current year opening cost  """  
      self.Rpt2CYOpenGrant:int = obj["Rpt2CYOpenGrant"]
      """  Current year opening cost  """  
      self.Rpt3CYOpenGrant:int = obj["Rpt3CYOpenGrant"]
      """  Current year opening cost  """  
      self.CYAddCost:int = obj["CYAddCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.DocCYAddCost:int = obj["DocCYAddCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt1CYAddCost:int = obj["Rpt1CYAddCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt2CYAddCost:int = obj["Rpt2CYAddCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt3CYAddCost:int = obj["Rpt3CYAddCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.CYImpCost:int = obj["CYImpCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.DocCYImpCost:int = obj["DocCYImpCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.Rpt1CYImpCost:int = obj["Rpt1CYImpCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.Rpt2CYImpCost:int = obj["Rpt2CYImpCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.Rpt3CYImpCost:int = obj["Rpt3CYImpCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.CYDispCost:int = obj["CYDispCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.DocCYDispCost:int = obj["DocCYDispCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.Rpt1CYDispCost:int = obj["Rpt1CYDispCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.Rpt2CYDispCost:int = obj["Rpt2CYDispCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.Rpt3CYDispCost:int = obj["Rpt3CYDispCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.CYDispProceeds:int = obj["CYDispProceeds"]
      """  Disposal proceed amount.  """  
      self.DocCYDispProceeds:int = obj["DocCYDispProceeds"]
      """  Disposal proceed amount.  """  
      self.Rpt1CYDispProceeds:int = obj["Rpt1CYDispProceeds"]
      """  Disposal proceed amount.  """  
      self.Rpt2CYDispProceeds:int = obj["Rpt2CYDispProceeds"]
      """  Disposal proceed amount.  """  
      self.Rpt3CYDispProceeds:int = obj["Rpt3CYDispProceeds"]
      """  Disposal proceed amount.  """  
      self.CYDispProfit:int = obj["CYDispProfit"]
      """  Disposal profit/loss amount.  """  
      self.DocCYDispProfit:int = obj["DocCYDispProfit"]
      """  Disposal profit/loss amount.  """  
      self.Rpt1CYDispProfit:int = obj["Rpt1CYDispProfit"]
      """  Disposal profit/loss amount.  """  
      self.Rpt2CYDispProfit:int = obj["Rpt2CYDispProfit"]
      """  Disposal profit/loss amount.  """  
      self.Rpt3CYDispProfit:int = obj["Rpt3CYDispProfit"]
      """  Disposal profit/loss amount.  """  
      self.CYAddGrant:int = obj["CYAddGrant"]
      """  Current Addition Grant is the grant amount added to the asset  this year.  """  
      self.DocCYAddGrant:int = obj["DocCYAddGrant"]
      """  Current Addition Grant is the grant amount added to the asset  this year.  """  
      self.Rpt1CYAddGrant:int = obj["Rpt1CYAddGrant"]
      """  Current Addition Grant is the grant amount added to the asset  this year.  """  
      self.Rpt2CYAddGrant:int = obj["Rpt2CYAddGrant"]
      """  Current Addition Grant is the grant amount added to the asset  this year.  """  
      self.Rpt3CYAddGrant:int = obj["Rpt3CYAddGrant"]
      """  Current Addition Grant is the grant amount added to the asset  this year.  """  
      self.CurrentCostvalue:int = obj["CurrentCostvalue"]
      """  Current cost value of the asset.  """  
      self.DocCurrentCostvalue:int = obj["DocCurrentCostvalue"]
      """  Current cost value of the asset.  """  
      self.Rpt1CurrentCostvalue:int = obj["Rpt1CurrentCostvalue"]
      """  Current cost value of the asset.  """  
      self.Rpt2CurrentCostvalue:int = obj["Rpt2CurrentCostvalue"]
      """  Current cost value of the asset.  """  
      self.Rpt3CurrentCostvalue:int = obj["Rpt3CurrentCostvalue"]
      """  Current cost value of the asset.  """  
      self.CurrentGrantAmt:int = obj["CurrentGrantAmt"]
      """  Current Grant Amount of the asset.  """  
      self.DocCurrentGrantAmt:int = obj["DocCurrentGrantAmt"]
      """  Current Grant Amount of the asset.  """  
      self.Rpt1CurrentGrantAmt:int = obj["Rpt1CurrentGrantAmt"]
      """  Current Grant Amount of the asset.  """  
      self.Rpt2CurrentGrantAmt:int = obj["Rpt2CurrentGrantAmt"]
      """  Current Grant Amount of the asset.  """  
      self.Rpt3CurrentGrantAmt:int = obj["Rpt3CurrentGrantAmt"]
      """  Current Grant Amount of the asset.  """  
      self.RateFactor:int = obj["RateFactor"]
      """  The Rate Factor is used as a multiplier when calculating Annual Depreciation Charge using the Declining Balance formula.  """  
      self.ResidualValue:int = obj["ResidualValue"]
      """  Residual value of the asset  """  
      self.DocResidualValue:int = obj["DocResidualValue"]
      """  Residual value of the asset in document currency  """  
      self.Rpt1ResidualValue:int = obj["Rpt1ResidualValue"]
      """  Residual value of the asset in reporting currency  """  
      self.Rpt2ResidualValue:int = obj["Rpt2ResidualValue"]
      """  Residual value of the asset in reporting currency  """  
      self.Rpt3ResidualValue:int = obj["Rpt3ResidualValue"]
      """  Residual value of the asset in reporting currency  """  
      self.ReplaceValue:int = obj["ReplaceValue"]
      """  Replacement value of the asset. For information purposes only.  """  
      self.DocReplaceValue:int = obj["DocReplaceValue"]
      """  Replacement value of the asset in document currency. For information purposes only.  """  
      self.Rpt1ReplaceValue:int = obj["Rpt1ReplaceValue"]
      """  Replacement value of the asset in reporting currency. For information purposes only.  """  
      self.Rpt2ReplaceValue:int = obj["Rpt2ReplaceValue"]
      """  Replacement value of the asset in reporting currency. For information purposes only.  """  
      self.Rpt3ReplaceValue:int = obj["Rpt3ReplaceValue"]
      """  Replacement value of the asset in reporting currency. For information purposes only.  """  
      self.BookValueDate:str = obj["BookValueDate"]
      """  The end date of the last posted depreciation period that has affected the book value of this asset register detail.  """  
      self.DateSwitched:str = obj["DateSwitched"]
      """  This is the starting date of the fiscal year or fiscal period when the actual switch of the depreciation method to the alternative method happened.  """  
      self.CurrActGrantPostedDepn:int = obj["CurrActGrantPostedDepn"]
      """  Actual posted grant depreciation recorded for the current year.  This grant depreciation amount is not affected by the disposal grant depreciation.  """  
      self.DocCurrActGrantPostedDepn:int = obj["DocCurrActGrantPostedDepn"]
      """  Actual posted grant depreciation recorded for the current year.  This grant depreciation amount is not affected by the disposal grant depreciation.  """  
      self.Rpt1CurrActGrantPostedDepn:int = obj["Rpt1CurrActGrantPostedDepn"]
      """  Actual posted grant depreciation recorded for the current year.  This grant depreciation amount is not affected by the disposal grant depreciation.  """  
      self.Rpt2CurrActGrantPostedDepn:int = obj["Rpt2CurrActGrantPostedDepn"]
      """  Actual posted grant depreciation recorded for the current year.  This grant depreciation amount is not affected by the disposal grant depreciation.  """  
      self.Rpt3CurrActGrantPostedDepn:int = obj["Rpt3CurrActGrantPostedDepn"]
      """  Actual posted grant depreciation recorded for the current year.  This grant depreciation amount is not affected by the disposal grant depreciation.  """  
      self.AcquisitionCost:int = obj["AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.DocAcquisitionCost:int = obj["DocAcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.Rpt1AcquisitionCost:int = obj["Rpt1AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.Rpt2AcquisitionCost:int = obj["Rpt2AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.Rpt3AcquisitionCost:int = obj["Rpt3AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.CYDispGrant:int = obj["CYDispGrant"]
      """  Current Disposal Grant is the grant amount disposed from the asset  this year.  """  
      self.DocCYDispGrant:int = obj["DocCYDispGrant"]
      """  Current Disposal Grant is the grant amount disposed from the asset  this year.  """  
      self.Rpt1CYDispGrant:int = obj["Rpt1CYDispGrant"]
      """  Current Disposal Grant is the grant amount disposed from the asset  this year.  """  
      self.Rpt2CYDispGrant:int = obj["Rpt2CYDispGrant"]
      """  Current Disposal Grant is the grant amount disposed from the asset  this year.  """  
      self.Rpt3CYDispGrant:int = obj["Rpt3CYDispGrant"]
      """  Current Disposal Grant is the grant amount disposed from the asset  this year.  """  
      self.DynamicDepYear:bool = obj["DynamicDepYear"]
      """  Flag to indicate if dynamic depreciation year should be used instead of the Fiscal Year to influence the depreciation schedule.  """  
      self.CYRevalueGainLoss:int = obj["CYRevalueGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.DocCYRevalueGainLoss:int = obj["DocCYRevalueGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt1CYRevalueGainLoss:int = obj["Rpt1CYRevalueGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt2CYRevalueGainLoss:int = obj["Rpt2CYRevalueGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt3CYRevalueGainLoss:int = obj["Rpt3CYRevalueGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.CYDepRevalGainLoss:int = obj["CYDepRevalGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.DocCYDepRevalGainLoss:int = obj["DocCYDepRevalGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt1CYDepRevalGainLoss:int = obj["Rpt1CYDepRevalGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt2CYDepRevalGainLoss:int = obj["Rpt2CYDepRevalGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt3CYDepRevalGainLoss:int = obj["Rpt3CYDepRevalGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.CYRevGrantGainLoss:int = obj["CYRevGrantGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.DocCYRevGrantGainLoss:int = obj["DocCYRevGrantGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt1CYRevGrantGainLoss:int = obj["Rpt1CYRevGrantGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt2CYRevGrantGainLoss:int = obj["Rpt2CYRevGrantGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt3CYRevGrantGainLoss:int = obj["Rpt3CYRevGrantGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.CYDepRevGrantGainLoss:int = obj["CYDepRevGrantGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.DocCYDepRevGrantGainLoss:int = obj["DocCYDepRevGrantGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt1CYDepRevGrantGainLoss:int = obj["Rpt1CYDepRevGrantGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt2CYDepRevGrantGainLoss:int = obj["Rpt2CYDepRevGrantGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt3CYDepRevGrantGainLoss:int = obj["Rpt3CYDepRevGrantGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DepOnDisposal:int = obj["DepOnDisposal"]
      """  Determines how depreciation is calculated in the period of disposal or revaluation.  """  
      self.ActDepStartDate:str = obj["ActDepStartDate"]
      """  Date of actual depreciation schedule start.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.CurrencySymbol:str = obj["CurrencySymbol"]
      self.CYDispTotalDepn:int = obj["CYDispTotalDepn"]
      """  Calculated field to store the sum of current year Disposal Current and Previous Depreciation.  """  
      self.DocCYDispTotalDepn:int = obj["DocCYDispTotalDepn"]
      """  Calculated field to store the sum of current year Disposal Current and Previous Depreciation.  """  
      self.DocRevalueGainLoss:int = obj["DocRevalueGainLoss"]
      """  Calculated field to store the total of all posted Revaluations as of the end of the current asset register year.  """  
      self.DocYTDAccumDepn:int = obj["DocYTDAccumDepn"]
      """  Calculated field to store the total of all posted Depreciations including the depreciations from Addition activities subtracted with depreciations from Disposals as of the end of the current asset register year.  """  
      self.DocYTDAddCost:int = obj["DocYTDAddCost"]
      """  Calculated field to store the total of all posted Addition Costs from the very first period up to the end of the current asset register year.  """  
      self.DocYTDDispCost:int = obj["DocYTDDispCost"]
      """  Calculated field to store the total of all posted Disposal Costs from the very first period up to the end of the current asset register year.  """  
      self.DocYTDGrantDepn:int = obj["DocYTDGrantDepn"]
      """  Calculated field to store the total of all posted Grant Depreciations including the depreciations from Addition activities as of the end of the current asset register year.  """  
      self.DocYTDImpCost:int = obj["DocYTDImpCost"]
      """  Calculated field to store the total of all posted Impairment Costs from the very first period up to the end of the current asset register year.  """  
      self.EnableAnnualDepRate:bool = obj["EnableAnnualDepRate"]
      self.EnableAssetLife:bool = obj["EnableAssetLife"]
      self.EnableProdUnitsSpread:bool = obj["EnableProdUnitsSpread"]
      self.EnableRateFactor:bool = obj["EnableRateFactor"]
      self.EnableTotalProductionUnits:bool = obj["EnableTotalProductionUnits"]
      self.RevalueGainLoss:int = obj["RevalueGainLoss"]
      """  Calculated field to store the total of all posted Revaluations as of the end of the current asset register year.  """  
      self.Rpt1CYDispTotalDepn:int = obj["Rpt1CYDispTotalDepn"]
      """  Calculated field to store the sum of current year Disposal Current and Previous Depreciation.  """  
      self.Rpt1RevalueGainLoss:int = obj["Rpt1RevalueGainLoss"]
      """  Calculated field to store the total of all posted Revaluations as of the end of the current asset register year.  """  
      self.Rpt1YTDAccumDepn:int = obj["Rpt1YTDAccumDepn"]
      """  Calculated field to store the total of all posted Depreciations including the depreciations from Addition activities subtracted with depreciations from Disposals as of the end of the current asset register year.  """  
      self.Rpt1YTDAddCost:int = obj["Rpt1YTDAddCost"]
      """  Calculated field to store the total of all posted Addition Costs from the very first period up to the end of the current asset register year.  """  
      self.Rpt1YTDDispCost:int = obj["Rpt1YTDDispCost"]
      """  Calculated field to store the total of all posted Disposal Costs from the very first period up to the end of the current asset register year.  """  
      self.Rpt1YTDGrantDepn:int = obj["Rpt1YTDGrantDepn"]
      """  Calculated field to store the total of all posted Grant Depreciations including the depreciations from Addition activities as of the end of the current asset register year.  """  
      self.Rpt1YTDImpCost:int = obj["Rpt1YTDImpCost"]
      """  Calculated field to store the total of all posted Impairment Costs from the very first period up to the end of the current asset register year.  """  
      self.Rpt2CYDispTotalDepn:int = obj["Rpt2CYDispTotalDepn"]
      """  Calculated field to store the sum of current year Disposal Current and Previous Depreciation.  """  
      self.Rpt2RevalueGainLoss:int = obj["Rpt2RevalueGainLoss"]
      """  Calculated field to store the total of all posted Revaluations as of the end of the current asset register year.  """  
      self.Rpt2YTDAccumDepn:int = obj["Rpt2YTDAccumDepn"]
      """  Calculated field to store the total of all posted Depreciations including the depreciations from Addition activities subtracted with depreciations from Disposals as of the end of the current asset register year.  """  
      self.Rpt2YTDAddCost:int = obj["Rpt2YTDAddCost"]
      """  Calculated field to store the total of all posted Addition Costs from the very first period up to the end of the current asset register year.  """  
      self.Rpt2YTDDispCost:int = obj["Rpt2YTDDispCost"]
      """  Calculated field to store the total of all posted Disposal Costs from the very first period up to the end of the current asset register year.  """  
      self.Rpt2YTDGrantDepn:int = obj["Rpt2YTDGrantDepn"]
      """  Calculated field to store the total of all posted Grant Depreciations including the depreciations from Addition activities as of the end of the current asset register year.  """  
      self.Rpt2YTDImpCost:int = obj["Rpt2YTDImpCost"]
      """  Calculated field to store the total of all posted Impairment Costs from the very first period up to the end of the current asset register year.  """  
      self.Rpt3CYDispTotalDepn:int = obj["Rpt3CYDispTotalDepn"]
      """  Calculated field to store the sum of current year Disposal Current and Previous Depreciation.  """  
      self.Rpt3RevalueGainLoss:int = obj["Rpt3RevalueGainLoss"]
      """  Calculated field to store the total of all posted Revaluations as of the end of the current asset register year.  """  
      self.Rpt3YTDAccumDepn:int = obj["Rpt3YTDAccumDepn"]
      """  Calculated field to store the total of all posted Depreciations including the depreciations from Addition activities subtracted with depreciations from Disposals as of the end of the current asset register year.  """  
      self.Rpt3YTDAddCost:int = obj["Rpt3YTDAddCost"]
      """  Calculated field to store the total of all posted Addition Costs from the very first period up to the end of the current asset register year.  """  
      self.Rpt3YTDDispCost:int = obj["Rpt3YTDDispCost"]
      """  Calculated field to store the total of all posted Disposal Costs from the very first period up to the end of the current asset register year.  """  
      self.Rpt3YTDGrantDepn:int = obj["Rpt3YTDGrantDepn"]
      """  Calculated field to store the total of all posted Grant Depreciations including the depreciations from Addition activities as of the end of the current asset register year.  """  
      self.Rpt3YTDImpCost:int = obj["Rpt3YTDImpCost"]
      """  Calculated field to store the total of all posted Impairment Costs from the very first period up to the end of the current asset register year.  """  
      self.YTDAccumDepn:int = obj["YTDAccumDepn"]
      """  Calculated field to store the total of all posted Depreciations including the depreciations from Addition activities subtracted with depreciations from Disposals as of the end of the current asset register year.  """  
      self.YTDAddCost:int = obj["YTDAddCost"]
      """  Calculated field to store the total of all posted Addition Costs from the very first period up to the end of the current asset register year.  """  
      self.YTDDispCost:int = obj["YTDDispCost"]
      """  Calculated field to store the total of all posted Disposal Costs from the very first period up to the end of the current asset register year.  """  
      self.YTDGrantDepn:int = obj["YTDGrantDepn"]
      """  Calculated field to store the total of all posted Grant Depreciations including the depreciations from Addition activities as of the end of the current asset register year.  """  
      self.YTDImpCost:int = obj["YTDImpCost"]
      """  Calculated field to store the total of all posted Impairment Costs from the very first period up to the end of the current asset register year.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.AddSpreadDescription:str = obj["AddSpreadDescription"]
      self.AltAssetMethodProrateType:str = obj["AltAssetMethodProrateType"]
      self.AltAssetMethodFinalspread:bool = obj["AltAssetMethodFinalspread"]
      self.AltAssetMethodDescription:str = obj["AltAssetMethodDescription"]
      self.AltAssetMethodAnnualChargeType:str = obj["AltAssetMethodAnnualChargeType"]
      self.AltAssetMethodPeriodChargeType:str = obj["AltAssetMethodPeriodChargeType"]
      self.AltAssetMethodDepChargeBasis:str = obj["AltAssetMethodDepChargeBasis"]
      self.AnnualSpreadDescription:str = obj["AnnualSpreadDescription"]
      self.FAMethodFinalspread:bool = obj["FAMethodFinalspread"]
      self.FAMethodDescription:str = obj["FAMethodDescription"]
      self.FAMethodAnnualChargeType:str = obj["FAMethodAnnualChargeType"]
      self.FAMethodProrateType:str = obj["FAMethodProrateType"]
      self.FAMethodDepChargeBasis:str = obj["FAMethodDepChargeBasis"]
      self.FAMethodPeriodChargeType:str = obj["FAMethodPeriodChargeType"]
      self.FAssetRegDescription:str = obj["FAssetRegDescription"]
      self.FinalSpreadDescription:str = obj["FinalSpreadDescription"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.PeriodSpreadDescription:str = obj["PeriodSpreadDescription"]
      self.ProdSpreadDescription:str = obj["ProdSpreadDescription"]
      self.RateSpreadDescription:str = obj["RateSpreadDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAssetListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the asset.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Identifier of the asset  """  
      self.AssetSeq:int = obj["AssetSeq"]
      """  The asset sequence allows for multiple fiscal instances of the asset. When greater than zero it is a fiscal instance of the asset. Currently only 0 is supported.  """  
      self.AssetDescription:str = obj["AssetDescription"]
      """  Mandatory description of the asset.  """  
      self.InActive:bool = obj["InActive"]
      """  flag to indicate an asset to be inactive. Inactive assets are not depreciated or recalculated.  """  
      self.ParentAsset:str = obj["ParentAsset"]
      """  Asset parent of this asset  """  
      self.NewAssetFlag:bool = obj["NewAssetFlag"]
      """  Informational indication of a newly bought asset.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  The code of the mandatory asset group.  """  
      self.ClassCode:str = obj["ClassCode"]
      """  Identifier of the asset class.  """  
      self.ResourceGroupID:str = obj["ResourceGroupID"]
      """  Identifier of the Resource Group of the asset. For informational purposes only.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The Resource identifier of the asset. For informational purposes only.  """  
      self.AcquiredDate:str = obj["AcquiredDate"]
      """  Date of acquisition of the asset.  """  
      self.CommissionedDate:str = obj["CommissionedDate"]
      """  Date of placing the asset in service. Also the start date of depreciation.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Identifier of the vendor of the asset.  """  
      self.VendorName:str = obj["VendorName"]
      """  The name of the vendor. The name can be entered without entering a vendor.  """  
      self.PONum:int = obj["PONum"]
      """  The po number the asset purchase order.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  The invoice number of asset invoice.  """  
      self.JobNum:str = obj["JobNum"]
      """  The job that created the asset.  """  
      self.Serialno:str = obj["Serialno"]
      """  The serial number of the asset.  """  
      self.Manufacturer:str = obj["Manufacturer"]
      """  The original manufacturer of the asset.  """  
      self.Model:str = obj["Model"]
      """  The model of the asset.  """  
      self.InsurancePolicy:str = obj["InsurancePolicy"]
      """  Insurance policy for the asset.  """  
      self.InsuranceCompany:str = obj["InsuranceCompany"]
      """  The insurance company.  """  
      self.InsurancePremium:int = obj["InsurancePremium"]
      """  Insurance premium  """  
      self.InsuranceRenewalDate:str = obj["InsuranceRenewalDate"]
      """  Insurance RenewalDate  """  
      self.InsuranceInsurer:str = obj["InsuranceInsurer"]
      """  The insurer.  """  
      self.LeaseFlag:bool = obj["LeaseFlag"]
      """  Flag the asset as leased.  """  
      self.LeaseValue:int = obj["LeaseValue"]
      """  Lease amount  """  
      self.LeaseMileage:int = obj["LeaseMileage"]
      """  Mileage limit of lease  """  
      self.LeaseEndDate:str = obj["LeaseEndDate"]
      """  End date of lease.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse where the asset is stored. This is for information purposes only. In the warehouse tracker no assets can be tracked.  """  
      self.BinNum:str = obj["BinNum"]
      """  The bin where the addition is stored. This is for information purposes only. In the bin tracker no assets can be tracked.  """  
      self.Location:str = obj["Location"]
      """  Freeform field for the location of tha aaset.  """  
      self.OverideCost:int = obj["OverideCost"]
      """  The overide cost is cost amount which is used instead of the asset cost amount for the calculation of a year depreciation.  """  
      self.ResidualValue:int = obj["ResidualValue"]
      """  Residual value of the asset  """  
      self.ReplaceValue:int = obj["ReplaceValue"]
      """  Replacement value of the asset. For information purposes only.  """  
      self.CYAdditionCost:int = obj["CYAdditionCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.CYDisposalCost:int = obj["CYDisposalCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.CYDisposalProceeds:int = obj["CYDisposalProceeds"]
      """  Disposal proceed amount.  """  
      self.CurrentCostvalue:int = obj["CurrentCostvalue"]
      """  Current cost value of the asset.  """  
      self.Acquire:int = obj["Acquire"]
      """  The amount the asset is acquired for.  """  
      self.ImageFileName:str = obj["ImageFileName"]
      """  Path and filename of asset image file.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the Company currency.  """  
      self.AssetStatus:str = obj["AssetStatus"]
      """  Current Status of the asset. Valid values are: 'NEW'; 'ACTIVE'; 'DISPOSED' or 'INACTIVE'.  """  
      self.AcquisitionCost:int = obj["AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the Asset with a project in the Project table.  This can be blank.  """  
      self.TagNum:str = obj["TagNum"]
      """  Tag number. This will keep the asset label.  """  
      self.CurrentGrantAmt:int = obj["CurrentGrantAmt"]
      """  The total Grant amount recorded for this Asset.  """  
      self.DocResidualValue:int = obj["DocResidualValue"]
      """  Residual value of the asset  """  
      self.DocReplaceValue:int = obj["DocReplaceValue"]
      """  Replacement value of the asset. For information purposes only.  """  
      self.DocCYAdditionCost:int = obj["DocCYAdditionCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.DocCYDisposalCost:int = obj["DocCYDisposalCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.DocAcquisitionCost:int = obj["DocAcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.DocCurrentGrantAmt:int = obj["DocCurrentGrantAmt"]
      """  The total Grant amount recorded for this Asset in document currency.  """  
      self.Rpt1ResidualValue:int = obj["Rpt1ResidualValue"]
      """  Residual value of the asset  """  
      self.Rpt1ReplaceValue:int = obj["Rpt1ReplaceValue"]
      """  Replacement value of the asset. For information purposes only.  """  
      self.Rpt1CYAdditionCost:int = obj["Rpt1CYAdditionCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt1CYDisposalCost:int = obj["Rpt1CYDisposalCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.Rpt1AcquisitionCost:int = obj["Rpt1AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.Rpt1CurrentGrantAmt:int = obj["Rpt1CurrentGrantAmt"]
      """  The total Grant amount recorded for this Asset in reporting currency.  """  
      self.Rpt2ResidualValue:int = obj["Rpt2ResidualValue"]
      """  Residual value of the asset  """  
      self.Rpt2ReplaceValue:int = obj["Rpt2ReplaceValue"]
      """  Replacement value of the asset. For information purposes only.  """  
      self.Rpt2CYAdditionCost:int = obj["Rpt2CYAdditionCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt2CYDisposalCost:int = obj["Rpt2CYDisposalCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.Rpt2AcquisitionCost:int = obj["Rpt2AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.Rpt2CurrentGrantAmt:int = obj["Rpt2CurrentGrantAmt"]
      """  The total Grant amount recorded for this Asset in reporting currency.  """  
      self.Rpt3ResidualValue:int = obj["Rpt3ResidualValue"]
      """  Residual value of the asset  """  
      self.Rpt3ReplaceValue:int = obj["Rpt3ReplaceValue"]
      """  Replacement value of the asset. For information purposes only.  """  
      self.Rpt3CYAdditionCost:int = obj["Rpt3CYAdditionCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt3CYDisposalCost:int = obj["Rpt3CYDisposalCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.Rpt3AcquisitionCost:int = obj["Rpt3AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.Rpt3CurrentGrantAmt:int = obj["Rpt3CurrentGrantAmt"]
      """  The total Grant amount recorded for this Asset in reporting currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.MXTaxCode:str = obj["MXTaxCode"]
      """  Tax Code (Mexico Localization field)  """  
      self.MXTaxRate:str = obj["MXTaxRate"]
      """  Tax Rate (Mexico Localization field)  """  
      self.MXInvestAmount:int = obj["MXInvestAmount"]
      """  Investment Value (Mexico Localization field)  """  
      self.MXTaxAmount:int = obj["MXTaxAmount"]
      """  Mexico Tax Amount (Mexico Localization field)  """  
      self.MXAnnualDepre:int = obj["MXAnnualDepre"]
      """  Annual depreciation Percentage (Mexico Localization field)  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line  (Mexico Localization field)  """  
      self.MXAssetLife:int = obj["MXAssetLife"]
      """  Mexico Asset Life (Mexico Localization field)  """  
      self.CYImpairCost:int = obj["CYImpairCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.DocCYImpairCost:int = obj["DocCYImpairCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.Rpt1CYImpairCost:int = obj["Rpt1CYImpairCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.Rpt2CYImpairCost:int = obj["Rpt2CYImpairCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.Rpt3CYImpairCost:int = obj["Rpt3CYImpairCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.DocCurrentCostValue:int = obj["DocCurrentCostValue"]
      """  Current cost value of the asset in document currency.  """  
      self.Rpt1CurrentCostvalue:int = obj["Rpt1CurrentCostvalue"]
      """  Current cost value of the asset in reporting currency.  """  
      self.Rpt2CurrentCostvalue:int = obj["Rpt2CurrentCostvalue"]
      """  Current cost value of the asset in reporting currency.  """  
      self.Rpt3CurrentCostValue:int = obj["Rpt3CurrentCostValue"]
      """  Current cost value of the asset in reporting currency.  """  
      self.LocID:str = obj["LocID"]
      """  Location ID.  """  
      self.DocCYDisposalProceeds:int = obj["DocCYDisposalProceeds"]
      """  Disposal proceed amount.  """  
      self.Rpt1CYDisposalProceeds:int = obj["Rpt1CYDisposalProceeds"]
      """  Disposal proceed amount.  """  
      self.Rpt2CYDisposalProceeds:int = obj["Rpt2CYDisposalProceeds"]
      """  Disposal proceed amount.  """  
      self.Rpt3CYDisposalProceeds:int = obj["Rpt3CYDisposalProceeds"]
      """  Disposal proceed amount.  """  
      self.CYAdditionGrant:int = obj["CYAdditionGrant"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.DocCYAdditionGrant:int = obj["DocCYAdditionGrant"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt1CYAdditionGrant:int = obj["Rpt1CYAdditionGrant"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt2CYAdditionGrant:int = obj["Rpt2CYAdditionGrant"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt3CYAdditionGrant:int = obj["Rpt3CYAdditionGrant"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  """  
      self.LastCalDate:str = obj["LastCalDate"]
      """  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.DepRecalcNeeded:bool = obj["DepRecalcNeeded"]
      """  System maintained field.  Indicates that asset depreciation needs to be recalculated for this asset.  """  
      self.EquipID:str = obj["EquipID"]
      """  Descriptive code to uniquely identify the Equipment.  """  
      self.Brand:str = obj["Brand"]
      """  Brand of equipment  """  
      self.AssetUnits:int = obj["AssetUnits"]
      """  This is the total number of units recorded for this asset.  This is not directly maintained by user.  This is increased when you add/transfer asset "qty" from the Asset Addition Entry.  This is decreased when you dispose/transfer asset "qty" from the Asset Disposal Entry.  This field is not a true quantity field since we do not perform any unit of measure conversion when we update AssetUnits based on the transferred qty.  """  
      self.Lineage:str = obj["Lineage"]
      """  Stores the keys (assetnum) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  """  
      self.DocInsurancePremium:int = obj["DocInsurancePremium"]
      """  Insurance premium in document currency.  """  
      self.Rpt1InsurancePremium:int = obj["Rpt1InsurancePremium"]
      """  Insurance premium in Reporting Currency.  """  
      self.Rpt2InsurancePremium:int = obj["Rpt2InsurancePremium"]
      """  Insurance premium in Reporting Currency.  """  
      self.Rpt3InsurancePremium:int = obj["Rpt3InsurancePremium"]
      """  Insurance premium in Reporting Currency.  """  
      self.DocLeaseValue:int = obj["DocLeaseValue"]
      """  Lease amount in document currency.  """  
      self.Rpt1LeaseValue:int = obj["Rpt1LeaseValue"]
      """  Lease amount in Reporting Currency.  """  
      self.Rpt2LeaseValue:int = obj["Rpt2LeaseValue"]
      """  Lease amount in Rocument Currency.  """  
      self.Rpt3LeaseValue:int = obj["Rpt3LeaseValue"]
      """  Lease amount in Reporting Currency.  """  
      self.InsuranceValue:int = obj["InsuranceValue"]
      """  Insurance Value  """  
      self.DocInsuranceValue:int = obj["DocInsuranceValue"]
      """  Insurance Value in document currency.  """  
      self.Rpt1InsuranceValue:int = obj["Rpt1InsuranceValue"]
      """  Insurance Value in Reporting Currency.  """  
      self.Rpt2InsuranceValue:int = obj["Rpt2InsuranceValue"]
      """  Insurance Value in Reporting Currency.  """  
      self.Rpt3InsuranceValue:int = obj["Rpt3InsuranceValue"]
      """  Insurance Value in Reporting Currency.  """  
      self.InsPremiumModifier:str = obj["InsPremiumModifier"]
      """  The premium modifier expresses if the Insurance Premium is per Period or per Year.  Values are: Periods and Years.  """  
      self.LeaseModifier:str = obj["LeaseModifier"]
      """  The lease value modifier expresses if the Lease Value is per Period or per Year.  Values are: Periods and Years.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  The Project Phase ID of this asset.  """  
      self.LeaseNum:str = obj["LeaseNum"]
      """  Lease Number of the asset.  """  
      self.LeaseCompany:str = obj["LeaseCompany"]
      """  The Leasing Company.  """  
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
      self.Department:str = obj["Department"]
      """  Department  """  
      self.IsPosted:bool = obj["IsPosted"]
      self.FinalSpread:bool = obj["FinalSpread"]
      self.AdditionSpread:bool = obj["AdditionSpread"]
      self.BinDescription:str = obj["BinDescription"]
      self.MXTaxCatID:str = obj["MXTaxCatID"]
      """  Mexico Localization Field  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.ImagePath:str = obj["ImagePath"]
      """  Path name of the Asset Image or Photo  """  
      self.EquipCreate:bool = obj["EquipCreate"]
      self.PhaseDescription:str = obj["PhaseDescription"]
      self.AssetGrpDescDescription:str = obj["AssetGrpDescDescription"]
      """  The description of the asset group.  """  
      self.ClassDescription:str = obj["ClassDescription"]
      """  Class description.  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.LocIDDescription:str = obj["LocIDDescription"]
      """  Description the Location.  Cannot be blank.  """  
      self.MachineDescDescription:str = obj["MachineDescDescription"]
      """  Full description of Resource.  """  
      self.ResrceGrpDescDescription:str = obj["ResrceGrpDescDescription"]
      """  Long description of the Resource Group.  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAssetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the asset.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Identifier of the asset  """  
      self.AssetSeq:int = obj["AssetSeq"]
      """  The asset sequence allows for multiple fiscal instances of the asset. When greater than zero it is a fiscal instance of the asset. Currently only 0 is supported.  """  
      self.AssetDescription:str = obj["AssetDescription"]
      """  Mandatory description of the asset.  """  
      self.InActive:bool = obj["InActive"]
      """  flag to indicate an asset to be inactive. Inactive assets are not depreciated or recalculated.  """  
      self.ParentAsset:str = obj["ParentAsset"]
      """  Asset parent of this asset  """  
      self.NewAssetFlag:bool = obj["NewAssetFlag"]
      """  Informational indication of a newly bought asset.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  The code of the mandatory asset group.  """  
      self.ClassCode:str = obj["ClassCode"]
      """  Identifier of the asset class.  """  
      self.ResourceGroupID:str = obj["ResourceGroupID"]
      """  Identifier of the Resource Group of the asset. For informational purposes only.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The Resource identifier of the asset. For informational purposes only.  """  
      self.AcquiredDate:str = obj["AcquiredDate"]
      """  Date of acquisition of the asset.  """  
      self.CommissionedDate:str = obj["CommissionedDate"]
      """  Date of placing the asset in service. Also the start date of depreciation.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Identifier of the vendor of the asset.  """  
      self.VendorName:str = obj["VendorName"]
      """  The name of the vendor. The name can be entered without entering a vendor.  """  
      self.PONum:int = obj["PONum"]
      """  The po number the asset purchase order.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  The invoice number of asset invoice.  """  
      self.JobNum:str = obj["JobNum"]
      """  The job that created the asset.  """  
      self.Serialno:str = obj["Serialno"]
      """  The serial number of the asset.  """  
      self.Manufacturer:str = obj["Manufacturer"]
      """  The original manufacturer of the asset.  """  
      self.Model:str = obj["Model"]
      """  The model of the asset.  """  
      self.InsurancePolicy:str = obj["InsurancePolicy"]
      """  Insurance policy for the asset.  """  
      self.InsuranceCompany:str = obj["InsuranceCompany"]
      """  The insurance company.  """  
      self.InsurancePremium:int = obj["InsurancePremium"]
      """  Insurance premium  """  
      self.InsuranceRenewalDate:str = obj["InsuranceRenewalDate"]
      """  Insurance RenewalDate  """  
      self.InsuranceInsurer:str = obj["InsuranceInsurer"]
      """  The insurer.  """  
      self.LeaseFlag:bool = obj["LeaseFlag"]
      """  Flag the asset as leased.  """  
      self.LeaseValue:int = obj["LeaseValue"]
      """  Lease amount  """  
      self.LeaseMileage:int = obj["LeaseMileage"]
      """  Mileage limit of lease  """  
      self.LeaseEndDate:str = obj["LeaseEndDate"]
      """  End date of lease.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse where the asset is stored. This is for information purposes only. In the warehouse tracker no assets can be tracked.  """  
      self.BinNum:str = obj["BinNum"]
      """  The bin where the addition is stored. This is for information purposes only. In the bin tracker no assets can be tracked.  """  
      self.Location:str = obj["Location"]
      """  Freeform field for the location of tha aaset.  """  
      self.OverideCost:int = obj["OverideCost"]
      """  The overide cost is cost amount which is used instead of the asset cost amount for the calculation of a year depreciation.  """  
      self.ResidualValue:int = obj["ResidualValue"]
      """  Residual value of the asset  """  
      self.ReplaceValue:int = obj["ReplaceValue"]
      """  Replacement value of the asset. For information purposes only.  """  
      self.CYAdditionCost:int = obj["CYAdditionCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.CYDisposalCost:int = obj["CYDisposalCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.CYDisposalProceeds:int = obj["CYDisposalProceeds"]
      """  Disposal proceed amount.  """  
      self.CurrentCostvalue:int = obj["CurrentCostvalue"]
      """  Current cost value of the asset.  """  
      self.Acquire:int = obj["Acquire"]
      """  The amount the asset is acquired for.  """  
      self.ImageFileName:str = obj["ImageFileName"]
      """  Path and filename of asset image file.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the Company currency.  """  
      self.AssetStatus:str = obj["AssetStatus"]
      """  Current Status of the asset. Valid values are: 'NEW'; 'ACTIVE'; 'DISPOSED' or 'INACTIVE'.  """  
      self.AcquisitionCost:int = obj["AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the Asset with a project in the Project table.  This can be blank.  """  
      self.TagNum:str = obj["TagNum"]
      """  Tag number. This will keep the asset label.  """  
      self.CurrentGrantAmt:int = obj["CurrentGrantAmt"]
      """  The total Grant amount recorded for this Asset.  """  
      self.DocResidualValue:int = obj["DocResidualValue"]
      """  Residual value of the asset  """  
      self.DocReplaceValue:int = obj["DocReplaceValue"]
      """  Replacement value of the asset. For information purposes only.  """  
      self.DocCYAdditionCost:int = obj["DocCYAdditionCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.DocCYDisposalCost:int = obj["DocCYDisposalCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.DocAcquisitionCost:int = obj["DocAcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.DocCurrentGrantAmt:int = obj["DocCurrentGrantAmt"]
      """  The total Grant amount recorded for this Asset in document currency.  """  
      self.Rpt1ResidualValue:int = obj["Rpt1ResidualValue"]
      """  Residual value of the asset  """  
      self.Rpt1ReplaceValue:int = obj["Rpt1ReplaceValue"]
      """  Replacement value of the asset. For information purposes only.  """  
      self.Rpt1CYAdditionCost:int = obj["Rpt1CYAdditionCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt1CYDisposalCost:int = obj["Rpt1CYDisposalCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.Rpt1AcquisitionCost:int = obj["Rpt1AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.Rpt1CurrentGrantAmt:int = obj["Rpt1CurrentGrantAmt"]
      """  The total Grant amount recorded for this Asset in reporting currency.  """  
      self.Rpt2ResidualValue:int = obj["Rpt2ResidualValue"]
      """  Residual value of the asset  """  
      self.Rpt2ReplaceValue:int = obj["Rpt2ReplaceValue"]
      """  Replacement value of the asset. For information purposes only.  """  
      self.Rpt2CYAdditionCost:int = obj["Rpt2CYAdditionCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt2CYDisposalCost:int = obj["Rpt2CYDisposalCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.Rpt2AcquisitionCost:int = obj["Rpt2AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.Rpt2CurrentGrantAmt:int = obj["Rpt2CurrentGrantAmt"]
      """  The total Grant amount recorded for this Asset in reporting currency.  """  
      self.Rpt3ResidualValue:int = obj["Rpt3ResidualValue"]
      """  Residual value of the asset  """  
      self.Rpt3ReplaceValue:int = obj["Rpt3ReplaceValue"]
      """  Replacement value of the asset. For information purposes only.  """  
      self.Rpt3CYAdditionCost:int = obj["Rpt3CYAdditionCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt3CYDisposalCost:int = obj["Rpt3CYDisposalCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.Rpt3AcquisitionCost:int = obj["Rpt3AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.Rpt3CurrentGrantAmt:int = obj["Rpt3CurrentGrantAmt"]
      """  The total Grant amount recorded for this Asset in reporting currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.MXTaxCode:str = obj["MXTaxCode"]
      """  Tax Code (Mexico Localization field)  """  
      self.MXTaxRate:str = obj["MXTaxRate"]
      """  Tax Rate (Mexico Localization field)  """  
      self.MXInvestAmount:int = obj["MXInvestAmount"]
      """  Investment Value (Mexico Localization field)  """  
      self.MXTaxAmount:int = obj["MXTaxAmount"]
      """  Mexico Tax Amount (Mexico Localization field)  """  
      self.MXAnnualDepre:int = obj["MXAnnualDepre"]
      """  Annual depreciation Percentage (Mexico Localization field)  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line  (Mexico Localization field)  """  
      self.MXAssetLife:int = obj["MXAssetLife"]
      """  Mexico Asset Life (Mexico Localization field)  """  
      self.CYImpairCost:int = obj["CYImpairCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.DocCYImpairCost:int = obj["DocCYImpairCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.Rpt1CYImpairCost:int = obj["Rpt1CYImpairCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.Rpt2CYImpairCost:int = obj["Rpt2CYImpairCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.Rpt3CYImpairCost:int = obj["Rpt3CYImpairCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.DocCurrentCostValue:int = obj["DocCurrentCostValue"]
      """  Current cost value of the asset in document currency.  """  
      self.Rpt1CurrentCostvalue:int = obj["Rpt1CurrentCostvalue"]
      """  Current cost value of the asset in reporting currency.  """  
      self.Rpt2CurrentCostvalue:int = obj["Rpt2CurrentCostvalue"]
      """  Current cost value of the asset in reporting currency.  """  
      self.Rpt3CurrentCostValue:int = obj["Rpt3CurrentCostValue"]
      """  Current cost value of the asset in reporting currency.  """  
      self.LocID:str = obj["LocID"]
      """  Location ID.  """  
      self.DocCYDisposalProceeds:int = obj["DocCYDisposalProceeds"]
      """  Disposal proceed amount.  """  
      self.Rpt1CYDisposalProceeds:int = obj["Rpt1CYDisposalProceeds"]
      """  Disposal proceed amount.  """  
      self.Rpt2CYDisposalProceeds:int = obj["Rpt2CYDisposalProceeds"]
      """  Disposal proceed amount.  """  
      self.Rpt3CYDisposalProceeds:int = obj["Rpt3CYDisposalProceeds"]
      """  Disposal proceed amount.  """  
      self.CYAdditionGrant:int = obj["CYAdditionGrant"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.DocCYAdditionGrant:int = obj["DocCYAdditionGrant"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt1CYAdditionGrant:int = obj["Rpt1CYAdditionGrant"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt2CYAdditionGrant:int = obj["Rpt2CYAdditionGrant"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt3CYAdditionGrant:int = obj["Rpt3CYAdditionGrant"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  """  
      self.LastCalDate:str = obj["LastCalDate"]
      """  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.DepRecalcNeeded:bool = obj["DepRecalcNeeded"]
      """  System maintained field.  Indicates that asset depreciation needs to be recalculated for this asset.  """  
      self.EquipID:str = obj["EquipID"]
      """  Descriptive code to uniquely identify the Equipment.  """  
      self.Brand:str = obj["Brand"]
      """  Brand of equipment  """  
      self.AssetUnits:int = obj["AssetUnits"]
      """  This is the total number of units recorded for this asset.  This is not directly maintained by user.  This is increased when you add/transfer asset "qty" from the Asset Addition Entry.  This is decreased when you dispose/transfer asset "qty" from the Asset Disposal Entry.  This field is not a true quantity field since we do not perform any unit of measure conversion when we update AssetUnits based on the transferred qty.  """  
      self.Lineage:str = obj["Lineage"]
      """  Stores the keys (assetnum) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  """  
      self.DocInsurancePremium:int = obj["DocInsurancePremium"]
      """  Insurance premium in document currency.  """  
      self.Rpt1InsurancePremium:int = obj["Rpt1InsurancePremium"]
      """  Insurance premium in Reporting Currency.  """  
      self.Rpt2InsurancePremium:int = obj["Rpt2InsurancePremium"]
      """  Insurance premium in Reporting Currency.  """  
      self.Rpt3InsurancePremium:int = obj["Rpt3InsurancePremium"]
      """  Insurance premium in Reporting Currency.  """  
      self.DocLeaseValue:int = obj["DocLeaseValue"]
      """  Lease amount in document currency.  """  
      self.Rpt1LeaseValue:int = obj["Rpt1LeaseValue"]
      """  Lease amount in Reporting Currency.  """  
      self.Rpt2LeaseValue:int = obj["Rpt2LeaseValue"]
      """  Lease amount in Rocument Currency.  """  
      self.Rpt3LeaseValue:int = obj["Rpt3LeaseValue"]
      """  Lease amount in Reporting Currency.  """  
      self.InsuranceValue:int = obj["InsuranceValue"]
      """  Insurance Value  """  
      self.DocInsuranceValue:int = obj["DocInsuranceValue"]
      """  Insurance Value in document currency.  """  
      self.Rpt1InsuranceValue:int = obj["Rpt1InsuranceValue"]
      """  Insurance Value in Reporting Currency.  """  
      self.Rpt2InsuranceValue:int = obj["Rpt2InsuranceValue"]
      """  Insurance Value in Reporting Currency.  """  
      self.Rpt3InsuranceValue:int = obj["Rpt3InsuranceValue"]
      """  Insurance Value in Reporting Currency.  """  
      self.InsPremiumModifier:str = obj["InsPremiumModifier"]
      """  The premium modifier expresses if the Insurance Premium is per Period or per Year.  Values are: Periods and Years.  """  
      self.LeaseModifier:str = obj["LeaseModifier"]
      """  The lease value modifier expresses if the Lease Value is per Period or per Year.  Values are: Periods and Years.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  The Project Phase ID of this asset.  """  
      self.LeaseNum:str = obj["LeaseNum"]
      """  Lease Number of the asset.  """  
      self.LeaseCompany:str = obj["LeaseCompany"]
      """  The Leasing Company.  """  
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
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.Department:str = obj["Department"]
      """  Department  """  
      self.UOM:str = obj["UOM"]
      """  UOM  """  
      self.CNUsageStatus:str = obj["CNUsageStatus"]
      """  CNUsageStatus  """  
      self.CNUsagePercent:int = obj["CNUsagePercent"]
      """  CNUsagePercent  """  
      self.CNImportedForProcessingTrade:bool = obj["CNImportedForProcessingTrade"]
      """  Imported for Processing Trade  """  
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      """  Declaration Bill  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  HS Commodity Code  """  
      self.CNDeclarationDate:str = obj["CNDeclarationDate"]
      """  Declaration Date  """  
      self.CNControlDueDate:str = obj["CNControlDueDate"]
      """  Control Due Date  """  
      self.CNManufacturingDate:str = obj["CNManufacturingDate"]
      """  Manufacturing Date  """  
      self.CNOrigCountryNum:int = obj["CNOrigCountryNum"]
      """  Country of Origin  """  
      self.CNSpecification:str = obj["CNSpecification"]
      """  Specification  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BinDescription:str = obj["BinDescription"]
      self.CNDeptChangeReason:str = obj["CNDeptChangeReason"]
      """  CNDeptChangeReason  """  
      self.CNLocChangeReason:str = obj["CNLocChangeReason"]
      """  CNLocChangeReason  """  
      self.IsPosted:bool = obj["IsPosted"]
      self.MXTaxCatID:str = obj["MXTaxCatID"]
      """  Mexico Localization Field  """  
      self.PhaseDescription:str = obj["PhaseDescription"]
      self.AdditionSpread:bool = obj["AdditionSpread"]
      self.EquipCreate:bool = obj["EquipCreate"]
      self.FinalSpread:bool = obj["FinalSpread"]
      self.ImagePath:str = obj["ImagePath"]
      """  Path name of the Asset Image or Photo  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssetGrpDescDescription:str = obj["AssetGrpDescDescription"]
      self.ClassDescription:str = obj["ClassDescription"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.LocIDDescription:str = obj["LocIDDescription"]
      self.MachineDescDescription:str = obj["MachineDescDescription"]
      self.ResrceGrpDescDescription:str = obj["ResrceGrpDescDescription"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CalcTaxAmtLine_input:
   """ Required : 
   ipSupplier
   ipInvoiceNum
   ipInvoiceLine
   ipTaxCode
   ipRateCode
   """  
   def __init__(self, obj):
      self.ipSupplier:int = obj["ipSupplier"]
      """  Supplier Invoice Line that was entered.  """  
      self.ipInvoiceNum:str = obj["ipInvoiceNum"]
      """  Invoice Num that was entered.  """  
      self.ipInvoiceLine:int = obj["ipInvoiceLine"]
      """  Invoice Line that was entered.  """  
      self.ipTaxCode:str = obj["ipTaxCode"]
      """  Tax Code Invoice Line that was entered.  """  
      self.ipRateCode:str = obj["ipRateCode"]
      """  Rate Code Invoice Line that was entered.  """  
      pass

class CalcTaxAmtLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opInvestAmount:int = obj["parameters"]
      self.opTaxAmount:int = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeAssetMethod_input:
   """ Required : 
   ipAssetMethod
   ds
   """  
   def __init__(self, obj):
      self.ipAssetMethod:str = obj["ipAssetMethod"]
      """  The Method proposed value  """  
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

class ChangeAssetMethod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeAssetRegister_input:
   """ Required : 
   ipAssetRegister
   ds
   """  
   def __init__(self, obj):
      self.ipAssetRegister:str = obj["ipAssetRegister"]
      """  The Register proposed value  """  
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

class ChangeAssetRegister_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   assetNum
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Duplicate_input:
   """ Required : 
   sourceAssetNum
   assetNum
   assetDesc
   acquiredDate
   commissionedDate
   dupCost
   additionDate
   dateKind
   """  
   def __init__(self, obj):
      self.sourceAssetNum:str = obj["sourceAssetNum"]
      """  Source Asset ID  """  
      self.assetNum:str = obj["assetNum"]
      """  New Asset Number  """  
      self.assetDesc:str = obj["assetDesc"]
      """  New Asset Description  """  
      self.acquiredDate:str = obj["acquiredDate"]
      """  New Acquisition Date  """  
      self.commissionedDate:str = obj["commissionedDate"]
      """  New Placed In Service Date  """  
      self.dupCost:bool = obj["dupCost"]
      """  Indicates whether an Addition is to be created. When true, Source Asset Cost is used as Addition Cost  """  
      self.additionDate:str = obj["additionDate"]
      """  Addition Date. Used when ipDupCost is true  """  
      self.dateKind:str = obj["dateKind"]
      """  Date Kind. When ACQ, additionDate is used for Acquisition and Placed In Service Dates; when PSD, additionDate is used for Placed in Service Date  """  
      pass

class Duplicate_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FAssetTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.warning:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_ChildAssetsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset Number  """  
      self.AssetDescription:str = obj["AssetDescription"]
      """  Asset Description  """  
      self.ParentAsset:str = obj["ParentAsset"]
      """  Parent Asset Number  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.AssetSeq:int = obj["AssetSeq"]
      """  Asset Sequence  """  
      self.ParentAssetSeq:int = obj["ParentAssetSeq"]
      """  Parent Asset Sequence  """  
      self.AssetStatus:str = obj["AssetStatus"]
      self.TagNum:str = obj["TagNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAssetAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.AssetNum:str = obj["AssetNum"]
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

class Erp_Tablesets_FAssetDtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.AssetNum:str = obj["AssetNum"]
      self.AssetRegID:str = obj["AssetRegID"]
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

class Erp_Tablesets_FAssetDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the asset.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Identifier of the asset  """  
      self.AssetRegID:str = obj["AssetRegID"]
      """  Identifier of the Asset Register.  """  
      self.AdditionSpread:bool = obj["AdditionSpread"]
      """  Flag to indicate that calculated depreciation between the fiscal period of asset commission date and the first open fiscal period should be distributed over all open remaining periods of the first depreciation year or when false then the calculated depreciation will be applied to the first open fiscal period.  """  
      self.SpreadCode:str = obj["SpreadCode"]
      """  Identifier of the spread code table that will be used for the Addition Spread option.  """  
      self.LifeModifier:str = obj["LifeModifier"]
      """  In case of life depreciation method the life modifier expresses the unit of measure of life. Values are: Periods and Years.  """  
      self.AnnualDepRate:int = obj["AnnualDepRate"]
      """  The Depreciation Rate that will be used to calculate the Annual Charge.  """  
      self.AssetLife:int = obj["AssetLife"]
      """  Number of periods or years - unit defined in the Life Modifier.  """  
      self.CYOpenDepn:int = obj["CYOpenDepn"]
      """  Current year opening depreciation  """  
      self.CYOpenBookValue:int = obj["CYOpenBookValue"]
      """  Current year opening bookvalue  """  
      self.CYOpenGrantDepn:int = obj["CYOpenGrantDepn"]
      """  Current year opening grant depreciation  """  
      self.CYOpenGrantBookValue:int = obj["CYOpenGrantBookValue"]
      """  Current year opening grant bookvalue  """  
      self.CYAddPrevDepn:int = obj["CYAddPrevDepn"]
      """  Depreciation applied in previous years through addition this year.  """  
      self.CYAddCurrDepn:int = obj["CYAddCurrDepn"]
      """  Current year depreciation  """  
      self.CYAddBookvalue:int = obj["CYAddBookvalue"]
      """  Current year Addition Bookvalue is the addition bookvalue added to the asset  this year.  """  
      self.CYDispPrevDepn:int = obj["CYDispPrevDepn"]
      """  Depreciation applied in previous years through disposal this year.  """  
      self.CYDispCurrDepn:int = obj["CYDispCurrDepn"]
      """  Depreciation applied this year through addition this year.  """  
      self.CYDispBookValue:int = obj["CYDispBookValue"]
      """  Current year disposal bookvalue is the disposal bookvalue disposed from the asset this year.  """  
      self.CurrentPrevYearDepn:int = obj["CurrentPrevYearDepn"]
      """  Depreciated in previous years  """  
      self.CurrentPostedDepn:int = obj["CurrentPostedDepn"]
      """  Depreciated (and posted) in the current year.  """  
      self.CurrentBookvalue:int = obj["CurrentBookvalue"]
      """  The current bookvalue.  """  
      self.CurrentUnpostedDepn:int = obj["CurrentUnpostedDepn"]
      """  Depreciations open for this year.  """  
      self.CurrentYEBookvalue:int = obj["CurrentYEBookvalue"]
      """  The projected bookvalue at the end of this year.  """  
      self.AssetMethod:str = obj["AssetMethod"]
      """  Identifier of the depreciation method table.  """  
      self.BookID:str = obj["BookID"]
      """  The G/L Book that will be used when posting asset depreciations against this register.  """  
      self.CalendarID:str = obj["CalendarID"]
      """  Identifies the Asset Calendar used when posting asset activities.  This calendar could be different from the G/L Book Fiscal Calendar.  """  
      self.DepConvention:str = obj["DepConvention"]
      """  Convention used for the depreciation calculation of the asset.  This will determine how depreciation is prorated for the year in which the asset is placed in service.  Valid values are: "HY" (Half Year); "MM" (Mid Month); "QR" (Quarter); "MQ" (Mid Quarter); "FM" (Full Month); "EM" (Entire Month); "SD" (Service Date), "NM" (Next Month), and "AD" (Acquisition Date).  This field can be blank.  """  
      self.RetroAdjust:bool = obj["RetroAdjust"]
      """  Flag to indicate if the changes in asset depreciation costs, due to an adjustment of asset cost or depreciation parameters, will affect the current year depreciation calculation.  """  
      self.ProdUnitSpread:str = obj["ProdUnitSpread"]
      """  Production Unit Spread Code.  """  
      self.TotalProdUnit:int = obj["TotalProdUnit"]
      """  Total Production Units.  This could be the total production units per Year or per Period depending on the depreciation charge basis of the asset depreciation method.  """  
      self.AnnualFixedValue:int = obj["AnnualFixedValue"]
      """  The Fixed Value that will be used as the Annual Charge amount during the asset depreciation calculation.  This field is only used if the depreciation method is set up to 'Use Fixed Value' for the annual charge calculation.  """  
      self.AnnualSpread:str = obj["AnnualSpread"]
      """  Annual Charge Spread Code  """  
      self.PeriodFixedValue:int = obj["PeriodFixedValue"]
      """  The Fixed Value that will be used as the Period Charge amount during the asset period depreciation calculation.  This field is only used if the depreciation method is set up to 'Use Fixed Value' for the period charge calculation.  """  
      self.PeriodSpread:str = obj["PeriodSpread"]
      """  Period Charge Spread  """  
      self.PeriodRateSpread:str = obj["PeriodRateSpread"]
      """  Spread Code used to determine the spread values used when prorating Annual Charge.  """  
      self.FinalSpread:str = obj["FinalSpread"]
      """  Final Spread Code  """  
      self.MethodSwitched:bool = obj["MethodSwitched"]
      """  Indicates if this asset register detail has already switched or used the alternate depreciation method. An asset register is only allowed to switch to an alternate depreciation method once and cannot switch back to original method.  """  
      self.AltAssetMethod:str = obj["AltAssetMethod"]
      """  Alternate Depreciation Method  """  
      self.DocCurrentPrevYearDepn:int = obj["DocCurrentPrevYearDepn"]
      """  Depreciated in previous years  """  
      self.DocCurrentPostedDepn:int = obj["DocCurrentPostedDepn"]
      """  Depreciated (and posted) in the current year.  """  
      self.DocCurrentBookvalue:int = obj["DocCurrentBookvalue"]
      """  The current bookvalue.  """  
      self.DocCurrentUnpostedDepn:int = obj["DocCurrentUnpostedDepn"]
      """  Depreciations open for this year.  """  
      self.DocCurrentYEBookvalue:int = obj["DocCurrentYEBookvalue"]
      """  The projected bookvalue at the end of this year.  """  
      self.Rpt1CurrentPrevYearDepn:int = obj["Rpt1CurrentPrevYearDepn"]
      """  Depreciated in previous years  """  
      self.Rpt1CurrentPostedDepn:int = obj["Rpt1CurrentPostedDepn"]
      """  Depreciated (and posted) in the current year.  """  
      self.Rpt1CurrentBookvalue:int = obj["Rpt1CurrentBookvalue"]
      """  The current bookvalue.  """  
      self.Rpt1CurrentUnpostedDepn:int = obj["Rpt1CurrentUnpostedDepn"]
      """  Depreciations open for this year.  """  
      self.Rpt1CurrentYEBookvalue:int = obj["Rpt1CurrentYEBookvalue"]
      """  The projected bookvalue at the end of this year.  """  
      self.Rpt2CurrentPrevYearDepn:int = obj["Rpt2CurrentPrevYearDepn"]
      """  Depreciated in previous years  """  
      self.Rpt2CurrentPostedDepn:int = obj["Rpt2CurrentPostedDepn"]
      """  Depreciated (and posted) in the current year.  """  
      self.Rpt2CurrentBookvalue:int = obj["Rpt2CurrentBookvalue"]
      """  The current bookvalue.  """  
      self.Rpt2CurrentUnpostedDepn:int = obj["Rpt2CurrentUnpostedDepn"]
      """  Depreciations open for this year.  """  
      self.Rpt2CurrentYEBookvalue:int = obj["Rpt2CurrentYEBookvalue"]
      """  The projected bookvalue at the end of this year.  """  
      self.Rpt3CurrentPrevYearDepn:int = obj["Rpt3CurrentPrevYearDepn"]
      """  Depreciated in previous years  """  
      self.Rpt3CurrentPostedDepn:int = obj["Rpt3CurrentPostedDepn"]
      """  Depreciated (and posted) in the current year.  """  
      self.Rpt3CurrentBookvalue:int = obj["Rpt3CurrentBookvalue"]
      """  The current bookvalue.  """  
      self.Rpt3CurrentUnpostedDepn:int = obj["Rpt3CurrentUnpostedDepn"]
      """  Depreciations open for this year.  """  
      self.Rpt3CurrentYEBookvalue:int = obj["Rpt3CurrentYEBookvalue"]
      """  The projected bookvalue at the end of this year.  """  
      self.UseFinalSpread:bool = obj["UseFinalSpread"]
      """  Flag to indicate that the total of depreciations in the last year of depreciation should be distributed over all fiscal periods of the last year.  """  
      self.DepRecalcNeeded:bool = obj["DepRecalcNeeded"]
      """  System maintained field.  Indicates that asset depreciation needs to be recalculated for this depreciation method.  """  
      self.CurrentGrantPYDepn:int = obj["CurrentGrantPYDepn"]
      """  Grant Depreciation in previous years  """  
      self.CurrentGrantPostedDepn:int = obj["CurrentGrantPostedDepn"]
      """  Grant Depreciation (and posted) in the current year.  """  
      self.CurrentGrantBookValue:int = obj["CurrentGrantBookValue"]
      """  The current grant book value.  """  
      self.CurrentGrantUnpostedDepn:int = obj["CurrentGrantUnpostedDepn"]
      """  Grant Depreciations open for this year.  """  
      self.CurrentGrantYEBookValue:int = obj["CurrentGrantYEBookValue"]
      """  The projected grant bookvalue at the end of this year.  """  
      self.DocCurrentGrantPYDepn:int = obj["DocCurrentGrantPYDepn"]
      """  Grant Depreciation in previous years  """  
      self.DocCurrentGrantPostedDepn:int = obj["DocCurrentGrantPostedDepn"]
      """  Grant Depreciation (and posted) in the current year.  """  
      self.DocCurrentGrantBookValue:int = obj["DocCurrentGrantBookValue"]
      """  The current grant book value.  """  
      self.DocCurrentGrantUnpostedDepn:int = obj["DocCurrentGrantUnpostedDepn"]
      """  Grant Depreciations open for this year.  """  
      self.DocCurrentGrantYEBookValue:int = obj["DocCurrentGrantYEBookValue"]
      """  The projected grant bookvalue at the end of this year.  """  
      self.Rpt1CurrentGrantPYDepn:int = obj["Rpt1CurrentGrantPYDepn"]
      """  Grant Depreciation in previous years  """  
      self.Rpt1CurrentGrantPostedDepn:int = obj["Rpt1CurrentGrantPostedDepn"]
      """  Grant Depreciation (and posted) in the current year.  """  
      self.Rpt1CurrentGrantBookValue:int = obj["Rpt1CurrentGrantBookValue"]
      """  The current grant book value.  """  
      self.Rpt1CurrentGrantUnpostedDepn:int = obj["Rpt1CurrentGrantUnpostedDepn"]
      """  Grant Depreciations open for this year.  """  
      self.Rpt1CurrentGrantYEBookValue:int = obj["Rpt1CurrentGrantYEBookValue"]
      """  The projected grant bookvalue at the end of this year.  """  
      self.Rpt2CurrentGrantPYDepn:int = obj["Rpt2CurrentGrantPYDepn"]
      """  Grant Depreciation in previous years  """  
      self.Rpt2CurrentGrantPostedDepn:int = obj["Rpt2CurrentGrantPostedDepn"]
      """  Grant Depreciation (and posted) in the current year.  """  
      self.Rpt2CurrentGrantBookValue:int = obj["Rpt2CurrentGrantBookValue"]
      """  The current grant book value.  """  
      self.Rpt2CurrentGrantUnpostedDepn:int = obj["Rpt2CurrentGrantUnpostedDepn"]
      """  Grant Depreciations open for this year.  """  
      self.Rpt2CurrentGrantYEBookValue:int = obj["Rpt2CurrentGrantYEBookValue"]
      """  The projected grant bookvalue at the end of this year.  """  
      self.Rpt3CurrentGrantPYDepn:int = obj["Rpt3CurrentGrantPYDepn"]
      """  Grant Depreciation in previous years  """  
      self.Rpt3CurrentGrantPostedDepn:int = obj["Rpt3CurrentGrantPostedDepn"]
      """  Grant Depreciation (and posted) in the current year.  """  
      self.Rpt3CurrentGrantBookValue:int = obj["Rpt3CurrentGrantBookValue"]
      """  The current grant book value.  """  
      self.Rpt3CurrentGrantUnpostedDepn:int = obj["Rpt3CurrentGrantUnpostedDepn"]
      """  Grant Depreciations open for this year.  """  
      self.Rpt3CurrentGrantYEBookValue:int = obj["Rpt3CurrentGrantYEBookValue"]
      """  The projected grant bookvalue at the end of this year.  """  
      self.DocCYOpenBookValue:int = obj["DocCYOpenBookValue"]
      """  Current year opening bookvalue  """  
      self.DocCYAddPrevDepn:int = obj["DocCYAddPrevDepn"]
      """  Previous years addition depreciation  """  
      self.DocCYAddCurrDepn:int = obj["DocCYAddCurrDepn"]
      """  Current year addition depreciation  """  
      self.DocCYAddBookValue:int = obj["DocCYAddBookValue"]
      """  Current year Addition Bookvalue is the addition bookvalue added to the asset  this year.  """  
      self.DocCYDispPrevDepn:int = obj["DocCYDispPrevDepn"]
      """  Previous years Disposal depreciation  """  
      self.DocCYDispCurrDepn:int = obj["DocCYDispCurrDepn"]
      """  Current year Disposal depreciation  """  
      self.DocCYDispBookValue:int = obj["DocCYDispBookValue"]
      """  Current year disposal bookvalue is the disposal bookvalue disposed from the asset this year.  """  
      self.Rpt1CYOpenBookValue:int = obj["Rpt1CYOpenBookValue"]
      """  Current year opening bookvalue  """  
      self.Rpt1CYAddPrevDepn:int = obj["Rpt1CYAddPrevDepn"]
      """  Previous years Addition depreciation  """  
      self.Rpt1CYAddCurrDepn:int = obj["Rpt1CYAddCurrDepn"]
      """  Current year Addition depreciation  """  
      self.Rpt1CYAddBookValue:int = obj["Rpt1CYAddBookValue"]
      """  Current year Addition Bookvalue is the addition bookvalue added to the asset  this year.  """  
      self.Rpt1CYDispPrevDepn:int = obj["Rpt1CYDispPrevDepn"]
      """  Previous years Disposal depreciation  """  
      self.Rpt1CYDispCurrDepn:int = obj["Rpt1CYDispCurrDepn"]
      """  Current year Disposal depreciation  """  
      self.Rpt1CYDispBookValue:int = obj["Rpt1CYDispBookValue"]
      """  Current year disposal bookvalue is the disposal bookvalue disposed from the asset this year.  """  
      self.Rpt2CYOpenBookValue:int = obj["Rpt2CYOpenBookValue"]
      """  Current year opening bookvalue  """  
      self.Rpt2CYAddPrevDepn:int = obj["Rpt2CYAddPrevDepn"]
      """  Previous years Addition depreciation  """  
      self.Rpt2CYAddCurrDepn:int = obj["Rpt2CYAddCurrDepn"]
      """  Current year Addition depreciation  """  
      self.Rpt2CYAddBookValue:int = obj["Rpt2CYAddBookValue"]
      """  Current year Addition Bookvalue is the addition bookvalue added to the asset  this year.  """  
      self.Rpt2CYDispPrevDepn:int = obj["Rpt2CYDispPrevDepn"]
      """  Previous years Disposal depreciation  """  
      self.Rpt2CYDispCurrDepn:int = obj["Rpt2CYDispCurrDepn"]
      """  Current year Disposal depreciation  """  
      self.Rpt2CYDispBookValue:int = obj["Rpt2CYDispBookValue"]
      """  Current year disposal bookvalue is the disposal bookvalue disposed from the asset this year.  """  
      self.Rpt3CYOpenBookValue:int = obj["Rpt3CYOpenBookValue"]
      """  Current year opening bookvalue  """  
      self.Rpt3CYAddPrevDepn:int = obj["Rpt3CYAddPrevDepn"]
      """  Previous years Addition depreciation  """  
      self.Rpt3CYAddCurrDepn:int = obj["Rpt3CYAddCurrDepn"]
      """  Current year Addition depreciation  """  
      self.Rpt3CYAddBookValue:int = obj["Rpt3CYAddBookValue"]
      """  Current year Addition Bookvalue is the addition bookvalue added to the asset  this year.  """  
      self.Rpt3CYDispPrevDepn:int = obj["Rpt3CYDispPrevDepn"]
      """  Previous years Disposal depreciation  """  
      self.Rpt3CYDispCurrDepn:int = obj["Rpt3CYDispCurrDepn"]
      """  Current year Disposal depreciation  """  
      self.Rpt3CYDispBookValue:int = obj["Rpt3CYDispBookValue"]
      """  Current year disposal bookvalue is the disposal bookvalue disposed from the asset this year.  """  
      self.DocCYOpenGrantDepn:int = obj["DocCYOpenGrantDepn"]
      """  Current year opening grant depreciation  """  
      self.Rpt1CYOpenGrantDepn:int = obj["Rpt1CYOpenGrantDepn"]
      """  Current year opening grant depreciation  """  
      self.Rpt2CYOpenGrantDepn:int = obj["Rpt2CYOpenGrantDepn"]
      """  Current year opening grant depreciation  """  
      self.Rpt3CYOpenGrantDepn:int = obj["Rpt3CYOpenGrantDepn"]
      """  Current year opening grant depreciation  """  
      self.DepRecalcDate:str = obj["DepRecalcDate"]
      """  The last depreciation recalculation apply date.  This is the date used to get the exchange rate for the depreciation calculation process.  """  
      self.InitBookValue:int = obj["InitBookValue"]
      """  This is the initial book value of the entire asset depreciation schedule.  """  
      self.DocInitBookValue:int = obj["DocInitBookValue"]
      """  This is the Initial book value of the entire asset depreciation schedule.  """  
      self.Rpt1InitBookValue:int = obj["Rpt1InitBookValue"]
      """  This is the Initial book value of the entire asset depreciation schedule.  """  
      self.Rpt2InitBookValue:int = obj["Rpt2InitBookValue"]
      """  This is the Initial book value of the entire asset depreciation schedule.  """  
      self.Rpt3InitBookValue:int = obj["Rpt3InitBookValue"]
      """  This is the Initial book value of the entire asset depreciation schedule.  """  
      self.InitGrantBookValue:int = obj["InitGrantBookValue"]
      """  This is the Initial grant book value of the entire asset depreciation schedule.  """  
      self.DocInitGrantBookValue:int = obj["DocInitGrantBookValue"]
      """  This is the Initial grant book value of the entire asset depreciation schedule.  """  
      self.Rpt1InitGrantBookValue:int = obj["Rpt1InitGrantBookValue"]
      """  This is the Initial grant book value of the entire asset depreciation schedule.  """  
      self.Rpt2InitGrantBookValue:int = obj["Rpt2InitGrantBookValue"]
      """  This is the Initial grant book value of the entire asset depreciation schedule.  """  
      self.Rpt3InitGrantBookValue:int = obj["Rpt3InitGrantBookValue"]
      """  This is the Initial grant book value of the entire asset depreciation schedule.  """  
      self.CYImpBookValue:int = obj["CYImpBookValue"]
      """  Current year Impairment Bookvalue is the impairment bookvalue subtracted from the asset this year.  """  
      self.CYDispGrantPrevDepn:int = obj["CYDispGrantPrevDepn"]
      """  Previous years Disposal Grant depreciation  """  
      self.CYDispGrantCurrDepn:int = obj["CYDispGrantCurrDepn"]
      """  Current year Disposal Grant depreciation  """  
      self.CYDispGrantBookValue:int = obj["CYDispGrantBookValue"]
      """  Current year disposal grant bookvalue is the disposal grant bookvalue disposed from the asset this year.  """  
      self.DocCYOpenGrantBookValue:int = obj["DocCYOpenGrantBookValue"]
      """  Current year opening grant bookvalue  """  
      self.DocCYImpBookValue:int = obj["DocCYImpBookValue"]
      """  Current year Impairment Bookvalue is the impairment bookvalue subtracted from the asset this year.  """  
      self.DocCYDispGrantPrevDepn:int = obj["DocCYDispGrantPrevDepn"]
      """  Previous years Disposal Grant depreciation  """  
      self.DocCYDispGrantCurrDepn:int = obj["DocCYDispGrantCurrDepn"]
      """  Current year Disposal Grant depreciation  """  
      self.DocCYDispGrantBookValue:int = obj["DocCYDispGrantBookValue"]
      """  Current year disposal grant bookvalue is the disposal grant bookvalue disposed from the asset this year.  """  
      self.Rpt1CYOpenGrantBookValue:int = obj["Rpt1CYOpenGrantBookValue"]
      """  Current year opening grant bookvalue  """  
      self.Rpt1CYImpBookValue:int = obj["Rpt1CYImpBookValue"]
      """  Current year Impairment Bookvalue is the impairment bookvalue subtracted from the asset this year.  """  
      self.Rpt1CYDispGrantPrevDepn:int = obj["Rpt1CYDispGrantPrevDepn"]
      """  Previous years Disposal Grant depreciation  """  
      self.Rpt1CYDispGrantCurrDepn:int = obj["Rpt1CYDispGrantCurrDepn"]
      """  Current year Disposal Grant depreciation  """  
      self.Rpt1CYDispGrantBookValue:int = obj["Rpt1CYDispGrantBookValue"]
      """  Current year disposal grant bookvalue is the disposal grant bookvalue disposed from the asset this year.  """  
      self.Rpt2CYOpenGrantBookValue:int = obj["Rpt2CYOpenGrantBookValue"]
      """  Current year opening grant bookvalue  """  
      self.Rpt2CYImpBookValue:int = obj["Rpt2CYImpBookValue"]
      """  Current year Impairment Bookvalue is the impairment bookvalue subtracted from the asset this year.  """  
      self.Rpt2CYDispGrantPrevDepn:int = obj["Rpt2CYDispGrantPrevDepn"]
      """  Previous years Disposal Grant depreciation  """  
      self.Rpt2CYDispGrantCurrDepn:int = obj["Rpt2CYDispGrantCurrDepn"]
      """  Current year Disposal Grant depreciation  """  
      self.Rpt2CYDispGrantBookValue:int = obj["Rpt2CYDispGrantBookValue"]
      """  Current year disposal grant bookvalue is the disposal grant bookvalue disposed from the asset this year.  """  
      self.Rpt3CYOpenGrantBookValue:int = obj["Rpt3CYOpenGrantBookValue"]
      """  Current year opening grant bookvalue  """  
      self.Rpt3CYImpBookValue:int = obj["Rpt3CYImpBookValue"]
      """  Current year Impairment Bookvalue is the impairment bookvalue subtracted from the asset this year.  """  
      self.Rpt3CYDispGrantPrevDepn:int = obj["Rpt3CYDispGrantPrevDepn"]
      """  Previous years Disposal Grant depreciation  """  
      self.Rpt3CYDispGrantCurrDepn:int = obj["Rpt3CYDispGrantCurrDepn"]
      """  Current year Disposal Grant depreciation  """  
      self.Rpt3CYDispGrantBookValue:int = obj["Rpt3CYDispGrantBookValue"]
      """  Current year disposal grant bookvalue is the disposal grant bookvalue disposed from the asset this year.  """  
      self.DocCYOpenDepn:int = obj["DocCYOpenDepn"]
      """  Current year opening depreciation  """  
      self.Rpt1CYOpenDepn:int = obj["Rpt1CYOpenDepn"]
      """  Current year opening depreciation  """  
      self.Rpt2CYOpenDepn:int = obj["Rpt2CYOpenDepn"]
      """  Current year opening depreciation  """  
      self.Rpt3CYOpenDepn:int = obj["Rpt3CYOpenDepn"]
      """  Current year opening depreciation  """  
      self.CurrentActPrevDepn:int = obj["CurrentActPrevDepn"]
      """  Actual posted depreciation recorded for the previous years.  This depreciation amount is not affected by the disposal depreciation.  """  
      self.CurrentActPostedDepn:int = obj["CurrentActPostedDepn"]
      """  Actual posted depreciation recorded for the current year.  This depreciation amount is not affected by the disposal depreciation.  """  
      self.DocCurrentActPrevDepn:int = obj["DocCurrentActPrevDepn"]
      """  Actual posted depreciation recorded for the previous years.  This depreciation amount is not affected by the disposal depreciation.  """  
      self.DocCurrentActPostedDepn:int = obj["DocCurrentActPostedDepn"]
      """  Actual posted depreciation recorded for the current year.  This depreciation amount is not affected by the disposal depreciation.  """  
      self.Rpt1CurrentActPrevDepn:int = obj["Rpt1CurrentActPrevDepn"]
      """  Actual posted depreciation recorded for the previous years.  This depreciation amount is not affected by the disposal depreciation.  """  
      self.Rpt1CurrentActPostedDepn:int = obj["Rpt1CurrentActPostedDepn"]
      """  Actual posted depreciation recorded for the current year.  This depreciation amount is not affected by the disposal depreciation.  """  
      self.Rpt2CurrentActPrevDepn:int = obj["Rpt2CurrentActPrevDepn"]
      """  Actual posted depreciation recorded for the previous years.  This depreciation amount is not affected by the disposal depreciation.  """  
      self.Rpt2CurrentActPostedDepn:int = obj["Rpt2CurrentActPostedDepn"]
      """  Actual posted depreciation recorded for the current year.  This depreciation amount is not affected by the disposal depreciation.  """  
      self.Rpt3CurrentActPrevDepn:int = obj["Rpt3CurrentActPrevDepn"]
      """  Actual posted depreciation recorded for the previous years.  This depreciation amount is not affected by the disposal depreciation.  """  
      self.Rpt3CurrentActPostedDepn:int = obj["Rpt3CurrentActPostedDepn"]
      """  Actual posted depreciation recorded for the current year.  This depreciation amount is not affected by the disposal depreciation.  """  
      self.CYAddGrantPrevDepn:int = obj["CYAddGrantPrevDepn"]
      """  Previous years Addition Grant depreciation  """  
      self.CYAddGrantCurrDepn:int = obj["CYAddGrantCurrDepn"]
      """  Previous years Addition Grant depreciation  """  
      self.CYAddGrantBookValue:int = obj["CYAddGrantBookValue"]
      """  Current year addition grant bookvalue is the addition grant bookvalue added to the asset this year.  """  
      self.DocCYAddGrantPrevDepn:int = obj["DocCYAddGrantPrevDepn"]
      """  Previous years Addition Grant depreciation  """  
      self.DocCYAddGrantCurrDepn:int = obj["DocCYAddGrantCurrDepn"]
      """  Current year Addition Grant depreciation  """  
      self.DocCYAddGrantBookValue:int = obj["DocCYAddGrantBookValue"]
      """  Current year addition grant bookvalue is the addition grant bookvalue added to the asset this year.  """  
      self.Rpt1CYAddGrantPrevDepn:int = obj["Rpt1CYAddGrantPrevDepn"]
      """  Previous years Addition Grant depreciation  """  
      self.Rpt1CYAddGrantCurrDepn:int = obj["Rpt1CYAddGrantCurrDepn"]
      """  Current year Addition Grant depreciation  """  
      self.Rpt1CYAddGrantBookValue:int = obj["Rpt1CYAddGrantBookValue"]
      """  Current year addition grant bookvalue is the addition grant bookvalue added to the asset this year.  """  
      self.Rpt2CYAddGrantPrevDepn:int = obj["Rpt2CYAddGrantPrevDepn"]
      """  Previous years Addition Grant depreciation  """  
      self.Rpt2CYAddGrantCurrDepn:int = obj["Rpt2CYAddGrantCurrDepn"]
      """  Current year Addition Grant depreciation  """  
      self.Rpt2CYAddGrantBookValue:int = obj["Rpt2CYAddGrantBookValue"]
      """  Current year addition grant bookvalue is the addition grant bookvalue added to the asset this year.  """  
      self.Rpt3CYAddGrantPrevDepn:int = obj["Rpt3CYAddGrantPrevDepn"]
      """  Previous years Addition Grant depreciation  """  
      self.Rpt3CYAddGrantCurrDepn:int = obj["Rpt3CYAddGrantCurrDepn"]
      """  Current year Addition Grant depreciation  """  
      self.Rpt3CYAddGrantBookValue:int = obj["Rpt3CYAddGrantBookValue"]
      """  Current year addition grant bookvalue is the addition grant bookvalue added to the asset this year.  """  
      self.Depreciate:bool = obj["Depreciate"]
      """  Depreciation Flag. When true then the asset register will be processed in the depreciation recalculation process and the depreciation posting process.  If set to false then all depreciation parameters are blank and not updatable.  """  
      self.CYOpenCost:int = obj["CYOpenCost"]
      """  Current year opening cost  """  
      self.DocCYOpenCost:int = obj["DocCYOpenCost"]
      """  Current year opening cost  """  
      self.Rpt1CYOpenCost:int = obj["Rpt1CYOpenCost"]
      """  Current year opening cost  """  
      self.Rpt2CYOpenCost:int = obj["Rpt2CYOpenCost"]
      """  Current year opening cost  """  
      self.Rpt3CYOpenCost:int = obj["Rpt3CYOpenCost"]
      """  Current year opening cost  """  
      self.CYOpenGrant:int = obj["CYOpenGrant"]
      """  Current year opening grant amount  """  
      self.DocCYOpenGrant:int = obj["DocCYOpenGrant"]
      """  Current year opening cost  """  
      self.Rpt1CYOpenGrant:int = obj["Rpt1CYOpenGrant"]
      """  Current year opening cost  """  
      self.Rpt2CYOpenGrant:int = obj["Rpt2CYOpenGrant"]
      """  Current year opening cost  """  
      self.Rpt3CYOpenGrant:int = obj["Rpt3CYOpenGrant"]
      """  Current year opening cost  """  
      self.CYAddCost:int = obj["CYAddCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.DocCYAddCost:int = obj["DocCYAddCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt1CYAddCost:int = obj["Rpt1CYAddCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt2CYAddCost:int = obj["Rpt2CYAddCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt3CYAddCost:int = obj["Rpt3CYAddCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.CYImpCost:int = obj["CYImpCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.DocCYImpCost:int = obj["DocCYImpCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.Rpt1CYImpCost:int = obj["Rpt1CYImpCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.Rpt2CYImpCost:int = obj["Rpt2CYImpCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.Rpt3CYImpCost:int = obj["Rpt3CYImpCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.CYDispCost:int = obj["CYDispCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.DocCYDispCost:int = obj["DocCYDispCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.Rpt1CYDispCost:int = obj["Rpt1CYDispCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.Rpt2CYDispCost:int = obj["Rpt2CYDispCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.Rpt3CYDispCost:int = obj["Rpt3CYDispCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.CYDispProceeds:int = obj["CYDispProceeds"]
      """  Disposal proceed amount.  """  
      self.DocCYDispProceeds:int = obj["DocCYDispProceeds"]
      """  Disposal proceed amount.  """  
      self.Rpt1CYDispProceeds:int = obj["Rpt1CYDispProceeds"]
      """  Disposal proceed amount.  """  
      self.Rpt2CYDispProceeds:int = obj["Rpt2CYDispProceeds"]
      """  Disposal proceed amount.  """  
      self.Rpt3CYDispProceeds:int = obj["Rpt3CYDispProceeds"]
      """  Disposal proceed amount.  """  
      self.CYDispProfit:int = obj["CYDispProfit"]
      """  Disposal profit/loss amount.  """  
      self.DocCYDispProfit:int = obj["DocCYDispProfit"]
      """  Disposal profit/loss amount.  """  
      self.Rpt1CYDispProfit:int = obj["Rpt1CYDispProfit"]
      """  Disposal profit/loss amount.  """  
      self.Rpt2CYDispProfit:int = obj["Rpt2CYDispProfit"]
      """  Disposal profit/loss amount.  """  
      self.Rpt3CYDispProfit:int = obj["Rpt3CYDispProfit"]
      """  Disposal profit/loss amount.  """  
      self.CYAddGrant:int = obj["CYAddGrant"]
      """  Current Addition Grant is the grant amount added to the asset  this year.  """  
      self.DocCYAddGrant:int = obj["DocCYAddGrant"]
      """  Current Addition Grant is the grant amount added to the asset  this year.  """  
      self.Rpt1CYAddGrant:int = obj["Rpt1CYAddGrant"]
      """  Current Addition Grant is the grant amount added to the asset  this year.  """  
      self.Rpt2CYAddGrant:int = obj["Rpt2CYAddGrant"]
      """  Current Addition Grant is the grant amount added to the asset  this year.  """  
      self.Rpt3CYAddGrant:int = obj["Rpt3CYAddGrant"]
      """  Current Addition Grant is the grant amount added to the asset  this year.  """  
      self.CurrentCostvalue:int = obj["CurrentCostvalue"]
      """  Current cost value of the asset.  """  
      self.DocCurrentCostvalue:int = obj["DocCurrentCostvalue"]
      """  Current cost value of the asset.  """  
      self.Rpt1CurrentCostvalue:int = obj["Rpt1CurrentCostvalue"]
      """  Current cost value of the asset.  """  
      self.Rpt2CurrentCostvalue:int = obj["Rpt2CurrentCostvalue"]
      """  Current cost value of the asset.  """  
      self.Rpt3CurrentCostvalue:int = obj["Rpt3CurrentCostvalue"]
      """  Current cost value of the asset.  """  
      self.CurrentGrantAmt:int = obj["CurrentGrantAmt"]
      """  Current Grant Amount of the asset.  """  
      self.DocCurrentGrantAmt:int = obj["DocCurrentGrantAmt"]
      """  Current Grant Amount of the asset.  """  
      self.Rpt1CurrentGrantAmt:int = obj["Rpt1CurrentGrantAmt"]
      """  Current Grant Amount of the asset.  """  
      self.Rpt2CurrentGrantAmt:int = obj["Rpt2CurrentGrantAmt"]
      """  Current Grant Amount of the asset.  """  
      self.Rpt3CurrentGrantAmt:int = obj["Rpt3CurrentGrantAmt"]
      """  Current Grant Amount of the asset.  """  
      self.RateFactor:int = obj["RateFactor"]
      """  The Rate Factor is used as a multiplier when calculating Annual Depreciation Charge using the Declining Balance formula.  """  
      self.ResidualValue:int = obj["ResidualValue"]
      """  Residual value of the asset  """  
      self.DocResidualValue:int = obj["DocResidualValue"]
      """  Residual value of the asset in document currency  """  
      self.Rpt1ResidualValue:int = obj["Rpt1ResidualValue"]
      """  Residual value of the asset in reporting currency  """  
      self.Rpt2ResidualValue:int = obj["Rpt2ResidualValue"]
      """  Residual value of the asset in reporting currency  """  
      self.Rpt3ResidualValue:int = obj["Rpt3ResidualValue"]
      """  Residual value of the asset in reporting currency  """  
      self.ReplaceValue:int = obj["ReplaceValue"]
      """  Replacement value of the asset. For information purposes only.  """  
      self.DocReplaceValue:int = obj["DocReplaceValue"]
      """  Replacement value of the asset in document currency. For information purposes only.  """  
      self.Rpt1ReplaceValue:int = obj["Rpt1ReplaceValue"]
      """  Replacement value of the asset in reporting currency. For information purposes only.  """  
      self.Rpt2ReplaceValue:int = obj["Rpt2ReplaceValue"]
      """  Replacement value of the asset in reporting currency. For information purposes only.  """  
      self.Rpt3ReplaceValue:int = obj["Rpt3ReplaceValue"]
      """  Replacement value of the asset in reporting currency. For information purposes only.  """  
      self.BookValueDate:str = obj["BookValueDate"]
      """  The end date of the last posted depreciation period that has affected the book value of this asset register detail.  """  
      self.DateSwitched:str = obj["DateSwitched"]
      """  This is the starting date of the fiscal year or fiscal period when the actual switch of the depreciation method to the alternative method happened.  """  
      self.CurrActGrantPostedDepn:int = obj["CurrActGrantPostedDepn"]
      """  Actual posted grant depreciation recorded for the current year.  This grant depreciation amount is not affected by the disposal grant depreciation.  """  
      self.DocCurrActGrantPostedDepn:int = obj["DocCurrActGrantPostedDepn"]
      """  Actual posted grant depreciation recorded for the current year.  This grant depreciation amount is not affected by the disposal grant depreciation.  """  
      self.Rpt1CurrActGrantPostedDepn:int = obj["Rpt1CurrActGrantPostedDepn"]
      """  Actual posted grant depreciation recorded for the current year.  This grant depreciation amount is not affected by the disposal grant depreciation.  """  
      self.Rpt2CurrActGrantPostedDepn:int = obj["Rpt2CurrActGrantPostedDepn"]
      """  Actual posted grant depreciation recorded for the current year.  This grant depreciation amount is not affected by the disposal grant depreciation.  """  
      self.Rpt3CurrActGrantPostedDepn:int = obj["Rpt3CurrActGrantPostedDepn"]
      """  Actual posted grant depreciation recorded for the current year.  This grant depreciation amount is not affected by the disposal grant depreciation.  """  
      self.AcquisitionCost:int = obj["AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.DocAcquisitionCost:int = obj["DocAcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.Rpt1AcquisitionCost:int = obj["Rpt1AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.Rpt2AcquisitionCost:int = obj["Rpt2AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.Rpt3AcquisitionCost:int = obj["Rpt3AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.CYDispGrant:int = obj["CYDispGrant"]
      """  Current Disposal Grant is the grant amount disposed from the asset  this year.  """  
      self.DocCYDispGrant:int = obj["DocCYDispGrant"]
      """  Current Disposal Grant is the grant amount disposed from the asset  this year.  """  
      self.Rpt1CYDispGrant:int = obj["Rpt1CYDispGrant"]
      """  Current Disposal Grant is the grant amount disposed from the asset  this year.  """  
      self.Rpt2CYDispGrant:int = obj["Rpt2CYDispGrant"]
      """  Current Disposal Grant is the grant amount disposed from the asset  this year.  """  
      self.Rpt3CYDispGrant:int = obj["Rpt3CYDispGrant"]
      """  Current Disposal Grant is the grant amount disposed from the asset  this year.  """  
      self.DynamicDepYear:bool = obj["DynamicDepYear"]
      """  Flag to indicate if dynamic depreciation year should be used instead of the Fiscal Year to influence the depreciation schedule.  """  
      self.CYRevalueGainLoss:int = obj["CYRevalueGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.DocCYRevalueGainLoss:int = obj["DocCYRevalueGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt1CYRevalueGainLoss:int = obj["Rpt1CYRevalueGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt2CYRevalueGainLoss:int = obj["Rpt2CYRevalueGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt3CYRevalueGainLoss:int = obj["Rpt3CYRevalueGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.CYDepRevalGainLoss:int = obj["CYDepRevalGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.DocCYDepRevalGainLoss:int = obj["DocCYDepRevalGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt1CYDepRevalGainLoss:int = obj["Rpt1CYDepRevalGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt2CYDepRevalGainLoss:int = obj["Rpt2CYDepRevalGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt3CYDepRevalGainLoss:int = obj["Rpt3CYDepRevalGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.CYRevGrantGainLoss:int = obj["CYRevGrantGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.DocCYRevGrantGainLoss:int = obj["DocCYRevGrantGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt1CYRevGrantGainLoss:int = obj["Rpt1CYRevGrantGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt2CYRevGrantGainLoss:int = obj["Rpt2CYRevGrantGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt3CYRevGrantGainLoss:int = obj["Rpt3CYRevGrantGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.CYDepRevGrantGainLoss:int = obj["CYDepRevGrantGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.DocCYDepRevGrantGainLoss:int = obj["DocCYDepRevGrantGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt1CYDepRevGrantGainLoss:int = obj["Rpt1CYDepRevGrantGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt2CYDepRevGrantGainLoss:int = obj["Rpt2CYDepRevGrantGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.Rpt3CYDepRevGrantGainLoss:int = obj["Rpt3CYDepRevGrantGainLoss"]
      """  The original Current Asset Cost before running the Asset Revaluation process.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DepOnDisposal:int = obj["DepOnDisposal"]
      """  Determines how depreciation is calculated in the period of disposal or revaluation.  """  
      self.ActDepStartDate:str = obj["ActDepStartDate"]
      """  Date of actual depreciation schedule start.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.CurrencySymbol:str = obj["CurrencySymbol"]
      self.CYDispTotalDepn:int = obj["CYDispTotalDepn"]
      """  Calculated field to store the sum of current year Disposal Current and Previous Depreciation.  """  
      self.DocCYDispTotalDepn:int = obj["DocCYDispTotalDepn"]
      """  Calculated field to store the sum of current year Disposal Current and Previous Depreciation.  """  
      self.DocRevalueGainLoss:int = obj["DocRevalueGainLoss"]
      """  Calculated field to store the total of all posted Revaluations as of the end of the current asset register year.  """  
      self.DocYTDAccumDepn:int = obj["DocYTDAccumDepn"]
      """  Calculated field to store the total of all posted Depreciations including the depreciations from Addition activities subtracted with depreciations from Disposals as of the end of the current asset register year.  """  
      self.DocYTDAddCost:int = obj["DocYTDAddCost"]
      """  Calculated field to store the total of all posted Addition Costs from the very first period up to the end of the current asset register year.  """  
      self.DocYTDDispCost:int = obj["DocYTDDispCost"]
      """  Calculated field to store the total of all posted Disposal Costs from the very first period up to the end of the current asset register year.  """  
      self.DocYTDGrantDepn:int = obj["DocYTDGrantDepn"]
      """  Calculated field to store the total of all posted Grant Depreciations including the depreciations from Addition activities as of the end of the current asset register year.  """  
      self.DocYTDImpCost:int = obj["DocYTDImpCost"]
      """  Calculated field to store the total of all posted Impairment Costs from the very first period up to the end of the current asset register year.  """  
      self.EnableAnnualDepRate:bool = obj["EnableAnnualDepRate"]
      self.EnableAssetLife:bool = obj["EnableAssetLife"]
      self.EnableProdUnitsSpread:bool = obj["EnableProdUnitsSpread"]
      self.EnableRateFactor:bool = obj["EnableRateFactor"]
      self.EnableTotalProductionUnits:bool = obj["EnableTotalProductionUnits"]
      self.RevalueGainLoss:int = obj["RevalueGainLoss"]
      """  Calculated field to store the total of all posted Revaluations as of the end of the current asset register year.  """  
      self.Rpt1CYDispTotalDepn:int = obj["Rpt1CYDispTotalDepn"]
      """  Calculated field to store the sum of current year Disposal Current and Previous Depreciation.  """  
      self.Rpt1RevalueGainLoss:int = obj["Rpt1RevalueGainLoss"]
      """  Calculated field to store the total of all posted Revaluations as of the end of the current asset register year.  """  
      self.Rpt1YTDAccumDepn:int = obj["Rpt1YTDAccumDepn"]
      """  Calculated field to store the total of all posted Depreciations including the depreciations from Addition activities subtracted with depreciations from Disposals as of the end of the current asset register year.  """  
      self.Rpt1YTDAddCost:int = obj["Rpt1YTDAddCost"]
      """  Calculated field to store the total of all posted Addition Costs from the very first period up to the end of the current asset register year.  """  
      self.Rpt1YTDDispCost:int = obj["Rpt1YTDDispCost"]
      """  Calculated field to store the total of all posted Disposal Costs from the very first period up to the end of the current asset register year.  """  
      self.Rpt1YTDGrantDepn:int = obj["Rpt1YTDGrantDepn"]
      """  Calculated field to store the total of all posted Grant Depreciations including the depreciations from Addition activities as of the end of the current asset register year.  """  
      self.Rpt1YTDImpCost:int = obj["Rpt1YTDImpCost"]
      """  Calculated field to store the total of all posted Impairment Costs from the very first period up to the end of the current asset register year.  """  
      self.Rpt2CYDispTotalDepn:int = obj["Rpt2CYDispTotalDepn"]
      """  Calculated field to store the sum of current year Disposal Current and Previous Depreciation.  """  
      self.Rpt2RevalueGainLoss:int = obj["Rpt2RevalueGainLoss"]
      """  Calculated field to store the total of all posted Revaluations as of the end of the current asset register year.  """  
      self.Rpt2YTDAccumDepn:int = obj["Rpt2YTDAccumDepn"]
      """  Calculated field to store the total of all posted Depreciations including the depreciations from Addition activities subtracted with depreciations from Disposals as of the end of the current asset register year.  """  
      self.Rpt2YTDAddCost:int = obj["Rpt2YTDAddCost"]
      """  Calculated field to store the total of all posted Addition Costs from the very first period up to the end of the current asset register year.  """  
      self.Rpt2YTDDispCost:int = obj["Rpt2YTDDispCost"]
      """  Calculated field to store the total of all posted Disposal Costs from the very first period up to the end of the current asset register year.  """  
      self.Rpt2YTDGrantDepn:int = obj["Rpt2YTDGrantDepn"]
      """  Calculated field to store the total of all posted Grant Depreciations including the depreciations from Addition activities as of the end of the current asset register year.  """  
      self.Rpt2YTDImpCost:int = obj["Rpt2YTDImpCost"]
      """  Calculated field to store the total of all posted Impairment Costs from the very first period up to the end of the current asset register year.  """  
      self.Rpt3CYDispTotalDepn:int = obj["Rpt3CYDispTotalDepn"]
      """  Calculated field to store the sum of current year Disposal Current and Previous Depreciation.  """  
      self.Rpt3RevalueGainLoss:int = obj["Rpt3RevalueGainLoss"]
      """  Calculated field to store the total of all posted Revaluations as of the end of the current asset register year.  """  
      self.Rpt3YTDAccumDepn:int = obj["Rpt3YTDAccumDepn"]
      """  Calculated field to store the total of all posted Depreciations including the depreciations from Addition activities subtracted with depreciations from Disposals as of the end of the current asset register year.  """  
      self.Rpt3YTDAddCost:int = obj["Rpt3YTDAddCost"]
      """  Calculated field to store the total of all posted Addition Costs from the very first period up to the end of the current asset register year.  """  
      self.Rpt3YTDDispCost:int = obj["Rpt3YTDDispCost"]
      """  Calculated field to store the total of all posted Disposal Costs from the very first period up to the end of the current asset register year.  """  
      self.Rpt3YTDGrantDepn:int = obj["Rpt3YTDGrantDepn"]
      """  Calculated field to store the total of all posted Grant Depreciations including the depreciations from Addition activities as of the end of the current asset register year.  """  
      self.Rpt3YTDImpCost:int = obj["Rpt3YTDImpCost"]
      """  Calculated field to store the total of all posted Impairment Costs from the very first period up to the end of the current asset register year.  """  
      self.YTDAccumDepn:int = obj["YTDAccumDepn"]
      """  Calculated field to store the total of all posted Depreciations including the depreciations from Addition activities subtracted with depreciations from Disposals as of the end of the current asset register year.  """  
      self.YTDAddCost:int = obj["YTDAddCost"]
      """  Calculated field to store the total of all posted Addition Costs from the very first period up to the end of the current asset register year.  """  
      self.YTDDispCost:int = obj["YTDDispCost"]
      """  Calculated field to store the total of all posted Disposal Costs from the very first period up to the end of the current asset register year.  """  
      self.YTDGrantDepn:int = obj["YTDGrantDepn"]
      """  Calculated field to store the total of all posted Grant Depreciations including the depreciations from Addition activities as of the end of the current asset register year.  """  
      self.YTDImpCost:int = obj["YTDImpCost"]
      """  Calculated field to store the total of all posted Impairment Costs from the very first period up to the end of the current asset register year.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.AddSpreadDescription:str = obj["AddSpreadDescription"]
      self.AltAssetMethodProrateType:str = obj["AltAssetMethodProrateType"]
      self.AltAssetMethodFinalspread:bool = obj["AltAssetMethodFinalspread"]
      self.AltAssetMethodDescription:str = obj["AltAssetMethodDescription"]
      self.AltAssetMethodAnnualChargeType:str = obj["AltAssetMethodAnnualChargeType"]
      self.AltAssetMethodPeriodChargeType:str = obj["AltAssetMethodPeriodChargeType"]
      self.AltAssetMethodDepChargeBasis:str = obj["AltAssetMethodDepChargeBasis"]
      self.AnnualSpreadDescription:str = obj["AnnualSpreadDescription"]
      self.FAMethodFinalspread:bool = obj["FAMethodFinalspread"]
      self.FAMethodDescription:str = obj["FAMethodDescription"]
      self.FAMethodAnnualChargeType:str = obj["FAMethodAnnualChargeType"]
      self.FAMethodProrateType:str = obj["FAMethodProrateType"]
      self.FAMethodDepChargeBasis:str = obj["FAMethodDepChargeBasis"]
      self.FAMethodPeriodChargeType:str = obj["FAMethodPeriodChargeType"]
      self.FAssetRegDescription:str = obj["FAssetRegDescription"]
      self.FinalSpreadDescription:str = obj["FinalSpreadDescription"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.PeriodSpreadDescription:str = obj["PeriodSpreadDescription"]
      self.ProdSpreadDescription:str = obj["ProdSpreadDescription"]
      self.RateSpreadDescription:str = obj["RateSpreadDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAssetListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the asset.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Identifier of the asset  """  
      self.AssetSeq:int = obj["AssetSeq"]
      """  The asset sequence allows for multiple fiscal instances of the asset. When greater than zero it is a fiscal instance of the asset. Currently only 0 is supported.  """  
      self.AssetDescription:str = obj["AssetDescription"]
      """  Mandatory description of the asset.  """  
      self.InActive:bool = obj["InActive"]
      """  flag to indicate an asset to be inactive. Inactive assets are not depreciated or recalculated.  """  
      self.ParentAsset:str = obj["ParentAsset"]
      """  Asset parent of this asset  """  
      self.NewAssetFlag:bool = obj["NewAssetFlag"]
      """  Informational indication of a newly bought asset.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  The code of the mandatory asset group.  """  
      self.ClassCode:str = obj["ClassCode"]
      """  Identifier of the asset class.  """  
      self.ResourceGroupID:str = obj["ResourceGroupID"]
      """  Identifier of the Resource Group of the asset. For informational purposes only.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The Resource identifier of the asset. For informational purposes only.  """  
      self.AcquiredDate:str = obj["AcquiredDate"]
      """  Date of acquisition of the asset.  """  
      self.CommissionedDate:str = obj["CommissionedDate"]
      """  Date of placing the asset in service. Also the start date of depreciation.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Identifier of the vendor of the asset.  """  
      self.VendorName:str = obj["VendorName"]
      """  The name of the vendor. The name can be entered without entering a vendor.  """  
      self.PONum:int = obj["PONum"]
      """  The po number the asset purchase order.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  The invoice number of asset invoice.  """  
      self.JobNum:str = obj["JobNum"]
      """  The job that created the asset.  """  
      self.Serialno:str = obj["Serialno"]
      """  The serial number of the asset.  """  
      self.Manufacturer:str = obj["Manufacturer"]
      """  The original manufacturer of the asset.  """  
      self.Model:str = obj["Model"]
      """  The model of the asset.  """  
      self.InsurancePolicy:str = obj["InsurancePolicy"]
      """  Insurance policy for the asset.  """  
      self.InsuranceCompany:str = obj["InsuranceCompany"]
      """  The insurance company.  """  
      self.InsurancePremium:int = obj["InsurancePremium"]
      """  Insurance premium  """  
      self.InsuranceRenewalDate:str = obj["InsuranceRenewalDate"]
      """  Insurance RenewalDate  """  
      self.InsuranceInsurer:str = obj["InsuranceInsurer"]
      """  The insurer.  """  
      self.LeaseFlag:bool = obj["LeaseFlag"]
      """  Flag the asset as leased.  """  
      self.LeaseValue:int = obj["LeaseValue"]
      """  Lease amount  """  
      self.LeaseMileage:int = obj["LeaseMileage"]
      """  Mileage limit of lease  """  
      self.LeaseEndDate:str = obj["LeaseEndDate"]
      """  End date of lease.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse where the asset is stored. This is for information purposes only. In the warehouse tracker no assets can be tracked.  """  
      self.BinNum:str = obj["BinNum"]
      """  The bin where the addition is stored. This is for information purposes only. In the bin tracker no assets can be tracked.  """  
      self.Location:str = obj["Location"]
      """  Freeform field for the location of tha aaset.  """  
      self.OverideCost:int = obj["OverideCost"]
      """  The overide cost is cost amount which is used instead of the asset cost amount for the calculation of a year depreciation.  """  
      self.ResidualValue:int = obj["ResidualValue"]
      """  Residual value of the asset  """  
      self.ReplaceValue:int = obj["ReplaceValue"]
      """  Replacement value of the asset. For information purposes only.  """  
      self.CYAdditionCost:int = obj["CYAdditionCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.CYDisposalCost:int = obj["CYDisposalCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.CYDisposalProceeds:int = obj["CYDisposalProceeds"]
      """  Disposal proceed amount.  """  
      self.CurrentCostvalue:int = obj["CurrentCostvalue"]
      """  Current cost value of the asset.  """  
      self.Acquire:int = obj["Acquire"]
      """  The amount the asset is acquired for.  """  
      self.ImageFileName:str = obj["ImageFileName"]
      """  Path and filename of asset image file.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the Company currency.  """  
      self.AssetStatus:str = obj["AssetStatus"]
      """  Current Status of the asset. Valid values are: 'NEW'; 'ACTIVE'; 'DISPOSED' or 'INACTIVE'.  """  
      self.AcquisitionCost:int = obj["AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the Asset with a project in the Project table.  This can be blank.  """  
      self.TagNum:str = obj["TagNum"]
      """  Tag number. This will keep the asset label.  """  
      self.CurrentGrantAmt:int = obj["CurrentGrantAmt"]
      """  The total Grant amount recorded for this Asset.  """  
      self.DocResidualValue:int = obj["DocResidualValue"]
      """  Residual value of the asset  """  
      self.DocReplaceValue:int = obj["DocReplaceValue"]
      """  Replacement value of the asset. For information purposes only.  """  
      self.DocCYAdditionCost:int = obj["DocCYAdditionCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.DocCYDisposalCost:int = obj["DocCYDisposalCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.DocAcquisitionCost:int = obj["DocAcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.DocCurrentGrantAmt:int = obj["DocCurrentGrantAmt"]
      """  The total Grant amount recorded for this Asset in document currency.  """  
      self.Rpt1ResidualValue:int = obj["Rpt1ResidualValue"]
      """  Residual value of the asset  """  
      self.Rpt1ReplaceValue:int = obj["Rpt1ReplaceValue"]
      """  Replacement value of the asset. For information purposes only.  """  
      self.Rpt1CYAdditionCost:int = obj["Rpt1CYAdditionCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt1CYDisposalCost:int = obj["Rpt1CYDisposalCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.Rpt1AcquisitionCost:int = obj["Rpt1AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.Rpt1CurrentGrantAmt:int = obj["Rpt1CurrentGrantAmt"]
      """  The total Grant amount recorded for this Asset in reporting currency.  """  
      self.Rpt2ResidualValue:int = obj["Rpt2ResidualValue"]
      """  Residual value of the asset  """  
      self.Rpt2ReplaceValue:int = obj["Rpt2ReplaceValue"]
      """  Replacement value of the asset. For information purposes only.  """  
      self.Rpt2CYAdditionCost:int = obj["Rpt2CYAdditionCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt2CYDisposalCost:int = obj["Rpt2CYDisposalCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.Rpt2AcquisitionCost:int = obj["Rpt2AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.Rpt2CurrentGrantAmt:int = obj["Rpt2CurrentGrantAmt"]
      """  The total Grant amount recorded for this Asset in reporting currency.  """  
      self.Rpt3ResidualValue:int = obj["Rpt3ResidualValue"]
      """  Residual value of the asset  """  
      self.Rpt3ReplaceValue:int = obj["Rpt3ReplaceValue"]
      """  Replacement value of the asset. For information purposes only.  """  
      self.Rpt3CYAdditionCost:int = obj["Rpt3CYAdditionCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt3CYDisposalCost:int = obj["Rpt3CYDisposalCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.Rpt3AcquisitionCost:int = obj["Rpt3AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.Rpt3CurrentGrantAmt:int = obj["Rpt3CurrentGrantAmt"]
      """  The total Grant amount recorded for this Asset in reporting currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.MXTaxCode:str = obj["MXTaxCode"]
      """  Tax Code (Mexico Localization field)  """  
      self.MXTaxRate:str = obj["MXTaxRate"]
      """  Tax Rate (Mexico Localization field)  """  
      self.MXInvestAmount:int = obj["MXInvestAmount"]
      """  Investment Value (Mexico Localization field)  """  
      self.MXTaxAmount:int = obj["MXTaxAmount"]
      """  Mexico Tax Amount (Mexico Localization field)  """  
      self.MXAnnualDepre:int = obj["MXAnnualDepre"]
      """  Annual depreciation Percentage (Mexico Localization field)  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line  (Mexico Localization field)  """  
      self.MXAssetLife:int = obj["MXAssetLife"]
      """  Mexico Asset Life (Mexico Localization field)  """  
      self.CYImpairCost:int = obj["CYImpairCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.DocCYImpairCost:int = obj["DocCYImpairCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.Rpt1CYImpairCost:int = obj["Rpt1CYImpairCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.Rpt2CYImpairCost:int = obj["Rpt2CYImpairCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.Rpt3CYImpairCost:int = obj["Rpt3CYImpairCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.DocCurrentCostValue:int = obj["DocCurrentCostValue"]
      """  Current cost value of the asset in document currency.  """  
      self.Rpt1CurrentCostvalue:int = obj["Rpt1CurrentCostvalue"]
      """  Current cost value of the asset in reporting currency.  """  
      self.Rpt2CurrentCostvalue:int = obj["Rpt2CurrentCostvalue"]
      """  Current cost value of the asset in reporting currency.  """  
      self.Rpt3CurrentCostValue:int = obj["Rpt3CurrentCostValue"]
      """  Current cost value of the asset in reporting currency.  """  
      self.LocID:str = obj["LocID"]
      """  Location ID.  """  
      self.DocCYDisposalProceeds:int = obj["DocCYDisposalProceeds"]
      """  Disposal proceed amount.  """  
      self.Rpt1CYDisposalProceeds:int = obj["Rpt1CYDisposalProceeds"]
      """  Disposal proceed amount.  """  
      self.Rpt2CYDisposalProceeds:int = obj["Rpt2CYDisposalProceeds"]
      """  Disposal proceed amount.  """  
      self.Rpt3CYDisposalProceeds:int = obj["Rpt3CYDisposalProceeds"]
      """  Disposal proceed amount.  """  
      self.CYAdditionGrant:int = obj["CYAdditionGrant"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.DocCYAdditionGrant:int = obj["DocCYAdditionGrant"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt1CYAdditionGrant:int = obj["Rpt1CYAdditionGrant"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt2CYAdditionGrant:int = obj["Rpt2CYAdditionGrant"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt3CYAdditionGrant:int = obj["Rpt3CYAdditionGrant"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  """  
      self.LastCalDate:str = obj["LastCalDate"]
      """  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.DepRecalcNeeded:bool = obj["DepRecalcNeeded"]
      """  System maintained field.  Indicates that asset depreciation needs to be recalculated for this asset.  """  
      self.EquipID:str = obj["EquipID"]
      """  Descriptive code to uniquely identify the Equipment.  """  
      self.Brand:str = obj["Brand"]
      """  Brand of equipment  """  
      self.AssetUnits:int = obj["AssetUnits"]
      """  This is the total number of units recorded for this asset.  This is not directly maintained by user.  This is increased when you add/transfer asset "qty" from the Asset Addition Entry.  This is decreased when you dispose/transfer asset "qty" from the Asset Disposal Entry.  This field is not a true quantity field since we do not perform any unit of measure conversion when we update AssetUnits based on the transferred qty.  """  
      self.Lineage:str = obj["Lineage"]
      """  Stores the keys (assetnum) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  """  
      self.DocInsurancePremium:int = obj["DocInsurancePremium"]
      """  Insurance premium in document currency.  """  
      self.Rpt1InsurancePremium:int = obj["Rpt1InsurancePremium"]
      """  Insurance premium in Reporting Currency.  """  
      self.Rpt2InsurancePremium:int = obj["Rpt2InsurancePremium"]
      """  Insurance premium in Reporting Currency.  """  
      self.Rpt3InsurancePremium:int = obj["Rpt3InsurancePremium"]
      """  Insurance premium in Reporting Currency.  """  
      self.DocLeaseValue:int = obj["DocLeaseValue"]
      """  Lease amount in document currency.  """  
      self.Rpt1LeaseValue:int = obj["Rpt1LeaseValue"]
      """  Lease amount in Reporting Currency.  """  
      self.Rpt2LeaseValue:int = obj["Rpt2LeaseValue"]
      """  Lease amount in Rocument Currency.  """  
      self.Rpt3LeaseValue:int = obj["Rpt3LeaseValue"]
      """  Lease amount in Reporting Currency.  """  
      self.InsuranceValue:int = obj["InsuranceValue"]
      """  Insurance Value  """  
      self.DocInsuranceValue:int = obj["DocInsuranceValue"]
      """  Insurance Value in document currency.  """  
      self.Rpt1InsuranceValue:int = obj["Rpt1InsuranceValue"]
      """  Insurance Value in Reporting Currency.  """  
      self.Rpt2InsuranceValue:int = obj["Rpt2InsuranceValue"]
      """  Insurance Value in Reporting Currency.  """  
      self.Rpt3InsuranceValue:int = obj["Rpt3InsuranceValue"]
      """  Insurance Value in Reporting Currency.  """  
      self.InsPremiumModifier:str = obj["InsPremiumModifier"]
      """  The premium modifier expresses if the Insurance Premium is per Period or per Year.  Values are: Periods and Years.  """  
      self.LeaseModifier:str = obj["LeaseModifier"]
      """  The lease value modifier expresses if the Lease Value is per Period or per Year.  Values are: Periods and Years.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  The Project Phase ID of this asset.  """  
      self.LeaseNum:str = obj["LeaseNum"]
      """  Lease Number of the asset.  """  
      self.LeaseCompany:str = obj["LeaseCompany"]
      """  The Leasing Company.  """  
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
      self.Department:str = obj["Department"]
      """  Department  """  
      self.IsPosted:bool = obj["IsPosted"]
      self.FinalSpread:bool = obj["FinalSpread"]
      self.AdditionSpread:bool = obj["AdditionSpread"]
      self.BinDescription:str = obj["BinDescription"]
      self.MXTaxCatID:str = obj["MXTaxCatID"]
      """  Mexico Localization Field  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.ImagePath:str = obj["ImagePath"]
      """  Path name of the Asset Image or Photo  """  
      self.EquipCreate:bool = obj["EquipCreate"]
      self.PhaseDescription:str = obj["PhaseDescription"]
      self.AssetGrpDescDescription:str = obj["AssetGrpDescDescription"]
      """  The description of the asset group.  """  
      self.ClassDescription:str = obj["ClassDescription"]
      """  Class description.  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.LocIDDescription:str = obj["LocIDDescription"]
      """  Description the Location.  Cannot be blank.  """  
      self.MachineDescDescription:str = obj["MachineDescDescription"]
      """  Full description of Resource.  """  
      self.ResrceGrpDescDescription:str = obj["ResrceGrpDescDescription"]
      """  Long description of the Resource Group.  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAssetListTableset:
   def __init__(self, obj):
      self.FAssetList:list[Erp_Tablesets_FAssetListRow] = obj["FAssetList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FAssetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the asset.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Identifier of the asset  """  
      self.AssetSeq:int = obj["AssetSeq"]
      """  The asset sequence allows for multiple fiscal instances of the asset. When greater than zero it is a fiscal instance of the asset. Currently only 0 is supported.  """  
      self.AssetDescription:str = obj["AssetDescription"]
      """  Mandatory description of the asset.  """  
      self.InActive:bool = obj["InActive"]
      """  flag to indicate an asset to be inactive. Inactive assets are not depreciated or recalculated.  """  
      self.ParentAsset:str = obj["ParentAsset"]
      """  Asset parent of this asset  """  
      self.NewAssetFlag:bool = obj["NewAssetFlag"]
      """  Informational indication of a newly bought asset.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  The code of the mandatory asset group.  """  
      self.ClassCode:str = obj["ClassCode"]
      """  Identifier of the asset class.  """  
      self.ResourceGroupID:str = obj["ResourceGroupID"]
      """  Identifier of the Resource Group of the asset. For informational purposes only.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The Resource identifier of the asset. For informational purposes only.  """  
      self.AcquiredDate:str = obj["AcquiredDate"]
      """  Date of acquisition of the asset.  """  
      self.CommissionedDate:str = obj["CommissionedDate"]
      """  Date of placing the asset in service. Also the start date of depreciation.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Identifier of the vendor of the asset.  """  
      self.VendorName:str = obj["VendorName"]
      """  The name of the vendor. The name can be entered without entering a vendor.  """  
      self.PONum:int = obj["PONum"]
      """  The po number the asset purchase order.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  The invoice number of asset invoice.  """  
      self.JobNum:str = obj["JobNum"]
      """  The job that created the asset.  """  
      self.Serialno:str = obj["Serialno"]
      """  The serial number of the asset.  """  
      self.Manufacturer:str = obj["Manufacturer"]
      """  The original manufacturer of the asset.  """  
      self.Model:str = obj["Model"]
      """  The model of the asset.  """  
      self.InsurancePolicy:str = obj["InsurancePolicy"]
      """  Insurance policy for the asset.  """  
      self.InsuranceCompany:str = obj["InsuranceCompany"]
      """  The insurance company.  """  
      self.InsurancePremium:int = obj["InsurancePremium"]
      """  Insurance premium  """  
      self.InsuranceRenewalDate:str = obj["InsuranceRenewalDate"]
      """  Insurance RenewalDate  """  
      self.InsuranceInsurer:str = obj["InsuranceInsurer"]
      """  The insurer.  """  
      self.LeaseFlag:bool = obj["LeaseFlag"]
      """  Flag the asset as leased.  """  
      self.LeaseValue:int = obj["LeaseValue"]
      """  Lease amount  """  
      self.LeaseMileage:int = obj["LeaseMileage"]
      """  Mileage limit of lease  """  
      self.LeaseEndDate:str = obj["LeaseEndDate"]
      """  End date of lease.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse where the asset is stored. This is for information purposes only. In the warehouse tracker no assets can be tracked.  """  
      self.BinNum:str = obj["BinNum"]
      """  The bin where the addition is stored. This is for information purposes only. In the bin tracker no assets can be tracked.  """  
      self.Location:str = obj["Location"]
      """  Freeform field for the location of tha aaset.  """  
      self.OverideCost:int = obj["OverideCost"]
      """  The overide cost is cost amount which is used instead of the asset cost amount for the calculation of a year depreciation.  """  
      self.ResidualValue:int = obj["ResidualValue"]
      """  Residual value of the asset  """  
      self.ReplaceValue:int = obj["ReplaceValue"]
      """  Replacement value of the asset. For information purposes only.  """  
      self.CYAdditionCost:int = obj["CYAdditionCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.CYDisposalCost:int = obj["CYDisposalCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.CYDisposalProceeds:int = obj["CYDisposalProceeds"]
      """  Disposal proceed amount.  """  
      self.CurrentCostvalue:int = obj["CurrentCostvalue"]
      """  Current cost value of the asset.  """  
      self.Acquire:int = obj["Acquire"]
      """  The amount the asset is acquired for.  """  
      self.ImageFileName:str = obj["ImageFileName"]
      """  Path and filename of asset image file.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the Company currency.  """  
      self.AssetStatus:str = obj["AssetStatus"]
      """  Current Status of the asset. Valid values are: 'NEW'; 'ACTIVE'; 'DISPOSED' or 'INACTIVE'.  """  
      self.AcquisitionCost:int = obj["AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the Asset with a project in the Project table.  This can be blank.  """  
      self.TagNum:str = obj["TagNum"]
      """  Tag number. This will keep the asset label.  """  
      self.CurrentGrantAmt:int = obj["CurrentGrantAmt"]
      """  The total Grant amount recorded for this Asset.  """  
      self.DocResidualValue:int = obj["DocResidualValue"]
      """  Residual value of the asset  """  
      self.DocReplaceValue:int = obj["DocReplaceValue"]
      """  Replacement value of the asset. For information purposes only.  """  
      self.DocCYAdditionCost:int = obj["DocCYAdditionCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.DocCYDisposalCost:int = obj["DocCYDisposalCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.DocAcquisitionCost:int = obj["DocAcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.DocCurrentGrantAmt:int = obj["DocCurrentGrantAmt"]
      """  The total Grant amount recorded for this Asset in document currency.  """  
      self.Rpt1ResidualValue:int = obj["Rpt1ResidualValue"]
      """  Residual value of the asset  """  
      self.Rpt1ReplaceValue:int = obj["Rpt1ReplaceValue"]
      """  Replacement value of the asset. For information purposes only.  """  
      self.Rpt1CYAdditionCost:int = obj["Rpt1CYAdditionCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt1CYDisposalCost:int = obj["Rpt1CYDisposalCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.Rpt1AcquisitionCost:int = obj["Rpt1AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.Rpt1CurrentGrantAmt:int = obj["Rpt1CurrentGrantAmt"]
      """  The total Grant amount recorded for this Asset in reporting currency.  """  
      self.Rpt2ResidualValue:int = obj["Rpt2ResidualValue"]
      """  Residual value of the asset  """  
      self.Rpt2ReplaceValue:int = obj["Rpt2ReplaceValue"]
      """  Replacement value of the asset. For information purposes only.  """  
      self.Rpt2CYAdditionCost:int = obj["Rpt2CYAdditionCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt2CYDisposalCost:int = obj["Rpt2CYDisposalCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.Rpt2AcquisitionCost:int = obj["Rpt2AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.Rpt2CurrentGrantAmt:int = obj["Rpt2CurrentGrantAmt"]
      """  The total Grant amount recorded for this Asset in reporting currency.  """  
      self.Rpt3ResidualValue:int = obj["Rpt3ResidualValue"]
      """  Residual value of the asset  """  
      self.Rpt3ReplaceValue:int = obj["Rpt3ReplaceValue"]
      """  Replacement value of the asset. For information purposes only.  """  
      self.Rpt3CYAdditionCost:int = obj["Rpt3CYAdditionCost"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt3CYDisposalCost:int = obj["Rpt3CYDisposalCost"]
      """  Current year disposal cost is the disposal cost  disposed from the asset this year.  """  
      self.Rpt3AcquisitionCost:int = obj["Rpt3AcquisitionCost"]
      """  This is the very first Addition Cost recorded for this asset.  """  
      self.Rpt3CurrentGrantAmt:int = obj["Rpt3CurrentGrantAmt"]
      """  The total Grant amount recorded for this Asset in reporting currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.MXTaxCode:str = obj["MXTaxCode"]
      """  Tax Code (Mexico Localization field)  """  
      self.MXTaxRate:str = obj["MXTaxRate"]
      """  Tax Rate (Mexico Localization field)  """  
      self.MXInvestAmount:int = obj["MXInvestAmount"]
      """  Investment Value (Mexico Localization field)  """  
      self.MXTaxAmount:int = obj["MXTaxAmount"]
      """  Mexico Tax Amount (Mexico Localization field)  """  
      self.MXAnnualDepre:int = obj["MXAnnualDepre"]
      """  Annual depreciation Percentage (Mexico Localization field)  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line  (Mexico Localization field)  """  
      self.MXAssetLife:int = obj["MXAssetLife"]
      """  Mexico Asset Life (Mexico Localization field)  """  
      self.CYImpairCost:int = obj["CYImpairCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.DocCYImpairCost:int = obj["DocCYImpairCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.Rpt1CYImpairCost:int = obj["Rpt1CYImpairCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.Rpt2CYImpairCost:int = obj["Rpt2CYImpairCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.Rpt3CYImpairCost:int = obj["Rpt3CYImpairCost"]
      """  Current year impairment cost is the cost subtracted from the asset this year.  """  
      self.DocCurrentCostValue:int = obj["DocCurrentCostValue"]
      """  Current cost value of the asset in document currency.  """  
      self.Rpt1CurrentCostvalue:int = obj["Rpt1CurrentCostvalue"]
      """  Current cost value of the asset in reporting currency.  """  
      self.Rpt2CurrentCostvalue:int = obj["Rpt2CurrentCostvalue"]
      """  Current cost value of the asset in reporting currency.  """  
      self.Rpt3CurrentCostValue:int = obj["Rpt3CurrentCostValue"]
      """  Current cost value of the asset in reporting currency.  """  
      self.LocID:str = obj["LocID"]
      """  Location ID.  """  
      self.DocCYDisposalProceeds:int = obj["DocCYDisposalProceeds"]
      """  Disposal proceed amount.  """  
      self.Rpt1CYDisposalProceeds:int = obj["Rpt1CYDisposalProceeds"]
      """  Disposal proceed amount.  """  
      self.Rpt2CYDisposalProceeds:int = obj["Rpt2CYDisposalProceeds"]
      """  Disposal proceed amount.  """  
      self.Rpt3CYDisposalProceeds:int = obj["Rpt3CYDisposalProceeds"]
      """  Disposal proceed amount.  """  
      self.CYAdditionGrant:int = obj["CYAdditionGrant"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.DocCYAdditionGrant:int = obj["DocCYAdditionGrant"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt1CYAdditionGrant:int = obj["Rpt1CYAdditionGrant"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt2CYAdditionGrant:int = obj["Rpt2CYAdditionGrant"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.Rpt3CYAdditionGrant:int = obj["Rpt3CYAdditionGrant"]
      """  Current Addition Cost is the addition cost  added to the asset  this year.  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  """  
      self.LastCalDate:str = obj["LastCalDate"]
      """  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.DepRecalcNeeded:bool = obj["DepRecalcNeeded"]
      """  System maintained field.  Indicates that asset depreciation needs to be recalculated for this asset.  """  
      self.EquipID:str = obj["EquipID"]
      """  Descriptive code to uniquely identify the Equipment.  """  
      self.Brand:str = obj["Brand"]
      """  Brand of equipment  """  
      self.AssetUnits:int = obj["AssetUnits"]
      """  This is the total number of units recorded for this asset.  This is not directly maintained by user.  This is increased when you add/transfer asset "qty" from the Asset Addition Entry.  This is decreased when you dispose/transfer asset "qty" from the Asset Disposal Entry.  This field is not a true quantity field since we do not perform any unit of measure conversion when we update AssetUnits based on the transferred qty.  """  
      self.Lineage:str = obj["Lineage"]
      """  Stores the keys (assetnum) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  """  
      self.DocInsurancePremium:int = obj["DocInsurancePremium"]
      """  Insurance premium in document currency.  """  
      self.Rpt1InsurancePremium:int = obj["Rpt1InsurancePremium"]
      """  Insurance premium in Reporting Currency.  """  
      self.Rpt2InsurancePremium:int = obj["Rpt2InsurancePremium"]
      """  Insurance premium in Reporting Currency.  """  
      self.Rpt3InsurancePremium:int = obj["Rpt3InsurancePremium"]
      """  Insurance premium in Reporting Currency.  """  
      self.DocLeaseValue:int = obj["DocLeaseValue"]
      """  Lease amount in document currency.  """  
      self.Rpt1LeaseValue:int = obj["Rpt1LeaseValue"]
      """  Lease amount in Reporting Currency.  """  
      self.Rpt2LeaseValue:int = obj["Rpt2LeaseValue"]
      """  Lease amount in Rocument Currency.  """  
      self.Rpt3LeaseValue:int = obj["Rpt3LeaseValue"]
      """  Lease amount in Reporting Currency.  """  
      self.InsuranceValue:int = obj["InsuranceValue"]
      """  Insurance Value  """  
      self.DocInsuranceValue:int = obj["DocInsuranceValue"]
      """  Insurance Value in document currency.  """  
      self.Rpt1InsuranceValue:int = obj["Rpt1InsuranceValue"]
      """  Insurance Value in Reporting Currency.  """  
      self.Rpt2InsuranceValue:int = obj["Rpt2InsuranceValue"]
      """  Insurance Value in Reporting Currency.  """  
      self.Rpt3InsuranceValue:int = obj["Rpt3InsuranceValue"]
      """  Insurance Value in Reporting Currency.  """  
      self.InsPremiumModifier:str = obj["InsPremiumModifier"]
      """  The premium modifier expresses if the Insurance Premium is per Period or per Year.  Values are: Periods and Years.  """  
      self.LeaseModifier:str = obj["LeaseModifier"]
      """  The lease value modifier expresses if the Lease Value is per Period or per Year.  Values are: Periods and Years.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  The Project Phase ID of this asset.  """  
      self.LeaseNum:str = obj["LeaseNum"]
      """  Lease Number of the asset.  """  
      self.LeaseCompany:str = obj["LeaseCompany"]
      """  The Leasing Company.  """  
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
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.Department:str = obj["Department"]
      """  Department  """  
      self.UOM:str = obj["UOM"]
      """  UOM  """  
      self.CNUsageStatus:str = obj["CNUsageStatus"]
      """  CNUsageStatus  """  
      self.CNUsagePercent:int = obj["CNUsagePercent"]
      """  CNUsagePercent  """  
      self.CNImportedForProcessingTrade:bool = obj["CNImportedForProcessingTrade"]
      """  Imported for Processing Trade  """  
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      """  Declaration Bill  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  HS Commodity Code  """  
      self.CNDeclarationDate:str = obj["CNDeclarationDate"]
      """  Declaration Date  """  
      self.CNControlDueDate:str = obj["CNControlDueDate"]
      """  Control Due Date  """  
      self.CNManufacturingDate:str = obj["CNManufacturingDate"]
      """  Manufacturing Date  """  
      self.CNOrigCountryNum:int = obj["CNOrigCountryNum"]
      """  Country of Origin  """  
      self.CNSpecification:str = obj["CNSpecification"]
      """  Specification  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BinDescription:str = obj["BinDescription"]
      self.CNDeptChangeReason:str = obj["CNDeptChangeReason"]
      """  CNDeptChangeReason  """  
      self.CNLocChangeReason:str = obj["CNLocChangeReason"]
      """  CNLocChangeReason  """  
      self.IsPosted:bool = obj["IsPosted"]
      self.MXTaxCatID:str = obj["MXTaxCatID"]
      """  Mexico Localization Field  """  
      self.PhaseDescription:str = obj["PhaseDescription"]
      self.AdditionSpread:bool = obj["AdditionSpread"]
      self.EquipCreate:bool = obj["EquipCreate"]
      self.FinalSpread:bool = obj["FinalSpread"]
      self.ImagePath:str = obj["ImagePath"]
      """  Path name of the Asset Image or Photo  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssetGrpDescDescription:str = obj["AssetGrpDescDescription"]
      self.ClassDescription:str = obj["ClassDescription"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.LocIDDescription:str = obj["LocIDDescription"]
      self.MachineDescDescription:str = obj["MachineDescDescription"]
      self.ResrceGrpDescDescription:str = obj["ResrceGrpDescDescription"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAssetTableset:
   def __init__(self, obj):
      self.FAsset:list[Erp_Tablesets_FAssetRow] = obj["FAsset"]
      self.FAssetAttch:list[Erp_Tablesets_FAssetAttchRow] = obj["FAssetAttch"]
      self.ChildAssets:list[Erp_Tablesets_ChildAssetsRow] = obj["ChildAssets"]
      self.FAssetDtl:list[Erp_Tablesets_FAssetDtlRow] = obj["FAssetDtl"]
      self.FAssetDtlAttch:list[Erp_Tablesets_FAssetDtlAttchRow] = obj["FAssetDtlAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtFAssetTableset:
   def __init__(self, obj):
      self.FAsset:list[Erp_Tablesets_FAssetRow] = obj["FAsset"]
      self.FAssetAttch:list[Erp_Tablesets_FAssetAttchRow] = obj["FAssetAttch"]
      self.ChildAssets:list[Erp_Tablesets_ChildAssetsRow] = obj["ChildAssets"]
      self.FAssetDtl:list[Erp_Tablesets_FAssetDtlRow] = obj["FAssetDtl"]
      self.FAssetDtlAttch:list[Erp_Tablesets_FAssetDtlAttchRow] = obj["FAssetDtlAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExportData_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class ExportProcess_input:
   """ Required : 
   fileName
   """  
   def __init__(self, obj):
      self.fileName:str = obj["fileName"]
      pass

class ExportProcess_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.msg:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   assetNum
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FAssetTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FAssetTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FAssetTableset] = obj["returnObj"]
      pass

class GetChildAssets_input:
   """ Required : 
   ds
   parentAssetNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      self.parentAssetNum:str = obj["parentAssetNum"]
      """  The Parent Asset Number  """  
      pass

class GetChildAssets_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetClientFileName_input:
   """ Required : 
   IP_ServerFileName
   """  
   def __init__(self, obj):
      self.IP_ServerFileName:str = obj["IP_ServerFileName"]
      pass

class GetClientFileName_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

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

class GetFAssetByID_input:
   """ Required : 
   ipAssetNum
   """  
   def __init__(self, obj):
      self.ipAssetNum:str = obj["ipAssetNum"]
      """  New Asset Number  """  
      pass

class GetFAssetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FAssetTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FAssetListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewChildAsset_input:
   """ Required : 
   ipParentAssetNum
   ds
   """  
   def __init__(self, obj):
      self.ipParentAssetNum:str = obj["ipParentAssetNum"]
      """  AssetNum of the current asset.  """  
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

class GetNewChildAsset_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFAssetAttch_input:
   """ Required : 
   ds
   assetNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      self.assetNum:str = obj["assetNum"]
      pass

class GetNewFAssetAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFAssetDtlAttch_input:
   """ Required : 
   ds
   assetNum
   assetRegID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      self.assetNum:str = obj["assetNum"]
      self.assetRegID:str = obj["assetRegID"]
      pass

class GetNewFAssetDtlAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFAssetDtl_input:
   """ Required : 
   ds
   assetNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      self.assetNum:str = obj["assetNum"]
      pass

class GetNewFAssetDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFAsset_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

class GetNewFAsset_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseFAsset
   whereClauseFAssetAttch
   whereClauseChildAssets
   whereClauseFAssetDtl
   whereClauseFAssetDtlAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFAsset:str = obj["whereClauseFAsset"]
      self.whereClauseFAssetAttch:str = obj["whereClauseFAssetAttch"]
      self.whereClauseChildAssets:str = obj["whereClauseChildAssets"]
      self.whereClauseFAssetDtl:str = obj["whereClauseFAssetDtl"]
      self.whereClauseFAssetDtlAttch:str = obj["whereClauseFAssetDtlAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FAssetTableset] = obj["returnObj"]
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

class ImportData_input:
   """ Required : 
   ImportData
   ErrorList
   """  
   def __init__(self, obj):
      self.ImportData      #schema had no properties on an object.
      self.ErrorList:str = obj["ErrorList"]
      pass

class ImportData_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FAssetTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ErrorList:list = obj[any]
      pass

      """  output parameters  """  

class ImportToDS_input:
   """ Required : 
   fileName
   """  
   def __init__(self, obj):
      self.fileName:str = obj["fileName"]
      pass

class ImportToDS_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class LeaveAcquiredDate_input:
   """ Required : 
   ipAcquiredDate
   ds
   """  
   def __init__(self, obj):
      self.ipAcquiredDate:str = obj["ipAcquiredDate"]
      """  AcquiredDate was entered.  """  
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

class LeaveAcquiredDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveChildAssetNum_input:
   """ Required : 
   ipChildAssetNum
   ipParentAssetNum
   ds
   """  
   def __init__(self, obj):
      self.ipChildAssetNum:str = obj["ipChildAssetNum"]
      """  AssetNum that was entered.  """  
      self.ipParentAssetNum:str = obj["ipParentAssetNum"]
      """  The current Asset AssetNum.  """  
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

class LeaveChildAssetNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveInsPremium_input:
   """ Required : 
   ipInsPremium
   ipbaseordoc
   ds
   """  
   def __init__(self, obj):
      self.ipInsPremium:int = obj["ipInsPremium"]
      """  InsurancePremium that was entered.  """  
      self.ipbaseordoc:str = obj["ipbaseordoc"]
      """  The field type - base or doc  """  
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

class LeaveInsPremium_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveInsValue_input:
   """ Required : 
   ipInsValue
   ipbaseordoc
   ds
   """  
   def __init__(self, obj):
      self.ipInsValue:int = obj["ipInsValue"]
      """  InsuranceValue that was entered.  """  
      self.ipbaseordoc:str = obj["ipbaseordoc"]
      """  The field type - base or doc  """  
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

class LeaveInsValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveInvoiceLine_input:
   """ Required : 
   ipInvoiceLine
   ds
   """  
   def __init__(self, obj):
      self.ipInvoiceLine:int = obj["ipInvoiceLine"]
      """  Invoice Line that was entered.  """  
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

class LeaveInvoiceLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveInvoiceNum_input:
   """ Required : 
   ipInvoiceNum
   ds
   """  
   def __init__(self, obj):
      self.ipInvoiceNum:str = obj["ipInvoiceNum"]
      """  Invoice Number that was entered.  """  
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

class LeaveInvoiceNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveJobNum_input:
   """ Required : 
   ipJobNum
   ds
   """  
   def __init__(self, obj):
      self.ipJobNum:str = obj["ipJobNum"]
      """  Job Number that was entered.  """  
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

class LeaveJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveLeaseValue_input:
   """ Required : 
   ipLeaseValue
   ipbaseordoc
   ds
   """  
   def __init__(self, obj):
      self.ipLeaseValue:int = obj["ipLeaseValue"]
      """  LeaseValue that was entered.  """  
      self.ipbaseordoc:str = obj["ipbaseordoc"]
      """  The field type - base or doc  """  
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

class LeaveLeaseValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeavePONum_input:
   """ Required : 
   ipPONum
   ds
   """  
   def __init__(self, obj):
      self.ipPONum:int = obj["ipPONum"]
      """  PO Number that is entered.  """  
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

class LeavePONum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveReplaceValue_input:
   """ Required : 
   ipReplaceValue
   ipbaseordoc
   ds
   """  
   def __init__(self, obj):
      self.ipReplaceValue:int = obj["ipReplaceValue"]
      """  ReplaceValue that was entered.  """  
      self.ipbaseordoc:str = obj["ipbaseordoc"]
      """  The field type - base or doc  """  
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

class LeaveReplaceValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveResidualValue_input:
   """ Required : 
   ipResidualValue
   ipbaseordoc
   ds
   """  
   def __init__(self, obj):
      self.ipResidualValue:int = obj["ipResidualValue"]
      """  ResidualValue that was entered.  """  
      self.ipbaseordoc:str = obj["ipbaseordoc"]
      """  The field type - base or doc  """  
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

class LeaveResidualValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveVendorID_input:
   """ Required : 
   ipVendorID
   ds
   """  
   def __init__(self, obj):
      self.ipVendorID:str = obj["ipVendorID"]
      """  VendorID or SupplierID that was entered.  """  
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

class LeaveVendorID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeCommodityCode_input:
   """ Required : 
   newCommodityCode
   ds
   """  
   def __init__(self, obj):
      self.newCommodityCode:str = obj["newCommodityCode"]
      """  New Commodity Code  """  
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

class OnChangeCommodityCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PostedDepExist_input:
   """ Required : 
   assetNum
   assetRegID
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      """  Asset number  """  
      self.assetRegID:str = obj["assetRegID"]
      """  Asset registry ID  """  
      pass

class PostedDepExist_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.depExist:bool = obj["depExist"]
      pass

      """  output parameters  """  

class PreDuplicate_input:
   """ Required : 
   oldAssetNum
   acquiredDate
   commissionedDate
   dupCost
   additionDate
   """  
   def __init__(self, obj):
      self.oldAssetNum:str = obj["oldAssetNum"]
      """  Original Asset ID  """  
      self.acquiredDate:str = obj["acquiredDate"]
      """  New Acquisition Date  """  
      self.commissionedDate:str = obj["commissionedDate"]
      """  New Placed In Service Date  """  
      self.dupCost:bool = obj["dupCost"]
      """  Identifies whether Addition must be created  """  
      self.additionDate:str = obj["additionDate"]
      """  New Addition Date  """  
      pass

class PreDuplicate_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Warning message  """  
      pass

class TestAllowDelete_input:
   """ Required : 
   assetNum
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      """  AssetNum of record that is being updated.  """  
      pass

class TestAllowDelete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sureMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class TestParentChildIntegrity_input:
   """ Required : 
   ipOrgAssetNum
   ipAssetNum
   ippAssetType
   """  
   def __init__(self, obj):
      self.ipOrgAssetNum:str = obj["ipOrgAssetNum"]
      """  Orig. Asset Number  """  
      self.ipAssetNum:str = obj["ipAssetNum"]
      """  New Asset Number  """  
      self.ippAssetType:str = obj["ippAssetType"]
      """  Asset Type  """  
      pass

class TestParentChildIntegrity_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtFAssetTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtFAssetTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FAssetTableset] = obj["ds"]
      pass

      """  output parameters  """  

