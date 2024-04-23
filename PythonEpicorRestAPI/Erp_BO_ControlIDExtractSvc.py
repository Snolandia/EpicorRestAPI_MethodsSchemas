import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ControlIDExtractSvc
# Description: Master file maintenance business logic for ControlIDExtract
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ControlIDExtracts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ControlIDExtracts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ControlIDExtracts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ControlIDExtractHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtracts",headers=creds) as resp:
           return await resp.json()

async def post_ControlIDExtracts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ControlIDExtracts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ControlIDExtractHeaderRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ControlIDExtractHeaderRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtracts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ControlIDExtracts_Company_ControlIDExtractCode(Company, ControlIDExtractCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ControlIDExtract item
   Description: Calls GetByID to retrieve the ControlIDExtract item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ControlIDExtract
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ControlIDExtractCode: Desc: ControlIDExtractCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ControlIDExtractHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtracts(" + Company + "," + ControlIDExtractCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ControlIDExtracts_Company_ControlIDExtractCode(Company, ControlIDExtractCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ControlIDExtract for the service
   Description: Calls UpdateExt to update ControlIDExtract. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ControlIDExtract
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ControlIDExtractCode: Desc: ControlIDExtractCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ControlIDExtractHeaderRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtracts(" + Company + "," + ControlIDExtractCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ControlIDExtracts_Company_ControlIDExtractCode(Company, ControlIDExtractCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ControlIDExtract item
   Description: Call UpdateExt to delete ControlIDExtract item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ControlIDExtract
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ControlIDExtractCode: Desc: ControlIDExtractCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtracts(" + Company + "," + ControlIDExtractCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_ControlIDExtracts_Company_ControlIDExtractCode_ControlIDExtractSegments(Company, ControlIDExtractCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ControlIDExtractSegments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ControlIDExtractSegments1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ControlIDExtractCode: Desc: ControlIDExtractCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ControlIDExtractSegmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtracts(" + Company + "," + ControlIDExtractCode + ")/ControlIDExtractSegments",headers=creds) as resp:
           return await resp.json()

async def get_ControlIDExtracts_Company_ControlIDExtractCode_ControlIDExtractSegments_Company_ControlIDExtractCode_SegmentNum(Company, ControlIDExtractCode, SegmentNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ControlIDExtractSegment item
   Description: Calls GetByID to retrieve the ControlIDExtractSegment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ControlIDExtractSegment1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ControlIDExtractCode: Desc: ControlIDExtractCode   Required: True   Allow empty value : True
      :param SegmentNum: Desc: SegmentNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ControlIDExtractSegmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtracts(" + Company + "," + ControlIDExtractCode + ")/ControlIDExtractSegments(" + Company + "," + ControlIDExtractCode + "," + SegmentNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ControlIDExtractSegments(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ControlIDExtractSegments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ControlIDExtractSegments
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ControlIDExtractSegmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtractSegments",headers=creds) as resp:
           return await resp.json()

async def post_ControlIDExtractSegments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ControlIDExtractSegments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ControlIDExtractSegmentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ControlIDExtractSegmentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtractSegments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ControlIDExtractSegments_Company_ControlIDExtractCode_SegmentNum(Company, ControlIDExtractCode, SegmentNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ControlIDExtractSegment item
   Description: Calls GetByID to retrieve the ControlIDExtractSegment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ControlIDExtractSegment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ControlIDExtractCode: Desc: ControlIDExtractCode   Required: True   Allow empty value : True
      :param SegmentNum: Desc: SegmentNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ControlIDExtractSegmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtractSegments(" + Company + "," + ControlIDExtractCode + "," + SegmentNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ControlIDExtractSegments_Company_ControlIDExtractCode_SegmentNum(Company, ControlIDExtractCode, SegmentNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ControlIDExtractSegment for the service
   Description: Calls UpdateExt to update ControlIDExtractSegment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ControlIDExtractSegment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ControlIDExtractCode: Desc: ControlIDExtractCode   Required: True   Allow empty value : True
      :param SegmentNum: Desc: SegmentNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ControlIDExtractSegmentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtractSegments(" + Company + "," + ControlIDExtractCode + "," + SegmentNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ControlIDExtractSegments_Company_ControlIDExtractCode_SegmentNum(Company, ControlIDExtractCode, SegmentNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ControlIDExtractSegment item
   Description: Call UpdateExt to delete ControlIDExtractSegment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ControlIDExtractSegment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ControlIDExtractCode: Desc: ControlIDExtractCode   Required: True   Allow empty value : True
      :param SegmentNum: Desc: SegmentNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtractSegments(" + Company + "," + ControlIDExtractCode + "," + SegmentNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ControlIDExtractPCIDs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ControlIDExtractPCIDs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ControlIDExtractPCIDs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ControlIDExtractPCIDRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtractPCIDs",headers=creds) as resp:
           return await resp.json()

async def post_ControlIDExtractPCIDs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ControlIDExtractPCIDs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ControlIDExtractPCIDRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ControlIDExtractPCIDRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtractPCIDs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ControlIDExtractPCIDs_Company_DataIdentifierCode(Company, DataIdentifierCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ControlIDExtractPCID item
   Description: Calls GetByID to retrieve the ControlIDExtractPCID item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ControlIDExtractPCID
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DataIdentifierCode: Desc: DataIdentifierCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ControlIDExtractPCIDRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtractPCIDs(" + Company + "," + DataIdentifierCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ControlIDExtractPCIDs_Company_DataIdentifierCode(Company, DataIdentifierCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ControlIDExtractPCID for the service
   Description: Calls UpdateExt to update ControlIDExtractPCID. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ControlIDExtractPCID
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DataIdentifierCode: Desc: DataIdentifierCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ControlIDExtractPCIDRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtractPCIDs(" + Company + "," + DataIdentifierCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ControlIDExtractPCIDs_Company_DataIdentifierCode(Company, DataIdentifierCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ControlIDExtractPCID item
   Description: Call UpdateExt to delete ControlIDExtractPCID item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ControlIDExtractPCID
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DataIdentifierCode: Desc: DataIdentifierCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/ControlIDExtractPCIDs(" + Company + "," + DataIdentifierCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ControlIDExtractHeaderListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseControlIDExtractHeader, whereClauseControlIDExtractSegment, whereClauseControlIDExtractPCID, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseControlIDExtractHeader=" + whereClauseControlIDExtractHeader
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseControlIDExtractSegment=" + whereClauseControlIDExtractSegment
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseControlIDExtractPCID=" + whereClauseControlIDExtractPCID
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(controlIDExtractCode, epicorHeaders = None):
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
   params += "controlIDExtractCode=" + controlIDExtractCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetControlIDExtractPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetControlIDExtractPCID
   Description: This method was coded to retreive the ControlIDExtractPCID records.  Since the ControlIDExtractPCID does not have a
relation to the other 2 tables, this needs to be retreived manually if getbyID is not called.
   OperationID: GetControlIDExtractPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetControlIDExtractPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetControlIDExtractPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDimension(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDimension
   Description: Call this method when the value of Dimension changed
   OperationID: OnChangeDimension
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDimension_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDimension_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeIsFixedLength(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeIsFixedLength
   Description: Call this method when the value of IsFixedLength changed
   OperationID: OnChangeIsFixedLength
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeIsFixedLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeIsFixedLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSegmentType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSegmentType
   Description: Call this method when the value of SegmentType changed
   OperationID: OnChangeSegmentType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSegmentType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSegmentType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeExtractPCIDIsFixedLength(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeExtractPCIDIsFixedLength
   Description: Call this method when the value of ExtractPCIDIsFixedLength changed
   OperationID: OnChangeExtractPCIDIsFixedLength
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeExtractPCIDIsFixedLength_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeExtractPCIDIsFixedLength_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: Returns the Code/Desc list of the column
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewControlIDExtractHeader(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewControlIDExtractHeader
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewControlIDExtractHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewControlIDExtractHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewControlIDExtractHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewControlIDExtractSegment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewControlIDExtractSegment
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewControlIDExtractSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewControlIDExtractSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewControlIDExtractSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewControlIDExtractPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewControlIDExtractPCID
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewControlIDExtractPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewControlIDExtractPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewControlIDExtractPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ControlIDExtractSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ControlIDExtractHeaderListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ControlIDExtractHeaderListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ControlIDExtractHeaderRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ControlIDExtractHeaderRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ControlIDExtractPCIDRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ControlIDExtractPCIDRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ControlIDExtractSegmentRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ControlIDExtractSegmentRow] = obj["value"]
      pass

class Erp_Tablesets_ControlIDExtractHeaderListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ControlIDExtractCode:str = obj["ControlIDExtractCode"]
      """  Code that makes this set of Control ID Extract rules unique.  """  
      self.ControlIDExtractDesc:str = obj["ControlIDExtractDesc"]
      """  Description of this set of Control ID Extract rules.  """  
      self.ExtractSequence:int = obj["ExtractSequence"]
      """  Identifies the sequence in which the Control ID Extract rules will be checked.  """  
      self.DataIdentifier:str = obj["DataIdentifier"]
      """  Identifies the character string match for the left side characters of the string defined with this set of Control ID Extract rules.  """  
      self.IsFixedLength:bool = obj["IsFixedLength"]
      """  Identifies if the string defined with this set of Control ID Extract rules is a fixed length.  """  
      self.DigitsInString:int = obj["DigitsInString"]
      """  Identifies the number of digits in the string defined with this set of Control ID Extract rules is a fixed length.  """  
      self.DataFormat:str = obj["DataFormat"]
      """  Identifies the Data Format for the Segments for this set of Control ID Extract rules.  """  
      self.GroupSeparatorCharacter:str = obj["GroupSeparatorCharacter"]
      """  Identifies the Group Separator Character for this set of Control ID Extract rules.  """  
      self.RecordSeparatorCharacter:str = obj["RecordSeparatorCharacter"]
      """  Identifies the Record Separator Character for this set of Control ID Extract rules.  """  
      self.EndOfTransmissionCharacter:str = obj["EndOfTransmissionCharacter"]
      """  Identifies the End of Transmission Character for this set of Control ID Extract rules.  """  
      self.ExtractComments:str = obj["ExtractComments"]
      """  Identifies additional information about this set of Control ID Extract rules.  """  
      self.Dimension:str = obj["Dimension"]
      """  Indicates if this set of Control ID Extract rules relates to a 1D, 2D or 3D barcode.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  Development use only.  """  
      self.DevCharacter02:str = obj["DevCharacter02"]
      """  Development use only.  """  
      self.DevInteger01:int = obj["DevInteger01"]
      """  Development use only.  """  
      self.DevInteger02:int = obj["DevInteger02"]
      """  Development use only.  """  
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  Development use only.  """  
      self.DevBoolean02:bool = obj["DevBoolean02"]
      """  Development use only.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.EndOfTransmissionASCII:int = obj["EndOfTransmissionASCII"]
      self.GroupSeparatorASCII:int = obj["GroupSeparatorASCII"]
      self.RecordSeparatorASCII:int = obj["RecordSeparatorASCII"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ControlIDExtractHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ControlIDExtractCode:str = obj["ControlIDExtractCode"]
      """  Code that makes this set of Control ID Extract rules unique.  """  
      self.ControlIDExtractDesc:str = obj["ControlIDExtractDesc"]
      """  Description of this set of Control ID Extract rules.  """  
      self.ExtractSequence:int = obj["ExtractSequence"]
      """  Identifies the sequence in which the Control ID Extract rules will be checked.  """  
      self.DataIdentifier:str = obj["DataIdentifier"]
      """  Identifies the character string match for the left side characters of the string defined with this set of Control ID Extract rules.  """  
      self.IsFixedLength:bool = obj["IsFixedLength"]
      """  Identifies if the string defined with this set of Control ID Extract rules is a fixed length.  """  
      self.DigitsInString:int = obj["DigitsInString"]
      """  Identifies the number of digits in the string defined with this set of Control ID Extract rules is a fixed length.  """  
      self.DataFormat:str = obj["DataFormat"]
      """  Identifies the Data Format for the Segments for this set of Control ID Extract rules.  """  
      self.GroupSeparatorCharacter:str = obj["GroupSeparatorCharacter"]
      """  Identifies the Group Separator Character for this set of Control ID Extract rules.  """  
      self.RecordSeparatorCharacter:str = obj["RecordSeparatorCharacter"]
      """  Identifies the Record Separator Character for this set of Control ID Extract rules.  """  
      self.EndOfTransmissionCharacter:str = obj["EndOfTransmissionCharacter"]
      """  Identifies the End of Transmission Character for this set of Control ID Extract rules.  """  
      self.ExtractComments:str = obj["ExtractComments"]
      """  Identifies additional information about this set of Control ID Extract rules.  """  
      self.Dimension:str = obj["Dimension"]
      """  Indicates if this set of Control ID Extract rules relates to a 1D, 2D or 3D barcode.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  Development use only.  """  
      self.DevCharacter02:str = obj["DevCharacter02"]
      """  Development use only.  """  
      self.DevInteger01:int = obj["DevInteger01"]
      """  Development use only.  """  
      self.DevInteger02:int = obj["DevInteger02"]
      """  Development use only.  """  
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  Development use only.  """  
      self.DevBoolean02:bool = obj["DevBoolean02"]
      """  Development use only.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.EndOfTransmissionASCII:int = obj["EndOfTransmissionASCII"]
      self.GroupSeparatorASCII:int = obj["GroupSeparatorASCII"]
      self.RecordSeparatorASCII:int = obj["RecordSeparatorASCII"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ControlIDExtractPCIDRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DataIdentifierCode:str = obj["DataIdentifierCode"]
      """  Unique code assigned by the user for this data identifier.  """  
      self.DataIdentifierDesc:str = obj["DataIdentifierDesc"]
      """  Description of the data identifier.  """  
      self.DataIdentifier:str = obj["DataIdentifier"]
      """  Identifies the character string match for the left side characters of the Control ID.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the record is inactive or not. Default is false.  """  
      self.ExtractSequence:int = obj["ExtractSequence"]
      """  Identifies the order in which the Control ID Extract data identifiers will be checked against the Control ID.  """  
      self.DigitsToExtract:int = obj["DigitsToExtract"]
      """  Identifies the number of digits from the right end of the Control ID string to be extracted.  """  
      self.IsFixedLength:bool = obj["IsFixedLength"]
      """  Identifies if the Control ID string is a fixed length.  """  
      self.DigitsInString:int = obj["DigitsInString"]
      """  Identifies the number of digits in the Control ID string if it is a fixed length.  """  
      self.ExtractComments:str = obj["ExtractComments"]
      """  Identifies additional information about the Control ID Extract data identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ScanMinLength:int = obj["ScanMinLength"]
      """  Scan Minimum Length  """  
      self.ScanMaxLength:int = obj["ScanMaxLength"]
      """  Scan Maximum Length  """  
      self.Active:bool = obj["Active"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ControlIDExtractSegmentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ControlIDExtractCode:str = obj["ControlIDExtractCode"]
      """  Code that makes this set of Control ID Extract rules unique.  """  
      self.SegmentNum:int = obj["SegmentNum"]
      """  Segment Number that uniquely identifies this segment within the set of Control ID Extract rules.  """  
      self.SegmentType:str = obj["SegmentType"]
      """  Segment Type.  Valid Values are PCID and OTHER.  This will be expended in the future to handle other types.  """  
      self.DataIdentifier:str = obj["DataIdentifier"]
      """  Identifies the character string match for the left side characters of the string defined with this segment.  """  
      self.PCIDSegmentPosition:int = obj["PCIDSegmentPosition"]
      """  The position of this segment in the concatenated PCID value.  """  
      self.SegmentPosition:int = obj["SegmentPosition"]
      """  Segment Position in the string.  """  
      self.StartCharacterPosition:int = obj["StartCharacterPosition"]
      """  Position in the string of the start character of this segment.  """  
      self.EndCharacterPosition:int = obj["EndCharacterPosition"]
      """  Position in the string of the end character of this segment.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  Development use only.  """  
      self.DevCharacter02:str = obj["DevCharacter02"]
      """  Development use only.  """  
      self.DevInteger01:int = obj["DevInteger01"]
      """  Development use only.  """  
      self.DevInteger02:int = obj["DevInteger02"]
      """  Development use only.  """  
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  Development use only.  """  
      self.DevBoolean02:bool = obj["DevBoolean02"]
      """  Development use only.  """  
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
   controlIDExtractCode
   """  
   def __init__(self, obj):
      self.controlIDExtractCode:str = obj["controlIDExtractCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ControlIDExtractHeaderListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ControlIDExtractCode:str = obj["ControlIDExtractCode"]
      """  Code that makes this set of Control ID Extract rules unique.  """  
      self.ControlIDExtractDesc:str = obj["ControlIDExtractDesc"]
      """  Description of this set of Control ID Extract rules.  """  
      self.ExtractSequence:int = obj["ExtractSequence"]
      """  Identifies the sequence in which the Control ID Extract rules will be checked.  """  
      self.DataIdentifier:str = obj["DataIdentifier"]
      """  Identifies the character string match for the left side characters of the string defined with this set of Control ID Extract rules.  """  
      self.IsFixedLength:bool = obj["IsFixedLength"]
      """  Identifies if the string defined with this set of Control ID Extract rules is a fixed length.  """  
      self.DigitsInString:int = obj["DigitsInString"]
      """  Identifies the number of digits in the string defined with this set of Control ID Extract rules is a fixed length.  """  
      self.DataFormat:str = obj["DataFormat"]
      """  Identifies the Data Format for the Segments for this set of Control ID Extract rules.  """  
      self.GroupSeparatorCharacter:str = obj["GroupSeparatorCharacter"]
      """  Identifies the Group Separator Character for this set of Control ID Extract rules.  """  
      self.RecordSeparatorCharacter:str = obj["RecordSeparatorCharacter"]
      """  Identifies the Record Separator Character for this set of Control ID Extract rules.  """  
      self.EndOfTransmissionCharacter:str = obj["EndOfTransmissionCharacter"]
      """  Identifies the End of Transmission Character for this set of Control ID Extract rules.  """  
      self.ExtractComments:str = obj["ExtractComments"]
      """  Identifies additional information about this set of Control ID Extract rules.  """  
      self.Dimension:str = obj["Dimension"]
      """  Indicates if this set of Control ID Extract rules relates to a 1D, 2D or 3D barcode.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  Development use only.  """  
      self.DevCharacter02:str = obj["DevCharacter02"]
      """  Development use only.  """  
      self.DevInteger01:int = obj["DevInteger01"]
      """  Development use only.  """  
      self.DevInteger02:int = obj["DevInteger02"]
      """  Development use only.  """  
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  Development use only.  """  
      self.DevBoolean02:bool = obj["DevBoolean02"]
      """  Development use only.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.EndOfTransmissionASCII:int = obj["EndOfTransmissionASCII"]
      self.GroupSeparatorASCII:int = obj["GroupSeparatorASCII"]
      self.RecordSeparatorASCII:int = obj["RecordSeparatorASCII"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ControlIDExtractHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ControlIDExtractCode:str = obj["ControlIDExtractCode"]
      """  Code that makes this set of Control ID Extract rules unique.  """  
      self.ControlIDExtractDesc:str = obj["ControlIDExtractDesc"]
      """  Description of this set of Control ID Extract rules.  """  
      self.ExtractSequence:int = obj["ExtractSequence"]
      """  Identifies the sequence in which the Control ID Extract rules will be checked.  """  
      self.DataIdentifier:str = obj["DataIdentifier"]
      """  Identifies the character string match for the left side characters of the string defined with this set of Control ID Extract rules.  """  
      self.IsFixedLength:bool = obj["IsFixedLength"]
      """  Identifies if the string defined with this set of Control ID Extract rules is a fixed length.  """  
      self.DigitsInString:int = obj["DigitsInString"]
      """  Identifies the number of digits in the string defined with this set of Control ID Extract rules is a fixed length.  """  
      self.DataFormat:str = obj["DataFormat"]
      """  Identifies the Data Format for the Segments for this set of Control ID Extract rules.  """  
      self.GroupSeparatorCharacter:str = obj["GroupSeparatorCharacter"]
      """  Identifies the Group Separator Character for this set of Control ID Extract rules.  """  
      self.RecordSeparatorCharacter:str = obj["RecordSeparatorCharacter"]
      """  Identifies the Record Separator Character for this set of Control ID Extract rules.  """  
      self.EndOfTransmissionCharacter:str = obj["EndOfTransmissionCharacter"]
      """  Identifies the End of Transmission Character for this set of Control ID Extract rules.  """  
      self.ExtractComments:str = obj["ExtractComments"]
      """  Identifies additional information about this set of Control ID Extract rules.  """  
      self.Dimension:str = obj["Dimension"]
      """  Indicates if this set of Control ID Extract rules relates to a 1D, 2D or 3D barcode.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  Development use only.  """  
      self.DevCharacter02:str = obj["DevCharacter02"]
      """  Development use only.  """  
      self.DevInteger01:int = obj["DevInteger01"]
      """  Development use only.  """  
      self.DevInteger02:int = obj["DevInteger02"]
      """  Development use only.  """  
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  Development use only.  """  
      self.DevBoolean02:bool = obj["DevBoolean02"]
      """  Development use only.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.EndOfTransmissionASCII:int = obj["EndOfTransmissionASCII"]
      self.GroupSeparatorASCII:int = obj["GroupSeparatorASCII"]
      self.RecordSeparatorASCII:int = obj["RecordSeparatorASCII"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ControlIDExtractListTableset:
   def __init__(self, obj):
      self.ControlIDExtractHeaderList:list[Erp_Tablesets_ControlIDExtractHeaderListRow] = obj["ControlIDExtractHeaderList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ControlIDExtractPCIDRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DataIdentifierCode:str = obj["DataIdentifierCode"]
      """  Unique code assigned by the user for this data identifier.  """  
      self.DataIdentifierDesc:str = obj["DataIdentifierDesc"]
      """  Description of the data identifier.  """  
      self.DataIdentifier:str = obj["DataIdentifier"]
      """  Identifies the character string match for the left side characters of the Control ID.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the record is inactive or not. Default is false.  """  
      self.ExtractSequence:int = obj["ExtractSequence"]
      """  Identifies the order in which the Control ID Extract data identifiers will be checked against the Control ID.  """  
      self.DigitsToExtract:int = obj["DigitsToExtract"]
      """  Identifies the number of digits from the right end of the Control ID string to be extracted.  """  
      self.IsFixedLength:bool = obj["IsFixedLength"]
      """  Identifies if the Control ID string is a fixed length.  """  
      self.DigitsInString:int = obj["DigitsInString"]
      """  Identifies the number of digits in the Control ID string if it is a fixed length.  """  
      self.ExtractComments:str = obj["ExtractComments"]
      """  Identifies additional information about the Control ID Extract data identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ScanMinLength:int = obj["ScanMinLength"]
      """  Scan Minimum Length  """  
      self.ScanMaxLength:int = obj["ScanMaxLength"]
      """  Scan Maximum Length  """  
      self.Active:bool = obj["Active"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ControlIDExtractSegmentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ControlIDExtractCode:str = obj["ControlIDExtractCode"]
      """  Code that makes this set of Control ID Extract rules unique.  """  
      self.SegmentNum:int = obj["SegmentNum"]
      """  Segment Number that uniquely identifies this segment within the set of Control ID Extract rules.  """  
      self.SegmentType:str = obj["SegmentType"]
      """  Segment Type.  Valid Values are PCID and OTHER.  This will be expended in the future to handle other types.  """  
      self.DataIdentifier:str = obj["DataIdentifier"]
      """  Identifies the character string match for the left side characters of the string defined with this segment.  """  
      self.PCIDSegmentPosition:int = obj["PCIDSegmentPosition"]
      """  The position of this segment in the concatenated PCID value.  """  
      self.SegmentPosition:int = obj["SegmentPosition"]
      """  Segment Position in the string.  """  
      self.StartCharacterPosition:int = obj["StartCharacterPosition"]
      """  Position in the string of the start character of this segment.  """  
      self.EndCharacterPosition:int = obj["EndCharacterPosition"]
      """  Position in the string of the end character of this segment.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  Development use only.  """  
      self.DevCharacter02:str = obj["DevCharacter02"]
      """  Development use only.  """  
      self.DevInteger01:int = obj["DevInteger01"]
      """  Development use only.  """  
      self.DevInteger02:int = obj["DevInteger02"]
      """  Development use only.  """  
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  Development use only.  """  
      self.DevBoolean02:bool = obj["DevBoolean02"]
      """  Development use only.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ControlIDExtractTableset:
   def __init__(self, obj):
      self.ControlIDExtractHeader:list[Erp_Tablesets_ControlIDExtractHeaderRow] = obj["ControlIDExtractHeader"]
      self.ControlIDExtractSegment:list[Erp_Tablesets_ControlIDExtractSegmentRow] = obj["ControlIDExtractSegment"]
      self.ControlIDExtractPCID:list[Erp_Tablesets_ControlIDExtractPCIDRow] = obj["ControlIDExtractPCID"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtControlIDExtractTableset:
   def __init__(self, obj):
      self.ControlIDExtractHeader:list[Erp_Tablesets_ControlIDExtractHeaderRow] = obj["ControlIDExtractHeader"]
      self.ControlIDExtractSegment:list[Erp_Tablesets_ControlIDExtractSegmentRow] = obj["ControlIDExtractSegment"]
      self.ControlIDExtractPCID:list[Erp_Tablesets_ControlIDExtractPCIDRow] = obj["ControlIDExtractPCID"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   controlIDExtractCode
   """  
   def __init__(self, obj):
      self.controlIDExtractCode:str = obj["controlIDExtractCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ControlIDExtractTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ControlIDExtractTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ControlIDExtractTableset] = obj["returnObj"]
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

class GetControlIDExtractPCID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDExtractTableset] = obj["ds"]
      pass

class GetControlIDExtractPCID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ControlIDExtractTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDExtractTableset] = obj["ds"]
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
      self.returnObj:list[Erp_Tablesets_ControlIDExtractListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewControlIDExtractHeader_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDExtractTableset] = obj["ds"]
      pass

class GetNewControlIDExtractHeader_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDExtractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewControlIDExtractPCID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDExtractTableset] = obj["ds"]
      pass

class GetNewControlIDExtractPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDExtractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewControlIDExtractSegment_input:
   """ Required : 
   ds
   controlIDExtractCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDExtractTableset] = obj["ds"]
      self.controlIDExtractCode:str = obj["controlIDExtractCode"]
      pass

class GetNewControlIDExtractSegment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDExtractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseControlIDExtractHeader
   whereClauseControlIDExtractSegment
   whereClauseControlIDExtractPCID
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseControlIDExtractHeader:str = obj["whereClauseControlIDExtractHeader"]
      self.whereClauseControlIDExtractSegment:str = obj["whereClauseControlIDExtractSegment"]
      self.whereClauseControlIDExtractPCID:str = obj["whereClauseControlIDExtractPCID"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ControlIDExtractTableset] = obj["returnObj"]
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

class OnChangeDimension_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDExtractTableset] = obj["ds"]
      pass

class OnChangeDimension_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDExtractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeExtractPCIDIsFixedLength_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDExtractTableset] = obj["ds"]
      pass

class OnChangeExtractPCIDIsFixedLength_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDExtractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeIsFixedLength_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDExtractTableset] = obj["ds"]
      pass

class OnChangeIsFixedLength_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDExtractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeSegmentType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDExtractTableset] = obj["ds"]
      pass

class OnChangeSegmentType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDExtractTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtControlIDExtractTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtControlIDExtractTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDExtractTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ControlIDExtractTableset] = obj["ds"]
      pass

      """  output parameters  """  

