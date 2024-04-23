import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.BOLSvc
# Description: Bill of Lading Entry
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_BOLs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BOLs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BOLs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BOLHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLs",headers=creds) as resp:
           return await resp.json()

async def post_BOLs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BOLs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BOLHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BOLHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BOLs_Company_BOLNum(Company, BOLNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BOL item
   Description: Calls GetByID to retrieve the BOL item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BOL
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BOLNum: Desc: BOLNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BOLHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLs(" + Company + "," + BOLNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BOLs_Company_BOLNum(Company, BOLNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BOL for the service
   Description: Calls UpdateExt to update BOL. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BOL
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BOLNum: Desc: BOLNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BOLHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLs(" + Company + "," + BOLNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BOLs_Company_BOLNum(Company, BOLNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BOL item
   Description: Call UpdateExt to delete BOL item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BOL
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BOLNum: Desc: BOLNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLs(" + Company + "," + BOLNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_BOLs_Company_BOLNum_BOLDetails(Company, BOLNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BOLDetails items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BOLDetails1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BOLNum: Desc: BOLNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BOLDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLs(" + Company + "," + BOLNum + ")/BOLDetails",headers=creds) as resp:
           return await resp.json()

async def get_BOLs_Company_BOLNum_BOLDetails_Company_BOLNum_BOLLine(Company, BOLNum, BOLLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BOLDetail item
   Description: Calls GetByID to retrieve the BOLDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BOLDetail1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BOLNum: Desc: BOLNum   Required: True
      :param BOLLine: Desc: BOLLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BOLDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLs(" + Company + "," + BOLNum + ")/BOLDetails(" + Company + "," + BOLNum + "," + BOLLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_BOLs_Company_BOLNum_BOLHeadAttches(Company, BOLNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BOLHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BOLHeadAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BOLNum: Desc: BOLNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BOLHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLs(" + Company + "," + BOLNum + ")/BOLHeadAttches",headers=creds) as resp:
           return await resp.json()

async def get_BOLs_Company_BOLNum_BOLHeadAttches_Company_BOLNum_DrawingSeq(Company, BOLNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BOLHeadAttch item
   Description: Calls GetByID to retrieve the BOLHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BOLHeadAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BOLNum: Desc: BOLNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BOLHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLs(" + Company + "," + BOLNum + ")/BOLHeadAttches(" + Company + "," + BOLNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_BOLDetails(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BOLDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BOLDetails
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BOLDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLDetails",headers=creds) as resp:
           return await resp.json()

async def post_BOLDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BOLDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BOLDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BOLDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLDetails", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BOLDetails_Company_BOLNum_BOLLine(Company, BOLNum, BOLLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BOLDetail item
   Description: Calls GetByID to retrieve the BOLDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BOLDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BOLNum: Desc: BOLNum   Required: True
      :param BOLLine: Desc: BOLLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BOLDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLDetails(" + Company + "," + BOLNum + "," + BOLLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BOLDetails_Company_BOLNum_BOLLine(Company, BOLNum, BOLLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BOLDetail for the service
   Description: Calls UpdateExt to update BOLDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BOLDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BOLNum: Desc: BOLNum   Required: True
      :param BOLLine: Desc: BOLLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BOLDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLDetails(" + Company + "," + BOLNum + "," + BOLLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BOLDetails_Company_BOLNum_BOLLine(Company, BOLNum, BOLLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BOLDetail item
   Description: Call UpdateExt to delete BOLDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BOLDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BOLNum: Desc: BOLNum   Required: True
      :param BOLLine: Desc: BOLLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLDetails(" + Company + "," + BOLNum + "," + BOLLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_BOLHeadAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BOLHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BOLHeadAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BOLHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLHeadAttches",headers=creds) as resp:
           return await resp.json()

async def post_BOLHeadAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BOLHeadAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BOLHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BOLHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLHeadAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BOLHeadAttches_Company_BOLNum_DrawingSeq(Company, BOLNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BOLHeadAttch item
   Description: Calls GetByID to retrieve the BOLHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BOLHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BOLNum: Desc: BOLNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BOLHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLHeadAttches(" + Company + "," + BOLNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BOLHeadAttches_Company_BOLNum_DrawingSeq(Company, BOLNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BOLHeadAttch for the service
   Description: Calls UpdateExt to update BOLHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BOLHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BOLNum: Desc: BOLNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BOLHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLHeadAttches(" + Company + "," + BOLNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BOLHeadAttches_Company_BOLNum_DrawingSeq(Company, BOLNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BOLHeadAttch item
   Description: Call UpdateExt to delete BOLHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BOLHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BOLNum: Desc: BOLNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/BOLHeadAttches(" + Company + "," + BOLNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BOLHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseBOLHead, whereClauseBOLHeadAttch, whereClauseBOLDetail, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseBOLHead=" + whereClauseBOLHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBOLHeadAttch=" + whereClauseBOLHeadAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBOLDetail=" + whereClauseBOLDetail
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(boLNum, epicorHeaders = None):
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
   params += "boLNum=" + boLNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: .
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeBOLHeadUseOTS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeBOLHeadUseOTS
   Description: Method to call when changing the UseOTS field the contract header record.
Refreshes the address list and contact info
   OperationID: ChangeBOLHeadUseOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBOLHeadUseOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBOLHeadUseOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeShipToCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeShipToCustID
   Description: Update BOL Header information with values from the Third Party Ship To when the Ship To is changed.
   OperationID: ChangeShipToCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeType
   Description: This method sets the default values when the BOLType field changes.  This should
only be possible on adds.  The field is not updateable in Update Mode.
   OperationID: ChangeType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyShipHedOTS(epicorHeaders = None):
   """  
   Summary: Invoke method CopyShipHedOTS
   Description: Purpose: To assign the ShipHed One Time Ship To info (found on the orderhed/orderrel) to the
BolHead fields.
Parameters:  none
Notes:
   OperationID: CopyShipHedOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyShipHedOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetBillingInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBillingInfo
   Description: This method populates the address information when the BillID field changes
   OperationID: GetBillingInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBillingInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBillingInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetShippingInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetShippingInfo
   Description: This method populates the Shipping information when the ShipID field changes
   OperationID: GetShippingInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShippingInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShippingInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSlips(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSlips
   Description: This method generates a list of linked or unlinked packs.  If the bolNum
field is not 0, then only the packs associated with that record will be returned.
Otherwise unlinked packs will be returned.  The records returned will be unlinked
pack lines (not the headers).
   OperationID: GetSlips
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSlips_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSlips_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrintBOL(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrintBOL
   Description: This method will print out the Bill of Lading.  Gives the option of Print Preview
   OperationID: PrintBOL
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrintBOL_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrintBOL_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateLinks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateLinks
   Description: If the linkFlag = yes,this method will either creates a new bill of lading linking
all of the selected packs to the new Bill of Lading created.  Or add a packing
slip to an existing Bill of Lading.  All of the packs selected for a new Slip
must have the same BOLType. When adding a pack to an exising BOL, the bolTypes
must match.
If the linkFlag = no, this method will unlink the specified pack from their
Bill of Lading.
The udpated/new Bill of Lading will be returned
   OperationID: UpdateLinks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateLinks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateLinks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateHeadShipTovsPackShipTo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateHeadShipTovsPackShipTo
   Description: When linking packages, validates if ShipTo from header match with ShipTo from Packs to link.
If don't match, fill a message to display to the user, continue linking if everything is OK.
When BOL is Linked and ShipTo from Header changes, validates if match with linked packages.
Fills The same mesasge, so user confirms continue or Cancel.
   OperationID: ValidateHeadShipTovsPackShipTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateHeadShipTovsPackShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateHeadShipTovsPackShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBOLHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBOLHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBOLHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBOLHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBOLHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBOLHeadAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBOLHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBOLHeadAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBOLHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBOLHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBOLDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBOLDetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBOLDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBOLDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBOLDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BOLSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BOLDetailRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BOLDetailRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BOLHeadAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BOLHeadAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BOLHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BOLHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BOLHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BOLHeadRow] = obj["value"]
      pass

class Erp_Tablesets_BOLDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BOLNum:int = obj["BOLNum"]
      """  When user creates a new BOL, the next available # is assigned by the system.  The system generates a number by finding the last BOLHead on file and uses its BOLNum + 1.  """  
      self.BOLLine:int = obj["BOLLine"]
      """  Bill of Lading line  """  
      self.Packages:int = obj["Packages"]
      """  Number of Packages (boxes, skids, drums...)  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Packaging Code ( "box" "skd" "drm" ...)  """  
      self.Weight:int = obj["Weight"]
      """  Weight Per Package.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Unit of Measure of the Weight Class that qualifies the weight.  """  
      self.Rate:int = obj["Rate"]
      """  NMFC Rate  """  
      self.ClassRate:str = obj["ClassRate"]
      """  NMFC Rate Classification  """  
      self.PkgClass:str = obj["PkgClass"]
      """  NMFC Packaging Classification code.  """  
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
      self.PkgClassDescription:str = obj["PkgClassDescription"]
      self.PkgCodeDescription:str = obj["PkgCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BOLHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BOLNum:int = obj["BOLNum"]
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

class Erp_Tablesets_BOLHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BOLNum:int = obj["BOLNum"]
      """  When user creates a new BOL, the next available # is assigned by the system.  The system generates a number by finding the last BOLHead on file and uses its BOLNum + 1.  """  
      self.BOLType:str = obj["BOLType"]
      """  Bill of Lading Type  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the BOL. Default as system date.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number.  Not user maintainable, Duplicated from the related Packing Slip.  Used to relate this record to the customer master.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used that this BOL was for.  This can only be one of the ShipToNum that exist on one of the Packing Slip records.  """  
      self.Carrier:str = obj["Carrier"]
      """  Carrier Name  """  
      self.ShipperNum:str = obj["ShipperNum"]
      """  Shipper Number  """  
      self.ProNumber:str = obj["ProNumber"]
      """  Pro Number  """  
      self.FreightCharges:str = obj["FreightCharges"]
      self.CODAmount:int = obj["CODAmount"]
      """  Collect On Delivery Amount  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Vendor to which this shipment is being made. This is the internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for project comments.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier for shipping origination.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Initials (user ID) of person who did the data entry.  This defaults as the current user ID, but can be changed.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  Used for Transfer Orders.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  Full name of the contact.  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready  """  
      self.CounterASN:int = obj["CounterASN"]
      """  Number of times the bill of lading has been printed, that means it changed from Non EDI Ready status to EDI Ready  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LinkedSlip:bool = obj["LinkedSlip"]
      """  Flag indicating if there are Linked Packing Slips  """  
      self.ShipAddr:str = obj["ShipAddr"]
      """  Shipping Address  """  
      self.BillAddr:str = obj["BillAddr"]
      """  Billing Address  """  
      self.BillID:str = obj["BillID"]
      """  Billing ID either VendorID or CustID  """  
      self.ShipID:str = obj["ShipID"]
      """  ShipTo ID (ToPlant, ShipToNum or PurPoint)  """  
      self.BillName:str = obj["BillName"]
      """  Billing Name (used for Searches)  """  
      self.TypeDesc:str = obj["TypeDesc"]
      """  BOLType Description  """  
      self.CustAllowOTS:bool = obj["CustAllowOTS"]
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.OTSCountryNumDescription:str = obj["OTSCountryNumDescription"]
      """  Country name  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.PurPointCountry:str = obj["PurPointCountry"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      """  Second address line  """  
      self.PurPointState:str = obj["PurPointState"]
      """  State portion of the address  """  
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      """  Third address line  """  
      self.PurPointName:str = obj["PurPointName"]
      """  Purchase Point Name...can't be blank.  """  
      self.PurPointZip:str = obj["PurPointZip"]
      """  Postal Code or Zip code portion of the address  """  
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      """  First address line  """  
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.PurPointCity:str = obj["PurPointCity"]
      """  City portion of the address  """  
      self.ShipToCustNumBTName:str = obj["ShipToCustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.ShipToCustNumCustID:str = obj["ShipToCustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.ShipToCustNumName:str = obj["ShipToCustNumName"]
      """  The full name of the customer.  """  
      self.ToPlantName:str = obj["ToPlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
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
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BOLHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BOLNum:int = obj["BOLNum"]
      """  When user creates a new BOL, the next available # is assigned by the system.  The system generates a number by finding the last BOLHead on file and uses its BOLNum + 1.  """  
      self.BOLType:str = obj["BOLType"]
      """  Bill of Lading Type  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the BOL. Default as system date.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number.  Not user maintainable, Duplicated from the related Packing Slip.  Used to relate this record to the customer master.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used that this BOL was for.  This can only be one of the ShipToNum that exist on one of the Packing Slip records.  """  
      self.Carrier:str = obj["Carrier"]
      """  Carrier Name  """  
      self.ShipperNum:str = obj["ShipperNum"]
      """  Shipper Number  """  
      self.ProNumber:str = obj["ProNumber"]
      """  Pro Number  """  
      self.FreightCharges:str = obj["FreightCharges"]
      self.CODAmount:int = obj["CODAmount"]
      """  Collect On Delivery Amount  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Vendor to which this shipment is being made. This is the internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for project comments.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier for shipping origination.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Initials (user ID) of person who did the data entry.  This defaults as the current user ID, but can be changed.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  Used for Transfer Orders.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  Full name of the contact.  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready  """  
      self.CounterASN:int = obj["CounterASN"]
      """  Number of times the bill of lading has been printed, that means it changed from Non EDI Ready status to EDI Ready  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LinkedSlip:bool = obj["LinkedSlip"]
      """  Flag indicating if there are Linked Packing Slips  """  
      self.ShipAddr:str = obj["ShipAddr"]
      """  Shipping Address  """  
      self.BillAddr:str = obj["BillAddr"]
      """  Billing Address  """  
      self.BillID:str = obj["BillID"]
      """  The ID of the customer or supplier.  """  
      self.ShipID:str = obj["ShipID"]
      """  ShipTo ID (ToPlant, ShipToNum or PurPoint)  """  
      self.BillName:str = obj["BillName"]
      """  Billing Name (used for Searches)  """  
      self.TypeDesc:str = obj["TypeDesc"]
      """  BOLType Description  """  
      self.CustAllowOTS:bool = obj["CustAllowOTS"]
      self.BillAddrFormatted:str = obj["BillAddrFormatted"]
      """  Billing Address Formatted  """  
      self.ShipAddrFormatted:str = obj["ShipAddrFormatted"]
      """  Shipping Address Formatted  """  
      self.InactiveCustomer:bool = obj["InactiveCustomer"]
      """  Indicates a customer referenced on the record is inactive.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.OTSCountryNumDescription:str = obj["OTSCountryNumDescription"]
      self.PlantName:str = obj["PlantName"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointState:str = obj["PurPointState"]
      self.ShipToCustNumBTName:str = obj["ShipToCustNumBTName"]
      self.ShipToCustNumCustID:str = obj["ShipToCustNumCustID"]
      self.ShipToCustNumName:str = obj["ShipToCustNumName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.ToPlantName:str = obj["ToPlantName"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeBOLHeadUseOTS_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BOLTableset] = obj["ds"]
      pass

class ChangeBOLHeadUseOTS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BOLTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeShipToCustID_input:
   """ Required : 
   iShipToCustID
   ds
   """  
   def __init__(self, obj):
      self.iShipToCustID:str = obj["iShipToCustID"]
      """  Proposed Third-Party Ship To  """  
      self.ds:list[Erp_Tablesets_BOLTableset] = obj["ds"]
      pass

class ChangeShipToCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BOLTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BOLTableset] = obj["ds"]
      pass

class ChangeType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BOLTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CopyShipHedOTS_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   boLNum
   """  
   def __init__(self, obj):
      self.boLNum:int = obj["boLNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_BOLDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BOLNum:int = obj["BOLNum"]
      """  When user creates a new BOL, the next available # is assigned by the system.  The system generates a number by finding the last BOLHead on file and uses its BOLNum + 1.  """  
      self.BOLLine:int = obj["BOLLine"]
      """  Bill of Lading line  """  
      self.Packages:int = obj["Packages"]
      """  Number of Packages (boxes, skids, drums...)  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Packaging Code ( "box" "skd" "drm" ...)  """  
      self.Weight:int = obj["Weight"]
      """  Weight Per Package.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Unit of Measure of the Weight Class that qualifies the weight.  """  
      self.Rate:int = obj["Rate"]
      """  NMFC Rate  """  
      self.ClassRate:str = obj["ClassRate"]
      """  NMFC Rate Classification  """  
      self.PkgClass:str = obj["PkgClass"]
      """  NMFC Packaging Classification code.  """  
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
      self.PkgClassDescription:str = obj["PkgClassDescription"]
      self.PkgCodeDescription:str = obj["PkgCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BOLHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BOLNum:int = obj["BOLNum"]
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

class Erp_Tablesets_BOLHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BOLNum:int = obj["BOLNum"]
      """  When user creates a new BOL, the next available # is assigned by the system.  The system generates a number by finding the last BOLHead on file and uses its BOLNum + 1.  """  
      self.BOLType:str = obj["BOLType"]
      """  Bill of Lading Type  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the BOL. Default as system date.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number.  Not user maintainable, Duplicated from the related Packing Slip.  Used to relate this record to the customer master.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used that this BOL was for.  This can only be one of the ShipToNum that exist on one of the Packing Slip records.  """  
      self.Carrier:str = obj["Carrier"]
      """  Carrier Name  """  
      self.ShipperNum:str = obj["ShipperNum"]
      """  Shipper Number  """  
      self.ProNumber:str = obj["ProNumber"]
      """  Pro Number  """  
      self.FreightCharges:str = obj["FreightCharges"]
      self.CODAmount:int = obj["CODAmount"]
      """  Collect On Delivery Amount  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Vendor to which this shipment is being made. This is the internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for project comments.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier for shipping origination.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Initials (user ID) of person who did the data entry.  This defaults as the current user ID, but can be changed.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  Used for Transfer Orders.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  Full name of the contact.  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready  """  
      self.CounterASN:int = obj["CounterASN"]
      """  Number of times the bill of lading has been printed, that means it changed from Non EDI Ready status to EDI Ready  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LinkedSlip:bool = obj["LinkedSlip"]
      """  Flag indicating if there are Linked Packing Slips  """  
      self.ShipAddr:str = obj["ShipAddr"]
      """  Shipping Address  """  
      self.BillAddr:str = obj["BillAddr"]
      """  Billing Address  """  
      self.BillID:str = obj["BillID"]
      """  Billing ID either VendorID or CustID  """  
      self.ShipID:str = obj["ShipID"]
      """  ShipTo ID (ToPlant, ShipToNum or PurPoint)  """  
      self.BillName:str = obj["BillName"]
      """  Billing Name (used for Searches)  """  
      self.TypeDesc:str = obj["TypeDesc"]
      """  BOLType Description  """  
      self.CustAllowOTS:bool = obj["CustAllowOTS"]
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.OTSCountryNumDescription:str = obj["OTSCountryNumDescription"]
      """  Country name  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.PurPointCountry:str = obj["PurPointCountry"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      """  Second address line  """  
      self.PurPointState:str = obj["PurPointState"]
      """  State portion of the address  """  
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      """  Third address line  """  
      self.PurPointName:str = obj["PurPointName"]
      """  Purchase Point Name...can't be blank.  """  
      self.PurPointZip:str = obj["PurPointZip"]
      """  Postal Code or Zip code portion of the address  """  
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      """  First address line  """  
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.PurPointCity:str = obj["PurPointCity"]
      """  City portion of the address  """  
      self.ShipToCustNumBTName:str = obj["ShipToCustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.ShipToCustNumCustID:str = obj["ShipToCustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.ShipToCustNumName:str = obj["ShipToCustNumName"]
      """  The full name of the customer.  """  
      self.ToPlantName:str = obj["ToPlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
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
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BOLHeadListTableset:
   def __init__(self, obj):
      self.BOLHeadList:list[Erp_Tablesets_BOLHeadListRow] = obj["BOLHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_BOLHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BOLNum:int = obj["BOLNum"]
      """  When user creates a new BOL, the next available # is assigned by the system.  The system generates a number by finding the last BOLHead on file and uses its BOLNum + 1.  """  
      self.BOLType:str = obj["BOLType"]
      """  Bill of Lading Type  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the BOL. Default as system date.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number.  Not user maintainable, Duplicated from the related Packing Slip.  Used to relate this record to the customer master.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used that this BOL was for.  This can only be one of the ShipToNum that exist on one of the Packing Slip records.  """  
      self.Carrier:str = obj["Carrier"]
      """  Carrier Name  """  
      self.ShipperNum:str = obj["ShipperNum"]
      """  Shipper Number  """  
      self.ProNumber:str = obj["ProNumber"]
      """  Pro Number  """  
      self.FreightCharges:str = obj["FreightCharges"]
      self.CODAmount:int = obj["CODAmount"]
      """  Collect On Delivery Amount  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Vendor to which this shipment is being made. This is the internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for project comments.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier for shipping origination.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Initials (user ID) of person who did the data entry.  This defaults as the current user ID, but can be changed.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  Used for Transfer Orders.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time ShipTo information should be used instead of the standard ShipTo.  One Time ShipTo info is stored in this record in the fields prefixed with "OTS"
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  Full name of the contact.  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready  """  
      self.CounterASN:int = obj["CounterASN"]
      """  Number of times the bill of lading has been printed, that means it changed from Non EDI Ready status to EDI Ready  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LinkedSlip:bool = obj["LinkedSlip"]
      """  Flag indicating if there are Linked Packing Slips  """  
      self.ShipAddr:str = obj["ShipAddr"]
      """  Shipping Address  """  
      self.BillAddr:str = obj["BillAddr"]
      """  Billing Address  """  
      self.BillID:str = obj["BillID"]
      """  The ID of the customer or supplier.  """  
      self.ShipID:str = obj["ShipID"]
      """  ShipTo ID (ToPlant, ShipToNum or PurPoint)  """  
      self.BillName:str = obj["BillName"]
      """  Billing Name (used for Searches)  """  
      self.TypeDesc:str = obj["TypeDesc"]
      """  BOLType Description  """  
      self.CustAllowOTS:bool = obj["CustAllowOTS"]
      self.BillAddrFormatted:str = obj["BillAddrFormatted"]
      """  Billing Address Formatted  """  
      self.ShipAddrFormatted:str = obj["ShipAddrFormatted"]
      """  Shipping Address Formatted  """  
      self.InactiveCustomer:bool = obj["InactiveCustomer"]
      """  Indicates a customer referenced on the record is inactive.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.OTSCountryNumDescription:str = obj["OTSCountryNumDescription"]
      self.PlantName:str = obj["PlantName"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointState:str = obj["PurPointState"]
      self.ShipToCustNumBTName:str = obj["ShipToCustNumBTName"]
      self.ShipToCustNumCustID:str = obj["ShipToCustNumCustID"]
      self.ShipToCustNumName:str = obj["ShipToCustNumName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.ToPlantName:str = obj["ToPlantName"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BOLSlipRow:
   def __init__(self, obj):
      self.BOLType:str = obj["BOLType"]
      self.ShipLog:str = obj["ShipLog"]
      """  BOLNum field for linked slips  """  
      self.PackNum:int = obj["PackNum"]
      self.OrderNum:str = obj["OrderNum"]
      self.ShipDate:str = obj["ShipDate"]
      self.Name:str = obj["Name"]
      """  Name from Packing Slip  """  
      self.ShipTo:str = obj["ShipTo"]
      """  ShipTo ID for SubContract  """  
      self.EntryName:str = obj["EntryName"]
      """  Name of User who entered the packing slip  """  
      self.LineNum:int = obj["LineNum"]
      self.Class:str = obj["Class"]
      self.PkgType:str = obj["PkgType"]
      self.Direct:bool = obj["Direct"]
      """  Indicates if this is a direct transfer  """  
      self.ActionFlag:str = obj["ActionFlag"]
      """  L - Linking slip, U - Unlinking slip  """  
      self.Weight:int = obj["Weight"]
      self.Packages:int = obj["Packages"]
      self.BillNum:str = obj["BillNum"]
      """  Billing ID, used in creating the linked BOL record  """  
      self.Carrier:str = obj["Carrier"]
      """  ShipVia Carrier description  """  
      self.BOLLine:int = obj["BOLLine"]
      """  BOL Line linked to  """  
      self.BOLNum:int = obj["BOLNum"]
      self.MasterPackFlag:bool = obj["MasterPackFlag"]
      """  Flag to indicate whether or not this is generated from a Masterpack to be used when updating the source tables.  """  
      self.TempCustNum:int = obj["TempCustNum"]
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      self.WeightUOM:str = obj["WeightUOM"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BOLSlipTableset:
   def __init__(self, obj):
      self.BOLSlip:list[Erp_Tablesets_BOLSlipRow] = obj["BOLSlip"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_BOLTableset:
   def __init__(self, obj):
      self.BOLHead:list[Erp_Tablesets_BOLHeadRow] = obj["BOLHead"]
      self.BOLHeadAttch:list[Erp_Tablesets_BOLHeadAttchRow] = obj["BOLHeadAttch"]
      self.BOLDetail:list[Erp_Tablesets_BOLDetailRow] = obj["BOLDetail"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtBOLTableset:
   def __init__(self, obj):
      self.BOLHead:list[Erp_Tablesets_BOLHeadRow] = obj["BOLHead"]
      self.BOLHeadAttch:list[Erp_Tablesets_BOLHeadAttchRow] = obj["BOLHeadAttch"]
      self.BOLDetail:list[Erp_Tablesets_BOLDetailRow] = obj["BOLDetail"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetBillingInfo_input:
   """ Required : 
   billID
   ds
   """  
   def __init__(self, obj):
      self.billID:str = obj["billID"]
      """  Proposed Billing ID.  """  
      self.ds:list[Erp_Tablesets_BOLTableset] = obj["ds"]
      pass

class GetBillingInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BOLTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   boLNum
   """  
   def __init__(self, obj):
      self.boLNum:int = obj["boLNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BOLTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_BOLTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_BOLTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  tableName  """  
      self.fieldName:str = obj["fieldName"]
      """  fieldName  """  
      pass

class GetCodeDescList_output:
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
      self.returnObj:list[Erp_Tablesets_BOLHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewBOLDetail_input:
   """ Required : 
   ds
   boLNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BOLTableset] = obj["ds"]
      self.boLNum:int = obj["boLNum"]
      pass

class GetNewBOLDetail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BOLTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBOLHeadAttch_input:
   """ Required : 
   ds
   boLNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BOLTableset] = obj["ds"]
      self.boLNum:int = obj["boLNum"]
      pass

class GetNewBOLHeadAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BOLTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBOLHead_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BOLTableset] = obj["ds"]
      pass

class GetNewBOLHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BOLTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseBOLHead
   whereClauseBOLHeadAttch
   whereClauseBOLDetail
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseBOLHead:str = obj["whereClauseBOLHead"]
      self.whereClauseBOLHeadAttch:str = obj["whereClauseBOLHeadAttch"]
      self.whereClauseBOLDetail:str = obj["whereClauseBOLDetail"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BOLTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetShippingInfo_input:
   """ Required : 
   shipID
   ds
   """  
   def __init__(self, obj):
      self.shipID:str = obj["shipID"]
      """  Proposed Shipping ID  """  
      self.ds:list[Erp_Tablesets_BOLTableset] = obj["ds"]
      pass

class GetShippingInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BOLTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSlips_input:
   """ Required : 
   bolNum
   bolType
   updateLinkFlag
   """  
   def __init__(self, obj):
      self.bolNum:int = obj["bolNum"]
      """  Bill of lading for which to get the linked Packs for.
            If 0, then unlinked Packs will be returned  """  
      self.bolType:str = obj["bolType"]
      """  Type of BOL record to create. If left blank, all unlinked
            packs will be returned so the UI can filter based on BOLType.  Otherwise only
            the specified BOLType records will be returned.  Can be left Blank if returning linked
            packs  """  
      self.updateLinkFlag:bool = obj["updateLinkFlag"]
      """  it's true when the method is called after Update Linked
            Packs  """  
      pass

class GetSlips_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BOLSlipTableset] = obj["returnObj"]
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

class PrintBOL_input:
   """ Required : 
   bolNum
   printPreview
   """  
   def __init__(self, obj):
      self.bolNum:int = obj["bolNum"]
      """  Bill of Lading number to print  """  
      self.printPreview:bool = obj["printPreview"]
      """  Flag indicating whether to preview the print job  """  
      pass

class PrintBOL_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtBOLTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtBOLTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateLinks_input:
   """ Required : 
   linkFlag
   bolNum
   bolLine
   wholePack
   ds
   """  
   def __init__(self, obj):
      self.linkFlag:bool = obj["linkFlag"]
      """  Yes if linking to a pack, no to unlink  """  
      self.bolNum:int = obj["bolNum"]
      """  Bill of Lading Number, 0 for creating a new BOL or if unlinking a
            pack  """  
      self.bolLine:int = obj["bolLine"]
      """  Bill of Lading Line, 0 for creating a new BOL  """  
      self.wholePack:bool = obj["wholePack"]
      """  Flag indicates the whole pack (all lines) should be linked
            or if only the selected lines should be linked.  """  
      self.ds:list[Erp_Tablesets_BOLSlipTableset] = obj["ds"]
      pass

class UpdateLinks_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BOLHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BOLSlipTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BOLTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BOLTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateHeadShipTovsPackShipTo_input:
   """ Required : 
   bolNum
   calledFrom
   isLinked
   newShipID
   ds
   """  
   def __init__(self, obj):
      self.bolNum:int = obj["bolNum"]
      """  BOL Number  """  
      self.calledFrom:str = obj["calledFrom"]
      """  specifies if procedure is called from Linking process or Changing header ShipToID  """  
      self.isLinked:bool = obj["isLinked"]
      """  defines if the BOL Header is already linked or not  """  
      self.newShipID:str = obj["newShipID"]
      """  Is the ShipID to be evaluated vs ShipToID from Packs  """  
      self.ds:list[Erp_Tablesets_BOLSlipTableset] = obj["ds"]
      pass

class ValidateHeadShipTovsPackShipTo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

