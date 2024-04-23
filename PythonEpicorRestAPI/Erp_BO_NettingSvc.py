import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.NettingSvc
# Description: class NettingSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Nettings(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Nettings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Nettings
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NettingHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/Nettings",headers=creds) as resp:
           return await resp.json()

async def post_Nettings(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Nettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.NettingHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.NettingHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/Nettings", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Nettings_Company_NettingID(Company, NettingID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Netting item
   Description: Calls GetByID to retrieve the Netting item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Netting
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param NettingID: Desc: NettingID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.NettingHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/Nettings(" + Company + "," + NettingID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Nettings_Company_NettingID(Company, NettingID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Netting for the service
   Description: Calls UpdateExt to update Netting. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Netting
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param NettingID: Desc: NettingID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.NettingHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/Nettings(" + Company + "," + NettingID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Nettings_Company_NettingID(Company, NettingID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Netting item
   Description: Call UpdateExt to delete Netting item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Netting
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param NettingID: Desc: NettingID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/Nettings(" + Company + "," + NettingID + ")",headers=creds) as resp:
           return await resp.json()

async def get_Nettings_Company_NettingID_NettingDtls(Company, NettingID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get NettingDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_NettingDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param NettingID: Desc: NettingID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NettingDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/Nettings(" + Company + "," + NettingID + ")/NettingDtls",headers=creds) as resp:
           return await resp.json()

async def get_Nettings_Company_NettingID_NettingDtls_Company_NettingID_LineNum(Company, NettingID, LineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the NettingDtl item
   Description: Calls GetByID to retrieve the NettingDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NettingDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param NettingID: Desc: NettingID   Required: True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.NettingDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/Nettings(" + Company + "," + NettingID + ")/NettingDtls(" + Company + "," + NettingID + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_Nettings_Company_NettingID_NettingHeadAttches(Company, NettingID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get NettingHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_NettingHeadAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param NettingID: Desc: NettingID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NettingHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/Nettings(" + Company + "," + NettingID + ")/NettingHeadAttches",headers=creds) as resp:
           return await resp.json()

async def get_Nettings_Company_NettingID_NettingHeadAttches_Company_NettingID_DrawingSeq(Company, NettingID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the NettingHeadAttch item
   Description: Calls GetByID to retrieve the NettingHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NettingHeadAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param NettingID: Desc: NettingID   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.NettingHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/Nettings(" + Company + "," + NettingID + ")/NettingHeadAttches(" + Company + "," + NettingID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_NettingDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get NettingDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_NettingDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NettingDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/NettingDtls",headers=creds) as resp:
           return await resp.json()

async def post_NettingDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_NettingDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.NettingDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.NettingDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/NettingDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_NettingDtls_Company_NettingID_LineNum(Company, NettingID, LineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the NettingDtl item
   Description: Calls GetByID to retrieve the NettingDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NettingDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param NettingID: Desc: NettingID   Required: True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.NettingDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/NettingDtls(" + Company + "," + NettingID + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_NettingDtls_Company_NettingID_LineNum(Company, NettingID, LineNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update NettingDtl for the service
   Description: Calls UpdateExt to update NettingDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_NettingDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param NettingID: Desc: NettingID   Required: True
      :param LineNum: Desc: LineNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.NettingDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/NettingDtls(" + Company + "," + NettingID + "," + LineNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_NettingDtls_Company_NettingID_LineNum(Company, NettingID, LineNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete NettingDtl item
   Description: Call UpdateExt to delete NettingDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_NettingDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param NettingID: Desc: NettingID   Required: True
      :param LineNum: Desc: LineNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/NettingDtls(" + Company + "," + NettingID + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_NettingHeadAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get NettingHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_NettingHeadAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NettingHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/NettingHeadAttches",headers=creds) as resp:
           return await resp.json()

async def post_NettingHeadAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_NettingHeadAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.NettingHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.NettingHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/NettingHeadAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_NettingHeadAttches_Company_NettingID_DrawingSeq(Company, NettingID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the NettingHeadAttch item
   Description: Calls GetByID to retrieve the NettingHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NettingHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param NettingID: Desc: NettingID   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.NettingHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/NettingHeadAttches(" + Company + "," + NettingID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_NettingHeadAttches_Company_NettingID_DrawingSeq(Company, NettingID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update NettingHeadAttch for the service
   Description: Calls UpdateExt to update NettingHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_NettingHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param NettingID: Desc: NettingID   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.NettingHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/NettingHeadAttches(" + Company + "," + NettingID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_NettingHeadAttches_Company_NettingID_DrawingSeq(Company, NettingID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete NettingHeadAttch item
   Description: Call UpdateExt to delete NettingHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_NettingHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param NettingID: Desc: NettingID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/NettingHeadAttches(" + Company + "," + NettingID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_CreditDocuments(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CreditDocuments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CreditDocuments
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CreditDocumentsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/CreditDocuments",headers=creds) as resp:
           return await resp.json()

async def post_CreditDocuments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CreditDocuments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CreditDocumentsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CreditDocumentsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/CreditDocuments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CreditDocuments_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CreditDocument item
   Description: Calls GetByID to retrieve the CreditDocument item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CreditDocument
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CreditDocumentsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/CreditDocuments(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CreditDocuments_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CreditDocument for the service
   Description: Calls UpdateExt to update CreditDocument. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CreditDocument
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CreditDocumentsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/CreditDocuments(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CreditDocuments_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CreditDocument item
   Description: Call UpdateExt to delete CreditDocument item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CreditDocument
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/CreditDocuments(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DebitDocuments(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DebitDocuments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DebitDocuments
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DebitDocumentsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/DebitDocuments",headers=creds) as resp:
           return await resp.json()

async def post_DebitDocuments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DebitDocuments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DebitDocumentsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DebitDocumentsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/DebitDocuments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DebitDocuments_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DebitDocument item
   Description: Calls GetByID to retrieve the DebitDocument item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DebitDocument
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DebitDocumentsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/DebitDocuments(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DebitDocuments_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DebitDocument for the service
   Description: Calls UpdateExt to update DebitDocument. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DebitDocument
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DebitDocumentsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/DebitDocuments(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DebitDocuments_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DebitDocument item
   Description: Call UpdateExt to delete DebitDocument item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DebitDocument
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/DebitDocuments(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NettingListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseNettingHead, whereClauseNettingHeadAttch, whereClauseNettingDtl, whereClauseCreditDocuments, whereClauseDebitDocuments, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseNettingHead=" + whereClauseNettingHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseNettingHeadAttch=" + whereClauseNettingHeadAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseNettingDtl=" + whereClauseNettingDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCreditDocuments=" + whereClauseCreditDocuments
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDebitDocuments=" + whereClauseDebitDocuments
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(nettingID, epicorHeaders = None):
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
   params += "nettingID=" + nettingID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_DeleteNettingDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteNettingDtl
   OperationID: DeleteNettingDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteNettingDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteNettingDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeofCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeofCustID
   OperationID: OnChangeofCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeofVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeofVendorID
   OperationID: OnChangeofVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateEnableNetting(epicorHeaders = None):
   """  
   Summary: Invoke method ValidateEnableNetting
   Description: Check if Enable Netting is true in Company Configuration
   OperationID: ValidateEnableNetting
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateEnableNetting_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ValidateCreditDebitSelection(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCreditDebitSelection
   Description: Validate Credit and Debit selected for the NettingID
   OperationID: ValidateCreditDebitSelection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCreditDebitSelection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCreditDebitSelection_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSelectedCredits(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSelectedCredits
   Description: On Selected of a Credit, we update the Header (NettingHead) to reflect updated Debit/Credit/Remain
   OperationID: OnChangeSelectedCredits
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSelectedCredits_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSelectedCredits_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSelectedDebits(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSelectedDebits
   Description: On Selected of a Debit, we update the Header (NettingHead) to reflect updated Debit/Credit/Remain
   OperationID: OnChangeSelectedDebits
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSelectedDebits_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSelectedDebits_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewNettingHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewNettingHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewNettingHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewNettingHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewNettingHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewNettingHeadAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewNettingHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewNettingHeadAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewNettingHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewNettingHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewNettingDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewNettingDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewNettingDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewNettingDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewNettingDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NettingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditDocumentsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CreditDocumentsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DebitDocumentsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DebitDocumentsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NettingDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_NettingDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NettingHeadAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_NettingHeadAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NettingHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_NettingHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NettingListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_NettingListRow] = obj["value"]
      pass

class Erp_Tablesets_CreditDocumentsRow:
   def __init__(self, obj):
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DocumentID:str = obj["DocumentID"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.Selected:bool = obj["Selected"]
      self.Type:str = obj["Type"]
      self.VendorID:str = obj["VendorID"]
      self.InvoiceDate:str = obj["InvoiceDate"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.InvoiceBal:int = obj["InvoiceBal"]
      self.DueDate:str = obj["DueDate"]
      self.InvoiceRef:str = obj["InvoiceRef"]
      self.TypeID:str = obj["TypeID"]
      """  The type of document as an ID, Type field hold the extended version.  """  
      self.DocWithholdingTax:int = obj["DocWithholdingTax"]
      self.WithholdingTax:int = obj["WithholdingTax"]
      self.Rpt1WithholdingTax:int = obj["Rpt1WithholdingTax"]
      self.Rpt2WithholdingTax:int = obj["Rpt2WithholdingTax"]
      self.Rpt3WithholdingTax:int = obj["Rpt3WithholdingTax"]
      self.VendorNum:int = obj["VendorNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DebitDocumentsRow:
   def __init__(self, obj):
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DocumentID:str = obj["DocumentID"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.CustID:str = obj["CustID"]
      self.Selected:bool = obj["Selected"]
      self.Type:str = obj["Type"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.InvoiceDate:str = obj["InvoiceDate"]
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.InvoiceBal:int = obj["InvoiceBal"]
      self.DueDate:str = obj["DueDate"]
      self.InvoiceRef:str = obj["InvoiceRef"]
      self.TypeID:str = obj["TypeID"]
      """  The type of document as an ID, Type field hold the extended version.  """  
      self.DocWithholdingTax:int = obj["DocWithholdingTax"]
      self.WithholdingTax:int = obj["WithholdingTax"]
      self.Rpt1WithholdingTax:int = obj["Rpt1WithholdingTax"]
      self.Rpt2WithholdingTax:int = obj["Rpt2WithholdingTax"]
      self.Rpt3WithholdingTax:int = obj["Rpt3WithholdingTax"]
      self.VendorNum:int = obj["VendorNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_NettingDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.NettingID:int = obj["NettingID"]
      """  Netting Identifier  """  
      self.LineNum:int = obj["LineNum"]
      """  Netting Line Number  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  AR Invoice Number used in the Netting  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  AP Invoice Number used in the netting  """  
      self.InitialBalance:int = obj["InitialBalance"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.DocInitialBalance:int = obj["DocInitialBalance"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.Rpt1InitialBalance:int = obj["Rpt1InitialBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt2InitialBalance:int = obj["Rpt2InitialBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt3InitialBalance:int = obj["Rpt3InitialBalance"]
      """  Reporting currency value of this field  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date that the record was last changed  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DocWithholdingTax:int = obj["DocWithholdingTax"]
      """  Amount of withholding tax calculated if the invoice was to be paid in full.  """  
      self.WithholdingTax:int = obj["WithholdingTax"]
      """  Amount of withholding tax calculated if the invoice was to be paid in full.  """  
      self.Rpt1WithholdingTax:int = obj["Rpt1WithholdingTax"]
      """  Reporting currency value of this field  """  
      self.Rpt2WithholdingTax:int = obj["Rpt2WithholdingTax"]
      """  Reporting currency value of this field  """  
      self.Rpt3WithholdingTax:int = obj["Rpt3WithholdingTax"]
      """  Reporting currency value of this field  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_NettingHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.NettingID:int = obj["NettingID"]
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

class Erp_Tablesets_NettingHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.NettingID:int = obj["NettingID"]
      """  Indicates netting ID for this transaction  """  
      self.NettingDescription:str = obj["NettingDescription"]
      """  Netting Description  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader.  """  
      self.CreditAmt:int = obj["CreditAmt"]
      """  Credit Amount  """  
      self.DebitAmt:int = obj["DebitAmt"]
      """  Debit Amount  """  
      self.RemainingAmt:int = obj["RemainingAmt"]
      """  Remaining Amount  """  
      self.DocCreditAmt:int = obj["DocCreditAmt"]
      """  Document Credit Amount  """  
      self.Rpt1CreditAmt:int = obj["Rpt1CreditAmt"]
      """  Reporting 1 Credit Amount  """  
      self.Rpt2CreditAmt:int = obj["Rpt2CreditAmt"]
      """  Reporting 2 Credit Amount  """  
      self.Rpt3CreditAmt:int = obj["Rpt3CreditAmt"]
      """  Reporting 3 Credit Amount  """  
      self.DocDebitAmt:int = obj["DocDebitAmt"]
      """  Document Debit Amount  """  
      self.Rpt1DebitAmt:int = obj["Rpt1DebitAmt"]
      """  Reporting 1 Debit Amount  """  
      self.Rpt2DebitAmt:int = obj["Rpt2DebitAmt"]
      """  Reporting 2 Debit Amount  """  
      self.Rpt3DebitAmt:int = obj["Rpt3DebitAmt"]
      """  Reporting 3 Debit Amount  """  
      self.DocRemainingAmt:int = obj["DocRemainingAmt"]
      """  Document Remaining Amount  """  
      self.Rpt1RemainingAmt:int = obj["Rpt1RemainingAmt"]
      """  Reporting 1 Remaining Amount  """  
      self.Rpt2RemainingAmt:int = obj["Rpt2RemainingAmt"]
      """  Reporting 2 Remaining Amount  """  
      self.Rpt3RemainingAmt:int = obj["Rpt3RemainingAmt"]
      """  Reporting 3 Remaining Amount  """  
      self.CreateCashRcptPay:bool = obj["CreateCashRcptPay"]
      """  If checked, a cash receipt or payment will be created for the invoices remaining with balance after the netting.  """  
      self.CashPayGroupID:str = obj["CashPayGroupID"]
      """  Group ID set to the Cash Receipt or Payment if there was one created for the netting.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date that the record was last changed  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Customer Name.  This must be valid in the Customer table.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Supplier Name.  This must be valid in the Supplier table.  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID.  This must be valid in the Customer table.  """  
      self.VendorID:str = obj["VendorID"]
      """  Supplier ID  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      """  A unique code that identifies the currency.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Posting Engine Lock Status  """  
      self.IsLocked:bool = obj["IsLocked"]
      """  Flag if the document is locked by the Posting Engine  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Display Posting Engine Review Journal  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CustCustID:str = obj["CustCustID"]
      self.CustName:str = obj["CustName"]
      self.SupplierName:str = obj["SupplierName"]
      self.SupplierVendorID:str = obj["SupplierVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_NettingListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.NettingID:int = obj["NettingID"]
      """  Indicates netting ID for this transaction  """  
      self.NettingDescription:str = obj["NettingDescription"]
      """  Netting Description  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader.  """  
      self.CreditAmt:int = obj["CreditAmt"]
      """  Credit Amount  """  
      self.DebitAmt:int = obj["DebitAmt"]
      """  Debit Amount  """  
      self.RemainingAmt:int = obj["RemainingAmt"]
      """  Remaining Amount  """  
      self.DocCreditAmt:int = obj["DocCreditAmt"]
      """  Document Credit Amount  """  
      self.DocDebitAmt:int = obj["DocDebitAmt"]
      """  Document Debit Amount  """  
      self.DocRemainingAmt:int = obj["DocRemainingAmt"]
      """  Document Remaining Amount  """  
      self.CreateCashRcptPay:bool = obj["CreateCashRcptPay"]
      """  If checked, a cash receipt or payment will be created for the invoices remaining with balance after the netting.  """  
      self.CashPayGroupID:str = obj["CashPayGroupID"]
      """  Group ID set to the Cash Receipt or Payment if there was one created for the netting.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      self.CustomerName:str = obj["CustomerName"]
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CustID:str = obj["CustID"]
      self.VendorID:str = obj["VendorID"]
      self.CustCustID:str = obj["CustCustID"]
      self.CustName:str = obj["CustName"]
      self.SupplierName:str = obj["SupplierName"]
      self.SupplierVendorID:str = obj["SupplierVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   nettingID
   """  
   def __init__(self, obj):
      self.nettingID:int = obj["nettingID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteNettingDtl_input:
   """ Required : 
   nettingID
   vendorID
   custID
   currencyCode
   tranDate
   ds
   """  
   def __init__(self, obj):
      self.nettingID:int = obj["nettingID"]
      self.vendorID:str = obj["vendorID"]
      self.custID:str = obj["custID"]
      self.currencyCode:str = obj["currencyCode"]
      self.tranDate:str = obj["tranDate"]
      self.ds:list[Erp_Tablesets_NettingTableset] = obj["ds"]
      pass

class DeleteNettingDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NettingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_CreditDocumentsRow:
   def __init__(self, obj):
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DocumentID:str = obj["DocumentID"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.Selected:bool = obj["Selected"]
      self.Type:str = obj["Type"]
      self.VendorID:str = obj["VendorID"]
      self.InvoiceDate:str = obj["InvoiceDate"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.InvoiceBal:int = obj["InvoiceBal"]
      self.DueDate:str = obj["DueDate"]
      self.InvoiceRef:str = obj["InvoiceRef"]
      self.TypeID:str = obj["TypeID"]
      """  The type of document as an ID, Type field hold the extended version.  """  
      self.DocWithholdingTax:int = obj["DocWithholdingTax"]
      self.WithholdingTax:int = obj["WithholdingTax"]
      self.Rpt1WithholdingTax:int = obj["Rpt1WithholdingTax"]
      self.Rpt2WithholdingTax:int = obj["Rpt2WithholdingTax"]
      self.Rpt3WithholdingTax:int = obj["Rpt3WithholdingTax"]
      self.VendorNum:int = obj["VendorNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DebitDocumentsRow:
   def __init__(self, obj):
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DocumentID:str = obj["DocumentID"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.CustID:str = obj["CustID"]
      self.Selected:bool = obj["Selected"]
      self.Type:str = obj["Type"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.InvoiceDate:str = obj["InvoiceDate"]
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.InvoiceBal:int = obj["InvoiceBal"]
      self.DueDate:str = obj["DueDate"]
      self.InvoiceRef:str = obj["InvoiceRef"]
      self.TypeID:str = obj["TypeID"]
      """  The type of document as an ID, Type field hold the extended version.  """  
      self.DocWithholdingTax:int = obj["DocWithholdingTax"]
      self.WithholdingTax:int = obj["WithholdingTax"]
      self.Rpt1WithholdingTax:int = obj["Rpt1WithholdingTax"]
      self.Rpt2WithholdingTax:int = obj["Rpt2WithholdingTax"]
      self.Rpt3WithholdingTax:int = obj["Rpt3WithholdingTax"]
      self.VendorNum:int = obj["VendorNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_NettingDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.NettingID:int = obj["NettingID"]
      """  Netting Identifier  """  
      self.LineNum:int = obj["LineNum"]
      """  Netting Line Number  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  AR Invoice Number used in the Netting  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  AP Invoice Number used in the netting  """  
      self.InitialBalance:int = obj["InitialBalance"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.DocInitialBalance:int = obj["DocInitialBalance"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.Rpt1InitialBalance:int = obj["Rpt1InitialBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt2InitialBalance:int = obj["Rpt2InitialBalance"]
      """  Reporting currency value of this field  """  
      self.Rpt3InitialBalance:int = obj["Rpt3InitialBalance"]
      """  Reporting currency value of this field  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date that the record was last changed  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DocWithholdingTax:int = obj["DocWithholdingTax"]
      """  Amount of withholding tax calculated if the invoice was to be paid in full.  """  
      self.WithholdingTax:int = obj["WithholdingTax"]
      """  Amount of withholding tax calculated if the invoice was to be paid in full.  """  
      self.Rpt1WithholdingTax:int = obj["Rpt1WithholdingTax"]
      """  Reporting currency value of this field  """  
      self.Rpt2WithholdingTax:int = obj["Rpt2WithholdingTax"]
      """  Reporting currency value of this field  """  
      self.Rpt3WithholdingTax:int = obj["Rpt3WithholdingTax"]
      """  Reporting currency value of this field  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_NettingHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.NettingID:int = obj["NettingID"]
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

class Erp_Tablesets_NettingHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.NettingID:int = obj["NettingID"]
      """  Indicates netting ID for this transaction  """  
      self.NettingDescription:str = obj["NettingDescription"]
      """  Netting Description  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader.  """  
      self.CreditAmt:int = obj["CreditAmt"]
      """  Credit Amount  """  
      self.DebitAmt:int = obj["DebitAmt"]
      """  Debit Amount  """  
      self.RemainingAmt:int = obj["RemainingAmt"]
      """  Remaining Amount  """  
      self.DocCreditAmt:int = obj["DocCreditAmt"]
      """  Document Credit Amount  """  
      self.Rpt1CreditAmt:int = obj["Rpt1CreditAmt"]
      """  Reporting 1 Credit Amount  """  
      self.Rpt2CreditAmt:int = obj["Rpt2CreditAmt"]
      """  Reporting 2 Credit Amount  """  
      self.Rpt3CreditAmt:int = obj["Rpt3CreditAmt"]
      """  Reporting 3 Credit Amount  """  
      self.DocDebitAmt:int = obj["DocDebitAmt"]
      """  Document Debit Amount  """  
      self.Rpt1DebitAmt:int = obj["Rpt1DebitAmt"]
      """  Reporting 1 Debit Amount  """  
      self.Rpt2DebitAmt:int = obj["Rpt2DebitAmt"]
      """  Reporting 2 Debit Amount  """  
      self.Rpt3DebitAmt:int = obj["Rpt3DebitAmt"]
      """  Reporting 3 Debit Amount  """  
      self.DocRemainingAmt:int = obj["DocRemainingAmt"]
      """  Document Remaining Amount  """  
      self.Rpt1RemainingAmt:int = obj["Rpt1RemainingAmt"]
      """  Reporting 1 Remaining Amount  """  
      self.Rpt2RemainingAmt:int = obj["Rpt2RemainingAmt"]
      """  Reporting 2 Remaining Amount  """  
      self.Rpt3RemainingAmt:int = obj["Rpt3RemainingAmt"]
      """  Reporting 3 Remaining Amount  """  
      self.CreateCashRcptPay:bool = obj["CreateCashRcptPay"]
      """  If checked, a cash receipt or payment will be created for the invoices remaining with balance after the netting.  """  
      self.CashPayGroupID:str = obj["CashPayGroupID"]
      """  Group ID set to the Cash Receipt or Payment if there was one created for the netting.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date that the record was last changed  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Customer Name.  This must be valid in the Customer table.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Supplier Name.  This must be valid in the Supplier table.  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID.  This must be valid in the Customer table.  """  
      self.VendorID:str = obj["VendorID"]
      """  Supplier ID  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      """  A unique code that identifies the currency.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Posting Engine Lock Status  """  
      self.IsLocked:bool = obj["IsLocked"]
      """  Flag if the document is locked by the Posting Engine  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Display Posting Engine Review Journal  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CustCustID:str = obj["CustCustID"]
      self.CustName:str = obj["CustName"]
      self.SupplierName:str = obj["SupplierName"]
      self.SupplierVendorID:str = obj["SupplierVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_NettingListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.NettingID:int = obj["NettingID"]
      """  Indicates netting ID for this transaction  """  
      self.NettingDescription:str = obj["NettingDescription"]
      """  Netting Description  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader.  """  
      self.CreditAmt:int = obj["CreditAmt"]
      """  Credit Amount  """  
      self.DebitAmt:int = obj["DebitAmt"]
      """  Debit Amount  """  
      self.RemainingAmt:int = obj["RemainingAmt"]
      """  Remaining Amount  """  
      self.DocCreditAmt:int = obj["DocCreditAmt"]
      """  Document Credit Amount  """  
      self.DocDebitAmt:int = obj["DocDebitAmt"]
      """  Document Debit Amount  """  
      self.DocRemainingAmt:int = obj["DocRemainingAmt"]
      """  Document Remaining Amount  """  
      self.CreateCashRcptPay:bool = obj["CreateCashRcptPay"]
      """  If checked, a cash receipt or payment will be created for the invoices remaining with balance after the netting.  """  
      self.CashPayGroupID:str = obj["CashPayGroupID"]
      """  Group ID set to the Cash Receipt or Payment if there was one created for the netting.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      self.CustomerName:str = obj["CustomerName"]
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CustID:str = obj["CustID"]
      self.VendorID:str = obj["VendorID"]
      self.CustCustID:str = obj["CustCustID"]
      self.CustName:str = obj["CustName"]
      self.SupplierName:str = obj["SupplierName"]
      self.SupplierVendorID:str = obj["SupplierVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_NettingListTableset:
   def __init__(self, obj):
      self.NettingList:list[Erp_Tablesets_NettingListRow] = obj["NettingList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_NettingTableset:
   def __init__(self, obj):
      self.NettingHead:list[Erp_Tablesets_NettingHeadRow] = obj["NettingHead"]
      self.NettingHeadAttch:list[Erp_Tablesets_NettingHeadAttchRow] = obj["NettingHeadAttch"]
      self.NettingDtl:list[Erp_Tablesets_NettingDtlRow] = obj["NettingDtl"]
      self.CreditDocuments:list[Erp_Tablesets_CreditDocumentsRow] = obj["CreditDocuments"]
      self.DebitDocuments:list[Erp_Tablesets_DebitDocumentsRow] = obj["DebitDocuments"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtNettingTableset:
   def __init__(self, obj):
      self.NettingHead:list[Erp_Tablesets_NettingHeadRow] = obj["NettingHead"]
      self.NettingHeadAttch:list[Erp_Tablesets_NettingHeadAttchRow] = obj["NettingHeadAttch"]
      self.NettingDtl:list[Erp_Tablesets_NettingDtlRow] = obj["NettingDtl"]
      self.CreditDocuments:list[Erp_Tablesets_CreditDocumentsRow] = obj["CreditDocuments"]
      self.DebitDocuments:list[Erp_Tablesets_DebitDocumentsRow] = obj["DebitDocuments"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   nettingID
   """  
   def __init__(self, obj):
      self.nettingID:int = obj["nettingID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_NettingTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_NettingTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_NettingTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_NettingListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewNettingDtl_input:
   """ Required : 
   ds
   nettingID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NettingTableset] = obj["ds"]
      self.nettingID:int = obj["nettingID"]
      pass

class GetNewNettingDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NettingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewNettingHeadAttch_input:
   """ Required : 
   ds
   nettingID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NettingTableset] = obj["ds"]
      self.nettingID:int = obj["nettingID"]
      pass

class GetNewNettingHeadAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NettingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewNettingHead_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NettingTableset] = obj["ds"]
      pass

class GetNewNettingHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NettingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseNettingHead
   whereClauseNettingHeadAttch
   whereClauseNettingDtl
   whereClauseCreditDocuments
   whereClauseDebitDocuments
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseNettingHead:str = obj["whereClauseNettingHead"]
      self.whereClauseNettingHeadAttch:str = obj["whereClauseNettingHeadAttch"]
      self.whereClauseNettingDtl:str = obj["whereClauseNettingDtl"]
      self.whereClauseCreditDocuments:str = obj["whereClauseCreditDocuments"]
      self.whereClauseDebitDocuments:str = obj["whereClauseDebitDocuments"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_NettingTableset] = obj["returnObj"]
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

class OnChangeSelectedCredits_input:
   """ Required : 
   nettingID
   documentID
   selected
   ds
   """  
   def __init__(self, obj):
      self.nettingID:int = obj["nettingID"]
      self.documentID:str = obj["documentID"]
      self.selected:bool = obj["selected"]
      self.ds:list[Erp_Tablesets_NettingTableset] = obj["ds"]
      pass

class OnChangeSelectedCredits_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NettingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeSelectedDebits_input:
   """ Required : 
   nettingID
   documentID
   selected
   ds
   """  
   def __init__(self, obj):
      self.nettingID:int = obj["nettingID"]
      self.documentID:str = obj["documentID"]
      self.selected:bool = obj["selected"]
      self.ds:list[Erp_Tablesets_NettingTableset] = obj["ds"]
      pass

class OnChangeSelectedDebits_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NettingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeofCustID_input:
   """ Required : 
   proposedCustID
   ds
   """  
   def __init__(self, obj):
      self.proposedCustID:str = obj["proposedCustID"]
      self.ds:list[Erp_Tablesets_NettingTableset] = obj["ds"]
      pass

class OnChangeofCustID_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NettingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeofVendorID_input:
   """ Required : 
   proposedVendorID
   ds
   """  
   def __init__(self, obj):
      self.proposedVendorID:str = obj["proposedVendorID"]
      self.ds:list[Erp_Tablesets_NettingTableset] = obj["ds"]
      pass

class OnChangeofVendorID_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NettingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtNettingTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtNettingTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NettingTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NettingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateCreditDebitSelection_input:
   """ Required : 
   nettingID
   """  
   def __init__(self, obj):
      self.nettingID:int = obj["nettingID"]
      """  nettingID  """  
      pass

class ValidateCreditDebitSelection_output:
   def __init__(self, obj):
      pass

class ValidateEnableNetting_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

