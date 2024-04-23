import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MktgLstSvc
# Description: Marketing Lists file.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_MktgLsts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MktgLsts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MktgLsts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MktgListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/MktgLsts",headers=creds) as resp:
           return await resp.json()

async def post_MktgLsts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MktgLsts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MktgListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MktgListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/MktgLsts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MktgLsts_Company_MktgListID(Company, MktgListID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MktgLst item
   Description: Calls GetByID to retrieve the MktgLst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MktgLst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MktgListID: Desc: MktgListID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MktgListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/MktgLsts(" + Company + "," + MktgListID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MktgLsts_Company_MktgListID(Company, MktgListID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MktgLst for the service
   Description: Calls UpdateExt to update MktgLst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MktgLst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MktgListID: Desc: MktgListID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MktgListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/MktgLsts(" + Company + "," + MktgListID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MktgLsts_Company_MktgListID(Company, MktgListID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MktgLst item
   Description: Call UpdateExt to delete MktgLst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MktgLst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MktgListID: Desc: MktgListID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/MktgLsts(" + Company + "," + MktgListID + ")",headers=creds) as resp:
           return await resp.json()

async def get_MktgLsts_Company_MktgListID_MktgLstDtls(Company, MktgListID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MktgLstDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MktgLstDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MktgListID: Desc: MktgListID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MktgLstDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/MktgLsts(" + Company + "," + MktgListID + ")/MktgLstDtls",headers=creds) as resp:
           return await resp.json()

async def get_MktgLsts_Company_MktgListID_MktgLstDtls_Company_MktgListID_SeqNum(Company, MktgListID, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MktgLstDtl item
   Description: Calls GetByID to retrieve the MktgLstDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MktgLstDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MktgListID: Desc: MktgListID   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MktgLstDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/MktgLsts(" + Company + "," + MktgListID + ")/MktgLstDtls(" + Company + "," + MktgListID + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_MktgLsts_Company_MktgListID_MktgListAttches(Company, MktgListID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MktgListAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MktgListAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MktgListID: Desc: MktgListID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MktgListAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/MktgLsts(" + Company + "," + MktgListID + ")/MktgListAttches",headers=creds) as resp:
           return await resp.json()

async def get_MktgLsts_Company_MktgListID_MktgListAttches_Company_MktgListID_DrawingSeq(Company, MktgListID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MktgListAttch item
   Description: Calls GetByID to retrieve the MktgListAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MktgListAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MktgListID: Desc: MktgListID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MktgListAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/MktgLsts(" + Company + "," + MktgListID + ")/MktgListAttches(" + Company + "," + MktgListID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_MktgLstDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MktgLstDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MktgLstDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MktgLstDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/MktgLstDtls",headers=creds) as resp:
           return await resp.json()

async def post_MktgLstDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MktgLstDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MktgLstDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MktgLstDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/MktgLstDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MktgLstDtls_Company_MktgListID_SeqNum(Company, MktgListID, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MktgLstDtl item
   Description: Calls GetByID to retrieve the MktgLstDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MktgLstDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MktgListID: Desc: MktgListID   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MktgLstDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/MktgLstDtls(" + Company + "," + MktgListID + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MktgLstDtls_Company_MktgListID_SeqNum(Company, MktgListID, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MktgLstDtl for the service
   Description: Calls UpdateExt to update MktgLstDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MktgLstDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MktgListID: Desc: MktgListID   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MktgLstDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/MktgLstDtls(" + Company + "," + MktgListID + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MktgLstDtls_Company_MktgListID_SeqNum(Company, MktgListID, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MktgLstDtl item
   Description: Call UpdateExt to delete MktgLstDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MktgLstDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MktgListID: Desc: MktgListID   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/MktgLstDtls(" + Company + "," + MktgListID + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_MktgListAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MktgListAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MktgListAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MktgListAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/MktgListAttches",headers=creds) as resp:
           return await resp.json()

async def post_MktgListAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MktgListAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MktgListAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MktgListAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/MktgListAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MktgListAttches_Company_MktgListID_DrawingSeq(Company, MktgListID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MktgListAttch item
   Description: Calls GetByID to retrieve the MktgListAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MktgListAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MktgListID: Desc: MktgListID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MktgListAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/MktgListAttches(" + Company + "," + MktgListID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MktgListAttches_Company_MktgListID_DrawingSeq(Company, MktgListID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MktgListAttch for the service
   Description: Calls UpdateExt to update MktgListAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MktgListAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MktgListID: Desc: MktgListID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MktgListAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/MktgListAttches(" + Company + "," + MktgListID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MktgListAttches_Company_MktgListID_DrawingSeq(Company, MktgListID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MktgListAttch item
   Description: Call UpdateExt to delete MktgListAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MktgListAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MktgListID: Desc: MktgListID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/MktgListAttches(" + Company + "," + MktgListID + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MktgListListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseMktgList, whereClauseMktgListAttch, whereClauseMktgLstDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseMktgList=" + whereClauseMktgList
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMktgListAttch=" + whereClauseMktgListAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMktgLstDtl=" + whereClauseMktgLstDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(mktgListID, epicorHeaders = None):
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
   params += "mktgListID=" + mktgListID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangedCreateCall(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedCreateCall
   Description: This method refreshes the dataset when the CreateTask flage is turned off
   OperationID: ChangedCreateCall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedCreateCall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedCreateCall_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangedCreateTask(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedCreateTask
   Description: This method refreshes the dataset when the CreateTask flage is turned off
   OperationID: ChangedCreateTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedCreateTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedCreateTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyDtlFrom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyDtlFrom
   Description: This method copies detail records from another MktgList to the current MktgList
   OperationID: CopyDtlFrom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyDtlFrom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyDtlFrom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateMktgLstDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateMktgLstDtl
   Description: This method creates detail records from MktgListGenerate dataset
   OperationID: GenerateMktgLstDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateMktgLstDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateMktgLstDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetExportList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetExportList
   Description: This method creates the MktgLstExp table using the values in the MktgLstExpParam table
   OperationID: GetExportList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExportList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExportList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExportParam(epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExportParam
   Description: This method creates the MktgLstParam table for use in the export process
   OperationID: GetNewExportParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExportParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCallType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCallType
   Description: This method validates and defaults Call Type information when CallType is changed
   OperationID: OnChangeCallType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCallType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCallType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCampaignID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCampaignID
   Description: This method validates the Campaign ID when the user changes the value
   OperationID: OnChangeCampaignID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCampaignID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCampaignID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeConNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeConNum
   Description: This method validates the Contact when the user changes the value
   OperationID: OnChangeConNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeConNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeConNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCustID
   Description: This method validates the Customer ID when the user changes the value
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeEvntSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeEvntSeq
   Description: This method validates the Event Sequence when the user changes the value
   OperationID: OnChangeEvntSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeEvntSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeEvntSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeShipTo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeShipTo
   Description: This method validates the Ship To Number when the user changes the value
   OperationID: OnChangeShipTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTaskID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTaskID
   Description: This method validates and defaults Task information when TaskID is changed
   OperationID: OnChangeTaskID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaskID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaskID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTaskType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTaskType
   Description: This method validates and defaults Task Type information when TaskType is changed
   OperationID: OnChangeTaskType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaskType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaskType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrePullList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrePullList
   Description: This method is to be run before the PullList method to validate the BatchID
if the batch Id already exists for the target Marketing List a question will
be returned to the user asking them if they'd like to reuse the batch ID.
If the user answers yes they can continue on to the PullList method.
   OperationID: PrePullList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePullList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePullList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PullList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PullList
   Description: This method takes the Busines Activity Query ID and runs the query internally.
It will create MktLstDtl record for every Customer/Contact that is returned by
the B.A. Query and will return the updated dataset to the UI
   OperationID: PullList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PullList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PullList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetVRDescription(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetVRDescription
   OperationID: GetVRDescription
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVRDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVRDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportListToCSV(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportListToCSV
   OperationID: ExportListToCSV
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportListToCSV_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportListToCSV_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBAQID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBAQID
   Description: Check entered BAQ ID
   OperationID: CheckBAQID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBAQID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBAQID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMktgList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMktgList
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMktgList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMktgList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMktgList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMktgListAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMktgListAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMktgListAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMktgListAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMktgListAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMktgLstDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMktgLstDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMktgLstDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMktgLstDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMktgLstDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MktgLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MktgListAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MktgListAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MktgListListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MktgListListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MktgListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MktgListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MktgLstDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MktgLstDtlRow] = obj["value"]
      pass

class Erp_Tablesets_MktgListAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.MktgListID:str = obj["MktgListID"]
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

class Erp_Tablesets_MktgListListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MktgListID:str = obj["MktgListID"]
      """  Identifier for this list.  """  
      self.ListDescription:str = obj["ListDescription"]
      """  Description, defaults from the Marketing Events table.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Creation Date  """  
      self.ModifiedDate:str = obj["ModifiedDate"]
      """  Modification Date  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Created by  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  Link to the Marketing Campaign related to this event.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  A sequence number that uniquely defines the MktgEvnt record within a specific MktgCamp. This is system assigned.  The next available number is determined by reading last MktgEvnt record on the Mktgcamp and then adding ten to it.  """  
      self.LastPullQuery:str = obj["LastPullQuery"]
      """  Last pulled query  """  
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
      self.MktgCampaignIDCampDescription:str = obj["MktgCampaignIDCampDescription"]
      """  Description of the Marketing campaign  """  
      self.MktgEvntSeqEvntDescription:str = obj["MktgEvntSeqEvntDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MktgListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MktgListID:str = obj["MktgListID"]
      """  Identifier for this list.  """  
      self.ListDescription:str = obj["ListDescription"]
      """  Description, defaults from the Marketing Events table.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Creation Date  """  
      self.ModifiedDate:str = obj["ModifiedDate"]
      """  Modification Date  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Created by  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  Link to the Marketing Campaign related to this event.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  A sequence number that uniquely defines the MktgEvnt record within a specific MktgCamp. This is system assigned.  The next available number is determined by reading last MktgEvnt record on the Mktgcamp and then adding ten to it.  """  
      self.LastPullQuery:str = obj["LastPullQuery"]
      """  Last pulled query  """  
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
      self.MktgCampaignIDCampDescription:str = obj["MktgCampaignIDCampDescription"]
      self.MktgEvntSeqEvntDescription:str = obj["MktgEvntSeqEvntDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MktgLstDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MktgListID:str = obj["MktgListID"]
      """  Identifier for this list.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Marketing list detail sequence  """  
      self.type:str = obj["type"]
      """  Marketing list detail type  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The number that the user assigned to the ship to that this contact is related to.  Note that this field is blank for contacts related to the customer only.  """  
      self.ConNum:int = obj["ConNum"]
      """  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  """  
      self.BatchID:str = obj["BatchID"]
      """  Batch ID  """  
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
      self.DisplayName:str = obj["DisplayName"]
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.BitFlag:int = obj["BitFlag"]
      self.ConNumFirstName:str = obj["ConNumFirstName"]
      self.ConNumCorpName:str = obj["ConNumCorpName"]
      self.ConNumName:str = obj["ConNumName"]
      self.ConNumFaxNum:str = obj["ConNumFaxNum"]
      self.ConNumPhoneNum:str = obj["ConNumPhoneNum"]
      self.ConNumLastName:str = obj["ConNumLastName"]
      self.ConNumMiddleName:str = obj["ConNumMiddleName"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.MktgListIDListDescription:str = obj["MktgListIDListDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangedCreateCall_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstExpTableset] = obj["ds"]
      pass

class ChangedCreateCall_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstExpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangedCreateTask_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstExpTableset] = obj["ds"]
      pass

class ChangedCreateTask_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstExpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckBAQID_input:
   """ Required : 
   ipBAQID
   """  
   def __init__(self, obj):
      self.ipBAQID:str = obj["ipBAQID"]
      pass

class CheckBAQID_output:
   def __init__(self, obj):
      pass

class CopyDtlFrom_input:
   """ Required : 
   fromListID
   toListID
   """  
   def __init__(self, obj):
      self.fromListID:str = obj["fromListID"]
      """  Marketing List ID to copy FROM  """  
      self.toListID:str = obj["toListID"]
      """  Marketing List ID to copy TO  """  
      pass

class CopyDtlFrom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MktgLstTableset] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   mktgListID
   """  
   def __init__(self, obj):
      self.mktgListID:str = obj["mktgListID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_MktgListAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.MktgListID:str = obj["MktgListID"]
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

class Erp_Tablesets_MktgListListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MktgListID:str = obj["MktgListID"]
      """  Identifier for this list.  """  
      self.ListDescription:str = obj["ListDescription"]
      """  Description, defaults from the Marketing Events table.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Creation Date  """  
      self.ModifiedDate:str = obj["ModifiedDate"]
      """  Modification Date  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Created by  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  Link to the Marketing Campaign related to this event.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  A sequence number that uniquely defines the MktgEvnt record within a specific MktgCamp. This is system assigned.  The next available number is determined by reading last MktgEvnt record on the Mktgcamp and then adding ten to it.  """  
      self.LastPullQuery:str = obj["LastPullQuery"]
      """  Last pulled query  """  
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
      self.MktgCampaignIDCampDescription:str = obj["MktgCampaignIDCampDescription"]
      """  Description of the Marketing campaign  """  
      self.MktgEvntSeqEvntDescription:str = obj["MktgEvntSeqEvntDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MktgListListTableset:
   def __init__(self, obj):
      self.MktgListList:list[Erp_Tablesets_MktgListListRow] = obj["MktgListList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MktgListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MktgListID:str = obj["MktgListID"]
      """  Identifier for this list.  """  
      self.ListDescription:str = obj["ListDescription"]
      """  Description, defaults from the Marketing Events table.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Creation Date  """  
      self.ModifiedDate:str = obj["ModifiedDate"]
      """  Modification Date  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Created by  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  Link to the Marketing Campaign related to this event.  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  A sequence number that uniquely defines the MktgEvnt record within a specific MktgCamp. This is system assigned.  The next available number is determined by reading last MktgEvnt record on the Mktgcamp and then adding ten to it.  """  
      self.LastPullQuery:str = obj["LastPullQuery"]
      """  Last pulled query  """  
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
      self.MktgCampaignIDCampDescription:str = obj["MktgCampaignIDCampDescription"]
      self.MktgEvntSeqEvntDescription:str = obj["MktgEvntSeqEvntDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MktgLstDtlGenerateRow:
   def __init__(self, obj):
      self.CustID:str = obj["CustID"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.ConNum:int = obj["ConNum"]
      self.MktgListID:str = obj["MktgListID"]
      self.BatchID:str = obj["BatchID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MktgLstDtlGenerateTableset:
   def __init__(self, obj):
      self.MktgLstDtlGenerate:list[Erp_Tablesets_MktgLstDtlGenerateRow] = obj["MktgLstDtlGenerate"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MktgLstDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MktgListID:str = obj["MktgListID"]
      """  Identifier for this list.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Marketing list detail sequence  """  
      self.type:str = obj["type"]
      """  Marketing list detail type  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The number that the user assigned to the ship to that this contact is related to.  Note that this field is blank for contacts related to the customer only.  """  
      self.ConNum:int = obj["ConNum"]
      """  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  """  
      self.BatchID:str = obj["BatchID"]
      """  Batch ID  """  
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
      self.DisplayName:str = obj["DisplayName"]
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.BitFlag:int = obj["BitFlag"]
      self.ConNumFirstName:str = obj["ConNumFirstName"]
      self.ConNumCorpName:str = obj["ConNumCorpName"]
      self.ConNumName:str = obj["ConNumName"]
      self.ConNumFaxNum:str = obj["ConNumFaxNum"]
      self.ConNumPhoneNum:str = obj["ConNumPhoneNum"]
      self.ConNumLastName:str = obj["ConNumLastName"]
      self.ConNumMiddleName:str = obj["ConNumMiddleName"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.MktgListIDListDescription:str = obj["MktgListIDListDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MktgLstExpParamRow:
   def __init__(self, obj):
      self.FileName:str = obj["FileName"]
      self.OutputFormat:str = obj["OutputFormat"]
      self.CreateCall:bool = obj["CreateCall"]
      """  Create Service call record  """  
      self.CallDescription:str = obj["CallDescription"]
      self.CallType:str = obj["CallType"]
      self.CallTypeDesc:str = obj["CallTypeDesc"]
      self.CreateTask:bool = obj["CreateTask"]
      self.TaskID:str = obj["TaskID"]
      self.TaskType:str = obj["TaskType"]
      self.TaskTypeDesc:str = obj["TaskTypeDesc"]
      self.StartDate:str = obj["StartDate"]
      self.DueDate:str = obj["DueDate"]
      self.SendAlert:bool = obj["SendAlert"]
      self.TaskComment:str = obj["TaskComment"]
      self.TaskDesc:str = obj["TaskDesc"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MktgLstExpRow:
   def __init__(self, obj):
      self.CustID:str = obj["CustID"]
      self.Name:str = obj["Name"]
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      self.Zip:str = obj["Zip"]
      self.Country:str = obj["Country"]
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.TerritoryID:str = obj["TerritoryID"]
      self.FaxNum:str = obj["FaxNum"]
      self.PhoneNum:str = obj["PhoneNum"]
      self.NoContact:int = obj["NoContact"]
      self.EMailAddress:str = obj["EMailAddress"]
      self.CustomerType:str = obj["CustomerType"]
      self.CustURL:str = obj["CustURL"]
      self.ExtID:str = obj["ExtID"]
      self.Character01:str = obj["Character01"]
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
      self.Date02:str = obj["Date02"]
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.Date05:str = obj["Date05"]
      self.CheckBox01:int = obj["CheckBox01"]
      self.CheckBox02:int = obj["CheckBox02"]
      self.CheckBox03:int = obj["CheckBox03"]
      self.CheckBox04:int = obj["CheckBox04"]
      self.CheckBox05:int = obj["CheckBox05"]
      self.ContactName:str = obj["ContactName"]
      self.ContactPrefix:str = obj["ContactPrefix"]
      self.ContactInitials:str = obj["ContactInitials"]
      self.ContactFirstName:str = obj["ContactFirstName"]
      self.ContactMiddleName:str = obj["ContactMiddleName"]
      self.ContactLastName:str = obj["ContactLastName"]
      self.ContactSuffix:str = obj["ContactSuffix"]
      self.ContactFunc:str = obj["ContactFunc"]
      self.ContactSpecialAddress:int = obj["ContactSpecialAddress"]
      self.ContactAddress1:str = obj["ContactAddress1"]
      self.ContactAddress2:str = obj["ContactAddress2"]
      self.ContactAddress3:str = obj["ContactAddress3"]
      self.ContactCity:str = obj["ContactCity"]
      self.ContactState:str = obj["ContactState"]
      self.ContactZip:str = obj["ContactZip"]
      self.ContactCountry:str = obj["ContactCountry"]
      self.ContactFaxNum:str = obj["ContactFaxNum"]
      self.ContactPhoneNum:str = obj["ContactPhoneNum"]
      self.ContactCorpName:str = obj["ContactCorpName"]
      self.ContactEMailAddress:str = obj["ContactEMailAddress"]
      self.ContactRoleCode:str = obj["ContactRoleCode"]
      self.ContactCellPhoneNum:str = obj["ContactCellPhoneNum"]
      self.ContactPagerNum:str = obj["ContactPagerNum"]
      self.ContactHomeNum:str = obj["ContactHomeNum"]
      self.ContactAltNum:str = obj["ContactAltNum"]
      self.ContactContactTitle:str = obj["ContactContactTitle"]
      self.ContactNoContact:int = obj["ContactNoContact"]
      self.ContactCharacter01:str = obj["ContactCharacter01"]
      self.ContactCharacter02:str = obj["ContactCharacter02"]
      self.ContactCharacter03:str = obj["ContactCharacter03"]
      self.ContactCharacter04:str = obj["ContactCharacter04"]
      self.ContactCharacter05:str = obj["ContactCharacter05"]
      self.ContactCharacter06:str = obj["ContactCharacter06"]
      self.ContactCharacter07:str = obj["ContactCharacter07"]
      self.ContactCharacter08:str = obj["ContactCharacter08"]
      self.ContactCharacter09:str = obj["ContactCharacter09"]
      self.ContactCharacter10:str = obj["ContactCharacter10"]
      self.ContactNumber01:int = obj["ContactNumber01"]
      self.ContactNumber02:int = obj["ContactNumber02"]
      self.ContactNumber03:int = obj["ContactNumber03"]
      self.ContactNumber04:int = obj["ContactNumber04"]
      self.ContactNumber05:int = obj["ContactNumber05"]
      self.ContactNumber06:int = obj["ContactNumber06"]
      self.ContactNumber07:int = obj["ContactNumber07"]
      self.ContactNumber08:int = obj["ContactNumber08"]
      self.ContactNumber09:int = obj["ContactNumber09"]
      self.ContactNumber10:int = obj["ContactNumber10"]
      self.ContactDate01:str = obj["ContactDate01"]
      self.ContactDate02:str = obj["ContactDate02"]
      self.ContactDate03:str = obj["ContactDate03"]
      self.ContactDate04:str = obj["ContactDate04"]
      self.ContactDate05:str = obj["ContactDate05"]
      self.ContactCheckBox01:int = obj["ContactCheckBox01"]
      self.ContactCheckBox02:int = obj["ContactCheckBox02"]
      self.ContactCheckBox03:int = obj["ContactCheckBox03"]
      self.ContactCheckBox04:int = obj["ContactCheckBox04"]
      self.ContactCheckBox05:int = obj["ContactCheckBox05"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MktgLstExpTableset:
   def __init__(self, obj):
      self.MktgLstExp:list[Erp_Tablesets_MktgLstExpRow] = obj["MktgLstExp"]
      self.MktgLstExpParam:list[Erp_Tablesets_MktgLstExpParamRow] = obj["MktgLstExpParam"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MktgLstTableset:
   def __init__(self, obj):
      self.MktgList:list[Erp_Tablesets_MktgListRow] = obj["MktgList"]
      self.MktgListAttch:list[Erp_Tablesets_MktgListAttchRow] = obj["MktgListAttch"]
      self.MktgLstDtl:list[Erp_Tablesets_MktgLstDtlRow] = obj["MktgLstDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtMktgLstTableset:
   def __init__(self, obj):
      self.MktgList:list[Erp_Tablesets_MktgListRow] = obj["MktgList"]
      self.MktgListAttch:list[Erp_Tablesets_MktgListAttchRow] = obj["MktgListAttch"]
      self.MktgLstDtl:list[Erp_Tablesets_MktgLstDtlRow] = obj["MktgLstDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExportListToCSV_input:
   """ Required : 
   mktgListID
   ds
   """  
   def __init__(self, obj):
      self.mktgListID:str = obj["mktgListID"]
      self.ds:list[Erp_Tablesets_MktgLstExpTableset] = obj["ds"]
      pass

class ExportListToCSV_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstExpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GenerateMktgLstDtl_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstDtlGenerateTableset] = obj["ds"]
      pass

class GenerateMktgLstDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstDtlGenerateTableset] = obj["ds"]
      self.statusMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   mktgListID
   """  
   def __init__(self, obj):
      self.mktgListID:str = obj["mktgListID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MktgLstTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MktgLstTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MktgLstTableset] = obj["returnObj"]
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

class GetExportList_input:
   """ Required : 
   listID
   ds
   """  
   def __init__(self, obj):
      self.listID:str = obj["listID"]
      """  Marketing List to export  """  
      self.ds:list[Erp_Tablesets_MktgLstExpTableset] = obj["ds"]
      pass

class GetExportList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstExpTableset] = obj["ds"]
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
      self.returnObj:list[Erp_Tablesets_MktgListListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewExportParam_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MktgLstExpTableset] = obj["returnObj"]
      pass

class GetNewMktgListAttch_input:
   """ Required : 
   ds
   mktgListID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstTableset] = obj["ds"]
      self.mktgListID:str = obj["mktgListID"]
      pass

class GetNewMktgListAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMktgList_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstTableset] = obj["ds"]
      pass

class GetNewMktgList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMktgLstDtl_input:
   """ Required : 
   ds
   mktgListID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstTableset] = obj["ds"]
      self.mktgListID:str = obj["mktgListID"]
      pass

class GetNewMktgLstDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseMktgList
   whereClauseMktgListAttch
   whereClauseMktgLstDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMktgList:str = obj["whereClauseMktgList"]
      self.whereClauseMktgListAttch:str = obj["whereClauseMktgListAttch"]
      self.whereClauseMktgLstDtl:str = obj["whereClauseMktgLstDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MktgLstTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetVRDescription_input:
   """ Required : 
   tableName
   fieldName
   fieldValue
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      self.fieldValue:str = obj["fieldValue"]
      pass

class GetVRDescription_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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

class OnChangeCallType_input:
   """ Required : 
   _callType
   ds
   """  
   def __init__(self, obj):
      self._callType:str = obj["_callType"]
      """  Proposed Call Type  """  
      self.ds:list[Erp_Tablesets_MktgLstExpTableset] = obj["ds"]
      pass

class OnChangeCallType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstExpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeCampaignID_input:
   """ Required : 
   campaignID
   ds
   """  
   def __init__(self, obj):
      self.campaignID:str = obj["campaignID"]
      """  Proposed Marketing Campaign ID  """  
      self.ds:list[Erp_Tablesets_MktgLstTableset] = obj["ds"]
      pass

class OnChangeCampaignID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeConNum_input:
   """ Required : 
   conNum
   ds
   """  
   def __init__(self, obj):
      self.conNum:int = obj["conNum"]
      """  Proposed Contact Number  """  
      self.ds:list[Erp_Tablesets_MktgLstTableset] = obj["ds"]
      pass

class OnChangeConNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeCustID_input:
   """ Required : 
   custID
   ds
   """  
   def __init__(self, obj):
      self.custID:str = obj["custID"]
      """  Proposed Customer ID  """  
      self.ds:list[Erp_Tablesets_MktgLstTableset] = obj["ds"]
      pass

class OnChangeCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeEvntSeq_input:
   """ Required : 
   evntSeq
   ds
   """  
   def __init__(self, obj):
      self.evntSeq:int = obj["evntSeq"]
      """  Proposed Marketing Event Sequence  """  
      self.ds:list[Erp_Tablesets_MktgLstTableset] = obj["ds"]
      pass

class OnChangeEvntSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeShipTo_input:
   """ Required : 
   _shipTo
   ds
   """  
   def __init__(self, obj):
      self._shipTo:str = obj["_shipTo"]
      """  Proposed ShipTo Number  """  
      self.ds:list[Erp_Tablesets_MktgLstTableset] = obj["ds"]
      pass

class OnChangeShipTo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTaskID_input:
   """ Required : 
   listID
   taskID
   ds
   """  
   def __init__(self, obj):
      self.listID:str = obj["listID"]
      """  Marketing List to export  """  
      self.taskID:str = obj["taskID"]
      """  Proposed Task ID  """  
      self.ds:list[Erp_Tablesets_MktgLstExpTableset] = obj["ds"]
      pass

class OnChangeTaskID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstExpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTaskType_input:
   """ Required : 
   _taskType
   ds
   """  
   def __init__(self, obj):
      self._taskType:str = obj["_taskType"]
      """  Proposed TaskType value  """  
      self.ds:list[Erp_Tablesets_MktgLstExpTableset] = obj["ds"]
      pass

class OnChangeTaskType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstExpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PrePullList_input:
   """ Required : 
   listID
   batchID
   """  
   def __init__(self, obj):
      self.listID:str = obj["listID"]
      """  Marketing List ID to add the data to  """  
      self.batchID:str = obj["batchID"]
      """  Batch id associated with the execution of the query  """  
      pass

class PrePullList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vQuestion:str = obj["parameters"]
      pass

      """  output parameters  """  

class PullList_input:
   """ Required : 
   queryID
   listID
   batchID
   noCustomer
   ds
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  Business Activity ID to run  """  
      self.listID:str = obj["listID"]
      """  Marketing List ID to add the data to  """  
      self.batchID:str = obj["batchID"]
      """  Batch id associated with the execution of the query  """  
      self.noCustomer:bool = obj["noCustomer"]
      """  If true, then only contacts will be created,
            otherwise a Customer record for every contact will be created  """  
      self.ds:list[Erp_Tablesets_MktgLstTableset] = obj["ds"]
      pass

class PullList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMktgLstTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMktgLstTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MktgLstTableset] = obj["ds"]
      pass

      """  output parameters  """  

