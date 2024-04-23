import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ReqSvc
# Description: Requisition Entry Business object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Reqs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Reqs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Reqs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReqHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/Reqs",headers=creds) as resp:
           return await resp.json()

async def post_Reqs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Reqs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ReqHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ReqHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/Reqs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Reqs_Company_ReqNum(Company, ReqNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Req item
   Description: Calls GetByID to retrieve the Req item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Req
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReqNum: Desc: ReqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ReqHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/Reqs(" + Company + "," + ReqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Reqs_Company_ReqNum(Company, ReqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Req for the service
   Description: Calls UpdateExt to update Req. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Req
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReqNum: Desc: ReqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ReqHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/Reqs(" + Company + "," + ReqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Reqs_Company_ReqNum(Company, ReqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Req item
   Description: Call UpdateExt to delete Req item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Req
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReqNum: Desc: ReqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/Reqs(" + Company + "," + ReqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_Reqs_Company_ReqNum_ReqDetails(Company, ReqNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ReqDetails items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ReqDetails1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReqNum: Desc: ReqNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReqDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/Reqs(" + Company + "," + ReqNum + ")/ReqDetails",headers=creds) as resp:
           return await resp.json()

async def get_Reqs_Company_ReqNum_ReqDetails_Company_ReqNum_ReqLine(Company, ReqNum, ReqLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ReqDetail item
   Description: Calls GetByID to retrieve the ReqDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReqDetail1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReqNum: Desc: ReqNum   Required: True
      :param ReqLine: Desc: ReqLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ReqDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/Reqs(" + Company + "," + ReqNum + ")/ReqDetails(" + Company + "," + ReqNum + "," + ReqLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_Reqs_Company_ReqNum_ReqHeadAttches(Company, ReqNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ReqHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ReqHeadAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReqNum: Desc: ReqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReqHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/Reqs(" + Company + "," + ReqNum + ")/ReqHeadAttches",headers=creds) as resp:
           return await resp.json()

async def get_Reqs_Company_ReqNum_ReqHeadAttches_Company_ReqNum_DrawingSeq(Company, ReqNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ReqHeadAttch item
   Description: Calls GetByID to retrieve the ReqHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReqHeadAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReqNum: Desc: ReqNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ReqHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/Reqs(" + Company + "," + ReqNum + ")/ReqHeadAttches(" + Company + "," + ReqNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ReqDetails(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ReqDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ReqDetails
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReqDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetails",headers=creds) as resp:
           return await resp.json()

async def post_ReqDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ReqDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ReqDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ReqDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetails", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ReqDetails_Company_ReqNum_ReqLine(Company, ReqNum, ReqLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ReqDetail item
   Description: Calls GetByID to retrieve the ReqDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReqDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReqNum: Desc: ReqNum   Required: True
      :param ReqLine: Desc: ReqLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ReqDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetails(" + Company + "," + ReqNum + "," + ReqLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ReqDetails_Company_ReqNum_ReqLine(Company, ReqNum, ReqLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ReqDetail for the service
   Description: Calls UpdateExt to update ReqDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ReqDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReqNum: Desc: ReqNum   Required: True
      :param ReqLine: Desc: ReqLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ReqDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetails(" + Company + "," + ReqNum + "," + ReqLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ReqDetails_Company_ReqNum_ReqLine(Company, ReqNum, ReqLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ReqDetail item
   Description: Call UpdateExt to delete ReqDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ReqDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReqNum: Desc: ReqNum   Required: True
      :param ReqLine: Desc: ReqLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetails(" + Company + "," + ReqNum + "," + ReqLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_ReqDetails_Company_ReqNum_ReqLine_ReqDetailAttches(Company, ReqNum, ReqLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ReqDetailAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ReqDetailAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReqNum: Desc: ReqNum   Required: True
      :param ReqLine: Desc: ReqLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReqDetailAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetails(" + Company + "," + ReqNum + "," + ReqLine + ")/ReqDetailAttches",headers=creds) as resp:
           return await resp.json()

async def get_ReqDetails_Company_ReqNum_ReqLine_ReqDetailAttches_Company_ReqNum_ReqLine_DrawingSeq(Company, ReqNum, ReqLine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ReqDetailAttch item
   Description: Calls GetByID to retrieve the ReqDetailAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReqDetailAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReqNum: Desc: ReqNum   Required: True
      :param ReqLine: Desc: ReqLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ReqDetailAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetails(" + Company + "," + ReqNum + "," + ReqLine + ")/ReqDetailAttches(" + Company + "," + ReqNum + "," + ReqLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ReqDetailAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ReqDetailAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ReqDetailAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReqDetailAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetailAttches",headers=creds) as resp:
           return await resp.json()

async def post_ReqDetailAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ReqDetailAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ReqDetailAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ReqDetailAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetailAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ReqDetailAttches_Company_ReqNum_ReqLine_DrawingSeq(Company, ReqNum, ReqLine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ReqDetailAttch item
   Description: Calls GetByID to retrieve the ReqDetailAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReqDetailAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReqNum: Desc: ReqNum   Required: True
      :param ReqLine: Desc: ReqLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ReqDetailAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetailAttches(" + Company + "," + ReqNum + "," + ReqLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ReqDetailAttches_Company_ReqNum_ReqLine_DrawingSeq(Company, ReqNum, ReqLine, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ReqDetailAttch for the service
   Description: Calls UpdateExt to update ReqDetailAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ReqDetailAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReqNum: Desc: ReqNum   Required: True
      :param ReqLine: Desc: ReqLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ReqDetailAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetailAttches(" + Company + "," + ReqNum + "," + ReqLine + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ReqDetailAttches_Company_ReqNum_ReqLine_DrawingSeq(Company, ReqNum, ReqLine, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ReqDetailAttch item
   Description: Call UpdateExt to delete ReqDetailAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ReqDetailAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReqNum: Desc: ReqNum   Required: True
      :param ReqLine: Desc: ReqLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqDetailAttches(" + Company + "," + ReqNum + "," + ReqLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ReqHeadAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ReqHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ReqHeadAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReqHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqHeadAttches",headers=creds) as resp:
           return await resp.json()

async def post_ReqHeadAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ReqHeadAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ReqHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ReqHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqHeadAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ReqHeadAttches_Company_ReqNum_DrawingSeq(Company, ReqNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ReqHeadAttch item
   Description: Calls GetByID to retrieve the ReqHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReqHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReqNum: Desc: ReqNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ReqHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqHeadAttches(" + Company + "," + ReqNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ReqHeadAttches_Company_ReqNum_DrawingSeq(Company, ReqNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ReqHeadAttch for the service
   Description: Calls UpdateExt to update ReqHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ReqHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReqNum: Desc: ReqNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ReqHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqHeadAttches(" + Company + "," + ReqNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ReqHeadAttches_Company_ReqNum_DrawingSeq(Company, ReqNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ReqHeadAttch item
   Description: Call UpdateExt to delete ReqHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ReqHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReqNum: Desc: ReqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/ReqHeadAttches(" + Company + "," + ReqNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReqHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseReqHead, whereClauseReqHeadAttch, whereClauseReqDetail, whereClauseReqDetailAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseReqHead=" + whereClauseReqHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseReqHeadAttch=" + whereClauseReqHeadAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseReqDetail=" + whereClauseReqDetail
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseReqDetailAttch=" + whereClauseReqDetailAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(reqNum, epicorHeaders = None):
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
   params += "reqNum=" + reqNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_BuildNextDispatcher(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildNextDispatcher
   Description: This methods builds next Dispatcher. Returns list of user
ids and list of user names.
   OperationID: BuildNextDispatcher
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildNextDispatcher_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildNextDispatcher_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildNextDispatcher_SingleList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildNextDispatcher_SingleList
   Description: Build list of Dispatcher Ids.
   OperationID: BuildNextDispatcher_SingleList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildNextDispatcher_SingleList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildNextDispatcher_SingleList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildReqActionsList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildReqActionsList
   Description: Build list of Requisition Actions.
   OperationID: BuildReqActionsList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildReqActionsList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildReqActionsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckJobNum
   Description: This method checks to see if the proposed Job Number is a valid Job
   OperationID: CheckJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPartStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPartStatus
   Description: Perform Part Inactive, Obsolete, Runout validation.
   OperationID: CheckPartStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPartStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPartStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CloseRequisition(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CloseRequisition
   Description: This method closes Requisition.
   OperationID: CloseRequisition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseRequisition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseRequisition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteReqLog(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteReqLog
   Description: This method deletes Requisition log with given type changedate and changetime.
   OperationID: DeleteReqLog
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteReqLog_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteReqLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCostInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCostInfo
   Description: This method sets Unit Cost and Extended Cost.
   OperationID: GetCostInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCostInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCostInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetExchangeRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetExchangeRate
   Description: This method gets the Exchange Rate by the given date.
   OperationID: GetExchangeRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartCrossRef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartCrossRef
   Description: This method defaults ShipDtl fields when the PartNum field changes
   OperationID: GetPartCrossRef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartCrossRef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartCrossRef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartInfo
   Description: This method defaults ReqDetail part fields.
   OperationID: GetPartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailOverridePriceList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailOverridePriceList
   Description: Run this method when the override pricelist is unchecked
   OperationID: ChangeDetailOverridePriceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailOverridePriceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailOverridePriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeUnitPriceConfirmOverride(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeUnitPriceConfirmOverride
   Description: Checks if the source of the unit price is from a supplier price list, if so
will prompt for confirmation of overriding if flag is set against purchase configuration.
   OperationID: ChangeUnitPriceConfirmOverride
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeUnitPriceConfirmOverride_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUnitPriceConfirmOverride_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMfgNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMfgNum
   Description: Called when MfgNum is changed. Updates MfgNumName.
   OperationID: ChangeMfgNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMfgNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMfgNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMfgPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMfgPartNum
   Description: Called when MfgNumPart is changed and need to retrieve Supplier Part
   OperationID: ChangeMfgPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMfgPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMfgPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePartClass(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePartClass
   Description: Run this method when the part Class Changes.
   OperationID: ChangePartClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePartClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTranType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTranType
   Description: Run this method when the Transaction Type Changes
   OperationID: ChangeTranType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTranType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTranType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQtyInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQtyInfo
   Description: This method applies PurchasingFactor to Qties by given field
that was changed OrderQty or XOrderQty.
   OperationID: GetQtyInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQtyInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQtyInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingNumberOfPieces(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new tran qty
   OperationID: OnChangingNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingAttributeSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckReqDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckReqDetail
   Description: Validates Inactive Part Class and Checks for attribute tracked parts.
   OperationID: CheckReqDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckReqDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckReqDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckReqDetailAttributeSets(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckReqDetailAttributeSets
   Description: Checks for attribute tracked parts.
   OperationID: CheckReqDetailAttributeSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckReqDetailAttributeSets_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckReqDetailAttributeSets_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReqLogList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetReqLogList
   Description: Public method to get the ReqLog dataset.
   OperationID: GetReqLogList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReqLogList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReqLogList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetVendorInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetVendorInfo
   Description: This method update Vendor related field.
   OperationID: GetVendorInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendorInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RDMenuFlags(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RDMenuFlags
   Description: returns flags indicating whether Reset Dispatching or
Dispatch Requisiton should be enabled or disabled
   OperationID: RDMenuFlags
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RDMenuFlags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RDMenuFlags_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ResetDispatching(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ResetDispatching
   Description: This method resets Dispatching.
UI needs to ask before running method "WARNING: This will delete
all entries in the action log and delete all previous Dispatching steps.
Do you wish to continue?"
   OperationID: ResetDispatching
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetDispatching_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetDispatching_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckLine(epicorHeaders = None):
   """  
   Summary: Invoke method CheckLine
   OperationID: CheckLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_CheckToDo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckToDo
   OperationID: CheckToDo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckToDo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckToDo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendorPP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendorPP
   Description: Method to call when changing the VendorPP.
   OperationID: ChangeVendorPP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendorPP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendorPP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCurrencyCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCurrencyCode
   Description: Method to call when changing the currency on the ReqLine.  Validates the currency code and
updates ReqLine with default values based on the currency.
   OperationID: ChangeCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCostInfoExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCostInfoExt
   OperationID: GetCostInfoExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCostInfoExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCostInfoExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewReqHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewReqHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewReqHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewReqHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReqHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewReqHeadAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewReqHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewReqHeadAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewReqHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReqHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewReqDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewReqDetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewReqDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewReqDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReqDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewReqDetailAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewReqDetailAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewReqDetailAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewReqDetailAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReqDetailAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReqSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqDetailAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ReqDetailAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqDetailRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ReqDetailRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqHeadAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ReqHeadAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ReqHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReqHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ReqHeadRow] = obj["value"]
      pass

class Erp_Tablesets_ReqDetailAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ReqNum:int = obj["ReqNum"]
      self.ReqLine:int = obj["ReqLine"]
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

class Erp_Tablesets_ReqDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if this line item is Open/Closed. This is not directly maintainable by the user.  This is a mirror of ReqHead.OpenReq and is used for performance reasons.  """  
      self.ReqNum:int = obj["ReqNum"]
      """  Requisition number that the detail line is linked to.  """  
      self.ReqLine:int = obj["ReqLine"]
      """  The line number of detail record on the requisition.  This number uniquely identifies the record within the Requisition number.  The number is not directly maintainable; it's assigned by the system when records are created.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records. If no job reference then uses the Part.PartDescription if its a valid PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  Issue(Our) Unit Of Measure.  """  
      self.UnitCost:int = obj["UnitCost"]
      """   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  The unit price in the vendors unit of measure and currency.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little misleading.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Taxable  """  
      self.RUM:str = obj["RUM"]
      """  Requisition UOM  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit cost for the line item. The logic is to divide the ReqDetail.ReqQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  """  
      self.PartNum:str = obj["PartNum"]
      """  OUR internal Part number for this item.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Supplier Part Number  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the detail request line item.  Defaults  from the related JobOper, JobMtl or Part file.  """  
      self.Class:str = obj["Class"]
      """  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.Class. The PartClass is used in determining a default G/L expense account. Updated indirectly via a DDSL widget in.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required when this requested line item is received. Inspection may also be enforced if the related PartClass, Vendor, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The VendorNum that ties back to the Vendor master file.  This field is a duplicate of the field in ReqHeader and is maintained  in the write triggers of POHeader and PODetail.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Ties the Requisition line back to the VendPP master file. This can be blank indicating No purchase point.  """  
      self.PurchasingFactor:int = obj["PurchasingFactor"]
      """   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Visa-Versa.
Formula: XRelQty * Factor = RelQty  """  
      self.DueDate:str = obj["DueDate"]
      """  Use the last date entered during the session for the Purchase order as a default.  """  
      self.PONUM:int = obj["PONUM"]
      """  Purchase order number  that the detail line item is linked to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PODetail record that the detail line item is related to.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the VendCnt  table. Use the Vendor.PRIMPCON as the default. or the VendorPP.PrimPCon if a vendor purchase point is referenced.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.ReqDate:str = obj["ReqDate"]
      """  Requisition Date for this requisition line. Initially defaults as "today".  """  
      self.OrderQty:int = obj["OrderQty"]
      """  Total Order Quantity for the line item.  This is stored in the Vendors Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the OrderQty is not maintainable. As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This ensures that Order quantity and scheduled  quantities are always in sync.  """  
      self.XOrderQty:int = obj["XOrderQty"]
      """  Total Order Quantity for the line item.  This is stored in Our  Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the XOrderQty is not maintainable. As the user modifies the quantities in the individual release lines the XOrderQty field will get adjusted. This ensures that Order quantity and scheduled  quantities are always in sync.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Qualifies the JobSeq field as to be a "M" - Material (JobMtl) record, "S" - Subcontract (JobOper) reference or "O" - Other.
FYI: This field can indirectly sets the TranType field via the write trigger. It can itself be set from the TranType. System keeps them compatible. JobSeqType/TranType values are; M = PUR-MTL,  S = PUR-SUB, "O " = PUR-UKN. This possibly could have been deleted. However we decided to keep it for backward compatablity reasons.  """  
      self.TranType:str = obj["TranType"]
      """  Indicates what the item is being requested for. Items can be requested for Job Material ("PUR-MTL"), Inventory ("PUR-STK"), or Other ("PUR-UKN"). FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are: M = PUR-MTL, O = PUR-STK, O = PUR-UKN.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbReqNum:int = obj["GlbReqNum"]
      """  Global Requisition identifier.  Used in Consolidated Purchasing.  """  
      self.GlbReqLine:int = obj["GlbReqLine"]
      """  Global Requisition Line identifier.  Used in Consolidated Purchasing.  """  
      self.PurchasingFactorDirection:str = obj["PurchasingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.Rpt1UnitCost:int = obj["Rpt1UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitCost:int = obj["Rpt2UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitCost:int = obj["Rpt3UnitCost"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.MfgNum:int = obj["MfgNum"]
      """  MfgNum  """  
      self.MfgPartNum:str = obj["MfgPartNum"]
      """  MfgPartNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the supplier price list has been overriden which will in turn prevent the unit price from being updated when taking into account quantity / price breaks.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.NumberOfPiecesUOM:str = obj["NumberOfPiecesUOM"]
      """  Unit of measure for the NumberOfPieces.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DocExtCost:int = obj["DocExtCost"]
      self.EnableRcvInspectionReq:bool = obj["EnableRcvInspectionReq"]
      """  Use Vendor / Class / Qualified Manufacturer / Inspection Plans to determine whether inspection required is enabled / disabled.  """  
      self.ExtCost:int = obj["ExtCost"]
      """  Extended Cost  """  
      self.IsNonMasterPart:bool = obj["IsNonMasterPart"]
      """  Flag to indicate if part is non master part  """  
      self.LeadTime:int = obj["LeadTime"]
      self.MinOrderQty:int = obj["MinOrderQty"]
      self.PartPUM:str = obj["PartPUM"]
      """  Part.PUM  """  
      self.PartQtyBearing:bool = obj["PartQtyBearing"]
      """  Set based on PartPlant.QtyBearing.  This flag is used in a row rule to disable the Transaction Type when the flag is false.  """  
      self.PostInvtyWipCos:bool = obj["PostInvtyWipCos"]
      self.Rpt1ExtCost:int = obj["Rpt1ExtCost"]
      self.Rpt2ExtCost:int = obj["Rpt2ExtCost"]
      self.Rpt3ExtCost:int = obj["Rpt3ExtCost"]
      self.UOMOverrideSPL:bool = obj["UOMOverrideSPL"]
      """  True when there is a UOM override from the Supplier Price List active for line  """  
      self.VendorID:str = obj["VendorID"]
      self.VendorInactive:bool = obj["VendorInactive"]
      """  Vendor.Inactive  """  
      self.VendorName:str = obj["VendorName"]
      self.VendorPayHold:bool = obj["VendorPayHold"]
      """  Vendor.PayHold  """  
      self.BaseDisplaySymbol:str = obj["BaseDisplaySymbol"]
      """  Currency.CurrSymbol for BASE currency Code  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ClassDescription:str = obj["ClassDescription"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.MfgNumMfgID:str = obj["MfgNumMfgID"]
      self.MfgNumName:str = obj["MfgNumName"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.PONUMShipToConName:str = obj["PONUMShipToConName"]
      self.PONUMShipName:str = obj["PONUMShipName"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.ReqNumShipToConName:str = obj["ReqNumShipToConName"]
      self.ReqNumShipName:str = obj["ReqNumShipName"]
      self.vrClassDescription:str = obj["vrClassDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReqHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ReqNum:int = obj["ReqNum"]
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

class Erp_Tablesets_ReqHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenReq:bool = obj["OpenReq"]
      """  Indicates if the requisition is open or closed.  This is set automatically when all the ReqDetail records have been closed or can be set if the user Voids the Requisition.  This field is not directly maintainable.  """  
      self.ReqNum:int = obj["ReqNum"]
      """  Requisition number that uniquely identifies the requisition.  """  
      self.RequestorID:str = obj["RequestorID"]
      """  The ID of the Original Requestor that links to the User master file.  """  
      self.RequestDate:str = obj["RequestDate"]
      """  Request date for the requisition.  Initially defaults as "today", then defaults as last date entered in this session.  """  
      self.ReqActionID:str = obj["ReqActionID"]
      """  Requisition Log Table  """  
      self.CurrDispatcherID:str = obj["CurrDispatcherID"]
      """  Requisition Action ID  """  
      self.StatusType:str = obj["StatusType"]
      """  "A" - Approve, "O" - Ordered, "P" - Pending, "R" - Reject, "C" - Closed, "" - for Notifications (No status).  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.StatusDesc:str = obj["StatusDesc"]
      """  StatusType Description  """  
      self.RequestorIDCurMenuID:str = obj["RequestorIDCurMenuID"]
      self.CurrDispatcherCurMenuID:str = obj["CurrDispatcherCurMenuID"]
      self.CurrDispatcherName:str = obj["CurrDispatcherName"]
      self.ReqActionIDReqActionDesc:str = obj["ReqActionIDReqActionDesc"]
      self.RequestorIDName:str = obj["RequestorIDName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReqHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenReq:bool = obj["OpenReq"]
      """  Indicates if the requisition is open or closed.  This is set automatically when all the ReqDetail records have been closed or can be set if the user Voids the Requisition.  This field is not directly maintainable.  """  
      self.ReqNum:int = obj["ReqNum"]
      """  Requisition number that uniquely identifies the requisition.  """  
      self.RequestorID:str = obj["RequestorID"]
      """  The ID of the Original Requestor that links to the User master file.  """  
      self.RequestDate:str = obj["RequestDate"]
      """  Request date for the requisition.  Initially defaults as "today", then defaults as last date entered in this session.  """  
      self.ShipName:str = obj["ShipName"]
      """  defaults from the company file.  """  
      self.ShipAddress1:str = obj["ShipAddress1"]
      """  First adress line  """  
      self.ShipAddress2:str = obj["ShipAddress2"]
      """  Second address line  """  
      self.ShipAddress3:str = obj["ShipAddress3"]
      """  Third address line  """  
      self.ShipCity:str = obj["ShipCity"]
      """  City portion of the address  """  
      self.ShipState:str = obj["ShipState"]
      """  Statee portion of the address  """  
      self.ShipZIP:str = obj["ShipZIP"]
      """  Postal code or Zip code portion of the address  """  
      self.ShipCountry:str = obj["ShipCountry"]
      """  Country is used as part of the Ship to  address. It can be left blank.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the VendCnt  table. Use the Vendor.PRIMPCON as the default. or the VendorPP.PrimPCon if a vendor purchase point is referenced.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about over all requisition.  """  
      self.ShipToConName:str = obj["ShipToConName"]
      """  Ship to contact name.  """  
      self.ShipCountryNum:int = obj["ShipCountryNum"]
      """  Country part of address. This field is in sync with the Country field. Must be a valid entry in the Country table.  """  
      self.ReqActionID:str = obj["ReqActionID"]
      """  Requisition Log Table  """  
      self.CurrDispatcherID:str = obj["CurrDispatcherID"]
      """  Requisition Action ID  """  
      self.NotifyUponReceipt:bool = obj["NotifyUponReceipt"]
      """  Notify upon Receipt flag  """  
      self.Note:str = obj["Note"]
      """  Notes associated with the requisition action log.  """  
      self.StatusType:str = obj["StatusType"]
      """  "A" - Approve, "O" - Ordered, "P" - Pending, "R" - Reject, "C" - Closed, "" - for Notifications (No status).  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbReqNum:int = obj["GlbReqNum"]
      """  Global Requisition identifier.  Used in Consolidated Purchasing.  """  
      self.CPDispatcherID:str = obj["CPDispatcherID"]
      """  Used in Consolidated Purchasing  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.AddrList:str = obj["AddrList"]
      self.CurrDispatcherCurMenuID:str = obj["CurrDispatcherCurMenuID"]
      self.LockLines:bool = obj["LockLines"]
      self.MemoAvailable:bool = obj["MemoAvailable"]
      self.NextActionDesc:str = obj["NextActionDesc"]
      """  Description of NextActionID  """  
      self.NextActionID:str = obj["NextActionID"]
      self.NextDispatcherID:str = obj["NextDispatcherID"]
      self.NextDispatcherName:str = obj["NextDispatcherName"]
      self.NextNote:str = obj["NextNote"]
      self.OkToBuy:bool = obj["OkToBuy"]
      self.ReplyOption:str = obj["ReplyOption"]
      """  "A", "R" or "F"  """  
      self.RequestorIDCurMenuID:str = obj["RequestorIDCurMenuID"]
      self.ReqUserId:str = obj["ReqUserId"]
      """  The current ReqUserId (not same as dcduserid)  """  
      self.StatusDesc:str = obj["StatusDesc"]
      """  StatusType Description  """  
      self.ToDoFlag:bool = obj["ToDoFlag"]
      """  Indicates Requests to manage for current user  """  
      self.ShipToAddressFormatted:str = obj["ShipToAddressFormatted"]
      """  Formatted ship to address used in Kinetic UI.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrDispatcherName:str = obj["CurrDispatcherName"]
      self.ReqActionIDReqActionDesc:str = obj["ReqActionIDReqActionDesc"]
      self.RequestorIDName:str = obj["RequestorIDName"]
      self.XbSystDisableOverridePriceListOption:bool = obj["XbSystDisableOverridePriceListOption"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.ProjectID_c:str = obj["ProjectID_c"]
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class BuildNextDispatcher_SingleList_input:
   """ Required : 
   nextActionID
   """  
   def __init__(self, obj):
      self.nextActionID:str = obj["nextActionID"]
      pass

class BuildNextDispatcher_SingleList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class BuildNextDispatcher_input:
   """ Required : 
   nextActionID
   """  
   def __init__(self, obj):
      self.nextActionID:str = obj["nextActionID"]
      """  The next action ID  """  
      pass

class BuildNextDispatcher_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.dispIDList:str = obj["parameters"]
      self.dispNmList:str = obj["parameters"]
      pass

      """  output parameters  """  

class BuildReqActionsList_input:
   """ Required : 
   replyOpt
   includeSendToPMCond
   """  
   def __init__(self, obj):
      self.replyOpt:str = obj["replyOpt"]
      self.includeSendToPMCond:bool = obj["includeSendToPMCond"]
      pass

class BuildReqActionsList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ChangeCurrencyCode_input:
   """ Required : 
   proposedCurrencyCode
   ds
   """  
   def __init__(self, obj):
      self.proposedCurrencyCode:str = obj["proposedCurrencyCode"]
      """  The proposed currency code  """  
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

class ChangeCurrencyCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailOverridePriceList_input:
   """ Required : 
   overridePriceList
   ds
   """  
   def __init__(self, obj):
      self.overridePriceList:bool = obj["overridePriceList"]
      """  True is override pricelist has been checked  """  
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

class ChangeDetailOverridePriceList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMfgNum_input:
   """ Required : 
   ipMfgNum
   ds
   """  
   def __init__(self, obj):
      self.ipMfgNum:int = obj["ipMfgNum"]
      """  Manufacturer Number  """  
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

class ChangeMfgNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMfgPartNum_input:
   """ Required : 
   ipMfgPartNum
   ds
   """  
   def __init__(self, obj):
      self.ipMfgPartNum:str = obj["ipMfgPartNum"]
      """  Manufacturer Number  """  
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

class ChangeMfgPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePartClass_input:
   """ Required : 
   ipClassID
   ds
   """  
   def __init__(self, obj):
      self.ipClassID:str = obj["ipClassID"]
      """  New Class ID  """  
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

class ChangePartClass_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTranType_input:
   """ Required : 
   ipTranType
   ds
   """  
   def __init__(self, obj):
      self.ipTranType:str = obj["ipTranType"]
      """  New TranType  """  
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

class ChangeTranType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeUnitPriceConfirmOverride_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

class ChangeUnitPriceConfirmOverride_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      self.sConfirmMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeVendorPP_input:
   """ Required : 
   proposedPurPoint
   ds
   """  
   def __init__(self, obj):
      self.proposedPurPoint:str = obj["proposedPurPoint"]
      """  The proposed Vendor Purchase Point  """  
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

class ChangeVendorPP_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckJobNum_input:
   """ Required : 
   jobNum
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      """  The proposed Job Number  """  
      pass

class CheckJobNum_output:
   def __init__(self, obj):
      pass

class CheckLine_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class CheckPartStatus_input:
   """ Required : 
   partNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number to be validated  """  
      pass

class CheckPartStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.vMessage:str = obj["parameters"]
      self.vSubAvail:bool = obj["vSubAvail"]
      self.vMsgType:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckReqDetailAttributeSets_input:
   """ Required : 
   reqNum
   """  
   def __init__(self, obj):
      self.reqNum:int = obj["reqNum"]
      pass

class CheckReqDetailAttributeSets_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckReqDetail_input:
   """ Required : 
   reqNum
   """  
   def __init__(self, obj):
      self.reqNum:int = obj["reqNum"]
      pass

class CheckReqDetail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckToDo_input:
   """ Required : 
   dispatchId
   """  
   def __init__(self, obj):
      self.dispatchId:str = obj["dispatchId"]
      pass

class CheckToDo_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class CloseRequisition_input:
   """ Required : 
   reqNum
   reqUserId
   """  
   def __init__(self, obj):
      self.reqNum:int = obj["reqNum"]
      """  The number of Requisition to close  """  
      self.reqUserId:str = obj["reqUserId"]
      """  The ID of user  """  
      pass

class CloseRequisition_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReqTableset] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   reqNum
   """  
   def __init__(self, obj):
      self.reqNum:int = obj["reqNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteReqLog_input:
   """ Required : 
   reqNum
   changeDate
   changeTime
   reqLogType
   """  
   def __init__(self, obj):
      self.reqNum:int = obj["reqNum"]
      """  The number of Requisition  """  
      self.changeDate:str = obj["changeDate"]
      """  The ChangeDate of log to delete  """  
      self.changeTime:int = obj["changeTime"]
      """  The ChangeTime of log to delete  """  
      self.reqLogType:str = obj["reqLogType"]
      """  The LogType of log to delete  """  
      pass

class DeleteReqLog_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ReqDetailAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ReqNum:int = obj["ReqNum"]
      self.ReqLine:int = obj["ReqLine"]
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

class Erp_Tablesets_ReqDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if this line item is Open/Closed. This is not directly maintainable by the user.  This is a mirror of ReqHead.OpenReq and is used for performance reasons.  """  
      self.ReqNum:int = obj["ReqNum"]
      """  Requisition number that the detail line is linked to.  """  
      self.ReqLine:int = obj["ReqLine"]
      """  The line number of detail record on the requisition.  This number uniquely identifies the record within the Requisition number.  The number is not directly maintainable; it's assigned by the system when records are created.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records. If no job reference then uses the Part.PartDescription if its a valid PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  Issue(Our) Unit Of Measure.  """  
      self.UnitCost:int = obj["UnitCost"]
      """   The unit price in the vendors unit of measure.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little
misleading  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  The unit price in the vendors unit of measure and currency.  Unfortunately the Field Name is UnitCost instead of UnitPrice which is a little misleading.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Taxable  """  
      self.RUM:str = obj["RUM"]
      """  Requisition UOM  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """   Indicates the costing per quantity. It can be "E" = per each,
"C" = per hundred,  "M" = per thousand. Used to calculate the extended unit cost for the line item. The logic is to divide the ReqDetail.ReqQty by the appropriate "per" value and then multiply by unit cost.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  """  
      self.PartNum:str = obj["PartNum"]
      """  OUR internal Part number for this item.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Supplier Part Number  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the detail request line item.  Defaults  from the related JobOper, JobMtl or Part file.  """  
      self.Class:str = obj["Class"]
      """  The foreign key to the PartClass Master. May be blank, if entered must be valid in PartClass file.  Defaulted from Part.Class. The PartClass is used in determining a default G/L expense account. Updated indirectly via a DDSL widget in.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  OUR revision number of the OUR part.  An optional field. Defaults from the most current  PartRev.RevisionNum.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required when this requested line item is received. Inspection may also be enforced if the related PartClass, Vendor, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The VendorNum that ties back to the Vendor master file.  This field is a duplicate of the field in ReqHeader and is maintained  in the write triggers of POHeader and PODetail.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Ties the Requisition line back to the VendPP master file. This can be blank indicating No purchase point.  """  
      self.PurchasingFactor:int = obj["PurchasingFactor"]
      """   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Visa-Versa.
Formula: XRelQty * Factor = RelQty  """  
      self.DueDate:str = obj["DueDate"]
      """  Use the last date entered during the session for the Purchase order as a default.  """  
      self.PONUM:int = obj["PONUM"]
      """  Purchase order number  that the detail line item is linked to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PODetail record that the detail line item is related to.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the VendCnt  table. Use the Vendor.PRIMPCON as the default. or the VendorPP.PrimPCon if a vendor purchase point is referenced.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.ReqDate:str = obj["ReqDate"]
      """  Requisition Date for this requisition line. Initially defaults as "today".  """  
      self.OrderQty:int = obj["OrderQty"]
      """  Total Order Quantity for the line item.  This is stored in the Vendors Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the OrderQty is not maintainable. As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This ensures that Order quantity and scheduled  quantities are always in sync.  """  
      self.XOrderQty:int = obj["XOrderQty"]
      """  Total Order Quantity for the line item.  This is stored in Our  Unit of Measure. This quantity must always be kept in sync with the scheduled release quantities stored in the PORel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line (more than one PORel record) the XOrderQty is not maintainable. As the user modifies the quantities in the individual release lines the XOrderQty field will get adjusted. This ensures that Order quantity and scheduled  quantities are always in sync.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Qualifies the JobSeq field as to be a "M" - Material (JobMtl) record, "S" - Subcontract (JobOper) reference or "O" - Other.
FYI: This field can indirectly sets the TranType field via the write trigger. It can itself be set from the TranType. System keeps them compatible. JobSeqType/TranType values are; M = PUR-MTL,  S = PUR-SUB, "O " = PUR-UKN. This possibly could have been deleted. However we decided to keep it for backward compatablity reasons.  """  
      self.TranType:str = obj["TranType"]
      """  Indicates what the item is being requested for. Items can be requested for Job Material ("PUR-MTL"), Inventory ("PUR-STK"), or Other ("PUR-UKN"). FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are: M = PUR-MTL, O = PUR-STK, O = PUR-UKN.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbReqNum:int = obj["GlbReqNum"]
      """  Global Requisition identifier.  Used in Consolidated Purchasing.  """  
      self.GlbReqLine:int = obj["GlbReqLine"]
      """  Global Requisition Line identifier.  Used in Consolidated Purchasing.  """  
      self.PurchasingFactorDirection:str = obj["PurchasingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.Rpt1UnitCost:int = obj["Rpt1UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitCost:int = obj["Rpt2UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitCost:int = obj["Rpt3UnitCost"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.MfgNum:int = obj["MfgNum"]
      """  MfgNum  """  
      self.MfgPartNum:str = obj["MfgPartNum"]
      """  MfgPartNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OverridePriceList:bool = obj["OverridePriceList"]
      """  Indicates if the supplier price list has been overriden which will in turn prevent the unit price from being updated when taking into account quantity / price breaks.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.NumberOfPiecesUOM:str = obj["NumberOfPiecesUOM"]
      """  Unit of measure for the NumberOfPieces.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DocExtCost:int = obj["DocExtCost"]
      self.EnableRcvInspectionReq:bool = obj["EnableRcvInspectionReq"]
      """  Use Vendor / Class / Qualified Manufacturer / Inspection Plans to determine whether inspection required is enabled / disabled.  """  
      self.ExtCost:int = obj["ExtCost"]
      """  Extended Cost  """  
      self.IsNonMasterPart:bool = obj["IsNonMasterPart"]
      """  Flag to indicate if part is non master part  """  
      self.LeadTime:int = obj["LeadTime"]
      self.MinOrderQty:int = obj["MinOrderQty"]
      self.PartPUM:str = obj["PartPUM"]
      """  Part.PUM  """  
      self.PartQtyBearing:bool = obj["PartQtyBearing"]
      """  Set based on PartPlant.QtyBearing.  This flag is used in a row rule to disable the Transaction Type when the flag is false.  """  
      self.PostInvtyWipCos:bool = obj["PostInvtyWipCos"]
      self.Rpt1ExtCost:int = obj["Rpt1ExtCost"]
      self.Rpt2ExtCost:int = obj["Rpt2ExtCost"]
      self.Rpt3ExtCost:int = obj["Rpt3ExtCost"]
      self.UOMOverrideSPL:bool = obj["UOMOverrideSPL"]
      """  True when there is a UOM override from the Supplier Price List active for line  """  
      self.VendorID:str = obj["VendorID"]
      self.VendorInactive:bool = obj["VendorInactive"]
      """  Vendor.Inactive  """  
      self.VendorName:str = obj["VendorName"]
      self.VendorPayHold:bool = obj["VendorPayHold"]
      """  Vendor.PayHold  """  
      self.BaseDisplaySymbol:str = obj["BaseDisplaySymbol"]
      """  Currency.CurrSymbol for BASE currency Code  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ClassDescription:str = obj["ClassDescription"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.MfgNumMfgID:str = obj["MfgNumMfgID"]
      self.MfgNumName:str = obj["MfgNumName"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.PONUMShipToConName:str = obj["PONUMShipToConName"]
      self.PONUMShipName:str = obj["PONUMShipName"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.ReqNumShipToConName:str = obj["ReqNumShipToConName"]
      self.ReqNumShipName:str = obj["ReqNumShipName"]
      self.vrClassDescription:str = obj["vrClassDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReqHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ReqNum:int = obj["ReqNum"]
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

class Erp_Tablesets_ReqHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenReq:bool = obj["OpenReq"]
      """  Indicates if the requisition is open or closed.  This is set automatically when all the ReqDetail records have been closed or can be set if the user Voids the Requisition.  This field is not directly maintainable.  """  
      self.ReqNum:int = obj["ReqNum"]
      """  Requisition number that uniquely identifies the requisition.  """  
      self.RequestorID:str = obj["RequestorID"]
      """  The ID of the Original Requestor that links to the User master file.  """  
      self.RequestDate:str = obj["RequestDate"]
      """  Request date for the requisition.  Initially defaults as "today", then defaults as last date entered in this session.  """  
      self.ReqActionID:str = obj["ReqActionID"]
      """  Requisition Log Table  """  
      self.CurrDispatcherID:str = obj["CurrDispatcherID"]
      """  Requisition Action ID  """  
      self.StatusType:str = obj["StatusType"]
      """  "A" - Approve, "O" - Ordered, "P" - Pending, "R" - Reject, "C" - Closed, "" - for Notifications (No status).  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.StatusDesc:str = obj["StatusDesc"]
      """  StatusType Description  """  
      self.RequestorIDCurMenuID:str = obj["RequestorIDCurMenuID"]
      self.CurrDispatcherCurMenuID:str = obj["CurrDispatcherCurMenuID"]
      self.CurrDispatcherName:str = obj["CurrDispatcherName"]
      self.ReqActionIDReqActionDesc:str = obj["ReqActionIDReqActionDesc"]
      self.RequestorIDName:str = obj["RequestorIDName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReqHeadListTableset:
   def __init__(self, obj):
      self.ReqHeadList:list[Erp_Tablesets_ReqHeadListRow] = obj["ReqHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ReqHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenReq:bool = obj["OpenReq"]
      """  Indicates if the requisition is open or closed.  This is set automatically when all the ReqDetail records have been closed or can be set if the user Voids the Requisition.  This field is not directly maintainable.  """  
      self.ReqNum:int = obj["ReqNum"]
      """  Requisition number that uniquely identifies the requisition.  """  
      self.RequestorID:str = obj["RequestorID"]
      """  The ID of the Original Requestor that links to the User master file.  """  
      self.RequestDate:str = obj["RequestDate"]
      """  Request date for the requisition.  Initially defaults as "today", then defaults as last date entered in this session.  """  
      self.ShipName:str = obj["ShipName"]
      """  defaults from the company file.  """  
      self.ShipAddress1:str = obj["ShipAddress1"]
      """  First adress line  """  
      self.ShipAddress2:str = obj["ShipAddress2"]
      """  Second address line  """  
      self.ShipAddress3:str = obj["ShipAddress3"]
      """  Third address line  """  
      self.ShipCity:str = obj["ShipCity"]
      """  City portion of the address  """  
      self.ShipState:str = obj["ShipState"]
      """  Statee portion of the address  """  
      self.ShipZIP:str = obj["ShipZIP"]
      """  Postal code or Zip code portion of the address  """  
      self.ShipCountry:str = obj["ShipCountry"]
      """  Country is used as part of the Ship to  address. It can be left blank.  """  
      self.PrcConNum:int = obj["PrcConNum"]
      """  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the VendCnt  table. Use the Vendor.PRIMPCON as the default. or the VendorPP.PrimPCon if a vendor purchase point is referenced.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about over all requisition.  """  
      self.ShipToConName:str = obj["ShipToConName"]
      """  Ship to contact name.  """  
      self.ShipCountryNum:int = obj["ShipCountryNum"]
      """  Country part of address. This field is in sync with the Country field. Must be a valid entry in the Country table.  """  
      self.ReqActionID:str = obj["ReqActionID"]
      """  Requisition Log Table  """  
      self.CurrDispatcherID:str = obj["CurrDispatcherID"]
      """  Requisition Action ID  """  
      self.NotifyUponReceipt:bool = obj["NotifyUponReceipt"]
      """  Notify upon Receipt flag  """  
      self.Note:str = obj["Note"]
      """  Notes associated with the requisition action log.  """  
      self.StatusType:str = obj["StatusType"]
      """  "A" - Approve, "O" - Ordered, "P" - Pending, "R" - Reject, "C" - Closed, "" - for Notifications (No status).  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbReqNum:int = obj["GlbReqNum"]
      """  Global Requisition identifier.  Used in Consolidated Purchasing.  """  
      self.CPDispatcherID:str = obj["CPDispatcherID"]
      """  Used in Consolidated Purchasing  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.AddrList:str = obj["AddrList"]
      self.CurrDispatcherCurMenuID:str = obj["CurrDispatcherCurMenuID"]
      self.LockLines:bool = obj["LockLines"]
      self.MemoAvailable:bool = obj["MemoAvailable"]
      self.NextActionDesc:str = obj["NextActionDesc"]
      """  Description of NextActionID  """  
      self.NextActionID:str = obj["NextActionID"]
      self.NextDispatcherID:str = obj["NextDispatcherID"]
      self.NextDispatcherName:str = obj["NextDispatcherName"]
      self.NextNote:str = obj["NextNote"]
      self.OkToBuy:bool = obj["OkToBuy"]
      self.ReplyOption:str = obj["ReplyOption"]
      """  "A", "R" or "F"  """  
      self.RequestorIDCurMenuID:str = obj["RequestorIDCurMenuID"]
      self.ReqUserId:str = obj["ReqUserId"]
      """  The current ReqUserId (not same as dcduserid)  """  
      self.StatusDesc:str = obj["StatusDesc"]
      """  StatusType Description  """  
      self.ToDoFlag:bool = obj["ToDoFlag"]
      """  Indicates Requests to manage for current user  """  
      self.ShipToAddressFormatted:str = obj["ShipToAddressFormatted"]
      """  Formatted ship to address used in Kinetic UI.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrDispatcherName:str = obj["CurrDispatcherName"]
      self.ReqActionIDReqActionDesc:str = obj["ReqActionIDReqActionDesc"]
      self.RequestorIDName:str = obj["RequestorIDName"]
      self.XbSystDisableOverridePriceListOption:bool = obj["XbSystDisableOverridePriceListOption"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.ProjectID_c:str = obj["ProjectID_c"]
      pass

class Erp_Tablesets_ReqLogRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReqNum:int = obj["ReqNum"]
      """  Requisition number that uniquely identifies the requisition.  """  
      self.ReqActionID:str = obj["ReqActionID"]
      """  Requisition Action ID  """  
      self.CurrDispatcherID:str = obj["CurrDispatcherID"]
      """  Current Dispatcher  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  UserID who made the changes.  Not maintainable by the user.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  System date when this change was made.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  System time (seconds since midnight) of when the changes were made.  """  
      self.Approved:bool = obj["Approved"]
      """   This filed is ONLY used for a Mandatory Requisition Action.
If a Requisition Action is tagged as Mandatory and this action is not yet in the log for a given requisition OR the last occurrence of this action has Approved equal to NO then this Requisition cannot be sent to Purchase Management.  """  
      self.OldActionID:str = obj["OldActionID"]
      """  Old Action ID  """  
      self.ReqLogType:str = obj["ReqLogType"]
      """  "A" Action, "N" Notify  """  
      self.CurrentAction:bool = obj["CurrentAction"]
      """  Current Action  """  
      self.StatusType:str = obj["StatusType"]
      """  "A" - Approve, "O" - Ordered, "P" - Pending, "R" - Reject, "C" - Closed, "" - for Notifications (No status).  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReqActionDesc:str = obj["ReqActionDesc"]
      self.ReqHeadNote:str = obj["ReqHeadNote"]
      """  ReqHead.Note  """  
      self.StatusDesc:str = obj["StatusDesc"]
      """  description of StatusType field  """  
      self.DispChgTime:str = obj["DispChgTime"]
      """  Change Time is display format HH:MM PM  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ChangedByName:str = obj["ChangedByName"]
      self.CurrDispatcherName:str = obj["CurrDispatcherName"]
      self.ReqActionIDReqActionDesc:str = obj["ReqActionIDReqActionDesc"]
      self.ReqNumShipToConName:str = obj["ReqNumShipToConName"]
      self.ReqNumShipName:str = obj["ReqNumShipName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReqLogTableset:
   def __init__(self, obj):
      self.ReqLog:list[Erp_Tablesets_ReqLogRow] = obj["ReqLog"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ReqTableset:
   def __init__(self, obj):
      self.ReqHead:list[Erp_Tablesets_ReqHeadRow] = obj["ReqHead"]
      self.ReqHeadAttch:list[Erp_Tablesets_ReqHeadAttchRow] = obj["ReqHeadAttch"]
      self.ReqDetail:list[Erp_Tablesets_ReqDetailRow] = obj["ReqDetail"]
      self.ReqDetailAttch:list[Erp_Tablesets_ReqDetailAttchRow] = obj["ReqDetailAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtReqTableset:
   def __init__(self, obj):
      self.ReqHead:list[Erp_Tablesets_ReqHeadRow] = obj["ReqHead"]
      self.ReqHeadAttch:list[Erp_Tablesets_ReqHeadAttchRow] = obj["ReqHeadAttch"]
      self.ReqDetail:list[Erp_Tablesets_ReqDetailRow] = obj["ReqDetail"]
      self.ReqDetailAttch:list[Erp_Tablesets_ReqDetailAttchRow] = obj["ReqDetailAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   reqNum
   """  
   def __init__(self, obj):
      self.reqNum:int = obj["reqNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReqTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ReqTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ReqTableset] = obj["returnObj"]
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

class GetCostInfoExt_input:
   """ Required : 
   proposedValue
   ds
   """  
   def __init__(self, obj):
      self.proposedValue:int = obj["proposedValue"]
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

class GetCostInfoExt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetCostInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

class GetCostInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetExchangeRate_input:
   """ Required : 
   ds
   reqDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      self.reqDate:str = obj["reqDate"]
      """  The last date a rate is valid  """  
      pass

class GetExchangeRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
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
      self.returnObj:list[Erp_Tablesets_ReqHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewReqDetailAttch_input:
   """ Required : 
   ds
   reqNum
   reqLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      self.reqNum:int = obj["reqNum"]
      self.reqLine:int = obj["reqLine"]
      pass

class GetNewReqDetailAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewReqDetail_input:
   """ Required : 
   ds
   reqNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      self.reqNum:int = obj["reqNum"]
      pass

class GetNewReqDetail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewReqHeadAttch_input:
   """ Required : 
   ds
   reqNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      self.reqNum:int = obj["reqNum"]
      pass

class GetNewReqHeadAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewReqHead_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

class GetNewReqHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPartCrossRef_input:
   """ Required : 
   ds
   reqLine
   partNum
   uomCode
   SysRowID
   rowType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      self.reqLine:int = obj["reqLine"]
      """  Detail Line Number to update  """  
      self.partNum:str = obj["partNum"]
      """  Proposed PartNumber change  """  
      self.uomCode:str = obj["uomCode"]
      """  Proposed UOM Code  """  
      self.SysRowID:str = obj["SysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      pass

class GetPartCrossRef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      self.partNum:str = obj["parameters"]
      self.uomCode:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class GetPartInfo_input:
   """ Required : 
   ds
   uomCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      self.uomCode:str = obj["uomCode"]
      """  Proposed Part Cross Reference UOM Code  """  
      pass

class GetPartInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetQtyInfo_input:
   """ Required : 
   ds
   fieldName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      self.fieldName:str = obj["fieldName"]
      """  Indicates field that was changed. Possible values OrderQty or XOrderQty  """  
      pass

class GetQtyInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetReqLogList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The where clause to restrict data for  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size, used only for UI adaptor  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page, used only for the UI adaptor  """  
      pass

class GetReqLogList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReqLogTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseReqHead
   whereClauseReqHeadAttch
   whereClauseReqDetail
   whereClauseReqDetailAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseReqHead:str = obj["whereClauseReqHead"]
      self.whereClauseReqHeadAttch:str = obj["whereClauseReqHeadAttch"]
      self.whereClauseReqDetail:str = obj["whereClauseReqDetail"]
      self.whereClauseReqDetailAttch:str = obj["whereClauseReqDetailAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReqTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetVendorInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

class GetVendorInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
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

class OnChangingAttributeSet_input:
   """ Required : 
   attributeSetID
   ds
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

class OnChangingAttributeSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingNumberOfPieces_input:
   """ Required : 
   numberOfPieces
   ds
   """  
   def __init__(self, obj):
      self.numberOfPieces:int = obj["numberOfPieces"]
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

class OnChangingNumberOfPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

class OnChangingRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RDMenuFlags_input:
   """ Required : 
   reqNum
   reqUserId
   """  
   def __init__(self, obj):
      self.reqNum:int = obj["reqNum"]
      """  The number of Requisition to close  """  
      self.reqUserId:str = obj["reqUserId"]
      """  The ID of user  """  
      pass

class RDMenuFlags_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.resetDispatch:bool = obj["resetDispatch"]
      self.dispatchReq:bool = obj["dispatchReq"]
      pass

      """  output parameters  """  

class ResetDispatching_input:
   """ Required : 
   reqNum
   reqUserId
   """  
   def __init__(self, obj):
      self.reqNum:int = obj["reqNum"]
      """  The number of Requisition  """  
      self.reqUserId:str = obj["reqUserId"]
      """  The user ID  """  
      pass

class ResetDispatching_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReqTableset] = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtReqTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtReqTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReqTableset] = obj["ds"]
      pass

      """  output parameters  """  

